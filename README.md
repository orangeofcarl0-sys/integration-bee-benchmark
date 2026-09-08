# Integration Bee Benchmark

**100 integration problems from real integration bees — each paired with the competition's own official answer.**

A small, carefully screened benchmark for evaluating mathematical integration: by language models, computer algebra systems, or humans. Every answer comes from the organizers' **official answer key / mark scheme** — never from third-party solutions, and never re-derived by the curator. Every statement was transcribed from the official paper in LaTeX and visually verified against a rendered page of the source PDF.

## Contents

| File | Description |
|---|---|
| [`INTEGRATION-BEE-BENCHMARK.md`](INTEGRATION-BEE-BENCHMARK.md) | The dataset, human-readable (LaTeX in Markdown) |
| [`benchmark.json`](benchmark.json) | The dataset, machine-readable |
| [`ATTRIBUTION.md`](ATTRIBUTION.md) | Source-by-source copyright and attribution |
| [`LICENSE`](LICENSE) | CC BY 4.0 — **applies to the curator's contributions only** (see [Copyright](#copyright-and-licensing)) |

## Composition

| Source | Problems | Official answer key |
|---|---|---|
| MIT Integration Bee 2024 Qualifying Exam | 19 | MIT Integration Bee official answers |
| MIT Integration Bee 2025 Qualifying Exam | 20 | MIT Integration Bee official answers |
| MIT Integration Bee 2023 Qualifying Exam | 17 | MIT Integration Bee official answers |
| UK University Integration Bee 2025/26 Round 1 (Online) | 30 | UKUIB Round One Mark Scheme |
| University of Florida Integration Bee 2025 Written Exam | 14 | UMS official solutions |
| **Total** | **100** | |

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
| UKUIB 2025/26 Round 1 | *Online Round*, UK University Integration Bee | *Round One Mark Scheme* |
| Florida 2025 | *Integration Bee 2025 Written Exam* | *2025 Written Exam solutions* |

The full archive from which this benchmark was curated is maintained privately; each item's source
is recorded in its `source` field.
