---
title: "Lab L-14: ANOVA and comparison of multiple groups"
description: Change the number of groups, their separation, the noise and the group size, and watch F, p and η² respond to each.
---

# Lab L-14: ANOVA and comparison of multiple groups

**Lab L-14 · Module [17 · ANOVA, chi-square and nonparametric tests](../modules/17-anova-chi-square-nonparametric/chapter.md) ·
paired with [Practical 17](../practicals/notebooks/17-anova-chi-square-nonparametric.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. partition total variation into between-group and within-group sums of squares;
2. compute the F statistic as a ratio of mean squares and interpret it;
3. explain why ANOVA is a single omnibus test rather than a set of pairwise tests;
4. read \(\eta^2\) as an effect size and distinguish it from the p-value;
5. explain how group count, separation, noise and sample size affect power.

## The idea in one paragraph

ANOVA asks whether several group means differ by more than the noise inside the groups
would explain. It does this by comparing two numbers: how far the group means spread
around the grand mean (between-group variation) and how far the observations spread
around their own group means (within-group variation). If the first is large relative
to the second, F is large and the p-value small. This lab lets you build that picture
by hand. Add a fifth group and the same separation becomes harder to detect, because
more groups means more ways to look different by chance; reduce the within-group noise
and detection becomes easy. The dot plot makes both sources of variation visible at
once.

## The mathematics

With \(k\) groups, group sizes \(n_j\), group means \(\bar y_j\) and grand mean
\(\bar y\),

\[
\text{SSB} = \sum_{j=1}^{k} n_j(\bar y_j - \bar y)^2, \qquad
\text{SSW} = \sum_{j=1}^{k}\sum_{i=1}^{n_j}(y_{ij}-\bar y_j)^2,
\]

and \(\text{SST} = \text{SSB} + \text{SSW}\). The mean squares are
\(\text{MSB} = \text{SSB}/(k-1)\) and \(\text{MSW} = \text{SSW}/(N-k)\) with
\(N = \sum n_j\), and

\[
F = \frac{\text{MSB}}{\text{MSW}} \sim F_{k-1,\,N-k} \quad \text{under } H_0,
\]

where \(H_0: \mu_1 = \dots = \mu_k\). The p-value is the upper tail
\(\Pr(F_{k-1,N-k} \ge F_{\text{obs}})\), and the effect size is

\[
\eta^2 = \frac{\text{SSB}}{\text{SST}},
\]

the share of total variation attributable to group membership.

**Assumptions.** Independent observations, normality within each group (for the exact
F distribution and small samples), and equal variances across groups. ANOVA is fairly
robust to mild non-normality with balanced groups but not to unequal variances
combined with unequal group sizes. A significant F says *some* means differ; it does
not say which, and following up with pairwise t tests without correction inflates the
Type I error rate.

## How to run the experiment

1. Start with four groups, separation 0.6, within-group SD 1, and 12 observations per
   group.
2. Read F and p: with these settings F is around 7 and p is small — the separation is
   detectable.
3. Raise the within-group SD to 3. The group means are in the same places, but F
   collapses and p rises.
4. Add a fifth group at the same separation. F falls a little, because the extra group
   costs a degree of freedom without adding separation.
5. Press **New run** several times at a low-power setting and count how often the test
   is significant. That is the power of the design.

<div class="psds-lab" data-lab="anova" data-seed="2026">
  <p class="psds-lab__instruction">
    Each column is a group, dots are observations, the red segment is the group mean and
    the dashed teal line is the grand mean. Between-group spread versus within-group
    spread is the whole test.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state: 4 groups,
        separation 0.6, within-group SD 1, 12 observations per group. The group means
        are roughly −0.9, −0.3, 0.3 and 0.9; F is near 7 on 3 and 44 degrees of
        freedom, so p is small and \(\eta^2\) is about a third.</p>
      </noscript>
    </div>
    <div class="psds-lab__figure">
      <div data-role="chart"></div>
      <div data-role="legend"></div>
      <div data-role="results"></div>
    </div>
  </div>
  <p class="psds-lab__readout" data-role="readout" aria-live="polite"></p>
  <p class="psds-lab__hint" data-role="hint"></p>
</div>

## Reading the results

The results panel is a compact ANOVA table in words: the two sums of squares with their
degrees of freedom, the two mean squares, F, p and \(\eta^2\). Check the arithmetic:
\(\text{SSB} + \text{SSW}\) must equal the total, and the mean squares are the sums of
squares divided by their degrees of freedom.

Compare F with the critical value at the 5 % level, which the panel also reports. F
above the critical value means p below 0.05 — the two statements are equivalent, and
seeing both makes the test less mysterious. Then look at \(\eta^2\): a significant
result with \(\eta^2 = 0.03\) is a real but small difference, and reporting only the
p-value would hide that.

## Guided activities

1. **Noise.** Hold everything else fixed and move the within-group SD from 1 to 3.
   Record F, p and \(\eta^2\). Explain which of the three changes most.
2. **Separation.** With SD fixed at 1, halve the separation. At what point does p cross
   0.05? How does that depend on the sample size?
3. **More groups.** Keep the separation and sample size and add a fifth group. What
   happens to the degrees of freedom, and to F? Why is a five-group design harder than
   a two-group design with the same effect?
4. **Balanced arithmetic.** Compute SSB by hand from the group means shown in the
   results panel and compare with the reported value.

## Independent challenges

1. **Two groups are a t test.** Set \(k = 2\) and verify that \(F = t^2\) for the
   corresponding two-sample test. (Run the numbers in the notebook; the identity is
   exact for equal group sizes.)
2. **Power by simulation.** Choose settings where p hovers around 0.05 and press New
   run twenty times. Estimate the power. How would you choose the sample size for 80 %
   power?
3. **Which groups differ?** A significant F does not identify the culprit. Describe a
   follow-up procedure (for example Tukey's HSD) and why an uncorrected set of pairwise
   t tests is not acceptable.
4. **Effect size.** With \(k = 5\), 10 per group and SD 1, find the separation at which
   \(\eta^2 \approx 0.10\) and note the p-value at that setting. Comment on the pair.

## Expected observations

| Setting | F (typical) | p | η² |
|---|---|---|---|
| \(k=4\), gap 0.6, SD 1, n=12 | ≈ 7 | < 0.001 | ≈ 0.33 |
| \(k=4\), gap 0.6, SD 3, n=12 | ≈ 0.8 | ≈ 0.50 | ≈ 0.05 |
| \(k=4\), gap 0.6, SD 1, n=6 | ≈ 3.5 | ≈ 0.03 | ≈ 0.30 |
| \(k=5\), gap 0.6, SD 1, n=12 | ≈ 5 | ≈ 0.002 | ≈ 0.30 |
| \(k=4\), gap 0, SD 1, n=12 | ≈ 1 | uniform | ≈ 0.02 |

## Self-assessment

<details><summary>1. Why not just run all pairwise t tests?</summary>

Because each test carries its own 5 % false-positive risk, and the chances accumulate:
with 4 groups there are 6 pairs, so the family-wise error rate for uncorrected tests is
about \(1-0.95^6 \approx 26\,\%\). ANOVA tests the family hypothesis with a single
5 % risk; follow-up tests need a correction (Tukey, Bonferroni) to keep it.
</details>

<details><summary>2. What does a significant F tell you?</summary>

That at least one group mean differs from the others, or that some combination does.
It does not identify which group, and it says nothing about the size of the difference.
</details>

<details><summary>3. Why does adding a group make detection harder at the same separation?</summary>

Because the between-group sum of squares is spread over more degrees of freedom, and
because more groups give more opportunity for chance differences. The critical F rises
with \(k-1\) while the numerator mean square does not rise proportionally.
</details>

<details><summary>4. What happens if group variances are very unequal?</summary>

The F test can be badly miscalibrated: too liberal when small groups have large
variances. Welch's ANOVA or a heteroscedasticity-robust test is the usual remedy, and
plotting the data — as the lab does — is the first diagnostic.
</details>

## Where this connects

- [Module 17](../modules/17-anova-chi-square-nonparametric/chapter.md) covers the
  partition of variation, the F test, and nonparametric alternatives.
- [Practical 17](../practicals/notebooks/17-anova-chi-square-nonparametric.ipynb) runs
  `scipy.stats.f_oneway`, Tukey follow-ups and Kruskal–Wallis on real data.
- [Figure 4.1 in Module 17](../modules/17-anova-chi-square-nonparametric/chapter.md)
  shows between-group and within-group variation as two spreads.
- Power for the two-group case is [Lab L-13](power-and-errors.md).

## Next

- Back to the [laboratory index](index.md)
- Continue to [Module 17](../modules/17-anova-chi-square-nonparametric/chapter.md) for
  chi-square and nonparametric tests.
