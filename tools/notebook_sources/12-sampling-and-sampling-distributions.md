# Practical 12 — Sampling and Sampling Distributions

## 1. Introduction

A statistic is a number computed from a sample: a mean, a proportion, a variance. Draw a
different sample and you get a different number. The **sampling distribution** is the
distribution of that number across all possible samples — and it is the object every
confidence interval and test in the course is built on.

You cannot observe the sampling distribution from one sample. This practical therefore
*constructs* it: define a population, draw thousands of samples, and look at the spread
of the statistics. That experiment is the clearest way to see why "the standard error of
the mean is \(\sigma/\sqrt{n}\)" is a statement about a procedure, not about your data.

## 2. Learning objectives

By the end of this practical you can:

1. Distinguish population, sample, parameter and statistic.
2. Simulate a sampling distribution for a mean, a proportion and a variance.
3. Verify \(\text{se}(\bar X)=\sigma/\sqrt n\) and explain the \(1/\sqrt{n}\) scaling.
4. Explain why the sampling distribution of \(s^{2}\) is skewed and uses \(n-1\).
5. State when the finite population correction is needed.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | populations and repeated sampling |
| `scipy.stats` | normal, t, chi-square reference curves |
| `matplotlib` | sampling distributions |

## 4. Concepts

### 4.1 Parameters and statistics

| | Population | Sample |
|---|---|---|
| Mean | \(\mu\) | \(\bar x\) |
| Standard deviation | \(\sigma\) | \(s\) |
| Proportion | \(p\) | \(\hat p\) |
| Size | \(N\) | \(n\) |

Parameters are fixed and unknown; statistics are random because the sample is random.
The sampling distribution describes the randomness of the statistic.

### 4.2 The standard error of the mean

\[ \se(\bar X)=\frac{\sigma}{\sqrt n}. \]

Four times the sample size halves the standard error. The formula assumes independent
observations; dependence (clusters, time series) makes the true standard error larger,
often much larger.

### 4.3 Sampling distribution of a proportion

\[ \se(\hat p)=\sqrt{\frac{p(1-p)}{n}}, \]

and \(\hat p\) is approximately normal when \(np\ge10\) and \(n(1-p)\ge10\) — the same
CLT result applied to a sum of 0/1 variables.

### 4.4 The sample variance

\[ \frac{(n-1)s^{2}}{\sigma^{2}}\sim\chi^{2}_{n-1}. \]

The sampling distribution of \(s^{2}\) is **skewed**, not normal, and its skewness falls
as \(n\) grows. This is why intervals for a variance use the chi-square distribution
rather than a normal approximation.

### 4.5 Finite population correction

When sampling without replacement from a population of size \(N\),

\[ \se(\bar X)=\frac{\sigma}{\sqrt n}\sqrt{\frac{N-n}{N-1}}. \]

The factor is close to 1 unless the sample is a substantial fraction of the population
(rule of thumb: more than 5%).

## 5. Formulas

\[ \se(\bar X)=\frac{\sigma}{\sqrt n},\qquad
   \se(\hat p)=\sqrt{\frac{p(1-p)}{n}},\qquad
   \Var(s^{2})=\frac{2\sigma^{4}}{n-1} \]

\[ z=\frac{\bar X-\mu}{\sigma/\sqrt n},\qquad
   t=\frac{\bar X-\mu}{s/\sqrt n}\ \sim t_{n-1} \]

## 6. Implementation

### 6.1 Define a population

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)

# A skewed population: salaries in thousands. The shape is the point.
population = rng.lognormal(mean=3.0, sigma=0.6, size=200_000)
mu = population.mean()
sigma = population.std(ddof=0)

print(f"population size : {population.size:,}")
print(f"mu              : {mu:.4f}")
print(f"sigma           : {sigma:.4f}")
print(f"median          : {np.median(population):.4f}")
print(f"skewness        : {stats.skew(population):.4f}")
```

### 6.2 The sampling distribution of the mean

```python
def sample_means(pop, n, reps, seed):
    """Draw `reps` samples of size n and return their means."""
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, pop.size, size=(reps, n))
    return pop[idx].mean(axis=1)

reps = 20_000
results = {}
for n in (5, 25, 100):
    means = sample_means(population, n, reps, seed=100 + n)
    results[n] = means
    print(f"n = {n:3d}: mean of means {means.mean():8.4f}  "
          f"sd of means {means.std(ddof=1):7.4f}  "
          f"theory sigma/sqrt(n) {sigma/np.sqrt(n):7.4f}")
```

```python
# How normal is the sampling distribution at each n? Compare quantiles with the
# normal curve that the CLT predicts.
for n, means in results.items():
    se = sigma / np.sqrt(n)
    z = (means - mu) / se
    print(f"n = {n:3d}: P(|Z| > 1.96) = {(np.abs(z) > 1.96).mean():.4f} "
          f"(normal 0.0500),  skewness {stats.skew(z):+.3f}")
```

### 6.3 Standard error against sample size

```python
ns = np.array([2, 5, 10, 25, 50, 100, 400])
print(f"{'n':>5} {'sigma/sqrt(n)':>15}")
for n in ns:
    print(f"{n:>5} {sigma/np.sqrt(n):>15.4f}")

print("\nquadrupling n:")
print(f"  n=25  -> {sigma/5:.4f}")
print(f"  n=100 -> {sigma/10:.4f}   (half)")
print(f"  n=400 -> {sigma/20:.4f}   (half again)")
```

### 6.4 A proportion

```python
p = 0.35
rng = np.random.default_rng(7)
draws = rng.random((20_000, 200)) < p
phats = draws.mean(axis=1)

print(f"mean of p-hat   : {phats.mean():.4f}  (p = {p})")
print(f"sd of p-hat     : {phats.std(ddof=1):.4f}  "
      f"(theory {np.sqrt(p*(1-p)/200):.4f})")
print(f"share within 1 se: {(np.abs(phats - p) < np.sqrt(p*(1-p)/200)).mean():.4f}")
```

### 6.5 The sampling distribution of \(s^{2}\)

```python
def sample_vars(pop, n, reps, seed):
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, pop.size, size=(reps, n))
    return pop[idx].var(axis=1, ddof=1)

for n in (5, 30, 100):
    vars_ = sample_vars(population, n, 5_000, seed=200 + n)
    print(f"n = {n:3d}: mean(s^2) {vars_.mean():8.3f}  sigma^2 {sigma**2:8.3f}  "
          f"skewness {stats.skew(vars_):+.3f}")
```

### 6.6 t instead of z when \(\sigma\) is estimated

```python
n = 10
rng = np.random.default_rng(31)
idx = rng.integers(0, population.size, size=(20_000, n))
samples = population[idx]
xbar = samples.mean(axis=1)
s = samples.std(axis=1, ddof=1)
t_stats = (xbar - mu) / (s / np.sqrt(n))
z_stats = (xbar - mu) / (sigma / np.sqrt(n))

print(f"sd of t statistics : {t_stats.std(ddof=1):.4f}   (t has heavier tails)")
print(f"sd of z statistics : {z_stats.std(ddof=1):.4f}")
print(f"P(|t| > 2.262) with 9 df = {(np.abs(t_stats) > 2.26216).mean():.4f}  (t theory 0.05)")
print(f"P(|z| > 2.262)           = {(np.abs(z_stats) > 2.26216).mean():.4f}  (normal 0.0238)")
```

### 6.7 Finite population correction

```python
N = 1000
for n in (10, 50, 200, 500):
    fpc = np.sqrt((N - n) / (N - 1))
    print(f"N = {N}, n = {n:3d}: fpc = {fpc:.4f}, "
          f"se reduced by {(1-fpc)*100:5.1f}%")
```

## 7. Output and interpretation

- **The population.** Salaries are right-skewed (skewness 2.23) with \(\mu=24.0\) and
  \(\sigma=15.8\) in thousands. Half the population earns less than 20.1, and the mean
  is pulled well above the median by the long right tail.
- **Sampling distribution of the mean.** At \(n=5\) the distribution of \(\bar X\) is
  still visibly right-skewed (skewness 1.03) and its standard deviation is 7.10, close to
  \(\sigma/\sqrt5=7.06\). At \(n=25\) the spread falls to 3.13 and the skewness to 0.44;
  at \(n=100\) the spread is 1.58, the skewness 0.24, and the share beyond 1.96 standard
  errors is 0.0515 — the normal approximation is working.
- **The \(1/\sqrt{n}\) law.** Going from 25 to 100 halves the standard error; going from
  100 to 400 halves it again. Precision is expensive: each halving costs four times the
  data.
- **Proportions.** The simulated standard deviation of \(\hat p\) matches
  \(\sqrt{p(1-p)/n}=0.0337\), and about 68% of samples fall within one standard error of
  \(p\).
- **Sample variance.** \(\E[s^{2}]=\sigma^{2}\) to within simulation error (241.5 and
  250.6 against 249.2), so \(s^{2}\) is unbiased. But its distribution is extremely
  right-skewed at \(n=5\) (skewness 7.1), less so at \(n=30\) (3.6), and still skewed at
  \(n=100\) (1.6). The skew is why variance intervals use \(\chi^{2}\), not a normal
  approximation.
- **t versus z.** With \(\sigma\) estimated from 10 observations, the t statistic has
  heavier tails: 5% of samples exceed \(|t|=2.262\), whereas only 2.4% exceed that value
  on the z scale. Using 1.96 with an estimated \(\sigma\) would understate the error.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.5), sharex=False)
for ax, n in zip(axes, (5, 25, 100)):
    means = results[n]
    ax.hist(means, bins=60, density=True, color="#4c72b0", alpha=0.65,
            edgecolor="white")
    grid = np.linspace(means.min(), means.max(), 300)
    ax.plot(grid, stats.norm.pdf(grid, mu, sigma/np.sqrt(n)),
            color="#c44e52", linewidth=2)
    ax.set(title=f"n = {n}: se = {sigma/np.sqrt(n):.2f}",
           xlabel="Sample mean", ylabel="Density")
fig.suptitle("Sampling distribution of the mean, with the CLT normal curve", y=1.02)
fig.tight_layout()
plt.show()
```

```python
fig, ax = plt.subplots(figsize=(6.4, 3.8))
se = sigma / np.sqrt(ns)
empirical = [sample_means(population, n, 4000, seed=300 + n).std(ddof=1) for n in ns]
ax.plot(ns, se, "-", color="#4c72b0", label="theory: sigma / sqrt(n)")
ax.plot(ns, empirical, "o", color="#c44e52", label="simulated sd of the mean")
ax.plot(ns, sigma / np.sqrt(25) * np.sqrt(25 / ns), ":", color="grey",
        label="1/sqrt(n) slope")
ax.set(xscale="log", yscale="log", xlabel="Sample size n (log)",
       ylabel="Standard error (log)", title="Doubling precision costs four times the data")
ax.legend(frameon=False)
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
plt.show()
```

**What to look at.** In the first figure the histogram narrows and becomes symmetric as
\(n\) grows, and the red normal curve fits better each time — the CLT at work. In the
second, the straight line on log–log axes is the signature of a power law: the slope is
\(-1/2\), which is exactly what \(\sigma/\sqrt n\) predicts.

## 9. Practical scenario

**How large a survey?** A university wants the mean monthly expenditure of its 12,000
students, with a 95% margin of error of 500 rupees. A pilot suggests \(\sigma\approx
4{,}000\).

```python
sigma_pilot = 4000
margin = 500
z = 1.96
n_required = (z * sigma_pilot / margin) ** 2
print(f"required n (no fpc) = {n_required:.1f} -> {int(np.ceil(n_required))}")

N = 12_000
n_fpc = n_required / (1 + (n_required - 1) / N)
print(f"with finite population correction = {n_fpc:.1f} -> {int(np.ceil(n_fpc))}")

print(f"\nsample as a share of the population: {n_required/N:.1%}")
```

The correction saves about 50 students here because the sample is 2% of the population.
The larger lesson is the cost structure: halving the margin of error from 500 to 250
quadruples the required sample, which is usually the constraint that decides the design.

## 10. Exercises

**Exercise 1.** Draw 5,000 samples of size 16 from a normal population with
\(\mu=50,\sigma=8\). Report the mean and standard deviation of the sample means and
compare with theory.

**Exercise 2.** Repeat Exercise 1 with a uniform population on \([0,10]\) and comment on
the shape of the sampling distribution at \(n=16\).

**Exercise 3.** For \(p=0.5\) and \(n=100\), compute \(\se(\hat p)\), then simulate to
confirm it.

**Exercise 4.** Simulate the sampling distribution of \(s^{2}\) for \(n=20\) and report
its skewness. Is it symmetric?

**Exercise 5.** A sample of 80 is drawn from a population of 100. Compute the finite
population correction and explain why it matters here but not for \(n=80\) from
\(N=100{,}000\).

## 11. Solutions

```python
# Solution 1
rng = np.random.default_rng(101)
samples = rng.normal(50, 8, size=(5000, 16))
means = samples.mean(axis=1)
print(f"mean of means {means.mean():.4f} (50), sd {means.std(ddof=1):.4f} "
      f"(theory {8/np.sqrt(16):.4f})")
```

```python
# Solution 2
rng = np.random.default_rng(102)
samples = rng.uniform(0, 10, size=(5000, 16))
means = samples.mean(axis=1)
print(f"mean of means {means.mean():.4f} (5), sd {means.std(ddof=1):.4f} "
      f"(theory {(10/np.sqrt(12))/4:.4f})")
print(f"skewness {stats.skew(means):+.4f} (uniform is symmetric; means are near-normal)")
```

```python
# Solution 3
p, n = 0.5, 100
theory = np.sqrt(p*(1-p)/n)
rng = np.random.default_rng(103)
phat = (rng.random((20_000, n)) < p).mean(axis=1)
print(f"theory {theory:.4f}, simulated {phat.std(ddof=1):.4f}")
```

```python
# Solution 4
v = sample_vars(population, 20, 20_000, seed=104)
print(f"mean s^2 {v.mean():.3f} (sigma^2 {sigma**2:.3f})")
print(f"skewness {stats.skew(v):+.3f} -> clearly right-skewed, not symmetric")
```

```python
# Solution 5
for N in (100, 100_000):
    fpc = np.sqrt((N - 80) / (N - 1))
    print(f"N = {N:>7,}: fpc = {fpc:.4f} -> se reduced by {(1-fpc)*100:.1f}%")
# With N=100 the sample is 80% of the population, so the correction is large; with
# N=100,000 it is negligible.
```

## 12. Summary

- A statistic has a sampling distribution; its standard deviation is the standard error.
- \(\se(\bar X)=\sigma/\sqrt n\): precision improves as the square root of the sample
  size, so each halving of error costs four times the data.
- \(\hat p\) has standard error \(\sqrt{p(1-p)/n}\) and is approximately normal for
  moderate counts.
- \((n-1)s^{2}/\sigma^{2}\sim\chi^{2}_{n-1}\), which is skewed for small \(n\) — hence
  the t and chi-square distributions.
- Sampling without replacement from a small population needs the finite population
  correction.
- The sampling distribution is a property of the *procedure*; you cannot see it in one
  sample, which is why we simulate it.

Next: [Practical 13](13-law-of-large-numbers-and-clt.ipynb) pushes the same experiment to
its limits.
