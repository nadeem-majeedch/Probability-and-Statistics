# P03 · Reference solution — Conversion and A/B testing

[Project brief](../p03-ecommerce-ab-test.md) · [Dataset](../../data/projects/ecommerce_experiment_project.csv) ·
[Starter notebook](../notebooks/p03_ecommerce_ab_test.ipynb)

## How to approach it

Start with balance, not with the outcome. An experiment that assigned 60 % of mobile users to one
arm cannot be rescued by a clever test. Then estimate the effect before testing it: the interval
is the result, and the p-value is a summary of compatibility with zero.

Keep three quantities separate throughout:

- **conversion** — did the session end in a purchase;
- **revenue per user** — includes the zeros, so it is the commercially relevant average;
- **average order value** — conditional on converting, so it measures basket size.

## Results you should obtain

| Quantity | Value |
|---|---|
| Sessions, A / B | 6,039 / 5,961 |
| Conversions, A / B | 530 / 661 |
| Conversion rate, A | 8.78 % |
| Conversion rate, B | 11.09 % |
| Difference (95 % CI) | +2.31 pp (1.24, 3.38) |
| Relative lift | +26.3 % |
| Test statistic | \(z=4.24\), \(p=2\times10^{-5}\) |
| Revenue per user, A / B | 3.66 / 4.64 (Welch \(t=-3.84\), \(p=0.0001\)) |
| Average order value, A / B | 41.74 / 41.85 (no material difference) |
| Device mix balance | \(\chi^2\) test, \(p=0.374\) |

## Worked key step: the difference and its interval

\[
\hat\Delta = 0.1109 - 0.0878 = 0.0231,
\qquad
\mathrm{SE}=\sqrt{\frac{0.0878(0.9122)}{6039}+\frac{0.1109(0.8891)}{5961}}=0.00546.
\]

The 95 % interval is \(0.0231\pm1.96(0.00546)=(0.0124,\,0.0338)\), i.e. 1.2 to 3.4 percentage
points. The \(z\) statistic is \(0.0231/0.00546=4.24\), giving \(p\approx2\times10^{-5}\).

In commercial terms: about **231 additional conversions per 10,000 sessions**, or a 26 % relative
improvement. Both the interval and the relative lift belong in the report; the interval bounds
the decision, the relative lift communicates scale.

## Revenue is consistent with conversion, not basket size

Revenue per user rises from 3.66 to 4.64, which is what a conversion lift predicts. Average
order value is essentially unchanged (41.74 vs 41.85), so the new checkout is not persuading
people to spend more per order — it is persuading more people to complete an order. That
distinction matters operationally: the lever is checkout friction, not pricing or
cross-selling.

## Segments

| Device | A | B | Difference |
|---|---|---|---|
| desktop | 10.04 % | 12.70 % | +2.66 pp |
| mobile | 7.97 % | 10.08 % | +2.11 pp |
| tablet | 9.15 % | 11.53 % | +2.38 pp |

The effect appears in every device, with overlapping intervals. Three subgroup tests were run;
at \(\alpha=0.05\) the chance of at least one false positive is about 14 %, so these are
exploratory. The honest statement is that the effect is consistent in direction and similar in
size, not that it is "significantly larger on desktop".

## Decision

Ship. The evidence is strong (\(p\approx2\times10^{-5}\)), the direction is consistent across
devices, and revenue per user moves with conversion rather than against it.

Before launch: confirm guardrails (page latency, error rate, refund rate), check that the result
holds in the most recent week rather than only in aggregate, and plan a holdback of 5 % to detect
long-term effects on retention. If traffic is 500,000 sessions per month, the point estimate
implies about 11,500 extra conversions per month; the lower bound of the interval still implies
about 6,200, which is the number to use in a conservative business case.

## Common mistakes

1. **Peeking.** Checking the dashboard daily and stopping when \(p<0.05\) inflates the
   false-positive rate far above 5 %. Pre-specify the duration or use a sequential method.
2. **Reporting only the relative lift.** "+26 %" sounds larger than "+2.3 percentage points";
   both are true and both should appear.
3. **Treating "not significant" in a segment as "no effect".** The mobile interval still
   includes a meaningful lift.
4. **Comparing AOV and concluding no revenue effect.** The revenue effect comes from conversion,
   not basket size.
5. **Ignoring the randomisation check.** If the arms differed on device mix, the comparison
   would be confounded.

## Marking notes

Strong reports check balance first, present the effect with an interval in both absolute and
relative terms, connect revenue per user to conversion rather than asserting it, label subgroup
claims as exploratory, and state the assumptions behind the revenue projection. Weak reports
quote a p-value with no interval, call the result "26 % more revenue", or claim a device-specific
effect from three uncorrected tests.
