---
title: "M15 — Hypothesis Testing"
description: Decision rules with two error rates, p-values that are not what most people think, power, effect sizes and multiplicity.
module: 15
part: 5
level: Core
hours: 18
prerequisites: [13, 14]
---

# M15 · Hypothesis Testing

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part V · Inference</span>
<span class="psds-chip">18 study hours</span>
<span class="psds-chip">Module 15 of 18</span>
</div>

## Introduction

A hypothesis test converts a question into a decision rule, and every decision rule
has two ways of being wrong. This module is about making those errors explicit,
quantifying them, and reporting results in a way that a reader can act on.

The mechanics are not difficult: choose a statistic, derive its distribution under the
null, define a rejection region, compute a p-value. The difficulty is interpretative,
and it is severe enough that whole fields have adopted the wrong definitions. A
p-value is **not** the probability that the null hypothesis is true. A non-significant
result is **not** evidence of no effect. A significant result is **not** necessarily
important.

This module treats interpretation as the primary content and the arithmetic as the
supporting detail. It also covers what most introductions omit: power analysis before
the study, effect sizes alongside p-values, and the multiplicity problem that turns
twenty honest tests into a false discovery.

## Why this matters

Hypothesis tests decide whether drugs are approved, features ship, and papers are
published. Misreporting them has consequences beyond a grade.

Three practical failures this module prevents:

- **Underpowered studies** that could not have detected a real effect, reported as
  "no effect found".
- **p-hacking** — testing until something is significant — which converts noise into
  publication.
- **Significance without size**, where a trivially small effect is reported as a win
  because \(n\) was large.

## Learning objectives

By the end of this module you can:

1. Formulate \(H_0\) and \(H_1\) for a research question, and choose one- or two-sided
   alternatives deliberately.
2. Define Type I error, Type II error, significance level and power, and compute them
   for a given design.
3. Conduct one-sample z and t tests, two-sample pooled and Welch tests, and paired
   tests, choosing correctly among them.
4. Compute and interpret a p-value correctly, and state four things it is not.
5. Derive a rejection region from the test statistic's distribution and show its
   equivalence to a p-value rule.
6. Determine sample size for a target power, and explain the power–effect–sample-size
   relationship.
7. Compute and report effect sizes (Cohen's d, relative risk, odds ratio) alongside
   significance.
8. Explain multiple-comparison inflation and apply Bonferroni and Benjamini–Hochberg
   corrections.
9. Explain p-hacking, optional stopping and publication bias, and identify them in
   published claims.
10. Distinguish statistical from practical significance, and explain equivalence
    testing.
11. Relate a test to the corresponding confidence interval and show the duality.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Sampling distributions, t, χ² | [M12](12-sampling-and-sampling-distributions.md) | Units 2–5 |
| CLT and normal approximation | [M13](13-law-of-large-numbers-and-clt.md) | Unit 3 |
| Intervals, standard errors, MLE | [M14](14-estimation-and-confidence-intervals.md) | Units 5–6 |
| Descriptive effect sizes | [M03](03-data-and-descriptive-statistics.md) | Units 4–5 |

## Topic breakdown

### Unit 1 — The logic of a test (2.5 h)

- A test as a decision rule over a sample space.
- \(H_0\) as a default with a specific distribution; \(H_1\) as the alternative.
- Why the null is usually "no effect" and what that costs.
- Test statistic: a summary whose distribution is known under \(H_0\).
- Rejection region and critical value.
- One-sided versus two-sided: the choice must precede the data.

### Unit 2 — Errors, power and the design triangle (3.5 h)

- Type I error \(\alpha\): rejecting a true null.
- Type II error \(\beta\): failing to reject a false null; power \(=1-\beta\).
- The four-cell reality/decision table, worked with numbers.
- Power depends on effect size, \(n\), \(\sigma\) and \(\alpha\) — the design triangle.
- Sample-size formula for a two-sample comparison; an explicit worked calculation.
- Why power analysis happens *before* the study, and what a post-hoc power
  calculation does not tell you.
- Underpowered studies as an ethical problem: they waste participants and produce
  unreliable literature.

### Unit 3 — The standard tests (4 h)

- One-sample z (known \(\sigma\)) and t (unknown \(\sigma\)).
- Two-sample: pooled (equal variances) versus Welch (default in modern software) —
  and why Welch is usually the right default.
- Paired t test: the design decides, not the data; the difference-of-differences
  argument.
- Test for a proportion: exact binomial and normal approximation, with the conditions.
- Variance tests: chi-square and F, and their sensitivity to normality.
- Reading software output: statistic, df, p-value, interval, and what each means.

### Unit 4 — p-values, correctly (3 h)

- Definition: the probability of data at least as extreme as observed, **given**
  \(H_0\).
- Uniformity of the p-value under \(H_0\); why 5% of true nulls fall below 0.05.
- What a p-value is not: not \(\Pr(H_0\mid \text{data})\), not an effect size, not a
  measure of importance, not a posterior probability.
- The ASA statement's principles, summarised.
- p-values and intervals: duality, demonstrated on one dataset.
- Reporting: statistic, df, p, effect size, interval, and a plain-language sentence.

### Unit 5 — Effect sizes and practical significance (2 h)

- Cohen's d, Hedges' g, relative risk, odds ratio, risk difference.
- Why a large \(n\) makes trivial differences significant.
- Equivalence testing and the "absence of evidence" problem.
- Choosing a smallest effect size of interest before the study.
- The CONSORT/STRANGE-style reporting mindset: pre-specify, report all outcomes.

### Unit 6 — Multiplicity (2.5 h)

- Family-wise error rate and its inflation: \(1-(1-\alpha)^m\).
- Bonferroni: valid, conservative, and its power cost.
- Holm's step-down procedure.
- Benjamini–Hochberg and false discovery rate — the right target when screening many
  hypotheses.
- The garden of forking paths: multiplicity without multiple tests.
- Simulation: twenty null tests, and what uncorrected significance looks like.

### Unit 7 — Testing in practice (0.5 h)

- Pre-registration and analysis plans.
- Sequential testing and peeking (developed in M18 for A/B tests).
- Reporting negative results honestly.
- When not to test at all: estimation with intervals is often the better answer.

## Important mathematical concepts

**The p-value.**

\[ p = \Pr\big(T \ge t_{\text{obs}} \,\big|\, H_0\big) \]

**Power and sample size** for a two-sample comparison of means:

\[ 1-\beta = \Pr\big(\text{reject} \mid H_1\big), \qquad
   n \ \approx\ \frac{2\,(z_{1-\alpha/2}+z_{1-\beta})^{2}\sigma^{2}}{\Delta^{2}} \]

**Family-wise error under \(m\) independent tests.**

\[ \Pr(\text{at least one false positive}) = 1-(1-\alpha)^{m} \]

*In words:* twenty independent tests at \(\alpha=0.05\) give about a 64% chance of at
least one spurious "significant" result.

**Benjamini–Hochberg** proceeds by ordering p-values and rejecting up to the largest
\(k\) with \(p_{(k)}\le \frac{k}{m}\alpha\).

## Expected knowledge after completion

You can, without notes:

- Write the four-cell error table with probabilities and compute power for a simple
  design.
- Compute and interpret a p-value, then state three things it does not mean.
- Choose between pooled and Welch, paired and unpaired, and justify it by design.
- Compute Cohen's d and explain why it can be small while p is tiny.
- Apply Bonferroni and BH to a list of p-values and explain the difference in target.
- Explain what peeking at an A/B test does to the Type I error rate.

## Connections to Data Science

- **A/B testing** is hypothesis testing with commercial stakes; every error in this
  module costs money (M18).
- **Feature selection by p-value** is multiplicity and selection bias at once.
- **Model comparison** uses the same logic through F tests and likelihood ratio tests.
- **Monitoring many metrics** creates a permanent multiplicity problem.
- **Fairness auditing** compares error rates across groups — testing again, with the
  same traps.

## Practical applications

| Setting | Question | Method |
|---|---|---|
| Two teaching methods | Is the difference real? | Two-sample t, Welch |
| Before/after training | Did scores improve within the same people? | Paired t |
| Conversion test | Is 3.1% vs 2.9% a real lift? | Two-proportion test with interval |
| Screening 500 genes | Which differ? | BH-controlled FDR |
| Quality control | Is the variance within spec? | Chi-square test |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 10 | Test selection and computation |
| ★★ Application | 8 | Full tests with assumptions, effect size, interpretation |
| ★★★ Challenge | 4 | Power analysis; p-hacking demonstration; multiplicity simulation; duality proof |
| Quiz | 10 items | Interpretation, including four misconception items |
| Practical notebook | 1 | Two teaching methods: full analysis, from design to report |
| Simulation lab | 1 | Errors and power: \(\alpha\), \(\beta\) and \(n\) |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: the logic of a test | 2.5 |
| 2 | Unit 2: errors, power, sample size | 3.5 |
| 3 | Unit 3: the standard tests | 4.0 |
| 4 | Unit 4: p-values correctly | 3.0 |
| 5 | Unit 5: effect sizes | 2.0 |
| 6 | Unit 6: multiplicity | 2.5 |
| 7 | Unit 7: practice and reporting | 0.5 |

**Before this module:** [M14](14-estimation-and-confidence-intervals.md). **After:**
[M16 — Correlation and Regression](16-correlation-and-regression.md) applies testing to
relationships between variables.
