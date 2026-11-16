# 11 — Approved Module Framework (18 modules)

**Status: authoritative.** This document records the approved 18-module curriculum
and its relationship to the earlier 30-module draft. Where the two disagree, this
document and `docs/modules/` win.

---

## 1. What changed and why

The 30-module draft in [02 — Curriculum](02-curriculum.md) split the course into fine
grains: separate modules for variance, for each distribution family, for correlation
and for simple regression. That structure had advantages for staged delivery, but
produced eighteen *parts-level* topics spread over thirty headers, and the
duplication of introductory material across M01–M04.

The approved framework consolidates to **18 modules**. Consolidation is not
compression of content: the same topics are taught, but where two topics share one
mathematical apparatus they now share one module, which reduces repetition and makes
prerequisite chains shorter and more honest.

| Change | Consequence |
|---|---|
| Introduction (new) becomes M01 | Orientation, vocabulary and study method before notation |
| Maths and data split stays | M02 notation, M03 data + descriptive measures |
| Expectation and variance unified in M08 | The two halves of "summarising a distribution" taught together |
| Correlation and regression unified in M16 | Correlation is the standardised slope; splitting them hid that |
| ANOVA, chi-square and nonparametrics unified in M17 | All three are "compare groups / counts without normality" |
| Bayesian and practice unified in M18 | Both answer "what do I do in real work" |

## 2. The approved modules

| # | Module | Part | Hours | Level |
|---|---|---|---|---|
| M01 | Introduction to Probability and Statistics | I | 6 | Beginner |
| M02 | Mathematical Foundations for Statistics | I | 12 | Beginner |
| M03 | Data and Descriptive Statistics | I | 14 | Beginner |
| M04 | Data Visualization and Exploratory Statistical Analysis | I | 12 | Beginner |
| M05 | Counting and Combinatorics | II | 10 | Beginner |
| M06 | Probability Fundamentals | II | 14 | Core |
| M07 | Conditional Probability and Bayes' Theorem | II | 14 | Core |
| M08 | Random Variables and Mathematical Expectation | III | 16 | Core |
| M09 | Discrete Probability Distributions | III | 14 | Core |
| M10 | Continuous Probability Distributions | III | 14 | Core |
| M11 | Joint Probability Distributions | III | 14 | Advanced |
| M12 | Sampling and Sampling Distributions | IV | 14 | Core |
| M13 | Law of Large Numbers and Central Limit Theorem | IV | 12 | Advanced |
| M14 | Statistical Estimation and Confidence Intervals | V | 16 | Core |
| M15 | Hypothesis Testing | V | 18 | Core |
| M16 | Correlation and Regression | VI | 18 | Core |
| M17 | ANOVA, Chi-Square and Nonparametric Statistics | VII | 16 | Advanced |
| M18 | Bayesian Statistics and Statistical Methods for Data Science | VIII | 18 | Advanced |

**Total: 252 study hours** (≈250). Two semesters at ~10 h/week, or one semester for the
core track.

## 3. Mapping from the 30-module draft

Every draft module has a home. Nothing was dropped.

| Draft (30) | Approved (18) | Note |
|---|---|---|
| 01 Mathematical Foundations | M02 | Same content, renumbered |
| 02 Data and Statistical Thinking | M01, M03 | Orientation split out; data typing moved to M03 |
| 03 Descriptive Statistics | M03 | — |
| 04 Data Visualization | M04 | — |
| 05 Counting | M05 | — |
| 06 Axioms of Probability | M06 | — |
| 07 Conditional Probability | M07 | — |
| 08 Bayes' Theorem | M07 | Merged: one theorem, one module |
| 09 Random Variables | M08 | — |
| 10 Discrete Distributions | M09 | — |
| 11 Continuous Distributions | M10 | — |
| 12 Joint Distributions | M11 | — |
| 13 Expectation and Moments | M08 | Merged into M08 |
| 14 Variance and Covariance | M08 (variance), M11 (covariance) | Split by object: one variable vs two |
| 15 Sampling Distributions | M12 | — |
| 16 Law of Large Numbers | M13 | — |
| 17 Central Limit Theorem | M13 | Merged: one convergence module |
| 18 Point Estimation | M14 | — |
| 19 Confidence Intervals | M14 | Merged: estimation and its uncertainty |
| 20 Hypothesis Testing | M15 | — |
| 21 Correlation and Association | M16 | — |
| 22 Simple Linear Regression | M16 | — |
| 23 Multiple Linear Regression | M16 | Merged with diagnostics |
| 24 ANOVA | M17 | — |
| 25 Chi-Square Tests | M17 | — |
| 26 Nonparametric Statistics | M17 | — |
| 27 Bayesian Statistics | M18 | — |
| 28 Monte Carlo | M18 | — |
| 29 Statistics for Data Science Practice | M18 | — |
| 30 Capstone | M18 (capstone subsection) | Capstone becomes the M18 deliverable, not a module |

## 4. Effects on the delivery plan

| Item | Change |
|---|---|
| Module pages | 30 → 18; each now carries the full overview (intro, rationale, objectives, prerequisites, units, mathematics, outcomes, DS connections, applications, assessment, sequence) |
| Notebooks | target 18 → **14–16** (one per module where computation matters; M01 needs none) |
| Parts | unchanged, eight parts (now 4/3/4/2/2/1/1/1 modules) |
| Phases | Phase 2 = M01–M04, Phase 3 = M05–M07, Phase 4 = M08–M11, Phase 5 = M12–M15, Phase 6 = M16–M18 |
| Hours | 254 → 252 |
| Labs | unchanged in count; L-04/L-05 already delivered |

Parts VI–VIII now hold a single module each. That is intentional: they remain useful
as thematic introductions, and the grouping keeps the eight-part navigation stable.

## 5. Documentation status

| Document | Status |
|---|---|
| `docs/modules/*.md` (18 pages) | **Authoritative** student-facing framework |
| `docs/modules/index.md` | Authoritative module map, dependency graph, sequences |
| [02 — Curriculum](02-curriculum.md) | Historical design record (30-module draft); kept for the sequencing rationale and coverage matrix |
| [04 — Module Learning Objectives](04-module-learning-objectives.md) | Historical design record (30-module draft); objectives are now published per module in `docs/modules/` |
| [08 — Implementation Roadmap](08-implementation-roadmap.md) | Phases still valid; module counts per phase updated in §4 above |

The historical documents are retained rather than deleted: they contain the reasoning
behind the sequencing, the simulation catalogue and the misconception lists, all of
which remain useful when writing chapters.
