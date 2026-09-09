# Integration Bee Benchmark — Hard Set

**25 problems from the MIT Integration Bee Finals, 2022–2026 — with the organizers' official answers.**

Companion to the [Base Set](BASE-SET.md). The Base Set draws on qualifying /
online / written rounds (entry-level speed rounds); this Hard Set is the other end of the
difficulty scale: one problem per finalist, 4–5 minutes each, from the MIT Integration Bee Finals.

## Composition

| Source | Problems |
|---|---|
| MIT Integration Bee Finals 2022 | 5 |
| MIT Integration Bee Finals 2023 | 5 |
| MIT Integration Bee Finals 2024 | 5 |
| MIT Integration Bee Finals 2025 | 5 |
| MIT Integration Bee Finals 2026 | 5 |
| **Total** | **25** |

Every answer is the official answer printed by the MIT Integration Bee in the Finals papers
(the papers alternate problem / problem-with-answer). Every statement was transcribed and then
**verified**: definite integrals by high-precision quadrature (mpmath, 35 digits), indefinite
integrals by differentiating the official antiderivative, and the floor/limit problems by exact
combinatorial or interval arguments. Tag `[N]` = verified numerically/exactly, `[A]` = verified
analytically.

Notation: `log` is natural; `⌊·⌋` floor; `φ = (1+√5)/2`; `+C` omitted on indefinite integrals.

---

## 2022 Finals

### H001 · MIT Finals 2022 #1 [N]
$$\int \sqrt{(\sin 20x+3\sin 21x+\sin 22x)^2+(\cos 20x+3\cos 21x+\cos 22x)^2}\,dx \qquad \textbf{Answer: } 3x+2\sin x$$

### H002 · MIT Finals 2022 #2 [N]
$$\int_0^{\infty} \frac{e^{-2x}\sin(3x)}{x}\,dx \qquad \textbf{Answer: } \arctan\frac32$$

### H003 · MIT Finals 2022 #3 [A]
$$\int_0^{2\pi} \cos(2022x)\,\frac{\sin(10050x)}{\sin(50x)}\,\frac{\sin(10251x)}{\sin(51x)}\,dx \qquad \textbf{Answer: } 6\pi$$
*(Dirichlet-kernel expansion: the constant term counts exactly 3 matching frequencies, giving `3·2π`.)*

### H004 · MIT Finals 2022 #4 [N]
$$\int_0^1 x^{1/3}(1-x)^{2/3}\,dx \qquad \textbf{Answer: } \frac{2\pi}{9\sqrt3}$$

### H005 · MIT Finals 2022 #5 [N]
$$\left\lfloor \log_{10}\int_{2022}^{\infty} 10^{-x^3}\,dx \right\rfloor \qquad \textbf{Answer: } -2022^3-8$$

## 2023 Finals

### H006 · MIT Finals 2023 #1 [N]
$$\int_0^{\pi/2} \frac{\sqrt[3]{\tan x}}{(\sin x+\cos x)^2}\,dx \qquad \textbf{Answer: } \frac{2\sqrt3\,\pi}{9}$$

### H007 · MIT Finals 2023 #2 [N]
$$\int_0^{\pi} \left(\frac{\sin(2x)\sin(3x)\sin(5x)\sin(30x)}{\sin(x)\sin(6x)\sin(10x)\sin(15x)}\right)^2 dx \qquad \textbf{Answer: } 7\pi$$

### H008 · MIT Finals 2023 #3 [N]
$$\int_{-1/2}^{1/2} \sqrt{x^2+1+\sqrt{x^4+x^2+1}}\;dx \qquad \textbf{Answer: } \frac{\sqrt7}{2\sqrt2}+\frac{3}{4\sqrt2}\log\!\left(\frac{\sqrt7+2}{\sqrt3}\right)$$

### H009 · MIT Finals 2023 #4 [N]
$$\left\lfloor 10^{20}\int_2^{\infty}\frac{x^9}{x^{20}-48x^{10}+575}\,dx\right\rfloor \qquad \textbf{Answer: } 10000003333335333$$

### H010 · MIT Finals 2023 #5 [N]
$$\int_0^1 \left(\sum_{n=1}^{\infty}\frac{\lfloor 2^n x\rfloor}{3^n}\right)^2 dx \qquad \textbf{Answer: } \frac{27}{32}$$

## 2024 Finals

### H011 · MIT Finals 2024 #1 [N]
$$\int \frac{e^{x/2}\cos x}{\sqrt[3]{3\cos x+4\sin x}}\,dx \qquad \textbf{Answer: } \frac{6}{25}\big(3\cos x+4\sin x\big)^{2/3}e^{x/2}$$

### H012 · MIT Finals 2024 #2 [N]
$$\int_0^{\infty} \frac{\log(2e^x-1)}{e^x-1}\,dx \qquad \textbf{Answer: } \frac{\pi^2}{4}$$

### H013 · MIT Finals 2024 #3 [N]
$$\int_{-\infty}^{\infty} \frac{dx}{x^4+x^3+x^2+x+1} \qquad \textbf{Answer: } \frac{\sqrt{10+2\sqrt5}}{5}\,\pi$$

### H014 · MIT Finals 2024 #4 [N]
$$\int_{-1/3}^{1}\left(\sqrt[3]{1+\sqrt{1-x^3}}+\sqrt[3]{1-\sqrt{1-x^3}}\right)dx \qquad \textbf{Answer: } \frac{14}{9}+\frac23\log 2$$

### H015 · MIT Finals 2024 #5 [N]
$$\int_0^1 \max_{n\in\mathbb{Z}_{\ge0}}\left(\frac{1}{2^n}\left(\lfloor 2^n x\rfloor-\left\lfloor 2^n x-\frac14\right\rfloor\right)\right)dx \qquad \textbf{Answer: } \frac{4}{11}$$
*(Both brackets are floors; exact dyadic computation agrees with 4/11 to 80-bit precision.)*

## 2025 Finals

### H016 · MIT Finals 2025 #1 [N]
$$\int \tan x\,\sqrt{2+\sqrt{4+\cos x}}\;dx \qquad \textbf{Answer: } -4\sqrt{2+\sqrt{4+\cos x}}-2\log\!\left(\frac{\sqrt{2+\sqrt{4+\cos x}}-2}{\sqrt{2+\sqrt{4+\cos x}}+2}\right)$$
*(The tangent multiplies the radical — it is not a quotient.)*

### H017 · MIT Finals 2025 #2 [N]
$$\int_0^{\infty} \frac{dx}{\big(x+1+\lfloor 2\sqrt{x}\rfloor\big)^2} \qquad \textbf{Answer: } \frac{2\pi^2}{3}-\frac{73}{12}$$

### H018 · MIT Finals 2025 #3 [N]
$$\int_0^{10} \left\lfloor \varphi^{\lfloor x\rfloor}\right\rfloor dx \qquad \textbf{Answer: } 193$$

### H019 · MIT Finals 2025 #4 [N]
$$\int_0^{\pi} \max\big(|2\sin x|,\,|2\cos 2x-1|\big)^2\cdot\min\big(|\sin 2x|,\,|\cos 3x|\big)^2 dx \qquad \textbf{Answer: } \pi$$

### H020 · MIT Finals 2025 #5 [N]
$$\int_0^1\left(\sqrt{\frac{1}{4x^2}+\frac1x-x}-\sqrt{\frac{x^4}{4}-x+1}-\frac{1}{2x}\right)dx \qquad \textbf{Answer: } -\frac16$$

## 2026 Finals

### H021 · MIT Finals 2026 #1 [N]
$$\lim_{n\to\infty}\int_0^1 \sum_{k=1}^{n}\frac{dx}{nx^2+kx+n} \qquad \textbf{Answer: } \frac{5\pi^2}{72}$$

### H022 · MIT Finals 2026 #2 [N]
$$\int \frac{dx}{(x-1)\sqrt[4]{x^3+x}} \qquad \textbf{Answer: } \frac{1}{4\sqrt[4]{2}}\left(\log\frac{x+1-\sqrt[4]{8x^3+8x}}{x+1+\sqrt[4]{8x^3+8x}}+2\arctan\frac{\sqrt[4]{8x^3+8x}}{x+1}\right)$$

### H023 · MIT Finals 2026 #3 [N]
$$\lim_{n\to\infty}\int_0^{2026}\underbrace{\log_{\sqrt2}\big(x+\log_{\sqrt2}\big(x+\cdots+\log_{\sqrt2}(x+2026)\cdots\big)\big)}_{n\ \text{nested logs}}dx \qquad \textbf{Answer: } 44806-\frac{4088}{\log 2}$$

### H024 · MIT Finals 2026 #4 [N]
$$\int_0^{1/4}\left(\left\lfloor\sqrt[4]{\frac1x-4}\right\rfloor^2+\left\lfloor\sqrt[4]{\frac1x-4}\right\rfloor\right)dx \qquad \textbf{Answer: } \frac34$$

### H025 · MIT Finals 2026 #5 [N]
$$\int_{-\infty}^{\infty}\left(\left(\frac{1}{x-2}+\frac{3}{x-4}+\frac{5}{x-6}\right)^{-2}+1\right)^{-1}dx \qquad \textbf{Answer: } 9\pi$$

---

## Provenance

| Year | Problem file |
|---|---|
| 2022 | `01_MIT/2022/Final.pdf` |
| 2023 | `01_MIT/2023/Final.pdf` |
| 2024 | `01_MIT/2024/Final.pdf` |
| 2025 | `01_MIT/2025/Final.pdf` |
| 2026 | `01_MIT/2026/Final.pdf` |

Machine-readable copy: [`hard-set.json`](hard-set.json). Copyright: © MIT Integration Bee / MIT —
see [`ATTRIBUTION.md`](ATTRIBUTION.md); reproduced for non-commercial research with attribution.
