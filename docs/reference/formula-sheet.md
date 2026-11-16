---
title: Formula sheet — foundations
description: Every formula from descriptive statistics to joint distributions, with symbols, purpose, assumptions, when to use it and a worked example.
---

# Formula sheet — foundations

Part 1 of 2: Modules 03–11. The second page covers [sampling, inference and modelling](formula-sheet-inference.md).

Every entry has the same shape: the formula, its symbols, what it is for, the assumptions it
carries, when to reach for it, and a numerical example. Symbols follow the
[notation page](notation.md). Formulas are tools with conditions attached; the assumptions line is
not decoration.

**How to revise with this page.** Cover the right-hand side of each entry, reconstruct it, then
check the example by hand. If you cannot reproduce the example, you have memorised the shape but
not the formula.

## 1. Descriptive statistics

### 1.1 Sample mean

\[ \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i \]

**Symbols.** \(n\) sample size; \(x_i\) the \(i\)-th observation; \(\bar{x}\) the arithmetic average.
**Purpose.** Summarises a batch of numbers by its balance point.
**Assumptions.** Quantitative data; the mean is meaningful (not for pure categories).
**When to use.** Symmetric data, or whenever the total matters (revenue, marks out of a fixed total).
**Example.** \(2, 4, 4, 9\): \(\bar{x} = 19/4 = 4.75\), although no observation equals it.

### 1.2 Median and quartiles

\[ \tilde{x} = \begin{cases} x_{(m+1)}, & n = 2m+1 \\ \tfrac{1}{2}\left(x_{(m)} + x_{(m+1)}\right), & n = 2m \end{cases} \]

**Symbols.** \(x_{(1)}\le\dots\le x_{(n)}\) the sorted data; \(\tilde{x}\) the median; \(Q_1, Q_3\) the 25th and 75th percentiles.
**Purpose.** A centre that ignores how extreme the extremes are.
**Assumptions.** At least ordinal data; no distributional assumption.
**When to use.** Skewed data, outliers, house prices, incomes, waiting times.
**Example.** \(2,4,4,9\): median \(= 4\); the mean was dragged to 4.75 by the 9.

### 1.3 Interquartile range and five-number summary

\[ IQR = Q_3 - Q_1, \qquad \text{outlier if } x < Q_1 - 1.5\,IQR \ \text{ or }\ x > Q_3 + 1.5\,IQR \]

**Symbols.** \(Q_1, Q_3\) first and third quartiles; \(IQR\) the middle 50 % span.
**Purpose.** A spread measure immune to outliers, and a rule for flagging them.
**Assumptions.** Quantitative data; quartile definition must be stated (methods differ slightly).
**When to use.** Box plots, skewed data, screening before modelling.
**Example.** \(Q_1=4, Q_3=9\): \(IQR=5\), fences at \(-3.5\) and 16.5, so nothing is flagged.

### 1.4 Standard score (z-score)

\[ z = \frac{x - \bar{x}}{s} \]

**Symbols.** \(s\) sample standard deviation.
**Purpose.** Puts different variables on one scale: "how many SDs from average".
**Assumptions.** A roughly symmetric distribution for the usual 68–95–99.7 reading.
**When to use.** Comparing across units (heights vs weights), standardising before regression.
**Example.** Score 80, \(\bar{x}=70\), \(s=10\): \(z=1\) — one SD above average, about the 84th percentile if normal.

## 2. Measures of central tendency

### 2.1 Weighted mean

\[ \bar{x}_w = \frac{\sum w_i x_i}{\sum w_i} \]

**Symbols.** \(w_i\) non-negative weights.
**Purpose.** Average when observations carry different importance or represent different counts.
**Assumptions.** Weights are meaningful and sum to something positive.
**When to use.** Course grades with credit hours, survey data with sampling weights, grouped data.
**Example.** Marks 60 (2 credits), 90 (1 credit): \((60\cdot2 + 90\cdot1)/3 = 70\), not 75.

### 2.2 Geometric and harmonic means

\[ G = \left(\prod_{i=1}^{n} x_i\right)^{1/n}, \qquad H = \frac{n}{\sum_{i=1}^{n} 1/x_i} \]

**Symbols.** \(x_i > 0\).
**Purpose.** \(G\) averages multiplicative growth; \(H\) averages rates.
**Assumptions.** Strictly positive values.
**When to use.** \(G\): growth rates, index numbers. \(H\): speeds, price-to-earnings, averaging ratios.
**Example.** Growth of 10 % then 20 %: \(G=\sqrt{1.1\times1.2}=1.1487\), i.e. 14.87 % per year, not 15 %.

## 3. Measures of dispersion

### 3.1 Sample variance and standard deviation

\[ s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2, \qquad s = \sqrt{s^2} \]

**Symbols.** \(s^2\) unbiased sample variance; divisor \(n-1\) (Bessel's correction).
**Purpose.** Average squared distance from the mean; the basis of nearly every standard error.
**Assumptions.** Quantitative data; divisor \(n-1\) when the mean is estimated from the same data.
**When to use.** Any time you need spread for inference; report \(s\) for interpretability.
**Example.** \(2,4,4,9\): deviations \(-2.75,-0.75,-0.75,4.25\), \(s^2 = 26.75/3 = 8.92\), \(s=2.99\).

### 3.2 Mean absolute deviation and coefficient of variation

\[ MAD = \frac{1}{n}\sum |x_i-\bar{x}|, \qquad CV = \frac{s}{\bar{x}} \]

**Symbols.** \(CV\) unitless.
**Purpose.** \(MAD\): spread in original units, less sensitive to squaring. \(CV\): spread relative to size.
**Assumptions.** \(CV\) requires a positive mean on a ratio scale.
**When to use.** \(CV\) to compare variability across variables with different units; \(MAD\) in robust reporting.
**Example.** \(s=2.99\), \(\bar{x}=4.75\): \(CV=0.63\), i.e. 63 % — highly variable.

### 3.3 Standard error of the mean

\[ SE(\bar{x}) = \frac{s}{\sqrt{n}} \]

**Symbols.** \(s\) sample SD; \(n\) sample size.
**Purpose.** How much a sample mean would wobble across repeated samples; the unit of every interval.
**Assumptions.** Independent observations (or a correction for finite populations).
**When to use.** Always, before quoting any mean as an estimate.
**Example.** \(s=10, n=100\): \(SE=1\); quadrupling \(n\) halves it.

## 4. Counting and combinatorics

### 4.1 Multiplication rule, permutations and combinations

\[ n! = n(n-1)\cdots 1, \qquad {}_nP_r = \frac{n!}{(n-r)!}, \qquad \binom{n}{r} = \frac{n!}{r!\,(n-r)!} \]

**Symbols.** \(n\) items, \(r\) chosen; order matters for \({}_{n}P_r\), not for \(\binom{n}{r}\).
**Purpose.** Count arrangements so probabilities can be built from equally likely outcomes.
**Assumptions.** Distinct items, sampling without replacement unless stated.
**When to use.** Lottery odds, card hands, arrangements of letters, binomial coefficients.
**Example.** A 5-card hand from 52: \(\binom{52}{5} = 2{,}598{,}960\); the probability of four aces is \(48/2{,}598{,}960 \approx 1.85\times10^{-5}\).

### 4.2 Permutations with repetition, and stars and bars

\[ \frac{n!}{n_1!\,n_2!\cdots n_k!}, \qquad \binom{n+k-1}{k-1} \]

**Symbols.** \(n_i\) copies of item \(i\); \(n\) identical items into \(k\) distinct boxes.
**Purpose.** Count distinct arrangements of repeated items; count distributions of identical objects.
**Assumptions.** Items identical within type; boxes distinguishable.
**When to use.** Anagram counts, allocating \(n\) identical tasks to \(k\) workers.
**Example.** "BANANA": \(6!/(3!2!1!) = 60\) distinct arrangements. Ten identical jobs to 3 teams: \(\binom{12}{2}=66\) ways.

## 5. Probability rules

### 5.1 Complement and addition

\[ P(A^c) = 1 - P(A), \qquad P(A\cup B) = P(A) + P(B) - P(A\cap B) \]

**Symbols.** \(A^c\) complement; \(\cup\) union ("or"); \(\cap\) intersection ("and").
**Purpose.** The two workhorses for combining events.
**Assumptions.** Kolmogorov axioms; for the simplified \(P(A)+P(B)\) the events must be disjoint.
**When to use.** "At least one" problems (use the complement), overlapping categories.
**Example.** \(P(A)=0.4, P(B)=0.5, P(A\cap B)=0.1\): \(P(A\cup B)=0.8\).

### 5.2 Independence and the multiplication rule

\[ P(A\cap B) = P(A)P(B) \iff A \perp B, \qquad P(A\cap B) = P(A)\,P(B\mid A) \]

**Symbols.** \(\perp\) independence; \(P(B\mid A)\) conditional probability.
**Purpose.** Multiplying along a path of a tree; testing whether events carry information about each other.
**Assumptions.** The first form *defines* independence and is not valid for dependent events.
**When to use.** Independent trials, series systems, and as the null model in contingency tables.
**Example.** Two independent servers each failing with \(p=0.01\): both fail with \(0.0001\).

## 6. Conditional probability

### 6.1 Definition and the chain rule

\[ P(A\mid B) = \frac{P(A\cap B)}{P(B)},\quad P(B)>0, \qquad P(A\cap B\cap C) = P(A)P(B\mid A)P(C\mid A\cap B) \]

**Symbols.** \(P(A\mid B)\) probability of \(A\) given that \(B\) occurred.
**Purpose.** Restrict attention to a subset of the sample space; the engine behind Bayes and Markov models.
**Assumptions.** \(P(B)>0\); the conditioning event is known, not merely likely.
**When to use.** Screening tests, diagnostic reasoning, updating beliefs, sampling without replacement.
**Example.** 52 cards: \(P(\text{ace}\mid\text{spade}) = 1/13\), whereas \(P(\text{ace}) = 4/52 = 1/13\) — here independent.

### 6.2 Law of total probability

\[ P(B) = \sum_{i} P(B\mid A_i)\,P(A_i), \qquad \{A_i\} \text{ a partition of } \Omega \]

**Symbols.** \(A_i\) mutually exclusive, exhaustive cases; \(\Omega\) sample space.
**Purpose.** Compute an overall probability by splitting on a case you know something about.
**Assumptions.** The \(A_i\) must be disjoint and cover everything.
**When to use.** Mixture populations: prevalence-split accuracy, factory lines, weighted forecasts.
**Example.** Two machines make 60 % and 40 % of output with defect rates 2 % and 5 %: \(P(\text{defect}) = 0.6(0.02)+0.4(0.05)=0.032\).

## 7. Bayes' theorem

### 7.1 Bayes' theorem

\[ P(A\mid B) = \frac{P(B\mid A)\,P(A)}{P(B)} = \frac{P(B\mid A)P(A)}{\sum_i P(B\mid A_i)P(A_i)} \]

**Symbols.** \(P(A)\) prior; \(P(B\mid A)\) likelihood; \(P(A\mid B)\) posterior; denominator the evidence.
**Purpose.** Turn a test result into the probability you actually want.
**Assumptions.** A genuine prior; a partition for the expanded form; likelihoods that match the population.
**When to use.** Diagnostic tests, spam filters, fraud alerts, any base-rate problem.
**Example.** Prevalence 1 %, sensitivity 90 %, specificity 95 %: \(P(\text{disease}\mid+) = \frac{0.9(0.01)}{0.9(0.01)+0.05(0.99)} = 0.154\) — a positive result still means only 15 %.

### 7.2 Odds form and posterior odds

\[ \underbrace{\frac{P(A\mid B)}{P(A^c\mid B)}}_{\text{posterior odds}} = \underbrace{\frac{P(B\mid A)}{P(B\mid A^c)}}_{\text{likelihood ratio}} \times \underbrace{\frac{P(A)}{P(A^c)}}_{\text{prior odds}} \]

**Symbols.** Likelihood ratio (LR) is the Bayes factor for two simple hypotheses.
**Purpose.** Updating is multiplication of odds, which is why evidence accumulates multiplicatively.
**Assumptions.** Two complementary hypotheses; the same data in both likelihoods.
**When to use.** Sequential testing, forensic evidence, explaining why a strong LR still leaves low posterior odds when the prior is tiny.
**Example.** Prior odds 1:99, LR 18: posterior odds \(18/99\), probability \(18/117 = 0.154\) — the same answer as 7.1.

## 8. Random variables

### 8.1 PMF, PDF and CDF

\[ p_X(x) = P(X=x), \qquad P(a<X\le b) = \int_a^b f_X(x)\,dx, \qquad F_X(x) = P(X\le x) \]

**Symbols.** \(p_X\) probability mass function (discrete); \(f_X\) density (continuous); \(F_X\) cumulative distribution function.
**Purpose.** Complete descriptions of a random variable's behaviour.
**Assumptions.** \(\sum p_X = 1\), \(f_X \ge 0\) with integral 1; a density is **not** a probability.
**When to use.** Any distributional calculation; \(F\) for quantiles and simulation (inverse transform).
**Example.** \(X\sim N(0,1)\): \(f(0)=0.399\), yet \(P(X=0)=0\). \(F(1.96)=0.975\).

### 8.2 Expectation of a function (LOTUS) and the MGF

\[ E[g(X)] = \sum_x g(x)p_X(x) \ \text{ or } \ \int g(x)f_X(x)\,dx, \qquad M_X(t) = E\left[e^{tX}\right] \]

**Symbols.** \(g\) any function; \(M_X\) moment generating function where it exists.
**Purpose.** Compute averages of transformed variables without deriving the new distribution; MGFs identify distributions and generate moments.
**Assumptions.** The sum or integral converges absolutely.
**When to use.** \(E[X^2]\), \(E[e^X]\), sums of independent variables (MGFs multiply).
**Example.** \(X\in\{1,2\}\) equally likely: \(E[X^2] = (1+4)/2 = 2.5\), so \(\mathrm{Var}(X)=2.5-2.25=0.25\).

## 9. Mathematical expectation

### 9.1 Linearity and the tower property

\[ E[aX+b] = aE[X]+b, \qquad E[X+Y] = E[X]+E[Y], \qquad E[X] = E\big[E[X\mid Y]\big] \]

**Symbols.** \(a,b\) constants; \(E[X\mid Y]\) a random variable.
**Purpose.** Expectation is linear always — independence is *not* required; the tower property averages conditional means.
**Assumptions.** Expectations exist (finite).
**When to use.** Simplifying sums, computing mixture means, proving unbiasedness.
**Example.** \(E[X]=3, E[Y]=4\): \(E[2X-Y+1] = 6-4+1 = 3\), whatever the dependence.

### 9.2 Moments, skewness and kurtosis

\[ \mu_k = E[(X-\mu)^k], \qquad \text{skew} = \frac{\mu_3}{\sigma^3}, \qquad \text{kurt} = \frac{\mu_4}{\sigma^4} \]

**Symbols.** \(\mu=E[X]\); \(\sigma^2=\mathrm{Var}(X)\).
**Purpose.** Describe asymmetry and tail weight beyond mean and variance.
**Assumptions.** The moments must exist — the Cauchy distribution has none.
**When to use.** Checking normality informally, describing financial returns, diagnosing heavy tails.
**Example.** A normal has skew 0 and kurtosis 3; returns with kurtosis 8 have far heavier tails than a normal with the same SD.

## 10. Variance and covariance

### 10.1 Variance rules

\[ \mathrm{Var}(X) = E[X^2] - (E[X])^2, \qquad \mathrm{Var}(aX+b)=a^2\mathrm{Var}(X) \]

\[ \mathrm{Var}(X\pm Y) = \mathrm{Var}(X)+\mathrm{Var}(Y)\pm 2\mathrm{Cov}(X,Y) \]

**Symbols.** \(a,b\) constants; \(\mathrm{Cov}\) covariance.
**Purpose.** Spread of a transformed or combined variable; note the plus sign even for a difference.
**Assumptions.** Finite second moments.
**When to use.** Portfolio risk, error propagation, standard errors of differences.
**Example.** \(\mathrm{Var}(X)=\mathrm{Var}(Y)=4\), \(\mathrm{Cov}=2\): \(\mathrm{Var}(X-Y)=4+4-4=4\), not 8.

### 10.2 Covariance and correlation

\[ \mathrm{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)], \qquad \rho = \frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y} \in [-1,1] \]

**Symbols.** \(\rho\) population correlation; \(r\) its sample estimate.
**Purpose.** Direction and strength of linear association.
**Assumptions.** Finite variances; \(\rho\) measures *linear* association only.
**When to use.** Screening relationships, building covariance matrices, checking collinearity.
**Example.** \(\sigma_X=2,\sigma_Y=5,\mathrm{Cov}=6\): \(\rho=0.6\).

## 11. Discrete distributions

### 11.1 Bernoulli and binomial

\[ P(X=x)=p^x(1-p)^{1-x}, \qquad P(X=k)=\binom{n}{k}p^k(1-p)^{n-k} \]

**Symbols.** \(n\) independent trials, success probability \(p\), \(k\) successes.
**Purpose.** Count successes in a fixed number of binary trials.
**Assumptions.** Fixed \(n\), constant \(p\), independence.
**When to use.** Conversion counts, defect counts with constant rate, survey yes/no.
**Example.** \(n=10,p=0.2\): \(P(X=2)=\binom{10}{2}(0.2)^2(0.8)^8=0.302\). Mean \(np=2\), variance \(np(1-p)=1.6\).

### 11.2 Geometric and negative binomial

\[ P(X=k)=(1-p)^{k-1}p, \qquad P(X=k)=\binom{k-1}{r-1}p^r(1-p)^{k-r} \]

**Symbols.** \(k\) trial on which the \(r\)-th success occurs.
**Purpose.** Waiting times to the first (or \(r\)-th) success.
**Assumptions.** Independent trials, constant \(p\), unbounded number of trials.
**When to use.** Number of attempts until a sale, failures before \(r\) defects.
**Example.** \(p=0.1\): mean attempts to first success \(1/p=10\); \(P(X=3)=0.9^2(0.1)=0.081\).

### 11.3 Poisson

\[ P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!}, \qquad E[X]=\mathrm{Var}(X)=\lambda \]

**Symbols.** \(\lambda\) expected count per unit of exposure.
**Purpose.** Counts of rare events in time, space or volume.
**Assumptions.** Independence, constant rate, mean equals variance. Over-dispersion breaks it.
**When to use.** Arrivals per hour, defects per batch, typos per page.
**Example.** \(\lambda=3\): \(P(X=0)=e^{-3}=0.0498\); \(P(X\ge1)=0.950\).

### 11.4 Hypergeometric

\[ P(X=k)=\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}} \]

**Symbols.** \(N\) population, \(K\) successes in it, \(n\) drawn without replacement, \(k\) successes drawn.
**Purpose.** Successes in sampling **without** replacement.
**Assumptions.** Finite population, fixed composition, no replacement.
**When to use.** Quality sampling from a lot, card hands, small-population audits.
**Example.** 3 defective in 20, sample 5: \(P(X=1)=\binom{3}{1}\binom{17}{4}/\binom{20}{5}=0.4605\).

## 12. Continuous distributions

### 12.1 Uniform and exponential

\[ f(x)=\frac{1}{b-a}\ \text{ on }[a,b], \qquad f(x)=\lambda e^{-\lambda x},\ x\ge0 \]

**Symbols.** \(a,b\) bounds; \(\lambda\) rate, mean \(1/\lambda\).
**Purpose.** \(U\): total ignorance on an interval (and the basis of simulation). \(E\): waiting time in a memoryless process.
**Assumptions.** \(U\): support is the whole interval. \(E\): constant hazard — no ageing, no clustering.
**When to use.** Random number generation; inter-arrival times, component lifetimes without wear-out.
**Example.** \(U(0,1)\): \(P(X<0.3)=0.3\). Exponential with mean 5 min: \(P(X>5)=e^{-1}=0.368\).

### 12.2 Normal distribution and standardisation

\[ X\sim N(\mu,\sigma^2):\quad f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \qquad Z=\frac{X-\mu}{\sigma} \]

**Symbols.** \(\mu\) mean, \(\sigma^2\) variance (never \(\sigma\) in the second slot); \(Z\sim N(0,1)\).
**Purpose.** The reference distribution of the CLT, of errors, and of most test statistics.
**Assumptions.** Symmetry and light tails; standardisation requires known \(\mu,\sigma\).
**When to use.** z-scores, z-tests when \(\sigma\) is known, approximating sums.
**Example.** \(\mu=70,\sigma=10\): \(P(X>85)=P(Z>1.5)=0.067\).

### 12.3 Gamma, chi-square, \(t\) and \(F\)

\[ \chi^2_k = \mathrm{Gamma}\left(\tfrac{k}{2},2\right), \qquad T=\frac{Z}{\sqrt{V/k}},\quad V\sim\chi^2_k \]

\[ F_{d_1,d_2} = \frac{V_1/d_1}{V_2/d_2}, \qquad V_i \sim \chi^2_{d_i} \text{ independent} \]

**Symbols.** \(k\) degrees of freedom; \(Z\) standard normal; \(V\) chi-square.
**Purpose.** The three sampling distributions behind variance tests, means with estimated SD, and variance ratios.
**Assumptions.** Underlying normality for exactness; independence of numerator and denominator.
**When to use.** \(t\): means with unknown \(\sigma\). \(\chi^2\): variances, goodness of fit, independence. \(F\): ANOVA and variance-ratio tests.
**Example.** \(t_{10}\) at 95 % is 2.228 versus 1.96 for \(z\) — the extra width is the price of estimating \(\sigma\).

## 13. Joint distributions

### 13.1 Joint, marginal and conditional

\[ f_{X,Y}(x,y), \qquad f_X(x)=\int f_{X,Y}(x,y)\,dy, \qquad f_{Y\mid X}(y\mid x)=\frac{f_{X,Y}(x,y)}{f_X(x)} \]

**Symbols.** Subscripts denote the variable(s) described.
**Purpose.** Move between the joint behaviour and each variable's own distribution.
**Assumptions.** The joint integrates to 1; conditioning requires \(f_X(x)>0\).
**When to use.** Two-variable problems, mixtures, conditional expectation, Bayes with continuous data.
**Example.** Uniform on the unit square: \(f_{X,Y}=1\), marginals \(U(0,1)\), and \(f_{Y\mid X}=1\) — independent.

### 13.2 Independence and the correlation of a sum

\[ f_{X,Y}(x,y)=f_X(x)f_Y(y) \iff X\perp Y, \qquad \mathrm{Var}(X+Y)=\sigma_X^2+\sigma_Y^2+2\rho\sigma_X\sigma_Y \]

**Symbols.** \(\rho\) correlation; independence is stronger than zero correlation.
**Purpose.** Test and exploit independence; compute the variance of an aggregate.
**Assumptions.** The factorisation must hold for **all** \((x,y)\), not just on average.
**When to use.** Sums of independent random variables, portfolio variance, error propagation.
**Example.** \(\sigma_X=\sigma_Y=1,\rho=0\): the sum has variance 2. With \(\rho=-1\) it has variance 0.

---

Continue to [Formula sheet — inference and modelling](formula-sheet-inference.md) for sampling
distributions, the CLT, intervals, tests, regression, ANOVA, chi-square, nonparametrics, Bayesian
methods and resampling.
