#!/usr/bin/env python3
"""DSH session usage/cost meter  --  DSH-SPECIFIC.

This tool is specific to DeepSeek Harness (DSH). It reads DSH session logs

    <dsh-home>/sessions/<cwd-slug>/<session-id>/session.v3.jsonl.zstd

sums the token usage recorded on assistant messages, and prices every LLM call
by its own timestamp against a configurable rate table.

It is included in this repository only because the Integration Bee Benchmark was
evaluated through DSH and this is how the run's tokens / wall-clock time / cost
were reported (see the benchmark run notes). It has no dependency on the
benchmark data itself; the grader (grade.py) is the dataset-facing tool.

Usage
-----
    python usage.py <session-file-or-dir> [...]        # per-session report + total
    python usage.py --dsh-home ~/.dsh --session <id>
    python usage.py --rates rates.json --json session.v3.jsonl.zstd
    python usage.py --selftest                          # parser smoke test

A session argument may be:
  * a path to a session.v3.jsonl.zstd file (plain .jsonl is also accepted);
  * a path to a session directory containing it;
  * a session id, searched under <dsh-home>/sessions/*/<id>/.

Rate table (default: DeepSeek V4 Flash, USD per million tokens; the model used
for the run was billed at these rates). Peak/off-peak schedule follows the
official DeepSeek pricing effective 2026-08-17 00:00 +08:00, peak hours 9-12 and
14-18 local time. Override everything with --rates (see DEFAULT_RATES below).
"""
from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys

DEFAULT_RATES = {
    "currency": "USD",
    "usd_cny": 7.2,
    "timezone_offset_hours": 8,
    "effective_at": "2026-08-17T00:00:00+08:00",
    "peak_hours": [[9, 12], [14, 18]],
    "base":    {"input": 0.14, "output": 0.28, "cache_read": 0.0028, "cache_write": 0.0},
    "peak":    {"input": 0.44, "output": 1.32, "cache_read": 0.014,  "cache_write": 0.0},
    "offpeak": {"input": 0.22, "output": 0.66, "cache_read": 0.007,  "cache_write": 0.0},
}


# --------------------------------------------------------------------------- IO

def read_session_bytes(path):
    """Return the decompressed text of a DSH session log."""
    if path.endswith(".zstd"):
        try:
            import zstandard  # optional
            with open(path, "rb") as fh:
                dctx = zstandard.ZstdDecompressor()
                return dctx.stream_reader(fh).read().decode("utf-8", "replace")
        except ImportError:
            pass
        zstd = shutil.which("zstd")
        if zstd is None:
            raise SystemExit("need the 'zstandard' Python package or the 'zstd' CLI to read %s" % path)
        out = subprocess.run([zstd, "-d", "-c", path], capture_output=True, timeout=300)
        if out.returncode != 0:
            raise SystemExit("zstd failed on %s: %s" % (path, out.stderr[:200]))
        return out.stdout.decode("utf-8", "replace")
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def resolve_session(arg, dsh_home):
    """Resolve one session argument to a log file path."""
    if os.path.isdir(arg):
        for name in ("session.v3.jsonl.zstd", "session.v3.jsonl"):
            cand = os.path.join(arg, name)
            if os.path.exists(cand):
                return cand
        raise SystemExit("no session log inside directory %s" % arg)
    if os.path.isfile(arg):
        return arg
    matches = glob.glob(os.path.join(dsh_home, "sessions", "*", arg, "session.v3.jsonl.zstd"))
    if not matches:
        matches = glob.glob(os.path.join(dsh_home, "sessions", "*", arg, "session.v3.jsonl"))
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        raise SystemExit("session id %s is ambiguous: %s" % (arg, ", ".join(matches)))
    raise SystemExit("cannot find session %s (looked for a file, a directory, or under %s/sessions/*/)" % (arg, dsh_home))


# --------------------------------------------------------------------------- pricing

def rate_tier(timestamp_ms, rates):
    """Return the rate tier name for one call timestamp."""
    tz = datetime.timezone(datetime.timedelta(hours=rates.get("timezone_offset_hours", 8)))
    when = datetime.datetime.fromtimestamp(timestamp_ms / 1000, tz=datetime.timezone.utc).astimezone(tz)
    effective = rates.get("effective_at")
    if effective:
        eff = datetime.datetime.fromisoformat(effective)
        if when < eff:
            return "base"
    hour = when.hour
    for start, end in rates.get("peak_hours", []):
        if start <= hour < end:
            return "peak"
    return "offpeak"


def price(usage, tier, rates):
    r = rates.get(tier, rates["base"])
    return (usage.get("inputTokens", 0) * r["input"]
            + usage.get("outputTokens", 0) * r["output"]
            + usage.get("cacheReadTokens", 0) * r["cache_read"]
            + usage.get("cacheWriteTokens", 0) * r.get("cache_write", 0.0)) / 1e6


# --------------------------------------------------------------------------- parsing

def parse_session(text, rates):
    """Fold a DSH session log into usage/time/cost totals."""
    totals = {"calls": 0, "input": 0, "output": 0, "cache_read": 0, "cache_write": 0, "reasoning": 0}
    tiers = {}
    cost = 0.0
    first = last = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except ValueError:
            continue
        ts = event.get("time")
        if isinstance(ts, (int, float)):
            first = ts if first is None else min(first, ts)
            last = ts if last is None else max(last, ts)
        if event.get("type") != "assistant/message":
            continue
        usage = (event.get("data") or {}).get("usage") or event.get("usage")
        if not usage:
            continue
        totals["calls"] += 1
        tier = rate_tier(ts if isinstance(ts, (int, float)) else (last or 0), rates)
        tiers[tier] = tiers.get(tier, 0) + 1
        for key, field in (("input", "inputTokens"), ("output", "outputTokens"),
                           ("cache_read", "cacheReadTokens"), ("cache_write", "cacheWriteTokens"),
                           ("reasoning", "reasoningTokens")):
            totals[key] += int(usage.get(field, 0) or 0)
        cost += price(usage, tier, rates)
    totals.update({
        "tiers": tiers,
        "cost_usd": round(cost, 6),
        "cost_cny": round(cost * rates.get("usd_cny", 7.2), 6),
        "start_utc": datetime.datetime.fromtimestamp(first / 1000, tz=datetime.timezone.utc).isoformat() if first else None,
        "end_utc": datetime.datetime.fromtimestamp(last / 1000, tz=datetime.timezone.utc).isoformat() if last else None,
        "duration_s": round((last - first) / 1000, 1) if first and last else 0.0,
        "total_tokens": totals["input"] + totals["output"] + totals["cache_read"] + totals["cache_write"],
    })
    return totals


def selftest():
    """Parse a synthetic DSH log and check the arithmetic."""
    sample = "\n".join([
        json.dumps({"type": "session", "time": 1788948719000}),
        json.dumps({"type": "assistant/message", "time": 1788948720000,
                    "data": {"usage": {"inputTokens": 1000, "outputTokens": 2000,
                                       "cacheReadTokens": 5000, "reasoningTokens": 1500}}}),
        json.dumps({"type": "assistant/message", "time": 1788948725000,
                    "data": {"usage": {"inputTokens": 500, "outputTokens": 1000,
                                       "cacheReadTokens": 2500}}}),
    ])
    got = parse_session(sample, DEFAULT_RATES)
    want_tokens = 1000 + 500 + 2000 + 1000 + 5000 + 2500
    ok = (got["calls"] == 2 and got["total_tokens"] == want_tokens
          and got["reasoning"] == 1500 and got["cost_usd"] > 0)
    print("selftest: calls=%d total_tokens=%d cost_usd=%.6f -> %s"
          % (got["calls"], got["total_tokens"], got["cost_usd"], "OK" if ok else "FAILED"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="DSH session usage/cost meter (DSH-specific).")
    ap.add_argument("sessions", nargs="*", help="session file, session directory, or session id")
    ap.add_argument("--dsh-home", default=os.environ.get("DSH_HOME") or os.path.join(os.path.expanduser("~"), ".dsh"))
    ap.add_argument("--session", action="append", default=[], help="session id to resolve under --dsh-home")
    ap.add_argument("--rates", help="JSON rate table overriding the built-in DeepSeek V4 Flash schedule")
    ap.add_argument("--json", dest="json_out", help="write the report as JSON")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    rates = json.loads(json.dumps(DEFAULT_RATES))
    if args.rates:
        with open(args.rates, encoding="utf-8") as fh:
            override = json.load(fh)
        for key, value in override.items():
            rates[key] = value

    args.sessions += args.session
    if not args.sessions:
        ap.error("give at least one session file/dir/id, or --selftest")

    report = []
    grand = {"calls": 0, "input": 0, "output": 0, "cache_read": 0, "cache_write": 0,
             "reasoning": 0, "cost_usd": 0.0, "duration_s": 0.0}
    for arg in args.sessions:
        path = resolve_session(arg, args.dsh_home)
        got = parse_session(read_session_bytes(path), rates)
        got["session"] = os.path.basename(os.path.dirname(path))
        got["file"] = path
        report.append(got)
        for key in ("calls", "input", "output", "cache_read", "cache_write", "reasoning", "duration_s"):
            grand[key] += got[key]
        grand["cost_usd"] += got["cost_usd"]

    for got in report:
        print("%-38s calls=%-3d in=%-8d out=%-8d cache_read=%-9d %6.1fs  $%.6f  %s"
              % (got["session"], got["calls"], got["input"], got["output"], got["cache_read"],
                 got["duration_s"], got["cost_usd"], got["tiers"]))
    grand["total_tokens"] = grand["input"] + grand["output"] + grand["cache_read"] + grand["cache_write"]
    grand["cost_cny"] = round(grand["cost_usd"] * rates.get("usd_cny", 7.2), 6)
    grand["cost_usd"] = round(grand["cost_usd"], 6)
    print("%-38s calls=%-3d in=%-8d out=%-8d cache_read=%-9d %6.1fs  $%.6f  (%.4f CNY)"
          % ("TOTAL", grand["calls"], grand["input"], grand["output"], grand["cache_read"],
             grand["duration_s"], grand["cost_usd"], grand["cost_cny"]))
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({"sessions": report, "total": grand, "rates": rates}, fh, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
