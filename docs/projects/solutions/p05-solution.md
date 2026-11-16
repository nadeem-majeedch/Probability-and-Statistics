# P05 · Reference solution — Weather, probability and distributions

[Project brief](../p05-weather-distributions.md) · [Dataset](../../data/projects/weather_project.csv) ·
[Starter notebook](../notebooks/p05_weather_distributions.ipynb)

## How to approach it

The dataset contains a mixture, not a single variable. On 72 % of days rainfall is exactly zero;
on the rest it is positive and right-skewed. Fitting one distribution to all days produces a
non-sense model that predicts a substantial probability of negative rain. Split first —
\(P(\text{rain})\) and then the amount given rain — and recombine with the law of total
probability.

Seasonality is the second trap: a pooled histogram of temperature across three years is not a
distribution of anything physical, it is a mixture of winter and summer.

## Results you should obtain

| Quantity | Value |
|---|---|
| Station-days | 3,288 (3 stations × 1,096 days) |
| Wet-day proportion | 27.7 % |
| Mean rainfall, wet days only | 8.68 mm |
| Median rainfall, wet days | 6.70 mm |
| Gamma fit to wet days | shape 1.53, scale 5.67 |
| Mean temperature: Karachi / Lahore / Murree | 30.0 / 28.5 / 19.0 °C |
| Station comparison | \(F=695.5\), \(p<10^{-200}\) |
| 99th percentile, all days | 23.9 mm |
| \(P(\text{rain}>30\text{ mm})\) | 0.49 % (about 1.8 days per year) |
| \(P(>30\text{ mm}\mid\text{wet})\) | 1.76 % |

## Worked key step: exceedance by the law of total probability

\[
P(X>30)=P(\text{wet})P(X>30\mid\text{wet})=0.277\times0.0176=0.0049 .
\]

That is roughly **1.8 exceedance days per year**. The naive calculation that treats the 99th
percentile of all days (23.9 mm) as a "1-in-100 day" and extrapolates a normal tail would
understate the 30 mm event and give no usable uncertainty.

The distinction the brief asks for: the 99th percentile of all days is the value exceeded on 1 %
of days; a "1-in-100 rainfall day" in engineering usually means a 1-in-100 *wet* event or an
annual exceedance probability. The two differ by the wet-day fraction, and mixing them changes
the design value by a factor of three.

## The two-part model

Rainfall is well described by

\[
P(\text{rain}) \approx 0.277, \qquad X\mid\text{rain} \sim \mathrm{Gamma}(1.53,\ 5.67),
\]

with mean \(1.53\times5.67=8.68\) mm, matching the observed wet-day mean. A lognormal fits
almost as well; the gamma is preferred here because the QQ plot is straighter in the tail and
the AIC is slightly lower. The choice matters for the 99th percentile, which is where the two
models disagree most — a good reason to report an interval rather than a single design value.

## Seasonality and station differences

Monthly mean maximum temperature runs from 16.4 °C in January to 35.2 °C in July, an amplitude
of about 19 °C. Murree sits 9–11 °C below the other stations, which is why the station comparison
gives an enormous \(F\). The test is technically inappropriate as specified, because daily
temperatures are strongly autocorrelated and the seasonal cycle is shared: the effective sample
size is far below 3,288, so the p-value overstates the evidence. The conclusion (stations differ)
is anyway obvious from the means; the lesson is about the assumption, not the conclusion.

Rainfall peaks in October in this record (monthly mean 3.45 mm), with a secondary wet period in
spring. A design that assumes a uniform rate across the year would misstate both the exceedance
probability and the maintenance schedule.

## Design recommendation

For a drainage capacity of 30 mm/day, the estimated exceedance probability is 0.49 %, or about
1.8 days per year, with substantial uncertainty because only three years are observed. A
bootstrap of the 99th percentile gives an interval roughly 20–30 mm wide at this sample size.
Recommend designing to the upper end of that interval, and state the model assumption — a
stationary climate — explicitly, since it is the assumption most likely to fail.

## Common mistakes

1. **Fitting a normal to all days.** It implies negative rainfall and understates the tail.
2. **Reporting the mean of all days as "typical rainfall".** It is 2.4 mm, but the typical wet
   day is 8.7 mm; both are true and they answer different questions.
3. **Ignoring seasonality.** Pooled temperature distributions are mixtures.
4. **Treating the 99th percentile of all days as a 100-year event.** Return periods depend on
   the reference set and the time unit.
5. **Running ANOVA on autocorrelated daily data without comment.** The p-value is not calibrated.

## Marking notes

Strong reports split the mixture, justify the distribution with a QQ plot and an information
criterion, compute exceedance with the law of total probability, and attach uncertainty to the
design value. Weak reports fit a normal to rainfall, report a mean, and call it a day.
