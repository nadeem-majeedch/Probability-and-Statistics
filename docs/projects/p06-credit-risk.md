# P06 · Financial risk and statistical modelling

**Level:** intermediate · **Suggested time:** 3 weeks · **Modules:** [M07](../modules/07-conditional-probability-and-bayes/chapter.md), [M15](../modules/15-hypothesis-testing/chapter.md), [M16](../modules/16-correlation-and-regression/chapter.md), [M18](../modules/18-bayesian-and-data-science-methods/chapter.md)

[Starter notebook](notebooks/p06_credit_risk.ipynb) ·
[Dataset](../data/projects/credit_risk_project.csv) ·
[Reference solution](solutions/p06-solution.md)

## Real-world background

A lender approves loans and loses money when borrowers default. The decision depends on a
probability, not on a yes/no test: the expected value of a loan is the probability of repayment
times the interest earned, minus the probability of default times the loss given default. A
model that ranks risk well but is badly calibrated will misprice every loan.

Regulation adds a second requirement: the lender must be able to explain why an applicant was
declined. That rules out opaque scores and makes the odds ratio — the language of logistic
regression — the working vocabulary of the credit analyst.

## Problem statement

Using 2,000 historical loans, model the probability of default as a function of credit score,
debt-to-income ratio, term and income, evaluate the model's discrimination and calibration, and
recommend an approval cut-off given stated profit and loss figures.

## Learning objectives

1. Estimate and interpret default rates with intervals.
2. Fit a logistic regression and convert coefficients to odds ratios with intervals.
3. Distinguish discrimination (AUC) from calibration.
4. Evaluate a score band as a pricing tool.
5. Compute expected value per loan and choose a cut-off from costs.
6. Discuss fairness, omitted variables and the limits of observational credit data.

## Dataset

`docs/data/projects/credit_risk_project.csv` — 2,000 loans, 8 columns, simulated.

## Dataset description

| Column | Type | Description |
|---|---|---|
| `loan_id` | identifier | Loan reference |
| `credit_score` | integer | 320–850 |
| `annual_income` | integer | Borrower income |
| `loan_amount` | integer | Amount advanced |
| `term_months` | categorical | 12, 24, 36, 48, 60 |
| `dti_pct` | numeric | Debt-to-income ratio at origination |
| `region` | categorical | urban, semi-urban, rural |
| `defaulted` | binary | 1 if the loan defaulted |

The simulation makes default more likely at lower scores and higher DTI, with income protective.
Term and region are included: one has a near-null effect, and part of the exercise is not
inventing a story for it.

## Research questions

1. What is the default rate, with a 95 % interval?
2. How do defaulters and non-defaulters differ on score, DTI and income?
3. What is the effect of a 50-point increase in credit score on the odds of default, holding
   other variables fixed?
4. How well does the model discriminate (AUC), and is it calibrated?
5. What default rate is observed in each score band, and how precise are those rates?
6. Given a profit of 3,000 on a performing loan and a loss of 20,000 on a default, where should
   the approval cut-off sit?

## Statistical methods required

- Proportions with intervals; comparison of group means with effect sizes.
- Logistic regression; odds ratios and their intervals; likelihood-ratio test.
- ROC curve and AUC; calibration by score band.
- Expected-value calculation from estimated probabilities.
- Optional: Bayesian updating of a band's default rate with a Beta prior.

## Mathematical concepts

- Logistic model \(\log\frac{p}{1-p}=\beta_0+\beta_1x_1+\cdots\).
- Odds ratio \(e^{\beta_j}\); for a \(c\)-unit change, \(e^{c\beta_j}\).
- Expected value per loan \(=p_{\text{repay}}\cdot G-p_{\text{default}}\cdot L\).
- AUC as \(P(\text{score}_{\text{defaulter}}<\text{score}_{\text{non-defaulter}})\) when lower
  scores mean higher risk.
- Interval for a proportion and for an odds ratio via the log scale.

## Step-by-step tasks

1. **Audit.** Check ranges, duplicated ids, and whether income or loan amount has impossible
   values. Note the skew of income.
2. **Describe.** Report the default rate with an interval, and summarise the predictors by
   default status.
3. **Compare.** Test the group differences and report standardised effect sizes; do not rely on
   p-values alone.
4. **Model.** Fit the logistic regression; report odds ratios with 95 % intervals and interpret
   the score effect per 50 points.
5. **Discrimination.** Compute the ROC curve and AUC. Explain what the AUC does not tell the
   lender.
6. **Calibration.** Group by score band, report observed default rates with intervals, and check
   whether the model's predicted rates match.
7. **Decision.** Compute expected value per loan by band and choose a cut-off. Show the
   sensitivity of the choice to the loss assumption.
8. **Fairness.** Discuss which variables are missing, which could act as proxies, and what you
   would report to a regulator.

## Python implementation requirements

- `pandas`, `numpy`, `matplotlib`.
- `statsmodels.formula.api.logit` with `.params`, `.conf_int()`, `.predict()`.
- `sklearn.metrics.roc_curve` and `roc_auc_score`.
- Binned calibration computed from the data (no hard-coded rates).
- Every expected-value calculation visible in code.

## Expected visualizations

| Figure | What it must show |
|---|---|
| Default rate by score band with intervals | The monotone risk gradient and its precision |
| Score distributions by outcome | Overlap — why no cut-off is perfect |
| ROC curve | Discrimination with the chosen cut-off marked |
| Calibration plot | Predicted vs observed default rate |
| Expected value by band | The economic cut-off and its sensitivity |

## Interpretation requirements

- Odds ratios are interpreted as multiplicative changes in odds, not probability.
- AUC is described as a ranking measure and explicitly not a pricing rule.
- The cut-off recommendation names the assumed loss and shows how it moves the answer.
- Causation is not claimed: the model is a risk association, and a declined applicant's
  counterfactual is unobserved.
- One limitation paragraph: selection bias (only approved loans are observed), omitted
  variables, and the fairness implications of proxy variables.

## Deliverables

1. Executed notebook.
2. A four-page credit risk report with model table, ROC, calibration and cut-off analysis.
3. A one-page policy memo with the recommended cut-off and the economic assumptions.
4. A fairness and limitations statement.

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Audit and description | 10 | Skew and ranges handled; rate with interval |
| Logistic model | 25 | Correct specification; odds ratios with intervals; interpretation |
| Discrimination and calibration | 25 | Both assessed; the difference explained |
| Economic decision | 20 | Expected value computed; cut-off justified; sensitivity shown |
| Fairness and limitations | 10 | Specific, not generic |
| Communication | 10 | Report is decision-oriented and honest |

## Extension challenges

1. **Bayesian band estimate.** With a Beta(2,2) prior, update each band's default rate and
   compare the posterior intervals with the frequentist ones. Which bands shrink most?
2. **Threshold sensitivity.** Plot the optimal cut-off as the loss given default varies from
   5,000 to 40,000. Where does the recommendation change?
3. **Interactions.** Test whether the effect of DTI differs by score band. Interpret the
   interaction and its policy implication.
4. **Reject inference.** Suppose the data only contain approved loans. Explain how the estimated
   default rate is biased and what reject inference attempts to do.
5. **Model comparison.** Add region and term, compare AIC, and explain why a more complex model
   is not automatically better for a regulated decision.
