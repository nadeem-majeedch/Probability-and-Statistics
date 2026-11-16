---
title: Part V — Statistical Inference
description: Estimation, confidence intervals and hypothesis testing. Modules M14–M15.
---

# Part V — Statistical Inference

**Modules M14–M15 · 34 study hours · Core · Prerequisites: Parts I–IV**

---

## Why this part exists

Inference is the act of saying something about a population you have not observed. This
part covers the two classical forms: estimating a quantity with a stated uncertainty,
and deciding between claims with stated error rates.

The emphasis is on interpretation rather than arithmetic, because the arithmetic is the
easy part and the interpretation is where practice goes wrong. A 95% confidence interval
does not mean "95% chance the parameter is in this interval". A p-value is not the
probability that the null hypothesis is true. A non-significant result is not evidence
of no effect. Each of those errors has caused real harm, and each is corrected here by
simulation rather than assertion: you will compute coverage rates and error rates and
watch the numbers fail to match the naive reading.

M14 and M15 are deliberately adjacent because they are the same theory seen twice. Every
interval has a test inside it, and every test has an interval inside it.

## Modules

| # | Module | Level | Hours | Focus |
|---|---|---|---|---|
| M14 | [Estimation and Confidence Intervals](../modules/14-estimation-and-confidence-intervals.md) | Core | 16 | Bias, variance, MSE, method of moments, maximum likelihood, sufficiency, pivots, coverage |
| M15 | [Hypothesis Testing](../modules/15-hypothesis-testing.md) | Core | 18 | Errors and power, standard tests, p-values, effect sizes, multiplicity, practice |

## What you will be able to do

- Derive a maximum-likelihood estimator and say why it is or is not unbiased.
- Explain the bias–variance decomposition of MSE, and connect it to regularisation.
- Construct a t interval from summary statistics and state its coverage interpretation
  in one correct sentence.
- Compute the sample size needed for a stated margin of error, and explain the quadratic
  cost.
- Run a power analysis before a study rather than a post-hoc calculation after it.
- Report a result as statistic, interval, effect size and plain-language sentence.
- Apply Bonferroni and Benjamini–Hochberg correction and explain what each controls.

## Simulation experiments in this part

Estimator bias and consistency across sample sizes; interval coverage under correct and
violated assumptions; the four-cell error table simulated; twenty null tests showing
multiplicity inflation.

**Interactive labs:** [confidence interval coverage](../labs/confidence-intervals.md),
and the errors-and-power lab.

## Common misconceptions this part removes

| Misconception | Corrected in |
|---|---|
| "A 95% interval has a 95% chance of containing μ" | M14 |
| "A wider interval is more accurate" | M14 |
| "*p* = 0.03 means a 3% chance the null is true" | M15 |
| "Non-significant means no effect" | M15 |
| "Significant means important" | M15 |
| "Running more tests is free" | M15 |

## Start

Begin with [M14 — Estimation and Confidence Intervals](../modules/14-estimation-and-confidence-intervals.md).
Allow the full 34 hours; this part is the one most often rushed, and most often needed
later.
