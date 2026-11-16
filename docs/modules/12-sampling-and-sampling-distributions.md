---
title: "M12 — Sampling and Sampling Distributions"
description: Why a statistic is itself random, and the chi-square, t and F distributions that follow from normal samples.
module: 12
part: 4
level: Core
hours: 14
prerequisites: [10, 11]
---

# M12 · Sampling and Sampling Distributions

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part IV · Sampling and limits</span>
<span class="psds-chip">14 study hours</span>
<span class="psds-chip">Module 12 of 18</span>
</div>

## Introduction

This module contains the single idea that turns probability into statistics: **a
statistic computed from a sample is itself a random variable, and it has a
distribution.**

Before this point, randomness belonged to the data. The sample mean was a number you
computed. Now it becomes a quantity that would have been different had you collected a
different sample — so it has a mean, a variance, and a shape. That distribution, the
**sampling distribution**, is the foundation of every confidence interval, every test,
and every standard error in the rest of the course.

Students who "do not understand p-values" almost always have a gap here rather than in
M15. If the sampling distribution is genuinely understood, intervals and tests are
short derivations; if it is not, they are recipes to be memorised and misapplied.

## Why this matters

Three consequences, all practical.

**Uncertainty is quantifiable.** The spread of \(\bar{X}\) is \(\sigma/\sqrt{n}\), so
you can say how precise an estimate is before collecting data, and how much more data
would buy.

**The \(\sqrt{n}\) law is brutal.** Halving a margin of error costs four times the
sample. Every sample-size calculation in M14 and M15 is this fact.

**Standard errors are not standard deviations.** Confusing the two is a category
error: one describes the data, the other describes an estimate. It is also the most
common misreading of a regression table.

## Learning objectives

By the end of this module you can:

1. Define a random sample as independent, identically distributed variables, and
   distinguish it from a convenience sample.
2. Derive \(\E[\bar{X}]=\mu\) and \(\Var(\bar{X})=\sigma^2/n\), and define the
   standard error.
3. Explain what a sampling distribution is and demonstrate it by repeated sampling.
4. State when the sampling distribution of the mean is exactly normal, and when it is
   only approximately so.
5. Derive the distribution of \((n-1)s^2/\sigma^2\) as chi-square with \(n-1\) degrees
   of freedom, and explain the loss of one degree of freedom.
6. Derive the t statistic \(t=(\bar{X}-\mu)/(s/\sqrt{n})\) and explain why its
   distribution has heavier tails than the normal.
7. State the F distribution as a ratio of scaled chi-squares and identify where it
   arises.
8. Apply the finite-population correction and explain when it matters.
9. Design and interpret a simulation study of a sampling distribution, including the
   Monte Carlo error of the summary you report.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Normal distribution, standardisation | [M10](10-continuous-distributions.md) | Units 1–4 |
| Variance of a sum, independence | [M11](11-joint-distributions.md) | Units 3, 5 |
| Expectation and variance rules | [M08](08-random-variables-and-expectation.md) | Units 4–5 |
| Sampling vocabulary (population, statistic) | [M01](01-introduction-to-statistics.md) | Unit 2 |

## Topic breakdown

### Unit 1 — Random samples and statistics (2 h)

- i.i.d. sampling: independence plus identical distribution; what each part buys.
- Sampling with and without replacement; the finite-population viewpoint.
- Statistic: any function of the sample that does not depend on unknown parameters.
- Common statistics: \(\bar{X}\), \(s^2\), median, proportion, min, max.
- Why the *distribution* of a statistic, not its value, is the object of inference.
- Sampling bias: how a non-random sample breaks every result in this module.

### Unit 2 — The sampling distribution of the mean (3 h)

- Derivation: \(\E[\bar{X}]=\mu\), \(\Var(\bar{X})=\sigma^2/n\), so
  \(\se(\bar{X})=\sigma/\sqrt{n}\).
- Exact normality when the population is normal; the CLT covers the rest (M13).
- Demonstrating the distribution by simulation: same population, many samples.
- The \(\sqrt{n}\) law and its cost implications.
- Distinguishing the distribution of the data from the distribution of the mean —
  the confusion this unit exists to eliminate.
- Standard error of a proportion: \(\sqrt{p(1-p)/n}\).

### Unit 3 — Degrees of freedom and the chi-square distribution (3 h)

- Why \(s^2\) has \(n-1\) degrees of freedom: the deviations sum to zero, so one is
  determined.
- Distribution of \((n-1)s^2/\sigma^2\) as \(\chi^2_{n-1}\); derivation sketch via
  orthogonal transformation of normal vectors.
- Mean and variance of a chi-square; additivity.
- Why the chi-square is skewed and becomes symmetric as \(n\) grows.
- Confidence interval for \(\sigma^2\) built on this (forward link to M14).

### Unit 4 — The t distribution (2.5 h)

- The problem: \(\sigma\) is unknown, so replacing it with \(s\) adds variability.
- The ratio \(T=(\bar{X}-\mu)/(s/\sqrt{n})\) and its t distribution with \(n-1\) df.
- Why t has heavier tails, and why the difference matters at small \(n\).
- The limit: \(t_\nu \to N(0,1)\) as \(\nu\to\infty\); the practical \(n>30\) rule and
  its caveats.
- Gosset's history, briefly, as a lesson in why small samples needed a new
  distribution.

### Unit 5 — The F distribution (1.5 h)

- Ratio of two independent scaled chi-squares; degrees of freedom in numerator and
  denominator.
- Ratio of two sample variances; the variance-ratio test.
- Where F appears: ANOVA (M17) and the overall regression test (M16).
- Reading an F distribution: right-skewed, support \((0,\infty)\), mean \(>1\).

### Unit 6 — Simulation of sampling distributions (2 h)

- The "sampling machine": \(B\) samples of size \(n\) from a known population,
  recording a statistic each time.
- Comparing empirical histograms to theoretical densities for \(\bar{X}\), \(s^2\),
  \(T\) and the variance ratio.
- Quantifying Monte Carlo error in the comparison.
- Demonstrating the effect of a non-normal population on each statistic.

## Important mathematical concepts

**Mean and variance of the sample mean.**

\[ \E[\bar{X}]=\mu, \qquad \Var(\bar{X})=\frac{\sigma^{2}}{n}, \qquad
   \se(\bar{X})=\frac{\sigma}{\sqrt{n}} \]

**Chi-square for the sample variance.**

\[ \frac{(n-1)s^{2}}{\sigma^{2}}\sim\chi^{2}_{n-1} \]

**The t statistic.**

\[ T=\frac{\bar{X}-\mu}{s/\sqrt{n}}\sim t_{n-1} \]

**The F statistic.**

\[ F=\frac{s_1^{2}/\sigma_1^{2}}{s_2^{2}/\sigma_2^{2}}\sim F_{n_1-1,\,n_2-1} \]

**Finite-population correction.**

\[ \Var(\bar{X})=\frac{\sigma^{2}}{n}\cdot\frac{N-n}{N-1} \]

*In words:* when the sample is a large share of the population, the mean is more
precise than \(\sigma/\sqrt{n}\) suggests, because you have nearly measured everything.

## Expected knowledge after completion

You can, without notes:

- Derive \(\Var(\bar{X})\) in three lines and say which assumption each line needs.
- Explain the difference between \(s\) and \(\se(\bar{X})\) to a non-specialist.
- Simulate 10,000 samples and overlay the theoretical distribution of \(\bar{X}\), then
  explain any visible discrepancy.
- Explain why \(s^2\) loses a degree of freedom and why that changes the distribution.
- Say why the t distribution exists and when the normal is an acceptable substitute.

## Connections to Data Science

- **Standard errors in model output** are sampling-distribution statements; reading
  them as data spread is a common error.
- **Cross-validation variability** is a sampling distribution of a performance
  statistic.
- **Bootstrap** (M18) estimates exactly these distributions without a formula — this
  module is what it is approximating.
- **Sample-size planning** for experiments is the \(\sqrt{n}\) law applied (M15).
- **A/B test precision** is the standard error of a difference of proportions.

## Practical applications

| Setting | Question | Concept |
|---|---|---|
| Survey | How precise is this mean, with \(n=400\)? | Standard error |
| Quality control | How variable is the batch standard deviation? | Chi-square sampling distribution |
| Pilot study | How much would \(n=1{,}000\) improve precision? | \(\sqrt{n}\) law |
| Small clinical sample | Can we use \(z\) or must we use \(t\)? | t versus normal |
| Model comparison | Is this variance ratio surprising? | F distribution |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 8 | Standard errors and sample-size arithmetic |
| ★★ Application | 7 | Derive and simulate sampling distributions |
| ★★★ Challenge | 4 | Derivation of \(\Var(\bar{X})\) under dependence; degrees of freedom; t versus z tails; finite-population correction |
| Quiz | 10 items | Sampling distribution versus data distribution |
| Practical notebook | 1 | The sampling machine for four statistics |
| Simulation lab | 1 | Sampling distributions of \(\bar{X}\) and \(s^2\) |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: samples and statistics | 2.0 |
| 2 | Unit 2: the sampling distribution of the mean | 3.0 |
| 3 | Unit 3: degrees of freedom and chi-square | 3.0 |
| 4 | Unit 4: the t distribution | 2.5 |
| 5 | Unit 5: the F distribution | 1.5 |
| 6 | Unit 6: simulation | 2.0 |

**Before this module:** [M11](11-joint-distributions.md). **After:**
[M13 — Law of Large Numbers and the Central Limit Theorem](13-law-of-large-numbers-and-clt.md)
explains why these distributions look the way they do.
