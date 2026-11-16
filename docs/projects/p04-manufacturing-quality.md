# P04 · Manufacturing quality control and defect analysis

**Level:** intermediate · **Suggested time:** 3 weeks · **Modules:** [M09](../modules/09-discrete-distributions/chapter.md), [M15](../modules/15-hypothesis-testing/chapter.md), [M16](../modules/16-correlation-and-regression/chapter.md), [M17](../modules/17-anova-chi-square-nonparametric/chapter.md)

[Starter notebook](notebooks/p04_manufacturing_quality.ipynb) ·
[Dataset](../data/projects/manufacturing_project.csv) ·
[Reference solution](solutions/p04-solution.md)

## Real-world background

A plant produces components in batches on three lines, across two shifts. Each batch is
inspected and the number of defects recorded. Quality engineering needs to know whether the
process is stable, which line or setting is responsible for the excess defects, and whether a
change to temperature control would pay for itself.

Counts are not continuous measurements. They are bounded below by zero, their variance grows
with their mean, and they are frequently over-dispersed relative to a Poisson model — three
facts that change both the model and the control chart.

## Problem statement

Using 900 batches, characterise the defect process, test whether defect rates differ by line and
shift, model the defect count as a function of process settings, and recommend where to
intervene. The plant also wants a monitoring rule that distinguishes normal variation from a
real deterioration.

## Learning objectives

1. Work with count data and recognise over-dispersion.
2. Build and interpret a c-chart with correct limits.
3. Fit a negative binomial regression with an exposure offset.
4. Compare nested count models with AIC and likelihood.
5. Test group differences in rates and follow up with post-hoc comparisons.
6. Turn a fitted model into an operational recommendation.
7. Explain why repeated significance testing is the wrong monitoring tool.

## Dataset

`docs/data/projects/manufacturing_project.csv` — 900 batches, 7 columns, simulated.

## Dataset description

| Column | Type | Description |
|---|---|---|
| `batch_id` | identifier | Batch code |
| `line` | categorical | L1, L2, L3 — unequal volumes |
| `shift` | categorical | day or night |
| `temperature_c` | numeric | Process temperature, °C |
| `pressure_bar` | numeric | Process pressure, bar |
| `batch_size` | integer | Units produced, 380–640 |
| `defect_count` | integer | Defective units in the batch |

The simulation makes defects increase with temperature deviation from 70 °C, makes L3 worse than
L2 and L2 worse than L1, adds a small night-shift penalty, and adds batch-to-batch variation
that a Poisson model cannot represent.

## Research questions

1. What is the defect rate per 1,000 units overall, and how variable is it between batches?
2. Is the variance of `defect_count` larger than its mean? What does that imply?
3. Is the process in statistical control? Which batches, if any, are out of control?
4. Do defect rates differ by line, and which lines differ from which?
5. What is the effect of a 1 °C increase in temperature on the defect count, holding line,
   shift and batch size fixed?
6. Where should the plant intervene first, and what improvement is plausible?

## Statistical methods required

- Poisson mean–variance check; dispersion test.
- c-chart (or u-chart for rates per unit) with 3-sigma limits.
- Negative binomial regression with `log(batch_size)` offset; Poisson comparison via AIC.
- One-way ANOVA or Kruskal–Wallis on defect rates with post-hoc comparisons.
- Confidence intervals for rates and rate ratios.

## Mathematical concepts

- Poisson pmf \(P(X=k)=e^{-\lambda}\lambda^k/k!\), with \(E[X]=\mathrm{Var}(X)=\lambda\).
- Over-dispersion: \(\mathrm{Var}(X)=\lambda+\alpha\lambda^2\) for the negative binomial.
- Log link \(\log E[Y]=\log(\text{size})+\beta_0+\beta_1x_1+\cdots\).
- Control limits \(\bar c\pm3\sqrt{\bar c}\), truncated at zero.
- Rate ratio \(e^{\beta_j}\) per unit change in \(x_j\).

## Step-by-step tasks

1. **Audit.** Check ranges, duplicates and the relationship between defects and batch size.
2. **Rates.** Compute defects per 1,000 units by line and shift, with intervals.
3. **Dispersion.** Compare mean and variance of `defect_count`; run a formal dispersion test.
   State the consequence for modelling.
4. **Control chart.** Build the c-chart, set the lower limit to zero, and flag out-of-control
   batches. Distinguish special-cause from common-cause variation.
5. **Group tests.** Test equality of rates across lines; if significant, run corrected pairwise
   comparisons and report which differ.
6. **Model.** Fit the negative binomial with an offset and interpret each rate ratio. Compare
   AIC with the Poisson fit.
7. **Settings.** Estimate the effect of a 2 °C reduction toward 70 °C. Convert to defects avoided
   per 1,000 units at the observed batch size.
8. **Monitoring.** Propose a control-chart rule and the false-alarm rate it implies.
9. **Recommend.** Write the engineering memo: root cause hypothesis, intervention, expected
   effect and how it would be verified.

## Python implementation requirements

- `pandas`, `numpy`, `matplotlib`.
- `statsmodels.stats.diagnostic` for the dispersion check, or compute the Pearson statistic.
- `statsmodels.formula.api.negativebinomial` and `.poisson`; use `offset=` correctly (log batch
  size) and do not double-apply it.
- `scipy.stats` for ANOVA, Kruskal–Wallis and pairwise comparisons with correction.

## Expected visualizations

| Figure | What it must show |
|---|---|
| Defect rate by line (with intervals) | Which line is worse, and by how much |
| c-chart over batch order | Stability, runs, and out-of-control points |
| Mean–variance plot or histogram of counts | Over-dispersion |
| Temperature vs defects, coloured by line | The setting effect and the line offsets |
| Model residuals | Fit adequacy |

## Interpretation requirements

- Rates are per 1,000 units, not raw counts, because batch sizes differ.
- The negative binomial coefficient is interpreted as a rate ratio, with an interval.
- The control chart is interpreted as a monitoring device, not a test.
- The intervention estimate states its assumptions (no other changes, same batch mix).
- One limitation paragraph: inspection may itself be imperfect, and the data are observational,
  so the temperature association is not a proven cause.

## Deliverables

1. Executed notebook.
2. A four-page quality report with the control chart, model table and recommendation.
3. A one-page monitoring plan: chart type, limits, review cadence, escalation rule.
4. A short note on why a Poisson model was or was not adequate.

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Audit and rates | 10 | Correct denominators; batch size handled |
| Dispersion and model choice | 25 | Over-dispersion demonstrated; NB justified with evidence |
| Control chart | 15 | Correct limits, sensible truncation, out-of-control points identified |
| Group comparisons | 15 | Omnibus test followed by corrected post-hoc analysis |
| Model interpretation | 20 | Rate ratios interpreted correctly with intervals |
| Recommendation | 15 | Specific, quantified, with assumptions and verification plan |

## Extension challenges

1. **u-chart.** Standardise by batch size instead of using a c-chart and compare the conclusions.
2. **Change point.** Test whether the defect rate changed partway through the record. What
   method would you use, and what would a shift imply?
3. **Operator effects.** If you were given operator ids, how would you model them, and why would
   a random effect be preferable to fixed dummies?
4. **Cost model.** With a cost per defect and a cost per temperature adjustment, compute the
   economic optimum. Does it sit at 70 °C?
5. **False alarms.** Simulate a stable process and count how often the 3-sigma chart signals.
   Compare with the nominal rate.
