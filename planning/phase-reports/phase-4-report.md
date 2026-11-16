# Phase 4 report — Chapters M07–M12

**Scope:** conditional probability and Bayes; random variables and expectation; the
discrete and continuous distribution families; joint distributions; sampling
distributions.
**Date:** 14 November 2026
**Status:** Delivered and verified. No commits, pushes or deployments.

---

## 1. Chapters created

| Module | Chapter | Lines | Words |
|---|---|---|---|
| M07 | Conditional Probability and Bayes' Theorem | 635 | 3,798 |
| M08 | Random Variables and Mathematical Expectation | 530 | 2,739 |
| M09 | Discrete Probability Distributions | 528 | 2,977 |
| M10 | Continuous Probability Distributions | 524 | 2,807 |
| M11 | Joint Probability Distributions | 484 | 2,380 |
| M12 | Sampling and Sampling Distributions | 516 | 3,154 |
| **Total** | **6 chapters** | **3,217** | **17,855** |

Site totals now: **12 chapters, 7,216 lines, 44,621 words**.

## 2. Required coverage

| Module | Required element | Where |
|---|---|---|
| M07 | Conditional probability | §4, with die and card examples |
| | Multiplication theorem | §4.2, derived from the definition |
| | Independent and dependent events | §5, including pairwise vs mutual and conditional independence |
| | Total probability theorem | §6, proved by partitioning |
| | Bayes' theorem | §7, plus the odds form |
| | Probability trees | §8, with a Mermaid tree and backward reading |
| | Medical testing | §9, twice-tested patient, prevalence sensitivity |
| | Spam detection | §10, one-word and two-word naive Bayes |
| M08 | Discrete and continuous variables | §4–§5 |
| | PMF, PDF, CDF | §4, §5, including density-is-not-probability |
| | Expected value | §6, with the linearity derivation |
| | Variance, SD | §7, with the shortcut derivation |
| | Moments | §8, raw/central moments and MGFs |
| | Covariance | §9, with bilinearity and \(\Var(X+Y)\) |
| | Transformations | §10, CDF method, linear case, Jacobian formula |
| M09 | Bernoulli, binomial, geometric, negative binomial, hypergeometric, Poisson | §4–§8, each with derivation and worked examples |
| | Distribution selection | §9 decision table + Mermaid decision tree + the four confusions resolved |
| M10 | Uniform, normal, standard normal, exponential, gamma, beta | §4–§8 |
| | z-scores | §9.2, plus the percentile table |
| | Percentiles and probability calculations | §5.3, §9.1, normal approximation with continuity correction |
| M11 | Joint, marginal, conditional distributions | §4–§6, discrete table and continuous density |
| | Independence | §7, with factoring and non-factoring examples |
| | Covariance, correlation | §8, worked both from a table and from a density |
| | Joint expectation | §9, including the law of total variance |
| M12 | Population and sample, sampling methods, random sampling, bias | §4–§5 |
| | Sampling distribution, standard error | §6, derived |
| | Distribution of the mean and of the proportion | §6, §7 |
| | \(t\), \(\chi^{2}\), \(F\) | §8–§10, with the \(F\)/ANOVA connection |

## 3. Worked examples, exercises and quizzes

| Module | Worked examples | Exercises | Solutions | Quiz / self-assessment |
|---|---|---|---|---|
| M07 | 8 | 8 | 8 | 10 |
| M08 | 7 | 9 | 9 | 10 |
| M09 | 6 | 8 | 8 | 10 |
| M10 | 6 | 8 | 8 | 10 |
| M11 | 8 | 8 | 8 | 10 |
| M12 | 5 | 8 | 8 | 10 |
| **Total** | **40** | **49** | **49** | **60** |

Zeros: none. Every exercise has a full solution, and exercise and solution counts match
1:1 in all six chapters.

## 4. Distribution-selection aids

Three tables and two diagrams exist specifically to stop the most common modelling
error — choosing the wrong family:

- **M09 §9:** six-family comparison across "trials fixed", "replacement", "what is
  counted", mean and variance, followed by a Mermaid decision tree and prose
  resolutions of the four genuine confusions (binomial/hypergeometric,
  geometric/negative binomial, binomial/Poisson, binomial/normal).
- **M10 §10:** five-family continuous comparison plus the exponential/Poisson,
  normal/\(t\), gamma/exponential and beta/uniform distinctions.
- **M12 §11:** which sampling distribution applies to which statistic, plus a decision
  tree.

## 5. Validation

| Check | Result |
|---|---|
| `mkdocs build --strict` | **exit 0** |
| `python tools/check_math.py` | **exit 0**, 51 files balanced |
| `python tools/check_assets.py` | **exit 0** |
| internal `.md` links | **0 broken** |
| `python tools/check_examples.py` | **exit 0 — 318 assertions** |

The checker gained numerical machinery to validate the sampling distributions without
SciPy: Simpson-rule integration of the \(\chi^{2}\), \(t\) and \(F\) densities, a
normal CDF via `math.erf`, and quantile checks. Verified values include
\(\Phi(1.96)=0.975002\), \(\chi^{2}_{15}\) upper 5% \(=24.996\), \(t_{9,0.975}=2.262\),
\(F_{15,20}\) upper 2.5% \(\approx2.57\), and the finite-population factors
\(0.8666\) and \(0.9492\). All match the prose.

## 6. Defects found and fixed

| # | Defect | Fix |
|---|---|---|
| D13 | M11 §8.3 first displayed \(\E[XY]=13/36\) and then corrected itself in prose to \(1/3\) | Replaced with the correct two-term derivation (\(\frac16+\frac16=\frac13\)); \(\Cov=-1/144\), \(\rho=-1/11\) verified |
| D14 | Three reference values in the new checker block were wrong (two finite-population factors, one too-tight tolerance) | Checker expectations corrected; the chapters' prose values were already right |
| D15 | M07–M12 labelled worked examples "Worked example — …" and exercises "Problem n", while M01–M06 used "Example n.n" and "Exercise n" | Normalised across the six files; a single regex now counts both cohorts consistently |

## 7. Deliberately not done

- **No figures.** Visual explanations are Mermaid diagrams, tables and ASCII schematics;
  they are text and therefore accessible, but not publication-quality vector art.
- **No notebooks**, no exercise bank beyond the 49 problems, no solutions manual
  separate from the chapters.
- **M13–M18 remain frameworks.** The roadmap was updated to say so.
- **No browser check.** Rendered pages were not viewed; validation is the strict build
  plus the three checkers.
- **No commits, pushes or deployments.**

## 8. Next phase (proposed)

1. M13 (LLN and CLT), completing Part IV.
2. M14–M15 (estimation, testing) to finish Part V.
3. Add the planned interactive labs for M09–M12 (distribution explorer, sampling
   machine, LLN) so the chapters have their companions.
