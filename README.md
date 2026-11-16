# Probability and Statistics for Data Science

**A complete, self-study course for BS Data Science students**

> Learn to reason under uncertainty — from counting principles and probability
> axioms to Bayesian inference, regression and Monte Carlo simulation — through
> full derivations, worked numerical examples, and Python you run yourself.

**Course instructor**

**Engr. Dr. Muhammad Nadeem Majeed**
Professor
Department of Data Science (PUCIT)
University of the Punjab, Lahore

---

## Welcome

Welcome to *Probability and Statistics for Data Science*. This repository is the
complete course: readings, derivations, worked examples, Python demonstrations,
exercises, solutions, quizzes and projects. It is written for **independent
study**. Nothing in it assumes that an instructor is standing beside you to fill
in a missing step — every result is derived, every symbol is defined, and every
example is worked out in full.

Statistics is the language in which data science makes claims. Machine learning
models, A/B tests, dashboards, clinical trials and public-policy decisions all
rest on the ideas in this course: what randomness is, what a sample can tell you
about a population, how much confidence a number deserves, and when a pattern is
real. The aim here is not to memorise tests. The aim is to think clearly about
uncertainty — and to be able to prove, compute and simulate what you think.

## Who this course is for

| | |
|---|---|
| **Programme** | BS Data Science (and closely related programmes) |
| **Level** | Beginner to advanced — no prior statistics assumed |
| **Prerequisites** | Intermediate (FSc / A-level) mathematics: algebra, functions, basic calculus. Module 02 rebuilds everything else you need. |
| **Programming** | Basic Python helpful but not required; every demonstration is explained line by line |
| **Study time** | 252 module-hours (~265 with revision): two semesters, or ~146 hours for the core track |
| **Cost** | Free. All software used is open source. |

## What you will be able to do

By the end of this course you will be able to:

1. **Summarise** a dataset honestly — choosing measures and graphics that fit the
   data type and expose, rather than hide, its structure.
2. **Model** randomness with probability spaces, random variables and
   distributions, and derive their properties from definitions.
3. **Reason conditionally** — apply conditional probability, independence and
   Bayes' theorem to diagnostic testing, classification and updating of belief.
4. **Work with several variables at once**, using joint, marginal and conditional
   distributions, expectation, covariance and correlation.
5. **Explain and use the limit theorems** — the Law of Large Numbers and the
   Central Limit Theorem — and know precisely when they fail.
6. **Estimate** unknown quantities by method of moments and maximum likelihood,
   and judge estimators by bias, variance, consistency and efficiency.
7. **Quantify uncertainty** with confidence intervals, and **test hypotheses**
   while controlling error rates and interpreting p-values correctly.
8. **Model relationships** with correlation, simple and multiple regression,
   ANOVA and chi-square procedures, checking assumptions rather than assuming them.
9. **Apply distribution-free and simulation-based methods** — rank tests,
   permutation tests, the bootstrap, Bayesian updating and Monte Carlo — when
   classical assumptions do not hold.
10. **Communicate** a statistical analysis reproducibly, in code, for a
    non-specialist audience.

## Course map

**Eighteen modules in eight parts, 252 study hours.** The course is a full
two-semester sequence; a shorter one-semester **core track** is described in the
study calendar below. Each module overview lists its prerequisites, topic
breakdown, mathematical core, assessment plan and study sequence — start at the
[course map on the website](docs/modules/index.md) for the dependency graph.

| # | Module | Part | Level | Hours |
|---|---|---|---|---|
| M01 | Introduction to Probability and Statistics | I | Beginner | 6 |
| M02 | Mathematical Foundations for Statistics | I | Beginner | 12 |
| M03 | Data and Descriptive Statistics | I | Beginner | 14 |
| M04 | Data Visualization and Exploratory Statistical Analysis | I | Beginner | 12 |
| M05 | Counting and Combinatorics | II | Beginner | 10 |
| M06 | Probability Fundamentals | II | Core | 14 |
| M07 | Conditional Probability and Bayes' Theorem | II | Core | 14 |
| M08 | Random Variables and Mathematical Expectation | III | Core | 16 |
| M09 | Discrete Probability Distributions | III | Core | 14 |
| M10 | Continuous Probability Distributions | III | Core | 14 |
| M11 | Joint Probability Distributions | III | Advanced | 14 |
| M12 | Sampling and Sampling Distributions | IV | Core | 14 |
| M13 | Law of Large Numbers and Central Limit Theorem | IV | Advanced | 12 |
| M14 | Statistical Estimation and Confidence Intervals | V | Core | 16 |
| M15 | Hypothesis Testing | V | Core | 18 |
| M16 | Correlation and Regression | VI | Core | 18 |
| M17 | ANOVA, Chi-Square and Nonparametric Statistics | VII | Advanced | 16 |
| M18 | Bayesian Statistics and Statistical Methods for Data Science | VIII | Advanced | 18 |

| Part | Modules | Title | Hours |
|---|---|---|---|
| I | M01–M04 | Foundations: orientation, mathematics, data, visualisation | 44 |
| II | M05–M07 | Probability: counting, axioms, conditioning, Bayes | 38 |
| III | M08–M11 | Random variables: distributions, expectation, joint laws | 58 |
| IV | M12–M13 | Sampling and limits: sampling distributions, LLN, CLT | 26 |
| V | M14–M15 | Inference: estimation, intervals, testing | 34 |
| VI | M16 | Relationships: correlation, regression, diagnostics | 18 |
| VII | M17 | Comparative inference: ANOVA, chi-square, nonparametrics | 16 |
| VIII | M18 | Modern statistics: Bayesian, Monte Carlo, practice, capstone | 18 |

> Every module is published in full: an overview and a complete chapter with
> derivations, worked examples, three-level exercise sets with solutions, a quiz and a
> revision summary. The [course roadmap](docs/roadmap.md) is the honest inventory.

## How each module is built

Every module follows the same structure, so you always know where you are:

1. **Learning objectives** — what you must be able to do, stated as actions.
2. **Prerequisites** — the exact earlier sections to review first.
3. **Conceptual explanation** — the idea in plain language before any algebra.
4. **Notation and derivations** — full, line-by-line mathematics.
5. **Intuition** — a second, informal explanation, usually visual or physical.
6. **Worked examples** — complete numerical solutions, not sketches.
7. **Real-world applications** — where the idea appears in data science practice.
8. **Visual explanations** — diagrams, plots and comparison tables that carry the
   argument, each with a caption explaining what to look at.
9. **Python demonstration** — runnable code that reproduces the mathematics, then
   extends it to a case you cannot do by hand.
10. **Exercises** — graded ★ (recall), ★★ (application), ★★★ (challenge).
11. **Self-assessment quiz** — with answers and explanations.
12. **Summary and revision sheet** — the module on one page.

## How to study this course

Self-study works when it is deliberate. Use this protocol for every module:

1. **Skim first (10 min).** Read the objectives and summary. You are building a
   frame, not learning details yet.
2. **Read the concept, not the equations (20 min).** Stop before the algebra and
   say the idea out loud in your own words.
3. **Derive with a pencil (30 min).** Re-derive each result yourself, covering the
   page. If you get stuck, the derivation is written for exactly that moment.
4. **Run the code (20 min).** Type it, do not paste it. Change one parameter and
   predict the output before running.
5. **Do the exercises (45 min).** Start at ★, move up. Attempt before reading
   solutions — a solution you read without trying teaches almost nothing.
6. **Quiz yourself (10 min).** Aim for 8/10. Below that, return to step 3.
7. **Write a five-line summary** in your own words, without looking. This is the
   step students skip and the one that makes the course stick.

**On using solutions.** Solutions are complete on purpose. Use them to check your
reasoning, never to replace it: read the first line only, then try again. A
module is finished when you can reproduce its main result on a blank page and
explain why it is true.

## Study calendar

### Two-semester sequence (recommended)

| Semester | Weeks | Modules | Hours | Focus |
|---|---|---|---|---|
| 1 | 1–16 | M01–M12 | 154 | Foundations, probability, random variables, sampling |
| 2 | 1–16 | M13–M18 | 98 | Limit theorems, inference, modelling, Bayesian, capstone |

### One-semester core track

If your programme allows only one semester, study M01–M08, M12 and M14–M15
(≈146 hours), and treat M09–M11, M13 and M16–M18 as a follow-on reading list.

| Weeks | Modules |
|---|---|
| 1–3 | M01, M02 |
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

This course is graded by you, for you. The weighting below mirrors how the
material would be assessed in a taught programme, so that your self-marking is
comparable.

| Component | Weight | What it measures |
|---|---|---|
| Module quizzes (18 × short) | 15% | recall and conceptual grip |
| Exercise sets (selected ★★/★★★) | 25% | derivation and problem solving |
| Python practicals | 20% | computation, simulation, reproducibility |
| Projects (3, see below) | 25% | end-to-end analysis and communication |
| Capstone (in Module 18) | 15% | independent statistical investigation |

**Projects.**

- **Project 1 — Describing a real dataset** (after M04): clean, summarise
  and visualise a dataset, and defend every summary statistic you chose.
- **Project 2 — Probability by simulation** (after M13): answer a
  probability question three ways — analytically, by exact enumeration, and by
  Monte Carlo — and reconcile the answers.
- **Project 3 — An inference study** (after M16): design and run a
  hypothesis test or interval estimate on real data, with a full assumption audit.

## What you need

- **Mathematics:** intermediate algebra and the idea of a derivative and an
  integral. Module 02 rebuilds sets, functions, summation notation, limits,
  differentiation, integration and series from scratch, so a rusty background is
  not a barrier.
- **A computer** running Windows, macOS or Linux with Python and Jupyter. All
  demonstrations use free, open-source libraries — no licences, no subscriptions.
- **A notebook and a pencil.** Derivations are meant to be reproduced by hand.

## Frequently asked questions

**Do I need to know calculus?** You need to be comfortable with the *idea* of a
derivative and an integral. Module 02 supplies the working technique, and every
calculus step in later modules is shown explicitly.

**Do I need to be good at programming?** No. Code appears as a way to *test*
mathematics, and every line is explained. Beginners should type the examples;
experienced programmers can read them and move to the exercises.

**Is this course enough for machine learning?** It gives you the statistical
foundation that machine learning assumes: distributions, expectation, estimation,
inference, regression and simulation. It deliberately does not teach ML
algorithms; it teaches the reasoning those algorithms are built on.

**Why are there so many derivations?** Because a formula you cannot derive is a
formula you cannot trust, debug, or adapt. Derivations are the difference between
using statistics and understanding it.

**Can I use this course for a taught class?** Yes. The module structure maps onto
a 16-week semester, and the assessment scheme can be adopted directly.

**Are the datasets real?** Yes — small, curated, openly licensed datasets are used
so that every result can be reproduced offline.

## Academic integrity

Work through the exercises yourself before opening a solution. If you use this
material in your own teaching or writing, cite it (see below). Copying solutions
into an assessed submission is misconduct in every programme, and it also defeats
the only purpose this course has.

## Licence and attribution

Course text, figures and exercises: **Creative Commons Attribution–NonCommercial–
ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.
Code and notebooks: **MIT Licence**.
Third-party datasets retain their original licences, credited where used.

When you cite this course:

> Majeed, M. N. (2026). *Probability and Statistics for Data Science*.
> Department of Data Science (PUCIT), University of the Punjab, Lahore.

## Contact

**Engr. Dr. Muhammad Nadeem Majeed**
Professor, Department of Data Science (PUCIT)
University of the Punjab, Lahore

Corrections and suggestions are welcome through the repository's issue tracker.

---

*Repository status: the 18-module framework and site architecture are complete;
full chapter content is in preparation.*
