# Integration Bee Benchmark

**100 curated integration problems from real integration bees — plus a 25-problem Hard Set from the MIT Finals — each paired with the competition's own official answer.**

A small, carefully screened benchmark for evaluating mathematical integration: by language models, computer algebra systems, or humans. Every answer comes from the organizers' **official answer key / mark scheme** — never from third-party solutions, and never re-derived by the curator. Every statement was transcribed from the official paper in LaTeX and visually verified against a rendered page of the source PDF.

## Contents

| File | Description |
|---|---|
| [`INTEGRATION-BEE-BENCHMARK.md`](INTEGRATION-BEE-BENCHMARK.md) | Core set, human-readable (LaTeX in Markdown) |
| [`benchmark.json`](benchmark.json) | Core set, machine-readable |
| [`HARD-SET.md`](HARD-SET.md) | Hard Set (MIT Finals 2022–2026), human-readable |
| [`hard-set.json`](hard-set.json) | Hard Set, machine-readable |
| [`ATTRIBUTION.md`](ATTRIBUTION.md) | Source-by-source copyright and attribution |
| [`grade.py`](grade.py) | Reference grader — scores answers with LaTeX/sympy equivalence checking |
| [`usage.py`](usage.py) | DSH session usage/cost meter (tooling used to report the benchmark run) |
| [`LICENSE`](LICENSE) | CC BY 4.0 — **applies to the curator's contributions only** (see [Copyright](#copyright-and-licensing)) |

## Difficulty tiers

| Tier | Problems | Rounds | File |
|---|---|---|---|
| **Core** | 100 | Qualifying / online / written rounds (entry-level speed rounds) | `benchmark.json` |
| **Hard** | 25 | MIT Integration Bee **Finals** 2022–2026 (4–5 min per problem) | `hard-set.json` |

The two tiers share the same schema and grading rules; `id`s are `B###` (core) and `H###` (hard).
Run them separately or concatenate the `problems` arrays.

## Composition — Core (100)

| Source | Problems | Official answer key |
|---|---|---|
| MIT Integration Bee 2024 Qualifying Exam | 19 | MIT Integration Bee official answers |
| MIT Integration Bee 2025 Qualifying Exam | 20 | MIT Integration Bee official answers |
| MIT Integration Bee 2023 Qualifying Exam | 17 | MIT Integration Bee official answers |
| UK University Integration Bee 2025/26 Round 1 (Online) | 30 | UKUIB Round One Mark Scheme |
| University of Florida Integration Bee 2025 Written Exam | 14 | UMS official solutions |
| **Total** | **100** | |

## Composition — Hard Set (25)

| Source | Problems | Official answer key |
|---|---|---|
| MIT Integration Bee Finals 2022 | 5 | MIT Finals papers (problem / problem-with-answer) |
| MIT Integration Bee Finals 2023 | 5 | idem |
| MIT Integration Bee Finals 2024 | 5 | idem |
| MIT Integration Bee Finals 2025 | 5 | idem |
| MIT Integration Bee Finals 2026 | 5 | idem |
| **Total** | **25** | |

All items are closed-form problems. Indefinite integrals omit `+C`; `log` is the natural logarithm
(as specified by all four sources). `⌊·⌋` floor, `⌈·⌉` ceiling, `{·}` fractional part, `φ = (1+√5)/2`.

## Verification tags

Each problem carries a `verify` tag:

| Tag | Meaning |
|---|---|
| `N` | **Numerically verified** — the official answer was reproduced by high-precision quadrature / derivative sampling (mpmath, 30–40 decimal digits). |
| `A` | **Analytically verified** — the answer was checked by hand during curation (substitution, telescoping, symmetry, differentiation, known identity). |
| `O` | **Official key only** — trusted as printed, not independently re-checked. |

## JSON schema

```json
{
  "id": "B001",
  "source": "MIT 2024 Q1",
  "verify": "A",
  "problem": "\\int_{2023}^{2025} 2024\\,dx",
  "answer": "4048"
}
```

Top-level fields: `name`, `version`, `date`, `count`, `problems[]`.
Each problem: `id` (stable identifier), `source` (competition, year, problem number),
`verify` (tag above), `problem` (LaTeX), `answer` (LaTeX, from the official key).

## Quick start

```python
import json

with open("benchmark.json", encoding="utf-8") as f:
    data = json.load(f)

print(data["count"], "problems")
for p in data["problems"][:3]:
    print(p["id"], p["source"], "|", p["problem"], "->", p["answer"])
```

## Grading

[`grade.py`](grade.py) is a reference grader: it checks a solver's answers against `benchmark.json`
while accepting **mathematically equivalent forms** — different but equal closed forms, additive
constants for indefinite integrals (the `+C` convention), equivalent algebraic/trig rewrites, and
high-precision decimal approximations of exact constants. Only dependency: `sympy`.

```bash
pip install sympy
python grade.py --answers answers.json          # per-item PASS/FAIL table + score
python grade.py --answers answers.json --json results.json
python grade.py --selftest                      # validates the reader against the official key
```

Answer file format — a JSON list (or an object with an `answers` key):

```json
[
  {"id": "B001", "answer_latex": "4048", "answer_sympy": "4048"},
  {"id": "B002", "answer": "x"}
]
```

`answer_sympy` (a sympy-parseable Python expression) is preferred when present; `answer_latex` /
`answer` are converted by the built-in LaTeX reader.

Notes and limits:

- The LaTeX reader covers the notation used in this dataset: fractions with or without braces
  (`\frac{a}{b}`, `\frac12`), roots (`\sqrt3`, `\sqrt[3]{4}`), function powers (`\tan^{2023}(x)`),
  inverse-function notation (`\sin^{-1}`), absolute values, floor/ceiling, `\operatorname{...}`,
  Euler's number (`e`, `ex`, `2e-4`), and multi-part answers split on `=`.
  `python grade.py --selftest` parses **100/100** official answers and rejects a deliberately
  wrong answer.
- Equivalence is up to an additive constant for indefinite integrals, and within `1e-9` relative
  tolerance for numeric answers to definite integrals — a high-precision decimal counts, an
  approximate-but-wrong value does not.
- The grader is a convenience, not a proof assistant. For disputed items, settle them by
  differentiation or high-precision quadrature (issues #1–#4 show the kind of check that does).

## Metering (DSH-specific, optional)

[`usage.py`](usage.py) is **not part of the benchmark**. It is a small helper for **DeepSeek Harness
(DSH)** sessions: it reads DSH session logs, sums the token usage recorded on assistant messages, and
prices every LLM call by its own timestamp against a configurable rate table (default: DeepSeek V4
Flash peak/off-peak schedule). It is included only because the benchmark evaluation runs in this
repository's history were metered with it; it has no dependency on the dataset.

```bash
python usage.py <session-file-or-dir-or-id> [...]   # per-session report + total
python usage.py --selftest                          # parser smoke test
```

A session argument may be a path to a `session.v3.jsonl.zstd` file, a session directory, or a session
id (resolved under `--dsh-home`, default `$DSH_HOME` or `~/.dsh`). Override the built-in rates with
`--rates rates.json`.

## Selection & screening

1. **Definite official answer** — answers are taken only from official answer keys.
2. **Clean statement** — any item whose printed statement could not be read unambiguously at high
   resolution was dropped.
3. **Consistency screening** — each candidate was checked for consistency between the printed
   statement and the official answer (numerical quadrature, derivative checks, or analytic
   reasoning). Items that failed to reproduce were **excluded and documented**, not silently fixed.

### Documented exclusions

- **MIT 2024 #18** — as printed, `∫₀¹ Σ_{n=0}^{2024} x^{2n−1012} dx` diverges at 0; the official key
  states `2025/2`, which could not be reproduced (apparent typo in the official paper).
- **MIT 2023 #18** — the official antiderivative differentiates to **2×** the integrand.
- **CMIMC 2025 (entire packet)** — the official problems + solutions files carry a wrong year header,
  one item's printed bound contradicts its own answer, and several items could not be reproduced
  from the printed statements; the packet was excluded as a whole rather than cherry-picked.

## Changelog

### v1.1 — 2026-09-09
Added the **Hard Set**: all 25 MIT Integration Bee Finals problems 2022–2026 with official answers
(`HARD-SET.md`, `hard-set.json`). Motivation: the core set draws only on entry-round material and
had no knockout-round problems at all, which capped its difficulty. Every Hard Set item was verified
(definite integrals by 35-digit quadrature; indefinite by differentiating the official antiderivative;
floor/limit problems by exact combinatorial arguments — e.g. H015 is exactly `4/11` by a dyadic
first-occurrence computation). The MIT Finals papers print each problem twice (alone, then with its
answer), so the answers are the organizers' own.

### v1.0.1 — 2026-09-09
Community review (issues #1–#4) found four transcription/metadata defects; all fixed and verified:

- **B031** (MIT 2025 Q12): the LaTeX used integer radical indices (`\sqrt[3]{…}`), but the paper
  prints **fractional** indices 3/1, 4/2, 5/3, 6/4, … (verified at 600 dpi). The LaTeX now shows them
  explicitly; with fractional indices the reciprocal products telescope to 1, so the integrand is `x`
  and the official answer `x²/2` is correct (closed form: `R(x) = x^{1−2/(N+2)} → x`).
- **B080** (UKUIB 2025 R1 #24): the numerator was missing two denominators — it reads
  `x² + 2^{−x/6}/7 − 2^{−x/7}/6`, not `x² + 2^{−x/7} − 2^{−x/6}`. With the corrected statement the
  official answer `0` is reproduced (−1.0e−37 by 40-digit quadrature).
- **B083** (UKUIB 2025 R1 #27): the answer's first term is `(√3−1)^x`, not `(√3−1)x`
  (verified by differentiation; equivalent to `[a^x − ln(1+a^x)]/ln a`, `a = √3−1`).
- **B084**: `benchmark.json` now carries the `mrt(f)` definition inline (it was only in the Markdown).

Thanks to the reviewer who filed the issues.

## Copyright and licensing

**Problem statements and official answers are not ours to license.** They remain the property of
their respective organizers:

- MIT Integration Bee problems © the MIT Integration Bee / MIT.
- UK University Integration Bee problems © the UK University Integration Bee committee.
- University of Florida Integration Bee problems © the University of Florida Mathematics Society (UMS).

They are reproduced here **solely for non-commercial research and educational evaluation**, with
attribution to each source (see [`ATTRIBUTION.md`](ATTRIBUTION.md)). They are **not** covered by this
repository's CC BY 4.0 license. If you are a rights holder and would like your problems removed or
amended, please open an issue — we will act promptly (see *Takedown policy* below).

**What this repository does license (CC BY 4.0):** the curator's own contributions — the selection
of problems, their LaTeX transcription, the transcription of the official answers, the verification
tags, and the JSON schema/structure. See [`LICENSE`](LICENSE).

This repository is **not affiliated with, sponsored by, or endorsed by** any competition listed above.

## Takedown policy

Rights holders can request removal of any item at any time by opening an issue (or contacting the
maintainer). We will remove or replace the affected items promptly and note the change in the
repository history. Corrections to transcriptions are equally welcome.

## Citation

If you use this benchmark, please cite it (and the underlying competitions where appropriate):

```bibtex
@misc{integrationbeebenchmark2026,
  title        = {Integration Bee Benchmark: 100 curated integration problems with official answers},
  author       = {Integration Bee Benchmark contributors},
  year         = {2026},
  howpublished = {\url{https://github.com/orangeofcarl0-sys/integration-bee-benchmark}},
  note         = {Problem statements and answers remain \copyright{} their respective competition organizers}
}
```

## Provenance

Statements and answers were transcribed from the official papers:

| Source | Problem paper | Answer key |
|---|---|---|
| MIT 2023 / 2024 / 2025 | MIT Integration Bee Qualifying Exams | MIT Integration Bee official answer sheets |
| MIT 2022–2026 (Hard Set) | MIT Integration Bee Finals papers | printed in the same Finals papers (problem / problem-with-answer) |
| UKUIB 2025/26 Round 1 | *Online Round*, UK University Integration Bee | *Round One Mark Scheme* |
| Florida 2025 | *Integration Bee 2025 Written Exam* | *2025 Written Exam solutions* |

The full archive from which this benchmark was curated is maintained privately; each item's source
is recorded in its `source` field.
