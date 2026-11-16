# Capstone · Reference solution — Why are subscribers leaving?

[Project brief](../p09-capstone.md) · [Dataset](../../data/projects/capstone_project.csv) ·
[Starter notebook](../notebooks/p09_capstone_churn.ipynb)

## How to approach it

The capstone is a chain of eight analyses, and each one hands a result to the next. The report
should read as one argument:

1. Who are the customers, and how often do they leave?
2. What does the churn process look like as a probability model?
3. Which behaviours vary, and with what distribution?
4. How much would a sample of 30 tell us, and how much would it mislead?
5. How precise are the churn rate and the channel differences?
6. Are the observed differences distinguishable from noise?
7. What does a model add beyond pairwise correlation?
8. What should the business do, and what would prove it worked?

The trap is the plan variable: raw churn is highest on the basic plan, but the adjusted model
reverses the ordering. That reversal is not an error. It is the capstone's central lesson about
conditional and marginal associations.

## Results you should obtain

| Quantity | Value |
|---|---|
| Customers | 1,400 |
| Churned | 256 (18.3 %) |
| Churn rate (95 % CI) | 18.3 % (16.3 %, 20.3 %) |
| Standard error of the rate | 0.0103 |
| \(P(\text{at least one churn among 20})\) | 0.982 |
| Mean monthly spend (median) | 43.42 (40.38) |
| Sessions: mean, variance, ratio | 16.12, 18.94, 1.17 |
| Tickets: mean, variance | 1.24, 1.32 |
| Churn by channel: organic / referral / partner / paid | 15.6 % / 15.1 % / 18.3 % / 23.9 % |
| Channel \(\chi^2\) | 12.83, df 3, \(p=0.005\) |
| Churn by plan: basic / plus / pro | 23.2 % / 15.5 % / 10.8 % |
| Plan \(\chi^2\) | \(p<0.001\) |
| Churn by region: East / North / South / West | 26.3 % / 16.4 % / 15.5 % / 14.5 % |
| Logistic AUC | 0.799 |
| Spend regression \(R^2\) | 0.868 |

## 1–2. Description and the churn rate

The base is 1,400 customers, 46 % basic, 36 % plus and 18 % pro. Mean spend is 43.42 with a
median of 40.38, so spend is mildly right-skewed by the pro tier; a mean alone would overstate
the typical customer's bill by about 3.

The churn rate is \(256/1400=0.183\), with

\[
\mathrm{SE}=\sqrt{\frac{0.183\times0.817}{1400}}=0.0103,
\qquad 0.183\pm1.96(0.0103)=(0.163,\,0.203).
\]

In business terms, between 163 and 203 of every 1,000 customers leave. The interval is what makes
the number usable; the point estimate alone invites false precision.

## 3. The process as a probability model

Treating each customer as an independent Bernoulli trial with \(p=0.183\), the chance that at
least one of the next 20 customers churns is

\[
1-(1-0.183)^{20}=0.982 .
\]

That is almost certain, and it is a useful sanity check for a manager who thinks of churn as rare.
The independence assumption is strong — churn clusters by cohort and channel — so the figure is
illustrative, not a forecast.

## 4. Distributions

Sessions per month have mean 16.12 and variance 18.94, a variance-to-mean ratio of 1.17. A
Poisson model would force the ratio to 1; the excess is small but real, consistent with
heterogeneity between customers. Tickets are closer to Poisson (mean 1.24, variance 1.32). The
practical consequence is modest here, but the check matters: with a ratio of 3 or more, a Poisson
standard error would be badly wrong.

## 5. Sampling

Simulating 2,000 samples of size 30 gives a sampling distribution of the churn rate centred on
0.183 with SD close to

\[
\sqrt{\frac{0.183\times0.817}{30}}=0.0706 .
\]

A pilot of 30 customers therefore estimates churn to within about ±14 percentage points — far too
coarse to evaluate any intervention. This is the most important practical result in the project:
small pilots cannot detect realistic effects.

## 6. Do channels and plans differ?

The channel rates are 15.6 % (organic), 15.1 % (referral), 18.3 % (partner) and 23.9 % (paid).
The chi-square test gives \(\chi^2=12.83\) with 3 df, \(p=0.005\). The paid–organic difference is
8.3 percentage points, and its interval excludes zero by a comfortable margin.

Plan differences are larger: 23.2 % on basic, 15.5 % on plus, 10.8 % on pro. The omnibus test is
significant, and the ordering is monotone. Region also differs, with East at 26.3 % against
14.5 % in West — a difference that deserves investigation but should not be interpreted as
geography causing churn.

## 7. Correlation and the model

The correlation matrix shows the expected pattern: tickets +0.38 with churn, satisfaction −0.36,
spend −0.15, tenure −0.12, sessions −0.08. It also shows tickets and satisfaction at −0.58, which
is a warning that the two variables carry overlapping information.

The logistic model (AUC 0.80) gives odds ratios:

| Predictor | Odds ratio | Reading |
|---|---|---|
| Support tickets (per ticket) | 1.75 | Each ticket raises the odds by 75 % |
| Satisfaction (per point) | 0.68 | Each point cuts the odds by a third |
| Tenure (per month) | 0.971 | About 3 % lower odds per month |
| Sessions (per session) | 0.963 | Small protective association |
| Spend (per unit) | 0.983 | Confounded with plan; do not read causally |
| Plan: pro vs basic | 1.51 | **Reversal — see below** |
| Channel: paid vs organic | 1.52 | Paid acquisition is the riskiest |

The plan reversal is the most interesting result. Raw churn is 10.8 % on pro against 23.2 % on
basic, but conditional on spend, tenure and the rest, pro's odds are 51 % higher. The reason is
collinearity between plan and spend: pro customers pay far more, and higher spend is associated
with lower churn, so once spend is held fixed, the plan comparison changes meaning entirely.

The honest interpretation: **plan is not a causal driver**; it is a marker for price level and
customer type. A report that says "upgrade customers to reduce churn" has misread the model. The
defensible statement is that basic customers churn more overall, and that the apparent pro
advantage is explained by their higher spend.

## 8. Spend, and what it does not mean

Regressing spend on tenure and plan gives \(R^2=0.868\):

\[
\widehat{\text{spend}} = 23.64 + 0.30\,\text{tenure} + 17.95\,\mathbb{1}[\text{plus}]
+ 43.39\,\mathbb{1}[\text{pro}].
\]

Tenure adds about 0.30 per month — about 3.60 per year — and plan differences dominate. This is
almost a tautology (plans have different prices), and it explains why spend is a poor causal
variable in the churn model.

## Recommendation

The strongest, most actionable association is **support tickets**: churn rises from 4.7 % with no
tickets to 13.6 % with one, 24.7 % with two and 51.1 % with three or more. The mechanism is
plausible (unresolved problems drive cancellation), the effect is large, and it is measurable in
real time.

Proposed action: a proactive outreach programme for customers who open a second ticket within 60
days — a human call, a credited month, and a check that the issue is resolved. Target the paid
channel first, where churn is highest.

**Test design.** Randomise eligible customers 50/50 to outreach or control, measure churn over 90
days, and pre-register the primary metric. To detect a reduction from 18 % to 15 % at 80 % power
requires about 2,400 customers per arm:

\[
n \approx \frac{(1.96+0.84)^2\,[p_1(1-p_1)+p_2(1-p_2)]}{\Delta^2}
=\frac{7.85\times0.275}{0.03^2}\approx 2{,}400 .
\]

Guardrails: contact volume, satisfaction of contacted customers, and cost per retained customer.

## What the data cannot tell you

- **Causation.** Every association here is observational; tickets may be a symptom of a failing
  product rather than its cause.
- **Counterfactuals.** We do not observe what churned customers would have done with an offer.
- **Time order.** The file is a snapshot; we cannot tell whether dissatisfaction preceded the
  tickets or followed them.
- **Selection.** Customers who already left may be missing from the records entirely.

## Common mistakes

1. **Reporting churn only as a percentage.** The interval is the finding.
2. **Running a pilot of 30 and expecting a decision.** The standard error is ±7 percentage
   points at that size.
3. **Interpreting the plan odds ratio causally.** The reversal shows why that fails.
4. **Treating correlated predictors as independent causes.** Tickets and satisfaction are
   strongly related.
5. **Stopping at the model.** The capstone is marked on the decision and the test design, not on
   the AUC.

## Marking notes

A strong capstone follows the eight areas in order, carries uncertainty through, notices and
explains the plan reversal, distinguishes association from causation throughout, and ends with a
specific, powered experiment. A weak one produces eight disconnected sections, reports only
point estimates, and recommends an action without a way to test it.
