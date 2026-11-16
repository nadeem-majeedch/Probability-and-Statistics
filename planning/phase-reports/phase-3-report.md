# Phase 3 report — Chapters M01–M06

**Scope:** the six chapters of Part I and Part II's first half, written as complete
self-study textbook chapters.
**Date:** 14 November 2026
**Status:** Delivered and verified. No commits, pushes or deployment performed.

---

## 1. Chapters created

Each module now has two pages: its framework overview (`docs/modules/NN-slug.md`, from
Phase 2) and a full chapter (`docs/modules/NN-slug/chapter.md`). Navigation nests both
under one entry per module.

| Module | Chapter | Lines | Words |
|---|---|---|---|
| M01 | Introduction to Probability and Statistics | 753 | 6,127 |
| M02 | Mathematical Foundations for Statistics | 706 | 3,968 |
| M03 | Data and Descriptive Statistics | 763 | 5,015 |
| M04 | Data Visualization and Exploratory Statistical Analysis | 618 | 4,681 |
| M05 | Counting and Combinatorics | 590 | 3,407 |
| M06 | Probability Fundamentals | 569 | 3,568 |
| **Total** | **6 chapters** | **3,999** | **26,766** |

Every chapter follows the same 14-element structure: intuitive opening; why it
matters; terminology and notation; mathematical principles; step-by-step derivations;
worked numerical examples; common mistakes and misconceptions; data-science
connections; real-world scenarios; visual explanations; exercises; detailed
solutions; knowledge-check quiz; revision summary.

## 2. Topics covered

**M01** — population/sample, parameter/statistic, notation conventions, four scales
of measurement, the PPDAC cycle, observational studies vs experiments, six sampling
methods, four bias sources, sampling error and the √n law, Simpson's paradox, screening
tests and base rates.

**M02** — sets and counting rules for unions, functions and the logistic curve,
summation/product notation with derivations of Σi and Σi², exponent and log rules,
growth and doubling time, limits and the derivation of e, geometric series derivation,
derivatives (rules, chain, optimisation), integrals (fundamental theorem, from-first-
principles Riemann sum, improper integrals), factorials, binomial coefficients,
binomial theorem, matrices and XᵀX.

**M03** — the data rectangle, scales restated, missingness mechanisms (MCAR/MAR/MNAR),
six data defects, frequency and cumulative tables, mean (with both algebraic
properties), median, mode, weighted and geometric means, trimmed mean, range/IQR,
population vs sample variance with the degrees-of-freedom argument, CV, MAD, skewness,
z-scores, empirical rule vs Chebyshev, outlier fences, boxplots, five-number summaries,
aggregation traps.

**M04** — grammar of graphics, chart selection by question, perceptual ranking, axes and
zero baselines, histogram binning (Sturges, Freedman–Diaconis), colour palettes,
small multiples, eight chart-integrity defects and the lie factor, a seven-step EDA
workflow, Anscombe's quartet, log scales, heteroscedasticity, matplotlib/seaborn
examples.

**M05** — multiplication principle and its precondition, the four-case counting table,
permutations and combinations with derivations, Pascal's identity and binomial sum,
circular and necklace arrangements, multinomial coefficients, inclusion–exclusion,
stars and bars, pigeonhole, applications (passwords, lotteries, teams, seating,
birthdays, grid paths).

**M06** — sample spaces and event algebra, Kolmogorov's three axioms, proofs of
P(∅)=0, complement rule, bounds, addition rule, monotonicity, three-event
inclusion–exclusion, De Morgan, equally likely outcomes as an assumption, probability
by counting with consistent conventions, classical/frequentist/subjective
interpretations, geometric probability, validating a proposed pmf, independence as a
forward pointer to M07.

## 3. Worked examples

**40 fully solved worked examples**, each with every intermediate step shown and a
"reading it" sentence that interprets the number rather than restating it:

| Module | Examples | Highlights |
|---|---|---|
| M01 | 6 | Sampling error 82.4% vs 86.0%; variable classification; 2×2 screening table (PPV 26.9%); Simpson's paradox with full arithmetic |
| M02 | 7 | Summation by splitting; decibels; compound interest and doubling; exponential tail integral; binomial coefficients; revenue maximisation by derivative |
| M03 | 7 | Ten marks summarised in eleven steps (mean 68.3, s 14.76); one typo destroying mean and SD; weighted grade; geometric growth; grouped mean; pooled defect rate; CV comparison |
| M04 | 6 | Two bin widths on one dataset; Anscombe's quartet; truncated-axis lie factor 7.5; log scale; chart choice; funnel diagnosis |
| M05 | 6 | PIN with constraints; committee with a named member (165 + 330 = 495); BANANA; three sampling conventions; grid paths; three-set inclusion–exclusion |
| M06 | 8 | Two-dice table; at-least-one-head; five-card ace; two aces; inclusion–exclusion; without-replacement cases; bus waiting; pmf validation |

## 4. Exercises

**54 exercises** (9 per chapter), graded ★ (guided), ★★ (application), ★★★
(challenge), each with a **full solution** including the reasoning, not just the
answer. Solution counts match exercise counts 1:1 in every chapter (verified by
matching `**Exercise n` and `**Solution n` markers).

Challenge exercises include: designing a survey that avoids a stated bias; computing a
combined SD and explaining why averaging SDs fails; reconstructing Simpson's paradox
and writing both a misleading and an accurate sentence; proving Pascal's identity;
proving Σ(xᵢ−x̄)=0; showing the union bound; finding the redundancy needed for 0.999
reliability.

## 5. Quiz questions

**60 quiz items** (10 per chapter), each with a worked answer and explanation, and each
targeting a specific misconception rather than recall — for example "a positive on a
99%-specificity test at 0.1% prevalence: more likely true or false?", "which summaries
change when 92 becomes 992?", "why is the mean of a 1–5 satisfaction scale only a rough
summary?", "what is the lie factor of this chart?".

## 6. Validation results

| Check | Command | Result |
|---|---|---|
| Strict site build | `mkdocs build --strict` | **exit 0** |
| Maths delimiters / stray `$` | `python tools/check_math.py` | **exit 0** — 45 files balanced |
| Asset references | `python tools/check_assets.py` | **exit 0** |
| Internal `.md` links | relative-link resolver | **0 broken** |
| Example arithmetic | `python tools/check_examples.py` | **exit 0 — 168 assertions pass** |
| Chapter/nav wiring | 6 chapters globbed, all in `nav` | **6/6** |

`tools/check_examples.py` is new in this phase. It recomputes every numeric claim in
the six chapters from first principles — means, variances, quartiles, fences,
z-scores, weighted and geometric means, Sturges values, Anscombe's four summary sets,
every combinatorial count, and every probability — with tolerances, and exits non-zero
on any mismatch. It is the mechanism behind the claim "all numerical answers are
validated".

## 7. Defects found and fixed

| # | Defect | Fix |
|---|---|---|
| D8 | M06's dependency diagram computed the union as 6+18−3=21 while the caption said the events are disjoint (correct union: 24 of 36) | Diagram and caption corrected to the disjoint case |
| D9 | M03 stated s ≈ 278 after the 92→992 typo; the correct value is 293 (s² ≈ 85,958) | Recomputed and corrected, with the intermediate sum of squares shown |
| D10 | M03's piecewise median used `\\[2pt]`, which the maths checker tallies as an unclosed `\[` (30 open vs 29 close) | Spacing token removed; delimiters balanced |
| D11 | Anscombe's y₄ was tabulated against the shared x column, implying r = 0.816 when the true construction uses ten x = 8 and one x = 19 | y₄'s own x values documented; checker updated and now verifies r for all four |
| D12 | Roadmap chapter links were written `../modules/…` from `docs/roadmap.md` | Corrected to `modules/…`; link check confirms 0 broken |

## 8. Deliberately not done

- **No notebooks.** The chapters reference Python inline (M04 shows four plotting
  recipes) but no `.ipynb` files were added; the roadmap still lists them as planned.
- **No figures.** The visual explanations use Mermaid diagrams, tables and ASCII
  schematics. They render and are accessible as text, but they are not publication-
  quality vector figures; a figure pipeline remains a Phase 4 task.
- **M07–M18 remain framework-only.** No chapter content was written for them, and the
  roadmap says so.
- **No commits, pushes, deployments.** `main` still has zero commits; the remote is
  unchanged; all files remain untracked.
- **No browser check.** The built site was validated by `--strict` and the link/maths
  checkers, but the rendered pages were not viewed in a browser this phase.

## 9. Next phase (proposed)

1. M07 chapter (conditional probability, independence, Bayes) to the same standard.
2. M08–M11 to complete Part III.
3. Add the Part I labs planned in the catalogue (mean/median explorer, distribution
   explorer) so the chapters have their interactive companions.
