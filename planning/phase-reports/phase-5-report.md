# Phase 5 report — chapters M13–M18

**Scope.** Write the six remaining full chapters (M13–M18), nest them in the navigation,
extend the numeric validator to cover them, and validate the complete website.

**Status.** Complete. All eighteen modules now have a framework overview and a full
chapter. Nothing was committed, pushed or published.

## 1. What was written

| Module | Chapter file | Lines | Words | Exercises | Self-assessment items |
|---|---|---|---|---|---|
| M13 | `docs/modules/13-law-of-large-numbers-and-clt/chapter.md` | 477 | 3,149 | 8 | 10 |
| M14 | `docs/modules/14-estimation-and-confidence-intervals/chapter.md` | 510 | 2,982 | 9 | 10 |
| M15 | `docs/modules/15-hypothesis-testing/chapter.md` | 528 | 3,279 | 9 | 10 |
| M16 | `docs/modules/16-correlation-and-regression/chapter.md` | 482 | 2,968 | 8 | 10 |
| M17 | `docs/modules/17-anova-chi-square-nonparametric/chapter.md` | 492 | 3,136 | 8 | 10 |
| M18 | `docs/modules/18-bayesian-and-data-science-methods/chapter.md` | 529 | 3,552 | 9 | 10 |

Topic coverage, as required:

- **M13** — weak law with the Chebyshev proof, strong law, modes of convergence, the CLT
  with an MGF argument and Berry–Esseen remainder, sampling distributions, the delta
  method, continuity correction, simulation-based understanding, the Cauchy
  counter-example, practical consequences.
- **M14** — point and interval estimation, unbiasedness, consistency, efficiency,
  bias–variance–MSE decomposition, MLE (exponential, Bernoulli, normal), Cramér–Rao,
  sufficiency, z/t/proportion/two-sample intervals, Wilson vs Wald, sample size, coverage
  interpretation, common mistakes.
- **M15** — hypotheses, \(\alpha\), Type I/II, power and its four-way trade-off, sample
  size and power curves, p-values correctly defined **and explicitly distinguished from
  \(\Pr(H_0\mid\text{data})\)** (with the Bayes argument and a table of common false
  statements), one/two-tailed tests, z, one-sample, two-sample (Welch), paired,
  proportion tests, assumptions, multiplicity (Bonferroni, Benjamini–Hochberg, forking
  paths).
- **M16** — covariance, Pearson, inference on \(r\), Spearman, least squares derived by
  differentiation, \(R^{2}\) decomposition, slope inference, confidence bands vs
  prediction intervals, multiple regression, adjusted \(R^{2}\), dummies, interactions,
  VIF, residual diagnostics, and a full section on **why correlation does not establish
  causation** (confounding, reverse causation, selection, and what would justify a causal
  claim).
- **M17** — one-way ANOVA with the variance decomposition, post-hoc Tukey, two-way ANOVA
  and interactions, \(F\), chi-square goodness of fit / independence / homogeneity,
  effect sizes (Cramér's \(V\), odds ratio), Mann–Whitney, Wilcoxon signed-rank,
  Kruskal–Wallis, permutation and bootstrap previews, a test-selection table.
- **M18** — Bayesian inference, priors, likelihood, conjugate updating
  (Beta–Bernoulli, Gamma–Poisson, Normal–Normal), credible vs confidence intervals,
  Bayes factors, MLE vs Bayesian estimation, bootstrap, permutation tests, Monte Carlo
  error, A/B testing with peeking and MDE, uncertainty in machine learning, calibration,
  cross-validation, conformal prediction, assumptions and limitations.

All chapters follow the established structure (idea → why → terminology → principles →
derivations → worked examples → mistakes → data-science connections → real-world
scenarios → visual explanations → three-level exercises → full solutions →
self-assessment → revision summary). Interpretations accompany every computation.

## 2. Navigation and site metadata

- `mkdocs.yml`: M15–M18 converted from flat entries to `Overview:`/`Chapter:` pairs, so
  all eighteen modules now nest identically.
- `docs/roadmap.md`: "Chapters M01–M12" row replaced with an eighteen-chapter row
  (all links), the "Twelve of the eighteen modules" paragraph replaced with an accurate
  statement, the release table updated to **Available** for M13–M18, and the
  "what complete means" paragraph corrected.
- Corrected two roadmap links whose paths did not match the real chapter directories
  (`08-random-variables-and-expectation`, `12-sampling-and-sampling-distributions`).

## 3. Validator

`tools/check_examples.py` extended from 318 to **506** assertions, covering M13–M18:
Chebyshev and CLT probabilities, continuity correction, delta method; z/t/proportion and
two-sample intervals, Wilson vs Wald, sample size, MLE identities, MSE decompositions;
test statistics and p-values for every M15 example; least squares, residuals,
\(R^{2}\), adjusted \(R^{2}\), VIF, prediction intervals; ANOVA tables, Tukey HSD,
all three chi-square procedures, rank statistics; conjugate posteriors, shrinkage
weights, bootstrap/permutation/Monte Carlo standard errors, and a fixed-seed simulation
of the optional-stopping inflation (five looks, 20,000 paths → 0.139, consistent with
the "about 14%" claim in the text).

Two validator defects were found and fixed:

1. `chi2_cdf` crashed for \(\nu=1\) (integrable singularity at 0). Now uses exact
   identities for \(\nu=1\) and \(\nu=2\) and Simpson integration only above that.
2. Several expected values were recorded at insufficient precision and tripped
   tolerances; all were recomputed independently and the tolerances tightened rather
   than loosened.

## 4. Defects found in the prose and fixed

| Where | Defect | Fix |
|---|---|---|
| M14 §8.3 | Wilson interval formula had \(1+z^{2}\) in the denominator instead of \(1+z^{2}/n\), so the worked check gave \([0,0.04]\) instead of \([0,0.161]\) | Formula corrected; the stated interval now reproduces exactly |
| M14 headings | Duplicate section number (`9.1` then `9.1b`) | Renumbered 9.2, 9.3 |
| M15 §9.2 | Benjamini–Hochberg paragraph contained a self-contradictory mid-paragraph correction about Bonferroni rejecting one or two hypotheses | Rewritten to state that both procedures reject two here and explain why the example does not separate them |
| M15 Example 7.2 | \(p\approx0.451\); recomputation gives 0.4495 | Corrected to \(p\approx0.450\) |
| `docs/roadmap.md` | Two chapter links pointed at non-existent paths | Corrected (also caught by the strict build) |

## 5. Validation results

Run after all edits, on the complete site:

| Check | Command | Result |
|---|---|---|
| Numeric examples | `python tools/check_examples.py` | **exit 0**, 506/506 assertions pass |
| Math delimiters | `python tools/check_math.py` | **exit 0**, 57 Markdown files, balanced, no stray `$` |
| Assets | `python tools/check_assets.py` | **exit 0**, all references resolve, sizes within budget |
| Relative links | inline script over `docs/**/*.md` | **0 broken** |
| Strict build | `.venv-docs/Scripts/python.exe -m mkdocs build --strict` | **exit 0**, 0 warnings |

Totals across the eighteen chapters: 10,234 lines, 63,687 words, 114 worked examples,
154 exercises each with a full solution, and 180 self-assessment items.

## 6. Known limitations (unchanged or newly explicit)

- The lab catalogue lists simulators for M13–M18 (LLN, p-values, power, regression,
  ANOVA, bootstrap, permutation, A/B). Only the CLT and CI-coverage labs are built; the
  rest remain specified, not implemented, and are labelled as planned on the roadmap.
- No Jupyter notebooks; chapters use Mermaid, tables and ASCII schematics, as decided in
  Phase 1.
- Exercise banks are 8–9 per chapter, not the larger sets a printed textbook would carry.
- Projects, glossary, formula sheet and statistical tables are still outstanding.
- Visual checks are limited to the strict build and link checking: the rendered pages
  have not been inspected in a browser in this phase.

## 7. Academic integrity notes

- Every numeric claim in M13–M18 is recomputed by the validator from first principles;
  no value was copied from an external source.
- No fabricated data, citations or references were introduced. Worked examples use
  explicitly constructed datasets and say so.
- Statistical wording is deliberate: tests conclude "reject"/"fail to reject", intervals
  are reported with their assumptions, and the two required cautions (correlation is not
  causation; a p-value is not the probability that \(H_0\) is true) are stated,
  justified, and used consistently in later chapters.
