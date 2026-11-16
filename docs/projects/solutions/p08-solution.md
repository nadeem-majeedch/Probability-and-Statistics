# P08 · Reference solution — Prediction uncertainty and model evaluation

[Project brief](../p08-model-uncertainty.md) · [Dataset](../../data/projects/model_uncertainty_project.csv) ·
[Starter notebook](../notebooks/p08_model_uncertainty.ipynb)

## How to approach it

Evaluate the two versions on four axes — discrimination, calibration, decision performance, and
stability across segments — and do not let one number decide. The dataset is constructed so that
the two versions rank similarly but one is badly calibrated; a report that only computes AUC will
conclude, wrongly, that they are equivalent.

## Results you should obtain

| Metric | v1 | v2 |
|---|---|---|
| n | 1,234 | 1,166 |
| Mean predicted probability | 0.370 | 0.307 |
| Observed rate | 0.355 | 0.305 |
| Brier score | 0.1842 | 0.1736 |
| AUC | 0.756 | 0.750 |
| Calibration slope (95 % CI) | 0.851 (0.719, 0.982) | 0.998 (0.839, 1.158) |
| Flag rate at 0.4 | 37.5 % | 28.0 % |
| Precision of flagged group | 0.577 | 0.538 |
| Recall of flagged group | 0.610 | 0.496 |

## Worked key step: calibration slope

Regress the outcome on the logit of the predicted probability:

\[
\operatorname{logit}P(Y=1)=\alpha+\beta\,\operatorname{logit}(\hat p).
\]

A perfectly calibrated model has \(\beta=1\) and \(\alpha=0\). Here v1 gives
\(\hat\beta=0.851\) (0.719, 0.982) and v2 gives \(0.998\) (0.839, 1.158). A slope below 1 means
the predictions are too extreme — over-confident — which is exactly what the reliability diagram
shows in the middle of the range.

The Brier score agrees: 0.184 versus 0.174. For reference, a constant predictor at the observed
base rate of about 33 % would score \(0.33\times0.67=0.221\), so both models add information, and
v2 adds more.

## The subtle part: threshold performance

At the same nominal threshold of 0.4, v1 flags more cases (37.5 % vs 28.0 %) with higher
precision (0.577 vs 0.538) and higher recall. That looks like v1 winning, and it is an artefact of
scale: v1's probabilities are inflated, so a 0.4 cut-off on v1 selects a different part of the
risk distribution than 0.4 on v2.

Compare at **matched capacity** instead. Taking the top 28 % of each version:

| Version | Threshold | Mean predicted | Observed |
|---|---|---|---|
| v1 | 0.473 | 0.677 | 0.668 |
| v2 | 0.400 | 0.562 | 0.538 |

Now v1's selected group is genuinely higher-risk. The honest conclusion is conditional: v2 is
better calibrated, so its probabilities can be used directly in a cost calculation; if the
decision is a fixed-capacity ranking, the two are close and v1 is not obviously worse. Reporting
only one of these comparisons would mislead.

## Segments

Calibration by segment shows where each version fails:

| Segment | v1 predicted / observed | v2 predicted / observed |
|---|---|---|
| new | 0.365 / 0.340 | 0.320 / 0.325 |
| casual | 0.386 / 0.353 | 0.300 / 0.264 |
| loyal | 0.208 / 0.219 | 0.172 / 0.203 |
| at_risk | 0.663 / 0.660 | 0.530 / 0.532 |

Both versions over-predict for casual users; v2 under-predicts for loyal users. The gaps are
modest but systematic, and any segment-specific offer should use segment-specific calibration.

## Recommendation

Deploy **v2** for any decision that uses the probability itself — expected-value calculations,
budget allocation, offer targeting — because its scores mean what they say. Keep v1 only as a
ranking fallback if a fixed-capacity review queue is the sole use, and recalibrate it (Platt or
isotonic) before doing so.

Monitor: mean predicted vs observed monthly, Brier score on a rolling window, and calibration
within segments. Alert when the calibration slope leaves 0.9–1.1, which is the signal that
retraining is due.

## Common mistakes

1. **Reporting AUC as "accuracy".** It is a ranking statistic and is blind to calibration.
2. **Comparing models at the same threshold when their scales differ.** Compare at matched
   capacity or after recalibration.
3. **Ignoring segments.** Aggregate calibration can hide a badly miscalibrated subgroup.
4. **Treating a Brier-score difference as significant without an interval.** With 1,200 cases
   per version the gap here is meaningful, but that should be checked by bootstrap.
5. **Choosing a threshold of 0.5 by convention.** The threshold follows from the cost ratio.

## Marking notes

Strong reports compute Brier, log loss and AUC, draw reliability diagrams, fit calibration
slopes, examine segments, and compare versions at matched capacity before recommending one. Weak
reports compute AUC only and declare the versions equivalent.
