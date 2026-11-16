---
title: Course roadmap
description: The honest inventory of everything in the course, and what is still planned.
---

# Course roadmap

The course is complete and everything below is published. This page is the honest
inventory: what you can study **today**, what was added when, and the small number of
extras that are still planned.

Nothing is marked available until it has passed verification — mathematical
checking, exercise solutions, notebook execution, link and accessibility checks,
and a clean site build. A page that exists but has not been verified is not
listed as ready.

## Available now

| Item | What it gives you |
|---|---|
| [Syllabus](syllabus.md) | Outcomes, schedule, assessment scheme, reading |
| [How to study](how-to-study.md) | The seven-step self-study protocol |
| [Set up your computer](setup.md) | A working Python environment |
| [Course map](modules/index.md) | All 18 modules, dependency graph, prerequisites, three study sequences |
| [Module overviews M01–M18](modules/index.md) | For every module: introduction, rationale, objectives, prerequisites, subtopic breakdown, key mathematics, expected outcomes, data-science connections, applications, assessment plan, study sequence |
| **Chapters M01–M18** | Full textbook chapters for all eighteen modules — [M01](modules/01-introduction-to-statistics/chapter.md), [M02](modules/02-mathematical-foundations/chapter.md), [M03](modules/03-data-and-descriptive-statistics/chapter.md), [M04](modules/04-data-visualization/chapter.md), [M05](modules/05-counting-and-combinatorics/chapter.md), [M06](modules/06-probability-fundamentals/chapter.md), [M07](modules/07-conditional-probability-and-bayes/chapter.md), [M08](modules/08-random-variables-and-expectation/chapter.md), [M09](modules/09-discrete-distributions/chapter.md), [M10](modules/10-continuous-distributions/chapter.md), [M11](modules/11-joint-distributions/chapter.md), [M12](modules/12-sampling-and-sampling-distributions/chapter.md), [M13](modules/13-law-of-large-numbers-and-clt/chapter.md), [M14](modules/14-estimation-and-confidence-intervals/chapter.md), [M15](modules/15-hypothesis-testing/chapter.md), [M16](modules/16-correlation-and-regression/chapter.md), [M17](modules/17-anova-chi-square-nonparametric/chapter.md), [M18](modules/18-bayesian-and-data-science-methods/chapter.md) — each with derivations, worked examples, misconceptions, data-science links, exercises with full solutions, a quiz and a revision summary |
| [Python practicals](practicals/index.md) | Nineteen runnable Jupyter notebooks — a Python foundation plus one per module — with formulas, code, interpretation, visualisations, exercises and solutions. Downloadable from each chapter. |
| [Case studies](case-studies/index.md) | Twenty-four scenario-based case studies — eight easy, eight intermediate, eight advanced — each with a problem statement, synthetic dataset, Python implementation and full solution. |
| [Self-assessment and examinations](assessments/index.md) | Eighteen module banks (15 interactive MCQs, 10 short, 10 numerical, 5 scenario and 3 analytical items each with worked answers) and five examination papers, all printable. |
| [Part I overview](part-1-foundations/index.md) … [Part VIII overview](part-8-modern/index.md) | The thematic argument for each part, with its misconceptions table |
| [Fourteen interactive laboratories](labs/index.md) | One per major topic, from random events to ANOVA: probability, conditional probability and Bayes, discrete and continuous distributions, the normal curve and z-scores, the law of large numbers, the CLT, sampling distributions, confidence intervals, p-values, correlation and regression, Bayesian updating, errors and power, and ANOVA. Each has objectives, the mathematics, a live experiment, interpretation, guided activities, challenges and self-assessment. |
| [Statistical tables](reference/tables/index.md) | Four critical-value references — standard normal, Student's \(t\), chi-square and \(F\) — each with the tail convention, the degrees-of-freedom rules, worked tests and a downloadable CSV, plus [a guide to choosing between them](reference/tables/choosing-a-table.md). Every cell is generated from SciPy and re-checked before the build. |
| Figures | 24 original SVG figures — counting trees, histograms and box plots, distributions, joint densities, sampling, the CLT, coverage, hypothesis tests, correlation and regression, ANOVA and Bayesian updating — embedded in 14 chapters, with captions and worked explanations |

All eighteen modules (M01–M18) now have **complete chapters** in addition to their
framework overview: derivations from first principles, step-by-step worked examples,
three-level exercise sets with full solutions, a quiz, and an honest statement of
assumptions and limitations. Every numerical claim in every chapter is recomputed by
`tools/check_examples.py`.

## Release history

| Release | Content | Status |
|---|---|---|
| **Done** | Part I — full chapters for M01–M04 | **Available** |
| **Done** | M05–M07 — counting, probability, conditional probability | **Available** |
| **Done** | Part III — M08–M11, random variables and distributions | **Available** |
| **Done** | M12 — sampling and sampling distributions | **Available** |
| **Done** | M13 — Law of Large Numbers and the CLT | **Available** |
| **Done** | Part V — M14 estimation, M15 hypothesis testing | **Available** |
| **Done** | Part VI — M16 correlation and regression | **Available** |
| **Done** | Part VII — M17 ANOVA, chi-square, nonparametric tests | **Available** |
| **Done** | Part VIII — M18 Bayesian statistics and data-science methods | **Available** |
| **Done** | Projects (nine, with datasets, notebooks and solutions), formula sheets, glossary, revision pack | **Available** |
| Planned | Quick-reference statistical tables (t, F, chi-square) | Not yet published |

## What "complete" will mean for each module

Every module is released as a chapter only when it contains all twelve sections:

1. Learning objectives
2. Before you start (prerequisites)
3. The idea in plain language
4. Notation and derivation
5. Intuition
6. Worked examples
7. Where this is used
8. Visual explanations
9. Python demonstration
10. Exercises (★, ★★, ★★★)
11. Self-assessment quiz with explained answers
12. Summary and revision

…plus a verified build, working links, and accessible figures. Today M01–M18 deliver all
twelve. Every numerical claim in all eighteen chapters is recomputed by
`tools/check_examples.py`; every notebook is executed end to end by
`tools/check_notebooks.py`, every case study by `tools/check_case_studies.py`; and the site is validated by a strict MkDocs build, a math
delimiter check, an asset check and a relative-link check.

## Labs planned

Interactive labs are released alongside the modules that use them. Two are live; the
rest are specified in the lab catalogue.

| Lab | Module | What you will manipulate |
|---|---|---|
| Mean, median and standard deviation | M03 | Draggable data points; the mean moves, the median resists |
| Distribution explorer | M09–M10 | Family and parameters; watch the shape, mean and variance respond |
| Bayes updater | M07, M18 | Prior, data and posterior, live |
| Sampling machine | M12 | Sample size and replications; the distribution of the sample mean |
| Law of Large Numbers | M13 | Running averages, including a heavy-tailed case that never settles |
| p-values and rejection regions | M15 | Effect size, sample size, α; watch p change with *n* |
| Type I / Type II errors and power | M15 | Overlapping hypotheses; trade off α, β and *n* |
| Correlation and regression | M16 | Correlation, noise, and one draggable outlier |
| ANOVA and post-hoc comparison | M17 | Group means, spread and \(n\); see F and Tukey intervals move |
| Bootstrap | M17–M18 | Resampling distribution and intervals |
| Permutation test | M17 | Randomisation as the reference distribution |
| A/B test simulator | M18 | Peeking, power and false positives under optional stopping |

!!! success "Live now"
    All fourteen laboratories are available in the
    [laboratory index](labs/index.md). They are dependency-free, keyboard accessible,
    work in light and dark themes, and every calculation is checked by an automated
    test suite against SciPy reference values.

## Applying it: projects

The [project-based learning section](projects/index.md) turns the modules into practice: eight
graded projects on student performance, diagnostics, A/B testing, quality control, weather,
credit risk, cricket and prediction uncertainty, plus a capstone that combines the whole
course. Each has a dataset, a starter notebook and a reference solution.

## How updates are announced

Each release adds pages to the navigation. Because the repository is version
controlled, every change is visible in its history — including corrections, which
are never made silently.

## Follow-on topics

Outside this course's scope, and worth studying afterwards: multivariate methods
(PCA, MANOVA, factor analysis), time-series analysis, stochastic processes,
causal inference, and statistical machine learning. The closing unit of
[M18](modules/18-bayesian-and-data-science-methods.md) points to which of these
follow naturally from what you have learned.
