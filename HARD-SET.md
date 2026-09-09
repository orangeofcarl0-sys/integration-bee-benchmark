# Integration Bee Benchmark — Hard Set

**100 problems from knockout rounds worldwide — MIT Finals and Semifinals, Lisbon, UKUIB R3, Caltech, Bonn, Chulalongkorn and Singapore — with the organizers' official answers.**

Companion to the [Base Set](BASE-SET.md). The Base Set draws on qualifying / online / written
rounds (entry-level speed rounds); this Hard Set is the other end of the difficulty scale —
knockout and final rounds from seven competitions on three continents.

## Composition

| Source | Problems | Rounds |
|---|---|---|
| MIT Integration Bee (USA) | 45 | Finals 2022–2026 (25) + Semifinals 2022–2026 (20) |
| Singapore Precollegiate Integration Bee | 20 | Round 2 (groups → QF → SF → 3rd place → Grand Final) |
| Lisbon Integration Bee (Portugal) | 8 | Semifinals + Final |
| UKUIB (UK) | 10 | Round 3 Tournament 2024/25 |
| Chulalongkorn University (Thailand) | 6 | Final Round 2025 |
| Caltech Math Meet (USA) | 6 | 2025 Final, Hard set |
| Bonn Integration Bee (Germany) | 5 | 2026 |
| **Total** | **100** | |

Every answer is the organizers' own official answer (MIT elimination papers alternate
problem / problem-with-answer; Lisbon, Singapore and Chulalongkorn print answers with the problems;
UKUIB/Caltech/Bonn print full official solutions). Every statement was transcribed and then
**verified**: definite integrals by high-precision quadrature (mpmath, 25–35 digits), indefinite
integrals by differentiating the official antiderivative, and floor/limit/series problems by exact
combinatorial arguments. Tag `[N]` = verified numerically/exactly, `[A]` = verified analytically.

Items that failed screening were excluded and documented in the repository README (source errors,
notably UKUIB R3 B2F1#3 and Chulalongkorn R2#3/R3#1 whose printed answers could not be reproduced).

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

## Lisbon Integration Bee 2025 (8)

### H026 · Lisbon 2025 Semifinal 1 #1 [N]
$$\int_0^{2025}\lfloor\sqrt{x}\rfloor\,dx \qquad \textbf{Answer: } 59730$$

### H027 · Lisbon 2025 Semifinal 1 #2 [N]
$$\int_{-\pi/2}^{\pi/2}\max\big(2\sin^2x,\,2\cos^2x\big)\,dx \qquad \textbf{Answer: } \pi+2$$

### H028 · Lisbon 2025 Semifinal 1 #3 [N]
$$\int_0^1 \frac{dx}{\sqrt{|\log x|}} \qquad \textbf{Answer: } \sqrt{\pi}$$

### H029 · Lisbon 2025 Semifinal 1 #4 [A]
$$\int_{-\infty}^{\infty} x^{100}e^{-x^2}\,dx \qquad \textbf{Answer: } \frac{\sqrt{\pi}}{4^{50}}\cdot\frac{100!}{50!}$$

### H030 · Lisbon 2025 Semifinal 2 #1 [N]
$$\int_0^{\infty}\frac{dx}{(x^2+4)^2} \qquad \textbf{Answer: } \frac{\pi}{32}$$

### H031 · Lisbon 2025 Semifinal 2 #2 [N]
$$\int_0^{\infty}\frac{3^{-\lfloor x\rfloor}\cos(\lfloor x\rfloor\pi)}{2\lfloor x\rfloor+1}\,dx \qquad \textbf{Answer: } \frac{\sqrt3}{6}\pi$$

### H032 · Lisbon 2025 Final #3 [N]
$$\int_0^{\infty}\frac{x^3}{e^x-1}\,dx \qquad \textbf{Answer: } \frac{\pi^4}{15}$$

### H033 · Lisbon 2025 Final #4 [N]
$$\int_0^1 \frac{x^4(1-x)^4}{1+x^2}\,dx \qquad \textbf{Answer: } \frac{22}{7}-\pi$$

## MIT Integration Bee Semifinals 2022–2026 (20)

### H034 · MIT Semifinal 2022 #1-1 [N]
$$\int_0^{\infty}\frac{x(e^{-x}+1)}{e^x-1}\,dx \qquad \textbf{Answer: } \frac{\pi^2}{3}-1$$

### H035 · MIT Semifinal 2022 #1-2 [N]
$$\int_0^{\infty} x^5 e^{-x}\sin x\,dx \qquad \textbf{Answer: } -15$$

### H036 · MIT Semifinal 2022 #2-2 [A]
$$\int \frac{dx}{(x^2+1)^3} \qquad \textbf{Answer: } \frac{3}{8}\arctan x+\frac{3x^3+5x}{8(x^2+1)^2}+C$$

### H037 · MIT Semifinal 2022 #2-4 [N]
$$\int_0^{\pi/6}\log(\sqrt3+\tan x)\,dx \qquad \textbf{Answer: } \frac{\pi}{6}\log 2$$

### H038 · MIT Semifinal 2023 #1-2 [N]
$$\int_0^1\big(9x^9-x^{90}+9x^{99}-x^{900}+9x^{909}-x^{990}+9x^{999}-x^{9000}+\cdots\big)dx \qquad \textbf{Answer: } 1$$

### H039 · MIT Semifinal 2023 #1-3 [N]
$$\int_0^{\pi}\frac{2\cos x-\cos(2021x)-2\cos(2022x)-\cos(2023x)+2}{1-\cos(2x)}\,dx \qquad \textbf{Answer: } 2022\pi$$

### H040 · MIT Semifinal 2023 #2-3 [N]
$$\int_0^{\infty}\frac{\tanh x}{x\cosh(2x)}\,dx \qquad \textbf{Answer: } \log 2$$

### H041 · MIT Semifinal 2023 #2-4 [A]
$$\int \sin(4\arctan x)\,dx \qquad \textbf{Answer: } -\frac{4}{1+x^2}-2\log(1+x^2)+C$$

### H042 · MIT Semifinal 2024 #1-1 [N]
$$\int_{-\infty}^{\infty}\frac{(x^3-4x)\sin x+(3x^2-4)\cos x}{(x^3-4x)^2+\cos^2x}\,dx \qquad \textbf{Answer: } -3\pi$$

### H043 · MIT Semifinal 2024 #1-2 [N]
$$\int_0^{\infty}\frac{xe^{-2x}}{e^{-x}+1}\,dx \qquad \textbf{Answer: } 1-\frac{\pi^2}{12}$$

### H044 · MIT Semifinal 2024 #1-3 [N]
$$\int_0^{\pi/2}\sin(\cot^2x)\sec^2x\,dx \qquad \textbf{Answer: } \sqrt{\frac{\pi}{2}}$$

### H045 · MIT Semifinal 2024 #2-1 [N]
$$\int_0^{\infty}\frac{\sin x\,\sin(2x)\sin(3x)}{x^3}\,dx \qquad \textbf{Answer: } \pi$$

### H046 · MIT Semifinal 2025 #1-1 [N]
$$\int_0^{\infty}\frac{\sqrt[3]{x}}{1+x^2}\,dx \qquad \textbf{Answer: } \frac{\pi}{\sqrt3}$$

### H047 · MIT Semifinal 2025 #1-4 [N]
$$\int_0^{\infty}\frac{x}{e^{2x}+1}\,dx \qquad \textbf{Answer: } \frac{\pi^2}{48}$$

### H048 · MIT Semifinal 2025 #2-2 [N]
$$\int_0^1\frac{\log x}{\sqrt{x-x^2}}\,dx \qquad \textbf{Answer: } -2\pi\log 2$$

### H049 · MIT Semifinal 2025 #2-3 [N]
$$\int_1^{\infty}\left(\sum_{k=0}^{\infty}(-1)^k\max(0,x-k)\right)^{-2}dx \qquad \textbf{Answer: } 1+\frac{\pi^2}{6}$$

### H050 · MIT Semifinal 2026 #1-1 [N]
$$\lim_{n\to\infty}\int_0^{\infty}\sqrt{n}\left(\frac{e^{x-1}}{x^x}\right)^n dx \qquad \textbf{Answer: } \sqrt{2\pi}$$

### H051 · MIT Semifinal 2026 #1-2 [A]
$$\int\frac{x^2-2}{(x^2+2)\sqrt{x^4+4}}\,dx \qquad \textbf{Answer: } \frac12\arctan\!\left(\frac{\sqrt{x^4+4}}{2x}\right)+C$$

### H052 · MIT Semifinal 2026 #2-1 [N]
$$\lim_{n\to\infty}\int_{-2}^{2}\big(\cdots((x^2-2)^2-2)^2\cdots-2\big)^4dx\ \ (n\ \text{squares}) \qquad \textbf{Answer: } 24$$

### H053 · MIT Semifinal 2026 #2-3 [N]
$$\int_0^{\pi}\cos(2x)\cos(3x)\cos(5x)\cos(7x)\cos(11x)\cos(13x)\cos(17x)\cos(19x)\cos(23x)\,dx \qquad \textbf{Answer: } \frac{5\pi}{256}$$

## UKUIB 2024/25 Round 3 — Tournament (10)

### H054 · UKUIB R3 2024/25 Battle 2 Fight 1 #1 [N]
$$\int_1^{e}\frac{x\ln x}{(1+\ln x)^3}\,dx \qquad \textbf{Answer: } \frac12\left(\frac{e^2}{4}-1\right)$$

### H055 · UKUIB R3 2024/25 Battle 2 Fight 3 #1 [N]
$$\int_3^4\frac{x-\sqrt{7x-x^2}}{2x-7}\,dx \qquad \textbf{Answer: } \frac12$$

### H056 · UKUIB R3 2024/25 Battle 2 Fight 3 #2 [N]
$$\int_1^{\infty}\frac{1+2x\ln 2}{x\sqrt{x\,4^x-1}}\,dx \qquad \textbf{Answer: } \frac{\pi}{3}$$

### H057 · UKUIB R3 2024/25 Battle 2 Fight 3 #3 [N]
$$\int \sec x\,(\sec x+\tan x)^{2025}\,dx \qquad \textbf{Answer: } \frac{(\sec x+\tan x)^{2025}}{2025}+C$$

### H058 · UKUIB R3 2024/25 Battle 3 Fight 1 #2 [N]
$$\int_0^{\infty}\frac{\tan^{-1}\!\left(\frac{x}{1+2x^2}\right)-\tan^{-1}\!\left(\frac{x}{1+12x^2}\right)}{x}\,dx \qquad \textbf{Answer: } \frac{\pi}{2}\ln\frac32$$

### H059 · UKUIB R3 2024/25 Battle 3 Fight 1 #3 [N]
$$\int_0^{\pi/2}\sin x\,\sqrt{\sin(2x)}\,dx \qquad \textbf{Answer: } \frac{\pi}{4}$$

### H060 · UKUIB R3 2024/25 Battle 3 Fight 2 #2 [N]
$$\int_{\pi/4}^{\pi/2}\sin(x)^{\tan x}\big(\sec^2x\,\ln\sin x+1\big)\,dx \qquad \textbf{Answer: } 1-\frac{\sqrt2}{2}$$

### H061 · UKUIB R3 2024/25 Battle 3 Fight 2 #3 [N]
$$\int_1^{\sqrt2}\frac{\sqrt{x^2+2\sqrt{x^2-1}}}{x}\,dx \qquad \textbf{Answer: } \frac12\ln 2+1-\frac{\pi}{4}$$

### H062 · UKUIB R3 2024/25 Battle 3 Fight 3 #1 [A]
$$\int_0^{\infty}\cos\!\left(x^2+\frac{1}{x^2}\right)dx \qquad \textbf{Answer: } \frac{\sqrt{2\pi}}{4}(\cos 2-\sin 2)$$

### H063 · UKUIB R3 2024/25 Battle 2 Fight 2 #2 [N]
$$\int_0^1\frac{\ln(x)(2x-1)}{\sqrt{x-x^2}}\,dx \qquad \textbf{Answer: } \pi$$

## Caltech 2025 Integration Bee Final — Hard (6)

### H064 · Caltech 2025 Final (Hard) #3 [A]
$$\int\frac{2x-9\sqrt x+9}{(x-3\sqrt x)^{1/3}}\,dx \qquad \textbf{Answer: } \frac65(x-3\sqrt x)^{5/3}+C$$

### H065 · Caltech 2025 Final (Hard) #5 [N]
$$\int_0^1\frac{x^3}{(3+2x^2)^2}\,dx \qquad \textbf{Answer: } \frac18\ln\frac53-\frac{1}{20}$$

### H066 · Caltech 2025 Final (Hard) #6 [N]
$$\int_0^1\arctan(x^2-x+1)\,dx \qquad \textbf{Answer: } \ln 2$$

### H067 · Caltech 2025 Final (Hard) #7 [N]
$$\int_0^{\infty}e^{-x^2}\cos(2x)\,dx \qquad \textbf{Answer: } \frac{\sqrt\pi}{2e}$$

### H068 · Caltech 2025 Final (Hard) #8 [N]
$$\int\frac{dx}{2+2\sin x+\cos x} \qquad \textbf{Answer: } \ln\left|\frac{\tan(x/2)+1}{\tan(x/2)+3}\right|+C$$

### H069 · Caltech 2025 Final (Hard) #9 [A]
$$\int\prod_{k=1}^{n-1}\sqrt{2x^2-2x^2\cos\!\left(\frac{2\pi k}{n}\right)}\,dx \qquad \textbf{Answer: } x^n+C$$

## Bonn Integration Bee (Bibee) 2026 (5)

### H070 · Bonn 2026 #9 [N]
$$\int_0^{\pi}\left(\frac{1}{1+\tan x}+\frac{1}{1+\cot x}\right)dx \qquad \textbf{Answer: } \pi$$

### H071 · Bonn 2026 #15 [N]
$$\int_0^{\sqrt{2026}}\frac{(2x)^2}{\sqrt{2026-x^2}}\,dx \qquad \textbf{Answer: } 2026\pi$$

### H072 · Bonn 2026 #18 [N]
$$\int_0^1\prod_{n=1}^{\infty}(1+x)^{1/n^2}\,dx \qquad \textbf{Answer: } \frac{2^{\pi^2/6+1}-1}{\pi^2/6+1}$$

### H073 · Bonn 2026 #20 [N]
$$\int_1^{\infty}\frac{dx}{\lceil x\rceil^2} \qquad \textbf{Answer: } \frac{\pi^2}{6}-1$$

### H074 · Bonn 2026 #21 [N]
$$\int_0^{\pi/2}e^{ix}\cos x\,dx \qquad \textbf{Answer: } \frac{\pi}{4}+\frac{i}{2}$$

## Chulalongkorn University Integration Bee 2025 — Final Round (6)

### H075 · Chulalongkorn 2025 Final R1 #3 [N]
$$\int_0^{e}\sin(4\arctan x)\,dx \qquad \textbf{Answer: } 4-\frac{4}{e^2+1}-2\ln(e^2+1)$$

### H076 · Chulalongkorn 2025 Final R2 #1 [A]
$$\int_0^{2\pi}\left(\sum_{k=1}^{99}k\cos kx\right)\left(\sum_{l=1}^{99}l\cos l^2x\right)dx \qquad \textbf{Answer: } 2025\pi$$

### H077 · Chulalongkorn 2025 Final R2 #5 [N]
$$\lim_{n\to\infty}n\int_0^{\pi/4}\tan^{2n}x\,dx \qquad \textbf{Answer: } \frac14$$

### H078 · Chulalongkorn 2025 Final R2 #7 [A]
$$\int_0^{2568\pi}x\cos^{2025}x\prod_{k=1}^{\infty}\cos\!\left(\frac{x}{2^k}\right)dx \qquad \textbf{Answer: } 0$$

### H079 · Chulalongkorn 2025 Final R3 #2 [A]
$$\int_0^{\pi}\frac{\sin^2(2^{2025}\pi x)}{\sin^2x}\,dx \qquad \textbf{Answer: } 2^{2025}\pi$$

### H080 · Chulalongkorn 2025 Final R3 #5 [A]
$$\int_1^{e^{2025}}\lceil\ln x\rceil\,dx \qquad \textbf{Answer: } 2025e^{2025}-\frac{e^{2025}-1}{e-1}$$

## Singapore Precollegiate Integration Bee 2026 — Round 2 (20)

### H081 · Singapore 2026 R2 Groups R1 #2 [N]
$$\int_0^{\pi}\frac{\sin\!\left((2026+\frac12)x\right)}{\sin(x/2)}\,dx \qquad \textbf{Answer: } \pi$$

### H082 · Singapore 2026 R2 Groups R2 #3 [N]
$$\int_0^{\infty}\sin^{-1}\!\left(\frac{1}{1+x^2}\right)dx \qquad \textbf{Answer: } \ln(3+2\sqrt2)$$

### H083 · Singapore 2026 R2 Groups R3 #1 [A]
$$\int\frac{\ln x+\ln\pi}{(\ln x)^{1-\ln\pi}}\,dx \qquad \textbf{Answer: } x(\ln x)^{\ln\pi}+C$$

### H084 · Singapore 2026 R2 Groups R3 #2 [N]
$$\int_0^1\big(\sin^{-1}x+2\sin^{-1}x\cos^{-1}x+\cos^{-1}x\big)dx \qquad \textbf{Answer: } 4-\frac{\pi}{2}$$

### H085 · Singapore 2026 R2 Groups R4 #1 [N]
$$\int_0^1\frac{\ln x}{\sqrt{1-x}}\,dx \qquad \textbf{Answer: } \ln 16-4$$

### H086 · Singapore 2026 R2 Groups R4 #3 [N]
$$\int_0^{\sqrt3}\frac{x^2+2}{\sqrt{x^2+1}}\,dx \qquad \textbf{Answer: } \sqrt3+\frac32\ln(2+\sqrt3)$$

### H087 · Singapore 2026 R2 Groups R5 #1 [N]
$$\int (x+1)e^x\ln x\,dx \qquad \textbf{Answer: } xe^x\ln x-e^x+C$$

### H088 · Singapore 2026 R2 Groups R5 #2 [A]
$$\int\frac{x^2+2x+2}{x(x^4+4)}\,dx \qquad \textbf{Answer: } \frac12\ln x-\frac14\ln(x^2-2x+2)+\frac12\tan^{-1}(x-1)+C$$

### H089 · Singapore 2026 R2 QF #1 [A]
$$\int_0^{2025}\{x\}\,d(\cos\pi x) \qquad \textbf{Answer: } -1$$

### H090 · Singapore 2026 R2 QF #2 [N]
$$\int_0^{\infty}\left(\frac{3x^2-9x+1}{x^3-x+1}\right)^2dx \qquad \textbf{Answer: } 26$$

### H091 · Singapore 2026 R2 QF #3 [A]
$$\int_1^{2027}\prod_{k=1}^{2026}(x-k)\sum_{j=1}^{2026}\frac{1}{x-j}\,dx \qquad \textbf{Answer: } 2026!$$

### H092 · Singapore 2026 R2 QF #4 [N]
$$\int_0^{x}\frac{\sqrt{2-y^2+2\sqrt{1-y^2}}-\sqrt{2-y^2-2\sqrt{1-y^2}}}{\sqrt{1-y^2}}\,dy\ (0<x<1) \qquad \textbf{Answer: } 2x$$

### H093 · Singapore 2026 R2 SF1 #2 [A]
$$\int_1^2\left(1+\frac2x+\frac{4}{x^2}-\frac{25}{(1+x)^2}\right)dx \qquad \textbf{Answer: } \ln 4-\frac76$$

### H094 · Singapore 2026 R2 SF1 #4 [N]
$$\int_0^{\pi/2}\frac{\sin^3\theta}{(1+\sin\theta)^4}\,d\theta \qquad \textbf{Answer: } \frac{2}{35}$$

### H095 · Singapore 2026 R2 SF2 #1 [N]
$$\int_4^{\infty}\frac{dx}{(x^2-4x+3)(x^2-4x+4)(x^2-4x+5)} \qquad \textbf{Answer: } -\frac12+\frac{\pi}{4}+\frac{\ln 3}{4}-\frac{\tan^{-1}2}{2}$$

### H096 · Singapore 2026 R2 SF2 #3 [N]
$$\lim_{n\to\infty}\int_0^{n+1}\frac{x}{n^2+\lfloor x\rfloor^2}\,dx \qquad \textbf{Answer: } \frac12\ln 2$$

### H097 · Singapore 2026 R2 Third-Place #3 [N]
$$\int_0^1\!\!\int_0^1\frac{dx\,dy}{(1+x^2)(2+x^2+y^2)} \qquad \textbf{Answer: } \frac{\pi^2}{32}$$

### H098 · Singapore 2026 R2 Third-Place #4 [N]
$$\int_0^{\pi/2}\frac{dx}{\cos^6x+\sin^6x} \qquad \textbf{Answer: } \pi$$

### H099 · Singapore 2026 R2 Grand Final #3 [N]
$$\int_0^{\infty}\frac{\tan^{-1}\!\left(\frac{x}{1+2x^2}\right)}{x}\,dx \qquad \textbf{Answer: } \frac{\pi}{2}\ln 2$$

### H100 · Singapore 2026 R2 Grand Final #5 [N]
$$\int_1^{\infty}\frac{\ln^3 x}{x(1-x)^2}\,dx \qquad \textbf{Answer: } 6\zeta(3)-\frac{\pi^4}{15}$$

## Provenance

| Source | Problem file(s) |
|---|---|
| MIT Finals 2022–2026 | `01_MIT/<year>/Final.pdf` |
| MIT Semifinals 2022–2026 | `01_MIT/<year>/Semifinal.pdf` |
| Lisbon 2025 | `23_Lisbon/2025/{Semifinal,Final}.pdf` |
| UKUIB R3 2024/25 | `02_UKUIB/2024/Final-Tournament-Solutions.pdf` |
| Caltech 2025 Final (Hard) | `07_Caltech/2025/Final-Hard-Solutions.pdf` |
| Bonn 2026 | `06_Bonn/2026/Problems-with-Solutions.pdf` |
| Chulalongkorn 2025 | `22_Chulalongkorn/2025/Final-Round.pdf` |
| Singapore 2026 R2 | `13_Singapore/2026/Round2-All-Questions-and-Answers.pdf` |

Machine-readable copy: [`hard-set.json`](hard-set.json). Copyright: © MIT Integration Bee / MIT —
see [`ATTRIBUTION.md`](ATTRIBUTION.md); reproduced for non-commercial research with attribution.
