# Statistics examination

**Covers:** Modules 12–18. **Time:** 90 minutes. **Total:** 100 marks.
**Instructions:** closed book; calculator allowed. Section C requires full working. The answer key
follows Section D.

| Section | Items | Marks | Suggested time |
|---|---|---|---|
| A. Multiple choice | 20 | 40 | 30 min |
| B. Short answers | 3 | 15 | 15 min |
| C. Numerical | 6 | 33 | 30 min |
| D. Scenario | 2 | 12 | 15 min |

## Section A — Multiple choice (2 marks each)

```quiz
Q1. The standard error of a mean estimated from 49 observations with \(s=14\) is
A) 14
B) 7
C) 2
D) 0.29
* C
Why: \(14/\sqrt{49}=14/7=2\). Dividing by 49 would wrongly give 0.29.

Q2. A 99 % confidence interval compared with a 95 % interval on the same data is
A) the same width
B) centred elsewhere
C) narrower
D) wider
* D
Why: The larger critical value (2.576 versus 1.96) widens the interval. Both are centred on the same estimate.

Q3. An estimator whose expected value differs from the parameter is
A) inconsistent
B) efficient
C) sufficient
D) biased
* D
Why: Bias is a statement about the mean of the sampling distribution. Consistency and efficiency concern large-sample behaviour and variance.

Q4. A test with power 0.85 has a Type II error rate of
A) 0.15
B) 0.85
C) 0.05
D) 0.30
* A
Why: Power is \(1-\beta\), so \(\beta=0.15\). The 0.05 figure would be the Type I error rate.

Q5. Doubling the sample size while keeping \(\alpha\) fixed
A) decreases power
B) leaves power unchanged
C) increases the Type I error rate
D) increases power for a given effect
* D
Why: A larger sample reduces the standard error, so a fixed effect is easier to detect. The Type I rate is set by \(\alpha\), not by \(n\).

Q6. A regression of sales on price gives a slope of −3.2 with a 95 % interval (−4.5, −1.9). The
A) higher prices are associated with lower mean sales
B) price explains most of the variation in sales
C) the intercept is negative
D) the slope is not distinguishable from zero
* A
Why: The interval excludes zero and is negative throughout. \(R^2\) and the intercept are separate questions.

Q7. \(R^2=0.81\) in a simple regression implies the correlation is
A) 0.09
B) 0.81
C) 0.9 or −0.9
D) 0.66
* C
Why: \(r=\pm\sqrt{0.81}=\pm0.9\); the sign comes from the slope, which \(R^2\) does not reveal.

Q8. The residual standard error is measured in
A) the units of \(x\)
B) squared units of \(y\)
C) no units
D) the units of \(y\)
* D
Why: Residuals are in \(y\)'s units, and their standard deviation is too. The residual variance is in squared units.

Q9. A one-way ANOVA with four groups and 40 observations has denominator degrees of freedom
A) 40
B) 36
C) 39
D) 3
* B
Why: \(N-k=40-4=36\). The numerator df is \(k-1=3\), and the two sum to 39.

Q10. A chi-square test of independence on a \(2\times3\) table has degrees of freedom
A) 2
B) 3
C) 5
D) 6
* A
Why: \((2-1)(3-1)=2\). Using the number of cells (6) inflates df and understates p.

Q11. Which test compares medians of two independent skewed samples?
A) Chi-square goodness of fit
B) Paired \(t\)-test
C) Mann–Whitney
D) One-sample \(t\)-test
* C
Why: Mann–Whitney is the rank-based two-sample test and does not require normality. The paired test needs matched observations.

Q12. A 95 % credible interval from a Bayesian analysis means
A) 95 % posterior probability that the parameter is in the interval
B) 95 % coverage over repeated samples
C) 95 % of observations lie in the interval
D) the prior is correct with probability 0.95
* A
Why: It is a direct posterior statement conditional on the model and prior. Coverage is the frequentist property.

Q13. With a Beta(2,2) prior and 6 successes in 10 trials, the posterior is
A) Beta(10,10)
B) Beta(8,6)
C) Beta(6,8)
D) Beta(2,2)
* B
Why: Add successes and failures to the prior parameters: Beta(2+6, 2+4) = Beta(8,6), mean 8/14.

Q14. Ridge regression differs from ordinary least squares by
A) using ranks
B) ignoring the residuals
C) adding a penalty on the sum of squared coefficients
D) removing the intercept
* C
Why: The penalty shrinks coefficients, trading bias for variance. It corresponds to a normal prior on the coefficients.

Q15. A confidence interval for a proportion with 8 successes in 20 observations should be computed
A) a \(t\) distribution with 19 df
B) a chi-square test
C) the usual normal approximation
D) an exact or Wilson method
* D
Why: Expected counts are small (8 and 12), so the normal approximation is unreliable. Exact or Wilson intervals maintain coverage.

Q16. Heteroscedasticity in a regression primarily invalidates
A) the residuals' mean
B) the sample size
C) the standard errors and tests
D) the fitted values
* C
Why: Unequal variance biases the estimated standard errors, so p-values and intervals are wrong. Point estimates remain unbiased under the usual conditions.

Q17. Which quantity is invariant to changing the units of both variables?
A) The slope
B) The correlation
C) The intercept
D) The residual variance
* B
Why: Correlation is unit-free. The slope scales with the ratio of units, and the intercept with \(y\)'s units.

Q18. A Bayesian analysis with a very informative prior and 5 observations will produce a posterior
A) the p-value
B) the prior
C) the data
D) neither
* B
Why: With little data, the prior's precision dominates the posterior. This is why prior sensitivity must be reported.

Q19. In a regression with a categorical predictor of 4 levels, the number of dummy variables is
A) 3
B) 5
C) 1
D) 4
* A
Why: One level is the reference, leaving \(k-1=3\) dummies. Using 4 creates perfect collinearity with the intercept.

Q20. A significant chi-square test in a \(3\times3\) table with 2,000 observations indicates
A) a strong association
B) some association, whose size must be assessed separately
C) causation
D) that the table is invalid
* B
Why: Significance is nearly guaranteed at this sample size; report Cramér's V or cell percentages to judge magnitude, and remember that association is not causation.
```

## Section B — Short answers (5 marks each)

**S1.** Explain the difference between a confidence interval and a prediction interval, and why
the latter is wider.

<details><summary>Model answer</summary>
A confidence interval quantifies uncertainty about the mean response at a given \(x\); a
prediction interval quantifies uncertainty about a single new observation. The latter adds the
observation's own variance \(\sigma^2\) to the variance of the fitted mean, so it is always wider
— often several times wider for small samples.
</details>

**S2.** Why does multiple testing require adjustment, and what does Bonferroni do?

<details><summary>Model answer</summary>
Each test at \(\alpha=0.05\) has a 5 % false-positive chance, so with \(m\) tests the chance of at
least one false positive rises toward 1. Bonferroni tests each hypothesis at \(\alpha/m\), which
keeps the family-wise error rate at or below \(\alpha\) at the cost of reduced power.
</details>

**S3.** State the assumptions of one-way ANOVA and one diagnostic for each.

<details><summary>Model answer</summary>
Independence of observations (check the design and residuals by group), approximate normality of
residuals (QQ plot or Shapiro–Wilk), and equal variances across groups (Levene's test or
residual plots). Violations suggest Welch's ANOVA, a transformation, or a rank-based test.
</details>

## Section C — Numerical problems (5–6 marks each)

**N1.** A sample of 36 gives mean 48 and \(s=9\). Compute the 95 % interval
(\(t_{0.975,35}\approx2.03\)).

<details><summary>Worked solution</summary>
\(\mathrm{SE}=9/6=1.5\); margin \(=2.03(1.5)=3.045\); interval \(44.96\) to \(51.04\).
</details>

**N2.** A test of \(H_0:\mu=100\) gives \(t=2.4\) with 24 df. Approximate the two-sided p-value and
state the decision at 5 %.

<details><summary>Worked solution</summary>
For 24 df the 5 % critical value is about 2.064 and the 1 % value about 2.797, so the p-value lies
between 0.02 and 0.05 (about **0.024**). Reject \(H_0\) at the 5 % level but not at 1 %.
</details>

**N3.** Regression output: \(\hat\beta_1=0.8\), \(\mathrm{SE}=0.25\), \(n=18\). Compute the
\(t\)-statistic, df and approximate 95 % interval.

<details><summary>Worked solution</summary>
\(t=0.8/0.25=3.2\) with 16 df; \(t_{0.975,16}\approx2.12\); interval
\(0.8\pm0.53=0.27\) to \(1.33\). The slope is clearly positive.
</details>

**N4.** Three groups give \(\mathrm{SSB}=84\) and \(\mathrm{SSW}=240\); each group has 9
observations. Compute \(F\), the df and \(\eta^2\).

<details><summary>Worked solution</summary>
\(\mathrm{MSB}=84/2=42\); \(\mathrm{MSW}=240/24=10\); \(F=4.2\) with \((2,24)\) df;
\(\eta^2=84/324=0.259\). The critical value at 5 % is about 3.40, so reject equality.
</details>

**N5.** A \(2\times2\) table has counts 18, 12, 22, 28. Compute the chi-square statistic and df.

<details><summary>Worked solution</summary>
Row totals 30 and 50; column totals 40 and 40; grand total 80. Expected: 15, 15, 25, 25.
Contributions: \(9/15=0.6\); \(9/15=0.6\); \(9/25=0.36\); \(9/25=0.36\). \(\chi^2=1.92\) with 1
df; p ≈ 0.17, no evidence of association.
</details>

**N6.** A Beta(1,1) prior is updated with 9 successes in 12 trials. Give the posterior mean, the
MAP, and a 95 % normal-approximation interval using the posterior SD.

<details><summary>Worked solution</summary>
Posterior Beta(10,4): mean \(10/14=0.714\); MAP \(9/12=0.75\). Posterior variance
\(=\frac{10\cdot4}{14^2\cdot15}=40/2940=0.01361\), SD \(=0.1167\); interval
\(0.714\pm1.96(0.1167)=0.486\) to \(0.943\) — wide because \(n\) is small.
</details>

## Section D — Scenario (6 marks each)

**P1.** A company tests a new pricing page with 3,000 visitors per arm and observes conversion
2.8 % versus 3.3 %. Compute an approximate test, state the decision at 5 %, and advise on
shipping.

<details><summary>Outline answer</summary>
\(\mathrm{SE}=\sqrt{0.028(0.972)/3{,}000+0.033(0.967)/3{,}000}\approx0.00429\);
\(z=0.005/0.00429=1.17\), p ≈ 0.24. Not significant. The 95 % interval for the difference is about
−0.0034 to 0.0134, so a meaningful lift is still possible; the test is underpowered for a 0.5-point
effect. Recommend extending the test or accepting the risk with monitoring, not shipping on this
evidence.
</details>

**P2.** A model predicting loan default reports AUC 0.71 on 5,000 loans, but the bank needs a
threshold for manual review. Explain what AUC does and does not tell them, and what analysis is
needed.

<details><summary>Outline answer</summary>
AUC measures ranking ability across all thresholds — the probability a random defaulter scores
higher than a random non-defaulter. It does not choose an operating point or reflect the costs of
false approvals versus false rejections. Needed: a cost-based threshold analysis, the confusion
matrix and expected loss at candidate thresholds, calibration of predicted probabilities, and
validation on a time-based holdout.
</details>

## Answer key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|
| 1 | C | 6 | B | 11 | B | 16 | A |
| 2 | D | 7 | B | 12 | A | 17 | B |
| 3 | D | 8 | A | 13 | A | 18 | A |
| 4 | A | 9 | A | 14 | A | 19 | B |
| 5 | D | 10 | B | 15 | B | 20 | B |

**Marking guide:** 70+ overall suggests readiness for the comprehensive paper. Below 50, revisit
Modules 14–16, where most lost marks concentrate.
