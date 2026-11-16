# Practical 14 — Estimation and Confidence Intervals

## 1. Introduction

A point estimate is a single number; an interval estimate says how wrong that number
might be. This practical computes both, and then does something a textbook cannot: it
draws thousands of samples and **counts how often the interval contains the true
parameter**. That count is what "95% confidence" means, and seeing it is the fastest way
to stop misreading a confidence interval as a probability about the parameter.

## 2. Learning objectives

By the end of this practical you can:

1. Compute point estimates and explain unbiasedness and mean squared error.
2. Fit a maximum-likelihood estimate for an exponential and a Bernoulli model.
3. Construct and interpret z, t, proportion and two-sample confidence intervals.
4. Verify coverage by simulation, and explain the difference between coverage and
   posterior probability.
5. Compute the sample size needed for a target margin of error.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | sampling and simulation |
| `scipy.stats` | normal and t quantiles |
| `matplotlib` | interval plots and coverage |

## 4. Concepts

### 4.1 Estimators and their properties

An **estimator** is a rule (a statistic); an **estimate** is its value on one sample.

- **Unbiased:** \(\E[\hat\theta]=\theta\). \(\bar X\) and \(s^{2}\) (with \(n-1\)) are
  unbiased for \(\mu\) and \(\sigma^{2}\); the MLE \(\hat\sigma^{2}\) (with \(n\)) is not.
- **Consistent:** \(\hat\theta\to\theta\) in probability as \(n\to\infty\).
- **Efficient:** small variance among unbiased estimators.

**Mean squared error** combines both:

\[ \text{MSE}(\hat\theta)=\Var(\hat\theta)+\text{bias}(\hat\theta)^{2}. \]

A biased estimator with much smaller variance can have lower MSE — that is the case for
shrinkage estimators, and the reason they are used.

### 4.2 Maximum likelihood

The likelihood is the probability of the observed data as a function of the parameter;
the MLE maximises it (equivalently, the log-likelihood). For an exponential,
\(\hat\lambda=1/\bar x\); for a Bernoulli, \(\hat p=x/n\); for a normal,
\(\hat\mu=\bar x\) and \(\hat\sigma^{2}=\frac1n\sum(x_i-\bar x)^{2}\).

### 4.3 Interval construction

Every interval has the same skeleton:

\[ \text{estimate}\ \pm\ \text{critical value}\times\text{standard error}. \]

| Parameter | Interval | Critical value |
|---|---|---|
| Mean, \(\sigma\) known | \(\bar x\pm z\,\sigma/\sqrt n\) | \(z_{1-\alpha/2}\) |
| Mean, \(\sigma\) estimated | \(\bar x\pm t\,s/\sqrt n\) | \(t_{n-1}\) |
| Proportion (Wald) | \(\hat p\pm z\sqrt{\hat p(1-\hat p)/n}\) | \(z\) |
| Difference of means | \((\bar x_1-\bar x_2)\pm t\,s_p\sqrt{1/n_1+1/n_2}\) | \(t_{n_1+n_2-2}\) |
| Paired difference | \(\bar d\pm t\,s_d/\sqrt n\) | \(t_{n-1}\) |

### 4.4 What 95% confidence means

If the procedure is repeated on many samples, 95% of the intervals produced contain
\(\theta\). It does **not** mean that a particular computed interval has a 95% chance of
containing \(\theta\): after the data are in, the interval either contains it or does
not, and the probability statement is about the procedure.

## 5. Formulas

\[ \bar x\pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n},\qquad
   \bar x\pm t_{n-1,1-\alpha/2}\frac{s}{\sqrt n} \]

\[ \hat p\pm z\sqrt{\frac{\hat p(1-\hat p)}{n}}\quad\text{(Wald)} \]

\[ n=\left(\frac{z\sigma}{m}\right)^{2}\quad\text{for margin }m \]

\[ \text{MSE}=\Var(\hat\theta)+[\text{bias}(\hat\theta)]^{2} \]

## 6. Implementation

### 6.1 Point estimates and bias

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)
sigma_true = 10.0
mu_true = 50.0
reps, n = 20_000, 8

samples = rng.normal(mu_true, sigma_true, size=(reps, n))
xbar = samples.mean(axis=1)
s2_unbiased = samples.var(axis=1, ddof=1)
s2_mle = samples.var(axis=1, ddof=0)

print(f"E[mean]        = {xbar.mean():.4f}   (mu = {mu_true})")
print(f"E[s^2 ddof=1]  = {s2_unbiased.mean():.4f}   (sigma^2 = {sigma_true**2:.1f})")
print(f"E[s^2 ddof=0]  = {s2_mle.mean():.4f}   ratio to sigma^2 {s2_mle.mean()/sigma_true**2:.4f}")
print(f"(n-1)/n        = {(n-1)/n:.4f}")

print(f"\nVar(mean)      = {xbar.var(ddof=1):.4f}   theory {sigma_true**2/n:.4f}")
print(f"MSE of s2_mle  = {((s2_mle - sigma_true**2)**2).mean():.4f}")
```

### 6.2 Maximum likelihood, numerically and in closed form

```python
rng = np.random.default_rng(7)
data = rng.exponential(scale=4.0, size=60)      # mean 4 -> lambda 0.25

def neg_log_lik(lam, x):
    """Negative log-likelihood for an exponential sample."""
    return -(len(x) * np.log(lam) - lam * x.sum())

grid = np.linspace(0.05, 0.8, 4000)
nll = np.array([neg_log_lik(lam, data) for lam in grid])
lam_grid = grid[nll.argmin()]

lam_closed = 1 / data.mean()
print(f"grid search   lambda_hat = {lam_grid:.5f}")
print(f"closed form 1/xbar       = {lam_closed:.5f}")
print(f"difference               = {abs(lam_grid - lam_closed):.2e}")

# Asymptotic standard error of the MLE: 1/sqrt(n I(lambda)) with I = 1/lambda^2.
se_mle = lam_closed / np.sqrt(len(data))
print(f"approximate 95% interval for lambda: "
      f"[{lam_closed - 1.96*se_mle:.4f}, {lam_closed + 1.96*se_mle:.4f}]")
```

### 6.3 z and t intervals for a mean

```python
rng = np.random.default_rng(11)
sample = rng.normal(52, 9, size=16)
xbar = sample.mean()
s = sample.std(ddof=1)

z_crit = stats.norm.ppf(0.975)
t_crit = stats.t.ppf(0.975, df=len(sample)-1)

z_ci = (xbar - z_crit * s/np.sqrt(16), xbar + z_crit * s/np.sqrt(16))
t_ci = (xbar - t_crit * s/np.sqrt(16), xbar + t_crit * s/np.sqrt(16))

print(f"xbar = {xbar:.3f}, s = {s:.3f}")
print(f"z crit {z_crit:.4f}, t crit {t_crit:.4f}")
print(f"z interval: [{z_ci[0]:.3f}, {z_ci[1]:.3f}]")
print(f"t interval: [{t_ci[0]:.3f}, {t_ci[1]:.3f}]")
print(f"t is wider by {(t_ci[1]-t_ci[0]) - (z_ci[1]-z_ci[0]):.3f}")

# Compare with SciPy's built-in interval.
ci = stats.t.interval(0.95, df=15, loc=xbar, scale=s/np.sqrt(16))
print(f"scipy.stats.t.interval: [{ci[0]:.3f}, {ci[1]:.3f}]")
```

### 6.4 Proportion intervals: Wald, Wilson, and the failure case

```python
def wald_ci(k, n, conf=0.95):
    p = k / n
    z = stats.norm.ppf(1 - (1 - conf)/2)
    se = np.sqrt(p * (1 - p) / n)
    return p - z*se, p + z*se

def wilson_ci(k, n, conf=0.95):
    p = k / n
    z = stats.norm.ppf(1 - (1 - conf)/2)
    denom = 1 + z*z/n
    centre = (p + z*z/(2*n)) / denom
    half = z/denom * np.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return centre - half, centre + half

for k, n in [(5, 20), (0, 20), (350, 400)]:
    w, wi = wald_ci(k, n), wilson_ci(k, n)
    print(f"k={k:3d}, n={n:3d}  p-hat={k/n:.3f}  "
          f"Wald [{w[0]:.3f}, {w[1]:.3f}]  Wilson [{wi[0]:.3f}, {wi[1]:.3f}]")
```

The Wald interval collapses to a point when \(k=0\) and can extend below zero — a
probability interval that contains impossible values. Wilson stays inside \((0,1)\) and
is the safer default.

### 6.5 Two-sample and paired intervals

```python
rng = np.random.default_rng(21)
g1 = rng.normal(68, 9, 20)
g2 = rng.normal(62, 11, 25)

n1, n2 = len(g1), len(g2)
sp2 = ((n1-1)*g1.var(ddof=1) + (n2-1)*g2.var(ddof=1)) / (n1+n2-2)
se = np.sqrt(sp2 * (1/n1 + 1/n2))
tcrit = stats.t.ppf(0.975, df=n1+n2-2)
diff = g1.mean() - g2.mean()

print(f"pooled variance {sp2:.3f}, se {se:.3f}")
print(f"difference {diff:.3f}, 95% CI [{diff - tcrit*se:.3f}, {diff + tcrit*se:.3f}]")

# Welch interval (unequal variances) for comparison.
welch = stats.ttest_ind(g1, g2, equal_var=False)
print(f"Welch t = {welch.statistic:.3f}, p = {welch.pvalue:.4f}")
```

```python
# Paired data: analyse the differences.
before = rng.normal(60, 8, 15)
after = before + rng.normal(3, 4, 15)
d = after - before

d_ci = stats.t.interval(0.95, df=len(d)-1, loc=d.mean(), scale=d.std(ddof=1)/np.sqrt(len(d)))
print(f"mean difference {d.mean():.3f}, sd {d.std(ddof=1):.3f}")
print(f"paired 95% CI: [{d_ci[0]:.3f}, {d_ci[1]:.3f}]")
print(f"ignoring pairing: width {2*stats.t.ppf(0.975, 28)*np.sqrt(2*8**2/15):.3f} "
      f"(wider because between-person variation is not removed)")
```

### 6.6 Coverage: the experiment that defines confidence

```python
rng = np.random.default_rng(42)
true_mu, true_sigma = 100.0, 15.0
n = 25
reps = 10_000

samples = rng.normal(true_mu, true_sigma, size=(reps, n))
xbar = samples.mean(axis=1)
s = samples.std(axis=1, ddof=1)
half = stats.t.ppf(0.975, df=n-1) * s / np.sqrt(n)

lower, upper = xbar - half, xbar + half
covered = (lower <= true_mu) & (true_mu <= upper)
print(f"coverage over {reps:,} samples: {covered.mean():.4f}")
print(f"standard error of that estimate: {np.sqrt(covered.mean()*(1-covered.mean())/reps):.4f}")

# A 90% interval should cover 90% of the time.
half90 = stats.t.ppf(0.95, df=n-1) * s / np.sqrt(n)
covered90 = ((xbar - half90) <= true_mu) & (true_mu <= (xbar + half90))
print(f"90% interval coverage: {covered90.mean():.4f}")
```

## 7. Output and interpretation

- **Bias.** The mean and \(s^{2}\) with \(n-1\) average to 50 and 100 as theory says. The
  MLE variance averages to \(0.875\times100=87.5\), exactly \((n-1)/n\), so it is biased
  downward by 12.5% at \(n=8\). Its MSE is larger than the unbiased estimator's variance
  for this model.
- **MLE.** The grid search and \(1/\bar x\) agree to five decimal places, which is what
  maximum likelihood means: locate the peak or solve the score equation, same answer. The
  asymptotic standard error gives an interval that is only approximate at \(n=60\).
- **z versus t.** With \(n=16\), \(t_{15}=2.131\) against \(z=1.96\), so the t interval is
  about 9% wider. At \(n=100\) the gap is under 2%; at \(n=5\) it is nearly 50%. The t
  correction is the price of estimating \(\sigma\).
- **Proportions.** At \(k=5, n=20\) Wald and Wilson are similar. At \(k=0\) Wald gives
  \([0,0]\) — an interval claiming certainty from 20 trials — while Wilson gives
  \([0,0.161]\), which is honest.
- **Coverage.** The 95% t intervals contain the true mean 95% of the time (within
  \(\pm0.002\)), and the 90% intervals 90%. Each individual interval either covers or does
  not; the 95% is a property of the procedure, demonstrated by repetition.
- **Pairing.** The paired interval is much narrower than the interval that ignores
  pairing, because the between-person variation cancels in the differences.

## 8. Visualisation

```python
fig, ax = plt.subplots(figsize=(7.2, 4.2))
show = 100
idx = np.arange(show)
ax.errorbar(idx, xbar[:show], yerr=half[:show], fmt="o", markersize=3,
            linewidth=0.8, capsize=0, color="#4c72b0", alpha=0.7)
missed = ~covered[:show]
ax.errorbar(idx[missed], xbar[:show][missed], yerr=half[:show][missed],
            fmt="o", markersize=3, linewidth=0.8, capsize=0, color="#c44e52")
ax.axhline(true_mu, color="black", linestyle="--", label=f"true mean {true_mu}")
ax.set(xlabel="Sample number", ylabel="95% confidence interval",
       title="100 intervals: the red ones miss the true mean")
ax.legend(frameon=False)
fig.tight_layout()
plt.show()

print(f"intervals shown: {show}, missed: {int(missed.sum())}")
```

```python
ns = np.array([5, 10, 25, 50, 100, 400])
half_width = stats.t.ppf(0.975, df=ns-1) * true_sigma / np.sqrt(ns)

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(ns, half_width, "o-", color="#55a868")
ax.set(xscale="log", yscale="log", xlabel="Sample size (log)",
       ylabel="Half-width of 95% interval (log)",
       title="Precision improves as 1/sqrt(n)")
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
plt.show()
```

**What to look at.** In the first figure most vertical bars cross the dashed line and a
few do not; about 5 of 100 miss, by construction. The second figure's straight log–log
line has slope \(-1/2\): to halve the interval you need four times the data.

## 9. Practical scenario

**Estimating a conversion rate.** A checkout variant has 37 conversions in 400 sessions.
The team wants a 95% interval and a recommendation about the sample size needed to
detect a 2-percentage-point improvement over the 8% baseline.

```python
k, n = 37, 400
lo, hi = wilson_ci(k, n)
print(f"p-hat = {k/n:.4f}, 95% Wilson interval [{lo:.4f}, {hi:.4f}]")
print(f"width = {hi-lo:.4f}")

p0, delta = 0.0925, 0.02
z_a, z_b = 1.96, 0.8416
n_needed = 2 * (z_a + z_b)**2 * p0 * (1-p0) / delta**2
print(f"\nsessions per arm for 80% power to detect {delta:.0%}: {np.ceil(n_needed):.0f}")
print(f"currently have {n}, so the experiment is underpowered by "
      f"a factor of {np.ceil(n_needed)/n:.1f}")
```

The interval is wide (±4 points) relative to the effect being sought (2 points), which
is the same message as the power calculation: this experiment cannot answer the
question, and the honest recommendation is to keep collecting data rather than to
interpret the point estimate.

## 10. Exercises

**Exercise 1.** Draw 10,000 samples of size \(n=12\) from \(N(70, 8^{2})\) and report
the mean of \(s^{2}\) with `ddof=0` and `ddof=1`.

**Exercise 2.** For a sample with \(\bar x=42\), \(s=6\), \(n=25\), construct the 95% t
interval and the 99% t interval.

**Exercise 3.** With 12 successes in 50 trials, compute the Wald and Wilson 95%
intervals and explain which you would report.

**Exercise 4.** Run the coverage simulation for \(n=10\) and confirm that the 95% t
interval still covers about 95%.

**Exercise 5.** A pilot gives \(s=250\). How large a sample is needed for a 95% margin of
error of 40?

## 11. Solutions

```python
# Solution 1
rng = np.random.default_rng(301)
s = rng.normal(70, 8, size=(10_000, 12))
print(f"mean s^2 ddof=0: {s.var(axis=1, ddof=0).mean():.4f}")
print(f"mean s^2 ddof=1: {s.var(axis=1, ddof=1).mean():.4f}")
print(f"sigma^2 = 64, (n-1)/n = {(12-1)/12:.4f}")
```

```python
# Solution 2
for conf in (0.95, 0.99):
    lo, hi = stats.t.interval(conf, df=24, loc=42, scale=6/5)
    print(f"{conf:.0%}: [{lo:.3f}, {hi:.3f}] width {hi-lo:.3f}")
```

```python
# Solution 3
k, n = 12, 50
print("Wald  :", tuple(round(v, 4) for v in wald_ci(k, n)))
print("Wilson:", tuple(round(v, 4) for v in wilson_ci(k, n)))
# Report Wilson: with n*p-hat = 12 the normal approximation behind Wald is shaky,
# and Wilson never produces limits outside [0, 1].
```

```python
# Solution 4
rng = np.random.default_rng(302)
n = 10
smp = rng.normal(100, 15, size=(10_000, n))
xb, sd = smp.mean(axis=1), smp.std(axis=1, ddof=1)
h = stats.t.ppf(0.975, n-1) * sd / np.sqrt(n)
cov = ((xb - h) <= 100) & (100 <= (xb + h))
print(f"coverage at n=10: {cov.mean():.4f}")
```

```python
# Solution 5
z = 1.96
s = 250
m = 40
print(f"n = {(z*s/m)**2:.1f} -> {int(np.ceil((z*s/m)**2))}")
```

## 12. Summary

- An estimator is a rule; its quality is judged by bias, variance and MSE together.
- MLE maximises the likelihood; for the exponential it is \(1/\bar x\), for a proportion
  \(x/n\), for a normal mean \(\bar x\).
- Every interval is estimate \(\pm\) critical value \(\times\) standard error; t replaces
  z when \(\sigma\) is estimated, and the difference matters at small \(n\).
- Wald intervals fail near 0 and 1; Wilson stays inside \((0,1)\).
- Coverage is a property of the procedure: 95% of intervals from repeated samples
  contain the parameter. It is not the probability that a given interval does.
- Pairing removes between-unit variance and narrows intervals substantially.

Next: [Practical 15](15-hypothesis-testing.ipynb) formalises the decision procedure.
