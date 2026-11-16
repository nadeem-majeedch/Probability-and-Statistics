# Comprehensive final examination

**Covers:** Modules 01–18. **Time:** 150 minutes. **Total:** 150 marks.
**Instructions:** closed book; calculator allowed. Sections A–D are compulsory. The answer key is
at the end; do not turn to it before finishing.

| Section | Items | Marks | Suggested time |
|---|---|---|---|
| A. Multiple choice | 25 | 50 | 40 min |
| B. Short answers | 4 | 20 | 25 min |
| C. Numerical | 7 | 49 | 55 min |
| D. Scenario | 3 | 21 | 30 min |

## Section A — Multiple choice (2 marks each)

```quiz
Q1. The same 30 patients are measured before and after treatment. The appropriate test compares
A) three or more means
B) two proportions
C) two independent means
D) paired differences
* D
Why: Measuring the same units twice creates dependence, and analysing differences removes between-patient variability, increasing power.

Q2. "p-hacking" refers to
A) testing many hypotheses and reporting only significant results
B) using a calculator incorrectly
C) increasing the sample size
D) correcting for multiple comparisons
* A
Why: Selective reporting inflates the false-positive rate. Pre-registration and multiplicity control are the remedies.

Q3. Cross-validation is used to
A) estimate out-of-sample performance
B) increase the sample size
C) remove outliers
D) compute a p-value
* A
Why: Repeatedly holding out data estimates how the model performs on unseen observations and exposes overfitting.

Q4. With 1 % positives, a classifier with 99 % accuracy may be
A) unbiased
B) excellent at detecting positives
C) no better than predicting "negative" always
D) perfectly calibrated
* C
Why: Predicting the majority class achieves 99 % accuracy while detecting nothing; use precision, recall or PR-AUC.

Q5. Precision is
A) TP/(TP+FN)
B) TN/(TN+FP)
C) (TP+TN)/total
D) TP/(TP+FP)
* D
Why: Precision is the share of flagged cases that are correct; TP/(TP+FN) is recall, and TN/(TN+FP) is specificity.

Q6. AUC of 0.5 indicates
A) inverted ranking
B) perfect calibration
C) perfect ranking
D) chance-level ranking
* D
Why: A random score ranks a positive above a negative half the time. AUC is about ranking, not calibration.

Q7. A log transformation of a right-skewed positive variable
A) removes the mean
B) guarantees normality
C) compresses large values and stabilises relative variation
D) makes the data discrete
* C
Why: Logs turn multiplicative differences into additive ones, reducing skew and stabilising variance. Normality is often improved but not guaranteed.

Q8. Data missing completely at random means
A) missingness is unrelated to any variable
B) missingness depends on the outcome
C) missingness depends on observed variables only
D) the data are invalid
* A
Why: MCAR means the missingness mechanism is independent of everything. MAR depends on observed variables; MNAR depends on the unobserved value itself.

Q9. A trend appears in every hospital but reverses when hospitals are combined. This is
A) regression to the mean
B) heteroscedasticity
C) Simpson's paradox
D) a Type I error
* C
Why: Aggregation reverses the conditional association, usually because of confounding by case mix or group size.

Q10. Before computing distances between features measured in different units, you should
A) take logarithms only
B) remove the mean only
C) rank them
D) standardise them
* D
Why: Distance metrics weight large-scale features more heavily; standardising puts them on a common scale so each contributes comparably.

Q11. A 95 % interval for a mean is 4 units wide with \(n=100\). To make it 2 units wide, you need
A) 50 observations
B) 1,000 observations
C) 200 observations
D) 400 observations
* D
Why: Width scales as \(1/\sqrt n\), so halving it needs \(2^2=4\) times the data.

Q12. Raising the significance threshold from 0.05 to 0.10, all else fixed
A) leaves both unchanged
B) increases the Type I error rate and power
C) decreases both
D) increases power only
* B
Why: A looser threshold rejects more often, so both false positives and true detections increase.

Q13. A correlation of zero between two variables implies
A) no linear association
B) a non-linear relationship
C) equal means
D) independence
* A
Why: Correlation measures linear association only; a strong curved relationship can have zero correlation.

Q14. In a multiple regression, a coefficient of 2.5 for experience means
A) experience causes a 2.5-unit increase
B) a one-unit increase in experience is associated with a 2.5-unit increase, holding other predictors fixed
C) the correlation is 2.5
D) \(R^2\) is 2.5
* B
Why: The coefficient is a partial association conditional on the other variables, and it does not by itself establish causation.

Q15. ANOVA is preferred to several pairwise \(t\)-tests because it
A) works with unequal variances automatically
B) estimates the medians
C) controls the family-wise error rate
D) requires no assumptions
* C
Why: A single omnibus test avoids the multiplicity inflation of repeated pairwise tests. Post-hoc procedures then localise differences.

Q16. A chi-square test of independence is unreliable when
A) the variables are nominal
B) many expected counts are below 5
C) the sample is large
D) the table is \(2\times2\)
* B
Why: Sparse cells invalidate the chi-square approximation; combine categories or use an exact test.

Q17. In Bayesian inference, a prior that is very concentrated relative to the data
A) dominates the posterior
B) is equivalent to a flat prior
C) makes the likelihood irrelevant
D) has little influence
* A
Why: High prior precision outweighs limited data. Report prior sensitivity when the posterior depends on it.

Q18. The bootstrap is least reliable for
A) a median
B) the sample mean
C) the sample maximum
D) a correlation
* C
Why: Resampling cannot produce values beyond the observed maximum, so the bootstrap distribution of the maximum is degenerate at the top observation.

Q19. For a fixed effect, power increases with
A) larger sample size
B) larger variance
C) smaller effect size
D) a stricter alpha
* A
Why: More data reduce the standard error. Larger variance, smaller effects and stricter alpha all reduce power.

Q20. The interquartile range measures
A) the distance from mean to median
B) the spread of the middle half of the data
C) the full range
D) the average deviation
* B
Why: It is \(Q_3-Q_1\), unaffected by extreme values, which is why it accompanies the median for skewed data.

Q21. Count data with variance far exceeding the mean are better modelled by
A) negative binomial
B) binomial
C) uniform
D) Poisson
* A
Why: Over-dispersion violates the Poisson's mean-equals-variance property; the negative binomial adds a dispersion parameter.

Q22. A 95 % prediction interval for a regression is wider than the confidence interval for the mean
A) it uses a lower confidence level
B) the sample is smaller
C) residuals are ignored
D) it accounts for individual observation noise as well as estimation uncertainty
* D
Why: Prediction variance adds \(\sigma^2\) to the variance of the fitted mean, and the gap widens away from the centre of the data.

Q23. An online poll of self-selected respondents most likely suffers from
A) measurement error only
B) no bias if the sample is large
C) non-response and selection bias
D) sampling error only
* C
Why: Volunteers differ systematically from the population, and a large self-selected sample is precisely wrong rather than imprecise.

Q24. A regression's residual plot shows a clear U-shape. This suggests
A) the slope is zero
B) the linear model is misspecified
C) the residuals are normal
D) the variance is constant
* B
Why: Systematic curvature in the residuals means the mean function is wrong; add polynomial terms or transform variables.

Q25. A credible interval and a confidence interval computed from the same data with a flat prior
A) always differ substantially
B) often be numerically close but differently interpreted
C) be identical in interpretation
D) have different centres
* B
Why: With little prior information the posterior is likelihood-shaped, so the numbers agree; the interpretations — posterior probability versus repeated-sampling coverage — do not.
```

## Section B — Short answers (5 marks each)

**S1.** Explain why a statistically significant result can be practically unimportant, and how you
would report it properly.

<details><summary>Model answer</summary>
Significance asks whether an effect is distinguishable from zero; with large samples even trivial
effects produce small p-values. Report the effect size with a confidence interval, state the
practical threshold that matters, and discuss the decision consequences. A precise estimate of a
tiny effect is a valid result, just not an important one.
</details>

**S2.** Distinguish MCAR, MAR and MNAR, and explain the consequence for imputation.

<details><summary>Model answer</summary>
MCAR: missingness is independent of all variables, so complete-case analysis is unbiased though
wasteful. MAR: missingness depends on observed variables, so multiple imputation or model-based
methods can correct it. MNAR: missingness depends on the unobserved value, which no standard
method identifies without assumptions; sensitivity analysis is required.
</details>

**S3.** Why is accuracy a poor metric for imbalanced classification, and what would you use
instead?

<details><summary>Model answer</summary>
Because the majority class dominates: predicting "negative" always can yield 99 % accuracy while
detecting nothing. Use precision, recall, F1 or PR-AUC, report the confusion matrix at the chosen
threshold, and evaluate expected cost, which reflects the asymmetric price of errors.
</details>

**S4.** Explain what overfitting is, how it is detected, and two ways to reduce it.

<details><summary>Model answer</summary>
Overfitting is fitting noise in the training sample, so performance is much better in-sample than
out-of-sample. Detect it with a holdout or cross-validation gap. Reduce it with regularisation,
simpler models, more data, or early stopping — all of which trade some training fit for
generalisation.
</details>

## Section C — Numerical problems (7 marks each)

**N1.** A sample of 25 gives mean 62 and \(s=10\). Compute the 95 % interval
(\(t_{0.975,24}=2.064\)) and state whether \(\mu=58\) is plausible.

<details><summary>Worked solution</summary>
\(\mathrm{SE}=2\); margin \(=2.064(2)=4.128\); interval \(57.87\) to \(66.13\). The value 58
lies just inside the interval, so it is plausible at the 5 % level.
</details>

**N2.** A screening test has sensitivity 0.88, specificity 0.94 and prevalence 4 %. Compute the PPV
and the number needed to screen to find one true case among positives.

<details><summary>Worked solution</summary>
Per 100,000: 4,000 diseased → 3,520 positive; 96,000 healthy → 5,760 false positives. PPV
\(=3{,}520/9{,}280=0.379\). About \(1/0.379=2.64\) positives are examined per true case.
</details>

**N3.** \(X\sim\mathrm{Poisson}(2)\). Compute \(P(X=3)\), \(P(X\ge2)\) and the probability of
exactly one event in a 30-minute window if the rate is 2 per hour.

<details><summary>Worked solution</summary>
\(P(3)=e^{-2}8/6=0.1804\). \(P(\ge2)=1-P(0)-P(1)=1-0.1353-0.2707=0.5940\). For 30 minutes,
\(\lambda=1\), so \(P(1)=e^{-1}=0.3679\).
</details>

**N4.** A regression of \(y\) on \(x\) gives \(\hat y=12+1.8x\) with \(s_e=3.2\), \(n=20\),
\(\bar x=10\), \(S_{xx}=500\). Compute the prediction at \(x=12\) and an approximate 95 %
prediction interval.

<details><summary>Worked solution</summary>
\(\hat y=12+1.8(12)=33.6\). Prediction variance
\(s_e^2[1+1/n+(x-\bar x)^2/S_{xx}]=10.24[1+0.05+4/500]=10.24(1.058)=10.83\), SE \(=3.29\).
With \(t_{0.975,18}=2.101\): \(33.6\pm6.91=26.69\) to \(40.51\).
</details>

**N5.** An A/B test has 8,000 users per arm, conversion 6.0 % versus 6.8 %. Compute the standard
error of the difference, the z-statistic and the two-sided p-value.

<details><summary>Worked solution</summary>
\(\mathrm{SE}=\sqrt{0.06(0.94)/8000+0.068(0.932)/8000}=\sqrt{0.00000705+0.00000792}=0.00387\).
\(z=0.008/0.00387=2.07\), two-sided p \(\approx0.038\). Significant at 5 %, though the
interval only just excludes zero.
</details>

**N6.** A one-way ANOVA on four groups of 10 gives \(\mathrm{SSB}=150\), \(\mathrm{SSW}=360\).
Compute \(F\), the df, \(\eta^2\) and the decision at 5 % (critical value ≈ 2.87).

<details><summary>Worked solution</summary>
\(\mathrm{MSB}=50\), \(\mathrm{MSW}=10\), \(F=5.0\) with \((3,36)\) df. Since
\(5.0>2.87\), reject equality. \(\eta^2=150/510=0.294\): about 29 % of variance is
between groups.
</details>

**N7.** A Beta(3,3) prior is updated with 8 successes and 4 failures. Give the posterior, its
mean, and the posterior predictive probability of success on the next trial.

<details><summary>Worked solution</summary>
Posterior Beta(11,7); mean \(11/18=0.611\). Predictive
\(=(\alpha+k)/(\alpha+\beta+n)=11/18=0.611\), the same as the posterior mean for a Bernoulli
model.
</details>

## Section D — Scenario (7 marks each)

**P1.** A bank's default model has AUC 0.78. Approval at score below 0.5 rejects 12 % of
applicants, of whom 35 % would have defaulted. The bank earns 2,000 on a good loan and loses 12,000
on a default. Using the 1,000-applicant illustration, compute the expected value of the rejected
group and advise.

<details><summary>Outline answer</summary>
Of 120 rejected, 35 % would default: 42 defaults avoided at 12,000 each (504,000 saved) and 78 good
customers lost at 2,000 each (156,000 forgone). Net benefit of the rule ≈ 348,000 per 1,000
applicants, before review costs. Check the threshold against costs at the margin — lower
thresholds reject more good applicants — and validate on a time-based holdout before adopting.
</details>

**P2.** An analyst reports that a new feature increases average order value by 4 %, based on 900
users, with a 95 % interval of (0.5 %, 7.5 %). The finance team asks whether to fund the rollout.
What analysis and caveats do you give?

<details><summary>Outline answer</summary>
The interval excludes zero but the lower bound is small, so the expected benefit may not cover
build and maintenance costs. Compute the revenue impact from the interval (worst and best case),
check guardrails (conversion, refunds, latency), verify randomisation balance and novelty effects,
and confirm the metric was pre-specified. Recommend a phased rollout with monitoring rather than a
full commitment on a single test.
</details>

**P3.** A hospital wants to compare readmission rates across 12 departments and flag the worst
three for review. Explain why raw rates are misleading and outline a fairer analysis.

<details><summary>Outline answer</summary>
Departments differ in case mix and volume: small units have noisy rates that fluctuate into the
"worst" group by chance, and complex patients raise readmission risk legitimately. Use a
risk-adjusted model (age, comorbidity, admission severity) with shrinkage for small units, compare
each department's adjusted rate against the overall with intervals, and apply multiplicity control
before flagging. Report uncertainty alongside rankings.
</details>

## Answer key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|---|---|
| 1 | D | 6 | B | 11 | B | 16 | A | 21 | B |
| 2 | A | 7 | A | 12 | A | 17 | B | 22 | A |
| 3 | A | 8 | A | 13 | B | 18 | B | 23 | A |
| 4 | C | 9 | A | 14 | B | 19 | A | 24 | A |
| 5 | D | 10 | A | 15 | A | 20 | A | 25 | B |

**Marking guide:** 105/150 (70 %) is a comfortable pass; below 75 indicates that the inference
modules (14–17) need another pass before the applied project.
