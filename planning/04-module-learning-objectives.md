# 04 — Module Learning Objectives

> **Superseded document.** These objectives were written for the *30-module draft*.
> The approved curriculum is **18 modules / 252 hours**
> ([11 — Module Framework](11-module-framework.md)), and each approved module's
> learning objectives are now published at the top of its student-facing page in
> `docs/modules/`. Use this document for the misconception analysis and the "results
> the module must establish" lists, which remain accurate; do not use its numbering.

For each module: prerequisites, measurable objectives, the results the module must
establish, its Python/data component, what is assessed, and the misconceptions the
prose must pre-empt.

Objectives are written as observable actions, so that a student can self-mark
against them ("I can derive…", "I can decide…") and so that content authors cannot
drift from the intended standard. Every module inherits the twelve-section anatomy
and the ★/★★/★★★ exercise ladder defined in
[07 — Design Specification](07-design-specification.md).

---

## Part I — Foundations

### Module 01 — Mathematical Foundations for Statistics

**Prerequisites:** none (intermediate algebra assumed).

**Objectives.** By the end of this module you can:
1. Use set notation and operations (union, intersection, complement, difference, Cartesian product, power set) and read set-builder notation fluently.
2. Recognise and construct functions; compute domain, range, inverse and composition; distinguish injective, surjective and bijective maps.
3. Read and manipulate summation and product notation, including double sums, index changes and the constant and linearity rules.
4. Evaluate limits and use continuity; compute derivatives with the product, quotient and chain rules; interpret a derivative as a rate.
5. Compute definite and indefinite integrals, use substitution and integration by parts, and interpret an integral as area.
6. Recognise arithmetic and geometric series, sum them, and state the geometric series condition for convergence.
7. Work confidently with exponents, logarithms, factorials and binomial coefficients.

**Core results.** Linearity of Σ; geometric series Σr^k = 1/(1−r) for |r| < 1; d/dx e^x, ln x, x^n; ∫x^n dx; log rules; factorial growth and Stirling's approximation (stated).

**Python and data.** Symbolic checking with `sympy` (differentiate, integrate, sum, simplify) so that hand-work can be verified; plotting y = f(x) and reading slope and area off the figure.

**Assessment.** Diagnostic self-test (20 items) plus ★ computational drills. Mastery threshold: 80%, because every later module uses this material.

**Misconceptions to pre-empt.** "Σ means add a few terms" (it is an operator with rules); "dx is decoration" (it sets the variable of integration); "a function and its formula are the same thing" (a function is a rule with a domain).

---

### Module 02 — Data and Statistical Thinking

**Prerequisites:** Module 01.

**Objectives.** By the end of this module you can:
1. Distinguish population, sample, parameter, statistic, estimator and estimate, and state which symbol belongs to which.
2. Classify variables by measurement scale (nominal, ordinal, interval, ratio) and by structure (discrete/continuous, quantitative/categorical) and say what each classification permits.
3. Explain the purpose of sampling and identify the four common sampling schemes in outline (SRS, stratified, cluster, systematic), deferring theory to Module 15.
4. Distinguish observational study from experiment, and explain confounding, randomisation, blinding and the placebo effect.
5. Recognise the main sources of bias — selection, survivorship, response, measurement, non-response — and describe how each corrupts an estimate.
6. Apply the tidy-data principles (one row per observation, one column per variable, one table per unit of analysis) to reshape a messy table.

**Core results.** The fundamental distinction *statistic ≠ parameter*; the idea of sampling variability (demonstrated, not yet formalised); the causal hierarchy (association → temporal order → mechanism → counterfactual).

**Python and data.** `pandas` loading, dtypes, `.info()`, `.describe()`, tidy reshaping with `melt`/`pivot`; a deliberately messy CSV is cleaned twice (badly, then well) to show the difference.

**Assessment.** ★ classification drills; ★★ "what is the population here?" case studies; ★★ a written critique of a published statistic.

**Misconceptions to pre-empt.** "A big sample is a good sample" (representativeness beats size); "correlation needs no design" (design determines what a correlation can mean); "ordinal numbers can be averaged" (they generally cannot without justification).

---

### Module 03 — Descriptive Statistics

**Prerequisites:** Modules 01–02.

**Objectives.** By the end of this module you can:
1. Compute and interpret mean, median, mode, and the five-number summary, and explain when each is the appropriate centre.
2. Compute range, interquartile range, variance, standard deviation and coefficient of variation, and explain why the sample variance uses n − 1.
3. Define and interpret z-scores, percentiles and quantiles; compute them by hand and with software.
4. Describe the shape of a distribution using skewness and kurtosis, and relate mean–median ordering to skew.
5. Detect outliers by the 1.5×IQR rule and by z-scores, and argue for or against removal in a given case.
6. Explain robustness and demonstrate it: which summaries survive a single extreme value and which do not.
7. Recognise Simpson's paradox in a two-way table and explain why aggregation changed the conclusion.

**Core results.** Σ(xᵢ − x̄) = 0; s² = Σ(xᵢ − x̄)²/(n − 1); the computational form s² = (Σxᵢ² − nx̄²)/(n − 1); linearity of the mean and the effect of linear transformation on s; Chebyshev's inequality preview.

**Python and data.** `pandas` `agg`, `quantile`, `describe`; `numpy` `mean/median/std(ddof=1)`; hand-computation versus `scipy.stats` agreement checked to the last digit; a short simulation showing n − 1 removing bias in s².

**Assessment.** ★ hand computation on a 10-value dataset; ★★ comparison of two distributions with equal means and different spread; ★★ Simpson's paradox reconstruction.

**Misconceptions to pre-empt.** "Standard deviation has the same units problem as variance" (it does not — that is why it exists); "the mean is the middle value"; "an outlier is an error" (it is a signal to investigate).

---

### Module 04 — Data Visualization and Exploratory Analysis

**Prerequisites:** Modules 01–03.

**Objectives.** By the end of this module you can:
1. Match a plot to a variable type and a question: bar, dot, histogram, density, box, violin, ECDF, scatter, line, heatmap, mosaic, Q–Q.
2. Construct and interpret a histogram, explaining the role of bin width and why the shape of a distribution can be an artefact of it.
3. Read a box plot correctly, including what it does *not* show (bimodality, sample size, exact tails).
4. Produce scatter plots and small multiples; identify trend, spread, clusters and outliers by eye before fitting anything.
5. Apply the principles of graphical integrity: no truncated axes without cause, no 3-D pie charts, no dual axes without explicit labels, proportionally sized encodings, colour that is colour-blind safe.
6. Perform a structured EDA: univariate → bivariate → multivariate → anomalies → hypotheses, and record findings as a narrative.
7. Write figure captions that state what to look at, not merely what the figure is.

**Core results.** Anscombe's quartet (four datasets, identical summary statistics, different structure); the grammar-of-graphics mapping (data → aesthetic → geom → scale → facet); the ECDF as the honest continuous analogue of a histogram.

**Python and data.** `matplotlib` object API (figure/axes), `seaborn` (`histplot`, `boxplot`, `scatterplot`, `pairplot`), optional `plotly` for one interactive figure; saving publication-quality SVG/PNG with fixed DPI, and a deliberate "bad chart vs good chart" pair.

**Assessment.** Project 1 (describing a real dataset) is released here; ★ plot-identification drills; ★★ rebuild a misleading published chart honestly.

**Misconceptions to pre-empt.** "More ink means more information"; "a density plot is always better than a histogram"; "EDA is optional before modelling".

---

## Part II — Probability Foundations

### Module 05 — Counting and Combinatorics

**Prerequisites:** Module 01 (factorials, summation).

**Objectives.** By the end of this module you can:
1. Apply the multiplication rule and construct tree diagrams for multi-stage processes.
2. Count arrangements with and without repetition: n!, nPr, n^r.
3. Count selections: binomial coefficients, and explain why order does and does not matter in a stated problem.
4. Count permutations of multisets and distribute identical objects into distinct boxes (stars and bars).
5. Apply the inclusion–exclusion principle for two and three sets, and derive |A ∪ B|.
6. Use the pigeonhole principle in simple arguments.
7. Count via complement and via conditioning, and choose the cheaper route deliberately.
8. Compute exact probabilities for equally likely outcomes and verify them by exhaustive enumeration in Python.

**Core results.** C(n,k) = n!/(k!(n−k)!); Vandermonde's identity; stars and bars C(n+k−1, k−1); |A∪B∪C| expansion; birthday-problem computation (n = 23 → P ≈ 0.507).

**Python and data.** `math.comb`, `itertools.permutations/combinations/product`, exhaustive enumeration of a small sample space compared with the closed form; a timing experiment showing why enumeration dies at scale (motivating Module 28).

**Assessment.** ★ direct counting; ★★ "which counting rule applies and why"; ★★★ a combinatorial identity proof and a simulation check.

**Misconceptions to pre-empt.** "Probability problems are about the formula" (they are about defining the sample space); double counting; treating distinguishable objects as identical.

---

### Module 06 — Axioms of Probability and Set Theory

**Prerequisites:** Modules 01, 05.

**Objectives.** By the end of this module you can:
1. Define sample space, event, and the algebra of events, and translate a word problem into set notation.
2. State Kolmogorov's three axioms and derive the standard consequences: P(∅) = 0, complement rule, monotonicity, addition rule, inclusion–exclusion for n events.
3. Compute probabilities under the classical, frequentist and subjective interpretations, and say which is being used.
4. Use the continuity property of probability for increasing and decreasing sequences of events.
5. Apply combinatorial counting inside the axiomatic framework to solve classical problems (dice, cards, occupancy).
6. Explain why not every subset needs to be an event (mention of σ-algebras without measure theory).

**Core results.** Axioms 1–3; P(Aᶜ) = 1 − P(A); P(A∪B) = P(A) + P(B) − P(A∩B); Boole's inequality; continuity from below.

**Python and data.** Simulating the axioms: verify P(A∪B) empirically over 10⁵ trials and watch the estimate approach the axiom's value; a small "random experiment" harness reused in later modules.

**Assessment.** ★ axiom consequences; ★★ proof that P(A) ≤ P(B) when A ⊆ B; ★★ occupancy problems; quiz on interpretation.

**Misconceptions to pre-empt.** "Probability is always a long-run frequency" (that is one interpretation); "mutually exclusive means independent" (the opposite, for non-null events); believing P(A∪B) = P(A) + P(B) always.

---

### Module 07 — Conditional Probability and Independence

**Prerequisites:** Module 06.

**Objectives.** By the end of this module you can:
1. Define conditional probability and justify it as a re-normalised measure on a reduced sample space.
2. Apply the multiplication rule to chains of events (P(A∩B∩C) = P(A)P(B|A)P(C|A∩B)).
3. Use the law of total probability with a partition, and draw the corresponding tree diagram.
4. Test and use independence; extend it to mutual independence of n events, and distinguish pairwise from mutual independence with a counterexample.
5. Explain conditional independence and why it differs from independence (with a concrete example where one holds and the other fails).
6. Solve the Monty Hall problem both by conditioning and by simulation, and explain the intuition failure.
7. Recognise when a conditional probability has been inverted in an argument (the prosecutor's fallacy).

**Core results.** P(A|B) = P(A∩B)/P(B); total probability; Bayes' theorem (forward reference to M08); independence criteria; pairwise ≠ mutual independence.

**Python and data.** Full enumeration and 10⁵-trial simulation of Monty Hall; a two-child problem variant; verifying total probability partitions numerically.

**Assessment.** ★ conditional computation from a two-way table; ★★ tree-diagram problems; ★★★ construct a set of three events pairwise independent but not mutually independent.

**Misconceptions to pre-empt.** "P(A|B) = P(B|A)" (the inversion error, revisited in M08); "independent events cannot be disjoint"; "conditioning on B halves the sample space" (only for equally likely outcomes).

---

### Module 08 — Bayes' Theorem and Bayesian Reasoning

**Prerequisites:** Modules 06–07.

**Objectives.** By the end of this module you can:
1. Derive Bayes' theorem from the definition of conditional probability and the law of total probability.
2. Identify prior, likelihood, marginal likelihood (evidence) and posterior in a stated problem.
3. Use the odds form: posterior odds = prior odds × likelihood ratio.
4. Solve diagnostic-testing problems and quantify the base-rate fallacy (sensitivity 99%, specificity 99%, prevalence 0.1% → PPV ≈ 9%).
5. Update beliefs sequentially and show that the order of evidence does not change the final posterior.
6. Explain how naive Bayes classification follows from the theorem plus a conditional-independence assumption, and why it works despite that assumption being false.
7. Update a Beta prior with Bernoulli data to obtain a Beta posterior (bridge to Module 27).

**Core results.** Bayes' theorem in probability and odds form; the base-rate result; sequential updating; Beta–Bernoulli conjugacy.

**Python and data.** A `bayes_update` function applied to spam filtering and to a medical screening scenario; a sensitivity/specificity/PPV grid plotted as a heat map; simulation check of the PPV.

**Assessment.** ★ posterior from a contingency table; ★★ full diagnostic-testing analysis with a recommendation; ★★★ a written explanation of the base-rate fallacy for a non-specialist.

**Misconceptions to pre-empt.** "A 99% accurate test means a 99% chance of disease"; "priors are subjective therefore useless" (they are explicit, and the data can dominate); ignoring the evidence term.

---

## Part III — Random Variables and Distributions

### Module 09 — Random Variables and Their Distributions

**Prerequisites:** Modules 06–08.

**Objectives.** By the end of this module you can:
1. Define a random variable as a measurable function from the sample space to ℝ, and distinguish discrete from continuous.
2. State the properties of a PMF and verify that a candidate function qualifies.
3. State the properties of a PDF, explain why P(X = x) = 0 for continuous X, and compute probabilities as integrals.
4. Define the CDF, derive it from the PMF/PDF, and use it to compute interval probabilities; state its four properties.
5. Recover the PMF/PDF from the CDF by differencing or differentiation.
6. Derive the distribution of a transformed variable Y = g(X) by the CDF method, and use the Jacobian formula for monotone g.
7. Compute and use indicator variables, and express counting quantities as sums of indicators.

**Core results.** F(x) = P(X ≤ x) is non-decreasing, right-continuous, with limits 0 and 1; f = F′; P(a < X ≤ b) = F(b) − F(a); transformation by CDF method and by Jacobian; E[I_A] = P(A) (preview of M13).

**Python and data.** Plot PMF/PDF against CDF for the same variable; verify F(b) − F(a) equals the integral numerically; simulate a transformation (e.g. Y = X²) and compare empirical and derived densities.

**Assessment.** ★ validate a PMF/PDF; ★★ CDF → density → probability chain; ★★★ derive the density of a non-monotone transformation.

**Misconceptions to pre-empt.** "f(x) is a probability" (it is a density; it can exceed 1); "F is the integral of the data"; confusing the density's height with likelihood of a value.

---

### Module 10 — Discrete Probability Distributions

**Prerequisites:** Modules 05, 09.

**Objectives.** By the end of this module you can:
1. Specify and use the Bernoulli, binomial, geometric, negative binomial, hypergeometric, discrete uniform, Poisson and multinomial distributions: PMF, parameters, mean, variance, and the situation each models.
2. Decide, for a described experiment, which family applies — by asking about trials, independence, replacement, and whether the count is of successes, trials or arrivals.
3. Derive the binomial mean and variance using indicator variables.
4. Derive the Poisson PMF as a limit of the binomial, and state the Poisson process assumptions; model inter-arrival times as exponential (forward reference to M11).
5. Use the memorylessness property of the geometric distribution and explain what it does and does not imply.
6. Compute binomial and Poisson probabilities, including tails, and choose between exact computation and a normal approximation (forward reference to M17).
7. Simulate each family and check that empirical mean and variance match theory.

**Core results.** Binomial mean np and variance np(1−p) via indicators; geometric mean 1/p; Poisson mean = variance = λ; hypergeometric variance with the finite-population correction (N−n)/(N−1); Poisson limit of binomial.

**Python and data.** `scipy.stats.binom/poisson/geom/hypergeom` (pmf, cdf, ppf, rvs); a "which distribution?" decision table turned into code; a call-centre arrival simulation.

**Assessment.** ★ PMF computations; ★★ model-selection case studies; ★★★ prove Var(X) = np(1−p) with indicators and verify by simulation.

**Misconceptions to pre-empt.** "Binomial requires a fixed number of trials — so counting patients until the third recovery is binomial" (it is negative binomial); "Poisson needs a time unit" (it needs a rate and an interval); treating without-replacement sampling as binomial.

---

### Module 11 — Continuous Probability Distributions

**Prerequisites:** Modules 09–10.

**Objectives.** By the end of this module you can:
1. Specify and use the uniform, exponential, gamma, beta, normal, lognormal and Weibull distributions: PDF, parameters, mean, variance, support and typical application.
2. Derive the exponential density from its CDF and prove memorylessness; contrast it with the geometric case.
3. Work with the normal distribution: standardise, use the z-table and software for both directions, and compute probabilities for arbitrary intervals.
4. Explain the role of the normal as a reference distribution and the empirical 68–95–99.7 rule.
5. Transform normal variables linearly (aX + b) and state the result.
6. Model positive, right-skewed quantities with the lognormal and explain why exponentiating a normal yields it.
7. Use Q–Q plots to assess normality, and state the limitations of that assessment.
8. Choose between exponential, gamma and Weibull for lifetime data and justify the choice.

**Core results.** Exponential mean 1/λ and memorylessness; gamma as a sum of exponentials; normal density and standardisation; lognormal mean exp(μ + σ²/2); beta as a distribution on [0,1] (bridge to M27).

**Python and data.** `scipy.stats.norm/expon/gamma/beta/lognorm`; z-table versus `norm.cdf` cross-check; Q–Q plots for normal and non-normal samples; fitting a distribution to real inter-arrival data.

**Assessment.** ★ standardisation drills; ★★ lifetime modelling with a justified family; ★★★ prove memorylessness and show the geometric analogue.

**Misconceptions to pre-empt.** "The normal distribution fits everything" (it has support on ℝ and is symmetric); "Q–Q looks straight therefore normal" (small samples mislead); "λ is the mean of an exponential" (it is the rate; mean is 1/λ).

---

### Module 12 — Joint and Multivariate Distributions

**Prerequisites:** Modules 09–11.

**Objectives.** By the end of this module you can:
1. Describe a bivariate distribution by its joint PMF/PDF and joint CDF, and verify the normalisation condition.
2. Compute marginal distributions from a joint distribution by summing or integrating out the other variable.
3. Compute conditional distributions and conditional expectations from a joint distribution.
4. Test independence from the factorisation f(x,y) = f_X(x) f_Y(y) and from the support's shape.
5. Apply the bivariate transformation technique (Jacobian) and derive the distribution of a sum via convolution.
6. Derive the distribution of the maximum and minimum of n independent variables from the CDF.
7. Recognise the multivariate normal, state that linear combinations of its components are normal, and explain the role of the covariance matrix.
8. Use the mixture idea to explain how a joint distribution can show dependence with zero correlation.

**Core results.** Marginals by summation/integration; conditional density f(y|x) = f(x,y)/f_X(x); convolution for sums; order-statistic CDFs F_max = F^n, F_min = 1 − (1−F)^n; independence ⇏ zero correlation and zero correlation ⇏ independence (except jointly normal).

**Python and data.** Bivariate normal sampling with `numpy.random.multivariate_normal`; a 2-D histogram and contour plot; simulation of sums of uniforms converging to a triangular-then-normal shape; a mixture with zero correlation plotted.

**Assessment.** ★ marginals from a table; ★★ conditional expectation from a joint density; ★★★ convolution derivation plus simulation; ★★★ order statistics.

**Misconceptions to pre-empt.** "Marginals determine the joint" (they do not); "uncorrelated means independent"; forgetting the support when integrating.

---

### Module 13 — Expectation, Moments and Generating Functions

**Prerequisites:** Modules 09–12.

**Objectives.** By the end of this module you can:
1. Define expectation for discrete and continuous variables and compute it from the definition.
2. Use the law of the unconscious statistician to compute E[g(X)] without deriving the distribution of g(X).
3. Prove and use linearity of expectation, including for dependent variables, and use indicators to compute expected counts.
4. Define raw and central moments, and compute them for the standard families.
5. Define the moment generating function, derive MGFs for the main families, and use them to identify distributions and to find moments.
6. Prove that the MGF of a sum of independent variables is the product of MGFs, and use this to establish the distribution of sums.
7. Apply Markov's inequality, Chebyshev's inequality and Jensen's inequality, and explain what each buys and costs.

**Core results.** E[aX + b] = aE[X] + b; E[X+Y] = E[X] + E[Y] always; E[XY] = E[X]E[Y] under independence; MGF uniqueness; Markov, Chebyshev, Jensen.

**Python and data.** Numerical integration (`scipy.integrate.quad`) versus closed-form expectation; Monte Carlo estimation of E[g(X)] for a g with no closed form; empirical verification of Jensen's inequality on a convex g.

**Assessment.** ★ expectation from a PMF/PDF; ★★ indicator-variable expectations (expected number of fixed points, coupons); ★★★ MGF of a sum and Chebyshev proof; quiz on inequality conditions.

**Misconceptions to pre-empt.** "Linearity needs independence" (it does not); "E[1/X] = 1/E[X]"; "MGF always exists" (it may not).

---

### Module 14 — Variance, Covariance and Correlation

**Prerequisites:** Module 13.

**Objectives.** By the end of this module you can:
1. Define variance and derive Var(X) = E[X²] − (E[X])².
2. Use the variance rules: Var(aX + b) = a²Var(X); Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y).
3. Define covariance, compute it from the definition and from the shortcut formula, and interpret its sign.
4. Prove the Cauchy–Schwarz inequality and use it to show |ρ| ≤ 1.
5. Define the correlation coefficient, state that it measures linear association only, and construct a counterexample with strong dependence and ρ ≈ 0.
6. Compute the variance of a sum of n variables under independence and under dependence, and use indicators to derive binomial variance.
7. Define conditional expectation and conditional variance, and state and use the tower property (law of total expectation) and the law of total variance.
8. Apply variance-stabilising and standardisation transformations correctly.

**Core results.** Var(aX+b) = a²Var(X); Cov bilinearity; ρ = Cov/(σ_X σ_Y); Var(ΣXᵢ) with covariance terms; E[X] = E[E[X|Y]]; Var(X) = E[Var(X|Y)] + Var(E[X|Y]).

**Python and data.** Computing covariance matrices with `numpy.cov` and `pandas.cov`; the correlation counterexample plotted (Y = X² with X symmetric); simulation confirming the law of total variance.

**Assessment.** ★ variance algebra; ★★ portfolio-style variance of a weighted sum with correlation; ★★★ prove the law of total variance; ★★★ construct a zero-correlation dependent pair.

**Misconceptions to pre-empt.** "Var(X+Y) = Var(X)+Var(Y)" without independence; "covariance magnitude is interpretable" (it is scale-dependent); "ρ = 0 means no relationship".

---

## Part IV — Sampling and Limit Theorems

### Module 15 — Sampling and Sampling Distributions

**Prerequisites:** Modules 03, 11, 13–14.

**Objectives.** By the end of this module you can:
1. Define a random sample as i.i.d. variables and distinguish it from a convenience sample.
2. Derive E[X̄] = μ and Var(X̄) = σ²/n, and state the standard error of the mean.
3. Explain what a sampling distribution is and demonstrate it by repeated sampling from a known population.
4. Derive the sampling distribution of the mean for normal populations, and state when it is exactly normal.
5. Derive and use the chi-square distribution of (n−1)s²/σ², and the t distribution of (X̄−μ)/(s/√n).
6. State the F distribution as a ratio of scaled chi-squares and identify where it arises (bridge to M24).
7. Compute the finite-population correction and explain when it matters.
8. Explain the difference between the standard deviation of the data and the standard error of an estimate, with a demonstration that halving the error costs quadrupling the sample.

**Core results.** X̄ ~ N(μ, σ²/n) for normal data; (n−1)s²/σ² ~ χ²_{n−1}; t = (X̄−μ)/(s/√n) ~ t_{n−1}; F = (S₁²/σ₁²)/(S₂²/σ₂²); SE ∝ 1/√n.

**Python and data.** The "sampling distribution machine": draw B = 10,000 samples of size n from a skewed population, plot the histogram of x̄ for three values of n; overlay the theoretical SE; repeat for s².

**Assessment.** ★ SE computation; ★★ derive E[X̄] and Var(X̄) under i.i.d. sampling; ★★★ show the t statistic's distribution by simulation and compare tails with normal.

**Misconceptions to pre-empt.** "The standard error is the standard deviation of the sample"; "the sampling distribution is the data's distribution" (the central confusion this module exists to remove); "a bigger sample makes the population normal".

---

### Module 16 — Law of Large Numbers and Convergence

**Prerequisites:** Modules 13–15.

**Objectives.** By the end of this module you can:
1. State the weak law of large numbers and prove it for finite variance using Chebyshev's inequality.
2. Distinguish convergence in probability, almost sure convergence, convergence in distribution and convergence in mean square, and give an example separating two of them.
3. Explain what the strong law adds to the weak law, and why the distinction matters in simulation.
4. State the delta method and use it to find the asymptotic distribution of a smooth function of an estimator.
5. Explain the practical meaning of "the average converges" — including that it says nothing about a single outcome, and nothing about the distribution's shape.
6. Demonstrate the law computationally, including a heavy-tailed case (Cauchy) where the sample mean does not converge.

**Core results.** WLLN by Chebyshev; SLLN (stated); convergence in probability ⇒ convergence in distribution; delta method: √n(g(X̄) − g(μ)) → N(0, g′(μ)²σ²); Cauchy mean does not converge.

**Python and data.** Running-mean plots for normal and Cauchy samples (the second never settles); convergence-in-distribution demo (t_n → normal); delta-method variance check by simulation.

**Assessment.** ★ identify the mode of convergence in stated examples; ★★ Chebyshev proof of the WLLN; ★★★ Cauchy counterexample explained; ★ delta-method computation.

**Misconceptions to pre-empt.** "The LLN says the sample must look like the population as n grows" (it says the average does); "convergence in distribution means the variables converge"; that all convergence modes are interchangeable.

---

### Module 17 — Central Limit Theorem

**Prerequisites:** Modules 13–16.

**Objectives.** By the end of this module you can:
1. State the classical CLT precisely, including the standardisation and the i.i.d. and finite-variance conditions.
2. Prove the CLT for the case where the MGF exists, using the MGF of a sum and a Taylor expansion.
3. Compute approximate probabilities for sums and means, with continuity correction for discrete variables.
4. Judge when the normal approximation is adequate, using simulation across parent distributions and sample sizes (uniform, exponential, Bernoulli with small p, heavy-tailed).
5. Explain the role of skewness in the required sample size, and give the practical rule of thumb with its caveats.
6. Apply the CLT to proportions and derive the standard error of a proportion.
7. Explain why the CLT is the reason so much of classical inference works, and name at least two situations where it fails.
8. State the Lyapunov/Lindeberg idea for non-identically-distributed terms (without proof) and give an application to measurement error.

**Core results.** √n(X̄ − μ)/σ → N(0,1); CLT for sums and for proportions; continuity correction; the delta method link; failure under infinite variance or extreme dependence.

**Python and data.** A simulation grid: 4 parent distributions × 4 sample sizes × 2,000 replications, with Q–Q plots against normal; the proportion approximation checked against exact binomial; a heavy-tailed failure demonstration.

**Assessment.** Project 2 (probability by simulation) is submitted here; ★ approximation with continuity correction; ★★ determine the n needed for a stated accuracy; ★★★ MGF proof of the CLT.

**Misconceptions to pre-empt.** "The data become normal as n grows" (the *mean* does); "n > 30 is always enough"; applying the CLT to a single observation.

---

## Part V — Statistical Inference

### Module 18 — Point Estimation

**Prerequisites:** Modules 15–17.

**Objectives.** By the end of this module you can:
1. Define an estimator, an estimate and a statistic, and distinguish an estimator's distribution from its realised value.
2. Derive method-of-moments estimators for standard models and explain when the method fails.
3. Derive maximum likelihood estimators from first principles: likelihood, log-likelihood, score, stationary point, second-derivative check.
4. Compute the MLE for Bernoulli, binomial, Poisson, exponential, normal and uniform models, including the uniform case where the derivative method fails.
5. Evaluate estimators by bias, variance, mean squared error, consistency and efficiency; derive the bias–variance decomposition of MSE.
6. State the Cramér–Rao lower bound and the Fisher information, and check whether an estimator attains it.
7. Define sufficiency and use the factorisation criterion; state the Rao–Blackwell idea.
8. Use the invariance property of MLEs and explain the bias of a transformed estimator.

**Core results.** MSE = bias² + variance; Var(θ̂) ≥ 1/(nI(θ)); MLE invariance; x̄ and s² as MLEs for the normal; the plug-in principle.

**Python and data.** Numerical maximisation of a log-likelihood with `scipy.optimize.minimize` and comparison with the closed form; a bias/variance simulation across sample sizes for two competing estimators; Fisher information computed symbolically with `sympy`.

**Assessment.** ★ method-of-moments derivations; ★★ full MLE derivation with second-order condition; ★★★ show an estimator is unbiased and consistent; ★★★ Cramér–Rao check.

**Misconceptions to pre-empt.** "MLE is unbiased" (it is not, in general); "the estimate is the parameter"; "unbiased is always better" (MSE can favour a biased estimator — bridge to M27 shrinkage).

---

### Module 19 — Confidence Intervals

**Prerequisites:** Modules 15, 17–18.

**Objectives.** By the end of this module you can:
1. Explain the frequentist meaning of 95% coverage, and state precisely what the interval does *not* mean.
2. Construct intervals by the pivotal-quantity method and derive the z-interval for a mean with known variance.
3. Derive the t-interval for a mean with unknown variance, and explain why the t distribution is used.
4. Construct intervals for a proportion (Wald and Wilson), for a variance (chi-square), and for the difference of two means (pooled and Welch).
5. Determine the sample size required for a target margin of error, and explain the quadratic cost.
6. Explain the relationship between a confidence interval and a two-sided hypothesis test, and demonstrate the duality.
7. Construct bootstrap percentile and BCa intervals and state when they are preferable.
8. Choose between intervals on the basis of design, sample size and distributional assumptions, and report them with correct interpretation.

**Core results.** x̄ ± z_{α/2} σ/√n; x̄ ± t_{α/2,n−1} s/√n; Wilson interval for p; (n−1)s²/χ² bounds for σ²; n = (zσ/E)²; duality with tests.

**Python and data.** `scipy.stats.norm.interval`, `t.interval`, `chi2.interval`; hand-built intervals compared with `statsmodels` `DescrStatsW.tconfint_mean`; coverage simulation showing ~95% of 10,000 intervals contain μ; bootstrap CI for a median.

**Assessment.** ★ interval construction; ★★ coverage simulation with a written interpretation; ★★ sample-size calculation; ★★★ explain why a Wald interval fails for small p.

**Misconceptions to pre-empt.** "95% probability the parameter is in this interval" (the parameter is fixed); "a wider interval is worse" (it may be more honest); "the interval covers 95% of the data".

---

### Module 20 — Hypothesis Testing

**Prerequisites:** Modules 17–19.

**Objectives.** By the end of this module you can:
1. Formulate H₀ and H₁ for a research question, and distinguish one- and two-sided alternatives.
2. Define Type I error, Type II error, significance level, and power, and compute β and power for a given design.
3. Conduct one-sample z and t tests, two-sample (pooled and Welch) tests, and paired tests, choosing correctly between them.
4. Compute and interpret a p-value correctly, and state the four things it is not.
5. Derive the rejection region from the test statistic's distribution and show its equivalence to a p-value rule.
6. Determine the sample size for a target power, and explain the power–sample size–effect size triangle.
7. Interpret and report effect sizes (Cohen's d, relative risk, odds ratio) alongside significance.
8. Explain multiple-comparison inflation and apply Bonferroni and Benjamini–Hochberg corrections.
9. Explain p-hacking, optional stopping and publication bias, and identify them in a published claim.
10. Distinguish statistical from practical significance, and state the role of equivalence testing.

**Core results.** p-value = P(data at least this extreme | H₀); power = 1 − β; n ∝ (z_{α/2} + z_β)²σ²/Δ²; test–interval duality; family-wise error under m tests; BH FDR control.

**Python and data.** `scipy.stats.ttest_1samp/ttest_ind/ttest_rel` and `statsmodels` power functions; a power curve plotted against n; a simulation of 20 null tests showing false positives and the effect of correction.

**Assessment.** ★ test selection from a scenario; ★★ full test with assumptions, statistic, p-value, effect size and conclusion; ★★★ power analysis for a stated design; ★★★ written critique of a p-hacking example.

**Misconceptions to pre-empt.** "p is the probability H₀ is true"; "p > 0.05 proves no effect"; "significant means important"; "power is irrelevant once the result is significant".

---

## Part VI — Relationships and Modelling

### Module 21 — Correlation and Association

**Prerequisites:** Modules 04, 14, 20.

**Objectives.** By the end of this module you can:
1. Compute and interpret Pearson's r, including its relationship to the regression slope and R².
2. Test H₀: ρ = 0 and construct a confidence interval via Fisher's z-transformation.
3. Compute Spearman's ρ and Kendall's τ, and state when rank correlation is the appropriate measure.
4. Choose a measure of association for every variable-type pair: Pearson (num–num), point-biserial, phi, Cramér's V, rank-biserial, and explain the choice.
5. Construct and interpret a correlation matrix and a correlogram, including the danger of reading many correlations.
6. Explain why correlation does not imply causation, using confounding, reverse causation and selection, and name the design that would establish causation.
7. Identify and explain Simpson's paradox in continuous data, and demonstrate the ecological fallacy.

**Core results.** r = Cov/(s_x s_y); r² as explained variance; Fisher z = artanh r with SE 1/√(n−3); rank measures invariant to monotone transforms; |r| sensitive to outliers and nonlinearity.

**Python and data.** `pandas.DataFrame.corr(method=...)`, `scipy.stats.pearsonr/spearmanr/kendalltau`, `seaborn.heatmap`; a demonstration that one outlier can move r from 0.1 to 0.9; Anscombe-style quartet revisited.

**Assessment.** ★ compute and interpret r; ★★ choose and justify an association measure for four scenarios; ★★★ confounding analysis written for a non-specialist.

**Misconceptions to pre-empt.** "r = 0.8 means 80% causation"; "r measures any relationship" (linear only); comparing r across groups with different ranges.

---

### Module 22 — Simple Linear Regression

**Prerequisites:** Modules 14, 19–21.

**Objectives.** By the end of this module you can:
1. Specify the simple linear model Y = β₀ + β₁x + ε with its assumptions, and distinguish the model from the fitted line.
2. Derive the least-squares estimators β̂₀ and β̂₁ by minimising the residual sum of squares.
3. Interpret β̂₁ as a unit change in the mean response, and β̂₀ correctly (including when it is meaningless).
4. Compute and interpret R², the residual standard error, and the F statistic for the model.
5. Construct confidence intervals for β₁ and prediction intervals for a new observation, and explain why the prediction interval is much wider.
6. Test H₀: β₁ = 0 and relate the t test to the F test and to the correlation test.
7. Check the four assumptions with residual plots, a Q–Q plot, and a scale–location plot; distinguish patterns and name the remedy.
8. Identify influential points with leverage, Cook's distance and DFBETAS, and decide whether to keep or remove them.
9. Explain extrapolation risk and the difference between interpolation and prediction.

**Core results.** β̂₁ = S_xy/S_xx; β̂₀ = ȳ − β̂₁x̄; R² = 1 − SSE/SST; σ̂² = SSE/(n−2); Var(β̂₁) = σ²/S_xx; prediction interval vs confidence band.

**Python and data.** `statsmodels.formula.api.ols` with a full `.summary()` read line by line; `scipy.stats.linregress`; residual diagnostics with `seaborn.residplot`; a leverage demonstration on a single high-leverage point.

**Assessment.** ★ derive the normal equations; ★★ complete analysis of a dataset with diagnostics and a written limitation; ★★★ show R² is the square of r in simple regression.

**Misconceptions to pre-empt.** "High R² means the model is right"; "β̂₀ is always interpretable"; "residuals should look normal, not random" (randomness matters most); ignoring heteroscedasticity.

---

### Module 23 — Multiple Linear Regression

**Prerequisites:** Module 22.

**Objectives.** By the end of this module you can:
1. Write the multiple regression model in matrix form, and derive the OLS estimator β̂ = (XᵀX)⁻¹Xᵀy.
2. Interpret each coefficient as a partial effect, holding the other predictors constant, and explain why this differs from the simple-regression coefficient.
3. Handle categorical predictors with dummy coding, and interpret the reference category and interaction terms.
4. Diagnose and address multicollinearity with correlation matrices and VIF, and explain its effect on coefficient variance (not on predictions).
5. Check all assumptions: linearity, independence, homoscedasticity, normality of errors, and no influential outliers; name a remedy for each failure.
6. Recognise heteroscedasticity and apply a transformation or robust standard errors.
7. Compare nested models with partial F tests, and compare non-nested models with AIC/BIC and adjusted R².
8. Apply model-building discipline: state the question, pre-specify predictors, avoid data-dredging, validate on held-out data.
9. Explain why adding predictors always raises R² and why adjusted R² exists.

**Core results.** β̂ = (XᵀX)⁻¹Xᵀy; Var(β̂) = σ²(XᵀX)⁻¹; VIF = 1/(1−R²_j); partial F test; AIC = −2ℓ + 2k; the omitted-variable and included-irrelevant-variable bias directions.

**Python and data.** `statsmodels` with `C()` categoricals and `:` interactions; VIF via `variance_inflation_factor`; `sklearn` for the held-out comparison (explicitly contrasting inference and prediction goals); residual and influence plots.

**Assessment.** ★ matrix derivation; ★★ full model build with diagnostics, VIF and a justified final model; ★★★ explain a sign reversal between simple and multiple regression.

**Misconceptions to pre-empt.** "Coefficients are causal effects" (only under a design that supports it); "drop variables to fix multicollinearity" (it changes the question); "more predictors is a better model".

---

## Part VII — Comparative and Categorical Inference

### Module 24 — Analysis of Variance

**Prerequisites:** Modules 19–20, 22–23.

**Objectives.** By the end of this module you can:
1. State the one-way ANOVA model and its assumptions, and identify the hypotheses it tests.
2. Decompose total sum of squares into between- and within-group components, and derive the F statistic from the mean squares.
3. Explain why ANOVA and the pooled two-sample t test agree when k = 2, and prove the F = t² relationship.
4. Interpret the ANOVA table (df, SS, MS, F, p) line by line.
5. Run post-hoc comparisons (Tukey HSD) after a significant F, and explain why uncorrected pairwise tests are invalid.
6. Report and interpret effect size (η², ω², Cohen's f), and explain why a significant F with tiny η² is not interesting.
7. Check ANOVA assumptions and choose remedies: Welch ANOVA for unequal variances, transformation or rank-based tests for non-normality.
8. Analyse a two-way design, interpret main effects in the presence of an interaction, and explain why main effects can mislead when interaction is present.
9. Describe a repeated-measures design and why independence fails there.

**Core results.** SST = SSB + SSW; MSB/MSW ~ F_{k−1, N−k}; F = t² for k = 2; η² = SSB/SST; Tukey's studentised range; interaction as a non-additive model term.

**Python and data.** `scipy.stats.f_oneway`, `statsmodels` `ols` + `anova_lm`, `pingouin` for Welch ANOVA and Tukey; interaction plots; a variance-decomposition bar chart.

**Assessment.** ★ complete an ANOVA table from partial information; ★★ full one-way analysis with post-hoc and effect size; ★★★ two-way analysis with interaction interpretation; ★★★ explain F = t².

**Misconceptions to pre-empt.** "ANOVA tells you which groups differ" (it does not); "run t tests instead, it is the same" (multiplicity); "a non-significant F means all means are equal" (it means insufficient evidence).

---

### Module 25 — Chi-Square Tests

**Prerequisites:** Modules 20, 24.

**Objectives.** By the end of this module you can:
1. Conduct a goodness-of-fit test for a specified distribution, computing expected counts and the test statistic.
2. Conduct a test of independence in an r × c contingency table, and compute expected counts under H₀.
3. Conduct a test of homogeneity across populations, and explain how it differs from independence in design though not in computation.
4. State and check the expected-count condition (≥ 5), and apply a remedy: category collapsing, exact tests, or a permutation test.
5. Compute and interpret Cramér's V and the odds ratio as effect sizes.
6. Use Fisher's exact test for 2 × 2 tables and McNemar's test for paired binary data.
7. Explain why the chi-square statistic has an approximate chi-square distribution with (r−1)(c−1) df, and count df correctly.
8. Identify the common misuse of chi-square on ordered categories and on paired data.

**Core results.** χ² = Σ(O−E)²/E; df = (r−1)(c−1) for independence, k−1 for goodness of fit (minus estimated parameters); Cramér's V = √(χ²/(n·min(r−1,c−1))); McNemar's statistic.

**Python and data.** `scipy.stats.chisquare`, `chi2_contingency`, `fisher_exact`, `statsmodels.stats.contingency_tables` for McNemar and table summaries; a simulation showing the χ² approximation degrading with small expected counts.

**Assessment.** ★ compute χ² and df by hand; ★★ independence analysis with effect size and a stated limitation; ★★★ choose between independence, homogeneity and goodness of fit for three designs.

**Misconceptions to pre-empt.** "χ² tests association strength" (it tests presence, and grows with n); using chi-square on paired data; df errors; ignoring small expected counts.

---

### Module 26 — Nonparametric Statistics

**Prerequisites:** Modules 20, 24–25.

**Objectives.** By the end of this module you can:
1. Explain what "distribution-free" means, and identify the assumption each parametric alternative makes that a rank test avoids.
2. Conduct the sign test and the Wilcoxon signed-rank test for one sample or paired data, and state the hypotheses they actually test (median / symmetry).
3. Conduct the Mann–Whitney U (Wilcoxon rank-sum) test for two independent samples, and interpret it as a test of stochastic dominance rather than of medians alone.
4. Conduct the Kruskal–Wallis test for k groups, with post-hoc Dunn correction, and Friedman's test for a randomised block design.
5. Use the Kolmogorov–Smirnov and Shapiro–Wilk tests appropriately, and explain why a normality test is not a substitute for judgement.
6. Construct a permutation test for any statistic, and state the exchangeability assumption it requires.
7. Construct bootstrap confidence intervals and explain when the bootstrap fails (extreme order statistics, small n, dependent data).
8. Choose between a parametric, rank-based and resampling method for a stated dataset, and justify the choice in writing.

**Core results.** Signed-rank statistic distribution; U statistic as a count of pairwise orderings; efficiency loss of rank tests under normality (≈ 0.955 for Wilcoxon vs t); permutation p-value = (1 + #{T* ≥ T})/(B + 1); bootstrap standard error.

**Python and data.** `scipy.stats.wilcoxon/mannwhitneyu/kruskal/friedmanchisquare/ks_1samp`; `pingouin` for Dunn and effect sizes; a hand-written `permutation_test` and `bootstrap_ci` (the reusable toolkit, Appendix E).

**Assessment.** ★ select the correct rank test; ★★ full nonparametric analysis with effect size and interpretation; ★★★ implement a permutation test from scratch and compare with the parametric result; ★★ bootstrap vs t-interval comparison under skew.

**Misconceptions to pre-empt.** "Nonparametric means assumption-free" (exchangeability, independence and similar shapes still matter); "Mann–Whitney tests medians"; "nonparametric is always safer" (power loss when assumptions hold).

---

## Part VIII — Modern and Applied Statistics

### Module 27 — Bayesian Statistics

**Prerequisites:** Modules 08, 18–20.

**Objectives.** By the end of this module you can:
1. State the Bayesian inferential framework and contrast it with the frequentist framework in terms of what is random, what is fixed, and what a probability statement means.
2. Specify a prior, likelihood and posterior for a problem, and derive the posterior for the Beta–Bernoulli, Gamma–Poisson and Normal–Normal conjugate families.
3. Interpret the posterior mean, median and mode, and explain shrinkage toward the prior.
4. Construct and interpret a credible interval, and state the difference from a confidence interval without caricature.
5. Choose an informative, weakly informative or non-informative prior, and conduct a sensitivity analysis.
6. Compare models with marginal likelihood and Bayes factors, and state the limitations of Bayes factors.
7. Explain why most posteriors are analytically intractable, and describe how MCMC samples from them; diagnose convergence with trace plots, R̂ and effective sample size.
8. Build and fit a simple Bayesian model with PyMC, and report the posterior with uncertainty.
9. State the strengths and costs of the Bayesian approach, and choose it or frequentist inference for a stated problem with reasons.

**Core results.** posterior ∝ prior × likelihood; Beta(a,b) + Binomial → Beta(a+x, b+n−x); Normal–Normal updating precision addition; posterior predictive distribution; R̂ ≈ 1 criterion.

**Python and data.** Closed-form conjugate updates computed by hand and plotted; the same model fitted in `pymc` with `pm.sample`; prior-sensitivity plots; posterior predictive checks.

**Assessment.** ★ derive a conjugate posterior; ★★ full Bayesian analysis with prior justification and sensitivity; ★★★ written comparison of the two paradigms on one dataset; quiz on credible vs confidence intervals.

**Misconceptions to pre-empt.** "Bayesian means subjective therefore arbitrary"; "the credible interval and confidence interval are the same number so they mean the same thing"; "a flat prior is no prior"; ignoring convergence diagnostics.

---

### Module 28 — Monte Carlo Simulation and Computational Statistics

**Prerequisites:** Modules 05, 15–17, 26.

**Objectives.** By the end of this module you can:
1. Explain what a pseudo-random number generator is, why seeds matter, and why the modern `Generator` API is preferred.
2. Generate samples by inverse-transform sampling and by rejection sampling, and prove the correctness of each.
3. Estimate integrals and expectations by Monte Carlo, and quantify the error as O(1/√B) with an estimated standard error.
4. Apply variance reduction: antithetic variates, control variates, stratified sampling, importance sampling.
5. Estimate a probability that is too small or too complex for enumeration, and report a confidence interval for the estimate.
6. Use simulation to verify a theoretical result, and design the simulation so that disagreement is diagnostic rather than mysterious.
7. Use simulation-based power analysis to plan a study.
8. Implement the bootstrap and a permutation test for an arbitrary statistic, and explain the resampling principle behind each.
9. State the failure modes: dependence, insufficient replications, unseeded runs, and treating a simulated p-value of 0 as evidence of impossibility.

**Core results.** Inverse transform: X = F⁻¹(U); rejection sampling acceptance probability; MC error σ/√B; antithetic variance reduction; bootstrap consistency for smooth statistics; (1 + k)/(B + 1) p-value rule.

**Python and data.** Hand-written samplers (exponential, normal via Box–Muller, rejection for a Beta) checked against `scipy.stats`; MC integration of a difficult integral; an importance-sampling example for a rare event; a power simulation for a t test.

**Assessment.** ★ inverse-transform derivation and implementation; ★★ rare-event estimation with error bars; ★★★ design a simulation study whose result would falsify a claim; ★★ bootstrap versus analytic SE comparison.

**Misconceptions to pre-empt.** "More simulations always fix a wrong estimator"; "a simulated probability of 0 means impossible"; using the same seed across conditions and calling it independent; ignoring Monte Carlo error when comparing groups.

---

### Module 29 — Statistics for Data Science Practice

**Prerequisites:** Modules 18–28.

**Objectives.** By the end of this module you can:
1. Design an A/B test: define the metric, the unit of randomisation, the minimum detectable effect, the sample size and the stopping rule, before looking at data.
2. Analyse an experiment correctly, including guardrail metrics, sequential-testing hazards, and multiple metrics.
3. Explain common inferential failure modes in analytics: peeking, metric drift, novelty effects, network interference, survivor bias and data leakage.
4. Apply cross-validation correctly for model assessment, and distinguish it from hypothesis testing.
5. Explain how regularisation (ridge, lasso) is a bias–variance trade-off, and connect it to the Bayesian shrinkage of Module 27.
6. Evaluate a classifier with the right metric (accuracy, precision/recall, ROC–AUC, calibration) and explain why accuracy alone misleads on imbalanced data.
7. Recognise statistical-validity threats in deployed systems: distribution shift, feedback loops, proxy variables and fairness across groups.
8. Write a statistical analysis plan and a reproducible report: question, data provenance, methods, diagnostics, limitations, decision.
9. State the ethical obligations of statistical work: honest reporting, transparency about multiplicity, privacy and the consequences of error.

**Core results.** Sample size for a two-proportion test; the sequential-testing inflation problem; k-fold CV bias–variance behaviour; ridge as a constrained least-squares problem; base-rate effects on precision; calibration curves.

**Python and data.** Sample-size calculation with `statsmodels.stats.power`; a simulated A/B test with a peeking demonstration; `sklearn` `cross_val_score`, `RidgeCV`, `roc_auc_score`, `calibration_curve`; a leakage example (scaling before splitting) that inflates performance.

**Assessment.** ★ design an experiment for a described product question; ★★ full A/B analysis with a decision recommendation; ★★★ audit a pipeline for leakage and validity threats; written ethics case analysis.

**Misconceptions to pre-empt.** "A significant A/B result is a shippable result"; "cross-validation estimates p-values"; "accuracy is the metric"; "more data removes bias".

---

### Module 30 — Capstone Project

**Prerequisites:** Modules 01–29.

**Objectives.** By the end of this module you can:
1. Formulate a statistical question that is answerable with available data, and justify why it matters.
2. Write an analysis plan before touching the data, including the primary method, the assumptions it needs, and the fallback if they fail.
3. Acquire, document and clean data with full provenance, and defend every exclusion.
4. Apply at least two appropriate methods, compare them, and explain any disagreement.
5. Conduct a complete assumption audit, with evidence and remedies, not assertions.
6. Quantify uncertainty for every estimate and effect size you report.
7. Produce a reproducible artefact: one command rebuilds every number and figure from raw data.
8. Write a report for a non-specialist reader that separates what the data show from what you infer, and states the limitations honestly.
9. Defend the work in a structured self-review: the three strongest objections and your answers to them.

**Core results.** Integration of the whole course; no new theory.

**Python and data.** A full project: `docs/projects/capstone/` with `analysis.ipynb`, `src/`, `data/`, `report.md`, `requirements.txt` and a `Makefile`-style single entry point.

**Assessment.** Capstone rubric (see [02 — Curriculum](02-curriculum.md) §9), weighted to independence: 20 marks design, 20 method, 20 diagnostics, 20 reproducibility, 20 communication.

**Misconceptions to pre-empt.** That a capstone is a long homework exercise; that a null result is a failed project (a well-evidenced null is a result); that a beautiful report compensates for an unexamined assumption.
