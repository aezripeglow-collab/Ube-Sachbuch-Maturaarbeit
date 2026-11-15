---
tags: [math, differential-calculus, exam]
course: MAT_G23f (T. Turini, G4)
exam: Short test, Monday 16.11.2026
---

# Differential Calculus 2 – Short Test Summary

> [!warning] Test logistics (from TT's message)
> - The test is **online** → bring your **laptop/tablet** (charged!).
> - Update **Safe Exam Browser (SEB)** to the **newest version** *before* Monday.
> - **No calculator, no formulae booklet.** → You must know every rule and derivative below **by heart**, and the exact values (trig, $e$, $\ln$).
> - Focus: **concepts + derivatives**.

---

## 0. Must-know cheat table (memorise this first)

| $f(x)$ | $f'(x)$ | Notes |
|---|---|---|
| $c$ (constant) | $0$ | |
| $x^n$ ($n \in \mathbb{R}$) | $n\,x^{n-1}$ | power rule |
| $\sqrt{x}=x^{1/2}$ | $\dfrac{1}{2\sqrt{x}}$ | |
| $\dfrac{1}{x}=x^{-1}$ | $-\dfrac{1}{x^2}$ | |
| $\sqrt[3]{x}=x^{1/3}$ | $\dfrac{1}{3\sqrt[3]{x^2}}$ | |
| $\sin x$ | $\cos x$ | |
| $\cos x$ | $-\sin x$ | ⚠ minus! |
| $\tan x$ | $\dfrac{1}{\cos^2 x} = 1+\tan^2 x$ | |
| $\cot x$ | $-\dfrac{1}{\sin^2 x} = -(1+\cot^2 x)$ | |
| $e^x$ | $e^x$ | the function is its own derivative |
| $b^x$ | $\ln(b)\cdot b^x$ | $b>0,\ b\neq 1$ |
| $\ln x$ | $\dfrac{1}{x}$ | $x>0$ |
| $\log_b x$ | $\dfrac{1}{\ln(b)\cdot x}$ | $\log x = \log_{10} x \Rightarrow \frac{1}{\ln(10)\,x}$ |
| $\sinh x = \frac12(e^x-e^{-x})$ | $\cosh x$ | |
| $\cosh x = \frac12(e^x+e^{-x})$ | $\sinh x$ | |

**Chain-rule versions (most common in tests):**
- $(e^{g(x)})' = g'(x)\,e^{g(x)}$  e.g. $(e^{4x-1})' = 4e^{4x-1}$
- $(b^{g(x)})' = \ln(b)\, g'(x)\, b^{g(x)}$
- $(\ln g(x))' = \dfrac{g'(x)}{g(x)}$
- $(\sin g(x))' = g'(x)\cos g(x)$, $(\cos g(x))' = -g'(x)\sin g(x)$
- $(\tan g(x))' = \dfrac{g'(x)}{\cos^2 g(x)}$
- $\big((g(x))^n\big)' = n\,(g(x))^{n-1}\cdot g'(x)$

---

## 1. Repetition – Differential Calculus 1

### 1.1 Difference quotient vs. derivative (Def. 1.1)
Let $f$ have domain $D_f$, with $(x_0, x_0+\Delta x) \subseteq D_f$.

- **Difference quotient / average rate of change** of $f$ on $[x_0, x_0+\Delta x]$:
$$\frac{f(x_0+\Delta x)-f(x_0)}{(x_0+\Delta x)-x_0}=\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$$
  **Geometrically:** slope of the **secant** $s$ through $(x_0, f(x_0))$ and $(x_0+\Delta x, f(x_0+\Delta x))$.

- **Derivative / instantaneous rate of change** at $x_0$: let $\Delta x \to 0$ (one point slides towards the other):
$$f'(x_0)=\lim_{\Delta x\to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$$
  **Geometrically:** slope of the **tangent** $t$ to the graph at $x_0$.

### 1.2 Tangent line $t(x)=ax+b$ at $x_0$ – recipe
1. $y_0 = f(x_0)$
2. $a = f'(x_0)$ → $t(x) = f'(x_0)\cdot x + b$
3. Plug in $(x_0, y_0)$ and solve for $b$:
$$f(x_0)=f'(x_0)\cdot x_0+b \iff b=f(x_0)-f'(x_0)\cdot x_0$$

(Equivalent short form: $t(x) = f'(x_0)(x - x_0) + f(x_0)$.)

### 1.3 Differentiability (Def. 1.2)
$f: D_f \to \mathbb{R}$, $I \subseteq D_f$ open interval, $x_0 \in I$.
- $f$ is **differentiable at $x_0$** if $f'(x_0)$ **exists**; $f$ is **differentiable** if it is differentiable on its **whole domain**.
- Then $f' : D_f \to \mathbb{R},\ x \mapsto f'(x)$ is the **derivative function / first derivative**: it sends every $x$ to the **slope of the tangent** to $f$ at $x$.

> [!tip] Rule of thumb
> Shape changes **abruptly** ("edge"/kink) at a point → **not** differentiable there.
> Shape changes **steadily** (smooth) → differentiable.

- **Ex. 1e:** $|x|$-shaped graph (V with a kink at 0) → **not differentiable** at $x=0$. Parabola → differentiable everywhere. Hyperbola $\frac1x$ → $x=0$ isn't in the domain, so it **is** differentiable on its whole domain.

> [!question] Ex. 1c – "derivative of $f$ at $x_0$" vs. "derivative of $f$"
> $f'(x_0)$ is a **number** (slope at one point). $f'$ is a **function** (gives the slope at every $x$).

### 1.4 Rules of derivation ($f,g$ differentiable, $c\in\mathbb{R}$, $n\in\mathbb{Q}$)
- **Power rule:** $(x^n)' = n x^{n-1}$
- **Sum rule:** $(f+g)' = f' + g'$
- **Factor rule:** $(c\cdot f)' = c\cdot f'$
- **Product rule:** $(f\cdot g)' = f'\cdot g + f\cdot g'$
- **Quotient rule:** $\left(\dfrac{f}{g}\right)' = \dfrac{f'\cdot g - f\cdot g'}{g^2}$ for $g\neq 0$  *("low d-high minus high d-low, over low squared")*
- **Chain rule:** $(u\circ v)'(x) = u'(v(x))\cdot v'(x)$  *(outer derivative × inner derivative)*

### 1.5 Derivative from the limit (h-method / Ex. 1b, 1d)
Example $f(x)=x^2-3x+1$ at $x_0$:
$$\frac{(x_0+\Delta x)^2-3(x_0+\Delta x)+1-(x_0^2-3x_0+1)}{\Delta x}=\frac{2x_0\Delta x+\Delta x^2-3\Delta x}{\Delta x}=2x_0+\Delta x-3 \xrightarrow{\Delta x\to0} 2x_0-3$$
Steps: expand → cancel → factor out $\Delta x$ → cancel $\Delta x$ → let $\Delta x\to 0$.

Results of Ex. 1b: $f(x)=x$: $f'(2)=1$; $-3x+1$: $f'(-4)=-3$; $mx+q$: $f'(1)=m$; $2x^2-3$: $f'(-2)=-8$; $x^2-3x+1$: $f'(-1)=-5$.
Ex. 1d: $(3x^2-4x+1)'=6x-4$; $(x^3-4)'=3x^2$; $\left(\frac{1}{3x-2}\right)'=\frac{-3}{(3x-2)^2}$.
For $\frac{1}{3x-2}$: put the two fractions on a common denominator → numerator $-3\Delta x$.

### 1.6 Second derivative & curvature (Def. 1.3)
$$f''(x) := (f')'(x)$$
On an interval $I$ (for all $x\in I$):
- $f''(x) < 0$ → **concave down** (right curve, clockwise) ∩
- $f''(x) > 0$ → **concave up** (left curve, anti-clockwise) ∪

### 1.7 Stationary points, extrema (Def. 1.4)
- **Stationary point** $S=(x_S,y_S)$: $f'(x_S)=0$ (horizontal tangent).
- **Local maximum** at $x_M$: $f'(x_M)=0$ and $f''(x_M)<0$.
- **Local minimum** at $x_m$: $f'(x_m)=0$ and $f''(x_m)>0$.
- Graphically: local max/min = greatest/smallest value of $f$ **in a small region** of the domain.
- **Global** max/min = greatest/smallest value on the **whole** domain (check boundaries & behaviour at infinity too!).
- Maxima and minima together = **extrema**.
- If $f'(x_0)=0$ **and** $f''(x_0)=0$ the test says nothing → check the **sign change of $f'$** (sign change → extremum; no sign change → **saddle/terrace point**).

### 1.8 Connection between $f$, $f'$, $f''$
- $x_0$ local min/max of $f$ ⟹ $f'(x_0)=0$.
- $f$ **increasing** ⟺ $f'$ **positive**; $f$ **decreasing** ⟺ $f'$ **negative**.
- $x_0$ **inflection point** ⟹ curvature changes (right curve ↔ left curve) and $f''(x_0)=0$.
  Sufficient check: $f''(x_0)=0$ **and** $f'''(x_0)\neq 0$ (or $f''$ changes sign).
- Where $f$ increases, $f'$ is **maximal** where $f$ changes from concave **up → down** (inflection point). Where $f$ decreases, $f'$ is **minimal** where $f$ changes from concave **down → up**.
  ⟹ **Inflection points of $f$ = extrema of $f'$.**

**Fill-in-the-dots (Ex. 1g):**
- Extrema of a graph are the points at which **the graph changes from increasing to decreasing (or vice versa); there $f'=0$ (horizontal tangent)**.
- An inflection point is a point at which **the curvature changes (concave up ↔ concave down); there $f''=0$ and the slope is extremal**.
- If $f$ is increasing/decreasing, then $f'$ is **positive/negative**.

### 1.9 Sketching $f'$ from the graph of $f$ (Ex. 1i)
- Extrema of $f$ → **zeros** of $f'$.
- $f$ rising → $f'$ above the $x$-axis; $f$ falling → $f'$ below.
- Inflection points of $f$ → **extrema** of $f'$.
- Straight line $f$ (slope $m$) → $f'$ is the **constant** line $y=m$.
- Cubic $f$ (like Ex. 1h/1i) → $f'$ is a **parabola**.

### 1.10 Angle of intersection (Def. 1.5)
The angle of intersection of two graphs = angle $\alpha$ between their **tangent lines** at the intersection point $I=(x_I,y_I)$.

With $t_f(x)=ax+b$, $t_g(x)=mx+q$ (i.e. $a=f'(x_I)$, $m=g'(x_I)$):
$$\alpha_f=\tan^{-1}(a)=\tan^{-1}(f'(x_I)),\quad \alpha_g=\tan^{-1}(m)=\tan^{-1}(g'(x_I)),\quad \alpha=|\alpha_f-\alpha_g|$$
Alternative formula:
$$\alpha=\left|\tan^{-1}\!\left(\frac{a-m}{1+am}\right)\right| = \left|\tan^{-1}\!\left(\frac{\tan\alpha_f-\tan\alpha_g}{1+\tan\alpha_f\tan\alpha_g}\right)\right|$$
- If $1+am=0$ the tangents are **perpendicular** → $\alpha=90°$.
- If $|\alpha_f-\alpha_g|>90°$, the intersection angle is usually given as $180°-|\alpha_f-\alpha_g|$ (the acute one).

**Recipe:** (1) solve $f(x)=g(x)$ → $x_I$; (2) slopes $f'(x_I)$, $g'(x_I)$; (3) formula.

Example (Ex. 1j) $f=x^2$, $g=(x-2)^2$: $x_I=1$, slopes $2$ and $-2$ → $\tan\alpha=\left|\frac{4}{1-4}\right|=\frac43$ → $\alpha\approx 53.1°$.

---

## 2. Derivatives of trigonometric functions

Recall (DC1): we studied **polynomial** $a_nx^n+\dots+a_1x+a_0$ and **rational** functions (quotients of polynomials), all coefficients real. Now: trig, exp, log.

### 2.1 Results
$$(\sin x)'=\cos x \qquad (\cos x)'=-\sin x$$
**Graphically (Discovery 1):** slope of $\sin$ is $1$ at $0$, $0$ at $\frac\pi2$, $-1$ at $\pi$ … → that's the $\cos$ curve. Slope of $\cos$ is $0$ at $0$, $-1$ at $\frac\pi2$, $0$ at $\pi$, $1$ at $\frac{3\pi}2$ → that's $-\sin$.

### 2.2 Proof of $(\sin x)' = \cos x$ (know it!)
$$\sin'(x)=\lim_{\Delta x\to0}\frac{\sin(x+\Delta x)-\sin x}{\Delta x}$$
Addition formula $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$:
$$=\lim_{\Delta x\to0}\frac{\sin x\cos\Delta x+\cos x\sin\Delta x-\sin x}{\Delta x}=\lim\frac{\sin x(\cos\Delta x-1)+\cos x\sin\Delta x}{\Delta x}$$
$$=\sin x\cdot\lim_{\Delta x\to0}\frac{\cos\Delta x-1}{\Delta x}+\cos x\cdot\lim_{\Delta x\to0}\frac{\sin\Delta x}{\Delta x}\quad(\star)$$
Need two limits: (1) $\lim\frac{\cos\Delta x-1}{\Delta x}$, (2) $\lim\frac{\sin\Delta x}{\Delta x}$. (1) is computed using (2), so prove (2) first.

**Limit (2): $\lim_{x\to0}\frac{\sin x}{x}=1$** — unit circle, $x\in[0,\frac\pi2]$ in **radians** (so the arc length is $x$):
$$\sin x\le x\le\tan x=\frac{\sin x}{\cos x}$$
Divide by $\sin x$: $1\le\frac{x}{\sin x}\le\frac{1}{\cos x}$. Take reciprocals (flip the inequalities): $1\ge\frac{\sin x}{x}\ge\cos x$.
Let $x\to0^+$: $1\ge\lim\frac{\sin x}{x}\ge\lim\cos x=1$ ⟹ $\lim_{x\to0}\frac{\sin x}{x}=1$ (squeeze/sandwich).

Into $(\star)$: $\sin'(x)=\sin x\cdot\lim\frac{\cos\Delta x-1}{\Delta x}+\cos x\quad(\star\star)$

**Limit (1) (Ex. 2): $\lim_{x\to0}\frac{\cos x-1}{x}=0$** — expand by $(\cos x+1)$ and use $\sin^2x+\cos^2x=1$:
$$\frac{\cos x-1}{x}\cdot\frac{\cos x+1}{\cos x+1}=\frac{\cos^2x-1}{x(\cos x+1)}=\frac{-\sin^2x}{x(\cos x+1)}=-\underbrace{\frac{\sin x}{x}}_{\to1}\cdot\underbrace{\frac{\sin x}{\cos x+1}}_{\to\frac{0}{2}=0}\to0$$
Into $(\star\star)$: $\sin'(x)=\sin x\cdot0+\cos x=\cos x$. ∎ (Similar proofs work for any angle $x$.)

### 2.3 Proof of $(\cos x)'=-\sin x$ (Ex. 3*)
$\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$:
$$\cos'(x)=\lim\frac{\cos x\cos\Delta x-\sin x\sin\Delta x-\cos x}{\Delta x}=\cos x\cdot\underbrace{\lim\frac{\cos\Delta x-1}{\Delta x}}_{0}-\sin x\cdot\underbrace{\lim\frac{\sin\Delta x}{\Delta x}}_{1}=-\sin x$$

### 2.4 $\tan$ and $\cot$ (Ex. 4) – quotient rule
$$(\tan x)'=\left(\frac{\sin x}{\cos x}\right)'=\frac{\cos x\cos x-\sin x(-\sin x)}{\cos^2x}=\frac{\cos^2x+\sin^2x}{\cos^2x}=\frac{1}{\cos^2x}=1+\tan^2x$$
$$(\cot x)'=\left(\frac{\cos x}{\sin x}\right)'=\frac{-\sin^2x-\cos^2x}{\sin^2x}=-\frac{1}{\sin^2x}=-(1+\cot^2x)$$

### 2.5 Higher derivatives (Ex. 5) – period 4
- $\sin \to \cos \to -\sin \to -\cos \to \sin$
- $\cos \to -\sin \to -\cos \to \sin \to \cos$
- The 4th derivative is the function again ⟹ $f^{(n+4)}=f^{(n)}$.

### 2.6 Worked examples
- **Ex. 2.1:** $(x\cos x)'=1\cdot\cos x+x\cdot(-\sin x)=\cos x-x\sin x$
- **Ex. 6:**
  - a) $(3x^2\sin x)'=6x\sin x+3x^2\cos x$
  - b) $\left(\frac{x^2\sin x}{3x-2}\right)'=\frac{(2x\sin x+x^2\cos x)(3x-2)-3x^2\sin x}{(3x-2)^2}$
  - c) $\left(\frac{x\sin x}{\cos x}\right)'=(x\tan x)'=\tan x+\frac{x}{\cos^2x}=\frac{\sin x\cos x+x}{\cos^2x}$
  - d) $(\tan^3x)'=3\tan^2x\cdot\frac{1}{\cos^2x}$ (outer: power; inner: tan)
  - e) $(\tan(x^3))'=\frac{1}{\cos^2(x^3)}\cdot3x^2$ (outer: tan; inner: $x^3$)
  - ⚠ Know the difference: $\tan^3x=(\tan x)^3$ vs. $\tan(x^3)$.
- **Ex. 2.2:** tangent to $\tan x$ at $P=(\frac\pi4,1)$: slope $\frac{1}{\cos^2(\pi/4)}=\frac{1}{1/2}=2$ → $t(x)=2x+1-\frac\pi2$.
- **Ex. 7:** tangent to $\cos x$ at $P=(\frac\pi2,0)$: slope $-\sin\frac\pi2=-1$ → $t(x)=-x+\frac\pi2$.
- **Ex. 8:** stationary points of $\sin^2x$ on $[0,2\pi)$: $f'=2\sin x\cos x=\sin(2x)=0$ → $x=0,\frac\pi2,\pi,\frac{3\pi}2$ → points $(0,0),(\frac\pi2,1),(\pi,0),(\frac{3\pi}2,1)$ (minima at $0,\pi$; maxima at $\frac\pi2,\frac{3\pi}2$).
- **Ex. 9:** domain of $\frac{4\sin x}{1-\cos x}$: need $\cos x\neq1$ → $D=\mathbb{R}\setminus\{2k\pi \mid k\in\mathbb{Z}\}$.

### 2.7 Exact trig values (no calculator!)
| $x$ | $0$ | $\frac\pi6$ (30°) | $\frac\pi4$ (45°) | $\frac\pi3$ (60°) | $\frac\pi2$ (90°) | $\pi$ | $\frac{3\pi}2$ |
|---|---|---|---|---|---|---|---|
| $\sin x$ | $0$ | $\frac12$ | $\frac{\sqrt2}2$ | $\frac{\sqrt3}2$ | $1$ | $0$ | $-1$ |
| $\cos x$ | $1$ | $\frac{\sqrt3}2$ | $\frac{\sqrt2}2$ | $\frac12$ | $0$ | $-1$ | $0$ |
| $\tan x$ | $0$ | $\frac{1}{\sqrt3}$ | $1$ | $\sqrt3$ | — | $0$ | — |

$\tan^{-1}(1)=45°$, $\tan^{-1}(\sqrt3)=60°$, $\tan^{-1}(\frac1{\sqrt3})=30°$. Useful: $\sin^2x+\cos^2x=1$, $2\sin x\cos x=\sin 2x$.

**Learning goals ch. 2:** know derivatives of sin, cos, tan; determine derivatives of sin/cos **graphically and algebraically**; apply all rules to terms with all function types.

---

## 3. Derivative of the exponential function

### 3.1 Natural exponential function (Thm 3.1)
$$(e^x)'=e^x$$
**Proof:**
$$(e^x)'=\lim_{\Delta x\to0}\frac{e^{x+\Delta x}-e^x}{\Delta x}=\lim\frac{e^x(e^{\Delta x}-1)}{\Delta x}=e^x\cdot\lim_{\Delta x\to0}\frac{e^{\Delta x}-1}{\Delta x}$$
Ex. 10 (table of values) shows $\lim_{\Delta x\to0}\frac{e^{\Delta x}-1}{\Delta x}=1$:

| $\Delta x$ | $0.1$ | $0.01$ | $0.001$ | $0.0001$ |
|---|---|---|---|---|
| $\frac{e^{\Delta x}-1}{\Delta x}$ | $1.0517$ | $1.0050$ | $1.0005$ | $1.00005$ |

| $\Delta x$ | $-0.1$ | $-0.01$ | $-0.001$ | $-0.0001$ |
|---|---|---|---|---|
| $\frac{e^{\Delta x}-1}{\Delta x}$ | $0.9516$ | $0.9950$ | $0.9995$ | $0.99995$ |

Both sides → 1, so $(e^x)'=e^x\cdot1=e^x$. ∎
(The script's last line says "$(e^x)'=1$" – that's a typo; it's the **limit** that equals 1.)

### 3.2 General exponential function (Thm 3.2)
For $b\in\mathbb{R}^+\setminus\{1\}$, $f(x)=b^x$ is differentiable everywhere and
$$(b^x)'=\ln(b)\cdot b^x$$
**Proof:** write in terms of $e$: $b^x=(e^{\ln b})^x=e^{x\ln b}$. Chain rule (inner derivative $\ln b$):
$$(b^x)'=e^{x\ln b}\cdot\ln b=\ln(b)\cdot b^x\ ∎$$

### 3.3 Worked examples
- **Ex. 3.3:** $(x\cdot2^x)'=2^x+x\ln2\cdot2^x=2^x(1+x\ln2)$
- **Ex. 11:** a) $(5^x)'=\ln5\cdot5^x$  b) $(3^{-5x^2})'=\ln3\cdot(-10x)\cdot3^{-5x^2}$  c) $\left(\frac{2^x}{x}\right)'=\frac{2^x(x\ln2-1)}{x^2}$  d) $(e^{4x-1})'=4e^{4x-1}$
- **Ex. 12:** a) $e^x+\cos x$  b) $(e^x\sin x)'=e^x(\sin x+\cos x)$  c) $6e^x$  d) $(-3x^3+\frac{e^x}5)'=-9x^2+\frac{e^x}5$  e) $\left(\frac{e^x}{x}\right)'=\frac{e^x(x-1)}{x^2}$  f) $\left(\frac{x^2}{e^{\sin x}}\right)'=(x^2e^{-\sin x})'=(2x-x^2\cos x)e^{-\sin x}$
- **Ex. 13 (hyperbolic):** $(\sinh x)'=\frac12(e^x+e^{-x})=\cosh x$, $(\cosh x)'=\frac12(e^x-e^{-x})=\sinh x$ (note $(e^{-x})'=-e^{-x}$).

### 3.4 Exp/log rules you need for simplifying
$e^0=1$, $e^{a+b}=e^ae^b$, $(e^a)^b=e^{ab}$, $e^{-a}=\frac1{e^a}$, $e^{\ln x}=x$, $\ln(e^x)=x$, $\ln1=0$, $\ln e=1$, $\ln(ab)=\ln a+\ln b$, $\ln\frac ab=\ln a-\ln b$, $\ln(a^r)=r\ln a$, $\log_bx=\frac{\ln x}{\ln b}$, $b^x=e^{x\ln b}$. Rough values: $e\approx2.718$, $e^2\approx7.39$, $\ln2\approx0.69$, $\ln3\approx1.10$.

**Learning goals ch. 3:** know derivatives of $e^x$ and $b^x$; **be able to prove** $(e^x)'=e^x$ and $(b^x)'=\ln(b)b^x$; apply all rules.

---

## 4. Derivative of the logarithmic function

### 4.1 Repetition: inverse function
An inverse $f^{-1}$ "undoes" $f$. It exists **iff $f$ is bijective**.
$$f^{-1}(f(x))=x\ \ \forall x\in D,\qquad f(f^{-1}(x))=x\ \ \forall x\in\text{range}$$

### 4.2 Derivative of $f^{-1}$
From $f(f^{-1}(x))=x$, differentiate both sides (chain rule):
$$f'(f^{-1}(x))\cdot(f^{-1})'(x)=1\iff (f^{-1})'(x)=\frac{1}{f'(f^{-1}(x))}$$

- **Ex. 4.1:** $f(x)=x^2$ on $[0,\infty)\to[0,\infty)$ is bijective, $f^{-1}(x)=\sqrt x$, $f'(x)=2x$:
  $(\sqrt x)'=\frac{1}{2\sqrt x}$.
- **Ex. 14:** $f(x)=x^3$, $f^{-1}(x)=\sqrt[3]x$, $f'(x)=3x^2$: $(\sqrt[3]x)'=\frac{1}{3(\sqrt[3]x)^2}=\frac{1}{3x^{2/3}}$.

### 4.3 Logarithm
$\log_b:(0,\infty)\to\mathbb{R}$ and $\exp_b:\mathbb{R}\to(0,\infty),\ x\mapsto b^x$ are **inverse** to each other. For all $b\in\mathbb{R}^+\setminus\{1\}$, $x\in\mathbb{R}^+$:
$$(\log_b x)'=\frac{1}{\ln(b)\,x}\qquad\text{in particular}\qquad(\ln x)'=\frac1x$$
**Proof:** $f(x)=b^x$, $f'(x)=\ln(b)\,b^x$, $f^{-1}(x)=\log_bx$:
$$(\log_bx)'=\frac{1}{f'(f^{-1}(x))}=\frac{1}{\ln(b)\cdot b^{\log_bx}}=\frac{1}{\ln(b)\cdot x}\ ∎$$
(For $\ln$: $b=e$, $\ln e=1$.)

### 4.4 Power rule for real exponents (Ex. 25)
$x^r=e^{r\ln x}$ ⟹ $(x^r)'=e^{r\ln x}\cdot\frac rx=x^r\cdot\frac rx=r\,x^{r-1}$.

### 4.5 Worked examples
- **Ex. 15:** a) $\ln(ex)=1+\ln x$ → $\frac1x$  b) $(-\log x)'=-\frac{1}{\ln(10)\,x}$  c) $\ln\frac{x-3}{x+1}=\ln(x-3)-\ln(x+1)$ → $\frac1{x-3}-\frac1{x+1}=\frac{4}{(x-3)(x+1)}$
- **Ex. 16:** zero of $e^x\ln x$ at $x=1$; $f'=e^x\ln x+\frac{e^x}x$, $f'(1)=e$ → $t(x)=ex-e$.

**Learning goals ch. 4:** know $(\log_bx)'$ **and its proof**; apply all rules.

---

## 5. Applications

### 5.1 Angle of intersection
- **Ex. 5.1:** $\ln(2x-1)=\ln(x+3)$ ⟹ $2x-1=x+3$ ⟹ $x=4$, $I=(4,\ln7)$. Slopes $\frac{2}{2x-1}=\frac27$, $\frac1{x+3}=\frac17$. $\tan\alpha=\frac{2/7-1/7}{1+2/49}=\frac{7}{51}$ → $\alpha\approx7.8°$.
- **Ex. 17:** $\sin x=\cos x$ on $[0,\frac\pi2]$ → $x=\frac\pi4$. Slopes $\cos\frac\pi4=\frac{\sqrt2}2$, $-\sin\frac\pi4=-\frac{\sqrt2}2$ → $\tan\alpha=\frac{\sqrt2}{1-\frac12}=2\sqrt2$ → $\alpha\approx70.5°$.
- **Ex. 20:** $e^{-\frac{x+1}2}=e^{-x^2}$ ⟹ $2x^2-x-1=0$ ⟹ $x=1$ or $x=-\frac12$. At $x=1$: $\tan\alpha=\frac{3e}{2(e^2+1)}$ ($\approx25.9°$); at $x=-\frac12$: $\tan\alpha=\frac{3e^{-1/4}}{2-e^{-1/2}}$ ($\approx59.2°$).
- **Ex. 26:** $3^x=2^{-x}$ ⟹ $6^x=1$ ⟹ $I=(0,1)$. Slopes $\ln3$ and $-\ln2$ → $\alpha=\tan^{-1}(\ln3)+\tan^{-1}(\ln2)\approx82.4°$.

### 5.2 Extreme value (optimisation) problems – recipe
1. Sketch, name variables.
2. **Target function** (what to max/min: area, cost, perimeter, distance).
3. **Constraint** (side condition) → eliminate a variable → target in **one** variable.
4. State the **domain** (e.g. $1<x<e$).
5. Derivative $=0$ → candidates.
6. Check max/min with $f''$ (and boundaries).
7. Answer the actual question (dimensions, point, value).

Examples:
- **Ex. 5.2:** rectangle under $e^{-2x}$: $A(x)=x\,e^{-2x}$, $A'=e^{-2x}(1-2x)=0$ → $x=\frac12$, $P=(\frac12,\frac1e)$, $A_{max}=\frac1{2e}$.
- **Ex. 1l (farmer):** front $x$ (15 CHF/m), depth $y$, $xy=200$. $C=15x+5x+2\cdot5y=20x+\frac{2000}x$, $C'=20-\frac{2000}{x^2}=0$ → $x=10$ m, $y=20$ m, cost 400 CHF.
- **Ex. 28:** $P=(x,2\ln x)$, rectangle from $x$ to $e$: perimeter $U=2(e-x)+2\cdot2\ln x$, $U'=-2+\frac4x=0$ → $x=2$, $P=(2,2\ln2)$ ($U''=-\frac4{x^2}<0$ → max).
- **Ex. 29:** vertical distance $d(x)=ex+5-\ln x$, $d'=e-\frac1x=0$ → $x=\frac1e$, $d=1+5+1=7$ units.
- **Ex. 23*:** shortest distance from $e^x$ to $y=3x-4$: tangent parallel to the line → $e^x=3$ → $P=(\ln3,3)$.

### 5.3 Curve sketching – checklist (Ex. 5.3 order)
1. **Domain** $D$ (+ vertical asymptotes where the denominator $=0$, or $\ln$ of $0$).
2. **Symmetry:** $f(-x)=f(x)$ → **even** (axis-symmetric to the $y$-axis); $f(-x)=-f(x)$ → **odd** (point-symmetric to the origin); else none.
3. **Intercepts:** zeros $f(x)=0$; $y$-intercept $f(0)$.
4. **Behaviour at infinity** $\lim_{x\to\pm\infty}f(x)$ → horizontal asymptotes. ($e^{-x}$ beats any polynomial: $x^ne^{-x}\to0$ as $x\to\infty$.)
5. **Extrema:** $f'=0$, classify with $f''$.
6. **Inflection points:** $f''=0$, check $f'''\neq0$.
7. Sketch.

**Ex. 5.3** $f(x)=(1-2x)e^{-x}$: $D=\mathbb{R}$; $f(-x)=(1+2x)e^x\neq\pm f(x)$ → no symmetry; zero $x=\frac12$, $f(0)=1$; $\lim_{x\to\infty}=0$, $\lim_{x\to-\infty}=+\infty$; $f'=\frac{2x-3}{e^x}$ → $x=\frac32$, $f''=\frac{5-2x}{e^x}$, $f''(\frac32)>0$ → **min** $(\frac32,-\frac2{e^{3/2}})$; $f''=0$ → $x=\frac52$, $f'''=\frac{2x-7}{e^x}\neq0$ → **inflection** $(\frac52,-\frac4{e^{5/2}})$.

**Tip – derivatives of $p(x)\,e^{-x}$:** always factor out $e^{-x}$: $(p\,e^{-x})'=(p'-p)\,e^{-x}$.

More results:
- **Ex. 1k** $3x^4-8x^3-6x^2+24x$: $f'=12(x+1)(x-1)(x-2)$ → min $(-1,-19)$, max $(1,13)$, min $(2,8)$; $f''=12(3x^2-4x-1)=0$ → inflection at $x=\frac{2\pm\sqrt7}3$.
- **Ex. 1m** $\frac{3x^2-1}{3x^2+1}$: $D=\mathbb{R}$, no VA; zeros $\pm\frac1{\sqrt3}$, $f(0)=-1$; **even**; $\to1$ at $\pm\infty$ (HA $y=1$); $f'=\frac{12x}{(3x^2+1)^2}$ → min $(0,-1)$; $f''=\frac{12(1-9x^2)}{(3x^2+1)^3}$ → inflection $(\pm\frac13,-\frac12)$.
- **Ex. 19** $\sin x(1+\sin x)$ on $[0,2\pi)$: no VA; zeros $0,\pi,\frac{3\pi}2$; $f(0)=0$; $f'=\cos x(1+2\sin x)$ → max $(\frac\pi2,2)$, local max $(\frac{3\pi}2,0)$, minima $(\frac{7\pi}6,-\frac14)$, $(\frac{11\pi}6,-\frac14)$; $2\pi$-periodic, so no limit at infinity.
- **Ex. 21** $\frac{e^x}x$: $D=\mathbb{R}\setminus\{0\}$, VA $x=0$ ($-\infty$ from the left, $+\infty$ from the right); $x\to\infty$: $+\infty$, $x\to-\infty$: $0$ (HA $y=0$); $f'=\frac{e^x(x-1)}{x^2}$ → min $(1,e)$.
- **Ex. 27** $5(x+1)e^{-x}$: zero $-1$, $f(0)=5$; $\to0$ ($x\to\infty$), $\to-\infty$ ($x\to-\infty$); $f'=-5xe^{-x}$ → max $(0,5)$; $f''=5(x-1)e^{-x}$ → inflection $(1,\frac{10}e)$.
- **Ex. 30a** $\frac{6-x}{\sqrt{9-x^2}}$: $D=(-3,3)$, VAs $x=\pm3$ (both $\to+\infty$), no zero, $f(0)=2$; $f'=\frac{6x-9}{(9-x^2)^{3/2}}$ → min $(\frac32,\sqrt3)$.
- **Ex. 30b** $\frac6{1+e^x}$: HAs $y=6$ ($x\to-\infty$) and $y=0$ ($x\to\infty$); $f(0)=3$; $f'=\frac{-6e^x}{(1+e^x)^2}<0$ → always decreasing; inflection $(0,3)$.
- **Ex. 30c** $(x-2)e^{x^2/2}$: zero $2$, $f(0)=-2$; $f'=(x-1)^2e^{x^2/2}\ge0$ → always increasing, **saddle point** $(1,-\sqrt e)$.

### 5.4 Determining function equations – translate conditions
| Condition | Equation |
|---|---|
| point $(x_0,y_0)$ on graph / zero at $x_0$ | $f(x_0)=y_0$ / $f(x_0)=0$ |
| extremum / stationary point at $x_0$ | $f'(x_0)=0$ |
| inflection point at $x_0$ | $f''(x_0)=0$ |
| slope $m$ / tangent slope at $x_0$ | $f'(x_0)=m$ |
| horizontal tangent | $f'(x_0)=0$ |

- **Ex. 1n** $ax^3+\frac{21}{20}x^2+cx-\frac{143}{40}$: $f''(4)=24a+\frac{21}{10}=0$ → $a=-\frac7{80}$; $f'(1)=3a+\frac{21}{10}+c=0$ → $c=-\frac{147}{80}$. (Heads-up: with these values $f''(1)>0$, so $x=1$ actually comes out as a **minimum**; the max is at $x=7$. The method is what counts.)
- **Ex. 18:** $f'=a\cos x+2$, $f'(\frac\pi3)=\frac a2+2=0$ → $a=-4$.
- **Ex. 22:** $(x^2+b)e^{ax}$, zero $(3,0)$ → $b=-9$; $f'(3)=6e^{3a}=6e$ → $a=\frac13$.
- **Ex. 24:** $f'=-2\sin x\cos x+t\cos x$, $f'(\frac\pi4)=-1+t\frac{\sqrt2}2=1$ → $t=2\sqrt2$.

**Learning goals ch. 5:** compute angles of intersection; solve extreme value problems; investigate properties and sketch graphs.

---

## 6. Common traps (no calculator!)
- $(\cos x)'=-\sin x$ (minus!), $(e^{-x})'=-e^{-x}$.
- Don't forget the **inner derivative** (chain rule): $(e^{3x})'=3e^{3x}$, not $e^{3x}$.
- $(b^x)'\neq x\,b^{x-1}$ — the power rule only works when the **exponent is constant**.
- $(\ln x)'=\frac1x$ only for $x>0$; simplify **before** differentiating ($\ln(ex)=1+\ln x$, $\ln\frac ab=\ln a-\ln b$).
- Quotient rule: order matters in the numerator ($f'g-fg'$), denominator **squared**.
- Angles: radians in derivatives ($\frac{\sin x}x\to1$ only in radians).
- $f'(x_0)=0$ alone does **not** guarantee an extremum (saddle point, e.g. $x^3$ at 0).
- Product $\neq$ product of derivatives: $(fg)'\neq f'g'$.
