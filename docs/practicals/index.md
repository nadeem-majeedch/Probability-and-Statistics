---
title: Python practicals
description: Nineteen runnable Jupyter notebooks — one for each module plus a Python foundation — with exercises, solutions and interpretation.
---

# Python practicals

Each module has a companion notebook that runs the chapter's methods on generated data,
prints the numbers, and interprets them. The notebooks are part of the course, not an
appendix: every statistical idea in the chapters appears here as something you can
execute and change.

The sequence starts with a short Python foundation and then mirrors the eighteen modules.

## Paired interactive laboratories

Every notebook now has a browser-based companion laboratory that isolates the one
idea the notebook demonstrates. Use the lab first to build intuition, then the
notebook to compute the same quantities in Python.

| Practical | Interactive laboratory |
|---|---|
| [06 · Probability fundamentals](notebooks/06-probability-fundamentals.ipynb) | [L-01 · random events](../labs/probability.md) |
| [07 · Conditional probability and Bayes](notebooks/07-conditional-probability-and-bayes.ipynb) | [L-02 · Bayes' theorem](../labs/conditional-probability.md) |
| [09 · Discrete distributions](notebooks/09-discrete-distributions.ipynb) | [L-03 · discrete distributions](../labs/discrete-distributions.md) |
| [10 · Continuous distributions](notebooks/10-continuous-distributions.ipynb) | [L-04](../labs/continuous-distributions.md) and [L-05](../labs/normal-and-z-scores.md) |
| [12 · Sampling distributions](notebooks/12-sampling-and-sampling-distributions.ipynb) | [L-08 · sampling distributions](../labs/sampling-distributions.md) |
| [13 · LLN and CLT](notebooks/13-law-of-large-numbers-and-clt.ipynb) | [L-06](../labs/law-of-large-numbers.md) and [L-07](../labs/clt.md) |
| [14 · Confidence intervals](notebooks/14-estimation-and-confidence-intervals.ipynb) | [L-09 · interval coverage](../labs/confidence-intervals.md) |
| [15 · Hypothesis testing](notebooks/15-hypothesis-testing.ipynb) | [L-10 · p-values](../labs/p-values.md) and [L-13 · power](../labs/power-and-errors.md) |
| [16 · Correlation and regression](notebooks/16-correlation-and-regression.ipynb) | [L-11 · regression](../labs/correlation-regression.md) |
| [17 · ANOVA and chi-square](notebooks/17-anova-chi-square-nonparametric.ipynb) | [L-14 · ANOVA](../labs/anova.md) |
| [18 · Bayesian methods](notebooks/18-bayesian-and-data-science-methods.ipynb) | [L-12 · Bayesian updating](../labs/bayesian-updating.md) |

## How to use a notebook

1. **Read the chapter first.** The notebook assumes the theory; it does not replace it.
2. **Predict before you run.** Read a cell, decide what the output should be, then run it.
3. **Change one thing.** A sample size, a seed, a probability — and check whether the
   output moves the way the theory says it should.
4. **Do the exercises before the solutions.** The solutions are in the notebook, so the
   only protection against reading them first is your own discipline.
5. **Restart and run all** when you finish, to confirm the notebook works from top to
   bottom in order.

## From practice to projects

These notebooks are guided: run the cell, read the number. The
[project section](../projects/index.md) is the other half — a question, a dataset and no
instructions beyond the brief. Start there once you can run a notebook without help.

## Download

Notebooks are ordinary `.ipynb` files. Use the links in the table — your browser saves
the file — then open it with JupyterLab:

```bash
jupyter lab 00-python-foundation.ipynb
```

They contain **no stored outputs**, which keeps the files small; running a cell produces
its output. Every notebook sets its random seeds, so your numbers will match the ones
described in the text. See [Python foundation](python-foundation.md) if you have not set
up the environment yet.

## Notebook index

| # | Notebook | Module chapter |
|---|---|---|
| 00 | [Python foundation](notebooks/00-python-foundation.ipynb) | — (start here) |
| 01 | [Descriptive statistics from examination data](notebooks/01-descriptive-statistics.ipynb) | [M01](../modules/01-introduction-to-statistics/chapter.md) |
| 02 | [Mathematical foundations](notebooks/02-mathematical-foundations.ipynb) | [M02](../modules/02-mathematical-foundations/chapter.md) |
| 03 | [Working with a student dataset](notebooks/03-data-and-descriptive-statistics.ipynb) | [M03](../modules/03-data-and-descriptive-statistics/chapter.md) |
| 04 | [Data visualization](notebooks/04-data-visualization.ipynb) | [M04](../modules/04-data-visualization/chapter.md) |
| 05 | [Counting and combinatorics](notebooks/05-counting-and-combinatorics.ipynb) | [M05](../modules/05-counting-and-combinatorics/chapter.md) |
| 06 | [Coins, dice and probability](notebooks/06-probability-fundamentals.ipynb) | [M06](../modules/06-probability-fundamentals/chapter.md) |
| 07 | [Conditional probability and Bayes](notebooks/07-conditional-probability-and-bayes.ipynb) | [M07](../modules/07-conditional-probability-and-bayes/chapter.md) |
| 08 | [Random variables and expectation](notebooks/08-random-variables-and-expectation.ipynb) | [M08](../modules/08-random-variables-and-expectation/chapter.md) |
| 09 | [Discrete distributions](notebooks/09-discrete-distributions.ipynb) | [M09](../modules/09-discrete-distributions/chapter.md) |
| 10 | [Continuous distributions and the normal curve](notebooks/10-continuous-distributions.ipynb) | [M10](../modules/10-continuous-distributions/chapter.md) |
| 11 | [Joint distributions](notebooks/11-joint-distributions.ipynb) | [M11](../modules/11-joint-distributions/chapter.md) |
| 12 | [Sampling distributions](notebooks/12-sampling-and-sampling-distributions.ipynb) | [M12](../modules/12-sampling-and-sampling-distributions/chapter.md) |
| 13 | [Law of Large Numbers and CLT](notebooks/13-law-of-large-numbers-and-clt.ipynb) | [M13](../modules/13-law-of-large-numbers-and-clt/chapter.md) |
| 14 | [Estimation and confidence intervals](notebooks/14-estimation-and-confidence-intervals.ipynb) | [M14](../modules/14-estimation-and-confidence-intervals/chapter.md) |
| 15 | [Hypothesis testing](notebooks/15-hypothesis-testing.ipynb) | [M15](../modules/15-hypothesis-testing/chapter.md) |
| 16 | [Correlation and regression](notebooks/16-correlation-and-regression.ipynb) | [M16](../modules/16-correlation-and-regression/chapter.md) |
| 17 | [ANOVA, chi-square and nonparametric tests](notebooks/17-anova-chi-square-nonparametric.ipynb) | [M17](../modules/17-anova-chi-square-nonparametric/chapter.md) |
| 18 | [Bayesian statistics and data-science methods](notebooks/18-bayesian-and-data-science-methods.ipynb) | [M18](../modules/18-bayesian-and-data-science-methods/chapter.md) |

## What is in every notebook

Each follows the same twelve sections, so you always know where to look:

1. Introduction
2. Learning objectives
3. Required libraries
4. Concepts
5. Formulas
6. Implementation
7. Output and interpretation
8. Visualisation
9. Practical scenario
10. Exercises
11. Solutions
12. Summary

The **Output and interpretation** section is the one to read even when the code works:
it says what the numbers mean in statistical language, and what they do not mean.

## The experiments covered

| Experiment | Notebook |
|---|---|
| Descriptive statistics from examination data | 01, 03 |
| Mean, median, mode, quantiles | 01 |
| Variance and standard deviation | 01, 08 |
| Histograms and box plots | 01, 04 |
| Random experiments and coin tossing | 06 |
| Dice simulations | 06 |
| Conditional probability | 07 |
| Bayes' theorem | 07 |
| Discrete distribution simulations | 09 |
| Normal distribution visualisation | 10 |
| Probability density and cumulative distribution | 10 |
| Monte Carlo estimation | 13, 18 |
| Law of Large Numbers | 13 |
| Central Limit Theorem | 13 |
| Sampling distribution simulations | 12 |
| Confidence interval calculations | 14 |
| Hypothesis testing | 15 |
| Correlation analysis | 16 |
| Linear regression | 16 |
| ANOVA | 17 |
| Chi-square tests | 17 |
| Bootstrap estimation | 18 |
| Bayesian updating | 07, 18 |

## Applied case studies

The notebooks teach the mechanics; the [case studies](../case-studies/index.md) apply them
to realistic problems. Twenty-four cases are graded easy, intermediate and advanced, each
with its own downloadable dataset, questions and worked solution.

## Reproducibility and checking

- Every simulation sets a seed with `np.random.default_rng(...)`.
- Notebooks are generated from Markdown sources in `tools/notebook_sources/` and stored
  without outputs, so the repository stays small and the site never embeds large cell
  output.
- `tools/check_notebooks.py` runs every notebook from top to bottom in a clean kernel and
  fails if any cell raises an error, if a required section is missing, or if the stored
  outputs are stale.

That check is run before every release, so a notebook that does not execute is a bug, not
an exercise.
