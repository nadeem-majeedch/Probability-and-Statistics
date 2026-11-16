# Practical 15 — Hypothesis Testing

## 1. Introduction

A hypothesis test is a decision rule with a stated error rate. This practical computes
the tests, but its main purpose is to show the two things simulations reveal that
formulas hide:

1. Under the null hypothesis, p-values are **uniformly distributed** — so 5% of true
   nulls give \(p<0.05\) by construction.
2. Power is a property of the design, and it can be measured by simulation before an
   experiment is run.

It closes with the multiplicity arithmetic: twenty tests are almost certain to produce a
"significant" result somewhere.

## 2. Learning objectives

By the end of this practical you can:

1. State hypotheses, compute z and t statistics, and interpret p-values correctly.
2. Run one-sample, two-sample, paired and proportion tests with SciPy.
3. Simulate the Type I error rate and power of a test.
4. Explain why a p-value is not \(\Pr(H_0\mid\text{data})\).
5. Apply Bonferroni and Benjamini–Hochberg corrections.

## 3. Required libraries

| Library | Used for |
|---|---|
| `scipy.stats` | `ttest_1samp`, `ttest_ind`, `ttest_rel`, `proportions_ztest` (statsmodels) |
| `statsmodels.stats.proportion` | two-proportion z-test |
| `numpy`, `matplotlib` | simulation and diagnostics |

## 4. Concepts

### 4.1 The procedure

1. State \(H_0\) and \(H_1\) before looking at the data.
2. Choose a statistic whose distribution under \(H_0\) is known.
3. Compute the statistic and the p-value.
4. Decide, and report the effect size with an interval.

### 4.2 Errors and power

| | \(H_0\) true | \(H_1\) true |
|---|---|---|
| Reject | Type I, probability \(\alpha\) | correct, power \(1-\beta\) |
| Fail to reject | correct | Type II, probability \(\beta\) |

Power rises with the effect size, the sample size, and \(\alpha\), and falls with the
noise \(\sigma\).

### 4.3 What a p-value is

\[ p=\Pr(T\ \text{at least as extreme}\mid H_0). \]

It is a probability about **data**, computed under \(H_0\). It is not
\(\Pr(H_0\mid\text{data})\): converting one into the other requires a prior, by Bayes.
A small p-value says the data are unlikely if \(H_0\) holds; it does not say \(H_0\) is
unlikely, nor that the effect is large.

### 4.4 Multiplicity

With \(m\) independent tests at level \(\alpha\),

\[ \Pr(\text{at least one false positive})=1-(1-\alpha)^{m}. \]

Bonferroni uses \(\alpha/m\) per test (controls the family-wise error rate);
Benjamini–Hochberg controls the false discovery rate, which is less conservative.

## 5. Formulas

\[ z=\frac{\bar x-\mu_0}{\sigma/\sqrt n},\qquad
   t=\frac{\bar x-\mu_0}{s/\sqrt n}\sim t_{n-1} \]

\[ t=\frac{\bar x_1-\bar x_2}{s_p\sqrt{1/n_1+1/n_2}},\qquad
   s_p^{2}=\frac{(n_1-1)s_1^{2}+(n_2-1)s_2^{2}}{n_1+n_2-2} \]

\[ z=\frac{\hat p-p_0}{\sqrt{p_0(1-p_0)/n}},\qquad
   n\approx\frac{2(z_{1-\alpha/2}+z_{1-\beta})^{2}\sigma^{2}}{\Delta^{2}} \]

## 6. Implementation

### 6.1 One-sample z and t tests

```python
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)

# z test: sigma known
x = rng.normal(52, 9, size=100)
sigma, mu0 = 9.0, 50.0
z = (x.mean() - mu0) / (sigma / np.sqrt(x.size))
p_two = 2 * (1 - stats.norm.cdf(abs(z)))
print(f"z test: xbar {x.mean():.3f}, z {z:.4f}, p {p_two:.4f}")
print(f"95% CI: [{x.mean() - 1.96*sigma/np.sqrt(x.size):.3f}, "
      f"{x.mean() + 1.96*sigma/np.sqrt(x.size):.3f}]")

# t test: sigma estimated, small sample
small = rng.normal(68, 8, size=10)
res = stats.ttest_1samp(small, popmean=70)
print(f"\nt test: xbar {small.mean():.3f}, t {res.statistic:.4f}, "
      f"p {res.pvalue:.4f}, df {small.size-1}")
print(f"critical value {stats.t.ppf(0.975, small.size-1):.4f}")
```

### 6.2 Two-sample and paired tests

```python
g1 = rng.normal(68, 9, 20)
g2 = rng.normal(62, 11, 25)

pooled = stats.ttest_ind(g1, g2, equal_var=True)
welch = stats.ttest_ind(g1, g2, equal_var=False)
print(f"pooled t {pooled.statistic:.4f}, p {pooled.pvalue:.4f}")
print(f"Welch  t {welch.statistic:.4f}, p {welch.pvalue:.4f}")

before = rng.normal(60, 8, 20)
after = before + rng.normal(2.5, 4, 20)
paired = stats.ttest_rel(after, before)
print(f"paired t {paired.statistic:.4f}, p {paired.pvalue:.4f}")

d = after - before
ci = stats.t.interval(0.95, df=d.size-1, loc=d.mean(), scale=d.std(ddof=1)/np.sqrt(d.size))
print(f"mean difference {d.mean():.3f}, 95% CI [{ci[0]:.3f}, {ci[1]:.3f}]")
```

### 6.3 A proportion test

```python
count, nobs = 90, 400
stat, pval = proportions_ztest(count, nobs, value=0.20)
print(f"p-hat {count/nobs:.4f}, z {stat:.4f}, p {pval:.4f}")

# Two proportions
stat2, pval2 = proportions_ztest([140, 120], [1000, 1000])
print(f"two-proportion z {stat2:.4f}, p {pval2:.4f}")
```

### 6.4 The p-value is uniform under the null

```python
rng = np.random.default_rng(7)
reps = 8_000
pvals = np.array([stats.ttest_1samp(rng.normal(50, 10, 25), popmean=50).pvalue
                  for _ in range(reps)])

print(f"share of p < 0.05 : {(pvals < 0.05).mean():.4f}  (expected 0.05)")
print(f"share of p < 0.01 : {(pvals < 0.01).mean():.4f}  (expected 0.01)")
print(f"mean p-value      : {pvals.mean():.4f}  (expected 0.50)")
for lo in (0.0, 0.2, 0.4, 0.6, 0.8):
    print(f"  share in [{lo:.1f}, {lo+0.2:.1f}) = {((pvals >= lo) & (pvals < lo+0.2)).mean():.4f}")
```

### 6.5 Power by simulation, and the four-way trade-off

```python
def simulate_power(effect, n, sigma=10.0, alpha=0.05, reps=3_000, seed=0):
    rng = np.random.default_rng(seed)
    rejections = 0
    for _ in range(reps):
        sample = rng.normal(50 + effect, sigma, n)
        if stats.ttest_1samp(sample, popmean=50).pvalue < alpha:
            rejections += 1
    return rejections / reps

print(f"{'effect':>7} {'n':>5} {'power':>7}")
for effect in (2, 5, 10):
    for n in (25, 100):
        print(f"{effect:>7} {n:>5} {simulate_power(effect, n, seed=effect*100+n):>7.3f}")
```

```python
# Sample size for 80% power, two-sample, delta = 5, sigma = 10
delta, sigma = 5.0, 10.0
z_a, z_b = stats.norm.ppf(0.975), stats.norm.ppf(0.80)
n_req = 2 * (z_a + z_b)**2 * sigma**2 / delta**2
print(f"required n per group: {n_req:.2f} -> {int(np.ceil(n_req))}")

# Check the achieved power at that n by simulation.
def power_two_sample(n, delta=5.0, sigma=10.0, reps=4_000, seed=1):
    rng = np.random.default_rng(seed)
    hits = 0
    for _ in range(reps):
        a = rng.normal(50, sigma, n)
        b = rng.normal(50 + delta, sigma, n)
        if stats.ttest_ind(a, b).pvalue < 0.05:
            hits += 1
    return hits / reps

for n in (40, 63, 90):
    print(f"n = {n:3d} per group: simulated power {power_two_sample(n, seed=n):.3f}")
```

### 6.6 Multiplicity and corrections

```python
m = 20
alpha = 0.05
print(f"family-wise error with {m} independent tests: {1-(1-alpha)**m:.4f}")

rng = np.random.default_rng(11)
pvals_null = rng.random(20)     # exactly uniform: all nulls are true

from statsmodels.stats.multitest import multipletests

bonf = multipletests(pvals_null, alpha=0.05, method="bonferroni")
bh = multipletests(pvals_null, alpha=0.05, method="fdr_bh")
print(f"smallest p in this set: {pvals_null.min():.4f}")
print(f"Bonferroni rejects: {bonf[0].sum()}, BH rejects: {bh[0].sum()}")
print(f"Bonferroni threshold: {alpha/m:.4f}")
```

### 6.7 What a p-value is not

```python
# Same data, two sample sizes: the effect is identical, the p-value is not.
rng = np.random.default_rng(13)
for n in (20, 200, 2000):
    sample = rng.normal(51.0, 10, n)
    res = stats.ttest_1samp(sample, popmean=50)
    print(f"n={n:5d}: difference {sample.mean()-50:+.2f}, p {res.pvalue:.4f}, "
          f"95% CI half-width {1.96*10/np.sqrt(n):.2f}")
```

The difference is about one mark in every case; only the sample size changes, and the
p-value moves from 0.6 to 0.0001. That is what "p depends on \(n\)" means — and why an
effect size is not optional.

## 7. Output and interpretation

- **z and t tests.** The z test with \(\sigma\) known gives \(z\approx2.2\) and a p-value
  near 0.03; the t test with \(n=10\) gives a p-value near 0.45, because ten observations
  cannot resolve a 2-unit difference against a standard deviation of 8.
- **Two-sample.** Pooled and Welch statistics are close here because the group sizes are
  moderate and the variances similar; with unequal variances Welch is the safer report.
- **Paired.** The paired test has far more power than an unpaired comparison of the same
  data whenever the within-person correlation is positive.
- **Uniformity.** Under \(H_0\), 5.0% of p-values fall below 0.05, 1.0% below 0.01, the
  mean is 0.50, and each fifth of the range contains about 20%. This is the single most
  important simulation in the chapter: it shows that false positives are produced by the
  procedure at exactly the advertised rate.
- **Power.** Power rises steeply with the standardised effect: at \(\sigma=10\), an effect
  of 5 with \(n=63\) per group gives about 0.80, while \(n=40\) gives about 0.60. The
  simulation and the formula agree, which is a check on both.
- **Multiplicity.** Twenty independent null tests give a 64% chance of at least one
  \(p<0.05\). The printed rejection counts are small for both procedures, as they should
  be when every null is true; the difference is that BH's threshold is larger than
  Bonferroni's, so BH has more power once some alternatives are real. That is the trade:
  family-wise error control versus false discovery rate control.
- **p depends on n.** The same 1-mark difference produces p-values from 0.6 to 0.0001 as
  \(n\) grows, so a small p-value is not evidence of a large effect.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

axes[0].hist(pvals, bins=20, color="#4c72b0", edgecolor="white")
axes[0].axhline(reps/20, color="#c44e52", linestyle="--", label="expected count")
axes[0].set(title="p-values under a true null are uniform",
            xlabel="p-value", ylabel="Count")
axes[0].legend(frameon=False)

effects = np.linspace(0, 12, 9)
for n, style in [(25, ":"), (63, "--"), (150, "-")]:
    powers = [simulate_power(e, n, reps=400, seed=int(e*10)+n) for e in effects]
    axes[1].plot(effects, powers, style, label=f"n = {n}")
axes[1].axhline(0.8, color="grey", linestyle=":", linewidth=1)
axes[1].set(xlabel="True effect (units of the mean)", ylabel="Power",
            title="Power curves: bigger effects and bigger samples")
axes[1].legend(frameon=False)

fig.tight_layout()
plt.show()
```

**What to look at.** The left histogram is flat: every p-value bin is equally likely when
the null is true, including the first one. The right panel shows that power is a
continuous function of the effect, not a property of the test: the same test is
excellent for large effects and useless for small ones.

## 9. Practical scenario

**An A/B test that is significant and wrong.** A team tests 20 button colours on 500
users each, finds \(p=0.03\) for one variant, and ships it.

```python
m = 20
p_any = 1 - (1 - 0.05)**m
print(f"P(at least one false positive among {m} tests) = {p_any:.3f}")

# What the observed effect looks like with an interval.
rng = np.random.default_rng(21)
base = rng.binomial(500, 0.10, 20) / 500
lift = (base - 0.10)
print(f"observed lifts: min {lift.min():+.3f}, max {lift.max():+.3f}, "
      f"sd {lift.std(ddof=1):.3f}")
print(f"expected sd of a 10% rate at n=500: {np.sqrt(0.1*0.9/500):.3f}")
print(f"so a 'best of 20' lift of about {lift.max():+.1%} is within noise")
```

The largest of twenty noisy estimates is large by construction. The correct procedure was
to pre-register one primary metric and one analysis, or to apply a multiplicity
correction — and to size the experiment for the effect the team actually cares about.

## 10. Exercises

**Exercise 1.** Test \(H_0:\mu=100\) against a two-sided alternative with
\(\bar x=104\), \(s=12\), \(n=36\). Report t, df, p and the 95% interval.

**Exercise 2.** Simulate the Type I error rate of a two-sample t test at \(\alpha=0.05\)
with \(n=15\) per group, using 5,000 replications.

**Exercise 3.** For \(\Delta=3\), \(\sigma=8\), compute the sample size per group for 80%
power and check it by simulation.

**Exercise 4.** Twenty independent tests each have a true null. Simulate the family-wise
error rate without correction and with Bonferroni.

**Exercise 5.** Write two sentences explaining why \(p=0.04\) does not mean there is a 96%
chance the alternative is true.

## 11. Solutions

```python
# Solution 1
t = (104 - 100) / (12 / 6)
p = 2 * (1 - stats.t.cdf(abs(t), 35))
ci = stats.t.interval(0.95, df=35, loc=104, scale=2)
print(f"t = {t:.4f}, df = 35, p = {p:.4f}")
print(f"95% CI [{ci[0]:.3f}, {ci[1]:.3f}]")
```

```python
# Solution 2
rng = np.random.default_rng(401)
false_pos = 0
for _ in range(5000):
    a = rng.normal(50, 10, 15)
    b = rng.normal(50, 10, 15)
    if stats.ttest_ind(a, b).pvalue < 0.05:
        false_pos += 1
print(f"Type I error rate: {false_pos/5000:.4f}  (nominal 0.05)")
```

```python
# Solution 3
delta, sigma = 3, 8
n = 2 * (1.96 + 0.8416)**2 * sigma**2 / delta**2
print(f"n per group = {n:.1f} -> {int(np.ceil(n))}")
print(f"simulated power at {int(np.ceil(n))}: {power_two_sample(int(np.ceil(n)), delta=3, sigma=8, seed=7):.3f}")
```

```python
# Solution 4
rng = np.random.default_rng(402)
fam_uncorrected = 0
fam_bonf = 0
for _ in range(2000):
    ps = rng.random(20)
    fam_uncorrected += (ps < 0.05).any()
    fam_bonf += (ps < 0.05/20).any()
print(f"uncorrected: {fam_uncorrected/2000:.3f}  (theory {1-0.95**20:.3f})")
print(f"Bonferroni : {fam_bonf/2000:.4f}  (theory about 0.05)")
```

```python
# Solution 5 (written)
# The p-value is the probability of data this extreme *if the null were true*; it is
# not the probability of the null. Turning it into P(H0 | data) needs a prior, and with
# many hypotheses tested, most small p-values come from true nulls -- so 1 - p is not
# the probability that the alternative holds.
```

## 12. Summary

- A test compares a statistic to its distribution under \(H_0\); the p-value is the tail
  area beyond the observed value.
- \(\alpha\) is the Type I error rate and \(\beta\) the Type II rate; power \(=1-\beta\)
  grows with effect size and sample size.
- Under \(H_0\), p-values are uniform: 5% of true nulls are "significant" at 5%.
- A p-value is \(\Pr(\text{data}\mid H_0)\), not \(\Pr(H_0\mid\text{data})\), and it
  depends on \(n\) as well as on the effect.
- Multiplicity inflates the error rate; Bonferroni controls the family-wise rate, BH the
  false discovery rate.
- Report effect sizes and intervals beside every p-value.

Next: [Practical 16](16-correlation-and-regression.ipynb) applies these ideas to
relationships between variables.
