# P06 · Reference solution — Credit risk modelling

[Project brief](../p06-credit-risk.md) · [Dataset](../../data/projects/credit_risk_project.csv) ·
[Starter notebook](../notebooks/p06_credit_risk.ipynb)

## How to approach it

Three questions, in order: how often do loans default, what predicts default, and where should the
cut-off be? The first is a proportion with an interval; the second is a logistic model with odds
ratios; the third is an expected-value calculation that uses both.

The most common failure is to stop after the model and report AUC as if it were a decision rule.
AUC says the ranking is useful; it says nothing about whether a predicted 6 % really means 6 %.

## Results you should obtain

| Quantity | Value |
|---|---|
| Loans | 2,000 |
| Default rate (95 % CI) | 12.2 % (10.8 %, 13.6 %) |
| Mean score, defaulters vs performers | 608.8 vs 658.7 |
| Mean DTI, defaulters vs performers | 25.6 % vs 22.4 % |
| Odds ratio: credit score (per point) | 0.990 (0.988, 0.992) |
| Odds ratio: credit score (per 50 points) | 0.601 |
| Odds ratio: DTI (per percentage point) | 1.046 (1.025, 1.068) |
| Odds ratio: term (per month) | 0.998 (0.989, 1.008) — not distinguishable from 1 |
| AUC | 0.716 |

## Worked key step: the odds ratio for credit score

The fitted coefficient is \(\hat\beta=-0.01019\) per point, so

\[
\widehat{\mathrm{OR}}_{50}=e^{-0.01019\times50}=e^{-0.5095}=0.601 .
\]

A 50-point higher credit score is associated with about **40 % lower odds** of default, holding
DTI and term fixed. For DTI, each additional percentage point multiplies the odds by 1.046, so a
10-point increase raises them by \(e^{0.452}=1.57\).

Note the difference between odds and probability: an odds ratio of 0.60 does not mean the
probability falls by 40 %. At a baseline probability of 20 %, the odds fall from 0.25 to 0.15 and
the probability from 20 % to 13 %.

## Bands, calibration and the cut-off

| Score band | n | Default rate | Expected value per loan |
|---|---|---|---|
| 300–600 | 429 | 24.2 % | −2,576 |
| 600–650 | 549 | 14.8 % | −393 |
| 650–700 | 544 | 7.4 % | +1,309 |
| 700–750 | 324 | 5.2 % | +1,793 |
| 750–900 | 154 | 1.3 % | +2,701 |

Expected value uses \(p_{\text{repay}}\times3{,}000-p_{\text{default}}\times20{,}000\). The
600–650 band is roughly break-even (−393 per loan), and everything below 650 loses money. The
cut-off implied by these figures is **650**, with the 600–650 band treated as marginal and
reviewed manually if capacity allows.

This recommendation is sensitive to the loss assumption: at a loss of 12,000 rather than 20,000,
the 600–650 band becomes profitable. The report must show this sensitivity rather than present a
single cut-off as if it were a law.

## Discrimination versus calibration

The AUC of 0.716 means a random defaulter has about a 72 % chance of scoring lower than a random
performer — useful, but far from a clean separation. The band table is the calibration check, and
it is broadly monotone, which is what makes the expected-value calculation meaningful. A model
with AUC 0.80 and badly calibrated probabilities would be worse for pricing.

## What the data do and do not show

**Supported:** lower scores and higher DTI are associated with default; the term is not
associated once score and DTI are included; the risk gradient is steep enough to support a
cut-off.

**Not supported:** that declining an applicant would have prevented their default. Only approved
loans are observed, so the counterfactual is missing — the classic reject-inference problem.
Also, region and income are correlated with score, and using them in pricing may raise fairness
questions that accuracy alone cannot settle.

## Common mistakes

1. **Reporting "the model is 88 % accurate".** At a 12 % default rate, predicting "no default"
   for everyone gives 88 % accuracy and detects nothing.
2. **Interpreting an odds ratio as a probability change.** The two diverge sharply away from
   p = 0.5.
3. **Using AUC to choose a cut-off.** AUC is threshold-free; the cut-off comes from costs.
4. **Including term because it is in the file.** Its interval includes 1; the honest conclusion
   is that it adds nothing here.
5. **Ignoring selection.** The sample contains only loans that were made.

## Marking notes

Strong reports give the default rate with an interval, interpret odds ratios per meaningful
increment, show the band table with intervals, compute expected value explicitly, state the
sensitivity of the cut-off to the loss assumption, and discuss reject inference. Weak reports
present AUC as accuracy and recommend a cut-off of 0.5.
