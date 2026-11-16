# Project-based learning

Eight projects and one capstone in which you carry out a full statistical investigation on a
dataset you have not seen: audit it, describe it, model it, quantify uncertainty, and defend a
decision. Each project comes with a brief, a starter notebook, the dataset, and a separate
reference solution that shows one defensible way to do it.

!!! note "Synthetic data"
    Every dataset here is simulated with a documented mechanism and a fixed random seed, so
    results are reproducible and no real person, institution or match is described. Do not
    present these findings as real-world research.

## How the section works

| Part | What you get |
|---|---|
| **Project brief** | Background, problem statement, objectives, dataset, research questions, methods, tasks, expected figures, deliverable list and rubric |
| **Starter notebook** | The section skeleton with imports, data loading and `# TODO` cells — never a finished analysis |
| **Dataset** | A CSV in `docs/data/projects/`, unchanged and reproducible |
| **Reference solution** | A worked investigation with the numbers actually obtained from the data, plus the reasoning and the mistakes to avoid |

The reference solution is published **after** you submit, and is deliberately not a golden
answer: several defensible analyses exist, and the rubric rewards justification, not agreement
with the reference.

## Projects

| # | Project | Focus | Level | Weeks |
|---|---|---|---|---|
| P01 | [University student performance](p01-student-performance.md) | Description, correlation, multiple regression, group comparison | Foundation | 2 |
| P02 | [Healthcare diagnostic accuracy](p02-diagnostics-bayes.md) | Bayes, screening, ROC, logistic regression | Foundation | 2 |
| P03 | [E-commerce conversion and A/B testing](p03-ecommerce-ab-test.md) | Proportions, intervals, hypothesis tests, segments | Foundation | 3 |
| P04 | [Manufacturing quality control](p04-manufacturing-quality.md) | Counts, over-dispersion, control charts, negative binomial | Intermediate | 3 |
| P05 | [Weather, probability and distributions](p05-weather-distributions.md) | Distributions, seasonality, extremes, model choice | Intermediate | 3 |
| P06 | [Credit risk modelling](p06-credit-risk.md) | Logistic regression, odds ratios, discrimination, decisions | Intermediate | 3 |
| P07 | [Cricket and statistical inference](p07-cricket-inference.md) | Binomial tests, paired data, small groups, shrinkage | Intermediate | 2 |
| P08 | [Prediction uncertainty](p08-model-uncertainty.md) | Calibration, Brier score, ROC, thresholds | Advanced | 3 |
| C | [Capstone: subscription churn](p09-capstone.md) | All of Modules 01–18 in one investigation | Capstone | 5 |

## What is expected of every project

1. **An audit before an analysis.** Types, ranges, missing values, duplicates, impossible
   values. Every cleaning decision is recorded.
2. **A description that matches the variable.** Medians and IQRs for skewed data, proportions
   with intervals for categories, not means of codes.
3. **Assumptions checked, not asserted.** Normality, independence, equal variance, expected
   counts: whichever apply, with a diagnostic.
4. **Uncertainty attached to every estimate.** A number without an interval is a rumour.
5. **Interpretation in the language of the problem.** "A 50-point higher credit score is
   associated with about 40 % lower odds of default", not "β = −0.010".
6. **A stated limitation that is specific.** "Selection into the loyalty programme could
   explain part of the association" beats "the sample is small".

## Marking

Every project is marked out of 100 with the same weights, so you always know where the marks
are:

| Criterion | Weight | What earns full marks |
|---|---|---|
| Data audit and preparation | 10 | Every issue found, every decision justified |
| Descriptive analysis | 15 | Appropriate summaries, correct figures, no meaningless statistics |
| Statistical method | 25 | Correct test or model, assumptions checked, alternatives considered |
| Uncertainty and inference | 15 | Intervals, effect sizes, and correct interpretation of p-values |
| Interpretation and decision | 20 | Conclusions answer the stated question, in context, with the limits named |
| Reproducibility and code | 10 | Notebook runs top to bottom, no manual edits, readable code |
| Communication | 5 | Report is structured, figures are captioned with takeaways |

## Submitting

Submit the executed notebook (outputs visible) and a report of at most six pages. The notebook
must run from top to bottom on a clean kernel with the dataset in place. Do not edit the CSV,
and do not delete rows without saying so.

## Getting help

- Module chapters for the method you are using.
- The [dataset files](../data/projects/README.md) — column meanings, row counts and the seeds
  that make every project CSV reproducible.
- The [case studies](../case-studies/index.md) for worked examples of the same techniques.
- The [self-assessment banks](../assessments/index.md) if a method feels shaky before you
  start.
