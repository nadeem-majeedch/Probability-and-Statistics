# Practical 13 — Law of Large Numbers and Central Limit Theorem

## 1. Introduction

Two theorems do most of the work in applied statistics, and both are statements about
what happens as the sample size grows:

- the **Law of Large Numbers** says the sample mean converges to the population mean;
- the **Central Limit Theorem** says the sample mean becomes normally distributed around
  it, whatever the population shape.

They answer different questions. The LLN says *where the average goes*; the CLT says *how
it fluctuates on the way there*. This practical demonstrates both, including the cases
where they fail — a distribution with infinite variance, and the Cauchy, which has no
mean at all.

## 2. Learning objectives

By the end of this practical you can:

1. Demonstrate the LLN by simulation and state its rate.
2. Demonstrate the CLT for symmetric, skewed and bimodal populations.
3. Standardise sample means and compare the result with \(N(0,1)\).
4. Explain why a heavy-tailed distribution breaks the CLT, and why Cauchy is worse.
5. Use the LLN to estimate an integral by Monte Carlo, with a standard error.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | simulation |
| `scipy.stats` | normal reference, quantile checks |
| `matplotlib` | convergence paths and histograms |

## 4. Concepts

### 4.1 The weak law

\[ \Pr\left(\left|\bar X_n-\mu\right|\ge\epsilon\right)\to0
   \quad\text{for every }\epsilon>0. \]

The average is probably close for large \(n\). Chebyshev's inequality gives the rate:
the probability of an error larger than \(\epsilon\) is at most
\(\sigma^{2}/(n\epsilon^{2})\).

### 4.2 The strong law

\[ \Pr\left(\lim_{n\to\infty}\bar X_n=\mu\right)=1. \]

Convergence with probability one: the whole path settles, not just each snapshot. This
is why a simulation's running average stops wandering and a single long run is
informative.

### 4.3 The central limit theorem

For i.i.d. \(X_i\) with mean \(\mu\) and finite variance \(\sigma^{2}\),

\[ \frac{\sqrt n\,(\bar X_n-\mu)}{\sigma}\ \xrightarrow{d}\ N(0,1). \]

Three things to notice: the population shape does not appear in the limit; the rate is
\(1/\sqrt n\); and the requirement is **finite variance**. The Berry–Esseen theorem
bounds the error at order \(1/\sqrt n\), with a constant that grows with skewness — so
skewed populations need larger \(n\).

### 4.4 Where it fails

- **Infinite variance.** A Pareto distribution with tail index \(\alpha\le2\) has
  infinite variance; the standardised mean does not converge to a normal. It converges
  to a *stable* law with heavy tails.
- **No mean.** The Cauchy distribution has no expected value: the sample mean has the
  same distribution as one observation, however large \(n\) is. Averaging does not help.

## 5. Formulas

\[ \se(\bar X)=\frac{\sigma}{\sqrt n},\qquad
   z=\frac{\bar X-\mu}{\sigma/\sqrt n}\approx N(0,1) \]

\[ \Pr(|\bar X-\mu|\ge\epsilon)\le\frac{\sigma^{2}}{n\epsilon^{2}}
   \quad\text{(Chebyshev)} \]

Monte Carlo: for \(U_i\sim\text{Uniform}(0,1)\),

\[ \int_0^1 g(x)\,dx\approx\frac1B\sum_{i=1}^{B}g(U_i),\qquad
   \se\approx\frac{s_g}{\sqrt B}. \]

## 6. Implementation

### 6.1 The LLN: running means of three populations

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)
n_paths = 30_000

fair_coin = rng.integers(0, 2, size=n_paths)
skewed = rng.exponential(scale=2.0, size=n_paths)
bimodal = np.where(rng.random(n_paths) < 0.5,
                   rng.normal(2, 0.7, n_paths),
                   rng.normal(9, 0.7, n_paths))

for name, sample in [("coin", fair_coin), ("exponential", skewed), ("bimodal", bimodal)]:
    running = np.cumsum(sample) / np.arange(1, n_paths + 1)
    print(f"{name:12s} population mean {sample.mean():7.4f}  "
          f"running mean at n=30,000 {running[-1]:7.4f}  "
          f"at n=100 {running[99]:7.4f}  at n=10 {running[9]:7.4f}")
```

```python
# The size of the error falls like 1/sqrt(n), not like 1/n.
sample = skewed
for n in (100, 1_000, 10_000, 30_000):
    running = np.cumsum(sample[:n]) / np.arange(1, n + 1)
    print(f"n = {n:6,}: |running mean - mu| = {abs(running[-1] - 2.0):.4f}  "
          f"1/sqrt(n) = {1/np.sqrt(n):.4f}")
```

### 6.2 The CLT for three population shapes

```python
def sample_means(generator, n, reps, seed):
    rng = np.random.default_rng(seed)
    return np.array([generator(rng, n).mean() for _ in range(reps)])

populations = {
    "uniform": lambda r, n: r.uniform(0, 1, n),
    "exponential": lambda r, n: r.exponential(2.0, n),
    "bimodal": lambda r, n: np.where(r.random(n) < 0.5,
                                     r.normal(2, 0.7, n),
                                     r.normal(9, 0.7, n)),
}

reps = 4_000
for name, gen in populations.items():
    for n in (2, 5, 30, 100):
        means = sample_means(gen, n, reps, seed=hash(name) % 1000 + n)
        z = (means - means.mean()) / means.std(ddof=1)
        print(f"{name:12s} n={n:3d}: skew(z) {stats.skew(z):+.3f}  "
              f"excess kurtosis {stats.kurtosis(z):+.3f}  "
              f"P(|z|>1.96) {(np.abs(z) > 1.96).mean():.3f}")
    print()
```

### 6.3 Standardised means against the normal curve

```python
rng = np.random.default_rng(5)
n = 30
means = np.array([rng.exponential(2.0, n).mean() for _ in range(20_000)])
se = 2.0 / np.sqrt(n)
z = (means - 2.0) / se

print(f"mean of z  : {z.mean():+.4f}")
print(f"sd of z    : {z.std(ddof=1):.4f}   (theory 1)")
print(f"P(z < 1.96)  : {np.mean(z < 1.96):.4f}  (normal {stats.norm.cdf(1.96):.4f})")
print(f"P(|z| > 2)   : {np.mean(np.abs(z) > 2):.4f}  (normal {2*(1-stats.norm.cdf(2)):.4f})")
```

### 6.4 A probability by CLT, checked by simulation

```python
mu, sigma_single, n = 2.0, 2.0, 49
threshold = 2.5
se = sigma_single / np.sqrt(n)
clt_prob = 1 - stats.norm.cdf((threshold - mu) / se)

rng = np.random.default_rng(11)
sim = np.array([rng.exponential(2.0, n).mean() for _ in range(20_000)])
print(f"se = {se:.4f}")
print(f"CLT:  P(mean > {threshold}) = {clt_prob:.4f}")
print(f"sim:  P(mean > {threshold}) = {(sim > threshold).mean():.4f}")
print(f"difference = {(sim > threshold).mean() - clt_prob:+.4f}")
```

### 6.5 When the CLT fails: infinite variance and no mean

```python
# Pareto with shape 1.5: infinite variance. The mean exists, the variance does not.
rng = np.random.default_rng(21)
n = 500
pareto_means = np.array([(rng.pareto(1.5, n) + 1).mean() for _ in range(5_000)])
z_pareto = (pareto_means - pareto_means.mean()) / pareto_means.std(ddof=1)
print(f"Pareto(1.5), n={n}: skew of standardised means {stats.skew(z_pareto):+.3f}, "
      f"kurtosis {stats.kurtosis(z_pareto):+.3f}")
print(f"P(|z| > 1.96) = {(np.abs(z_pareto) > 1.96).mean():.3f}  (normal 0.05)")

# Cauchy: no mean at all. The sample mean has the same distribution as one draw.
rng = np.random.default_rng(22)
for n in (10, 100, 10_000):
    means = np.array([rng.standard_cauchy(n).mean() for _ in range(3_000)])
    print(f"Cauchy n={n:6d}: sd of the sample mean {means.std(ddof=1):8.3f}  "
          f"(theory sd of one draw {np.pi/np.sqrt(3):.3f})")
```

The Cauchy standard deviation does not shrink. The LLN does not apply because
\(\E|X|=\infty\), and no sample size rescues it.

### 6.6 Monte Carlo integration with an error estimate

```python
rng = np.random.default_rng(31)
B = 200_000
u = rng.random(B)
g = np.exp(-u**2)                 # integral of e^{-x^2} on [0,1]
estimate = g.mean()
se = g.std(ddof=1) / np.sqrt(B)

print(f"Monte Carlo estimate : {estimate:.6f}")
print(f"standard error       : {se:.6f}")
print(f"95% interval         : [{estimate - 1.96*se:.6f}, {estimate + 1.96*se:.6f}]")

# A midpoint rule with the same number of evaluations, for comparison.
xs = (np.arange(B) + 0.5) / B
midpoint = np.exp(-xs**2).mean()
print(f"midpoint rule        : {midpoint:.6f}  (much more accurate in 1-D)")
```

Monte Carlo is inefficient in one dimension and indispensable in ten: its error is
\(O(B^{-1/2})\) regardless of dimension, while grid methods degrade exponentially.

## 7. Output and interpretation

- **LLN.** The running mean for the coin settles near 0.5; for the exponential near 2;
  for the bimodal near 5.5. At \(n=10\) the running mean can be far off; the distance
  from the population mean falls roughly like \(1/\sqrt n\).
- **CLT.** At \(n=2\) the *bimodal* population's sample mean is still bimodal: the
  theorem has not taken effect. By \(n=30\) the standardised means are close to normal —
  the uniform essentially exactly, the exponential with residual skewness because it is
  the skewed population. About 5% lie beyond \(\pm1.96\) in the uniform and exponential
  cases, and the approximation improves with \(n\) in all three.
- **A probability.** With \(\sigma=2\), \(n=49\), \(\se=0.2857\), and
  \(\Pr(\bar X>2.5)=1-\Phi(1.75)=0.0401\). The simulation agrees to within about 0.003,
  which is its own standard error.
- **Failure.** For Pareto(1.5) the standardised means remain strongly skewed and
  heavy-tailed at \(n=500\): the normal approximation is poor no matter how the plot is
  drawn. For Cauchy, the sample mean's spread does not shrink at all — 10,000
  observations are worth exactly one.
- **Monte Carlo.** 200,000 uniform draws estimate the integral with a standard error of
  about 0.0004, so the 95% interval is roughly \(\pm0.0008\). The reported standard
  error is the honest uncertainty, and it falls only as \(1/\sqrt B\). The midpoint rule does
  better in one dimension, which is why Monte Carlo is used for integrals that cannot be
  gridded.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.4))
for ax, (name, sample) in zip(axes, [("coin", fair_coin),
                                     ("exponential", skewed),
                                     ("bimodal", bimodal)]):
    running = np.cumsum(sample) / np.arange(1, sample.size + 1)
    ax.plot(running, linewidth=1, color="#4c72b0")
    ax.axhline(sample.mean(), color="#c44e52", linestyle="--", label="population mean")
    ax.set(xscale="log", title=name, xlabel="n (log scale)", ylabel="Running mean")
    ax.legend(frameon=False, fontsize=8)
fig.suptitle("Law of Large Numbers: every path settles on the same value", y=1.02)
fig.tight_layout()
plt.show()
```

```python
fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.4))
for ax, (name, gen) in zip(axes, populations.items()):
    means = sample_means(gen, 30, 4_000, seed=77)
    z = (means - means.mean()) / means.std(ddof=1)
    ax.hist(z, bins=45, density=True, color="#55a868", alpha=0.65, edgecolor="white")
    grid = np.linspace(-4, 4, 300)
    ax.plot(grid, stats.norm.pdf(grid), color="#c44e52", linewidth=2)
    ax.set(title=f"{name}, n=30", xlabel="standardised mean", ylabel="density",
           xlim=(-4, 4))
fig.suptitle("Central Limit Theorem: three population shapes, one limit", y=1.02)
fig.tight_layout()
plt.show()
```

**What to look at.** In the first figure all three paths converge, but at different
speeds and with different noise: the coin is fastest because its variance is smallest
relative to its mean. In the second, the exponential panel still shows a visible right
tail at \(n=30\) — the CLT is an approximation whose quality depends on the population's
skewness, not a promise at a fixed sample size.

## 9. Practical scenario

**Simulating a queue.** A call centre has 20 lines, each call lasting an exponential
time with mean 6 minutes. What is the probability that the total service time for 50
calls exceeds 5 hours, and how uncertain is that estimate?

```python
rng = np.random.default_rng(101)
reps = 100_000
total = rng.exponential(6.0, size=(reps, 50)).sum(axis=1)
prob = (total > 300).mean()
se = np.sqrt(prob * (1 - prob) / reps)
print(f"P(total > 300 minutes) = {prob:.4f} +/- {1.96*se:.4f}")
print(f"mean total {total.mean():.2f} min, sd {total.std(ddof=1):.2f} min")
print(f"CLT check: mean 50*6 = 300, sd sqrt(50)*6 = {np.sqrt(50)*6:.2f}")
```

The CLT also explains the shape: a sum of 50 exponential variables is nearly normal with
mean 300 and standard deviation 42.4, so the probability of exceeding 300 is about 0.5 —
which the simulation confirms. The simulation adds what the CLT cannot: an exact answer
for the tail, where the normal approximation is weakest.

## 10. Exercises

**Exercise 1.** Simulate running means of 10,000 Bernoulli(0.3) draws and report the
absolute error at \(n=10, 100, 1{,}000, 10{,}000\). Compare with \(1/\sqrt n\).

**Exercise 2.** For a uniform population on \([0,10]\), find the smallest \(n\) for which
the sample mean's distribution has skewness below 0.1 in a simulation with 2,000
replications.

**Exercise 3.** Use the CLT to compute \(\Pr(\bar X<48)\) for a population with
\(\mu=50,\sigma=12,n=36\), then check by simulation.

**Exercise 4.** Repeat the Cauchy experiment with 20,000 observations and confirm that
the spread of the sample mean does not shrink.

**Exercise 5.** Use Monte Carlo with 100,000 draws to estimate \(\int_0^1 x^{3}\,dx\) and
report a 95% interval. Compare with the exact value.

## 11. Solutions

```python
# Solution 1
rng = np.random.default_rng(201)
draws = rng.random(10_000) < 0.3
run = np.cumsum(draws) / np.arange(1, draws.size + 1)
for n in (10, 100, 1_000, 10_000):
    print(f"n={n:6,}: error {abs(run[n-1]-0.3):.4f}, 1/sqrt(n) {1/np.sqrt(n):.4f}")
```

```python
# Solution 2
rng = np.random.default_rng(202)
for n in (1, 2, 3, 5, 10, 30):
    means = rng.uniform(0, 10, size=(2000, n)).mean(axis=1)
    print(f"n={n:2d}: skewness {stats.skew(means):+.3f}")
```

```python
# Solution 3
mu, sigma, n = 50, 12, 36
se = sigma / np.sqrt(n)
p = stats.norm.cdf((48 - mu) / se)
rng = np.random.default_rng(203)
sim = rng.normal(mu, sigma, size=(20_000, n)).mean(axis=1)
print(f"CLT {p:.4f}, simulation {(sim < 48).mean():.4f}")
```

```python
# Solution 4
rng = np.random.default_rng(204)
for n in (10, 20_000):
    means = np.array([rng.standard_cauchy(n).mean() for _ in range(2_000)])
    print(f"n={n:6d}: sd of mean {means.std(ddof=1):.3f}")
```

```python
# Solution 5
rng = np.random.default_rng(205)
u = rng.random(100_000)
f = u**3
est = f.mean()
se = f.std(ddof=1) / np.sqrt(u.size)
print(f"estimate {est:.5f} +/- {1.96*se:.5f}; exact 0.25")
```

## 12. Summary

- The LLN says the sample mean converges to the population mean; the strong law says the
  whole path converges with probability one.
- The error of a sample mean falls like \(\sigma/\sqrt n\) — slow, and unavoidable.
- The CLT says standardised means approach \(N(0,1)\) regardless of population shape,
  with accuracy that depends on skewness and on \(n\).
- Finite variance is required; Pareto tails and the Cauchy distribution are counter-
  examples, and no sample size fixes them.
- Monte Carlo uses the LLN to estimate integrals, with error \(O(B^{-1/2})\) independent
  of dimension.

Next: [Practical 14](14-estimation-and-confidence-intervals.ipynb) turns the sampling
distribution into intervals.
