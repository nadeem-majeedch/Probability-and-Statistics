# P04 · Reference solution — Quality control and defect analysis

[Project brief](../p04-manufacturing-quality.md) · [Dataset](../../data/projects/manufacturing_project.csv) ·
[Starter notebook](../notebooks/p04_manufacturing_quality.ipynb)

## How to approach it

Counts first, models second. Report rates per 1,000 units, because batch sizes differ by more
than 50 % and raw counts would mostly measure batch size. Then check whether the Poisson
assumption holds: if the variance exceeds the mean, the standard errors from a Poisson model are
too small and the control limits are too tight.

## Results you should obtain

| Quantity | Value |
|---|---|
| Batches | 900 |
| Total defects | 2,357 |
| Defects per 1,000 units (mean) | 5.33 |
| Mean defects per batch | 2.62 |
| Variance of defects | 4.65 |
| Variance-to-mean ratio | 1.77 |
| Rate per 1,000: L1 / L2 / L3 | 4.05 / 5.44 / 7.65 |
| Mean defects, day vs night | 2.41 vs 2.91 |
| ANOVA across lines | \(F=46.5\), \(p<0.001\) |
| Batches above the 3-sigma limit | 31 |
| Poisson AIC / negative binomial AIC | 3,538.9 / 3,488.5 |
| Negative binomial \(\alpha\) | 0.145 |
| Coefficient: temperature (per °C) | 0.067 |
| Rate ratio: L2 vs L1 | \(e^{0.3115}=1.37\) |
| Rate ratio: L3 vs L1 | \(e^{0.6599}=1.93\) |
| Rate ratio: night vs day | \(e^{0.1996}=1.22\) |

## Worked key step: the count model

A Poisson model would fix \(\mathrm{Var}(Y)=E[Y]=2.62\), but the observed variance is 4.65 —
over-dispersion by a factor of 1.77. The negative binomial allows

\[
\mathrm{Var}(Y)=\lambda+\alpha\lambda^2,
\]

with \(\hat\alpha=0.145\). Its AIC is 50 points lower than the Poisson's, so the extra parameter
is justified. The fitted model is

\[
\log \hat\lambda = \beta_0 + 0.067\,(\text{temp}-70) + 0.31\,\mathbb{1}[\text{L2}]
+ 0.66\,\mathbb{1}[\text{L3}] + 0.20\,\mathbb{1}[\text{night}]
+ \log(\text{batch size}).
\]

Coefficients are multiplicative on the rate scale: L3 produces about 93 % more defects than L1
for the same batch size and settings, and each degree above 70 °C multiplies the expected count
by \(e^{0.067}=1.069\).

## Control chart

With centre line \(\bar c=2.62\), the 3-sigma limits are

\[
2.62 \pm 3\sqrt{2.62} = (-2.24,\ 7.47).
\]

The lower limit is set to zero, because a negative defect count is impossible and a limit below
zero would make the chart insensitive. Thirty-one batches lie above 7.47 — too many for a process
in control, which is itself evidence that the variation is not Poisson: with a correctly
specified model, roughly 0.3 % of batches should exceed the limit, not 3.4 %.

## The intervention

Reducing temperature by 2 °C multiplies the expected defect count by
\(e^{-0.067\times2}=0.874\), a 12.6 % reduction. Applied to L3, whose mean is 3.74 defects per
batch, this saves about 0.47 defects per batch, or roughly 0.9 per 1,000 units at the average
batch size of 504.

That is a modest gain, and the report should say so: the line effect (L3 vs L1, a factor of 1.93)
is much larger than the temperature effect. The priority is the line, not the thermostat. A
process change on L3 — tooling, calibration, operator training — would need to be verified with
a designed comparison rather than assumed from this observational record.

## What the data do and do not show

**Supported:** defect rates differ by line and shift; temperature is positively associated with
defects; the counts are over-dispersed, so Poisson-based limits are too tight.

**Not supported:** that lowering the temperature *causes* fewer defects. Temperature, pressure
and line are correlated with unrecorded factors — material batch, operator, maintenance state —
and the data are observational. A small designed experiment on temperature would settle it.

## Common mistakes

1. **Using raw defect counts.** L3 produces larger batches, so counts alone exaggerate its
   problem; the rate is the comparable quantity.
2. **Fitting a Poisson model because the outcome is a count.** The dispersion check is not
   optional.
3. **A negative lower control limit.** Truncate at zero and explain why.
4. **Reading the control chart as a hypothesis test.** It is a monitoring rule with a designed
   false-alarm rate; repeated testing is a different procedure.
5. **Reporting the temperature coefficient without the offset.** Forgetting `log(batch_size)`
   turns a rate model into a count model and makes coefficients uninterpretable.

## Marking notes

Strong reports use rates, demonstrate over-dispersion with a statistic rather than an assertion,
justify the negative binomial with AIC, interpret coefficients as rate ratios, truncate the
control limit at zero, and prioritise the line effect over the smaller temperature effect. Weak
reports run a Poisson regression, find "significance", and recommend a temperature change without
noting that the line effect is twice as large.
