---
title: "M04 — Data Visualization and Exploratory Analysis"
description: Choosing the plot that answers the question, reading it honestly, and the EDA workflow that precedes every model.
module: 4
part: 1
level: Beginner
hours: 12
prerequisites: [3]
---

# M04 · Data Visualization and Exploratory Analysis

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--beginner">Beginner</span>
<span class="psds-chip">Part I · Foundations</span>
<span class="psds-chip">12 study hours</span>
<span class="psds-chip">Module 4 of 18</span>
</div>

## Introduction

A number answers the question you asked. A picture answers questions you did not
know to ask — and that is why visualisation is not decoration but a method.

The classic demonstration is Anscombe's quartet: four datasets with identical means,
variances and correlations, and four completely different structures. Three are
linear; one is a perfect curve with a single outlier making it look linear. Every
summary in M03 is identical, and every conclusion drawn from those summaries is
wrong for one of them.

This module therefore teaches two skills together: **production** (building the plot
that answers the question) and **reading** (extracting the finding, including its
absence). It ends with the exploratory workflow that should precede every model —
univariate, then bivariate, then multivariate, then anomalies, then hypotheses.

## Why this matters

In practice, visualisation does three jobs that nothing else does.

It **catches errors** before they propagate: an impossible value, a broken join, a
time zone shift, a duplicated batch.

It **chooses the model**: skew suggests a transformation, curvature suggests an
interaction, heteroscedasticity suggests robust standard errors or a different link.

It **communicates** the finding to people who will not read a coefficient table. A
misleading chart is not a cosmetic failure — in public health, finance and policy it
is the failure.

## Learning objectives

By the end of this module you can:

1. Explain the grammar of graphics: data → aesthetic mapping → geom → scale → facet,
   and use it to describe any chart precisely.
2. Choose a plot from the variable types and the question, using a decision table
   rather than habit.
3. Build and correctly interpret histograms, density plots, box plots, violin plots,
   ECDFs and Q–Q plots — including what each one hides.
4. Build scatter plots, line charts, heatmaps, small multiples and paired
   comparisons for bivariate and multivariate structure.
5. Explain the role of bin width, smoothing bandwidth and axis limits in shaping the
   impression a chart gives.
6. Apply the principles of graphical integrity: no truncated axes without cause, no
   misleading aspect ratios, no 3-D encodings of 2-D data, no colour that fails
   accessibility.
7. Produce a colour-blind-safe, accessible palette choice and verify it.
8. Write a caption that states the finding rather than the file name.
9. Run a structured EDA: univariate → bivariate → multivariate → anomalies →
   candidate hypotheses, and record findings as a narrative.
10. Identify at least six misleading-chart patterns in published material and explain
    the distortion mechanism in each.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Mean, median, SD, IQR, quantiles | [M03](03-data-and-descriptive-statistics.md) | Units 4–6 |
| Skewness and shape vocabulary | M03 | Unit 6 |
| Tidy data structure | M03 | Unit 1 |
| `matplotlib` basics | [Setup](../setup.md) | Practical |

## Topic breakdown

### Unit 1 — Why pictures work, and when they lie (1.5 h)

- Pre-attentive processing: what the eye detects without effort (position, length)
  versus what it does not (area, angle, colour intensity).
- Cleveland's hierarchy of encodings: position > length > angle > area > colour.
- Anscombe's quartet and the Datasaurus dozen.
- The misleading-chart catalogue: truncated axis, dual axis, 3-D pie, area-scaled
  icons, cherry-picked windows, log axis presented as linear.

### Unit 2 — The grammar of graphics (1.5 h)

- Data, aesthetics, geoms, scales, coordinates, facets, themes.
- Why the grammar lets you translate between tools (`matplotlib`, `seaborn`,
  `plotly`, `ggplot2`).
- `matplotlib`'s object API: figure, axes, artists — and why `.plot()` without an
  `ax` is a habit worth breaking.
- Saving for print: DPI, vector versus raster, fonts embedded.

### Unit 3 — Univariate plots (2.5 h)

- Histogram: bin width as a modelling choice; the same data with three widths.
- Kernel density: bandwidth, and why a density can exceed 1.
- Box plot: five-number summary, whisker rule, and the four things it hides
  (bimodality, sample size, tail shape, exact values).
- Violin and strip/jitter plots as the honest alternatives.
- ECDF: the plot that hides nothing.
- Q–Q plot: reading deviation from a reference distribution, and its limits at
  small \(n\).
- Bar charts for categories: order, baseline at zero, and the pie-chart problem.

### Unit 4 — Bivariate structure (2 h)

- Scatter: overplotting, transparency, hexbin, jitter.
- Line charts: time on the x-axis, and the missing-data gap that changes the story.
- Correlation is not visible in one number (preview of M16): the four shapes with
  \(r \approx 0\).
- Small multiples and faceting versus colour-by-group.
- Heatmaps and mosaic plots for categorical pairs.

### Unit 5 — Multivariate and multivariate-ish (1.5 h)

- Scatter-plot matrices and pair plots: cost and readability.
- Encoding a third variable: size, colour, panel; the ceiling of each.
- Parallel coordinates — power and illegibility.
- Dimensionality and overplotting: why ten thousand points is a rendering problem
  as well as a perceptual one.

### Unit 6 — Design, colour and accessibility (2 h)

- Chart titles as findings; axis labels with units; caption as argument.
- Gridlines, tick density, ordering, and whitespace.
- Colour: sequential, diverging and qualitative; viridis and Okabe–Ito; never a
  rainbow for ordered data.
- Contrast and colour-blind safety: deuteranopia checks.
- Alt text that describes the finding; data tables as a fallback.
- Print and dark-mode rendering.

### Unit 7 — The exploratory workflow (2 h)

- Step 1: structure — shape, types, missingness.
- Step 2: univariate distributions, one per variable.
- Step 3: bivariate relationships against the target.
- Step 4: multivariate checks, interactions, confounding.
- Step 5: anomalies and their causes.
- Step 6: candidate hypotheses, written down before testing.
- Recording an EDA: a narrative log with the three most important figures.

## Important mathematical concepts

The plotting units are largely visual, but three quantities are computed and must be
understood, not merely plotted.

**The ECDF** — the empirical distribution function, which is the histogram's honest
cousin:

\[ \hat{F}_n(x) = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}\{x_i \le x\} \]

*In words:* the fraction of observations at or below \(x\). Non-decreasing, steps of
\(1/n\), and it converges to the true CDF (this is the Glivenko–Cantelli theorem,
stated for later).

**Density as a scaled histogram** — for bin width \(h\) and count \(c_k\):

\[ \hat{f}(x) = \frac{c_k}{n h} \quad\text{for } x \text{ in bin } k \]

This is why a density integrates to 1 while the histogram's vertical axis counts.

**Q–Q coordinates** — plotting sample quantiles against theoretical quantiles:

\[ \left(\; \Phi^{-1}\!\left(\frac{i-0.5}{n}\right),\; x_{(i)} \;\right) \]

A straight line indicates agreement with the reference distribution; curvature
indicates skew; an S-shape indicates heavier or lighter tails.

## Expected knowledge after completion

You can, without notes:

- Given a question and variable types, name the correct plot and justify it.
- Build a three-panel figure showing a histogram, an ECDF and a box plot of the same
  variable, and explain what each adds.
- Demonstrate that changing bin width changes the apparent shape, and explain why
  the underlying data are unchanged.
- Read a Q–Q plot and say whether the tails are heavy.
- Take a published chart and state precisely what is misleading and how to fix it.
- Produce an EDA narrative with three figures and a written finding per figure.

## Connections to Data Science

- **Model diagnostics** are visualisation: residual plots, Q–Q plots of residuals,
  calibration curves, lift charts.
- **Imbalanced classification** is invisible in accuracy and obvious in a histogram
  of predicted probabilities.
- **Distribution shift** in production is detected by comparing ECDFs.
- **Feature selection** starts with pair plots and correlation heatmaps.
- **Stakeholder communication** is Unit 6: a chart with a finding as its title is
  read; one with a variable name is not.

## Practical applications

| Setting | Question | Plot |
|---|---|---|
| Hospital admissions | Is the daily count seasonal? | Line chart with a 7-day rolling mean |
| Loan defaults | How do defaulters differ? | Small multiples of key variables by outcome |
| Sensor network | Which sensor is failing? | ECDF comparison and z-score heatmap |
| Survey of satisfaction | Is the ordinal scale usable? | Stacked bars in order, never a pie |
| Model residuals | Is linearity plausible? | Residual vs fitted, Q–Q of residuals |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 6 | Identify the appropriate plot for stated questions |
| ★★ Application | 6 | Build specified figures correctly, with captions stating findings |
| ★★★ Challenge | 3 | Rebuild a misleading published chart honestly; find bimodality hidden by a box plot; produce an EDA narrative |
| Quiz | 10 items | Read charts, spot distortions |
| Practical notebook | 1 | Complete EDA of a provided dataset, six figures minimum |
| Critique | 1 page | Analysis of one misleading chart, with a corrected version |

Project 1 (describing a real dataset) is released here.

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Units 1–2: perception, integrity, grammar | 2.5 |
| 2 | Unit 3: univariate plots, bin width, box plot limits | 3.0 |
| 3 | Units 4–5: bivariate and multivariate | 2.5 |
| 4 | Unit 6: colour, accessibility, captions | 2.0 |
| 5 | Unit 7: full EDA workflow | 2.0 |

**Before this module:** [M03](03-data-and-descriptive-statistics.md). **After:**
[M05 — Counting and Combinatorics](05-counting-and-combinatorics.md) begins the
probability sequence, where the shapes you have just learned to see acquire
mathematical names.
