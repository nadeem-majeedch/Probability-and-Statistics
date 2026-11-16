# Practical 10 — Continuous Distributions and the Normal Curve

## 1. Introduction

A continuous random variable can take any value in an interval, so the probability of
any single value is zero. Probabilities are instead **areas under a density**. That one
sentence explains why we integrate, why \(f(x)\) can exceed 1, and why
\(\Pr(X=x)=0\) does not mean \(X=x\) is impossible.

This practical works with the three continuous families the course uses — uniform,
exponential and normal — computes probabilities and quantiles with SciPy, checks the
68–95–99.7 rule, and uses a Q–Q plot to judge whether data are normal.

## 2. Learning objectives

By the end of this practical you can:

1. Explain why a density is not a probability, and compute a probability as an area.
2. Use `scipy.stats` for `pdf`, `cdf`, `ppf` and `sf` of the normal distribution.
3. Standardise a normal variable and use the empirical rule.
4. Read a Q–Q plot and say what a deviation at the tails means.
5. Generate samples by inverting the CDF, and explain why that works.

## 3. Required libraries

| Library | Used for |
|---|---|
| `scipy.stats` | `norm`, `uniform`, `expon` |
| `numpy` | grids, simulation |
| `matplotlib` | densities, shaded areas, Q–Q plots |

## 4. Concepts

### 4.1 Density, not probability

For a continuous \(X\) with density \(f\),

\[ \Pr(a\le X\le b)=\int_a^b f(x)\,dx,\qquad \int_{-\infty}^{\infty}f(x)\,dx=1. \]

\(f(x)\) is a *density*: its height has units of probability per unit of \(x\), so it can
be greater than 1 (a uniform on \([0,0.5]\) has density 2). Only areas are
probabilities.

### 4.2 Uniform and exponential

**Uniform** on \([a,b]\): constant density \(1/(b-a)\), mean \((a+b)/2\), variance
\((b-a)^{2}/12\). The analogue of "every outcome equally likely".

**Exponential** with rate \(\lambda\): density \(\lambda e^{-\lambda x}\) on \(x\ge0\),
mean \(1/\lambda\), variance \(1/\lambda^{2}\). It is **memoryless**:

\[ \Pr(X>s+t\mid X>s)=\Pr(X>t), \]

which is why it models waiting times for events that occur at a constant rate.

### 4.3 The normal distribution

\[ f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^{2}}{2\sigma^{2}}\right),
   \qquad X\sim N(\mu,\sigma^{2}). \]

Standardising, \(Z=(X-\mu)/\sigma\sim N(0,1)\), turns every normal question into a
z-table lookup. The empirical rule:

| Interval | Probability |
|---|---|
| \(\mu\pm1\sigma\) | 0.6827 |
| \(\mu\pm2\sigma\) | 0.9545 |
| \(\mu\pm3\sigma\) | 0.9973 |

The normal is the limit of many sums (Practical 13), which is why it appears where no
individual observation is normal.

### 4.4 Quantiles and the inverse CDF

The quantile function \(Q(p)=F^{-1}(p)\) returns the value below which a proportion
\(p\) of the distribution lies. It is also the basis of simulation: if \(U\sim
\text{Uniform}(0,1)\), then \(Q(U)\) has distribution \(F\). That is **inverse
transform sampling**.

## 5. Formulas

\[ \Pr(a\le X\le b)=F(b)-F(a),\qquad \Pr(X>a)=1-F(a) \]

\[ z=\frac{x-\mu}{\sigma},\qquad x=\mu+z\sigma \]

\[ Q(0.975)=1.959964\ \text{for }N(0,1),\qquad
   \Pr(|Z|\le1.96)=0.9500 \]

For a uniform on \([a,b]\): \(\E[X]=(a+b)/2\), \(\Var(X)=(b-a)^{2}/12\).

## 6. Implementation

### 6.1 The normal density and the empirical rule

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

mu, sigma = 65.0, 10.0
X = stats.norm(mu, sigma)

for k in (1, 2, 3):
    within = X.cdf(mu + k*sigma) - X.cdf(mu - k*sigma)
    print(f"P(|X - mu| <= {k} sigma) = {within:.4f}")

print(f"\nP(X > 70)      = {X.sf(70):.4f}")
print(f"P(50 <= X <= 80) = {X.cdf(80) - X.cdf(50):.4f}")
print(f"95th percentile = {X.ppf(0.95):.3f}")
print(f"z for the 95th percentile = {stats.norm.ppf(0.95):.5f}")
```

### 6.2 Standardisation in both directions

```python
x_value = 78.0
z = (x_value - mu) / sigma
print(f"x = {x_value} -> z = {z:.4f}")
print(f"P(X <= {x_value}) = {X.cdf(x_value):.4f} = Phi({z:.4f}) = {stats.norm.cdf(z):.4f}")

z_target = 1.5
print(f"z = {z_target} -> x = {mu + z_target*sigma}")
print(f"P(X <= {mu + z_target*sigma}) = {X.cdf(mu + z_target*sigma):.4f}")
```

### 6.3 Density is not probability

```python
dense = stats.norm(0, 0.1)
print(f"density at 0 for N(0, 0.01): {dense.pdf(0):.3f}")
print(f"P(-0.0001 < X < 0.0001)     = {dense.cdf(0.0001) - dense.cdf(-0.0001):.6f}")
print(f"probability of exact value 0 = {dense.pdf(0) * 0:.6f} (limit of a shrinking interval)")

narrow = stats.uniform(0, 0.5)
print(f"\nUniform(0, 0.5) density = {narrow.pdf(0.1):.2f}  (> 1, and that is allowed)")
print(f"area over the support   = {narrow.cdf(0.5) - narrow.cdf(0.0):.4f}")
```

### 6.4 Exponential and memorylessness

```python
lam = 0.25          # mean 4 minutes
E = stats.expon(scale=1/lam)

print(f"mean = {E.mean():.3f}, sd = {E.std():.3f}")
print(f"P(X > 4)   = {E.sf(4):.4f}   (e^-1 = {np.exp(-1):.4f})")
print(f"P(X > 8)   = {E.sf(8):.4f}   (e^-2 = {np.exp(-2):.4f})")

p_given = E.sf(8) / E.sf(4)
print(f"P(X > 8 | X > 4) = {p_given:.4f}   P(X > 4) = {E.sf(4):.4f}")
print("equal? memoryless:", np.isclose(p_given, E.sf(4)))
```

```python
rng = np.random.default_rng(2026)
waits = rng.exponential(scale=1/lam, size=200_000)
beyond4 = waits[waits > 4]
print(f"\nsimulated P(X > 4)        = {(waits > 4).mean():.4f}")
print(f"of those beyond 4, P(> 8) = {(beyond4 > 8).mean():.4f}")
print(f"unconditional P(> 4)      = {(waits > 4).mean():.4f}")
```

### 6.5 Inverse transform sampling

```python
rng = np.random.default_rng(11)
u = rng.random(100_000)
simulated = E.ppf(u)          # inverse CDF applied to uniforms

print(f"mean of simulated   = {simulated.mean():.4f}   exact {E.mean():.4f}")
print(f"P(simulated > 4)    = {(simulated > 4).mean():.4f}   exact {E.sf(4):.4f}")

# The same trick for a discrete variable: Poisson via its CDF.
u2 = rng.random(200_000)
poisson_draws = stats.poisson(4).ppf(u2)
print(f"\nPoisson(4) mean from inverse CDF = {poisson_draws.mean():.4f}")
```

### 6.6 Are these data normal? A Q–Q plot

```python
rng = np.random.default_rng(5)
normal_sample = rng.normal(65, 10, 300)
skewed_sample = rng.exponential(10, 300) + 40

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
stats.probplot(normal_sample, dist="norm", plot=axes[0])
axes[0].set_title("Normal data: points follow the line")
stats.probplot(skewed_sample, dist="norm", plot=axes[1])
axes[1].set_title("Skewed data: points bend away")
for ax in axes:
    ax.get_lines()[0].set_markersize(3)
fig.tight_layout()
plt.show()

print("skewness of normal sample:", round(stats.skew(normal_sample), 3))
print("skewness of skewed sample:", round(stats.skew(skewed_sample), 3))
```

### 6.7 Sums of uniforms approach normality

```python
rng = np.random.default_rng(3)
for k in (1, 2, 5, 20):
    sums = rng.random((20_000, k)).sum(axis=1)
    print(f"sum of {k:2d} uniforms: mean {sums.mean():.3f}, "
          f"sd {sums.std(ddof=1):.3f}, excess kurtosis {stats.kurtosis(sums):+.3f}")
```

Each uniform is flat, yet the sum becomes bell-shaped: its excess kurtosis moves from
-1.2 (the flat shape of one uniform) towards 0, the normal value. Skewness is already
zero because a uniform is symmetric, which is why kurtosis is the informative number
here. This is a preview of the Central Limit Theorem: the shape of the population
matters less as the number of terms grows.

## 7. Output and interpretation

- **Empirical rule.** 0.6827, 0.9545 and 0.9973 within one, two and three standard
  deviations. With \(\mu=65\), \(\sigma=10\), about 16% of students score above 75 and
  about 2.3% above 85.
- **Standardisation.** \(x=78\) corresponds to \(z=1.3\), and
  \(\Pr(X\le78)=\Phi(1.3)=0.9032\): the two routes — `norm.cdf` on \(X\) and
  `norm.cdf` on \(z\) — agree exactly.
- **Density versus probability.** The density at 0 for \(N(0,0.01)\) is about 4 — larger
  than 1, which would be impossible for a probability. The probability of a value within
  0.0001 of 0 is about 0.0008, and the probability of exactly 0 is zero. The density is
  a height; only area is probability.
- **Memorylessness.** \(\Pr(X>8\mid X>4)=\Pr(X>4)=0.3679\). The simulation reproduces
  this: among waits beyond 4 minutes, the share beyond 8 is the same as the share of all
  waits beyond 4. Nothing is "due" after a wait.
- **Inverse transform.** Feeding uniforms through the inverse CDF reproduces the
  exponential and the Poisson, which is how many random generators work internally.
- **Sums.** The excess kurtosis of a single uniform is -1.2; of a sum of 20 it is about
  -0.06, close to the normal value of 0. The sum looks normal even though no single term
  does.
- **Q–Q plots.** Normal data lie on the reference line. The exponential sample bends up
  at the right and down at the left — the signature of right skew. The tails are where
  non-normality shows first, which is why a histogram can look "normal enough" while the
  Q–Q plot does not.

## 8. Visualisation

```python
xs = np.linspace(mu - 4*sigma, mu + 4*sigma, 400)
density = X.pdf(xs)

fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

axes[0].plot(xs, density, color="#4c72b0", linewidth=2)
shade = (xs >= 50) & (xs <= 80)
axes[0].fill_between(xs[shade], density[shade], color="#4c72b0", alpha=0.3)
axes[0].set(xlabel="Mark", ylabel="Density",
            title="P(50 <= X <= 80) is the shaded area")
axes[0].grid(alpha=0.3)

axes[1].plot(xs, X.cdf(xs), color="#55a868", linewidth=2)
axes[1].axhline(0.95, color="grey", linestyle=":")
axes[1].axvline(X.ppf(0.95), color="#c44e52", linestyle="--",
                label=f"95th percentile = {X.ppf(0.95):.1f}")
axes[1].set(xlabel="Mark", ylabel="F(x)", title="CDF: reading quantiles off the curve")
axes[1].legend(frameon=False)
axes[1].grid(alpha=0.3)

fig.tight_layout()
plt.show()

print(f"area check: {X.cdf(80) - X.cdf(50):.6f}")
```

```python
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.hist(normal_sample, bins=25, density=True, alpha=0.6, color="#4c72b0",
        edgecolor="white", label="300 draws")
ax.plot(xs, density, color="#c44e52", linewidth=2, label="true density")
ax.set(xlabel="Value", ylabel="Density", title="A histogram is a noisy density estimate")
ax.legend(frameon=False)
fig.tight_layout()
plt.show()
```

**What to look at.** The shaded region is the probability, and its width matters as much
as its height. The CDF is monotone from 0 to 1, so any quantile is a horizontal read.
The histogram approximates the density but is noisy at \(n=300\), especially in the
tails — one reason not to judge normality from a histogram alone.

## 9. Practical scenario

**Setting a pass mark.** Marks are modelled as \(N(65,10)\). The department wants the
pass rate to be 80%, and separately wants to identify the top 5%.

```python
X = stats.norm(65, 10)
pass_mark = X.ppf(0.20)          # 20% below, so 80% pass
top_mark = X.ppf(0.95)
print(f"pass mark for an 80% pass rate: {pass_mark:.1f}")
print(f"top-5% threshold              : {top_mark:.1f}")
print(f"check: P(X >= pass mark) = {X.sf(pass_mark):.3f}")
print(f"check: P(X >= top mark)  = {X.sf(top_mark):.3f}")
```

The model is doing real work here: the answer depends on the assumed \(\mu\) and
\(\sigma\), and a skewed distribution would move both thresholds. That is why the
Q–Q plot in Section 6.6 comes before the calculation in practice — check the model, then
use it.

## 10. Exercises

**Exercise 1.** For \(X\sim N(100,15)\), compute \(\Pr(X<120)\), \(\Pr(90<X<110)\) and
the 90th percentile.

**Exercise 2.** A uniform variable on \([2, 10]\): compute its mean, variance, and
\(\Pr(4<X<7)\) both from the density and with `scipy.stats.uniform`.

**Exercise 3.** For an exponential with mean 5, compute \(\Pr(X<2)\) and
\(\Pr(X>10\mid X>5)\).

**Exercise 4.** Generate 5,000 draws from \(N(0,1)\) by inverse transform sampling and
compare the mean and standard deviation with 0 and 1.

**Exercise 5.** Explain in two sentences why \(\Pr(X=x)=0\) for a continuous variable,
and why that does not make the value impossible.

## 11. Solutions

```python
# Solution 1
X = stats.norm(100, 15)
print(f"P(X < 120)      = {X.cdf(120):.4f}")
print(f"P(90 < X < 110) = {X.cdf(110) - X.cdf(90):.4f}")
print(f"90th percentile = {X.ppf(0.90):.3f}")
```

```python
# Solution 2
U = stats.uniform(2, 8)          # loc=2, scale=8 -> support [2, 10]
print(f"mean = {U.mean():.3f}, variance = {U.var():.3f}")
print(f"P(4 < X < 7) = {U.cdf(7) - U.cdf(4):.4f}")
print(f"by density   = {(7-4) * (1/8):.4f}")
```

```python
# Solution 3
E = stats.expon(scale=5)
print(f"P(X < 2)         = {E.cdf(2):.4f}")
print(f"P(X > 10 | X > 5) = {E.sf(10)/E.sf(5):.4f}")
print(f"P(X > 5)          = {E.sf(5):.4f}  (equal: memoryless)")
```

```python
# Solution 4
rng = np.random.default_rng(42)
u = rng.random(5000)
z = stats.norm.ppf(u)
print(f"mean {z.mean():+.4f}, sd {z.std(ddof=1):.4f}")
print(f"min {z.min():.3f}, max {z.max():.3f}")
```

```python
# Solution 5 (written)
# For a continuous variable the probability of an interval is the area under the
# density, and a single point has zero width, hence zero area. That does not make the
# value impossible: the variable must take *some* value, and every individual value has
# probability zero. Probability statements are about intervals, not points.
```

## 12. Summary

- Continuous probabilities are areas under a density; the density itself is not a
  probability and may exceed 1.
- The normal is fixed by \(\mu\) and \(\sigma\); standardisation turns it into
  \(N(0,1)\), and 68–95–99.7 summarises its spread.
- The exponential is memoryless; waiting time already spent does not change the
  distribution of the remaining wait.
- Quantiles come from the inverse CDF, which also generates random draws from any
  distribution.
- Q–Q plots diagnose normality better than histograms, especially in the tails.
- Sums of non-normal variables become normal: the CLT in one line of code.

Next: [Practical 11](11-joint-distributions.ipynb) moves to two variables at once.
