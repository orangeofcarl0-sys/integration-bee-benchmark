#!/usr/bin/env python3
"""Reference answer grader for the Integration Bee Benchmark.

Scores a solver's answers against the Base Set (base-set.json) or the Hard Set
(hard-set.json) while accepting
mathematically equivalent forms: different but equal closed forms, additive
constants for indefinite integrals, equivalent algebraic/trig rewrites, and
high-precision decimal approximations of exact constants.

Only dependency: sympy (mpmath ships with it).

Usage
-----
    python grade.py --answers answers.json                 # Base Set (default)
    python grade.py --set hard --answers answers.json      # Hard Set
    python grade.py --answers a.json --json out.json
    python grade.py --selftest                             # validate the selected set

Answer file format (JSON) -- a list, or an object with an "answers" key::

    [
      {"id": "B001", "answer_latex": "4048", "answer_sympy": "4048"},
      {"id": "B002", "answer": "x"}
    ]

"answer_sympy" (a sympy-parseable Python expression) is preferred when present;
"answer_latex" / "answer" are converted by the built-in LaTeX reader.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys

from sympy import (Abs, E, Float, I, N, Rational, acos, acosh, asin, asinh, atan, atanh,
                   ceiling, cos, cosh, cot, csc, diff, exp, floor, gamma, lambdify, log, oo, pi,
                   sec, simplify, sin, sinh, sqrt, symbols, tan, tanh, sympify)
from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application,
                                        parse_expr, standard_transformations)

x = symbols("x", real=True)
a = symbols("a", real=True)
b = symbols("b", real=True)
n = symbols("n", real=True)

LOCALS = dict(pi=pi, E=E, I=I, oo=oo, log=log, ln=log, sqrt=sqrt, sin=sin, cos=cos, tan=tan,
              cot=cot, sec=sec, csc=csc, sinh=sinh, cosh=cosh, tanh=tanh, atan=atan, asin=asin,
              acos=acos, atanh=atanh, asinh=asinh, acosh=acosh, exp=exp, Rational=Rational,
              Abs=Abs, floor=floor, ceiling=ceiling, gamma=gamma, x=x, a=a, b=b, n=n)
TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)

CONST_RTOL = 1e-9        # relative tolerance for constant (definite-integral) answers
DERIV_RTOL = 1e-6        # relative tolerance for numeric derivative comparison
SAMPLE_POINTS = (0.55, 0.7, 0.85, 1.2, 1.5, 1.9, 2.2)


# --------------------------------------------------------------------------- LaTeX reader

def _brace(s, i):
    assert s[i] == "{"
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
    raise ValueError("unbalanced braces")


def _paren(s, i):
    assert s[i] == "("
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "(":
            depth += 1
        elif s[j] == ")":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
    raise ValueError("unbalanced parentheses")


def _tok(s, i):
    m = re.match(r"[0-9]+(\.[0-9]+)?", s[i:])
    if m:
        return m.group(0), i + len(m.group(0))
    m = re.match(r"\\[a-zA-Z]+", s[i:])
    if m:
        return m.group(0), i + len(m.group(0))
    m = re.match(r"[a-zA-Z]+", s[i:])
    if m:
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def _commands(t):
    subs = [
        (r"\\operatorname\{([a-zA-Z]+)\}", r"\1"),
        (r"\\pi\b", " pi "), (r"\\infty\b", " oo "), (r"\\Gamma\b", " gamma "), (r"\\psi\b", " psi "),
        (r"(?<![A-Za-z_])arctanh(?![A-Za-z_])", "atanh"),
        (r"(?<![A-Za-z_])arcsinh(?![A-Za-z_])", "asinh"),
        (r"(?<![A-Za-z_])arccosh(?![A-Za-z_])", "acosh"),
        (r"(?<![A-Za-z_])sech(?![A-Za-z_])", "sech"),
        (r"(?<![A-Za-z_])csch(?![A-Za-z_])", "csch"),
        (r"(?<![A-Za-z_])coth(?![A-Za-z_])", "coth"),
        (r"\\arctanh\b", "atanh"), (r"\\arcsinh\b", "asinh"), (r"\\arccosh\b", "acosh"),
        (r"\\arctan\b", "atan"), (r"\\arcsin\b", "asin"), (r"\\arccos\b", "acos"),
        (r"\\sinh\b", "sinh"), (r"\\cosh\b", "cosh"), (r"\\tanh\b", "tanh"),
        (r"\\cot\b", "cot"), (r"\\sec\b", "sec"), (r"\\csc\b", "csc"),
        (r"\\sin\b", "sin"), (r"\\cos\b", "cos"), (r"\\tan\b", "tan"),
        (r"\\ln\b", "log"), (r"\\log\b", "log"), (r"\\exp\b", "exp"),
        (r"\\mathrm\{([^}]*)\}", r"\1"), (r"\\text\{([^}]*)\}", r"\1"),
    ]
    for pat, rep in subs:
        t = re.sub(pat, rep, t)
    return t


def latex_to_sympy(t):
    """Translate a (small but practical) LaTeX subset into a sympy-parseable string."""
    t = t.strip().replace("$", "")
    t = re.sub(r"\\(left|right|big|Big|bigg|Bigg|displaystyle|limits|quad|qquad)", "", t)
    t = t.replace("\\tfrac", "\\frac").replace("\\dfrac", "\\frac")
    t = t.replace("\\!", "").replace("\\,", "*").replace("\\;", "*").replace("\\ ", "*")
    t = t.replace("\\cdot", "*").replace("\\times", "*")
    t = t.replace("\\zeta", "zeta")
    t = re.sub(r"(\d+)\s*!", r"factorial(\1)", t)
    t = re.sub(r"\+\s*C\s*$", "", t).strip()
    t = re.sub(r"\\lfloor\s*(.*?)\s*\\rfloor", r"floor(\1)", t)
    t = re.sub(r"\\lceil\s*(.*?)\s*\\rceil", r"ceiling(\1)", t)
    # inverse function notation: \sin^{-1}(u) and \tan^{-1}3
    for f, inv in (("sin", "asin"), ("cos", "acos"), ("tan", "atan"),
                   ("sinh", "asinh"), ("cosh", "acosh"), ("tanh", "atanh")):
        t = re.sub(r"\\" + f + r"\^\{-1\}\s*([0-9a-zA-Z]+)", inv + r"(\1)", t)
        t = re.sub(r"\\" + f + r"\^\{-1\}", inv, t)
    # function powers: \tan^{n}(arg) -> (\tan(arg))**n
    pat = re.compile(r"\\(tan|sin|cos|cot|sec|csc|sinh|cosh|tanh)\^\{([^{}]*)\}\(")
    while True:
        m = pat.search(t)
        if not m:
            break
        arg, end = _paren(t, m.end() - 1)
        t = t[:m.start()] + "(\\" + m.group(1) + "(" + arg + "))**(" + m.group(2) + ")" + t[end:]
    # \cos^x(arg) -> (\cos(arg))**x
    pat2 = re.compile(r"\\(tan|sin|cos)\^([a-zA-Z])\(")
    while True:
        m = pat2.search(t)
        if not m:
            break
        arg, end = _paren(t, m.end() - 1)
        t = t[:m.start()] + "(\\" + m.group(1) + "(" + arg + "))**" + m.group(2) + t[end:]

    def arg(s, i):
        while i < len(s) and s[i] in " \t":
            i += 1
        if i < len(s) and s[i] == "{":
            return _brace(s, i)
        if i < len(s) and s[i] == "\\":
            m = re.match(r"\\[a-zA-Z]+", s[i:])
            if m:
                return m.group(0), i + len(m.group(0))
        return s[i], i + 1

    while "\\frac" in t:                      # \frac{a}{b}, \frac12, \frac\pi2
        k = t.find("\\frac")
        num, i = arg(t, k + 5)
        den, i = arg(t, i)
        t = t[:k] + "((" + num + ")/(" + den + "))" + t[i:]
    while True:                               # \sqrt[n]{a}, \sqrt{a}, \sqrt3
        k = t.find("\\sqrt")
        if k < 0:
            break
        i = k + 5
        deg = None
        if i < len(t) and t[i] == "[":
            j = t.index("]", i)
            deg, i = t[i + 1:j], j + 1
        while i < len(t) and t[i] in " \t":
            i += 1
        if i < len(t) and t[i] == "{":
            body, i = _brace(t, i)
        else:
            body, i = _tok(t, i)
        t = t[:k] + ("((" + body + ")**(1/(" + deg + ")))" if deg else "sqrt(" + body + ")") + t[i:]
    while "^" in t:                           # ^{...} and ^x
        k = t.index("^")
        i = k + 1
        while i < len(t) and t[i] in " \t":
            i += 1
        if i < len(t) and t[i] == "{":
            body, i = _brace(t, i)
        else:
            body, i = _tok(t, i)
        t = t[:k] + "**(" + body + ")" + t[i:]
    t = re.sub(r"\|([^|]*)\|", r"(Abs(\1))", t)   # |u| -> Abs(u)
    t = _commands(t)
    t = t.replace("\\{", "(").replace("\\}", ")").replace("{", "(").replace("}", ")")
    # Euler's number: e^x, e**, bare e, "ex", "2e-4"
    t = re.sub(r"(?<=[0-9\)])\s*\*?\s*e\*\*", "*E**", t)
    t = t.replace("e**", "E**")
    t = re.sub(r"(?<![A-Za-z_])e(?=(log|exp|sin|cos|tan|atan|asin|acos|sqrt|pi)\b)", "E*", t)
    t = re.sub(r"(?<![A-Za-z_])e(?=x(?![A-Za-z]))", "E*", t)
    t = re.sub(r"(\d)\s*e(?![A-Za-z0-9_])", r"\1*E", t)
    t = re.sub(r"(?<![A-Za-z_])e(?![A-Za-z0-9_])", "E", t)
    return re.sub(r"\s+", " ", t).strip()


def parse_latex_answer(text):
    """Return candidate sympy expressions for one answer string (splits on '=')."""
    out = []
    for part in re.split(r"(?<![<>!=])=(?![=])", str(text)):
        part = part.strip().rstrip(".").strip()
        if not part:
            continue
        try:
            conv = latex_to_sympy(part)
            out.append(parse_expr(conv, local_dict=LOCALS, transformations=TRANSFORMS))
        except Exception:
            try:
                out.append(sympify(latex_to_sympy(part), locals=LOCALS))
            except Exception:
                continue
    return out


# --------------------------------------------------------------------------- equivalence

def _numeric_derivatives_match(expr_a, expr_b, free):
    import mpmath as mp
    mp.mp.dps = 30
    syms = [v for v in free if v.is_Symbol]
    if len(syms) != 1:
        return False
    v = syms[0]
    try:
        fa, fb = lambdify(v, expr_a, "mpmath"), lambdify(v, expr_b, "mpmath")
    except Exception:
        return False
    hits = 0
    for x0 in SAMPLE_POINTS:
        try:
            da, db = mp.diff(fa, mp.mpf(x0), 1), mp.diff(fb, mp.mpf(x0), 1)
        except Exception:
            continue
        if abs(da) > 1e12 or abs(db) > 1e12:
            continue
        if abs(complex(da) - complex(db)) > DERIV_RTOL * max(1.0, abs(complex(da)), abs(complex(db))):
            return False
        hits += 1
    return hits >= 4


def equivalent(expr, official):
    """True when expr answers official (up to an additive constant for antiderivatives)."""
    free = expr.free_symbols | official.free_symbols
    if not free:                                    # constant (definite integral)
        try:
            va, vb = N(expr, 40), N(official, 40)
            if abs(va - vb) <= CONST_RTOL * max(sympify(1), abs(va), abs(vb)):
                return True, "numeric-const"
        except Exception:
            pass
        return False, "const-mismatch"
    for label, cand in (("simplify", None), ("rewrite-log", "log")):
        try:
            d = simplify(expr - official) if cand is None else simplify((expr - official).rewrite(cand))
            if d == 0:
                return True, label
            if not d.free_symbols:                  # antiderivatives may differ by a constant
                return True, "const-offset"
        except Exception:
            pass
    try:
        d = diff(expr, x) - diff(official, x)
        if simplify(d) == 0 or simplify(d.rewrite("log")) == 0:
            return True, "derivative"
    except Exception:
        pass
    if _numeric_derivatives_match(expr, official, free):
        return True, "numeric-derivative"
    random.seed(11)
    hits = 0
    for _ in range(20):
        subs = {v: Float(round(random.uniform(0.45, 2.2), 6)) for v in free}
        try:
            va, vb = complex(expr.subs(subs).evalf(35)), complex(official.subs(subs).evalf(35))
        except Exception:
            continue
        if any(z != z or abs(z) == float("inf") for z in (va, vb)):
            continue
        if abs(va - vb) > 1e-9 * max(1.0, abs(va), abs(vb)):
            return False, "numeric-sampled"
        hits += 1
    if hits >= 5:
        return True, "numeric-sampled"
    return False, "no-match"


def parse_model_answer(entry):
    """Parse one answer entry ({answer_sympy|answer_latex|answer}) into a sympy expression."""
    for key in ("answer_sympy", "answer_latex", "answer"):
        raw = entry.get(key)
        if not raw:
            continue
        text = str(raw).strip().strip("$")
        if key == "answer_sympy":
            try:
                return parse_expr(text, local_dict=LOCALS, transformations=TRANSFORMS), key
            except Exception:
                pass
        cands = parse_latex_answer(text)
        if cands:
            return cands[0], key
    return None, None


# --------------------------------------------------------------------------- driver

def load_benchmark(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return {p["id"]: p for p in data["problems"]}


def load_answers(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    rows = data if isinstance(data, list) else data.get("answers", [])
    return {row["id"]: row for row in rows}


def grade(benchmark_path, answers_path):
    bench = load_benchmark(benchmark_path)
    answers = load_answers(answers_path)
    results, correct = [], 0
    for pid in sorted(bench):
        entry = answers.get(pid)
        if entry is None:
            results.append({"id": pid, "status": "missing"})
            continue
        official = parse_latex_answer(bench[pid]["answer"])
        if not official:
            results.append({"id": pid, "status": "official-unparseable",
                            "official": bench[pid]["answer"]})
            continue
        expr, source = parse_model_answer(entry)
        if expr is None:
            results.append({"id": pid, "status": "unparseable", "entry": entry})
            continue
        ok, how = False, "no-match"
        for cand in official:
            ok, how = equivalent(expr, cand)
            if ok:
                break
        correct += int(ok)
        results.append({"id": pid, "status": "pass" if ok else "fail", "method": how,
                        "model_answer": entry.get("answer_sympy") or entry.get("answer_latex")
                        or entry.get("answer")})
    return correct, len(bench), results


def selftest(benchmark_path):
    bench = load_benchmark(benchmark_path)
    parsed = 0
    bad = []
    for pid, item in sorted(bench.items()):
        cands = parse_latex_answer(item["answer"])
        if not cands:
            bad.append((pid, item["answer"]))
            continue
        parsed += 1
        ok, _ = equivalent(cands[0], cands[0])
        if not ok:
            bad.append((pid, item["answer"] + "  [self-match failed]"))
    ctrl_id = sorted(bench)[0]
    wrong_ok, _ = equivalent(sympify("0"), parse_latex_answer(bench[ctrl_id]["answer"])[0])
    print("set: %s | official answers parsed: %d/%d" % (os.path.basename(benchmark_path), parsed, len(bench)))
    if bad:
        print("unparsed / self-match failures:")
        for pid, raw in bad:
            print("  %s  %s" % (pid, raw[:120]))
    print("negative control (%s answered 0): %s" % (ctrl_id, "FAILED (bad)" if wrong_ok else "rejected (good)"))
    return 0 if not bad and not wrong_ok else 1


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Grade answers against the Integration Bee Benchmark.")
    ap.add_argument("--set", dest="set_name", choices=["base", "hard"], default="base",
                    help="which set to grade against (default: base)")
    ap.add_argument("--benchmark", default=None,
                    help="explicit path to a set JSON (overrides --set)")
    ap.add_argument("--answers")
    ap.add_argument("--json", dest="json_out")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.benchmark is None:
        args.benchmark = os.path.join(here, "base-set.json" if args.set_name == "base" else "hard-set.json")

    if args.selftest:
        return selftest(args.benchmark)
    if not args.answers:
        ap.error("--answers is required unless --selftest is given")

    correct, total, results = grade(args.benchmark, args.answers)
    width = max(len(r["id"]) for r in results)
    for r in results:
        mark = {"pass": "PASS", "fail": "FAIL"}.get(r["status"], r["status"].upper())
        print("%-*s  %-5s  %-16s  %s" % (width, r["id"], mark, r.get("method", ""),
                                         (r.get("model_answer") or "")[:70]))
    print("\nscore: %d/%d" % (correct, total))
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({"correct": correct, "total": total, "results": results}, fh,
                      ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
