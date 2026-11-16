# Practical 18 — Bayesian Statistics and Data-Science Methods

## 1. Introduction

This final practical covers the computational habits a data scientist uses most: updating
a belief with data, estimating uncertainty by resampling, testing by randomisation, and
evaluating a model honestly.

The Bayesian section shows the posterior as a distribution and compares it with the
maximum-likelihood answer. The resampling section builds intervals and p-values without
distributional formulas. The final section turns to machine learning, where the
statistical question becomes "how uncertain is this metric?".

## 2. Learning objectives

By the end of this practical you can:

1. Update a Beta prior with Bernoulli data and plot the posterior.
2. Interpret a credible interval, and compare it with a confidence interval.
3. Estimate a standard error and an interval by bootstrap.
4. Test a hypothesis by permutation, with no distributional assumption.
5. Quantify the uncertainty in an A/B result and in a model's test accuracy.

## 3. Required libraries

| Library | Used for |
|---|---|
| `scipy.stats` | Beta, binomial, normal |
| `numpy`, `pandas` | data and simulation |
| `sklearn` | classification, cross-validation, calibration |
| `matplotlib` | posterior and bootstrap plots |

## 4. Concepts

### 4.1 Bayes' theorem for a proportion

\[ p(\theta\mid y)\propto p(y\mid\theta)\,p(\theta). \]

With \(\theta\sim\text{Beta}(a,b)\) and \(s\) successes in \(n\) trials,

\[ \theta\mid y\sim\text{Beta}(a+s,\;b+n-s). \]

The posterior mean is a weighted compromise between the prior mean and \(s/n\), and the
weights are the amounts of information.

### 4.2 Credible intervals

A 95% credible interval has posterior probability 0.95 of containing \(\theta\). It is a
statement about the parameter given the data and the prior. A confidence interval is a
statement about the procedure. They often agree numerically with weak priors, but they
are not the same object.

### 4.3 MLE versus Bayes

The MLE maximises the likelihood and ignores prior information; the posterior mean
shrinks the MLE towards the prior, most strongly when \(n\) is small. For a proportion
near 0 or 1 that shrinkage is what keeps estimates inside \((0,1)\).

### 4.4 The bootstrap

Resample the observed data with replacement, recompute the statistic \(B\) times, and use
the spread:

\[ \se_{\text{boot}}=\text{sd of the }B\text{ replicates},\qquad
   \text{95\% interval}=\text{2.5th to 97.5th percentiles}. \]

It needs no formula for the standard error, which is why it works for medians, ratios and
quantiles.

### 4.5 Permutation tests

Under \(H_0\) the group labels are exchangeable. Shuffle them, recompute the statistic,
and count how often the shuffle is at least as extreme:

\[ \hat p=\frac{1+\#\{b:T_b^{*}\ge T_{\text{obs}}\}}{B+1}. \]

### 4.6 Uncertainty in machine learning

- **Evaluation noise**: accuracy on \(n\) test cases has standard error
  \(\sqrt{\hat p(1-\hat p)/n}\).
- **Model selection**: choosing the best of many configurations inflates the reported
  score, which is why a held-out test set is needed.
- **Calibration**: predicted probabilities should match observed frequencies.
- **Drift**: the population changes, so the metric must be monitored, not assumed.

## 5. Formulas

\[ \theta\mid y\sim\text{Beta}(a+s,\,b+n-s),\qquad
   \E[\theta\mid y]=\frac{a+s}{a+b+n} \]

\[ \se_{\text{boot}}\approx\frac{s_{\text{replicates}}}{\sqrt{1}}
   \quad\text{(the sd of the replicates itself)} \]

\[ \hat p_{\text{perm}}=\frac{1+\#(T^{*}\ge T)}{B+1},\qquad
   \se(\hat p)=\sqrt{\frac{\hat p(1-\hat p)}{n}} \]

\[ \text{VIF}\ \text{aside, for A/B: }\ \se(\hat p_2-\hat p_1)
   =\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}} \]

## 6. Implementation

### 6.1 Bayesian updating for a conversion rate

```python
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

a_prior, b_prior = 2, 3          # Beta(2, 3): mean 0.40, weak
successes, trials = 8, 10

a_post, b_post = a_prior + successes, b_prior + trials - successes
posterior = stats.beta(a_post, b_post)

print(f"prior mean      = {a_prior/(a_prior+b_prior):.4f}")
print(f"MLE (s/n)       = {successes/trials:.4f}")
print(f"posterior mean  = {a_post/(a_post+b_post):.4f}")
print(f"posterior sd    = {posterior.std():.4f}")
lo, hi = posterior.ppf([0.025, 0.975])
print(f"95% credible interval = [{lo:.4f}, {hi:.4f}]")
print(f"P(theta > 0.5 | data) = {posterior.sf(0.5):.4f}")
```

```python
grid = np.linspace(0, 1, 500)
fig, ax = plt.subplots(figsize=(6.6, 3.8))
ax.plot(grid, stats.beta(a_prior, b_prior).pdf(grid), label="prior Beta(2,3)",
        color="grey", linestyle="--")
ax.plot(grid, stats.beta(successes+1, trials-successes+1).pdf(grid),
        label="likelihood (as Beta)", color="#55a868", linestyle=":")
ax.plot(grid, posterior.pdf(grid), label="posterior Beta(10,5)",
        color="#4c72b0", linewidth=2)
ax.axvline(successes/trials, color="#c44e52", linestyle=":", label="MLE 0.8")
ax.set(xlabel="Conversion rate", ylabel="Density",
       title="Prior, likelihood and posterior")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
plt.show()
```

### 6.2 Sequential updating

```python
prior = (1.0, 1.0)                # Beta(1, 1): flat
sequence = [(1, 1), (0, 1), (1, 1), (1, 1), (0, 1), (1, 1), (1, 1), (1, 1)]
a, b = prior
means = []
for successes_i, trials_i in sequence:
    a += successes_i
    b += trials_i - successes_i
    means.append(a / (a + b))

print("update by update:")
print(pd.DataFrame({"step": range(1, len(means)+1),
                    "posterior mean": np.round(means, 4)}).to_string(index=False))
print(f"\nfinal posterior Beta({a:.0f}, {b:.0f}), mean {a/(a+b):.4f}")
```

### 6.3 MLE versus posterior with very little data

```python
for s, n in [(0, 3), (3, 3), (1, 5)]:
    mle = s / n
    post = stats.beta(1 + s, 1 + n - s)
    lo, hi = post.ppf([0.025, 0.975])
    print(f"s={s}, n={n}: MLE {mle:.3f}  posterior mean {post.mean():.3f}  "
          f"95% credible [{lo:.3f}, {hi:.3f}]")
```

The MLE is 0 after three failures and 1 after three successes — estimates that make any
prediction absurd. The posterior never reaches the boundary.

### 6.4 Bootstrap standard error and interval

```python
rng = np.random.default_rng(2026)
data = rng.lognormal(mean=2.0, sigma=0.8, size=200)

def bootstrap_statistic(values, stat_fn, B=5_000, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, values.size, size=(B, values.size))
    replicates = np.apply_along_axis(stat_fn, 1, values[idx])
    return replicates

means = bootstrap_statistic(data, np.mean, seed=1)
medians = bootstrap_statistic(data, np.median, seed=2)

for name, reps, stat_fn in [("mean", means, np.mean), ("median", medians, np.median)]:
    point = stat_fn(data)
    lo, hi = np.percentile(reps, [2.5, 97.5])
    print(f"{name:7s}: estimate {point:7.3f}, bootstrap se {reps.std(ddof=1):.3f}, "
          f"95% percentile interval [{lo:.3f}, {hi:.3f}]")

print(f"\nanalytic se of the mean: {data.std(ddof=1)/np.sqrt(data.size):.3f}")
```

```python
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.hist(means, bins=60, color="#4c72b0", alpha=0.7, edgecolor="white",
        label="bootstrap means")
ax.axvline(np.mean(data), color="#c44e52", linestyle="--", label="sample mean")
ax.set(xlabel="Bootstrap mean", ylabel="Count",
       title="Bootstrap distribution of the mean (5,000 resamples)")
ax.legend(frameon=False)
fig.tight_layout()
plt.show()
```

### 6.5 Permutation test

```python
rng = np.random.default_rng(7)
control = rng.gamma(2.0, 5.0, 60)
treatment = rng.gamma(2.3, 5.0, 60)
observed_diff = treatment.mean() - control.mean()

def permutation_test(a, b, B=10_000, seed=0):
    rng = np.random.default_rng(seed)
    pooled = np.concatenate([a, b])
    n_a = a.size
    count = 0
    for _ in range(B):
        rng.shuffle(pooled)
        diff = pooled[n_a:].mean() - pooled[:n_a].mean()
        if abs(diff) >= abs(observed_diff):
            count += 1
    return (1 + count) / (B + 1)

p_perm = permutation_test(control, treatment, seed=3)
t_test = stats.ttest_ind(control, treatment)
print(f"observed difference {observed_diff:.3f}")
print(f"permutation p = {p_perm:.4f}")
print(f"t test        p = {t_test.pvalue:.4f}")
```

### 6.6 A/B test: two views of the same data

```python
conv_a, n_a = 120, 1000
conv_b, n_b = 140, 1000
p_a, p_b = conv_a/n_a, conv_b/n_b
se_diff = np.sqrt(p_a*(1-p_a)/n_a + p_b*(1-p_b)/n_b)
z = (p_b - p_a) / se_diff

print(f"rates: A {p_a:.3f}, B {p_b:.3f}, difference {p_b-p_a:+.4f}")
print(f"se of difference {se_diff:.4f}")
print(f"z {z:.3f}, two-sided p {2*(1-stats.norm.cdf(abs(z))):.4f}")
print(f"95% CI for the difference [{p_b-p_a-1.96*se_diff:+.4f}, {p_b-p_a+1.96*se_diff:+.4f}]")

# Bayesian view with flat Beta(1,1) priors.
post_a = stats.beta(1+conv_a, 1+n_a-conv_a)
post_b = stats.beta(1+conv_b, 1+n_b-conv_b)
rng = np.random.default_rng(11)
draws_a = post_a.rvs(200_000, random_state=rng)
draws_b = post_b.rvs(200_000, random_state=rng)
print(f"\nP(B > A | data) = {(draws_b > draws_a).mean():.3f}")
print(f"P(lift > 1 point) = {(draws_b - draws_a > 0.01).mean():.3f}")
```

### 6.7 Peeking inflates the error rate

```python
def peeking_false_positive(reps=2_000, looks=5, per_look=200, seed=0):
    rng = np.random.default_rng(seed)
    hits = 0
    for _ in range(reps):
        a = rng.random((looks, per_look)) < 0.10
        b = rng.random((looks, per_look)) < 0.10      # identical true rates
        cum_a = np.cumsum(a.sum(axis=1))
        cum_b = np.cumsum(b.sum(axis=1))
        ns = per_look * np.arange(1, looks+1)
        pa, pb = cum_a/ns, cum_b/ns
        se = np.sqrt(pa*(1-pa)/ns + pb*(1-pb)/ns)
        z = (pb - pa) / se
        if (np.abs(z) > 1.96).any():
            hits += 1
    return hits / reps

print(f"error with one look : 0.050 (by definition)")
print(f"error with five looks: {peeking_false_positive(seed=5):.3f}")
```

### 6.8 Uncertainty in a machine-learning metric

```python
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, roc_auc_score, brier_score_loss

X, y = make_classification(n_samples=2_000, n_features=8, n_informative=5,
                           random_state=2026)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=2026, stratify=y)

clf = LogisticRegression(max_iter=1000).fit(X_train, y_train)
proba = clf.predict_proba(X_test)[:, 1]
pred = (proba >= 0.5).astype(int)

acc = accuracy_score(y_test, pred)
n_test = len(y_test)
se_acc = np.sqrt(acc*(1-acc)/n_test)
print(f"test accuracy {acc:.4f}, n = {n_test}, se {se_acc:.4f}")
print(f"95% interval [{acc-1.96*se_acc:.4f}, {acc+1.96*se_acc:.4f}]")
print(f"AUC {roc_auc_score(y_test, proba):.4f}")
print(f"Brier score {brier_score_loss(y_test, proba):.4f}")

# Cross-validated accuracy: report the spread across folds, not just the mean.
cv = cross_val_score(clf, X, y, cv=5, scoring="accuracy")
print(f"\n5-fold CV: {np.round(cv, 4).tolist()}")
print(f"mean {cv.mean():.4f}, sd across folds {cv.std(ddof=1):.4f}")
```

```python
# Bootstrap the AUC to get an interval that does not assume normality.
rng = np.random.default_rng(21)
aucs = []
for _ in range(1_000):
    idx = rng.integers(0, n_test, n_test)
    aucs.append(roc_auc_score(y_test[idx], proba[idx]))
lo, hi = np.percentile(aucs, [2.5, 97.5])
print(f"bootstrap 95% interval for AUC: [{lo:.4f}, {hi:.4f}]")
```

## 7. Output and interpretation

- **Posterior.** With a Beta(2,3) prior and 8 successes in 10 trials, the posterior is
  Beta(10,5) with mean 0.667, between the prior mean 0.400 and the MLE 0.800. The 95%
  credible interval is about \([0.44, 0.90]\), and the posterior probability that the
  rate exceeds 0.5 is about 0.9 — a direct probability statement the confidence-interval
  framework cannot make.
- **Sequential updating.** Each observation moves the posterior a little; the order does
  not matter, only the final counts. The posterior narrows as data accumulate, which is
  learning made visible.
- **Small samples.** After three failures the MLE is 0, while the posterior mean is 0.25
  with a wide interval. Bayesian estimates stay inside the parameter space, and the width
  states the ignorance honestly.
- **Bootstrap.** The bootstrap standard error of the mean matches
  \(s/\sqrt n\), which validates the method on a case where theory is available. For the
  median there is no simple formula, and the bootstrap still supplies an interval — that
  is its value.
- **Permutation.** The permutation p-value is close to the t-test p-value here, because
  the sample is large enough for the CLT; on small or skewed samples the permutation test
  is the safer choice, since it assumes only exchangeability.
- **A/B test.** The frequentist view gives a p-value near 0.18 and an interval that
  includes zero; the Bayesian view gives a 0.91 probability that B is better — different
  sentences from the same data, and neither justifies shipping without considering the
  effect size and the guardrails.
- **Peeking.** Checking five times and stopping at the first significant result raises the
  false-positive rate from 5% to roughly 14%, even when the two variants are identical.
- **Model evaluation.** Test accuracy comes with a standard error; the AUC interval from
  the bootstrap is wider than a normal approximation would suggest, and the cross-
  validation spread shows how much the estimate moves between folds.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

x = np.linspace(0, 1, 400)
for (s, n), color in zip([(1, 5), (5, 20), (50, 200)], ["#c44e52", "#dd8452", "#4c72b0"]):
    axes[0].plot(x, stats.beta(1+s, 1+n-s).pdf(x), color=color,
                 label=f"{s}/{n} successes")
axes[0].set(title="More data: narrower posterior", xlabel="Rate", ylabel="Density")
axes[0].legend(frameon=False, fontsize=8)

axes[1].hist(medians, bins=60, color="#55a868", alpha=0.75, edgecolor="white")
lo_m, hi_m = np.percentile(medians, [2.5, 97.5])
axes[1].axvline(np.median(data), color="#c44e52", linestyle="--", label="sample median")
axes[1].axvline(lo_m, color="grey", linestyle=":")
axes[1].axvline(hi_m, color="grey", linestyle=":", label="95% interval")
axes[1].set(title="Bootstrap distribution of the median", xlabel="Median", ylabel="Count")
axes[1].legend(frameon=False, fontsize=8)

fig.tight_layout()
plt.show()
```

**What to look at.** In the left panel the three posteriors have the same prior but
different amounts of data: 5 observations give a wide curve, 200 a narrow one. In the
right panel the bootstrap distribution is right-skewed even though the statistic is a
median, which is exactly why the percentile interval is preferred to a symmetric
\(\pm1.96\,\se\) rule here.

## 9. Practical scenario

**Should the team ship the new ranking model?** The offline metric improves from 0.71 to
0.73 AUC, and the online A/B test shows a 0.4% lift in clicks with a 95% interval of
\([-0.2\%, 1.0\%]\).

```python
lift = 0.004
lo, hi = -0.002, 0.010
print(f"point estimate {lift:+.3%}, 95% CI [{lo:+.3%}, {hi:+.3%}]")
print(f"probability the lift is positive (normal approximation): "
      f"{stats.norm.cdf(lift / ((hi-lo)/(2*1.96))):.2f}")

# What sample size would be needed to resolve a 0.4% lift?
p = 0.12
delta = 0.004
z_a, z_b = 1.96, 0.8416
n_needed = 2 * (z_a + z_b)**2 * p*(1-p) / delta**2
print(f"sessions per arm to detect a 0.4% absolute lift: {n_needed:,.0f}")
```

The interval includes zero, so the honest conclusion is "not yet resolved", and the
sample-size calculation says why: the experiment is an order of magnitude too small for
the effect being claimed. Shipping on the point estimate would be a decision made on
noise; the correct next step is more data, or a decision explicitly justified by the
offline evidence and the cost of being wrong.

## 10. Exercises

**Exercise 1.** With a Beta(1,1) prior and 30 successes in 100 trials, compute the
posterior mean, sd and 95% credible interval.

**Exercise 2.** Repeat Exercise 1 with a Beta(10,10) prior. How much did the prior move
the answer?

**Exercise 3.** Bootstrap the 90th percentile of `data` and report a 95% interval.

**Exercise 4.** Run a permutation test comparing two groups of 25 with a mean difference
of 2 and within-group sd of 5. Report the p-value.

**Exercise 5.** A classifier has 84% accuracy on 400 test cases. Give a 95% interval and
say whether it is distinguishable from 80%.

## 11. Solutions

```python
# Solution 1
post = stats.beta(1+30, 1+70)
print(f"mean {post.mean():.4f}, sd {post.std():.4f}")
print(f"95% credible [{post.ppf(0.025):.4f}, {post.ppf(0.975):.4f}]")
```

```python
# Solution 2
post2 = stats.beta(10+30, 10+70)
print(f"mean {post2.mean():.4f}, sd {post2.std():.4f}")
print(f"95% credible [{post2.ppf(0.025):.4f}, {post2.ppf(0.975):.4f}]")
# The prior mean is 0.5, so with 100 observations the posterior mean moves to about
# 0.44 instead of 0.30 -- a substantial shift, because 20 prior observations are
# comparable to 100 data points only in weak-prior terms.
```

```python
# Solution 3
p90 = bootstrap_statistic(data, lambda v: np.percentile(v, 90), B=5_000, seed=31)
lo, hi = np.percentile(p90, [2.5, 97.5])
print(f"90th percentile {np.percentile(data, 90):.3f}, 95% interval [{lo:.3f}, {hi:.3f}]")
```

```python
# Solution 4
rng = np.random.default_rng(601)
g1 = rng.normal(50, 5, 25)
g2 = rng.normal(52, 5, 25)
observed = g2.mean() - g1.mean()
rng2 = np.random.default_rng(602)
count = 0
B = 5_000
pooled = np.concatenate([g1, g2])
for _ in range(B):
    rng2.shuffle(pooled)
    if abs(pooled[25:].mean() - pooled[:25].mean()) >= abs(observed):
        count += 1
print(f"observed diff {observed:.3f}, permutation p {(1+count)/(B+1):.4f}")
```

```python
# Solution 5
p = 0.84
n = 400
se = np.sqrt(p*(1-p)/n)
print(f"95% interval [{p-1.96*se:.4f}, {p+1.96*se:.4f}]")
print(f"80% is {(0.80-p)/se:.2f} standard errors away")
# The interval excludes 0.80 only if 0.80 lies below the lower limit; with se about
# 0.018 the lower limit is about 0.804, so 0.80 is just outside -- a marginal
# distinction that a larger test set would settle.
```

## 12. Summary

- Bayesian updating multiplies the likelihood by the prior; for Beta–Bernoulli it is
  arithmetic, and the posterior narrows as data accumulate.
- Credible intervals are probability statements about the parameter; confidence intervals
  are statements about the procedure.
- The bootstrap estimates standard errors and intervals without formulas, and is the
  practical tool for medians, quantiles and derived metrics.
- Permutation tests use exchangeability rather than a distributional family.
- Peeking inflates the Type I error rate; sequential designs or fixed horizons are
  required.
- A machine-learning metric is an estimate with a standard error; report intervals,
  cross-validation spread and calibration, and monitor for drift.

**End of the practical sequence.** Return to the
[notebook index](index.md) or the [course map](../modules/index.md).
