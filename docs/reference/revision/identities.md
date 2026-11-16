---
title: Mathematical identities
description: The algebraic, probabilistic and distributional identities that shorten derivations and catch errors.
---

# Mathematical identities

Identities are shortcuts with proofs behind them. Each line here is something you can quote in an
examination, and each is worth reconstructing once so you know where it comes from.

## Sums and deviations

\[ \sum_{i=1}^{n}(x_i-\bar x) = 0 \]

The deviations always cancel: the mean is the balance point.

\[ \sum_{i=1}^{n}(x_i-\bar x)^2 = \sum_{i=1}^{n}x_i^2 - n\bar x^2 \]

The computational form of the sum of squares; handy by hand, numerically worse than the two-pass
form on a computer.

\[ \sum_{i=1}^{n}(x_i-\bar x)(y_i-\bar y) = \sum_{i=1}^{n}x_iy_i - n\bar x\bar y \]

The same shift for covariance, and the reason the slope can be computed from three sums.

\[ s^2 = \frac{1}{n-1}\left(\sum x_i^2 - n\bar x^2\right) \]

Bessel's correction appears because the deviations were measured from an estimated centre.

## Probability

\[ P(A\cup B\cup C) = P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)+P(A\cap B\cap C) \]

Inclusion–exclusion: add singles, subtract pairs, add the triple.

\[ P(A\cap B) \le \min\{P(A),P(B)\}, \qquad P(A\cup B) \ge \max\{P(A),P(B)\} \]

Two inequalities that catch impossible answers instantly.

\[ P(A\mid B) = 1 - P(A^c\mid B) \]

Conditioning does not break the complement rule; only the sample space changed.

\[ \frac{P(A\mid B)}{P(A^c\mid B)} = \frac{P(B\mid A)}{P(B\mid A^c)}\cdot\frac{P(A)}{P(A^c)} \]

Bayes in odds form: posterior odds = likelihood ratio × prior odds.

## Expectation and variance

\[ E[aX+bY+c] = aE[X]+bE[Y]+c \qquad \text{(always, dependent or not)} \]

\[ E[XY] = E[X]E[Y] \quad \text{if } X\perp Y \]

The converse fails: zero correlation does not imply independence.

\[ \mathrm{Var}(X) = E[X^2] - (E[X])^2 \]

\[ \mathrm{Var}(aX+b) = a^2\mathrm{Var}(X), \qquad \mathrm{SD}(aX+b) = |a|\,\mathrm{SD}(X) \]

\[ \mathrm{Var}(X+Y) = \mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y) \]

The sign does **not** flip when you subtract; the covariance term flips instead.

\[ \mathrm{Cov}(X,Y) = E[XY]-E[X]E[Y] \]

\[ \mathrm{Var}(X) = E[\mathrm{Var}(X\mid Y)] + \mathrm{Var}(E[X\mid Y]) \]

The law of total variance: variability within groups plus variability between group means.

\[ E[X] = \sum_{k\ge1}P(X\ge k) \quad \text{for non-negative integer } X \]

A trick that turns tail sums into expectations, useful for waiting times.

## Distribution relations

\[ X\sim\mathrm{Bin}(n,p) \Rightarrow E[X]=np,\quad \mathrm{Var}(X)=np(1-p) \]

\[ \mathrm{Bin}(n,p) \to \mathrm{Poisson}(\lambda) \ \text{ as } n\to\infty,\ p\to0,\ np\to\lambda \]

Why the Poisson is the distribution of rare events.

\[ X_1+\cdots+X_n \sim \mathrm{Poisson}(n\lambda) \quad \text{for independent } X_i\sim\mathrm{Poisson}(\lambda) \]

Poisson counts add — the reason rates per unit exposure work.

\[ \text{If } X\sim\mathrm{Exp}(\lambda),\quad P(X>s+t\mid X>s)=P(X>t) \]

Memorylessness, and the only continuous distribution that has it.

\[ X_i\sim\mathrm{Gamma}(\alpha_i,\beta) \Rightarrow \sum_i X_i\sim\mathrm{Gamma}\left(\sum_i\alpha_i,\beta\right) \]

\[ X_i\sim N(\mu_i,\sigma_i^2) \text{ independent} \Rightarrow \sum_i X_i \sim N\left(\sum_i\mu_i,\ \sum_i\sigma_i^2\right) \]

The normal is closed under addition — with variances adding, never standard deviations.

\[ X\sim N(0,1),\ Y\sim\chi^2_k \text{ independent} \Rightarrow T=\frac{X}{\sqrt{Y/k}}\sim t_k \]

\[ T\sim t_k \Rightarrow T^2\sim F_{1,k} \]

So a two-sided \(t\)-test and a one-way ANOVA with two groups give the same p-value.

\[ (n-1)s^2/\sigma^2 \sim \chi^2_{n-1} \quad \text{for normal data} \]

## Estimation and inference

\[ \mathrm{Var}(\bar X) = \sigma^2/n, \qquad SE(\bar x)=s/\sqrt n \]

\[ s_p^2 = \frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2} \]

The pooled variance, valid only under equal population variances; Welch's approximation avoids it.

\[ SE(\bar x_1-\bar x_2) = \sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}} \]

\[ \text{A 95 % CI excludes } \mu_0 \iff \text{a two-sided test rejects } H_0:\mu=\mu_0 \text{ at } \alpha=0.05 \]

Interval and test are the same calculation viewed twice; inconsistency between them is an error.

\[ \text{power} \uparrow \text{ with } |\Delta|,\ n,\ \alpha; \qquad \beta \downarrow \text{ as power } \uparrow \]

\[ n \approx \frac{2(z_{1-\alpha/2}+z_{1-\beta})^2\sigma^2}{\Delta^2} \quad \text{(two-group means)} \]

## Regression and ANOVA

\[ b_1 = r\,\frac{s_y}{s_x}, \qquad R^2 = r^2 \ \text{(simple regression only)} \]

\[ \sum (y_i-\bar y)^2 = \sum(\hat y_i-\bar y)^2 + \sum(y_i-\hat y_i)^2 \]

\[ SST = SSR + SSE \]

The decomposition that gives ANOVA its name; it holds only when the model includes an intercept.

\[ F = t^2 \quad \text{for a two-group comparison} \]

\[ \hat\beta = (\mathbf X^\top\mathbf X)^{-1}\mathbf X^\top\mathbf y \]

\[ \mathrm{Var}(\hat\beta) = \sigma^2(\mathbf X^\top\mathbf X)^{-1} \]

## Bayesian and resampling

\[ \theta\mid y \sim \mathrm{Beta}(a+y,\ b+n-y) \quad \text{for } y \text{ successes in } n \text{ Bernoulli trials} \]

\[ E[\theta\mid y] = \frac{a+y}{a+b+n} \]

A weighted average of the prior mean and the data proportion — the shrinkage made explicit.

\[ \text{posterior mean} \to \hat p \ \text{ as } n\to\infty \]

Enough data overwhelms any reasonable prior.

\[ \widehat{SE}_{\text{boot}} \approx \frac{s}{\sqrt n} \quad \text{for the sample mean} \]

The bootstrap reproduces known theory where theory exists — a good check before using it where it
does not.

\[ p_{\text{perm}} = \frac{1+\#\{T^*\ge T_{\text{obs}}\}}{B+1} \]

The “+1” keeps the p-value from ever being exactly zero.
