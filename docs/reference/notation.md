---
title: Notation
description: One symbol, one meaning — the canonical notation used throughout the course.
---

# Notation

Statistics is unreadable when the same letter means three things. This page is the
single authority on symbols: if a module uses a symbol that is not here, that is an
error, and it should be reported.

Read this page once now, and return to it whenever a symbol looks unfamiliar.

## The four distinctions that matter most

Before the tables, four conventions cause most of the confusion in the subject.

**1. Random variable versus realised value.** A capital italic letter is a random
quantity; the lowercase letter is the number you actually observed.

\[ X \text{ is a random variable}, \qquad x \text{ is the value it took.} \]

**2. Parameter versus statistic.** A parameter describes the population and is
unknown; a statistic is computed from the sample and is known.

\[ \mu \text{ (parameter, unknown)} \qquad \bar{x} \text{ (statistic, known)} \]

**3. Estimator versus estimate.** An estimator is the *rule*, and it is random
because it depends on the sample. An estimate is the number the rule produced.

\[ \hat{\theta} \text{ (estimator, random)} \qquad \hat{\theta}_{\text{obs}}
\text{ (estimate, a number)} \]

**4. Variance, never standard deviation, in a normal's second argument.**

\[ X \sim N(\mu, \sigma^2) \]

## Symbols

### Data and samples

| Symbol | Meaning | Notes |
|---|---|---|
| \(n\) | sample size | number of observations |
| \(N\) | population size | capital for the population |
| \(x_1, \dots, x_n\) | observed values | lowercase: realised numbers |
| \(\bar{x}\) | sample mean | \(\frac{1}{n}\sum x_i\) |
| \(s^2\), \(s\) | sample variance, standard deviation | divisor \(n-1\) |
| \(s^2_n\) | population-style variance | divisor \(n\); used only when stated |
| \(Q_1, Q_2, Q_3\) | quartiles | \(Q_2\) is the median |
| \(IQR\) | interquartile range | \(Q_3 - Q_1\) |
| \(CV\) | coefficient of variation | \(s/\bar{x}\) |
| \(z\) | standard score | \((x-\bar{x})/s\) |

### Probability

| Symbol | Meaning | Notes |
|---|---|---|
| \(\Omega\) | sample space | set of all outcomes |
| \(\omega\) | an outcome | element of \(\Omega\) |
| \(A, B, C\) | events | subsets of \(\Omega\) |
| \(\Pr(A)\) | probability of \(A\) | a number in \([0,1]\) |
| \(A^c\) | complement of \(A\) | also written \(\bar{A}\) (avoided here) |
| \(A \cap B\), \(A \cup B\) | intersection, union | "and", "or" |
| \(\Pr(A \mid B)\) | conditional probability | read "given \(B\)" |
| \(A \indep B\) | independence | never written \(A \perp B\) |
| \(\emptyset\) | empty set / impossible event | \(\Pr(\emptyset)=0\) |
| \(\binom{n}{k}\) | binomial coefficient | \(n!/(k!(n-k)!)\) |

### Random variables and distributions

| Symbol | Meaning | Notes |
|---|---|---|
| \(X, Y, Z\) | random variables | capital italic |
| \(F_X(x)\) | cumulative distribution function | \(\Pr(X \le x)\) |
| \(f_X(x)\) | probability density function | continuous case |
| \(p_X(x)\) | probability mass function | discrete case |
| \(X \sim F\) | "\(X\) has distribution \(F\)" | |
| \(X_1,\dots,X_n \iid F\) | independent and identically distributed | replaces vague "random sample" |
| \(\Phi(z)\), \(\phi(z)\) | standard normal CDF, density | |
| \(\mathrm{Bern}(p)\), \(\mathrm{Bin}(n,p)\) | Bernoulli, binomial | |
| \(\mathrm{Geom}(p)\), \(\mathrm{NB}(r,p)\) | geometric, negative binomial | |
| \(\mathrm{Hypergeom}(N,K,n)\) | hypergeometric | |
| \(\mathrm{Pois}(\lambda)\) | Poisson | \(\lambda\) is a rate, not a mean duration |
| \(\mathrm{U}(a,b)\), \(\mathrm{Exp}(\lambda)\) | uniform, exponential | |
| \(\mathrm{Gamma}(\alpha,\beta)\), \(\mathrm{Beta}(a,b)\) | gamma, beta | |
| \(N(\mu,\sigma^2)\) | normal | variance, never SD |
| \(\mathrm{Lognormal}(\mu,\sigma^2)\) | lognormal | parameters of the log |
| \(\mathrm{Weibull}(k,\lambda)\) | Weibull | shape, scale |
| \(t_\nu\), \(\chi^2_\nu\), \(F_{\nu_1,\nu_2}\) | t, chi-square, F | subscript = degrees of freedom |

### Expectation and moments

| Symbol | Meaning | Notes |
|---|---|---|
| \(\E[X]\) | expectation | also \(\mu_X\) |
| \(\Var(X)\) | variance | \(\E[(X-\mu)^2]\) |
| \(\sd(X)\) | standard deviation | \(\sqrt{\Var(X)}\) |
| \(\Cov(X,Y)\) | covariance | |
| \(\rho\) | population correlation | |
| \(r\) | sample correlation | Pearson's |
| \(\rho_s\), \(\tau\) | Spearman's rho, Kendall's tau | |
| \(M_X(t)\) | moment generating function | \(\E[e^{tX}]\) |
| \(\mu_k'\), \(\mu_k\) | raw, central moments | |
| \(\E[X \mid Y]\) | conditional expectation | a random variable in \(Y\) |
| \(\Var(X \mid Y)\) | conditional variance | |

### Inference

| Symbol | Meaning | Notes |
|---|---|---|
| \(\theta\) | generic parameter | |
| \(\hat{\theta}\) | estimator of \(\theta\) | random |
| \(\se(\hat{\theta})\) | standard error | \(\sqrt{\Var(\hat{\theta})}\) |
| \(\alpha\) | significance level | \(\Pr(\text{Type I error})\) |
| \(\beta\) | \(\Pr(\text{Type II error})\) | power \(= 1-\beta\) |
| \(H_0, H_1\) | null, alternative hypothesis | |
| \(p\) | p-value | never "the probability \(H_0\) is true" |
| \(1-\alpha\) | confidence level | |
| \(\mathrm{CI}_{1-\alpha}\) | confidence interval | |
| \(d\) | Cohen's \(d\) effect size | |
| \(\eta^2\), \(\omega^2\) | ANOVA effect sizes | |
| \(V\) | Cramér's \(V\) | chi-square effect size |
| \(\hat{R}\) | MCMC convergence diagnostic | "R-hat"; target \(\approx 1\) |
| \(B\) | number of simulation replications | |
| \(\ell(\theta)\) | log-likelihood | |

## How formulas are read on this site

- Display mathematics is centred and numbered where a later section refers to it.
- Inline mathematics never breaks a sentence's grammar: "the mean \(\bar{x}\) is…",
  not "the mean is \(\bar{x}\) is…".
- A **plain-language reading** follows any display equation that carries an
  argument. If you cannot read the symbols, read that sentence first.
- Conditions of validity are stated with the result, not afterwards.
- Probabilities are proportions in derivations \(0 \le p \le 1\) and percentages
  only in interpretation sentences, never mixed in one expression.

## Reporting a notation error

If a module uses a symbol that contradicts this page, the module is wrong. Please
report it through the repository's issue tracker and state the module, section and
symbol.
