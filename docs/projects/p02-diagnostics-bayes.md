# P02 · Healthcare diagnostic accuracy and Bayesian reasoning

**Level:** foundation · **Suggested time:** 2 weeks · **Modules:** [M06](../modules/06-probability-fundamentals/chapter.md), [M07](../modules/07-conditional-probability-and-bayes/chapter.md), [M10](../modules/10-continuous-distributions/chapter.md), [M15](../modules/15-hypothesis-testing/chapter.md)

[Starter notebook](notebooks/p02_diagnostics_bayes.ipynb) ·
[Dataset](../data/projects/diagnostics_project.csv) ·
[Reference solution](solutions/p02-solution.md)

## Real-world background

A hospital introduces a blood biomarker to help decide who should be referred for further
investigation. The laboratory reports its "accuracy", the ward reports how many patients test
positive, and the patient asks the only question that matters: *given my result, what is the
chance I have the disease?* Those three numbers are different, and confusing them harms patients
in both directions — unnecessary investigations, and missed disease.

## Problem statement

Using records for 1,600 patients with a confirmed disease status, evaluate the biomarker as a
diagnostic tool, choose an operating threshold, and translate the result into a testing policy.
The analysis must distinguish the probability of a positive test given disease from the
probability of disease given a positive test, and must show how both depend on prevalence.

## Learning objectives

1. Build and read a 2×2 confusion matrix.
2. Compute and distinguish sensitivity, specificity, PPV, NPV and likelihood ratios.
3. Apply Bayes' theorem in probability and odds form, and explain base-rate effects.
4. Choose a threshold from explicit consequences rather than convention.
5. Evaluate a continuous marker with an ROC curve and AUC.
6. Fit a logistic regression and use it to target testing.
7. Communicate a probabilistic result to a patient without misleading them.

## Dataset

`docs/data/projects/diagnostics_project.csv` — 1,600 patients, 7 columns, simulated.

## Dataset description

| Column | Type | Description |
|---|---|---|
| `patient_id` | identifier | Anonymous patient code |
| `age` | integer | Years, 18–90 |
| `sex` | categorical | F / M |
| `symptom_severity` | integer | 0–10 clinical score |
| `biomarker` | numeric | Continuous assay value |
| `test_positive` | binary | 1 if `biomarker` exceeds the laboratory threshold |
| `disease` | binary | Confirmed diagnosis — the reference standard |

The simulation makes disease more common with age and symptom severity, and shifts the biomarker
distribution upward in diseased patients. The laboratory threshold is fixed in the data, but you
will also choose your own.

## Research questions

1. What is the prevalence of the disease in this sample, with a 95 % interval?
2. What are the sensitivity, specificity, PPV and NPV of the laboratory threshold?
3. How does the PPV change at prevalences of 1 %, 5 % and 30 %, holding the test fixed?
4. Where would you place the threshold if a missed case is five times as costly as a false
   alarm?
5. How well does the biomarker rank patients (AUC), and what does that add to the 2×2 table?
6. Which patients should be prioritised for testing, and what does the logistic model imply?

## Statistical methods required

- Proportions with confidence intervals; the 2×2 table.
- Bayes' theorem, in probability and odds form; likelihood ratios.
- ROC curve, AUC, and threshold-specific operating characteristics.
- Logistic regression with odds ratios.
- Comparison of two proportions if you split by sex or severity band.

## Mathematical concepts

- Conditional probability \(P(A\mid B)=P(A\cap B)/P(B)\).
- Bayes: \(P(D\mid +)=\dfrac{P(+\mid D)P(D)}{P(+\mid D)P(D)+P(+\mid D^c)P(D^c)}\).
- Odds form: posterior odds = prior odds × LR\(^+\), with
  \(\mathrm{LR}^+=se/(1-sp)\).
- Sensitivity \(=TP/(TP+FN)\), specificity \(=TN/(TN+FP)\),
  PPV \(=TP/(TP+FP)\), NPV \(=TN/(TN+FN)\).
- Logistic model \(\log\frac{p}{1-p}=\beta_0+\beta_1x_1+\cdots\), with
  \(e^{\beta_j}\) the odds ratio.

## Step-by-step tasks

1. **Audit.** Check ranges and duplicates; confirm the coding of `disease` and `test_positive`.
2. **Prevalence.** Estimate the prevalence with a 95 % interval.
3. **2×2 table.** Build the confusion matrix and compute all four operating characteristics by
   hand from the cells, then confirm with code.
4. **Bayes.** Compute PPV from sensitivity, specificity and prevalence. Repeat at 1 %, 5 % and
   30 %, and explain the pattern in two sentences.
5. **Thresholds.** Evaluate the laboratory threshold and two alternatives (for example 60 and
   72). Tabulate sensitivity, specificity, PPV and the number of missed cases per 1,000
   patients.
6. **Costs.** Assume a missed case costs five times a false alarm. Compute the expected cost per
   1,000 patients for each threshold and choose one.
7. **ROC.** Plot the ROC curve, compute the AUC, and mark your chosen threshold.
8. **Who to test.** Fit a logistic regression of disease on age and symptom severity; report
   odds ratios with intervals and propose a testing policy.
9. **Check.** Verify that the model's predicted probabilities are broadly calibrated in bands.
10. **Communicate.** Write the patient-facing paragraph for a positive result, then the
    clinician-facing summary.

## Python implementation requirements

- `pandas` for the table; `scipy.stats` for intervals.
- `sklearn.metrics.roc_curve` and `roc_auc_score`.
- `statsmodels.formula.api.logit` for the model, with `.params`, `.conf_int()` and
  `.predict()`.
- All confusion-matrix numbers must be derived from the data, not typed in.

## Expected visualizations

| Figure | What it must show |
|---|---|
| Biomarker distributions by disease status | Separation and overlap — the reason no threshold is perfect |
| ROC curve | Trade-off, chosen threshold marked, AUC in the caption |
| PPV vs prevalence | The base-rate effect, with the observed prevalence marked |
| Calibration plot | Predicted vs observed risk by band |
| Cost curve (optional) | Expected cost per 1,000 across thresholds |

## Interpretation requirements

- Sensitivity and PPV are never used interchangeably.
- The PPV is always stated with the prevalence at which it applies.
- The chosen threshold is justified by consequences, not by "0.5" or "the laboratory default".
- The word "accuracy" is either avoided or defined precisely.
- One limitation paragraph: the reference standard may itself be imperfect, and the sample is
  not a random sample of the population.

## Deliverables

1. Executed notebook.
2. A four-page evaluation report with the table, ROC curve, threshold analysis and policy
   recommendation.
3. A one-paragraph patient explanation and a one-paragraph clinician summary.
4. A statement of the threshold you would adopt and the evidence for it.

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Audit and table construction | 10 | Correct cells; coding confirmed |
| Operating characteristics | 20 | All four computed correctly and distinguished |
| Bayesian reasoning | 25 | Correct formula, correct arithmetic, prevalence effect explained |
| Threshold and cost analysis | 20 | Explicit costs, correct expected-cost comparison, justified choice |
| Model and calibration | 15 | Odds ratios interpreted; calibration checked |
| Communication | 10 | Patient paragraph accurate and readable |

## Extension challenges

1. **Two tests.** Assume a second, independent test with its own sensitivity and specificity.
   Compute the PPV when both are positive, and when either is positive.
2. **Net benefit.** Perform a decision-curve analysis: plot net benefit against threshold
   probability and interpret the range where the test is useful.
3. **Age-specific prevalence.** Estimate prevalence by age band and recompute PPV for each.
   Why does a single PPV mislead?
4. **Measurement error.** Add noise to the biomarker and recompute the AUC. How much degradation
   does the test tolerate?
5. **Screening programme.** Estimate the number of false positives per true case detected at 1 %
   prevalence, and the follow-up workload per 100,000 screened.
