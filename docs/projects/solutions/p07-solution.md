# P07 · Reference solution — Cricket and statistical inference

[Project brief](../p07-cricket-inference.md) · [Dataset](../../data/projects/cricket_project.csv) ·
[Starter notebook](../notebooks/p07_cricket_inference.ipynb)

## How to approach it

Two questions dominate: is there a home advantage, and does the toss matter? They need different
tools. The first is a proportion against a fixed value, and the exact binomial test is the right
instrument at \(n=260\). The second is a test of association in a 2×2 table.

The dataset was simulated with a home scoring advantage and with the toss assigned independently
of the result. A careful analysis recovers both facts; an over-eager one "discovers" a toss effect
in a subgroup and reports it.

## Results you should obtain

| Quantity | Value |
|---|---|
| Matches | 260 |
| Home wins | 169 (65.0 %) |
| 95 % CI for home win rate | (59.2 %, 70.8 %) |
| Exact binomial test vs 50 % | \(p<0.001\) |
| Mean runs, home vs away | 167.6 vs 157.0 |
| SD of runs | 28.6 vs 27.2 |
| Paired \(t\)-test | \(t=4.48\), \(p<0.001\) |
| Home win rate when home wins toss | 69.0 % (n = 142) |
| Home win rate when away wins toss | 60.2 % |
| Chi-square, toss winner vs result | \(\chi^2=1.84\), \(p=0.174\) |
| Win rate by venue | 59.1 % to 69.4 % |
| Mean margin | 31.6 runs (median 27) |

## Worked key step: the home advantage

\[
\hat p = \frac{169}{260}=0.650,\qquad
\mathrm{SE}=\sqrt{\frac{0.65\times0.35}{260}}=0.0296,
\]

giving a 95 % interval of \(0.650\pm1.96(0.0296)=(0.592,\,0.708)\). The exact binomial test
against \(p=0.5\) gives \(p<0.001\). The effect is about 15 percentage points, and the interval
excludes 50 % comfortably.

The paired comparison confirms the mechanism: home teams score about 10.6 more runs per match
(167.6 vs 157.0, \(t=4.48\), \(p<0.001\)). Because each match contributes a pair of scores, the
paired test is correct; treating the two columns as independent samples would ignore that they
come from the same match and lose precision.

## The toss

Home teams win 69.0 % of matches in which they win the toss and 60.2 % when they do not, a
difference of 8.8 percentage points. It looks like an effect until the test is run:
\(\chi^2=1.84\), \(p=0.174\), and the interval for the difference includes zero. The toss is
assigned independently of the result in this dataset, so this is noise — exactly the kind of
"finding" that a report which tests many subgroups will eventually produce.

The toss decision shows the same pattern: 63.5 % home wins when the toss winner bats, 67.3 % when
they field. Neither the size nor the sample supports a claim.

This is the most valuable lesson in the project: with 260 matches, a difference of 9 percentage
points is well within chance. Detecting a genuine 5-point toss effect at 80 % power would need
about 785 matches.

## Venues and teams

Venue win rates range from 59.1 % to 69.4 %, with 44–62 matches each. The intervals overlap
substantially, and five venues were compared without correction. Reporting a "best venue for the
home team" from these numbers would be over-reading.

Team-level rates have the same problem in a sharper form: 33–49 home matches per team. Shrinkage
helps — a team with 3 wins in 4 matches should not be ranked above one with 20 in 40 — and a
simple empirical-Bayes adjustment pulls small-sample rates toward the overall 65 %.

## What the data do and do not show

**Supported:** a home advantage exists in this dataset, both in win rate and in runs scored.

**Not supported:** a toss advantage, a venue effect, or a team ranking. The dataset contains no
player quality, pitch condition, weather, or toss-dependent pitch deterioration — the mechanisms
through which a toss could matter are simply not measured.

## Common mistakes

1. **Testing home and away runs as independent samples.** They are paired within matches.
2. **Reporting the toss difference without a test.** 69 % vs 60 % looks decisive and is not.
3. **Ranking venues or teams by raw rate.** Small groups produce unstable extremes.
4. **Ignoring multiplicity.** Five venues and six teams mean eleven comparisons.
5. **Concluding "the toss does not matter at all".** The correct conclusion is that this dataset
   provides no evidence of an association; a small effect could still exist.

## Marking notes

Strong reports use the exact binomial test, justify the paired analysis, test the toss and
correctly fail to reject, apply intervals or shrinkage to group rates, and compute the power
calculation. Weak reports find the toss difference, run a one-sided test, and declare an
advantage.
