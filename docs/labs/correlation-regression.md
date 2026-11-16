---
title: "Lab L-11: Correlation and linear regression"
description: Move the slope, the residual noise and the sample size to see what r, R², the fitted line and the p-value for the slope really depend on.
---

# Lab L-11: Correlation and linear regression

**Lab L-11 · Module [16 · Correlation and regression](../modules/16-correlation-and-regression/chapter.md) ·
paired with [Practical 16](../practicals/notebooks/16-correlation-and-regression.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. interpret Pearson's \(r\) as a standardised measure of linear association;
2. fit a least-squares line and explain what "least squares" minimises;
3. relate \(R^2\) to the share of variation explained;
4. test \(H_0: \beta_1 = 0\) with a t statistic and interpret the interval for the
   slope;
5. explain why correlation does not imply causation and why a high \(R^2\) is not a
   quality guarantee.

## The idea in one paragraph

Regression draws the line that makes the vertical distances to the points as small as
possible in squared terms, and correlation measures how tightly the points hug any
straight line. The two are linked by one formula: \(b_1 = r\,s_y/s_x\). That link is
also the reason the controls in this lab cannot all be independent: once you fix the
slope of the generating line and the residual noise, the population correlation is
determined, \(\rho = \beta_1/\sqrt{\beta_1^2+\sigma^2}\) for a standardised predictor.
The lab therefore lets you set the slope, the intercept, the noise and \(n\), and it
*reports* the implied \(\rho\) rather than pretending you can choose it separately.

## The mathematics

With data \((x_i,y_i)\), the least-squares estimates are

\[
b_1 = \frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2},
\qquad b_0 = \bar y - b_1\bar x,
\]

and Pearson's correlation is

\[
r = \frac{\sum (x_i-\bar x)(y_i-\bar y)}
{\sqrt{\sum (x_i-\bar x)^2}\sqrt{\sum (y_i-\bar y)^2}}
= b_1\frac{s_x}{s_y}.
\]

The coefficient of determination is \(R^2 = r^2\), the share of the variance of \(y\)
explained by the fitted line. For inference, with \(n-2\) degrees of freedom,

\[
\se(b_1) = \sqrt{\frac{\text{SSE}/(n-2)}{\sum (x_i-\bar x)^2}},
\qquad
t = \frac{b_1}{\se(b_1)} \sim t_{n-2} \text{ under } H_0,
\]

and a \(100(1-\alpha)\%\) confidence interval is
\(b_1 \pm t_{n-2,\,1-\alpha/2}\,\se(b_1)\).

**Assumptions.** Independent observations, linearity of the conditional mean,
constant residual variance (homoscedasticity), and approximately normal residuals for
the small-sample t inference. The slope estimate is unbiased under the first two;
the p-value needs the rest.

## How to run the experiment

1. Start with slope 1, intercept 2, residual SD 1, \(n = 40\).
2. Read the implied \(\rho = 1/\sqrt{2} = 0.707\), the fitted slope near 1 and
   \(R^2\) near 0.5.
3. Raise the noise to 3. The implied \(\rho\) falls to about 0.32, the cloud widens
   and the p-value rises — with the same true slope.
4. Raise \(n\) to 120 at the high noise setting. The cloud does not change, but the
   slope becomes precisely estimated again.
5. Set the slope to 0 and confirm that the fitted slope wanders around zero and the
   p-value is uniform-ish across runs.

<div class="psds-lab" data-lab="regression" data-seed="2026">
  <p class="psds-lab__instruction">
    The solid line is the least-squares fit; the dashed teal line is the true
    generating line. The gap between them is estimation error, not bias.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state: slope 1,
        intercept 2, residual SD 1, \(n = 40\). The implied correlation is
        \(0.707\), the fitted slope is near 1, \(R^2 \approx 0.5\) and the slope is
        significant.</p>
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

The readout reports both the estimate and its uncertainty. The fitted slope should be
close to the true slope, but "close" is measured in standard errors: with \(n = 40\)
and residual SD 1 the standard error is roughly 0.1, so estimates between 0.8 and 1.2
are ordinary. The confidence interval makes that explicit; an interval that excludes 0
is the same statement as \(p < 0.05\).

\(R^2\) answers a different question from the p-value. It is about *fit*: how much of
the variation in \(y\) the line accounts for. The p-value is about *evidence*: whether
the slope could plausibly be zero. A large \(n\) makes the p-value small even when
\(R^2\) is tiny, and a small \(n\) makes it large even when the fit is good.

## Guided activities

1. **r and R².** For each of three noise settings, record \(r\), \(R^2\) and the
   p-value. Verify \(R^2 = r^2\) to the digits shown.
2. **Same slope, different evidence.** Hold slope 1 and set the noise to 3. Compare
   \(n = 20\) and \(n = 120\). The true slope has not changed; the confidence interval
   has.
3. **Zero slope.** Set slope 0. Run five times and record the five p-values. Roughly
   how often is \(p < 0.05\)?
4. **Intercept.** Change the intercept only. Which reported quantities change, and
   which do not?

## Independent challenges

1. **Predict then check.** For slope 2 and residual SD 2, compute the implied
   \(\rho = 2/\sqrt{4+4} = 0.707\) by hand, then set the lab and compare with \(r\).
2. **Sample size for precision.** Find an \(n\) that gives a 95 % interval for the
   slope of width at most 0.2, at residual SD 1, slope 1.
3. **Extrapolation.** Change the intercept to 3 and slope to -1. The line still fits,
   but what happens to predictions at \(x = 6\), outside the plotted range? Discuss
   why the standard error of a prediction grows away from \(\bar x\).
4. **Correlation without causation.** Give a plausible dataset with a strong
   correlation and no causal link, and explain which third variable you would control
   for.

## Expected observations

| Setting | Implied ρ | Fitted slope | R² | p (typical) |
|---|---|---|---|---|
| slope 1, σ 1, n 40 | 0.707 | ≈ 1.0 | ≈ 0.50 | < 0.001 |
| slope 1, σ 3, n 40 | 0.316 | ≈ 1.0 | ≈ 0.10 | ≈ 0.04 |
| slope 1, σ 3, n 120 | 0.316 | ≈ 1.0 | ≈ 0.10 | < 0.001 |
| slope 0, σ 1, n 40 | 0.000 | ≈ 0.0 | ≈ 0.03 | uniform |
| slope 2, σ 2, n 40 | 0.707 | ≈ 2.0 | ≈ 0.50 | < 0.001 |

## Self-assessment

<details><summary>1. Why can the correlation be computed from the slope and the noise?</summary>

With a standardised predictor, \(\rho = \beta_1/\sqrt{\beta_1^2+\sigma^2}\). The
numerator is the signal and the denominator the total spread of \(y\), so the ratio is
exactly the correlation. Set \(\sigma = 0\) and \(\rho = 1\): a noiseless line is a
perfect correlation.
</details>

<details><summary>2. \(R^2 = 0.10\) and \(p < 0.001\). Is the model good?</summary>

It is well evidenced and poorly explanatory. The slope is almost certainly not zero,
but 90 % of the variation in \(y\) is still unexplained. Whether that is "good" depends
on the question — for screening a biomarker, 0.10 can be useful; for prediction
marketing, it is usually not.
</details>

<details><summary>3. What does least squares minimise?</summary>

The sum of squared vertical distances between the points and the line,
\(\sum (y_i - b_0 - b_1x_i)^2\). Squared distances make large residuals count more and
give a closed-form solution; they also make the estimate sensitive to outliers.
</details>

<details><summary>4. Does a slope of zero mean x and y are unrelated?</summary>

No. It means there is no *linear* association. A strong U-shaped relationship can have
a slope near zero and a correlation near zero. Always plot.
</details>

## Where this connects

- [Module 16](../modules/16-correlation-and-regression/chapter.md) derives least
  squares, residuals and inference for the slope.
- [Practical 16](../practicals/notebooks/16-correlation-and-regression.ipynb) fits
  the same models with `statsmodels` and examines residual diagnostics.
- Figures [4.1 and 5.1 in Module 16](../modules/16-correlation-and-regression/chapter.md)
  show correlation patterns and a fitted line with its confidence bands.
- Multiple groups rather than a continuous predictor: [Lab L-14](anova.md).

## Next

- [Lab L-12 — Bayesian updating](bayesian-updating.md)
- Back to the [laboratory index](index.md)
