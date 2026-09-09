# Integration Bee Benchmark — Base Set (100 problems with official answers)

**Base Set · v1.0.1 · 2026-09-09 · from the Integration-Bee-Archive**

A 100-problem benchmark of integration-bee integrals whose **answers come from the competitions'
own official answer keys**, with statements transcribed in LaTeX from the original papers (each
statement was visually verified against a rendered page of the source PDF; several were additionally
checked numerically or analytically).

> **Licensing:** problem statements and official answers remain © their respective organizers
> (MIT Integration Bee, UK University Integration Bee, University of Florida Mathematics Society) and
> are reproduced for non-commercial research with attribution — see [`ATTRIBUTION.md`](ATTRIBUTION.md).
> The curator's contributions (selection, transcription, verification metadata, data structure) are
> licensed CC BY 4.0 — see [`LICENSE`](LICENSE). Not affiliated with or endorsed by any organizer.

## Composition

| Source | Problems | Official answer key |
|---|---|---|
| MIT Integration Bee 2024 Qualifying Exam | 19 | `01_MIT/2024/Qualifier-Solutions.pdf` |
| MIT Integration Bee 2025 Qualifying Exam | 20 | `01_MIT/2025/Qualifier-Solutions.pdf` |
| MIT Integration Bee 2023 Qualifying Exam | 17 | `01_MIT/2023/Qualifier-Solutions.pdf` |
| UK University Integration Bee 2025/26 Round 1 (Online) | 30 | `02_UKUIB/2025/Regular-MarkScheme.pdf` |
| University of Florida Integration Bee 2025 Written Exam | 14 | `05_Florida/2025/Qualifier-Solutions.pdf` |
| **Total** | **100** | |

## Selection criteria

1. **Definite official answer.** Every problem's answer is taken from the competition's official
   answer key / mark scheme — never from third-party solutions and never re-derived by the curator.
2. **Clean statement.** Statements were transcribed from the official paper; any item whose printed
   statement could not be read unambiguously at high resolution was dropped.
3. **Consistency screening.** Every candidate was checked for mathematical consistency with its
   official answer (numeric quadrature via mpmath where feasible; derivative checks for indefinite
   integrals; analytic reasoning otherwise). Items where the official problem/answer pair failed to
   reproduce were **excluded** rather than silently fixed — see "Screened out" below.
4. **No computational-aid problems** (no estimation/tiebreaker decimals), no problems requiring
   unstated special-function definitions.

### Screened out (documented, not included)

- **MIT 2024 #18** — as printed, `∫₀¹ Σ_{n=0}^{2024} x^{2n−1012} dx` diverges at 0; the official key
  states `2025/2`, which could not be reproduced (likely a typo in the official paper).
- **MIT 2023 #18** — the official antiderivative differentiates to **2×** the integrand.
- **CMIMC 2025 (whole packet)** — the official problems+solutions files carry a wrong year header
  ("2024"), and of 15 items, #5 has a bound typo (answer corresponds to π/4, paper prints π/2), and
  #1/#3/#6/#7/#11 could not be reproduced from the printed statements; the packet was excluded
  entirely rather than cherry-picked. (Files remain in the archive at `08_CMIMC/2025/`.)

## Verification tags

Each problem carries a tag:

- **[N]** numerically verified — the official answer was reproduced by high-precision quadrature /
  derivative sampling (mpmath, 30–40 dps).
- **[A]** analytically verified — the curator checked the answer by hand (substitution, telescoping,
  symmetry, differentiation, known identity).
- **[O]** official key only — not independently re-checked; trusted as printed.

Notation: `log` is the natural logarithm (all four sources state this). `⌊·⌋` floor, `⌈·⌉` ceiling,
`{·}` fractional part. `+C` omitted on indefinite integrals. `φ = (1+√5)/2`.

---

## A · MIT Integration Bee 2024 — Qualifying Exam (19)

### B001 · MIT 2024 Q1 [A]
$$\int_{2023}^{2025} 2024\,dx \qquad\qquad \textbf{Answer: } 4048$$

### B002 · MIT 2024 Q2 [A]
$$\int \frac{(x-1)^{\log(x+1)}}{(x+1)^{\log(x-1)}}\,dx \qquad\qquad \textbf{Answer: } x$$

### B003 · MIT 2024 Q3 [A]
$$\int (x\log x + 2x)\,dx \qquad\qquad \textbf{Answer: } \tfrac12 x^2\log x + \tfrac34 x^2$$

### B004 · MIT 2024 Q4 [A]
$$\int \frac{dx}{x\log x + 2x} \qquad\qquad \textbf{Answer: } \log(\log x + 2)$$

### B005 · MIT 2024 Q5 [A]
$$\int_0^{2\pi} \arccos(\sin x)\,dx \qquad\qquad \textbf{Answer: } \pi^2$$

### B006 · MIT 2024 Q6 [A]
$$\int \frac{\cos x + \cot x + \csc x + 1}{\sin x + \tan x + \sec x + 1}\,dx \qquad\qquad \textbf{Answer: } \log(\sin x)$$

### B007 · MIT 2024 Q7 [A]
$$\int \frac{x^{2024}-1}{x^{506}-1}\,dx \qquad\qquad \textbf{Answer: } x + \frac{x^{507}}{507} + \frac{x^{1013}}{1013} + \frac{x^{1519}}{1519}$$

### B008 · MIT 2024 Q8 [A]
$$\int_{-1}^{1} (5x^3-3x)^2\,dx \qquad\qquad \textbf{Answer: } \tfrac87$$

### B009 · MIT 2024 Q9 [A]
$$\int_0^{2\pi} (\sin x + \cos x)^{11}\,dx \qquad\qquad \textbf{Answer: } 0$$

### B010 · MIT 2024 Q10 [A]
$$\int_0^{2\pi} (\sinh x + \cosh x)^{11}\,dx \qquad\qquad \textbf{Answer: } \frac{e^{22\pi}-1}{11}$$

### B011 · MIT 2024 Q11 [N]
$$\int \csc^2(x)\tan^{2024}(x)\,dx \qquad\qquad \textbf{Answer: } \frac{\tan^{2023}(x)}{2023}$$

### B012 · MIT 2024 Q12 [N]
$$\int \cos^x(x)\big(\log(\cos x) - x\tan x\big)\,dx \qquad\qquad \textbf{Answer: } \cos^x(x)$$

### B013 · MIT 2024 Q13 [N]
$$\int_{-\infty}^{\infty} e^{-(x-2024)^2/4}\,dx \qquad\qquad \textbf{Answer: } 2\sqrt{\pi}$$

### B014 · MIT 2024 Q14 [A]
$$\int_{1/e}^{e} \left(1-\frac{1}{x^2}\right)e^{e^x+1/x}\,dx \qquad\qquad \textbf{Answer: } 0$$

### B015 · MIT 2024 Q15 [A]
$$\int (x+1-e^{-x})e^{xe^x}\,dx \qquad\qquad \textbf{Answer: } e^{(e^x-1)x}$$

### B016 · MIT 2024 Q16 [A]
$$\int \left(\frac{\arctan(x)}{1-x^2} + \frac{\operatorname{arctanh}(x)}{1+x^2}\right)dx \qquad\qquad \textbf{Answer: } \arctan(x)\operatorname{arctanh}(x)$$

### B017 · MIT 2024 Q17 [A]
$$\int \left(\sum_{k=0}^{\infty} \sin\!\left(\frac{k\pi}{2}\right)x^k\right)dx \qquad\qquad \textbf{Answer: } \frac{\log(x^2+1)}{2}$$

### B018 · MIT 2024 Q19 [A]
$$\int \frac{x^4}{3-6x+6x^2-4x^3+2x^4}\,dx \qquad\qquad \textbf{Answer: } \frac{x}{2} + \frac14\log(3-6x+6x^2-4x^3+2x^4)$$

### B019 · MIT 2024 Q20 [N]
$$\int_1^3 \frac{x + \frac{x+\cdots}{1+\cdots}}{1 + \frac{x+\cdots}{1+\cdots}}\,dx \qquad\qquad \textbf{Answer: } 2\sqrt3 - \tfrac23$$
*(The self-similar continued fraction `y = (x+y)/(1+y)` gives `y = √x`, so the integrand simplifies to `√x`.)*

---

## B · MIT Integration Bee 2025 — Qualifying Exam (20)

### B020 · MIT 2025 Q1 [A]
$$\int \frac{x+\sqrt{x}}{1+\sqrt{x}}\,dx \qquad\qquad \textbf{Answer: } \tfrac23 x^{3/2}$$

### B021 · MIT 2025 Q2 [A]
$$\int \frac{e^{x+1}}{e^x+1}\,dx \qquad\qquad \textbf{Answer: } e\log(e^x+1)$$

### B022 · MIT 2025 Q3 [A]
$$\int \sqrt[3]{3\sin(x)-\sin(3x)}\,dx \qquad\qquad \textbf{Answer: } -\sqrt[3]{4}\cos(x)$$

### B023 · MIT 2025 Q4 [A]
$$\int_1^{e^e} \frac{\log\!\big(x^{\log(x^x)}\big)}{x^2}\,dx \qquad\qquad \textbf{Answer: } \frac{e^3}{3}$$

### B024 · MIT 2025 Q5 [A]
$$\int_{-\pi/2}^{\pi/2} \cos(20x)\sin(25x)\,dx \qquad\qquad \textbf{Answer: } 0$$

### B025 · MIT 2025 Q6 [A]
$$\int_0^{2\pi} \sin(x)\cos(x)\tan(x)\cot(x)\sec(x)\csc(x)\,dx \qquad\qquad \textbf{Answer: } 2\pi$$

### B026 · MIT 2025 Q7 [A]
$$\int \frac{x\log(x)\cos(x)-\sin(x)}{x\log^2(x)}\,dx \qquad\qquad \textbf{Answer: } \frac{\sin(x)}{\log(x)}$$

### B027 · MIT 2025 Q8 [A]
$$\int_1^2 \big(2^{x-1}+\log_2(2x)\big)\,dx \qquad\qquad \textbf{Answer: } 3$$

### B028 · MIT 2025 Q9 [A]
$$\int_0^1 x^{2024}(1-x^{2025})^{2025}\,dx \qquad\qquad \textbf{Answer: } \frac{1}{2025\cdot 2026}$$

### B029 · MIT 2025 Q10 [A]
$$\int_0^{10} x\left(x-\tfrac12\right)(x-1)\,dx \qquad\qquad \textbf{Answer: } 2025$$

### B030 · MIT 2025 Q11 [N]
$$\int_0^{20} \left\lfloor \frac{\lceil x\rceil}{2}\right\rfloor dx \qquad\qquad \textbf{Answer: } 100$$

### B031 · MIT 2025 Q12 [N]
$$\int \sqrt[3/1]{x\sqrt[4/2]{x\sqrt[5/3]{x\sqrt[6/4]{\cdots}}}}\,dx \qquad\qquad \textbf{Answer: } \frac{x^2}{2}$$
*(Radical indices are the fractions 3/1, 4/2, 5/3, 6/4, … exactly as printed; their reciprocal products telescope to 1, so the integrand equals `x`.)*

### B032 · MIT 2025 Q13 [A]
$$\int \frac{e^{2x}(x^2+x)}{(xe^x)^4+1}\,dx \qquad\qquad \textbf{Answer: } \tfrac12\arctan(x^2e^{2x})$$

### B033 · MIT 2025 Q14 [A]
$$\int \big(\sec^4(x)-\tan^4(x)\big)\,dx \qquad\qquad \textbf{Answer: } 2\tan(x)-x$$

### B034 · MIT 2025 Q15 [N]
$$\int_0^1 \sqrt{x(1-x)}\,dx \qquad\qquad \textbf{Answer: } \frac{\pi}{8}$$

### B035 · MIT 2025 Q16 [A]
$$\int \frac{\sin(4x)\cos(x)}{\cos(2x)\sin(x)}\,dx \qquad\qquad \textbf{Answer: } 2x+\sin(2x)$$

### B036 · MIT 2025 Q17 [N]
$$\int \sin(x)\sinh(x)\,dx \qquad\qquad \textbf{Answer: } \tfrac12\big(\sin(x)\cosh(x)-\cos(x)\sinh(x)\big)$$

### B037 · MIT 2025 Q18 [N]
$$\int_0^{\pi/3} \sin(x)\cos\!\left(\frac{\pi}{3}-x\right)dx \qquad\qquad \textbf{Answer: } \frac{\pi}{4\sqrt3}$$

### B038 · MIT 2025 Q19 [A]
$$\int \left(\cos(x)+\cos\!\left(x+\frac{2\pi}{3}\right)+\cos\!\left(x-\frac{2\pi}{3}\right)\right)^2 dx \qquad\qquad \textbf{Answer: } 0$$

### B039 · MIT 2025 Q20 [N]
$$\int_0^1 \left(\sum_{k=1}^{\infty}(-1)^k x^{2k}\right)dx \qquad\qquad \textbf{Answer: } \frac{\pi}{4}-1$$

---

## C · MIT Integration Bee 2023 — Qualifying Exam (17)

### B040 · MIT 2023 Q1 [A]
$$\int x^{\frac{1}{\log x}}\,dx \qquad\qquad \textbf{Answer: } ex$$

### B041 · MIT 2023 Q2 [A]
$$\int \operatorname{sech}(x)\,dx \qquad\qquad \textbf{Answer: } 2\arctan(e^x)$$

### B042 · MIT 2023 Q3 [A]
$$\int \frac{e^x}{(1+e^x)\log(1+e^x)}\,dx \qquad\qquad \textbf{Answer: } \log(\log(1+e^x))$$

### B043 · MIT 2023 Q4 [N]
$$\int (1+x+x^2+x^3+x^4)(1-x+x^2-x^3+x^4)\,dx \qquad\qquad \textbf{Answer: } x+\frac{x^3}{3}+\frac{x^5}{5}+\frac{x^7}{7}+\frac{x^9}{9}$$

### B044 · MIT 2023 Q5 [N]
$$\int_0^4 \binom{x}{5}\,dx \qquad\qquad \textbf{Answer: } 0$$

### B045 · MIT 2023 Q6 [A]
$$\int \big(x+\sin(x)+x\cos(x)+\sin(x)\cos(x)\big)\,dx \qquad\qquad \textbf{Answer: } \frac{(x+\sin x)^2}{2}$$

### B046 · MIT 2023 Q7 [A]
$$\int \big(\sin^2x+\cos^2x+\tan^2x+\cot^2x+\sec^2x+\csc^2x\big)\,dx \qquad\qquad \textbf{Answer: } 2\tan x - 2\cot x - x$$

### B047 · MIT 2023 Q8 [N]
$$\int_0^{2\pi} \lfloor 2023\sin(x)\rfloor\,dx \qquad\qquad \textbf{Answer: } -\pi$$

### B048 · MIT 2023 Q9 [A]
$$\int (2\log x+1)e^{(\log x)^2}\,dx \qquad\qquad \textbf{Answer: } x\,e^{(\log x)^2}$$

### B049 · MIT 2023 Q10 [A]
$$\int \Big((1-x)^3+(x-x^2)^3+(x^2-1)^3-3(1-x)(x-x^2)(x^2-1)\Big)dx \qquad\qquad \textbf{Answer: } 0$$
*(`a+b+c = 0` with `a=1−x, b=x−x², c=x²−1`.)*

### B050 · MIT 2023 Q11 [A]
$$\int_{-2023}^{2023} \underbrace{\big|\,\big|\,\big|\,\big|\,|x|-1\,\big|-1\,\big|\cdots-1\,\big|}_{2023\ \text{“}-1\text{”s}}\,dx \qquad\qquad \textbf{Answer: } 2023$$

### B051 · MIT 2023 Q13 [A]
$$\int (x+e+1)x^e e^x\,dx \qquad\qquad \textbf{Answer: } x^{e+1}e^x$$

### B052 · MIT 2023 Q15 [A]
$$\int \frac{1+2x^{2022}}{x+x^{2023}}\,dx \qquad\qquad \textbf{Answer: } \frac{1}{2022}\log\!\big(x^{2022}+x^{4044}\big)$$

### B053 · MIT 2023 Q16 [A]
$$\int \big(3\sin(20x)\cos(23x)+20\sin(43x)\big)\,dx \qquad\qquad \textbf{Answer: } \sin(20x)\sin(23x)$$

### B054 · MIT 2023 Q17 [N]
$$\int_0^1 \prod_{k=0}^{\infty} \frac{1}{1+x^{2^k}}\,dx \qquad\qquad \textbf{Answer: } \tfrac12$$

### B055 · MIT 2023 Q19 [N]
$$\int \frac{\log(x/\pi)}{(\log x)^{\log(\pi e)}}\,dx \qquad\qquad \textbf{Answer: } \frac{x}{(\log x)^{\log\pi}}$$

### B056 · MIT 2023 Q20 [N]
$$\int_{-3/2}^{-1/2} \big(x^5+5x^4+10x^3+8x^2+x\big)\,dx \qquad\qquad \textbf{Answer: } \tfrac56$$

---

## D · UK University Integration Bee 2025/26 — Round 1, Online (30)

*(Official Mark Scheme also lists half-credit conventions for #6, #12, #18, #21 — omitted here.)*

### B057 · UKUIB 2025 R1 #1 [N]
$$\int_0^{\pi/4} \frac{dx}{x^2+1} \qquad\qquad \textbf{Answer: } \arctan\!\left(\frac{\pi}{4}\right)$$

### B058 · UKUIB 2025 R1 #2 [N]
$$\int_0^{\infty} \sin(\pi\lfloor x\rfloor)\,dx \qquad\qquad \textbf{Answer: } 0$$

### B059 · UKUIB 2025 R1 #3 [N]
$$\int_0^{\infty} \operatorname{sech}(2\ln x)\,dx \qquad\qquad \textbf{Answer: } \frac{\pi}{\sqrt2}$$

### B060 · UKUIB 2025 R1 #4 [A]
$$\int_0^a e^{i\pi/2}\,dz \qquad\qquad \textbf{Answer: } ai$$

### B061 · UKUIB 2025 R1 #5 [A]
$$\int_{-\pi/2}^{\pi/2} \frac{\cos x}{1+e^{x/2}}\,dx \qquad\qquad \textbf{Answer: } 1$$

### B062 · UKUIB 2025 R1 #6 [N]
$$\int_0^1 \sqrt{-\ln x}\,dx \qquad\qquad \textbf{Answer: } \frac{\sqrt\pi}{2}$$

### B063 · UKUIB 2025 R1 #7 [N]
$$\int_0^1\Big(1+x+x^2+\cdots+x^{2025} - \big(\{x\}+\{x\{x\}\}+\{x\{x\{x\}\}\}+\cdots+\underbrace{\{x\{\cdots\{x\}\cdots\}\}}_{2025\ \text{times}}\big)\Big)dx \qquad\qquad \textbf{Answer: } 1$$

### B064 · UKUIB 2025 R1 #8 [A]
$$\int_0^{\infty}\left(1-\frac{x}{1}\left(1-\frac{x}{2}\left(1-\frac{x}{3}\left(1-\frac{x}{4}(\cdots)\right)\right)\right)\right)dx \qquad\qquad \textbf{Answer: } 1$$

### B065 · UKUIB 2025 R1 #9 [N]
$$\int_{-\pi/4}^{\pi/4} \frac{7x^7-5x^5+3x^3-x+1}{\cos^2(x)}\,dx \qquad\qquad \textbf{Answer: } 2$$

### B066 · UKUIB 2025 R1 #10 [A]
$$\int_0^{\pi/2} \frac{\tan^{-1}(b\sin x)}{\sin x}\,dx \qquad\qquad \textbf{Answer: } \frac{\pi}{2}\sinh^{-1}(b) = \frac{\pi}{2}\ln\!\big(b+\sqrt{b^2+1}\big)$$

### B067 · UKUIB 2025 R1 #11 [A]
$$\int \frac{dx}{x\sin^{-1}(\ln x)\sqrt{1-(\ln x)^2}} \qquad\qquad \textbf{Answer: } \ln\big|\sin^{-1}(\ln x)\big| + C$$

### B068 · UKUIB 2025 R1 #12 [A]
$$\lim_{n\to\infty}\int_0^1 \big|x-|x^2-|x^3-\cdots-|x^{n-1}-|x^n||\cdots|\big|\,dx \qquad\qquad \textbf{Answer: } 1-\ln 2$$

### B069 · UKUIB 2025 R1 #13 [A]
$$\int_{|x|+|y|+|z|\le 1} \big\lceil x^2+y^2+z^2\big\rceil\,dx\,dy\,dz \qquad\qquad \textbf{Answer: } \frac43$$
*(The paper prints brackets `[·]`; the official answer 4/3 equals the octahedron's volume, which fixes the intended meaning as the ceiling function — the integrand is 1 almost everywhere.)*

### B070 · UKUIB 2025 R1 #14 [A]
$$\int_0^{2\pi} \sin(\sin x + 2025x)\,dx \qquad\qquad \textbf{Answer: } 0$$

### B071 · UKUIB 2025 R1 #15 [N]
$$\int_0^{\pi} \sqrt{1+\sin(2x)}\,dx \qquad\qquad \textbf{Answer: } 2\sqrt2$$

### B072 · UKUIB 2025 R1 #16 [N]
$$\int_0^{\infty} \frac{dx}{(x^4+1)^2} \qquad\qquad \textbf{Answer: } \frac{3\pi}{8\sqrt2}$$

### B073 · UKUIB 2025 R1 #17 [A]
$$\int_1^{\infty} \frac{dx}{x+nx^n} \quad (n>1) \qquad\qquad \textbf{Answer: } \frac{1}{1-n}\ln\!\left(\frac{n}{n+1}\right)$$

### B074 · UKUIB 2025 R1 #18 [N]
$$\int_0^{\pi/2} \frac{x}{\tan x}\,dx \qquad\qquad \textbf{Answer: } \frac{\pi}{2}\ln 2$$

### B075 · UKUIB 2025 R1 #19 [A]
$$\int_0^{2025}\left(\frac{x}{\sqrt{x+\sqrt{x+\sqrt{x+\cdots}}}} - \sqrt{x-\sqrt{x-\sqrt{x-\cdots}}}\right)dx \qquad\qquad \textbf{Answer: } 0$$

### B076 · UKUIB 2025 R1 #20 [N]
$$\int_0^{\pi/2}\int_0^1 \exp\!\big(t+t^{\tan\theta}\big)\,dt\,d\theta \qquad\qquad \textbf{Answer: } \frac{\pi}{4}\big(e^2-1\big)$$

### B077 · UKUIB 2025 R1 #21 [A]
$$\int_0^1\cdots\int_0^1 \max(x_1,\dots,x_{2025})\,dx_1\cdots dx_{2025} \qquad\qquad \textbf{Answer: } \frac{2025}{2026}$$

### B078 · UKUIB 2025 R1 #22 [N]
$$\int_0^{\infty}\left(\frac{x}{(2^x-1)^2} - \frac{4x}{(4^x-1)^2}\right)dx \qquad\qquad \textbf{Answer: } \frac{1}{\ln 2}$$

### B079 · UKUIB 2025 R1 #23 [N]
$$\int_1^{e}\left(\sqrt{\ln x} + \frac{1}{e-1}\exp\!\left(\left(\frac{x-1}{e-1}\right)^2\right)\right)dx \qquad\qquad \textbf{Answer: } e$$

### B080 · UKUIB 2025 R1 #24 [N]
$$\int_0^{\infty} \frac{x^2 + \frac{2^{-x/6}}{7} - \frac{2^{-x/7}}{6}}{(2^{-x/7}+36x^2)(2^{-x/6}+49x^2)}\,dx \qquad\qquad \textbf{Answer: } 0$$

### B081 · UKUIB 2025 R1 #25 [N]
$$\int_0^{25} \sqrt{1+x\sqrt{1+(x+1)\sqrt{1+(x+2)\sqrt{\cdots}}}}\,dx \qquad\qquad \textbf{Answer: } \frac{675}{2}$$

### B082 · UKUIB 2025 R1 #26 [N]
$$\int_0^1 \frac{x(x-1)}{(x+1)\ln x}\,dx \qquad\qquad \textbf{Answer: } \ln\!\left(\frac{4}{\pi}\right)$$

### B083 · UKUIB 2025 R1 #27 [N]
$$\int \frac{2^x}{(1+\sqrt3)^x+(2+\sqrt3)^x}\,dx \qquad\qquad \textbf{Answer: } \frac{(\sqrt3-1)^x - \ln\!\big(1+(\sqrt3-1)^x\big)}{\ln(\sqrt3-1)} + C$$

### B084 · UKUIB 2025 R1 #28 [O]
$$\int_{-90}^{90} \operatorname{mrt}\big(x^3-(3+a)x^2+(4+2a)x-(2+a)\big)\,da$$
where `mrt(f)` is 0 if `f` has fewer than two distinct real roots, else the smallest distance between distinct real roots.
$$\textbf{Answer: } 90\big(45-\sqrt{2024}\big) - 2\ln\!\big(45-\sqrt{2024}\big) - 3\ln 2$$

### B085 · UKUIB 2025 R1 #29 [N]
$$\int_0^{124} (f(x))^2\,dx,\quad \text{where } f:[0,\infty)\to\mathbb{R}\ \text{satisfies } (f(x))^3+xf(x)=125 \qquad\qquad \textbf{Answer: } 812$$

### B086 · UKUIB 2025 R1 #30 [N]
$$\int_1^2 \frac{\tan^{-1}(1+x)}{x}\,dx \qquad\qquad \textbf{Answer: } \frac{3\pi\ln 2}{8} = \frac{\ln 2\,(\tan^{-1}3+\tan^{-1}2)}{2}$$

---

## E · University of Florida Integration Bee 2025 — Written Exam (14)

### B087 · Florida 2025 #4 [A]
$$\int_0^{2\pi} \max(\sin x,\cos x)\,dx \qquad\qquad \textbf{Answer: } 2\sqrt2$$

### B088 · Florida 2025 #5 [A]
$$\int \frac{dx}{(x-1)(x-2)(x-3)(x-4)} \qquad\qquad \textbf{Answer: } \frac16\big(-\ln(x-1)+3\ln(x-2)-3\ln(x-3)+\ln(x-4)\big)$$

### B089 · Florida 2025 #6 [A]
$$\int_0^{\pi} \sin^4(x)\cos^2(x)\,dx \qquad\qquad \textbf{Answer: } \frac{\pi}{16}$$

### B090 · Florida 2025 #7 [A]
$$\int \frac{\sin x+\cos x}{2\sin x+3\cos x}\,dx \qquad\qquad \textbf{Answer: } \frac{1}{13}\big(5x-\ln(2\sin x+3\cos x)\big)$$

### B091 · Florida 2025 #8 [A]
$$\int \frac{e^x(x-3)}{(x+1)^5}\,dx \qquad\qquad \textbf{Answer: } \frac{e^x}{(x+1)^4}$$

### B092 · Florida 2025 #9 [A]
$$\int \big(\sec^6(x)-\tan^6(x)\big)\,dx \qquad\qquad \textbf{Answer: } x+\tan^3(x)$$

### B093 · Florida 2025 #10 [A]
$$\int_1^{2025} \sqrt{1+\frac{1}{x^2}+\frac{1}{(x+1)^2}}\,dx \qquad\qquad \textbf{Answer: } 2024+\ln\!\left(\frac{2025}{1013}\right)$$

### B094 · Florida 2025 #13 [A]
$$\int_0^{\pi/4} \cfrac{1}{2\tan x + \cfrac{1}{2\tan x + \cfrac{1}{2\tan x + \cdots}}}\,dx \qquad\qquad \textbf{Answer: } \ln\!\left(1+\frac{1}{\sqrt2}\right)$$

### B095 · Florida 2025 #14 [A]
$$\int_0^1 \frac{\sqrt{x}-\sqrt[4]{x}}{\ln x}\,dx \qquad\qquad \textbf{Answer: } \ln\!\left(\frac65\right)$$

### B096 · Florida 2025 #16 [A]
$$\int \frac{\ln x}{x}\cdot\frac{dx}{x^{\ln x}+x^{-\ln x}} \qquad\qquad \textbf{Answer: } \tfrac12\arctan\!\big(x^{\ln x}\big)$$

### B097 · Florida 2025 #17 [A]
$$\int_{-\infty}^{\infty} (20x+25)e^{-2025x^2}\,dx \qquad\qquad \textbf{Answer: } \frac{5\sqrt\pi}{9}$$

### B098 · Florida 2025 #18 [A]
$$\lim_{n\to\infty} \sqrt{n}\int_0^2 \big[x(2-x)\big]^n\,dx \qquad\qquad \textbf{Answer: } \sqrt{\pi}$$

### B099 · Florida 2025 #20 [A]
$$\frac{\displaystyle\int_0^{\infty}(1+x^2)^{-2024}\,dx}{\displaystyle\int_0^{\infty}(1+x^2)^{-2025}\,dx} \qquad\qquad \textbf{Answer: } \frac{4048}{4047}$$

### B100 · Florida 2025 #21 [A]
$$\int \frac{xe^x-e^x}{x^2+e^{2x}}\,dx \qquad\qquad \textbf{Answer: } \arctan\!\left(\frac{e^x}{x}\right)$$

---

## Provenance

All statements and answers were transcribed from the archive's copies of the official papers:

| Source | Problem file | Answer file |
|---|---|---|
| MIT 2024 | `01_MIT/2024/Qualifier.pdf` | `01_MIT/2024/Qualifier-Solutions.pdf` |
| MIT 2025 | `01_MIT/2025/Qualifier.pdf` | `01_MIT/2025/Qualifier-Solutions.pdf` |
| MIT 2023 | `01_MIT/2023/Qualifier.pdf` | `01_MIT/2023/Qualifier-Solutions.pdf` |
| UKUIB 2025/26 R1 | `02_UKUIB/2025/Regular-Original.pdf` | `02_UKUIB/2025/Regular-MarkScheme.pdf` |
| Florida 2025 | `05_Florida/2025/Qualifier.pdf` | `05_Florida/2025/Qualifier-Solutions.pdf` |

Machine-readable copy: [`base-set.json`](base-set.json) (fields: `id`, `source`, `number`, `problem`,
`answer`, `verify`).
