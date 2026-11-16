# Integrated data-science problem-solving assessment

**Covers:** the whole course, applied. **Time:** 120 minutes. **Total:** 100 marks.
**Instructions:** open book (notes and the course pages), but no communication and no AI
assistants. Every question is about a decision, not a formula. Show your reasoning.

| Section | Items | Marks | Suggested time |
|---|---|---|---|
| A. Multiple choice | 20 | 40 | 25 min |
| B. Short answers | 4 | 16 | 20 min |
| C. Numerical | 6 | 24 | 35 min |
| D. Scenario | 3 | 20 | 40 min |

## Section A — Multiple choice (2 marks each)

```quiz
Q1. For a fraud model with 0.2 % positives, the most informative headline metric is
A) accuracy
B) precision–recall AUC
C) \(R^2\)
D) mean squared error
* B
Why: PR-AUC focuses on the positive class and is not inflated by the vast negative majority, unlike accuracy or ROC-AUC in extreme imbalance.

Q2. Fitting a scaler on the full dataset before splitting into train and test causes
A) no problem
B) data leakage that inflates test performance
C) underfitting
D) a smaller sample
* B
Why: The test set's statistics influence preprocessing, so information leaks from test to train; fit transforms on training data only.

Q3. For a time series forecast, the correct validation scheme is
A) leave-one-out
B) random k-fold cross-validation
C) a rolling-origin or forward-chaining split
D) bootstrap resampling of rows
* C
Why: Random splits let the model see the future, which is unavailable in deployment. Forward chaining mirrors real forecasting.

Q4. A model is calibrated when
A) its features are standardised
B) its predicted probabilities match observed frequencies
C) its AUC is above 0.7
D) it has high accuracy
* B
Why: Calibration is about the meaning of the score as a probability; a model can rank well yet be systematically overconfident.

Q5. The decision threshold for a classifier should be chosen from
A) the relative costs of false positives and false negatives
B) the AUC maximum
C) the training accuracy
D) 0.5 always
* A
Why: The economically optimal threshold depends on the loss ratio, the base rate and the capacity to act on flags.

Q6. Training accuracy 0.99 with test accuracy 0.72 indicates
A) leakage
B) calibration
C) underfitting
D) overfitting
* D
Why: A large train–test gap is the signature of memorising the training sample. Regularisation, more data or a simpler model would help.

Q7. Running 20 variants of an experiment and reporting the best at \(p<0.05\) inflates
A) power
B) the false-positive rate
C) the sample size
D) the effect size
* B
Why: With 20 independent tests, the chance of at least one false positive is about 64 %. Pre-register one primary metric or correct for multiplicity.

Q8. A guardrail metric in an experiment is used to
A) increase traffic
B) reduce the sample size
C) detect harm to other important outcomes even if the primary metric improves
D) replace the primary metric
* C
Why: Guardrails (latency, refunds, churn) bound collateral damage; a win on clicks that raises refunds is not a win.

Q9. A model looks better overall but worse in every customer segment. This is
A) heteroscedasticity
B) multicollinearity
C) Simpson's paradox
D) overfitting
* C
Why: Aggregation over segments with different sizes and base rates can reverse the comparison; evaluate per segment.

Q10. Multiple imputation is preferred to mean imputation because it
A) preserves variability and reflects imputation uncertainty
B) is faster
C) requires no assumptions
D) removes missing rows
* A
Why: Mean imputation shrinks variance and distorts relationships; multiple imputation produces several plausible datasets and pools the results.

Q11. A 95 % prediction interval for next month's revenue is wider than a confidence interval for
A) revenue is always skewed
B) it includes month-to-month variability
C) the sample is smaller
D) the model is biased
* B
Why: A single future month has its own noise on top of estimation uncertainty; the interval must cover both.

Q12. L2 regularisation is used mainly to
A) increase training accuracy
B) remove the intercept
C) make features independent
D) reduce variance at the cost of some bias
* D
Why: Shrinking coefficients stabilises estimates and improves generalisation, especially with many correlated predictors.

Q13. A model trained on last year's customers is deployed to a new market. The main risk is
A) distribution shift
B) excessive sample size
C) perfect calibration
D) too few features
* A
Why: The relationship and feature distributions differ, so performance degrades; monitor inputs and outcomes and revalidate.

Q14. To estimate the effect of a promotion on spending, a predictive model of spending is
A) insufficient, because prediction is not causation
B) better than an experiment
C) equivalent to a randomised trial
D) sufficient
* A
Why: A predictive model captures associations, including confounding. Causal claims need a design — randomisation, or explicit assumptions with adjustment.

Q15. The bootstrap is useful for a business metric because it
A) increases the sample size
B) removes outliers
C) proves causation
D) gives an interval without assuming normality
* D
Why: Resampling estimates the metric's sampling distribution, which is valuable for ratios, medians and percentile-based metrics.

Q16. Response times spanning three orders of magnitude are best summarised on
A) a pie chart
B) a cumulative count
C) a linear scale
D) a log scale
* D
Why: A log scale makes multiplicative differences visible and prevents the largest values from dominating the display; report the median and high percentiles.

Q17. A high correlation between a feature and the target does not guarantee that the feature is
A) the target may be categorical
B) features must be normally distributed
C) the relationship may be non-linear or confounded, and may not hold out of sample
D) correlation is always zero
* C
Why: Correlation is a marginal, linear summary of the training sample; usefulness depends on incremental information and stability.

Q18. When comparing models with different numbers of parameters, prefer
A) the largest \(R^2\)
B) the smallest sample
C) the model with most features
D) adjusted \(R^2\) or AIC rather than raw \(R^2\)
* D
Why: These criteria penalise complexity, preventing the automatic selection of overfitted models.

Q19. Grouped cross-validation is needed when
A) the target is continuous
B) features are standardised
C) the same customer appears in several rows
D) the dataset is small
* C
Why: Random folds would put the same customer in train and test, leaking information and overstating performance.

Q20. A dashboard shows a metric improving while its confidence interval widens. The correct
A) the improvement is uncertain and may be noise
B) the improvement is proven
C) the metric is broken
D) the sample doubled
* A
Why: A widening interval signals less precision; point estimates alone should not drive decisions.
```

## Section B — Short answers (4 marks each)

**S1.** Explain the difference between a model that ranks well and a model that is well
calibrated, and why a bank needs both.

<details><summary>Model answer</summary>
Ranking (AUC) says how well the model orders cases by risk; calibration says whether a score of
0.2 corresponds to roughly 20 % observed default. A bank needs ranking to prioritise reviews and
calibration to price loans, set provisions and compute expected losses from the predicted
probabilities.
</details>

**S2.** Why can a feature that improves offline accuracy harm a deployed system?

<details><summary>Model answer</summary>
It may be unavailable or delayed at prediction time, may leak future information, may not be
stable across populations, or may encode a proxy for a protected attribute. Offline accuracy also
ignores operational costs and feedback loops. Validate availability, stability and fairness before
deployment.
</details>

**S3.** Describe how you would choose between a simpler and a more complex model for a production
system.

<details><summary>Model answer</summary>
Compare out-of-sample performance with proper validation (grouped or time-based), check
calibration, then weigh interpretability, latency, maintenance and failure modes. Prefer the
simpler model when performance is close; a small accuracy gain rarely justifies substantial
operational risk.
</details>

**S4.** Why is a 0.05 p-value threshold not a decision rule in a business context?

<details><summary>Model answer</summary>
Because decisions depend on effect size, costs and uncertainty. A significant but tiny lift may
not repay implementation costs, and an imprecise estimate may include large losses. Decision rules
should combine the estimated effect, its interval and the loss function.
</details>

## Section C — Numerical problems (4 marks each)

**N1.** A classifier gives TP = 100, FP = 50, FN = 30, TN = 820. Compute precision, recall,
accuracy and F1.

<details><summary>Worked solution</summary>
Precision \(=100/150=0.667\); recall \(=100/130=0.769\); accuracy
\(=(100+820)/1{,}000=0.92\); F1 \(=2(0.667)(0.769)/(0.667+0.769)=0.714\). Accuracy looks
excellent while 30 of 130 positives are missed.
</details>

**N2.** A model flags 2,000 transactions with 70 % precision. Each true fraud saves 300; each
false flag costs 20 in review. Compute the net benefit.

<details><summary>Worked solution</summary>
True flags \(=1{,}400\) → \(1{,}400\times300=420{,}000\). False flags \(=600\) →
\(600\times20=12{,}000\). Net \(=408{,}000\). The high precision justifies reviewing all
flagged cases.
</details>

**N3.** A test has sensitivity 0.85 and specificity 0.93 at 6 % prevalence. Compute the PPV and
the false-omission rate among positives.

<details><summary>Worked solution</summary>
Per 10,000: 600 diseased → 510 positive; 9,400 healthy → 658 false positives. PPV
\(=510/1{,}168=0.437\). False omission rate \(=1-\mathrm{NPV}\): true negatives 8,742, total
negatives 8,832, so NPV \(=0.9898\) and the omission rate is **0.0102**.
</details>

**N4.** Baseline conversion is 5 % and you want to detect a 10 % relative lift at 80 % power and
5 % significance. Using
\(n=2(z_{0.975}+z_{0.8})^2\bar p(1-\bar p)/\Delta^2\) with \(\bar p=0.0525\) and
\(\Delta=0.005\), estimate the sample size per arm.

<details><summary>Worked solution</summary>
\((1.96+0.8416)^2=7.849\); \(2\times7.849\times0.0525\times0.9475=0.7808\); divided by
\(0.005^2=0.000025\) gives \(31{,}235\), so about \(31{,}300\) per arm.
</details>

**N5.** A churn model assigns 500 customers a predicted probability of 0.20; 90 churn. Comment on
calibration and compute the ratio of observed to predicted.

<details><summary>Worked solution</summary>
Observed rate \(=90/500=0.18\) versus predicted 0.20, a ratio of **0.90** — the model is
slightly over-predicting churn in this bin. Calibration curves across bins would show whether the
error is systematic.
</details>

**N6.** A bootstrap gives a 95 % interval for uplift of (−0.4 %, 3.1 %) with a point estimate of
1.3 %. State the decision-theoretic reading.

<details><summary>Worked solution</summary>
The interval includes zero, so a null or slightly harmful effect is compatible with the data. The
expected uplift is 1.3 %, but the downside risk is 0.4 %; a risk-averse decision would extend the
test, while a risk-neutral one would weigh 1.3 % against rollout cost and the probability of harm
(about 2.5 % below zero under the bootstrap distribution).
</details>

## Section D — Scenario (7 marks each)

**P1.** A retailer's churn model has AUC 0.81 offline, but in production the churn rate doubles and
precision collapses. Diagnose and propose a response.

<details><summary>Outline answer</summary>
Likely causes: distribution shift (customer mix, seasonality, a competitor launch), label delay or
definition change, leakage in the offline evaluation, or a feedback loop from retention offers.
Diagnose by comparing feature distributions over time, checking calibration by month, and
reviewing the label pipeline. Respond with monitoring and alerts, recalibration, retraining on
recent data with time-based validation, and a threshold review based on capacity.
</details>

**P2.** A team proposes shipping a recommendation model because offline NDCG improved by 3 %. What
evidence would you require before rollout?

<details><summary>Outline answer</summary>
Online A/B evidence on the business metric with a pre-registered analysis, guardrails on latency,
diversity and satisfaction, a check that the offline improvement used a time-based split without
leakage, segment-level results, and an estimate of the revenue effect against serving cost.
Offline gains often fail to transfer because the offline metric and the live objective differ.
</details>

**P3.** A hospital asks you to rank departments by mortality to target inspections. Design the
analysis and state its limits.

<details><summary>Outline answer</summary>
Risk-adjust for age, comorbidity and admission severity; model mortality with a hierarchical
structure so small departments shrink toward the mean; report adjusted rates with intervals and
apply multiplicity control before flagging. Limits: unmeasured severity, coding differences,
small numbers, and the risk that inspection targets gaming. Present uncertainty and avoid
labelling departments on a single year.
</details>

## Answer key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|
| 1 | B | 6 | B | 11 | A | 16 | B |
| 2 | B | 7 | B | 12 | A | 17 | A |
| 3 | C | 8 | A | 13 | A | 18 | A |
| 4 | B | 9 | A | 14 | B | 19 | A |
| 5 | A | 10 | A | 15 | A | 20 | A |
