# Self-assessment and practice examinations

A complete assessment system for the eighteen modules: question banks, five examination
papers, worked answers, and an interactive quiz format that gives immediate feedback. Use it
to find out what you actually know before an examination does it for you.

!!! note "No accounts, no tracking"
    The quizzes run entirely in your browser. Nothing is sent anywhere, nothing is stored,
    and nothing needs to be installed. You can print any page as a practice sheet.

## What is here

| Part | What it contains | How to use it |
|---|---|---|
| **Module banks** (18 pages) | 15+ multiple-choice, 10 short conceptual, 10 numerical, 5 scenario, 3 challenging items per module, all with answers | Work through the bank when you finish a module |
| **Mid-course revision** | Mixed paper on Modules 01–09 | Halfway through the course, closed book |
| **Probability examination** | Modules 05–13, 90 minutes | After Part IV |
| **Statistics examination** | Modules 12–18, 90 minutes | After Part VII |
| **Comprehensive final** | All eighteen modules, 150 minutes | Before the real thing |
| **Data-science assessment** | Integrated problem-solving on messy, applied questions | After the case studies |

Every multiple-choice question is interactive: choose an option, press **Check answer**, and
the correct option, the reason, and the usual trap are shown immediately. With JavaScript
disabled the same page still works — open "Answer and explanation" under each question — and
it prints as a question sheet.

## How the assessment pages are organised

Each module page has the same six sections:

1. **Multiple-choice questions** — 15 items, four options, one correct. These test
   definitions, formula selection and quick interpretation.
2. **Conceptual short questions** — 10 items, answered in two to five sentences. These test
   whether you can explain a result to someone else.
3. **Numerical problems** — 10 items, full working. These test calculation and the ability
   to choose the right formula.
4. **Scenario problems** — 5 items set in a Data Science context. These test modelling
   judgement, not arithmetic.
5. **Challenging analytical problems** — 3 items requiring a derivation, a proof, or a
   comparison of competing methods.
6. **Answer key** — the MCQ answers in one table, for marking a printed attempt.

## Marking yourself

| Score on a section | What it means | What to do next |
|---|---|---|
| 90–100 % | Secure | Move on; revisit only before the exam |
| 70–89 % | Working knowledge | Re-read the chapter section behind each miss |
| 50–69 % | Fragile | Redo the module's notebook and the numerical items |
| below 50 % | Not yet | Return to the chapter, then the foundation notebook |

A useful rule: if you cannot explain *why* an option is wrong, you do not yet own the
concept, even if you chose the right one.

## Suggested study sequence

1. Finish the module chapter, then its [notebook](../practicals/index.md).
2. Take the module bank closed-book; mark it; read every explanation, including the ones you
   got right.
3. Do the [case study](../case-studies/index.md) that uses the same ideas when one exists.
4. At the halfway point, sit the mid-course paper under time pressure.
5. Two weeks before the examination, take the probability or statistics paper depending on
   which half is weaker.
6. In the final week, the comprehensive paper and the data-science assessment.

## Printing

Every page prints cleanly: choose **File → Print** (or `Ctrl/Cmd + P`). The print layout
keeps the questions, drops the buttons and the per-question answers, and keeps the answer-key
table, so one printout gives you a practice sheet and a marking sheet. See
[Printing practice sets](printable.md) for the details and a suggested print plan.

## Module banks

| Module | Bank | Focus |
|---|---|---|
| M01 | [Introduction to probability and statistics](m01.md) | Variables, scales, study design, describing data |
| M02 | [Mathematical foundations](m02.md) | Sets, functions, sums, limits, calculus for statistics |
| M03 | [Data and descriptive statistics](m03.md) | Centre, spread, shape, grouped data, robustness |
| M04 | [Data visualization](m04.md) | Chart choice, encoding, distortion, interpretation |
| M05 | [Counting and combinatorics](m05.md) | Permutations, combinations, multinomial counting |
| M06 | [Probability fundamentals](m06.md) | Axioms, independence, conditional probability |
| M07 | [Conditional probability and Bayes](m07.md) | Bayes, base rates, screening, updating |
| M08 | [Random variables and expectation](m08.md) | PMF, PDF, expectation, variance, transforms |
| M09 | [Discrete distributions](m09.md) | Binomial, Poisson, geometric, negative binomial |
| M10 | [Continuous distributions](m10.md) | Uniform, normal, exponential, gamma, lognormal |
| M11 | [Joint distributions](m11.md) | Joint, marginal, conditional, covariance, correlation |
| M12 | [Sampling and sampling distributions](m12.md) | Sampling variation, standard error, t and chi-square |
| M13 | [LLN and the CLT](m13.md) | Convergence, CLT, normal approximation, simulation |
| M14 | [Estimation and confidence intervals](m14.md) | Estimators, bias, MSE, intervals, sample size |
| M15 | [Hypothesis testing](m15.md) | Errors, power, p-values, tests, multiplicity |
| M16 | [Correlation and regression](m16.md) | Correlation, least squares, inference, diagnostics |
| M17 | [ANOVA, chi-square and nonparametric](m17.md) | ANOVA, chi-square, rank tests, assumptions |
| M18 | [Bayesian statistics and DS methods](m18.md) | Priors, posteriors, credible intervals, model comparison |

## Examination papers

- [Mid-course revision assessment](exams/mid-course.md) — Modules 01–09, 75 minutes.
- [Probability examination](exams/probability.md) — Modules 05–13, 90 minutes.
- [Statistics examination](exams/statistics.md) — Modules 12–18, 90 minutes.
- [Comprehensive final examination](exams/final.md) — all modules, 150 minutes.
- [Integrated data-science problem-solving assessment](exams/data-science.md) — applied,
  open-book, 120 minutes.

## How the questions are checked

Every page is validated by `tools/check_assessments.py`, which confirms the item counts, that
each MCQ has exactly one marked answer and an explanation, that every written item has a
solution, and that no multiple-choice stem is reused across pages. Numerical answers were
computed independently in Python before being written into the solutions; where a question
depends on a table or a simulation, the generating code is stated.
