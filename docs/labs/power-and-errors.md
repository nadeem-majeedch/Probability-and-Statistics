---
title: "Lab L-13: Type I and Type II errors, and statistical power"
description: Move the effect size, sample size and significance level to see the two error rates trade off — and what sample size 80 % power actually costs.
---

# Lab L-13: Type I and Type II errors, and statistical power

**Lab L-13 · Module [15 · Hypothesis testing](../modules/15-hypothesis-testing/chapter.md) ·
paired with [Practical 15](../practicals/notebooks/15-hypothesis-testing.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. define Type I error (\(\alpha\)), Type II error (\(\beta\)) and power (\(1-\beta\)) and
   say which one is under the researcher's direct control;
2. draw the two sampling distributions and shade the two error regions;
3. compute the critical value for a test of a mean with known \(\sigma\);
4. explain why lowering \(\alpha\) costs power, and why raising \(n\) does not have
   that cost;
5. choose a sample size for a target power, and state the assumption that makes the
   calculation exact.

## The idea in one paragraph

A hypothesis test is a decision made under uncertainty, so it can go wrong in two
ways. Rejecting a true null is a Type I error, whose rate you choose: it is the
significance level \(\alpha\). Failing to reject a false null is a Type II error,
whose rate \(\beta\) depends on how false the null is, how much data you have, and
the level you chose. Power is \(1-\beta\), the probability of finding a real effect.
The lab draws the two sampling distributions — one under \(H_0\), one under \(H_1\) —
and shades the two error regions. Moving a single slider changes which way the mistake
is made, which is why the picture is more useful than the definitions.

## The mathematics

Consider a one-sample test of \(H_0: \mu = 0\) against \(H_1: \mu = \delta\), with
known \(\sigma\), so that \(\bar X \sim N(\mu, \sigma^2/n)\). Under \(H_0\),
\(\se = \sigma/\sqrt n\) and the two-sided critical value on the \(\bar X\) scale is

\[
c = z_{1-\alpha/2}\,\frac{\sigma}{\sqrt n}.
\]

The Type I error rate is exactly \(\alpha\) by construction. The Type II error rate is
the chance of falling below the critical value when the alternative is true:

\[
\beta = \Pr\left(|\bar X| \le c \;\middle|\; \mu = \delta\right)
= \Phi\!\left(\frac{c-\delta}{\se}\right) - \Phi\!\left(\frac{-c-\delta}{\se}\right),
\]

and power is \(1-\beta\). In standardised form, with effect size \(d = \delta/\sigma\)
and \(z_c = z_{1-\alpha/2}\),

\[
\text{power} = \Phi\!\left(d\sqrt n - z_c\right) + \Phi\!\left(-d\sqrt n - z_c\right).
\]

This is exact when \(\sigma\) is known. When \(\sigma\) is estimated the test statistic
is t rather than normal, and the formula above is a slight over-estimate of power —
the lab labels it as a **z approximation**. The approximation is good for \(n\)
above about 30 and conservative for small \(n\).

A one-sided alternative replaces \(z_{1-\alpha/2}\) with \(z_{1-\alpha}\), which is why
one-sided tests have more power at the same \(\alpha\) — and why they are only
legitimate when the opposite direction is genuinely uninteresting.

## How to run the experiment

1. Start with \(d = 0.5\), \(n = 30\), \(\alpha = 0.05\), two-sided. Read the power:
   about 0.78.
2. Lower \(\alpha\) to 0.01 without touching \(n\): power drops. This is the trade-off.
3. Restore \(\alpha = 0.05\) and raise \(n\) to 120. Power rises above 0.99 and the two
   curves separate visibly.
4. Set \(d = 0\): power equals \(\alpha\) and every rejection is a Type I error.
5. Switch to one-sided with \(d = 0.5\): power rises, at the cost of ignoring effects
   in the other direction.

<div class="psds-lab" data-lab="power" data-seed="2026">
  <p class="psds-lab__instruction">
    Left curve: the distribution of the sample mean when H₀ is true. Right curve: when
    the true effect is δ. The shaded tails are α (left) and β (right).
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state:
        \(d = 0.5\), \(n = 30\), \(\alpha = 0.05\) two-sided. Power is about 0.78, so
        \(\beta \approx 0.22\): a real half-SD effect is missed about one time in five
        at this sample size.</p>
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

The results panel reports the four quantities that define the design: \(\alpha\),
\(\beta\), power and the critical value. It also reports the sample size needed for
80 % and 90 % power at the current effect size — the most useful numbers for planning,
because they convert a vague wish ("we want to detect a real effect") into a budget.

Two numbers should be interpreted together. The **critical value** moves when
\(\alpha\) or \(n\) changes; the **standard error** shrinks only with \(n\). That is
why \(n\) is the only lever that improves both error rates at once: it narrows both
curves and pushes them apart.

## Guided activities

1. **The trade-off.** Hold \(d = 0.5\), \(n = 30\). Record power at \(\alpha = 0.01\),
   0.05 and 0.10. Plot power against \(\alpha\).
2. **Size beats level.** At \(\alpha = 0.01\), find the \(n\) that restores the power
   you had at \(\alpha = 0.05\), \(n = 30\). How much extra data does the stricter
   level cost?
3. **Effect size.** With \(n = 50\) fixed, record power at \(d = 0.2, 0.5, 0.8\). Which
   is the "conventional" small/medium/large triple, and what power do you get at each?
4. **One-sided.** Compare two-sided and one-sided power at \(d = 0.5\), \(n = 30\).
   Explain the difference in terms of which tail is being used.

## Independent challenges

1. **Plan a study.** You want 90 % power to detect \(d = 0.4\) at \(\alpha = 0.05\)
   two-sided. Find \(n\) from the lab, then solve \(d\sqrt n - z_c = z_{0.90}\)
   approximately and compare.
2. **Underpowered replication.** A published study with \(n = 20\) found
   \(p < 0.05\) for an effect of about \(d = 0.5\). Using this lab, estimate the
   probability that a replication with the same \(n\) also finds it. What does that
   imply about "failed replications"?
3. **Significance versus importance.** At \(n = 1000\), a trivial effect \(d = 0.1\) is
   detected with high probability. Write a paragraph explaining why statistical
   significance and practical importance are different questions, with numbers from
   the lab.
4. **Where the approximation bites.** Compare the z-approximation power at \(n = 8\)
   with a simulation of the t test in the notebook. Is the approximation optimistic or
   conservative?

## Expected observations

| Setting | Power | β | Comment |
|---|---|---|---|
| \(d=0.5, n=30, \alpha=0.05\) | 0.782 | 0.218 | the default; one miss in five |
| \(d=0.5, n=30, \alpha=0.01\) | ≈ 0.55 | ≈ 0.45 | stricter level costs power |
| \(d=0.5, n=120, \alpha=0.05\) | > 0.99 | < 0.01 | four times the data |
| \(d=0.2, n=50, \alpha=0.05\) | ≈ 0.29 | ≈ 0.71 | small effects need big samples |
| \(d=0, \text{any } n\) | = α | \(1-\alpha\) | no effect: every rejection is Type I |
| one-sided, \(d=0.5, n=30\) | ≈ 0.85 | ≈ 0.15 | more power, narrower question |

## Self-assessment

<details><summary>1. Which error rate does the researcher choose?</summary>

\(\alpha\), the Type I error rate, is chosen when the significance level is set. It is
a decision about how much false-positive risk is acceptable. \(\beta\) is a consequence
of that choice, of the effect size and of \(n\) — it is computed, not chosen.
</details>

<details><summary>2. Why does increasing n help both error rates?</summary>

Because the standard error \(\sigma/\sqrt n\) shrinks: the two sampling distributions
narrow and separate. At fixed \(\alpha\), the critical value also moves towards zero,
but the separation grows faster, so power rises and \(\beta\) falls.
</details>

<details><summary>3. Is power a property of the test or of the data?</summary>

Of the design, given an assumed effect size. You cannot compute the power of a
completed study from its own data without circularity; power belongs to the planning
stage, before the data exist.
</details>

<details><summary>4. Why is a one-sided test more powerful?</summary>

Because the whole \(\alpha\) is spent in one tail, so the critical value is closer to
the null value. The price is that effects in the other direction cannot be detected at
all, and the choice must be made before looking at the data.
</details>

## Where this connects

- [Module 15](../modules/15-hypothesis-testing/chapter.md) develops tests, errors
  and power; [Figure 11.1](../modules/15-hypothesis-testing/chapter.md) draws the
  same two-curve geometry.
- [Practical 15](../practicals/notebooks/15-hypothesis-testing.ipynb) computes power
  with `statsmodels` and compares it with simulation.
- The p-value side of the same story is [Lab L-10](p-values.md).
- Multi-group power is a natural extension of [Lab L-14](anova.md).

## Next

- [Lab L-14 — ANOVA and comparison of multiple groups](anova.md)
- Back to the [laboratory index](index.md)
