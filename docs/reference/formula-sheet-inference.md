---
title: Formula sheet — inference and modelling
description: Sampling distributions, the CLT, intervals, hypothesis tests, regression, ANOVA, chi-square, nonparametrics, Bayesian methods and resampling — with assumptions and examples.
---

# Formula sheet — inference and modelling

Part 2 of 2: Modules 12–18. Part 1 covers [descriptive statistics to joint distributions](formula-sheet.md).

Each entry gives the formula, its symbols, its purpose, its assumptions, when to use it, and a
numerical example. The [test selection guide](test-selection.md) turns these into a decision.

!!! tip "Where the \(z\), \(t\), \(\chi^2\) and \(F\) numbers come from"
    Every critical value on this page has a tabled entry in
    [statistical tables](tables/index.md): [standard normal](tables/standard-normal.md),
    [Student's \(t\)](tables/t-distribution.md), [chi-square](tables/chi-square.md) and
    [\(F\)](tables/f-distribution.md). The tables are generated from SciPy, state their
    upper-tail convention, and are re-verified cell by cell before every build — so a
    hand calculation and a Python one should agree to the printed digit.

## 14. Sampling distributions

### 14.1 Standard error of a mean and of a proportion

\[ SE(\bar{x}) = \frac{s}{\sqrt{n}}, \qquad SE(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \]

**Symbols.** \(s\) sample SD; \(\hat p\) sample proportion; \(n\) sample size.
**Purpose.** The spread of an estimator across repeated samples.
**Assumptions.** Independent observations; for a finite population of size \(N\), multiply by
\(\sqrt{(N-n)/(N-1)}\).
**When to use.** Building every interval and test statistic for a mean or a proportion.
**Example.** \(s=10,n=100\): \(SE=1\). \(\hat p=0.2,n=400\): \(SE=\sqrt{0.16/400}=0.02\).

### 14.2 Distribution of the sample variance

\[ \frac{(n-1)s^2}{\sigma^2} \sim \chi^2_{n-1} \quad \text{for normal data} \]

**Symbols.** \(\sigma^2\) population variance; \(\chi^2_{n-1}\) chi-square with \(n-1\) df.
**Purpose.** Inference about a variance, and the reason \(t\) has heavier tails than \(z\).
**Assumptions.** The population must be normal — this is the most fragile assumption in the course.
**When to use.** Variance intervals, variance-ratio tests, checking process variability.
**Example.** \(n=10,s^2=4\): the 95 % interval for \(\sigma^2\) is \((9\cdot4/19.02,\ 9\cdot4/2.70)=(1.89,13.3)\) — wide, because variance is hard to estimate.

## 15. Central Limit Theorem

### 15.1 The theorem

\[ \frac{\bar{X}_n-\mu}{\sigma/\sqrt{n}} \xrightarrow{\ d\ } N(0,1), \qquad \sum_{i=1}^n X_i \approx N(n\mu,\ n\sigma^2) \]

**Symbols.** \(\mu,\sigma^2\) population mean and variance (finite); \(\xrightarrow{d}\) convergence in distribution.
**Purpose.** Justifies normal-based intervals and tests even when the data are not normal.
**Assumptions.** Independent, identically distributed observations with finite variance; \(n\) large enough.
**When to use.** Means and sums from large samples; not for the raw data, and not for extreme quantiles.
**Example.** Exponential data (very skewed) with \(n=50\): the mean is already close to normal; with \(n=5\) it is not.

### 15.2 Continuity correction and the normal approximation to the binomial

\[ P(a \le X \le b) \approx \Phi\!\left(\frac{b+0.5-np}{\sqrt{np(1-p)}}\right) - \Phi\!\left(\frac{a-0.5-np}{\sqrt{np(1-p)}}\right) \]

**Symbols.** \(X\sim\mathrm{Bin}(n,p)\); \(\Phi\) standard normal CDF; \(\pm0.5\) the correction.
**Purpose.** Fast binomial probabilities before computers, and the logic behind proportion tests.
**Assumptions.** \(np\ge5\) and \(n(1-p)\ge5\); the correction helps near the boundary.
**When to use.** Hand calculations; understanding why \(z\)-tests for proportions work.
**Example.** \(n=100,p=0.5\): \(P(X\le 45)\approx\Phi((45.5-50)/5)=\Phi(-0.9)=0.184\) (exact 0.184).

## 16. Confidence intervals

### 16.1 Mean: known and unknown \(\sigma\)

\[ \bar{x} \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}, \qquad \bar{x} \pm t_{1-\alpha/2,\,n-1}\frac{s}{\sqrt{n}} \]

**Symbols.** \(z\) and \(t\) critical values; \(\alpha\) error rate.
**Purpose.** A range of plausible values for \(\mu\) with a stated procedure-level coverage.
**Assumptions.** Random sample; independence; normal population or large \(n\) for the \(t\) form.
**When to use.** Reporting any estimated mean; use \(t\) whenever \(s\) estimates \(\sigma\).
**Example.** \(\bar x=50,s=10,n=25\): \(50\pm2.064(2)=(45.9,54.1)\).

### 16.2 Proportion, and difference of two means

\[ \hat p \pm z_{1-\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}, \qquad (\bar x_1-\bar x_2)\pm t\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}} \]

**Symbols.** Subscripts 1 and 2 denote groups; \(t\) uses Welch's degrees of freedom unless equal variances are assumed.
**Purpose.** Intervals for a rate, and for a comparison between two independent groups.
**Assumptions.** Independent samples; for proportions, at least 5 successes and 5 failures per group; normality or large \(n\) for means.
**When to use.** Conversion rates, A/B tests, two-arm trials.
**Example.** \(\hat p=0.12,n=500\): \(0.12\pm1.96(0.0145)=(0.092,0.148)\).

### 16.3 Paired difference, variance, and sample size

\[ \bar d \pm t_{n-1}\frac{s_d}{\sqrt n}, \qquad \left(\frac{(n-1)s^2}{\chi^2_{1-\alpha/2}},\ \frac{(n-1)s^2}{\chi^2_{\alpha/2}}\right), \qquad n=\left(\frac{z_{\alpha/2}\sigma}{E}\right)^2 \]

**Symbols.** \(d_i\) within-pair differences; \(E\) target margin of error.
**Purpose.** Exploit pairing; quantify uncertainty in a variance; plan a study.
**Assumptions.** Paired analysis needs the pairs, not just the group means; the sample-size formula assumes known \(\sigma\) (use \(t\) and iterate otherwise).
**When to use.** Before/after measurements, matched designs, precision planning.
**Example.** \(E=2,\sigma=10\): \(n=(1.96\cdot10/2)^2=96.04\), so 97.

## 17. Hypothesis testing

### 17.1 One-sample and two-sample statistics

\[ z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}, \qquad t=\frac{\bar x-\mu_0}{s/\sqrt n}, \qquad t=\frac{\bar x_1-\bar x_2}{\sqrt{s_1^2/n_1+s_2^2/n_2}} \]

**Symbols.** \(\mu_0\) hypothesised mean; \(s\) sample SD.
**Purpose.** Measure how far an estimate is from the null, in standard-error units.
**Assumptions.** Random sampling, independence, normality or large \(n\); the \(z\) form needs known \(\sigma\).
**When to use.** Mean comparisons; use the paired \(t\) on differences instead when data are matched.
**Example.** \(\bar x=52,\mu_0=50,s=8,n=36\): \(t=1.5\), \(p=0.14\) two-sided — not distinguishable from 50.

### 17.2 Proportions, and the paired proportion

\[ z=\frac{\hat p-p_0}{\sqrt{p_0(1-p_0)/n}}, \qquad z=\frac{\hat p_1-\hat p_2}{\sqrt{\hat p(1-\hat p)\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}} \]

**Symbols.** \(\hat p\) pooled proportion under \(H_0\).
**Purpose.** Test a rate against a benchmark, or compare two rates.
**Assumptions.** Independent observations; expected counts at least 5 in each cell; the pooled form is for the null of equality.
**When to use.** A/B tests, defect rates, survey proportions.
**Example.** 530/6039 vs 661/5961: \(z=4.24\), \(p\approx2\times10^{-5}\).

### 17.3 Errors, power and effect size

\[ \alpha = P(\text{reject}\mid H_0), \quad \beta = P(\text{fail to reject}\mid H_1), \quad \text{power}=1-\beta, \quad d=\frac{\bar x_1-\bar x_2}{s_p} \]

**Symbols.** \(s_p\) pooled SD; \(d\) Cohen's effect size (0.2 small, 0.5 medium, 0.8 large).
**Purpose.** Separate the two ways of being wrong and quantify an effect independently of \(n\).
**Assumptions.** A specified alternative is needed for power; \(d\) assumes comparable SDs.
**When to use.** Designing a study, interpreting a non-significant result, meta-analysis.
**Example.** \(d=0.5\), two-sided \(\alpha=0.05\), power 0.8: about 64 per group.

## 18. Correlation

### 18.1 Pearson correlation and its test

\[ r=\frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum (x_i-\bar x)^2\sum (y_i-\bar y)^2}}, \qquad t=r\sqrt{\frac{n-2}{1-r^2}}\ \sim\ t_{n-2} \]

**Symbols.** \(r\in[-1,1]\); \(n\) pairs.
**Purpose.** Strength and direction of linear association; the test asks whether \(\rho=0\).
**Assumptions.** Linear relationship, bivariate normality for the exact test, no extreme outliers.
**When to use.** Screening, validation, collinearity checks. Not for curved relationships.
**Example.** \(r=0.30,n=100\): \(t=0.30\sqrt{98/0.91}=3.11\), \(p=0.002\) — statistically clear, but only 9 % of variance explained.

### 18.2 Spearman and Fisher's transform

\[ r_s = 1-\frac{6\sum d_i^2}{n(n^2-1)}, \qquad z_r=\operatorname{artanh}(r),\quad SE=\frac{1}{\sqrt{n-3}} \]

**Symbols.** \(d_i\) rank differences; \(z_r\) Fisher's z.
**Purpose.** \(r_s\): monotone association, robust to outliers. \(z_r\): interval for a correlation and comparison of two.
**Assumptions.** \(r_s\): monotone relationship, no ties dominating; \(z_r\): approximate bivariate normality, \(n\ge10\).
**When to use.** Ordinal data, skewed data, pooling correlations.
**Example.** \(r=0.5,n=50\): \(z_r=0.549\), 95 % CI \(0.549\pm1.96/6.86=(0.263,0.835)\), back-transformed \((0.257,0.683)\).

## 19. Regression

### 19.1 Simple linear regression

\[ \hat\beta_1=\frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2}, \qquad \hat\beta_0=\bar y-\hat\beta_1\bar x, \qquad \hat y=\hat\beta_0+\hat\beta_1x \]

**Symbols.** \(\beta_1\) slope (change in \(y\) per unit \(x\)); \(\beta_0\) intercept.
**Purpose.** Model and predict a linear relationship.
**Assumptions.** Linearity, independent errors, constant variance, normal errors for tests and intervals.
**When to use.** Prediction, adjustment for confounders (multiple regression), trend description.
**Example.** \(\bar x=4,\bar y=60,\hat\beta_1=5\): \(\hat\beta_0=40\); predicted \(y\) at \(x=6\) is 70.

### 19.2 Inference, fit and prediction

\[ SE(\hat\beta_1)=\frac{s_e}{\sqrt{\sum (x_i-\bar x)^2}}, \qquad R^2=1-\frac{SSE}{SST}, \qquad \hat y_0\pm t\,s_e\sqrt{1+\frac{1}{n}+\frac{(x_0-\bar x)^2}{\sum (x_i-\bar x)^2}} \]

**Symbols.** \(s_e\) residual SD; \(SSE\) residual sum of squares; \(SST\) total sum of squares.
**Purpose.** Test a slope, measure fit, and give an interval for a **new** observation.
**Assumptions.** As above; the prediction interval is much wider than the confidence interval for the mean response.
**When to use.** Reporting a regression coefficient with an interval; forecasting.
**Example.** \(R^2=0.59\): 59 % of the variation in \(y\) is explained; \(s_e=6.7\) makes a single prediction far less precise than the average line.

### 19.3 Multiple regression

\[ \hat{\boldsymbol\beta}=(\mathbf X^\top\mathbf X)^{-1}\mathbf X^\top\mathbf y, \qquad \mathrm{Var}(\hat{\boldsymbol\beta})=\sigma^2(\mathbf X^\top\mathbf X)^{-1} \]

**Symbols.** \(\mathbf X\) design matrix with a column of ones; \(\mathbf y\) response vector.
**Purpose.** Estimate partial effects holding other predictors fixed; the basis of adjustment.
**Assumptions.** No perfect collinearity, correct functional form, homoscedastic independent errors.
**When to use.** Confounder adjustment, multivariable prediction. A coefficient is a *conditional* association.
**Example.** Study-hours coefficient 1.66 (1.52, 1.79): one extra weekly hour is associated with about 1.7 more marks at fixed attendance, GPA and workload.

## 20. ANOVA

### 20.1 One-way decomposition

\[ SS_T=\sum_{i}\sum_{j}(y_{ij}-\bar y)^2,\quad SS_A=\sum_i n_i(\bar y_i-\bar y)^2,\quad SS_E=SS_T-SS_A \]

\[ F=\frac{SS_A/(k-1)}{SS_E/(N-k)}\ \sim\ F_{k-1,\,N-k} \]

**Symbols.** \(k\) groups, \(n_i\) per group, \(N\) total; \(\bar y_i\) group means.
**Purpose.** Test whether several group means are equal, without inflating error by pairwise testing.
**Assumptions.** Independent groups, normal residuals, equal variances (Levene's test), fixed groups.
**When to use.** Three or more groups on a quantitative outcome. With two groups it equals the two-sample \(t\).
**Example.** Three programmes, \(F=1.43\), \(p=0.241\) — no evidence of a difference; do not run post-hoc tests.

### 20.2 Effect size and Tukey HSD

\[ \eta^2=\frac{SS_A}{SS_T}, \qquad HSD=q_{1-\alpha,\,k,\,N-k}\sqrt{\frac{MS_E}{n}} \]

**Symbols.** \(\eta^2\) proportion of variance explained; \(MS_E=SS_E/(N-k)\); \(q\) studentised range critical value.
**Purpose.** \(\eta^2\): how large the effect is. Tukey: which pairs differ, controlling family-wise error.
**Assumptions.** Equal group sizes for the simple HSD formula; balanced designs otherwise adjust \(n\).
**When to use.** After a significant omnibus test, to locate the difference.
**Example.** \(\eta^2=0.14\) is a large effect; a pair differing by more than HSD is declared different.

## 21. Chi-square tests

### 21.1 Goodness of fit and independence

\[ \chi^2=\sum_{i}\frac{(O_i-E_i)^2}{E_i}, \qquad E_{ij}=\frac{(\text{row }i\text{ total})(\text{column }j\text{ total})}{N} \]

**Symbols.** \(O\) observed, \(E\) expected under \(H_0\); df \(=k-1\) for fit, \((r-1)(c-1)\) for independence.
**Purpose.** Compare observed counts with a hypothesised pattern or test association in a table.
**Assumptions.** Independent observations, expected counts at least 5, categories exhaustive and exclusive.
**When to use.** Survey cross-tabs, screening agreement, testing a claimed distribution.
**Example.** 2×2 table of 1,600 patients: \(\chi^2\) for association; a \(p<0.001\) means the test result and disease are not independent.

### 21.2 Association strength, small tables, and paired binary data

\[ V=\sqrt{\frac{\chi^2}{N\min(r-1,c-1)}}, \qquad \chi^2_{\text{Yates}}=\sum\frac{(|O-E|-0.5)^2}{E}, \qquad \chi^2_{\text{McNemar}}=\frac{(b-c)^2}{b+c} \]

**Symbols.** \(V\) Cramér's \(V\in[0,1]\); \(b,c\) discordant pairs in a matched 2×2 table.
**Purpose.** Effect size for a table; a continuity correction for 2×2 tables; a test for paired binary data.
**Assumptions.** Yates for small expected counts; McNemar for matched pairs, not independent groups.
**When to use.** Reporting association beyond \(p\); before/after binary outcomes.
**Example.** \(\chi^2=12.8,N=1{,}400\) in a 4×2 table: \(V=\sqrt{12.8/1400}=0.096\) — a real but small association.

## 22. Nonparametric tests

### 22.1 Sign test and Wilcoxon signed-rank

\[ S=\#\{d_i>0\}\sim\mathrm{Bin}(n,0.5), \qquad W=\sum_{i}r_i\,\mathbb 1[d_i>0] \]

**Symbols.** \(d_i\) paired differences; \(r_i\) ranks of \(|d_i|\); \(W\) the sum of positive ranks.
**Purpose.** Test a median difference without assuming normality.
**Assumptions.** Pairs are independent; the signed-rank test assumes symmetric differences.
**When to use.** Small samples, ordinal data, obvious outliers.
**Example.** 10 pairs, 8 positive: sign-test \(p=2(0.055)=0.11\) — suggestive, not conclusive.

### 22.2 Mann–Whitney U, Kruskal–Wallis and Friedman

\[ U=n_1n_2+\frac{n_1(n_1+1)}{2}-R_1, \qquad H=\frac{12}{N(N+1)}\sum_i\frac{R_i^2}{n_i}-3(N+1) \]

**Symbols.** \(R_1\) rank sum of group 1; \(R_i\) rank sum per group; \(H\) Kruskal–Wallis statistic (approx. \(\chi^2_{k-1}\)).
**Purpose.** Two-group and \(k\)-group comparisons on ranks; Friedman does the same for repeated measures.
**Assumptions.** Independent groups (U, H); exchangeability under the null; similar shapes for a pure location interpretation.
**When to use.** Skewed or ordinal outcomes, violated normality, small \(n\).
**Example.** Two groups of 8 with rank sums 90 and 46: \(U=64+36-90=10\), near the lower tail.

## 23. Bayesian inference

### 23.1 Posterior, conjugate beta–binomial, credible interval

\[ p(\theta\mid y)\propto p(y\mid\theta)p(\theta), \qquad \theta\mid y\sim\mathrm{Beta}(a+y,\ b+n-y) \]

**Symbols.** \(\theta\) parameter; \(y\) successes in \(n\) trials; \(a,b\) beta prior parameters.
**Purpose.** Full distribution of belief about a parameter; intervals read as "95 % probability the parameter lies here".
**Assumptions.** A stated prior; the likelihood must match the data-generating process; conjugacy needs the right pair.
**When to use.** Small samples, sequential updating, decision problems with explicit priors.
**Example.** Prior Beta(2,8) (mean 0.2), observe 7/20: posterior Beta(9,21), mean \(9/30=0.30\).

### 23.2 Posterior predictive and Bayes factor

\[ p(\tilde y\mid y)=\int p(\tilde y\mid\theta)p(\theta\mid y)\,d\theta, \qquad BF_{10}=\frac{p(y\mid H_1)}{p(y\mid H_0)} \]

**Symbols.** \(\tilde y\) future observation; \(BF_{10}\) evidence for \(H_1\) over \(H_0\).
**Purpose.** Predict new data accounting for parameter uncertainty; compare hypotheses without a \(p\)-value.
**Assumptions.** Priors must be proper for the Bayes factor; the comparison depends on them.
**When to use.** Forecasting, model comparison, communicating evidence as a ratio.
**Example.** \(BF_{10}=4\) means the data are four times more likely under \(H_1\) — moderate evidence, not proof.

## 24. Bootstrap and Monte Carlo

### 24.1 Bootstrap standard error and percentile interval

\[ \widehat{SE}_{\text{boot}}=\sqrt{\frac{1}{B-1}\sum_{b=1}^{B}\left(\hat\theta^{*}_b-\bar\theta^{*}\right)^2}, \qquad \left[\hat\theta^*_{(\alpha/2)},\ \hat\theta^*_{(1-\alpha/2)}\right] \]

**Symbols.** \(B\) resamples; \(\hat\theta^*_b\) the estimate from resample \(b\); parentheses denote order statistics.
**Purpose.** Uncertainty for statistics with no closed-form standard error (medians, ratios, \(R^2\)).
**Assumptions.** Observations independent and representative; \(B\) large (1,000+); the percentile method is poor for very skewed statistics (use BCa).
**When to use.** Complex estimators, small samples with a clear data-generating story, model validation.
**Example.** Median with 1,000 resamples: bootstrap SE 0.8, 95 % percentile interval \((54.9,58.1)\).

### 24.2 Permutation test and Monte Carlo integration

\[ p=\frac{1+\#\{T^{*}_b\ge T_{\text{obs}}\}}{B+1}, \qquad \hat I=\frac{1}{M}\sum_{m=1}^{M}g(U_m),\quad SE=\frac{s_g}{\sqrt M} \]

**Symbols.** \(T^*\) statistic under random relabelling; \(U_m\) uniform draws; \(g\) integrand.
**Purpose.** Exact-ish \(p\)-values under the sharp null; numerical integration where calculus fails.
**Assumptions.** Permutation: exchangeability under \(H_0\). Monte Carlo: independent draws, finite variance.
**When to use.** Small samples, unusual statistics, checking a parametric test, Bayesian computation.
**Example.** 999 permutations, 12 as extreme as observed: \(p=13/1000=0.013\).

---

Back to [Formula sheet — foundations](formula-sheet.md) · See also the
[test selection guide](test-selection.md) and the [distribution comparison](revision/distributions.md).
