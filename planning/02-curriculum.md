# 02 — Curriculum

**Probability and Statistics for Data Science**
BS Data Science · Department of Data Science (PUCIT), University of the Punjab

30 modules · 8 parts · 254 module-hours (~270 with orientation and appendices)
Two-semester sequence, with a documented one-semester core track.

> **Superseded document.** This is the *historical 30-module draft*, retained for
> its sequencing rationale, coverage matrix and assessment design. The approved
> curriculum is **18 modules / 252 hours**, recorded in
> [11 — Module Framework](11-module-framework.md) and published to students in
> `docs/modules/`. The mapping from each draft module to its approved home is in §3
> of that document. Do not implement content against the numbering below.

---

## 1. Design principles

Five principles determine the ordering of topics and the shape of every module.
They are stated first because they explain why the curriculum looks the way it
does, and they are the criteria against which any future topic proposal is judged.

**P1 — Reasoning before recipes.** A student who knows why the sample variance
divides by *n − 1* can debug a pipeline; a student who has memorised
`ddof=1` cannot. Every procedure is derived before it is used.

**P2 — Simulation is a proof you can run.** From Module 05 onward, every
theoretical result is accompanied by a simulation that reproduces it. Simulation
serves three purposes: it validates the mathematics, it builds intuition for
variability, and it is the actual working method of modern data science. This is
the single strongest differentiator of a data-science statistics course from a
mathematics-department one.

**P3 — Data first, theory immediately after.** Descriptive statistics and graphics
(Modules 02–04) come before probability, so that every later abstraction has a
concrete referent. Students meet a histogram before a density, a residual plot
before an error term.

**P4 — Recurrence, not repetition.** Key ideas return at higher levels: Bayes
appears as a formula (M08), as a classifier (M29) and as inference (M27);
correlation appears descriptively (M04), algebraically (M14), inferentially (M21)
and as a modelling assumption (M23). Each return adds a layer rather than
repeating a definition.

**P5 — Honest uncertainty.** Interpretation, assumptions and failure modes are
taught with the same seriousness as computation: p-value misuse (M20), the
assumption audit (M22–M26), the limits of the CLT (M17), and the ethics of
statistical claims (M29).

## 2. Outcomes

### Course learning outcomes (CLOs)

| CLO | Statement | Bloom level | Assessed by |
|---|---|---|---|
| CLO1 | Summarise and visualise data appropriately for its type and structure | Apply | Quizzes M02–M04, Project 1 |
| CLO2 | Construct probability models and derive distributional properties from axioms | Apply/Analyse | Exercises M05–M11 |
| CLO3 | Apply conditioning, independence and Bayes' theorem to solve applied problems | Apply | Exercises M07–M08, Project 2 |
| CLO4 | Analyse joint behaviour of variables using expectation, variance and covariance | Analyse | Exercises M12–M14 |
| CLO5 | Explain and apply the Law of Large Numbers and the Central Limit Theorem, including their limits | Understand/Analyse | Quiz M16–M17, Project 2 |
| CLO6 | Derive estimators and evaluate them by bias, variance, consistency and efficiency | Analyse/Evaluate | Exercises M18 |
| CLO7 | Construct and interpret interval estimates and hypothesis tests with correct error control | Apply/Evaluate | Exercises M19–M20, Project 3 |
| CLO8 | Build and diagnose regression, ANOVA and chi-square models on real data | Apply/Evaluate | Exercises M21–M25, Project 3 |
| CLO9 | Select and justify distribution-free, Bayesian or simulation-based methods when assumptions fail | Evaluate | Exercises M26–M28 |
| CLO10 | Conduct and communicate a complete, reproducible statistical investigation | Create | Capstone M30 |

### Mapping to programme outcomes

The course carries the quantitative-reasoning load of a BS Data Science
programme. It supplies the probabilistic foundation for machine learning,
the inferential foundation for research methodology, and the modelling foundation
for regression-based analytics. It does **not** teach machine-learning algorithms;
it teaches the statistical reasoning those algorithms presuppose.

## 3. Course facts

| Item | Value |
|---|---|
| Credit hours (equivalent) | 3 + 3 across two semesters |
| Modules | 30 (+ 5 reference appendices) |
| Module learning hours | 254 (≈10 h/week for 16 weeks in Semester 1; ≈6 h/week plus projects in Semester 2) |
| Assessment | 5 components, criterion-referenced, self-marked |
| Software | Python 3.12/3.13, Jupyter, numpy, pandas, scipy, statsmodels, matplotlib, seaborn, plotly, PyMC (optional) |
| Language of instruction | English |

## 4. The curriculum

### Part I — Foundations (Modules 01–04, 30 h)

*Purpose:* establish the mathematical vocabulary, the data vocabulary and the
descriptive toolkit, so that probability arrives with something to be probable
about. Module 01 exists because a cohort's calculus is genuinely uneven; it
rebuilds sets, functions, summation, limits, differentiation, integration and
series at exactly the depth later modules use — no more.

| # | Module | Level | Hours | The one idea |
|---|---|---|---|---|
| 01 | Mathematical Foundations for Statistics | Beginner | 8 | Statistics is written in the language of sums, integrals and functions; learn the grammar first |
| 02 | Data and Statistical Thinking | Beginner | 6 | A statistic is an answer to a question about a *population*, obtained from a *sample*, and the gap between them is the whole subject |
| 03 | Descriptive Statistics | Beginner | 8 | Every summary is a lossy compression; choose the compression that preserves what matters |
| 04 | Data Visualization and Exploratory Analysis | Beginner | 8 | A good graphic makes the structure of the data visible before any model is fitted |

### Part II — Probability Foundations (Modules 05–08, 30 h)

*Purpose:* build probability as a mathematical model of uncertainty, not as a bag
of formulas. Counting comes first because it makes equally-likely probability
computable by hand, which is the only way the axioms stop feeling arbitrary.

| # | Module | Level | Hours | The one idea |
|---|---|---|---|---|
| 05 | Counting and Combinatorics | Beginner | 6 | Most exact probability is counting done carefully |
| 06 | Axioms of Probability and Set Theory | Core | 8 | Probability is a measure on a set of outcomes, and everything else follows from three axioms |
| 07 | Conditional Probability and Independence | Core | 8 | Information changes probabilities, and independence is a claim about *when it does not* |
| 08 | Bayes' Theorem and Bayesian Reasoning | Core | 8 | Belief is updated by the likelihood of evidence, and the base rate is never optional |

### Part III — Random Variables and Distributions (Modules 09–14, 54 h)

*Purpose:* the technical heart of the course. Random variables turn events into
numbers; distributions describe those numbers; joint distributions describe
several at once; expectation, variance and covariance summarise them. This is
where a student's ability to read a formula as a statement about data is built.

| # | Module | Level | Hours | The one idea |
|---|---|---|---|---|
| 09 | Random Variables and Their Distributions | Core | 8 | A random variable is a function from outcomes to numbers; PMF, PDF and CDF are three views of one object |
| 10 | Discrete Probability Distributions | Core | 10 | A handful of discrete families model most counting-and-arrival phenomena; choosing the family is the modelling act |
| 11 | Continuous Probability Distributions | Core | 10 | For continuous quantities, probability is area, and the normal distribution is the reference scale |
| 12 | Joint and Multivariate Distributions | Advanced | 10 | Two variables are described by their joint law; marginals and conditionals are what you can see and what you learn |
| 13 | Expectation, Moments and Generating Functions | Core | 8 | Expectation is a weighted average, and once you can compute it, distributions become manageable |
| 14 | Variance, Covariance and Correlation | Core | 8 | Variance measures spread, covariance measures shared spread, and correlation rescales it to a pure number |

### Part IV — Sampling and Limit Theorems (Modules 15–17, 22 h)

*Purpose:* the bridge from probability to statistics. Sampling distributions are
the conceptual pivot of the entire course: they explain how a statistic computed
from data can itself be random, which is the question every confidence interval
and test silently depends on.

| # | Module | Level | Hours | The one idea |
|---|---|---|---|---|
| 15 | Sampling and Sampling Distributions | Core | 8 | A statistic is a random variable, and its distribution is what makes inference possible |
| 16 | Law of Large Numbers and Convergence | Advanced | 6 | Averages stabilise; convergence has several distinct meanings that matter in practice |
| 17 | Central Limit Theorem | Core | 8 | Sums of many small independent effects are approximately normal — and knowing when that fails is as important as knowing it holds |

### Part V — Statistical Inference (Modules 18–20, 26 h)

*Purpose:* the three instruments of classical inference — estimation, intervals,
tests — derived rather than asserted, with interpretation and error control given
equal weight to computation.

| # | Module | Level | Hours | The one idea |
|---|---|---|---|---|
| 18 | Point Estimation | Core | 8 | An estimator is a guess with a distribution, and good guesses are judged by bias, variance and consistency |
| 19 | Confidence Intervals | Core | 8 | An interval is a procedure with a long-run coverage guarantee, not a statement of probability about a fixed parameter |
| 20 | Hypothesis Testing | Core | 10 | A test is a decision rule with two error rates, and the p-value is neither of them |

### Part VI — Relationships and Modelling (Modules 21–23, 24 h)

*Purpose:* from association to explanation. Correlation is treated as a measure
first and a warning second; regression is derived by least squares and then
diagnosed, because a regression that has not been checked is a claim, not a
finding.

| # | Module | Level | Hours | The one idea |
|---|---|---|---|---|
| 21 | Correlation and Association | Core | 6 | Correlation is a standardised covariance that measures *linear* association only |
| 22 | Simple Linear Regression | Core | 8 | Least squares is a geometry: the fitted line is the projection of the data onto a plane of predictions |
| 23 | Multiple Linear Regression | Advanced | 10 | Each coefficient is an effect *holding the others constant*, which is what makes multiple regression powerful and fragile |

### Part VII — Comparative and Categorical Inference (Modules 24–26, 22 h)

*Purpose:* the procedures a practising analyst uses most and understands least.
ANOVA is presented as a variance decomposition, chi-square as a comparison of
observed and expected counts, and nonparametrics as the honest answer when
distributional assumptions cannot be defended.

| # | Module | Level | Hours | The one idea |
|---|---|---|---|---|
| 24 | Analysis of Variance (ANOVA) | Core | 8 | Compare means by splitting total variation into what the model explains and what it does not |
| 25 | Chi-Square Tests | Core | 6 | Categorical data is compared through counts, and every chi-square test is one of three closely related procedures |
| 26 | Nonparametric Statistics | Advanced | 8 | When you cannot assume a distribution, use ranks, signs and resampling instead of likelihoods |

### Part VIII — Modern and Applied Statistics (Modules 27–30, 46 h)

*Purpose:* the course turns computational. Bayesian inference is taught as a
coherent alternative paradigm with an honest comparison; Monte Carlo is taught as
a general problem-solving method; Module 29 assembles the toolkit for practice —
A/B testing, experimental design, statistical learning connections, and the
ethical dimension of statistical claims. The capstone requires a complete,
defensible investigation.

| # | Module | Level | Hours | The one idea |
|---|---|---|---|---|
| 27 | Bayesian Statistics | Advanced | 10 | Treat the parameter as uncertain, and inference is just probability done conditionally |
| 28 | Monte Carlo Simulation and Computational Statistics | Advanced | 8 | If you can simulate a process, you can answer questions about it |
| 29 | Statistics for Data Science Practice | Advanced | 8 | Statistics in production is design, diagnostics, multiple comparisons and communication |
| 30 | Capstone Project | Advanced | 20 | A defensible statistical claim, from question to reproducible report |

## 5. Thematic threads

Seven threads recur deliberately. The table shows where each is introduced and
where it is revisited, so that no thread depends on a single exposure.

| Thread | Introduced | Developed | Mastered |
|---|---|---|---|
| **Simulation** | M04 (random plots, seeding) | M05, M07, M10–M12, M16–M17 | M28, M26 (permutation/bootstrap) |
| **Notation discipline** | M01, M02 | M06, M09 | M13–M14, M18 |
| **Inference logic** | M02 (population vs sample) | M15, M17 | M18–M20, M27 |
| **Model diagnostics** | M03 (outliers) | M22 | M23–M26, M29 |
| **Data workflow** | M02 (tidy data) | M04 | M22, M29, M30 |
| **Uncertainty communication** | M03 | M19 | M20, M27, M29 |
| **Ethics and validity** | M02 (study design) | M20 (p-hacking, multiplicity) | M29 (fairness, leakage) |
| **Computation cost** | M05 (enumeration limits) | M28 (Monte Carlo error) | M29 (bootstrap at scale) |

## 6. Coverage matrix

Every topic named in the brief, mapped to its primary module (secondary modules
in brackets).

| Requested topic | Primary | Also |
|---|---|---|
| Mathematical foundations | 01 | 06, 13 |
| Descriptive statistics | 03 | 04 |
| Data visualization | 04 | 22, 29 |
| Counting and combinatorics | 05 | 06, 10 |
| Probability theory | 06 | 07, 09 |
| Conditional probability | 07 | 08 |
| Bayes' theorem | 08 | 27, 29 |
| Random variables | 09 | 10–14 |
| Discrete distributions | 10 | 12, 28 |
| Continuous distributions | 11 | 12, 17 |
| Joint distributions | 12 | 14, 23 |
| Mathematical expectation | 13 | 14, 18 |
| Variance and covariance | 14 | 15, 22 |
| Sampling and sampling distributions | 15 | 17, 18 |
| Law of Large Numbers | 16 | 28 |
| Central Limit Theorem | 17 | 19, 20, 28 |
| Statistical estimation | 18 | 19, 27 |
| Confidence intervals | 19 | 20, 26 |
| Hypothesis testing | 20 | 24, 25, 29 |
| Correlation | 21 | 14, 23 |
| Regression | 22, 23 | 24, 29 |
| ANOVA | 24 | 26, 29 |
| Chi-square tests | 25 | 26 |
| Nonparametric statistics | 26 | 28 |
| Bayesian statistics | 27 | 08, 29 |
| Monte Carlo simulation | 28 | 05, 17, 26 |
| Statistical applications in Data Science | 29 | 30 |

**Additional topics included with justification.**

| Addition | Module | Why it is necessary |
|---|---|---|
| Statistical thinking, study design, data types, ethics | 02 | Without it, "sample" and "population" are words, not concepts; also covers measurement scales that every later method depends on |
| Convergence concepts, delta method | 16 | Needed to state the CLT correctly and to understand why asymptotic tests work |
| Moment and probability generating functions | 13 | The cleanest route to distributions of sums (M12, M17) and to the Poisson process |
| Conditional expectation and variance (tower property) | 14 | Underpins regression (M22), ANOVA decomposition (M24) and Bayesian shrinkage (M27) |
| Multiple regression diagnostics and multicollinearity | 23 | Predictive modelling in data science fails on these, not on the algebra |
| Bootstrap and permutation tests | 26, 28 | The default inferential tools when assumptions fail; ties classical inference to computation |
| Experimental design and A/B testing | 29 | The main industrial use of this course's content |
| Statistical learning connections, leakage, cross-validation | 29 | Connects inference to the ML curriculum that follows |
| Capstone | 30 | Integrates CLO1–CLO10 into one deliverable |

## 7. Two-semester schedule

### Semester 1 — Probability and Inference Foundations (Modules 01–20)

| Week | Modules | Milestone |
|---|---|---|
| 1 | 01 | Diagnostic self-test; maths toolkit |
| 2 | 02, 03 | Project 1 released |
| 3 | 04 | Project 1 submitted; first data report |
| 4 | 05 | — |
| 5 | 06 | — |
| 6 | 07 | — |
| 7 | 08 | Mid-course quiz (M05–M08) |
| 8 | 09 | — |
| 9 | 10 | — |
| 10 | 11 | — |
| 11 | 12, 13 | — |
| 12 | 14, 15 | — |
| 13 | 16, 17 | Project 2 (simulation) submitted |
| 14 | 18 | — |
| 15 | 19 | — |
| 16 | 20 | Semester quiz (M15–M20); revision |

### Semester 2 — Modelling and Modern Statistics (Modules 21–30)

| Week | Modules | Milestone |
|---|---|---|
| 1 | 21 | — |
| 2–3 | 22 | Project 3 released |
| 4–5 | 23 | Project 3 submitted |
| 6–7 | 24 | — |
| 8 | 25 | Mid-course quiz (M21–M25) |
| 9–10 | 26 | — |
| 11–12 | 27 | — |
| 13 | 28 | — |
| 14 | 29 | Capstone brief released |
| 15–16 | 30 | Capstone submitted and defended |

## 8. One-semester core track

For programmes that can allocate a single semester. Total ≈ 150 hours; Modules
12, 16 and 21–27 are deferred to a follow-on reading list, and simulation (28) is
retained because it carries the data-science method.

| Week | Modules |
|---|---|
| 1 | 01 |
| 2 | 02, 03 |
| 3 | 04 |
| 4 | 05 |
| 5 | 06 |
| 6 | 07 |
| 7 | 08 |
| 8 | 09 |
| 9 | 10 |
| 10 | 11 |
| 11 | 13, 14 |
| 12 | 15 |
| 13 | 17 |
| 14 | 18 |
| 15 | 19, 20 |
| 16 | 28, revision |

## 9. Assessment architecture

### Components and weighting

| Component | Weight | Frequency | Marked against |
|---|---|---|---|
| Module quizzes | 15% | 30 (one per module), 10 items each | Model answers with explanations |
| Exercise sets | 25% | Continuous; ★★ and ★★★ items | Worked solutions + marking rubric |
| Python practicals | 20% | 1 notebook per 2 modules | Reproducibility + interpretation rubric |
| Projects | 25% | 3 | Analytic rubric (see below) |
| Capstone | 15% | 1 | Same rubric, weighted to independence |

### CLO coverage

| Component | CLOs |
|---|---|
| Quizzes | 1–9 (recall and conceptual grip) |
| Exercise sets | 2–9 (derivation and problem solving) |
| Practicals | 1, 5, 9, 10 (computation, simulation, reproducibility) |
| Projects 1–3 | 1, 3, 5, 7, 8 |
| Capstone | 1–10 |

### Project rubric (100 marks)

| Criterion | Marks | Descriptor for full marks |
|---|---|---|
| Question and design | 15 | A precise, answerable question; design that could actually answer it |
| Data handling | 15 | Provenance stated, cleaning justified, no silent drops |
| Method choice | 20 | Method matched to data type and design; alternatives considered |
| Assumption audit | 20 | Each assumption stated, checked, and its violation addressed |
| Computation | 15 | Reproducible: seeds, versions, one command to rebuild |
| Interpretation | 10 | Conclusions scoped to the evidence; uncertainty quantified |
| Communication | 5 | Figures self-explanatory; non-specialist can follow the argument |

### Difficulty ladder for exercises

| Level | Marker | Intent | Typical count per module |
|---|---|---|---|
| Recall and check | ★ | Confirm definitions, one-step computation | 4–6 |
| Application | ★★ | Multi-step problems, choose the method | 4–6 |
| Challenge | ★★★ | Proofs, counterexamples, simulation, open-ended | 2–4 |

## 10. Study-hour budget

| Part | Modules | Hours | Share |
|---|---|---|---|
| I Foundations | 01–04 | 30 | 12% |
| II Probability | 05–08 | 30 | 12% |
| III Random variables | 09–14 | 54 | 21% |
| IV Sampling and limits | 15–17 | 22 | 9% |
| V Inference | 18–20 | 26 | 10% |
| VI Relationships | 21–23 | 24 | 9% |
| VII Comparative | 24–26 | 22 | 9% |
| VIII Modern | 27–30 | 46 | 18% |
| **Total** | | **254** | **100%** |

Orientation pages, appendices and revision add ~16 hours → **≈270 hours**.

## 11. Deliberate exclusions

Stated so that scope stays controlled and later additions are argued, not drifted
into:

- **Measure theory.** Axioms are stated rigorously but not in measure-theoretic
  language; σ-algebras are named, not required.
- **Stochastic processes.** Poisson processes appear inside M10 as an
  application; Markov chains and queuing theory do not belong in this course.
- **Machine learning algorithms.** M29 draws the connection; the algorithms
  belong to the ML course that follows.
- **Advanced Bayesian computation.** M27 uses conjugate models and introduces
  MCMC through PyMC; Hamiltonian Monte Carlo internals are out of scope.
- **Survey sampling theory in depth.** M15 covers SRS, stratified, cluster and
  systematic sampling at working depth, not design-based estimation theory.
- **Multivariate methods** (PCA, MANOVA, factor analysis) — flagged as a natural
  successor course.

## 12. Reference appendices

Not modules; consulted throughout and printable.

| Appendix | Purpose |
|---|---|
| A — Statistical Tables | z, t, χ², F tables plus guidance on when a table beats software |
| B — Formula Reference | One-page-per-part formula sheet with conditions of validity |
| C — Glossary | 300+ terms, cross-linked from every module |
| D — Python Reference | Idiomatic pandas/scipy/statsmodels recipes for each procedure |
| E — Simulation Toolkit | Reusable functions: `simulate_mean`, `bootstrap_ci`, `permutation_test`, `power_curve` |

Appendices are also the mechanism that keeps module pages from repeating
boilerplate: a module links to the recipe instead of re-deriving the syntax.
