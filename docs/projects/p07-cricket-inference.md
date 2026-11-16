# P07 · Cricket performance and statistical inference

**Level:** intermediate · **Suggested time:** 2 weeks · **Modules:** [M06](../modules/06-probability-fundamentals/chapter.md), [M09](../modules/09-discrete-distributions/chapter.md), [M15](../modules/15-hypothesis-testing/chapter.md), [M17](../modules/17-anova-chi-square-nonparametric/chapter.md)

[Starter notebook](notebooks/p07_cricket_inference.ipynb) ·
[Dataset](../data/projects/cricket_project.csv) ·
[Reference solution](solutions/p07-solution.md)

## Real-world background

Cricket is a natural laboratory for inference: 260 matches, a binary outcome, paired scores, and
a persistent folk claim that winning the toss matters. The analyst's job is to separate a real
effect from the noise that small samples generate, and to resist the temptation to explain every
ranking.

The dataset is simulated, so the true effects are known to the person who generated it. That
makes it unusually good for learning: you can check whether your method recovered the structure
that was built in, and whether you over-interpreted what was not.

## Problem statement

Using 260 matches, test whether the home team wins more often than chance, whether the toss
confers an advantage, whether home and away scores differ, and whether venues or teams differ in
win rate. Then explain which of the observed rankings are stable enough to act on.

## Learning objectives

1. Test a proportion against a specified value with an exact binomial test.
2. Analyse paired data correctly and explain why pairing matters.
3. Distinguish association from advantage.
4. Interpret small-group rankings with intervals and shrinkage.
5. Recognise multiple comparisons across venues and teams.
6. State clearly what a dataset of this kind cannot answer.

## Dataset

`docs/data/projects/cricket_project.csv` — 260 matches, 10 columns, simulated.

## Dataset description

| Column | Type | Description |
|---|---|---|
| `match_id` | identifier | Match reference |
| `home_team`, `away_team` | categorical | Six teams |
| `venue` | categorical | Five venues |
| `toss_winner` | categorical | Team that won the toss |
| `toss_decision` | categorical | bat or field |
| `home_runs`, `away_runs` | integer | Runs scored |
| `home_won` | binary | 1 if the home team won |
| `margin_runs` | integer | Absolute difference in runs |

The simulation gives the home team a scoring advantage, which produces a home win rate above
50 %. The toss is assigned independently of the result, so any toss "effect" you find is noise —
which is exactly the lesson.

## Research questions

1. What is the home win rate, with a 95 % interval, and is it distinguishable from 50 %?
2. Do home and away teams score differently? Which test is appropriate and why?
3. Is winning the toss associated with winning the match?
4. Does the toss decision (bat or field) matter?
5. Do win rates differ by venue or by team, and are those differences stable?
6. What would you need to answer "does the toss cause an advantage"?

## Statistical methods required

- Exact binomial test for a proportion; Wilson interval.
- Paired \(t\)-test or Wilcoxon signed-rank for home vs away scores.
- Chi-square test of independence for toss and outcome.
- Confidence intervals for group proportions; comparison with multiplicity caution.
- Optional: logistic regression of `home_won` on toss and venue.

## Mathematical concepts

- Binomial model \(X\sim\mathrm{Binomial}(n,p)\) and the exact test for \(p=0.5\).
- Standard error of a proportion and the Wilson interval.
- Paired differences \(d_i=x_i-y_i\) and the paired \(t\) statistic.
- Chi-square statistic \(\sum (O-E)^2/E\) with \((r-1)(c-1)\) df.
- Shrinkage: \(\hat p_{\text{shrunk}}=\frac{x+\kappa\bar p}{n+\kappa}\).

## Step-by-step tasks

1. **Audit.** Check for duplicate matches, impossible scores (a tie after adjustment), and
   verify that `home_won` agrees with the scores.
2. **Home advantage.** Compute the win rate with an interval and run the exact binomial test.
   Report the effect size in percentage points.
3. **Scoring.** Compare home and away runs with a paired test; check the distribution of the
   difference first.
4. **Toss.** Test the association between winning the toss and winning the match. Compute the
   same for the toss decision.
5. **Groups.** Estimate win rates by venue and by team with intervals. Comment on the smallest
   groups and apply shrinkage or a multiplicity correction.
6. **Model (optional).** Fit a logistic regression of `home_won` on toss winner and venue, and
   compare with the unadjusted tests.
7. **Power.** Compute the sample size needed to detect a 5-percentage-point toss effect at 80 %
   power. Was 260 matches enough?
8. **Interpret.** Write the analysis for a cricket audience: what is established, what is noise,
   and what the data cannot settle.

## Python implementation requirements

- `pandas` for grouping; `scipy.stats` for `binomtest`, `ttest_rel`, `wilcoxon`,
  `chi2_contingency`.
- Wilson intervals computed explicitly, not taken from a library default without comment.
- A shrinkage estimate for at least one small group.
- All p-values accompanied by the effect estimate.

## Expected visualizations

| Figure | What it must show |
|---|---|
| Home win rate with interval and 50 % line | The size of the advantage relative to uncertainty |
| Distribution of run margins | Spread and shape of the outcome |
| Home vs away runs (scatter or paired plot) | Pairing and the average difference |
| Win rate by venue with intervals | Overlap, and why rankings are unstable |
| Optional: toss outcome contingency heatmap | The absence of association |

## Interpretation requirements

- The win rate is reported with an interval, not as a bare percentage.
- The toss result is interpreted as "no evidence of an association", not "the toss does not
  matter at all".
- Venue and team rankings carry intervals and a warning about multiple comparisons.
- The paired analysis explains why the same match produces two dependent scores.
- One limitation paragraph: simulated data, no player-level information, no pitch or weather
  conditions, and no information about team strength beyond the labels.

## Deliverables

1. Executed notebook.
2. A three-page analysis with the home-advantage test, toss analysis, and group comparisons.
3. A one-page summary for a non-technical audience.
4. A power calculation for the toss question.

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Audit and description | 10 | Consistency checks done |
| Proportion inference | 25 | Exact test, interval, effect size, correct interpretation |
| Paired analysis | 20 | Pairing justified; appropriate test; assumptions checked |
| Toss and group tests | 20 | Tests correct; multiplicity and small groups handled |
| Communication | 15 | Clear, honest, free of over-claiming |
| Extensions and reflection | 10 | Insightful discussion of what the data cannot show |

## Extension challenges

1. **Shrinkage comparison.** Estimate team win rates with and without empirical-Bayes shrinkage
   and show how the ranking changes.
2. **Venue effects.** Test whether the home advantage differs by venue using an interaction in a
   logistic model.
3. **Score distribution.** Model `home_runs` with a normal and a skew-normal distribution and
   compare the fits.
4. **Sequential monitoring.** If you checked the toss association after every 20 matches, how
   often would you have declared a false positive?
5. **Design.** Propose the data you would collect to answer the toss question causally, and
   explain why randomisation is difficult in sport.
