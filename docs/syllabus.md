---
title: Syllabus
description: Course outcomes, structure, schedule, assessment scheme and reading for Probability and Statistics for Data Science.
---

# Syllabus

**Probability and Statistics for Data Science**
BS Data Science · Department of Data Science (PUCIT), University of the Punjab, Lahore
Instructor: Engr. Dr. Muhammad Nadeem Majeed, Professor

---

## Course description

Statistics is the language in which data science makes claims. This course builds
that language from its foundations: what randomness is, how to model it, what a
sample can tell you about a population, how much confidence a number deserves, and
when a pattern is real.

The course is computational throughout. Every theoretical result is accompanied by
a simulation that reproduces it and a Python implementation that applies it. By
the end you will be able to derive a procedure, check it numerically, apply it to
real data, and state honestly what it does and does not support.

## Prerequisites

| Requirement | Detail |
|---|---|
| Mathematics | Intermediate (FSc / A-level) algebra. Calculus is rebuilt in Module 02; a rusty background is not a barrier. |
| Programming | None assumed. Basic Python helps; every line of code is explained. |
| Statistics | None assumed. |

## Course learning outcomes

By the end of the course you will be able to:

| # | Outcome | Assessed by |
|---|---|---|
| 1 | Summarise and visualise data appropriately for its type and structure | Quizzes M01–M04, Project 1 |
| 2 | Construct probability models and derive distributional properties from axioms | Exercises M05–M07 |
| 3 | Apply conditioning, independence and Bayes' theorem to applied problems | Exercises M07, Project 2 |
| 4 | Analyse single and joint behaviour of variables using expectation, variance and covariance | Exercises M08–M11 |
| 5 | Explain and apply the Law of Large Numbers and CLT, including their limits | Quiz M13, Project 2 |
| 6 | Derive estimators and evaluate them by bias, variance, consistency, efficiency | Exercises M14 |
| 7 | Construct and interpret intervals and tests with correct error control | Exercises M14–M15, Project 3 |
| 8 | Build and diagnose regression, ANOVA and chi-square models | Exercises M16–M17, Project 3 |
| 9 | Select and justify distribution-free, Bayesian or simulation-based methods | Exercises M17–M18 |
| 10 | Conduct and communicate a complete, reproducible statistical investigation | Capstone |

## Structure

**Eighteen modules in eight parts, 252 study hours.** Each module is a self-contained
study unit with objectives, prerequisites, a subtopic breakdown, derivations, worked
examples, a Python practical, exercises, a quiz and a revision summary. The
[dependency map](modules/index.md) shows which module must precede which.

| Part | Modules | Title | Hours | Focus |
|---|---|---|---|---|
| I | M01–M04 | Foundations | 44 | Orientation, mathematics, data, descriptive statistics, visualisation |
| II | M05–M07 | Probability | 38 | Counting, axioms, conditioning, Bayes |
| III | M08–M11 | Random variables | 58 | Distributions, expectation, joint laws |
| IV | M12–M13 | Sampling and limits | 26 | Sampling distributions, LLN, CLT |
| V | M14–M15 | Inference | 34 | Estimation, intervals, testing |
| VI | M16 | Relationships and modelling | 18 | Correlation, regression, diagnostics |
| VII | M17 | Comparative inference | 16 | ANOVA, chi-square, nonparametrics |
| VIII | M18 | Modern statistics | 18 | Bayesian, Monte Carlo, practice, capstone |

Full module list with levels and study hours: the [course map](modules/index.md). Each
part also has an overview page starting at [Part I](part-1-foundations/index.md).

## Schedule

### Two-semester sequence (recommended)

**Semester 1 — foundations, probability and sampling (M01–M12, 154 hours)**

| Week | Modules | Milestone |
|---|---|---|
| 1 | M01 | Diagnostic self-test |
| 2–3 | M02 | — |
| 4–5 | M03 | Project 1 released |
| 6 | M04 | Project 1 submitted |
| 7 | M05 | — |
| 8–9 | M06 | — |
| 10–11 | M07 | Quiz: M05–M07 |
| 12–13 | M08 | — |
| 14 | M09 | — |
| 15 | M10 | — |
| 16 | M11 | Semester revision |

**Semester 2 — inference, modelling and modern statistics (M13–M18, 98 hours)**

| Week | Modules | Milestone |
|---|---|---|
| 1 | M13 | Project 2 released |
| 2–3 | M14 | Project 2 submitted |
| 4–5 | M15 | — |
| 6–7 | M16 | Project 3 released |
| 8 | M16 | Project 3 submitted |
| 9–10 | M17 | Quiz: M16–M17 |
| 11–12 | M18 | Capstone brief read |
| 13–16 | Capstone | Capstone submitted |

### One-semester core track

If you have a single semester, take **M01–M08, M12, M14–M15** (≈146 hours) and treat
M09–M11, M13 and M16–M18 as a follow-on reading list. This covers description,
probability, random variables, sampling, estimation and testing — enough to read
applied work critically, though not enough to run a full modelling study.

| Week | Modules |
|---|---|
| 1 | M01 |
| 2–3 | M02 |
| 4–5 | M03 |
| 6 | M04 |
| 7 | M05 |
| 8–9 | M06 |
| 10–11 | M07 |
| 12–13 | M08 |
| 14 | M12 |
| 15 | M14 |
| 16 | M15, revision |

## Assessment

| Component | Weight | What it measures |
|---|---|---|
| Module quizzes (18) | 15% | Recall and conceptual grip |
| Exercise sets | 25% | Derivation and problem solving |
| Python practicals | 20% | Computation, simulation, reproducibility |
| Projects (3) | 25% | End-to-end analysis and communication |
| Capstone | 15% | Independent investigation |

**Projects**

1. **Describing a real dataset** (after M04) — clean, summarise and visualise, and defend every summary you chose.
2. **Probability by simulation** (after M13) — answer one probability question analytically, by exact enumeration, and by Monte Carlo, then reconcile the three.
3. **An inference study** (after M16) — design and run a test or interval on real data with a full assumption audit.

**Exercise difficulty**

| Marker | Meaning | What you should be able to do |
|---|---|---|
| ★ | Guided | Apply the definition or formula directly |
| ★★ | Application | Choose the method and carry it through several steps |
| ★★★ | Independent challenge | Prove, construct a counterexample, design a simulation, or critique a claim |

**How self-marking works.** Every quiz item and exercise has a complete solution.
Mark yourself against the *reasoning*, not the final number: a correct answer with
a wrong justification scores as a miss. A module is complete when you can
reproduce its central result on a blank page.

## Study time

| Part | Hours | Share |
|---|---|---|
| I Foundations | 44 | 17% |
| II Probability | 38 | 15% |
| III Random variables | 58 | 23% |
| IV Sampling and limits | 26 | 10% |
| V Inference | 34 | 14% |
| VI Relationships | 18 | 7% |
| VII Comparative | 16 | 6% |
| VIII Modern | 18 | 7% |
| **Total** | **252** | **100%** |

With orientation, reference reading and revision: **≈265 hours**. That is roughly
10 hours per week for a 16-week first semester and about 6 hours per week plus
capstone work in the second.

## Tools

Python 3.12 or 3.13 with NumPy, pandas, SciPy, Matplotlib, Seaborn, statsmodels and
scikit-learn. All free and open source; no licences, subscriptions or accounts are
required anywhere in the course. Setup instructions: [set up your computer](setup.md).

## Reading

The course is self-contained: every result is derived in the module where it is
used, so no textbook is required. For deeper or alternative treatments, each
module ends with a short "Further reading" list. The works most often referenced
are:

- Casella, G. & Berger, R. L. *Statistical Inference*, 2nd ed., Duxbury, 2002.
- Ross, S. *A First Course in Probability*, 10th ed., Pearson, 2019.
- Wasserman, L. *All of Statistics*, Springer, 2004.
- DeGroot, M. H. & Schervish, M. J. *Probability and Statistics*, 4th ed., Pearson, 2012.
- Gelman, A. et al. *Bayesian Data Analysis*, 3rd ed., CRC Press, 2013.
- James, G. et al. *An Introduction to Statistical Learning*, 2nd ed., Springer, 2021.
- Efron, B. & Tibshirani, R. J. *An Introduction to the Bootstrap*, Chapman & Hall, 1993.
- McKinney, W. *Python for Data Analysis*, 3rd ed., O'Reilly, 2022.

## Policies

**Academic integrity.** Work the exercises before opening solutions. Submitting
copied solutions as your own work is misconduct in every programme, and it defeats
the only purpose this course has.

**Data and privacy.** All datasets used are openly licensed and contain no personal
or identifiable information. Synthetic data is labelled as synthetic wherever it
appears. Progress tracking is stored only in your own browser; the course collects
no analytics and sets no tracking cookies.

**Accessibility.** The site targets WCAG 2.2 AA: keyboard navigation, sufficient
contrast, figure descriptions, and a plain-language reading of every display
equation. If you meet a barrier, please report it through the repository's issue
tracker.

**Corrections.** Errata are welcome and are corrected in the open. See
[licence and citation](about/licence.md) for how to cite the course and report
errors.
