---
title: "M14 — Statistical Estimation and Confidence Intervals"
description: Method of moments, maximum likelihood, estimator quality, and intervals that state their own reliability.
module: 14
part: 5
level: Core
hours: 16
prerequisites: [12, 13]
---

# M14 · Statistical Estimation and Confidence Intervals

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part V · Inference</span>
<span class="psds-chip">16 study hours</span>
<span class="psds-chip">Module 14 of 18</span>
</div>

## Introduction

Estimation is the first genuinely inferential act in the course: producing a number
about a population from a sample. There are two questions, and they are different.
*How do we construct an estimate?* — method of moments, maximum likelihood, or a
sensible guess. *How do we know whether it is any good?* — bias, variance,
consistency, efficiency, and mean squared error.

Then comes the part students find hardest to interpret: an estimate without an
uncertainty statement is incomplete. A confidence interval attaches a range and a
coverage guarantee. And the guarantee is about the **procedure**, not about the
interval you just computed. A 95% interval either contains the parameter or it does
not; what is 95% is the long-run fraction of intervals that do.

That distinction is not pedantry. It determines what you may say to a decision-maker,
and getting it wrong produces overconfident claims in public health, finance and
product analytics.

## Why this matters

Every model you fit produces estimates, and every estimate needs an error bar.

Estimator theory tells you *why* the standard choices are standard: why the sample
mean beats the median for normal data and loses to it for heavy tails; why maximum
likelihood is the default; why adding an assumption buys precision.

Interval construction tells you how to communicate. And the failure modes are
concrete: a Wald interval for a proportion near 0.001 has coverage far below nominal,
which is exactly the regime of click-through and conversion metrics.

## Learning objectives

By the end of this module you can:

1. Distinguish parameter, estimator and estimate, and explain why the estimator is a
   random variable.
2. Derive method-of-moments estimators for standard models and state when the method
   fails.
3. Derive maximum-likelihood estimators: likelihood, log-likelihood, score,
   stationary point, second-order check.
4. Compute MLEs for the Bernoulli, binomial, Poisson, exponential, normal and uniform
   models, including the uniform case where differentiation fails.
5. Evaluate estimators by bias, variance, MSE, consistency and efficiency, and derive
   the bias–variance decomposition of MSE.
6. State the Cramér–Rao bound and Fisher information, and check whether an estimator
   attains it.
7. Define sufficiency, apply the factorisation criterion, and explain the
   Rao–Blackwell idea.
8. Construct confidence intervals by the pivotal method, and derive the z, t,
   proportion, variance and two-sample intervals.
9. Determine the sample size required for a target margin of error.
10. Explain and demonstrate the coverage interpretation of confidence intervals.
11. Construct bootstrap percentile intervals and say when they are preferable.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Sampling distributions: \(\bar{X}\), \(s^2\), t, χ² | [M12](12-sampling-and-sampling-distributions.md) | Units 2–5 |
| CLT and its conditions | [M13](13-law-of-large-numbers-and-clt.md) | Unit 3 |
| Derivatives, log-likelihood, series | [M02](02-mathematical-foundations.md) | Units 4, 6 |
| Normal, gamma, beta families | [M10](10-continuous-distributions.md) | — |

## Topic breakdown

### Unit 1 — Estimators and their properties (2.5 h)

- Estimator as a rule; estimate as its value; sampling distribution as its behaviour.
- Bias: \(\text{bias}(\hat\theta)=\E[\hat\theta]-\theta\); unbiasedness is a property of
  the procedure, for a given \(n\).
- Variance and MSE; the decomposition
  \(\text{MSE}=\text{bias}^2+\text{variance}\).
- Consistency: \(\hat\theta_n \xrightarrow{p}\theta\); sufficient conditions.
- Efficiency: relative variance among unbiased estimators.
- Why unbiasedness is not the only virtue: shrinkage (M18) trades bias for variance
  deliberately.

### Unit 2 — Method of moments (2 h)

- Set sample moments equal to population moments; solve.
- Worked cases: normal, exponential, gamma, binomial.
- When the method produces impossible values (negative variance estimates).
- Why moment estimators are useful as starting points for optimisation.

### Unit 3 — Maximum likelihood (4 h)

- Likelihood as a function of the parameter for fixed data; why we maximise it.
- Log-likelihood: monotone transform, turns products into sums.
- Score function and the stationarity condition; second-derivative check.
- Full derivations: Bernoulli, binomial, Poisson, exponential, normal (mean and
  variance), uniform.
- The uniform case: the derivative never vanishes; the maximum is at the boundary —
  a lesson in not trusting calculus blindly.
- Invariance: if \(\hat\theta\) is the MLE of \(\theta\), then \(g(\hat\theta)\) is the
  MLE of \(g(\theta)\).
- Numerical maximisation with `scipy.optimize`, and why closed forms are worth having.
- Bias of MLEs: \(\hat\sigma^2\) is biased; the MLE is not automatically unbiased.

### Unit 4 — Information and sufficiency (2 h)

- Fisher information \(I(\theta)\); observed versus expected.
- Cramér–Rao: \(\Var(\hat\theta)\ge 1/(nI(\theta))\) for unbiased estimators.
- Checking attainment: the mean of a normal sample attains it.
- Sufficiency: a statistic that captures all information about the parameter.
- Factorisation criterion, with the Poisson and normal examples.
- Rao–Blackwell: conditioning on a sufficient statistic never increases variance.

### Unit 5 — Confidence intervals by pivots (3.5 h)

- Pivot: a function of data and parameter whose distribution does not depend on the
  parameter.
- Deriving the z interval for a mean with known \(\sigma\).
- The t interval when \(\sigma\) is unknown; why the t quantile is larger.
- Interval for a proportion: Wald and Wilson, and why Wald fails near 0 or 1.
- Interval for a variance via the chi-square pivot.
- Difference of two means: pooled and Welch.
- Sample size for a target margin of error: \(n=(z\sigma/E)^2\), and its quadratic
  cost.

### Unit 6 — Interpreting coverage (2 h)

- The operational meaning: repeated sampling, 95% of intervals capture \(\mu\).
- What you may and may not say about the interval you computed.
- Coverage simulation; the small-\(n\) shortfall; coverage near the boundary for
  proportions.
- Duality with hypothesis tests (formalised in M15).
- Width versus confidence versus sample size: the three-way trade.

### Unit 7 — The bootstrap preview (1 h)

- Resampling with replacement from the observed sample.
- Bootstrap standard error; percentile interval.
- When it works and when it fails: extreme quantiles, tiny samples, dependent data.
- Full treatment in M18.

## Important mathematical concepts

**Bias–variance decomposition.**

\[ \text{MSE}(\hat\theta)=\E\big[(\hat\theta-\theta)^{2}\big]
   =\big(\text{bias}(\hat\theta)\big)^{2}+\Var(\hat\theta) \]

**Log-likelihood and score.**

\[ \ell(\theta)=\sum_{i=1}^{n}\log f(x_i;\theta), \qquad
   \ell'(\hat\theta)=0 \]

**Cramér–Rao bound.**

\[ \Var(\hat\theta)\ \ge\ \frac{1}{n\,I(\theta)}, \qquad
   I(\theta)=-\,\E\!\left[\frac{\partial^{2}}{\partial\theta^{2}}\log f(X;\theta)\right] \]

**The t interval for a mean.**

\[ \bar{x}\ \pm\ t_{n-1,\,1-\alpha/2}\,\frac{s}{\sqrt{n}} \]

**Wilson interval for a proportion** (schematic):

\[ \frac{\hat p+\frac{z^{2}}{2n}}{1+\frac{z^{2}}{n}}
   \ \pm\ \frac{z}{1+\frac{z^{2}}{n}}
   \sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^{2}}{4n^{2}}} \]

## Expected knowledge after completion

You can, without notes:

- Derive the MLE for an exponential sample and check the second-order condition.
- Show that \(s^2\) is unbiased and that the MLE \(\hat\sigma^2\) is not.
- Construct a 95% t interval from summary statistics and interpret it correctly in one
  sentence.
- Explain why a 99% interval is wider and why that is not "more accurate".
- Compute the sample size needed for a \(\pm 2\)% margin on a proportion.
- Explain why the Wald interval collapses at \(\hat p = 0\).

## Connections to Data Science

- **Model coefficients** are MLEs; their standard errors are Cramér–Rao-flavoured.
- **Confidence intervals in dashboards** are what turn a metric into a decision aid.
- **Bootstrap intervals** are the default in modern applied work (M18).
- **Regularisation** is deliberate bias for variance reduction — Unit 1's MSE
  decomposition applied.
- **Conversion metrics** near zero are exactly where naive intervals fail.

## Practical applications

| Setting | Question | Method |
|---|---|---|
| Average order value | Estimate and interval from a sample | t interval |
| Conversion rate | Interval for a small proportion | Wilson |
| Process variability | Interval for \(\sigma^2\) | Chi-square pivot |
| Survey planning | How many respondents for \(\pm3\)%? | Sample size formula |
| Small pilot | Estimate with no formula available | Bootstrap |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 8 | MLE computations; interval arithmetic |
| ★★ Application | 8 | Derive an estimator; construct and interpret intervals |
| ★★★ Challenge | 4 | Cramér–Rao check; sufficiency; coverage simulation; Wald versus Wilson |
| Quiz | 10 items | Estimation and interpretation |
| Practical notebook | 1 | MLE by hand and by optimiser; interval coverage simulation |
| Simulation lab | 1 | [Coverage lab](../labs/confidence-intervals.md) |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: estimator properties | 2.5 |
| 2 | Units 2–3: moments and maximum likelihood | 4.0 |
| 3 | Unit 4: information and sufficiency | 2.0 |
| 4 | Unit 5: interval construction | 3.5 |
| 5 | Unit 6: coverage | 2.0 |
| 6 | Unit 7: bootstrap preview | 1.0 |

**Before this module:** [M12](12-sampling-and-sampling-distributions.md),
[M13](13-law-of-large-numbers-and-clt.md). **After:** [M15 — Hypothesis
Testing](15-hypothesis-testing.md).
