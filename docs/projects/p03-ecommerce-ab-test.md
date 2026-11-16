# P03 · E-commerce conversion and A/B testing

**Level:** foundation · **Suggested time:** 3 weeks · **Modules:** [M06](../modules/06-probability-fundamentals/chapter.md), [M12](../modules/12-sampling-and-sampling-distributions/chapter.md), [M14](../modules/14-estimation-and-confidence-intervals/chapter.md), [M15](../modules/15-hypothesis-testing/chapter.md)

[Starter notebook](notebooks/p03_ecommerce_ab_test.ipynb) ·
[Dataset](../data/projects/ecommerce_experiment_project.csv) ·
[Reference solution](solutions/p03-solution.md)

## Real-world background

An online retailer redesigns its checkout page and runs a controlled experiment: half of the
visitors see the current page, half see the new one. The dashboard shows a higher conversion
rate for the new page, the growth team wants to ship it, and the finance team asks whether the
difference is real, how large it is, and whether it holds for the customers who matter most.

This is the most common statistical decision in a technology company, and most of the mistakes
are made before any test is run: peeking at results, ignoring segments, measuring only clicks,
or forgetting that revenue per user and conversion are different questions.

## Problem statement

Using 12,000 sessions from a two-arm experiment, determine whether the new checkout increases
conversion, estimate the size of the effect with an interval, check whether the effect is
consistent across devices, and recommend a launch decision that accounts for revenue and risk.

## Learning objectives

1. Check randomisation balance before comparing outcomes.
2. Estimate proportions and differences with confidence intervals.
3. Run and interpret a two-proportion test, including the correct null and alternative.
4. Distinguish conversion, revenue per user and average order value.
5. Analyse a subgroup without falling into multiple-comparison errors.
6. Explain why "not significant" is not "no effect".
7. Write a launch recommendation with an explicit decision rule.

## Dataset

`docs/data/projects/ecommerce_experiment_project.csv` — 12,000 sessions, 8 columns, simulated.

## Dataset description

| Column | Type | Description |
|---|---|---|
| `user_id` | identifier | Anonymous session identifier |
| `variant` | categorical | A (control) or B (new checkout) |
| `device` | categorical | mobile, desktop, tablet |
| `channel` | categorical | organic, paid, email, social |
| `session_minutes` | numeric | Time on site, right-skewed |
| `pages_viewed` | integer | Pages in the session |
| `converted` | binary | 1 if the session ended in a purchase |
| `revenue` | numeric | Order value; zero for non-converters |

The simulation gives arm B a higher conversion rate, keeps basket size unchanged, and makes
mobile conversion lower than desktop in both arms.

## Research questions

1. Are the arms balanced on device and channel? Why does this matter?
2. What are the conversion rates and their 95 % intervals?
3. What is the difference in conversion, with an interval, and is it distinguishable from zero?
4. Does the effect differ by device? Report each subgroup honestly, including its precision.
5. How do revenue per user and average order value compare between arms?
6. What is the estimated annual revenue effect under stated traffic assumptions, and what would
   you monitor after launch?

## Statistical methods required

- Proportions with Wald or Wilson intervals.
- Chi-square test for randomisation balance (device × variant).
- Two-proportion \(z\)-test; difference in proportions with an interval.
- Subgroup analysis with a multiplicity caveat.
- Welch \(t\)-test on revenue per user, with a note on skew.
- Optional: logistic regression of conversion on variant, device and their interaction.

## Mathematical concepts

- Standard error of a proportion \(\sqrt{\hat p(1-\hat p)/n}\).
- Difference in proportions with
  \(\mathrm{SE}=\sqrt{\frac{p_1(1-p_1)}{n_1}+\frac{p_2(1-p_2)}{n_2}}\).
- Test statistic \(z=\hat\Delta/\mathrm{SE}\), two-sided p-value.
- Relative lift \(=(\hat p_B-\hat p_A)/\hat p_A\), and its interval by transformation.
- Revenue per user \(=\) conversion × average order value.

## Step-by-step tasks

1. **Audit.** Confirm the row counts per arm, check for duplicate user ids, and verify that
   `revenue` is zero exactly when `converted` is zero.
2. **Balance.** Compare device and channel mixes across arms with a chi-square test. State what
   a non-significant result does and does not prove.
3. **Conversion.** Compute rates with intervals and plot them. Describe the difference in
   absolute and relative terms.
4. **Test.** Run the two-proportion test. Report the difference, its interval, the \(z\)
   statistic and the p-value.
5. **Revenue.** Compare revenue per user and average order value. Explain why one can differ
   while the other does not.
6. **Segments.** Repeat the conversion comparison within each device. Report every subgroup,
   not only the favourable ones, and note the multiplicity issue.
7. **Power.** Estimate the sample size needed to detect the observed effect at 80 % power. Was
   the experiment adequately sized?
8. **Decision.** Write the memo: ship, iterate or stop; the expected annual effect with
   assumptions; the main risk; the guardrail metrics.

## Python implementation requirements

- `pandas` for grouping; `scipy.stats` for chi-square and \(t\) tests.
- `statsmodels.stats.proportion.proportions_ztest` for the primary test, or a hand-computed
  \(z\) with `scipy.stats.norm`.
- `statsmodels.stats.power` (optional) for the power calculation.
- Every reported number must come from code; no copy-pasted dashboard values.

## Expected visualizations

| Figure | What it must show |
|---|---|
| Conversion by arm with 95 % intervals | Overlap or separation, and the scale of the effect |
| Absolute vs relative lift | Two ways of stating the same difference |
| Conversion by device and arm | Whether the effect is consistent |
| Revenue distribution by arm (log scale) | Skew and the absence of a basket-size change |
| Optional: funnel or cumulative lift | Why peeking changes the error rate |

## Interpretation requirements

- The difference is stated in percentage points and as a relative lift.
- The p-value is interpreted as compatibility with the null, not as the probability the null is
  true.
- Subgroup results are labelled exploratory unless pre-specified.
- The revenue projection states its traffic and period assumptions explicitly.
- One limitation paragraph: one retailer, one period, possible novelty effects, and no
  long-term retention data.

## Deliverables

1. Executed notebook.
2. A three-page decision report: balance, primary result, segments, revenue, recommendation.
3. A one-page memo to the growth team with the decision rule and guardrails.
4. The power calculation that justifies the experiment's size (or shows it was too small).

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Audit and balance | 15 | Duplicates checked; balance tested and interpreted correctly |
| Estimation | 25 | Correct rates, differences and intervals; both absolute and relative |
| Hypothesis test | 20 | Correct test, assumptions, and p-value interpretation |
| Segment analysis | 15 | All subgroups reported, multiplicity acknowledged |
| Revenue analysis | 15 | Distinguishes conversion, RPU and AOV; skew handled |
| Decision and communication | 10 | Clear recommendation with assumptions and guardrails |

## Extension challenges

1. **Sequential testing.** Simulate daily peeking at the p-value and show how the false-positive
   rate inflates. What would a sequential design require?
2. **Interaction model.** Fit a logistic regression with `variant * device` and test the
   interaction. Does the effect really differ by device?
3. **Segment discovery.** Test channel subgroups and apply a Bonferroni or FDR correction. Which
   findings survive?
4. **Non-inferiority.** Reformulate the question as "B is not worse than A by more than 0.5
   percentage points" and carry out the appropriate test.
5. **Bayesian view.** With a Beta(1,1) prior per arm, compute the posterior probability that B
   is better and compare it with the frequentist conclusion.
