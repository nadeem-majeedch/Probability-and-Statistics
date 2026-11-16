---
title: Conceptual questions
description: Thirty-five questions that test understanding rather than computation, with answers — the ones examinations use to separate memorising from knowing.
---

# Conceptual questions

Answer out loud before reading the answer. Each one is a question an examiner can ask in one
sentence and that a formula sheet cannot answer.

## Probability

**1. Why does P(A|B) usually differ from P(B|A)?**
They condition on different things. P(disease | positive test) conditions on the test result;
P(positive test | disease) conditions on the disease. The first depends on prevalence, the second
does not.

**2. If P(A|B) = P(A), what follows?**
That A and B are independent — knowing B tells you nothing about A. Independence is symmetric, so
P(B|A) = P(B) too.

**3. Can two events be mutually exclusive and independent?**
Only if one has probability zero. Mutually exclusive events with positive probability are maximally
dependent: one occurring rules the other out.

**4. Why is the law of total probability useful?**
It converts a hard unconditional probability into easy conditional ones, split by a variable you
can condition on — the formal version of "break it down by case".

**5. A test is 99 % accurate and the disease affects 1 in 10,000. A patient tests positive. What
is the chance they have it?**
About 1 %. The 99 false positives per 10,000 healthy people overwhelm the 1 true positive. This is
the base-rate fallacy, and Bayes' theorem is the fix.

## Random variables

**6. What is the difference between a density and a probability?**
A density is a height; probability is area under it. For a continuous variable, P(X = x) = 0 for
every x, yet densities can exceed 1.

**7. Why does the sample variance divide by n − 1?**
Because the deviations are measured from x̄, which was itself estimated from the same data. That
costs one degree of freedom; dividing by n − 1 makes the estimator unbiased.

**8. Does Var(X + Y) always equal Var(X) + Var(Y)?**
No — only when the covariance is zero. Generally there is a 2Cov(X, Y) term, and it can be negative.

**9. Is zero correlation the same as independence?**
No. Independence implies zero correlation, not the reverse. X and X² are dependent but uncorrelated
when X is symmetric about zero.

**10. Why is E[X²] not (E[X])²?**
E[X²] includes the spread. The difference between them *is* the variance, which is zero only for a
constant.

**11. When is the Poisson distribution inappropriate?**
When the variance exceeds the mean (over-dispersion), when events cluster, or when the rate changes
over the exposure — the negative binomial or a mixed model is then needed.

**12. Why is the exponential distribution memoryless, and why does that matter?**
Because P(X > s + t | X > s) = P(X > t): past waiting tells you nothing. It matters because it makes
the maths simple and because real processes that wear out are *not* memoryless, so the model fails
exactly where engineering cares.

## Sampling and limit theorems

**13. What exactly does the Central Limit Theorem say?**
That the standardised sample mean converges in distribution to N(0, 1) as n grows, for independent
observations with finite variance. It is about the distribution of the *mean*, not of the data.

**14. Does the CLT apply to the sample median?**
Not directly, but a version does: suitably standardised sample quantiles are also asymptotically
normal, with a different variance.

**15. Why does the standard error shrink with √n rather than n?**
Because variances of independent sums add, so the variance of a mean falls as 1/n and its SD as
1/√n. Quadrupling the sample halves the error — a law of diminishing returns.

**16. When does the CLT fail?**
With infinite variance (Cauchy), with strong dependence (time series), with extreme quantiles, and
for very small samples from very skewed populations.

**17. What is the difference between a sampling distribution and a population distribution?**
The population distribution describes individuals; the sampling distribution describes a statistic
over repeated samples. Their spreads differ by a factor of √n.

## Inference

**18. What is a p-value?**
The probability of observing data at least as extreme as yours, assuming the null hypothesis is
true. It is not the probability that the null is true, nor the probability you are wrong.

**19. What does "95 % confidence" mean?**
That the procedure produces intervals containing the true parameter in 95 % of repeated samples. A
particular interval either contains it or does not; the probability attaches to the method.

**20. Why can a result be statistically significant but practically useless?**
Because significance measures evidence against the null, and with a large enough sample even a
trivial difference is detectable. The effect size and interval answer the practical question.

**21. Why is "not significant" not "no effect"?**
A non-significant result may reflect low power. The interval may still contain effects of real
importance; the correct statement is that the data are compatible with no effect, not that none
exists.

**22. What happens to the Type II error rate when you lower α?**
It rises. Requiring stronger evidence reduces false positives and increases missed effects, unless
the sample grows.

**23. Why is power important before a study rather than after?**
Because it determines whether the study can answer the question at all. A post-hoc power
calculation from the observed effect is a transformation of the p-value and adds nothing.

**24. Why should the number of tests be limited, or corrected?**
Each test carries its own false-positive risk; 20 independent tests at α = 0.05 give a 64 % chance
of at least one false positive. Correction procedures control the family-wise error or the false
discovery rate.

**25. Why is a one-tailed test not simply "more powerful"?**
It is more powerful *in one direction* and completely blind in the other. Choosing the direction
after seeing the data invalidates the p-value.

**26. What is the relationship between a confidence interval and a hypothesis test?**
They are inversions of each other: a 95 % interval contains exactly the null values that a
two-sided test at α = 0.05 would not reject. The interval is more informative because it shows the
whole set.

## Regression and modelling

**27. What does R² = 0.9 tell you, and what does it not?**
That 90 % of the variation in the outcome is explained in this sample. It does not show causation, a
correct functional form, or good out-of-sample prediction.

**28. Why can a regression coefficient change sign when another predictor is added?**
Because the coefficient is a *partial* effect. Adding a correlated predictor changes what is being
held constant; this is confounding or suppression, and it is a finding, not a bug.

**29. Why is extrapolation dangerous?**
The model is fitted only where data exist. Outside that range the functional form is an assumption
with no evidence behind it.

**30. Why is a prediction interval wider than a confidence interval?**
The confidence interval is for the mean response at a given x; the prediction interval is for a
single new observation, so it adds the residual variance to the uncertainty.

**31. When is a logistic regression coefficient an odds ratio?**
Always — exp(β) is the multiplicative change in odds per unit of the predictor. It is *not* a change
in probability, which depends on where you start.

## Bayesian and computational

**32. What is the difference between a confidence interval and a credible interval?**
The credible interval is a statement about the parameter given the data and the prior; the
confidence interval is a statement about the procedure. They often coincide numerically with a flat
prior, which is why the confusion persists.

**33. Why does a Bayesian interval shrink toward the prior with small samples?**
Because the posterior is a weighted compromise between prior and likelihood; with little data the
prior carries more weight. That is a feature when the prior is genuine, and a hazard when it is not.

**34. When is the bootstrap unreliable?**
With dependent data (time series, clusters), with very small samples, for extreme order statistics,
and when the statistic is not smooth (e.g. the maximum).

**35. Why report the Monte Carlo error?**
Because a simulation estimate is itself an estimate. Without its standard error you cannot tell
whether two simulated answers differ or whether you simply used too few draws.
