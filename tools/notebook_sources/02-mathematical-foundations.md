# Practical 02 — Mathematical Foundations

## 1. Introduction

The mathematics in this course is not decoration: every statistic is a function of
the data, every density is an integrand, and every maximum-likelihood estimate is a
point where a derivative is zero. This practical makes those objects computable.

You will plot functions, differentiate and integrate them numerically, check a
numeric answer against a closed form, and see a series converge. Wherever a formula
can be checked two ways, it is checked two ways.

## 2. Learning objectives

By the end of this practical you can:

1. Plot \(f(x)=x^{2}\), \(e^{x}\) and \(\log x\) and state each domain.
2. Read and evaluate sigma notation, including \(\sum x_i^{2}\) versus \((\sum x_i)^{2}\).
3. Approximate a derivative with a central difference and compare it to the analytic one.
4. Approximate an integral with a Riemann sum and with Simpson's rule.
5. Explain why \(\sum_{k\ge 0}(1/2)^{k}=2\) and what that has to do with waiting times.
6. Apply the inclusion–exclusion rule to two events.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | arrays, `exp`, `log`, vectorised operations |
| `matplotlib` | function plots |
| `math` | factorials, logarithms, constants |

## 4. Concepts

### 4.1 Functions and their domains

A function maps each input to exactly one output. Three used constantly here:

| Function | Domain | Range | Appears in |
|---|---|---|---|
| \(x^{2}\) | all reals | \([0,\infty)\) | variance, least squares |
| \(e^{x}\) | all reals | \((0,\infty)\) | likelihoods, logistic models |
| \(\log x\) | \(x>0\) | all reals | log-likelihood, entropy, odds |

\(\log\) and \(\exp\) are inverses: \(\log(e^{x})=x\) and \(e^{\log x}=x\) for \(x>0\).
That inverse relationship is why a log-likelihood can be maximised in place of a
likelihood: the log is monotone, so it does not move the maximum.

### 4.2 Sigma notation

\[ \sum_{i=1}^{n}x_i = x_1+x_2+\cdots+x_n. \]

The index is a dummy: \(\sum_{i=1}^{n}x_i=\sum_{j=1}^{n}x_j\). Two distinct
quantities are easy to confuse:

\[ \sum_{i=1}^{n}x_i^{2}\ \neq\ \left(\sum_{i=1}^{n}x_i\right)^{2}. \]

For \(x=(1,2,3)\): the left side is \(1+4+9=14\), the right is \(6^{2}=36\). The
variance numerator uses the first, centred at the mean.

### 4.3 Derivative as a limit

\[ f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}
   \approx\frac{f(x+h)-f(x-h)}{2h}. \]

The **central** difference on the right is more accurate than the forward
difference, because the first-order error terms cancel. Statistics uses derivatives
to find maxima: at a maximum \(f'(x)=0\) and \(f''(x)<0\).

### 4.4 Integral as area

\[ \int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^{*})\,\Delta x. \]

A probability density integrates to 1 over its support, and probabilities are areas
under it. Simpson's rule approximates the integral by fitting parabolas to pairs of
intervals, which is far more accurate than rectangles for the same number of points.

### 4.5 Series

\[ \sum_{k=0}^{\infty}r^{k}=\frac{1}{1-r}\quad\text{for }|r|<1. \]

With \(r=1/2\) the sum is 2. That identity is the geometric distribution's
normalising constant: the probabilities \(p(1-p)^{k}\) sum to 1 because they form a
geometric series with ratio \(1-p\).

## 5. Formulas

\[ \frac{d}{dx}x^{3}=3x^{2},\qquad \int_0^1 x^{2}\,dx=\frac{1}{3},\qquad
   \int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}\,dz=1 \]

\[ \Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B) \]

\[ \text{Riemann: }\sum_{i=1}^{n}f(a+i\Delta x)\Delta x,\qquad
   \text{Simpson: }\frac{\Delta x}{3}\left[f_0+4f_1+2f_2+\cdots+4f_{n-1}+f_n\right] \]

## 6. Implementation

### 6.1 Three functions and their inverses

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 3, 200)

fig, axes = plt.subplots(1, 3, figsize=(11, 3.4))
axes[0].plot(x, x ** 2, color="#4c72b0")
axes[0].set(title=r"$f(x)=x^2$", xlabel="x", ylabel="f(x)")
axes[1].plot(x, np.exp(x), color="#55a868")
axes[1].set(title=r"$f(x)=e^x$", xlabel="x", ylabel="f(x)")
axes[2].plot(x, np.log(x), color="#c44e52")
axes[2].set(title=r"$f(x)=\log x$", xlabel="x", ylabel="f(x)")
for ax in axes:
    ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()
```

```python
# exp and log are inverses where log is defined.
values = np.array([0.5, 1.0, 2.5, 10.0])
print("x        :", values)
print("exp(log x):", np.exp(np.log(values)))
print("log(exp x):", np.log(np.exp(values)))

# The log of a product is a sum — the reason log-likelihoods are easy to differentiate.
a, b = 3.0, 7.0
print("\nlog(a*b) =", np.log(a * b), " log a + log b =", np.log(a) + np.log(b))
```

### 6.2 Sigma notation, carefully

```python
x = np.array([1.0, 2.0, 3.0, 4.0])

sum_squares = np.sum(x ** 2)
square_of_sum = np.sum(x) ** 2
print(f"sum of squares      = {sum_squares:.1f}")
print(f"square of the sum   = {square_of_sum:.1f}")
print(f"difference          = {square_of_sum - sum_squares:.1f}")

n = x.size
mean = x.mean()
squared_deviations = np.sum((x - mean) ** 2)
print(f"\nsum (x - mean)^2    = {squared_deviations:.1f}")
print(f"sample variance     = {squared_deviations / (n - 1):.4f}")
print("expansion check: sum x^2 - n*mean^2 =", f"{sum_squares - n * mean**2:.4f}")
```

The last line is the identity \(\sum(x_i-\bar x)^{2}=\sum x_i^{2}-n\bar x^{2}\),
which is how the shortcut formula for variance is derived.

### 6.3 Derivative: numeric versus analytic

```python
def f(x):
    """f(x) = x^3."""
    return x ** 3


def central_difference(f, x, h=1e-6):
    """Approximate f'(x) with a symmetric difference quotient."""
    return (f(x + h) - f(x - h)) / (2 * h)


x0 = 2.0
analytic = 3 * x0 ** 2
print(f"analytic f'({x0}) = {analytic:.6f}")
for h in (1e-2, 1e-4, 1e-6, 1e-8, 1e-10):
    approx = central_difference(f, x0, h)
    print(f"h = {h:>6.0e}   numeric = {approx:12.6f}   error = {abs(approx - analytic):.2e}")
```

Read the table: the error falls as \(h^{2}\) until about \(h=10^{-8}\), then rises.
That rise is floating-point round-off — subtracting two nearly equal numbers loses
significant digits. Every numeric derivative has this trade-off; the choice of \(h\)
is a compromise, not a detail.

### 6.4 Finding a maximum where the derivative vanishes

```python
def neg_log_likelihood(mu, data):
    """Negative log-likelihood for a normal model with known sigma."""
    sigma = 2.0
    return -np.sum(-0.5 * np.log(2 * np.pi * sigma**2)
                   - 0.5 * ((data - mu) / sigma) ** 2)


rng = np.random.default_rng(2026)
sample = rng.normal(loc=5.0, scale=2.0, size=200)

grid = np.linspace(3.0, 7.0, 4001)
nll = np.array([neg_log_likelihood(m, sample) for m in grid])
mu_hat_grid = grid[nll.argmin()]

print(f"grid search  mu_hat = {mu_hat_grid:.4f}")
print(f"sample mean          = {sample.mean():.4f}")
print(f"difference           = {abs(mu_hat_grid - sample.mean()):.2e}")
```

The grid search finds the value that minimises the negative log-likelihood, and it
agrees with the sample mean to four decimal places — which is the analytic result
for a normal model with known variance. This is the pattern behind every fitted
model: write a loss, minimise it, and check the answer against theory when theory is
available.

### 6.5 Integration: rectangles, trapezoids, Simpson

```python
def rectangle_rule(f, a, b, n):
    edges = np.linspace(a, b, n + 1)
    mid = (edges[:-1] + edges[1:]) / 2
    return np.sum(f(mid)) * (b - a) / n


def trapezoid_rule(f, a, b, n):
    xg = np.linspace(a, b, n + 1)
    yg = f(xg)
    return (b - a) / n * (yg[0] / 2 + yg[1:-1].sum() + yg[-1] / 2)


def simpson_rule(f, a, b, n):
    if n % 2:
        n += 1
    xg = np.linspace(a, b, n + 1)
    yg = f(xg)
    weights = np.ones(n + 1)
    weights[1:-1:2] = 4
    weights[2:-1:2] = 2
    return (b - a) / n / 3 * np.sum(weights * yg)


g = lambda t: t ** 2
exact = 1 / 3
print(f"exact integral of x^2 on [0,1] = {exact:.10f}\n")
for n in (10, 100, 1000):
    print(f"n = {n:5d}  rectangle {rectangle_rule(g, 0, 1, n):.8f}"
          f"  trapezoid {trapezoid_rule(g, 0, 1, n):.8f}"
          f"  simpson {simpson_rule(g, 0, 1, n):.8f}")
```

### 6.6 A density integrates to one

```python
from math import erf

normal_pdf = lambda z: np.exp(-z ** 2 / 2) / np.sqrt(2 * np.pi)

total = simpson_rule(normal_pdf, -8, 8, 2000)
print(f"integral of the standard normal density over [-8, 8] = {total:.10f}")

area = simpson_rule(normal_pdf, -1.96, 1.96, 2000)
print(f"area between z = -1.96 and 1.96                   = {area:.6f}")
print(f"2*Phi(1.96) - 1 (closed form)                      = {2 * 0.5 * (1 + erf(1.96 / np.sqrt(2))) - 1:.6f}")
```

Two independent computations of the same probability agree to five decimal places.
This is the habit the whole course asks for: when a library returns 0.950004, you
know where that number comes from.

### 6.7 Series and convergence

```python
partial = np.cumsum([0.5 ** k for k in range(25)])
print("partial sums of (1/2)^k:", np.round(partial[:10], 6))
print("after 25 terms         :", f"{partial[-1]:.10f}")
print("closed form 1/(1-1/2)  :", 2.0)

# Geometric probabilities normalise: sum_k p(1-p)^k = 1
p = 0.3
total_prob = sum(p * (1 - p) ** k for k in range(500))
print(f"\nsum of geometric probabilities (p={p}) = {total_prob:.10f}")
```

### 6.8 Inclusion–exclusion, computed from a contingency table

```python
rng = np.random.default_rng(7)
n = 100_000
likes_coffee = rng.random(n) < 0.60
likes_tea = rng.random(n) < 0.45
both = likes_coffee & likes_tea

p_a = likes_coffee.mean()
p_b = likes_tea.mean()
p_ab = both.mean()
print(f"P(coffee)          = {p_a:.4f}")
print(f"P(tea)             = {p_b:.4f}")
print(f"P(coffee and tea)  = {p_ab:.4f}")
print(f"P(coffee or tea)   = {(likes_coffee | likes_tea).mean():.4f}")
print(f"inclusion-exclusion= {p_a + p_b - p_ab:.4f}")
```

The two routes agree because they compute the same set from different directions —
one by counting the union directly, one by the rule. Note that this simulation
assumes the two preferences are **independent**, which is why the intersection is
close to \(0.60\times0.45=0.27\).

## 7. Output and interpretation

- **Derivatives.** At \(x=2\), \(f'(x)=3x^{2}=12\); the numeric estimate with
  \(h=10^{-6}\) matches to about eight significant figures. The error growing at
  \(h=10^{-10}\) is round-off, not mathematics.
- **Integrals.** The rectangle rule at \(n=10\) is off in the third decimal; at
  \(n=1000\) it is off in the sixth; Simpson's rule is exact for a quadratic on the
  first try, because it fits parabolas to a parabola. Accuracy costs evaluations —
  Simpson gets much more per evaluation.
- **Maximum likelihood.** Minimising the negative log-likelihood by grid search
  returns the sample mean, confirming the analytic derivation in Module 14.
- **Series.** The partial sums approach 2 from below, and the geometric
  probabilities sum to 1. Both are the same fact viewed from two directions.
- **Sets.** Inclusion–exclusion and direct counting give the same union
  probability, which is why the rule can be used instead of a full table.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))

# (a) the function and its tangent line
xs = np.linspace(0.5, 3.5, 100)
axes[0].plot(xs, xs ** 3, label=r"$f(x)=x^3$", color="#4c72b0")
tangent = analytic * (xs - x0) + f(x0)
axes[0].plot(xs, tangent, "--", label=f"tangent at x={x0}", color="#c44e52")
axes[0].scatter([x0], [f(x0)], color="black", zorder=3)
axes[0].set(title="A derivative is a slope", xlabel="x", ylabel="f(x)")
axes[0].legend(frameon=False, fontsize=9)
axes[0].grid(alpha=0.3)

# (b) rectangles under a curve
xs = np.linspace(0, 1, 200)
axes[1].plot(xs, xs ** 2, color="#55a868", linewidth=2)
n_show = 8
edges = np.linspace(0, 1, n_show + 1)
mids = (edges[:-1] + edges[1:]) / 2
axes[1].bar(mids, mids ** 2, width=1 / n_show, alpha=0.35,
            edgecolor="black", color="#55a868")
axes[1].set(title="An integral is an area", xlabel="x", ylabel="f(x)")
axes[1].grid(alpha=0.3)

fig.tight_layout()
plt.show()
```

**What to look at.** In the left panel the tangent touches the curve at one point and
has slope 12 there: the derivative is local, and it is a slope. In the right panel the
rectangles fill the area under the curve as \(n\) grows; the error is the part of each
rectangle poking above or leaving a gap below the curve. Simpson's rule replaces
rectangles with parabolas, which is why it converges so much faster.

## 9. Practical scenario

You are asked to check a colleague's likelihood code. It reports a log-likelihood of
\(-412.7\) for a normal model. Three checks catch most errors before any data are
involved:

1. **Units and scale.** For 200 observations a log-likelihood around \(-400\) is
   plausible; a positive log-likelihood for a continuous density is not.
2. **A known special case.** Set the data to a constant and check that the MLE
   returns that constant and the likelihood its closed form.
3. **A derivative check.** Numerically differentiate the log-likelihood at the
   reported estimate; it should be approximately zero. If it is not, the estimate is
   not a maximum.

The third check is the one this practical gives you the tool for.

## 10. Exercises

**Exercise 1.** Write a function `derivative(f, x, h=1e-5)` using a forward
difference and compare its accuracy at \(x=2\) for \(f(x)=x^{3}\) with the central
difference.

**Exercise 2.** Use `simpson_rule` to compute \(\int_0^{\pi}\sin x\,dx\) and compare
with the exact value 2.

**Exercise 3.** For \(x=(2,4,6,8)\), verify numerically that
\(\sum(x_i-\bar x)^{2}=\sum x_i^{2}-n\bar x^{2}\).

**Exercise 4.** A geometric random variable has \(\Pr(X=k)=(1-p)^{k}p\) for
\(k=0,1,2,\dots\). With \(p=0.2\), compute \(\Pr(X\le5)\) by summing, and check it
against the closed form \(1-(1-p)^{6}\).

**Exercise 5.** Explain in two sentences why maximising a log-likelihood gives the
same estimate as maximising the likelihood.

## 11. Solutions

```python
# Solution 1
def forward_difference(f, x, h=1e-5):
    """Approximate f'(x) with a forward difference quotient."""
    return (f(x + h) - f(x)) / h


for h in (1e-3, 1e-5, 1e-7):
    fwd = forward_difference(f, 2.0, h)
    ctr = central_difference(f, 2.0, h)
    print(f"h={h:.0e}  forward {fwd:.8f} (err {abs(fwd-12):.2e})"
          f"   central {ctr:.8f} (err {abs(ctr-12):.2e})")
```

The central difference is more accurate at every \(h\), by roughly a factor of
\(h\) — its error is \(O(h^{2})\) against the forward difference's \(O(h)\).

```python
# Solution 2
print(f"Simpson  : {simpson_rule(np.sin, 0, np.pi, 100):.10f}")
print(f"exact    : 2.0")
print(f"error    : {abs(simpson_rule(np.sin, 0, np.pi, 100) - 2):.2e}")
```

```python
# Solution 3
y = np.array([2.0, 4.0, 6.0, 8.0])
lhs = np.sum((y - y.mean()) ** 2)
rhs = np.sum(y ** 2) - y.size * y.mean() ** 2
print(f"sum (y - mean)^2       = {lhs:.6f}")
print(f"sum y^2 - n * mean^2   = {rhs:.6f}")
print("equal?", np.isclose(lhs, rhs))
```

```python
# Solution 4
p = 0.2
by_sum = sum((1 - p) ** k * p for k in range(6))
closed = 1 - (1 - p) ** 6
print(f"sum k=0..5 : {by_sum:.10f}")
print(f"1-(1-p)^6  : {closed:.10f}")
print("equal?", np.isclose(by_sum, closed))
```

```python
# Solution 5 (written)
# The logarithm is strictly increasing, so for positive likelihoods L1 > L2
# exactly when log L1 > log L2. The maximum is therefore at the same parameter
# value, and the product of many likelihoods becomes a sum that is far easier to
# differentiate and far less prone to numerical underflow.
```

## 12. Summary

- \(\sum x_i^{2}\) and \((\sum x_i)^{2}\) differ; the variance uses the centred sum,
  and \(\sum(x_i-\bar x)^{2}=\sum x_i^{2}-n\bar x^{2}\).
- A derivative is a local slope; the central difference is \(O(h^{2})\), and very
  small \(h\) is defeated by round-off.
- An integral is an area; Simpson's rule converges far faster than rectangles and
  makes "a density integrates to 1" checkable.
- Geometric series explain why discrete distributions normalise, and link to waiting
  times.
- Inclusion–exclusion is the two-event case of the general union rule.
- Numerical methods are how assumptions get tested: if the derivative at your estimate
  is not zero, you have not found a maximum.

Next: [Practical 03](03-data-and-descriptive-statistics.ipynb) moves from single
variables to a full dataset.
