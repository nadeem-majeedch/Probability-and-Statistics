---
title: "M03 — Data and Descriptive Statistics"
description: Measurement scales, data quality, and the measures of centre, spread and shape that summarise a dataset honestly.
module: 3
part: 1
level: Beginner
hours: 14
prerequisites: [2]
---

# M03 · Data and Descriptive Statistics

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--beginner">Beginner</span>
<span class="psds-chip">Part I · Foundations</span>
<span class="psds-chip">14 study hours</span>
<span class="psds-chip">Module 3 of 18</span>
</div>

## Introduction

Every summary is a compression, and every compression loses something. The question
this module answers is which loss is acceptable for which question.

A mean of house prices says nothing useful when one mansion is in the sample; a
median income hides the fact that the distribution has two peaks; a standard
deviation of a bimodal variable is a number with no interpretation at all. None of
these is a calculation error. They are summarisation errors, and they are far more
common than arithmetic ones.

The module therefore does three things in order. It establishes what kind of
variable you have (because that determines which summaries are even legal). It
builds the measures of centre, spread, position and shape, deriving each. And it
shows, with data, how a summary can be technically correct and substantively
misleading.

## Why this matters

Descriptive statistics is the only part of statistics every data scientist uses every
day, and the part most often done carelessly.

Concretely: the sample variance divides by \(n-1\), not \(n\). That single fact —
which most students memorise — is a statement about estimation (unbiasedness for
\(\sigma^2\)), not about description. Understanding *why* is the difference between
a student who can debug a pipeline and one who cannot.

The second reason is interpretive. Skew determines whether the mean or median is the
right summary; spread determines whether a difference is meaningful; the shape
determines whether a later model's assumptions are plausible. Every modelling
decision downstream depends on a judgement made here.

## Learning objectives

By the end of this module you can:

1. Load a tabular dataset and classify every column by type, scale and role
   (identifier, feature, target, date).
2. Diagnose common data-quality problems — missingness, duplicates, impossible
   values, inconsistent units, mixed types — and choose a defensible treatment.
3. Reshape data into tidy form and explain why tidy structure matters for analysis.
4. Compute and interpret measures of centre: mean, median, mode, trimmed mean,
   weighted mean, geometric mean — and choose among them for a stated variable.
5. Compute and interpret measures of spread: range, IQR, variance, standard
   deviation, coefficient of variation, mean absolute deviation.
6. Derive \(s^2 = \sum (x_i-\bar{x})^2/(n-1)\) and explain the \(n-1\) correction
   through unbiasedness.
7. Compute quantiles, percentiles and z-scores by hand and with software, and
   explain the different quantile conventions.
8. Describe the shape of a distribution using skewness and kurtosis, and relate
   mean–median ordering to skew.
9. Detect outliers by the 1.5×IQR rule and by z-scores, and argue for or against
   removal in a specific case.
10. Explain robustness: which summaries survive an extreme value and which do not.
11. Recognise Simpson's paradox and the ecological fallacy in tabular data.
12. Produce a one-page descriptive report whose numbers can be defended.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Summation notation, \(\sum\), linearity | [M02](02-mathematical-foundations.md) | Unit 3 |
| Functions and notation \(f(x)\) | M02 | Unit 2 |
| Population/sample vocabulary, scales | [M01](01-introduction-to-statistics.md) | Unit 3 |
| Basic `pandas` (for the notebook) | [Setup](../setup.md) | Practical |

## Topic breakdown

### Unit 1 — Data structures and types (1.5 h)

- Rectangular data: observations (rows), variables (columns), the tidy convention.
- Types: numeric (integer, float), categorical (nominal, ordinal), datetime, text,
  boolean, identifier.
- Continuous versus discrete; why the distinction is about possible values, not
  storage.
- Long versus wide format; `melt`/`pivot` and the analysis consequences.
- Unit of analysis: the most common serious error is a table whose rows are not the
  thing you are describing.

### Unit 2 — Data quality and preparation (2 h)

- Missing data: MCAR, MAR, MNAR — what each does to a summary.
- Duplicates, near-duplicates, and record linkage.
- Impossible and implausible values; validation rules.
- Inconsistent categories ("Male", "male", "M") and the cost of silent coercion.
- Dates and time zones; durations versus timestamps.
- Outliers as errors versus outliers as signal — the decision framework.
- Documentation: a data dictionary as part of the analysis, not an afterthought.

### Unit 3 — Frequency distributions and grouped data (1.5 h)

- Frequency, relative frequency, cumulative frequency.
- Class intervals, width choice, and the information lost by binning.
- Computing a grouped mean and grouped variance, and the approximation error.
- Why you should almost never bin a continuous variable for analysis (only for
  display).

### Unit 4 — Measures of centre (2.5 h)

- Arithmetic mean: definition, properties, linearity, sensitivity.
- Median: definition, even-\(n\) convention, insensitivity to extremes.
- Mode, and the multi-modal case.
- Trimmed mean; winsorised mean.
- Weighted mean and why survey estimates are weighted.
- Geometric mean for growth rates and ratios; harmonic mean for rates.
- Choosing a centre: the decision table by shape and scale.

### Unit 5 — Measures of spread (3 h)

- Range and its dependence on \(n\).
- Interquartile range; the five-number summary.
- Variance: definition, computational form, units problem.
- Why \(n-1\): deriving \(\E[s^2] = \sigma^2\) and contrasting with the biased
  divisor \(n\).
- Standard deviation and its interpretation in original units.
- Coefficient of variation for comparing spread across scales.
- Mean absolute deviation; why variance is preferred mathematically.
- Spread of a difference: preview of variance algebra (M11).

### Unit 6 — Position, standardisation and shape (2 h)

- Quantiles and percentiles; competing definitions and why software disagrees.
- z-scores: standardisation, interpretation, and the assumption behind them.
- Skewness: definition via the third standardised moment; interpretation; the
  mean–median rule of thumb and its limits.
- Kurtosis: tails, not "peakedness", despite the textbook phrase.
- Detecting non-normality from summaries alone — and why summaries are not enough
  (M04 supplies the plots).

### Unit 7 — Outliers and robustness (1.5 h)

- The 1.5×IQR rule; the z-score rule; their different assumptions.
- Influence versus extremeness: an outlier may not be influential, and vice versa.
- Robust statistics: median, IQR, MAD, trimmed estimators.
- The breakpoint idea: how much contamination a summary tolerates.
- A defensible protocol for outliers: flag, investigate, document, decide — never
  silently delete.

### Unit 8 — Aggregation traps (1 h)

- Simpson's paradox: a real two-way table where the aggregate reverses the
  subgroup conclusion.
- The ecological fallacy: group-level statistics applied to individuals.
- Averaging averages: when it is valid and when it is not.
- Rates versus counts; denominators.

## Important mathematical concepts

**Sample mean and variance.**

\[ \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i, \qquad
   s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2 \]

**Computational form** (used by software, and to be used with care):

\[ s^2 = \frac{\sum x_i^2 - n\bar{x}^2}{n-1} \]

**The \(n-1\) correction.** For i.i.d. observations with variance \(\sigma^2\),

\[ \E\!\left[\frac{1}{n-1}\sum (x_i-\bar{x})^2\right] = \sigma^2
   \qquad\text{but}\qquad
   \E\!\left[\frac{1}{n}\sum (x_i-\bar{x})^2\right]
   = \frac{n-1}{n}\sigma^2 \neq \sigma^2 \]

*In words:* dividing by \(n-1\) removes the average underestimate caused by measuring
deviations from the sample mean rather than from the true mean.

**Coefficient of variation and z-score.**

\[ CV = \frac{s}{\bar{x}}, \qquad z_i = \frac{x_i - \bar{x}}{s} \]

**Skewness** (third standardised moment):

\[ g_1 = \frac{1}{n}\sum_{i=1}^{n}\left(\frac{x_i-\bar{x}}{s}\right)^{3} \]

## Expected knowledge after completion

You can, without notes:

- Compute mean, median, variance, IQR and z-scores for a small dataset by hand and
  check them in `pandas` to the last digit.
- Explain to a non-specialist why the sample variance divides by \(n-1\).
- Choose centre and spread for a skewed variable, and defend the choice.
- Detect an outlier by two rules and explain why they may disagree.
- Construct a dataset where the mean and median give opposite impressions, and
  explain which is right for which question.
- Identify Simpson's paradox in a table and say which conclusion the design supports.

## Connections to Data Science

- **Feature engineering** begins with Unit 1: a variable typed as numeric but
  semantically categorical will corrupt a model.
- **Imputation** is Unit 2: choosing mean imputation changes variance and biases
  standard errors — a fact that becomes precise in M14.
- **Standardisation** (z-scores) is required by regularised models and PCA, and its
  assumptions are stated here.
- **Anomaly detection** is Unit 7: the rule you use implies a theory of what "normal"
  is.
- **Reporting to stakeholders** is the one-page descriptive report — the most
  common deliverable in analytics.

## Practical applications

| Setting | Question | Method |
|---|---|---|
| Salaries in a company | What is a typical salary? | Median and IQR; why the mean is misleading under skew |
| Delivery times | Is the service consistent? | SD, IQR, and the shape of the tail |
| Exam scores across sections | Which section did better? | Compare centres **and** spreads, not means alone |
| Sensor readings | Is this value an error? | 1.5×IQR and z-score rules; investigation protocol |
| Two stores, three product lines | Which line sells best? | Simpson's paradox check before any conclusion |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 8 | Compute summaries by hand |
| ★★ Application | 6 | Choose and justify summaries; clean a messy dataset |
| ★★★ Challenge | 3 | Prove unbiasedness of \(s^2\); construct a Simpson's paradox; compare robust and classical summaries |
| Quiz | 10 items | Interpretation and choice, with explanations |
| Practical notebook | 1 | Full descriptive analysis with a data dictionary and a defended summary table |
| Deliverable | 1 page | Descriptive report of a public dataset |

**Assessment weighting for this module:** quiz 30%, ★★/★★★ exercises 40%,
practical notebook 30%.

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Units 1–2: types, quality, tidying | 3.0 |
| 2 | Units 3–4: frequencies and centre | 3.0 |
| 3 | Unit 5: spread and the \(n-1\) derivation | 3.5 |
| 4 | Unit 6: quantiles, z-scores, shape | 2.5 |
| 5 | Units 7–8: outliers, robustness, aggregation traps | 1.5 |
| 6 | Practical and descriptive report | 0.5 |

**Before this module:** [M02](02-mathematical-foundations.md). **After:**
[M04 — Data Visualization](04-data-visualization.md), which turns these summaries
into pictures and reveals what they hide.
