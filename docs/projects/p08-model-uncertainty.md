# P08 · Machine learning prediction uncertainty and model evaluation

**Level:** advanced · **Suggested time:** 3 weeks · **Modules:** [M07](../modules/07-conditional-probability-and-bayes/chapter.md), [M15](../modules/15-hypothesis-testing/chapter.md), [M16](../modules/16-correlation-and-regression/chapter.md), [M18](../modules/18-bayesian-and-data-science-methods/chapter.md)

[Starter notebook](notebooks/p08_model_uncertainty.ipynb) ·
[Dataset](../data/projects/model_uncertainty_project.csv) ·
[Reference solution](solutions/p08-solution.md)

## Real-world background

Two versions of a churn model are in production. Version 2 was retrained and has a better Brier
score; version 1 has a slightly higher AUC. The product team wants to know which to keep, and
the answer depends on what the scores are used for. If they rank customers for a limited
retention budget, ranking matters; if they decide who receives an offer costing money, the
probability must mean what it says.

This is the difference between discrimination and calibration, and it is where most applied
machine-learning evaluations go wrong.

## Problem statement

Using 2,400 scored cases from two model versions, evaluate discrimination and calibration
overall and by segment, quantify how far each version's probabilities are from the observed
rates, choose an operating threshold for a retention offer, and recommend which version to
deploy. The evaluation must be honest about what a single holdout can and cannot establish.

## Learning objectives

1. Compute and interpret the Brier score and its decomposition into calibration and refinement.
2. Build and read a reliability diagram.
3. Distinguish ranking (AUC) from calibration.
4. Evaluate calibration within segments and identify where a model is over-confident.
5. Choose a threshold from the consequences of false positives and false negatives.
6. Explain why accuracy is misleading for imbalanced outcomes.
7. Write an evaluation that a product owner can act on.

## Dataset

`docs/data/projects/model_uncertainty_project.csv` — 2,400 cases, 6 columns, simulated.

## Dataset description

| Column | Type | Description |
|---|---|---|
| `case_id` | identifier | Scored case |
| `segment` | categorical | new, casual, loyal, at_risk |
| `model_version` | categorical | v1 or v2 |
| `predicted_prob` | numeric | Model score in [0, 1] |
| `outcome` | binary | Whether the event occurred |
| `feature_drift` | numeric | Standardised drift of the top feature |

Version 1 is systematically over-confident; version 2 is calibrated. Both rank similarly, which
is the point: a model can be good at ordering and bad at probabilities.

## Research questions

1. What is the base rate of the outcome, and what does a trivial "always predict the majority"
   model achieve?
2. How do the two versions compare on Brier score, log loss and AUC?
3. Where is each version miscalibrated, and by how much?
4. Which segment has the largest over-confidence, and what would that mean operationally?
5. At a threshold of 0.4, what proportion is flagged, and what is the precision of the flagged
   group in each version?
6. Which version should be deployed, and what monitoring would you put in place?

## Statistical methods required

- Proportions with intervals; confusion matrices at chosen thresholds.
- Brier score, log loss, and AUC.
- Reliability diagram with binned predicted vs observed rates and intervals.
- Calibration slope (regression of outcome on the logit of the prediction).
- Subgroup analysis with multiplicity caution.
- Optional: bootstrap intervals for the difference in Brier score.

## Mathematical concepts

- Brier score \(\frac1n\sum(\hat p_i-y_i)^2\); lower is better, 0.25 for a constant 0.5
  predictor with a 50 % base rate.
- Log loss \(-\frac1n\sum[y_i\log\hat p_i+(1-y_i)\log(1-\hat p_i)]\).
- Calibration: \(E[Y\mid \hat p=p]=p\).
- Calibration slope from \(\mathrm{logit}(P(Y=1))=\alpha+\beta\,\mathrm{logit}(\hat p)\);
  \(\beta=1\) is perfect, \(\beta<1\) indicates over-confidence.
- AUC as a rank statistic, unaffected by monotone transformations of the score.

## Step-by-step tasks

1. **Audit.** Confirm the score range, the version split and the outcome rate. Check for
   duplicate case ids.
2. **Baseline.** Compute the majority-class accuracy and the Brier score of a constant predictor.
   Explain why accuracy is a poor headline.
3. **Overall metrics.** Compute Brier, log loss and AUC by version, with bootstrap intervals for
   the Brier difference.
4. **Reliability.** Bin the scores and plot observed against predicted for both versions, with
   intervals. Describe the pattern.
5. **Calibration slope.** Fit the calibration regression per version and interpret the slope.
6. **Segments.** Repeat calibration by segment; identify the worst segment and quantify the gap.
7. **Threshold.** At 0.4, compute the flag rate, precision, recall and expected cost under a
   stated loss ratio. Compare the versions.
8. **Recommend.** State which version to deploy, for which use, and the monitoring that would
   catch future miscalibration.

## Python implementation requirements

- `pandas`, `numpy`, `matplotlib`.
- `sklearn.metrics.brier_score_loss`, `log_loss`, `roc_auc_score`.
- `statsmodels.formula.api.logit` or `glm` for the calibration slope.
- Binned tables built from the data with counts and intervals.
- Fixed seed for any bootstrap; report it.

## Expected visualizations

| Figure | What it must show |
|---|---|
| Reliability diagram, both versions | The diagonal reference and the direction of miscalibration |
| Predicted score distributions by outcome | Overlap and the difficulty of the task |
| ROC curves with AUC | Similar ranking ability |
| Calibration by segment | Where the model fails |
| Flag rate and precision vs threshold | The operating trade-off |

## Interpretation requirements

- Brier score is decomposed into a calibration and a refinement component, and the interpretation
  is stated in plain language.
- AUC is explicitly described as insensitive to calibration.
- The threshold recommendation is tied to a cost ratio, not to 0.5.
- Segment differences are reported with intervals, and the multiple-comparison issue is named.
- One limitation paragraph: one holdout, possible drift, and no information about how the scores
  are used downstream.

## Deliverables

1. Executed notebook.
2. A four-page model evaluation with reliability diagrams, metrics table and threshold analysis.
3. A deployment recommendation with monitoring plan.
4. A short explanation for a non-technical stakeholder of why a "better" model can be worse.

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Audit and baseline | 10 | Base rate and trivial model established |
| Metrics | 20 | Brier, log loss and AUC computed and correctly distinguished |
| Calibration analysis | 25 | Reliability diagram, slope, and segment analysis with intervals |
| Threshold and cost | 20 | Confusion matrix, expected cost, justified operating point |
| Recommendation | 15 | Specific, conditional on use, with monitoring |
| Communication | 10 | Explains discrimination vs calibration clearly |

## Extension challenges

1. **Bootstrap comparison.** Resample cases and compute the distribution of the Brier difference.
   Is the improvement distinguishable from zero?
2. **Recalibration.** Fit isotonic or Platt scaling to v1 and show the improvement in Brier score
   without changing the ranking.
3. **Drift.** Use `feature_drift` to split the data and test whether calibration degrades in the
   drifted subgroup.
4. **Decision curve.** Plot net benefit against threshold for both versions and identify where
   each is preferable.
5. **Cost sensitivity.** Show how the preferred version changes as the cost ratio varies from
   1:1 to 10:1.
