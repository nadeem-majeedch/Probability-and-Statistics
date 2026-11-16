---
title: "Lab L-04: Continuous probability distributions"
description: Explore normal, exponential, gamma and uniform densities; shade an interval and see why the area is the probability, not the height.
---

# Lab L-04: Continuous probability distributions

**Lab L-04 · Module [10 · Continuous distributions](../modules/10-continuous-distributions/chapter.md) ·
paired with [Practical 10](../practicals/notebooks/10-continuous-distributions.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. state what a probability density is and why it is not a probability;
2. compute probabilities as areas, \(\Pr(a < X \le b) = \int_a^b f(x)\,dx\);
3. recognise the normal, exponential, gamma and uniform families and their parameters;
4. explain why \(\Pr(X = x) = 0\) for every \(x\) when \(X\) is continuous;
5. check a density against simulated data and say how much disagreement is expected.

## The idea in one paragraph

A continuous random variable has no separated outcomes to put bars on, so its
distribution is described by a curve whose *area* is probability. The curve's height
is a density: it tells you how much probability sits in a small neighbourhood, per
unit of \(x\). This lab lets you switch families, move their parameters, and drag an
interval across the axis. The shaded area is the probability of that interval — and
when you squeeze the interval to a point, the area goes to zero while the curve stays
exactly where it was. That single observation resolves most confusion about densities.

## The mathematics

A density \(f\) satisfies \(f(x) \ge 0\) and \(\int_{-\infty}^{\infty} f(x)\,dx = 1\).
For any interval,

\[
\Pr(a < X \le b) = \int_{a}^{b} f(x)\,dx = F(b) - F(a),
\]

where \(F\) is the cumulative distribution function. Because the integral over a point
has zero width, \(\Pr(X = x) = 0\) for every \(x\); this is why a density may exceed 1
(for example a uniform on \((0, 0.5)\) has density 2 everywhere).

The four families in the lab:

| Family | Density | Mean | Variance |
|---|---|---|---|
| Normal\((\mu,\sigma^2)\) | \(\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}\) | \(\mu\) | \(\sigma^2\) |
| Exponential\((\lambda)\) | \(\lambda e^{-\lambda x}\), \(x \ge 0\) | \(1/\lambda\) | \(1/\lambda^2\) |
| Gamma\((k,\lambda)\) | \(\frac{\lambda^{k}x^{k-1}e^{-\lambda x}}{\Gamma(k)}\), \(x \ge 0\) | \(k/\lambda\) | \(k/\lambda^2\) |
| Uniform\((a,b)\) | \(\frac{1}{b-a}\), \(a \le x \le b\) | \((a+b)/2\) | \((b-a)^2/12\) |

The exponential is the gamma with \(k = 1\), which is why the gamma family interpolates
between a sharply peaked distribution and a smooth hump as \(k\) grows.

## How to run the experiment

1. Start with the normal, \(\mu = 0\), \(\sigma = 1\), interval \((-1, 1]\).
2. Read the shaded area: 0.683. Read the density at the midpoint: 0.399 — a number
   with no probability interpretation.
3. Narrow the interval to \((-0.1, 0.1]\) and watch the area fall to 0.08 while the
   curve itself does not move.
4. Switch to the exponential with \(\lambda = 1\) and set the interval to \((0, 1]\):
   the area is 0.632.
5. Switch to the gamma with shape 3 and rate 1: the density is zero at the origin,
   rises, then decays. Explain in one sentence why it cannot be exponential.

<div class="psds-lab" data-lab="continuous" data-seed="2026">
  <p class="psds-lab__instruction">
    The curve is the density; the shaded area is \(\Pr(\text{lo} < X \le \text{hi})\).
    The faint bars are simulated draws, so a correct density should follow their
    outline.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state: standard
        normal with the interval \((-1, 1]\), giving area \(0.683\). The density at the
        midpoint is \(0.399\), which is not a probability. The mathematics is above.</p>
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

The results panel puts the three quantities side by side: the density at the
midpoint, the theoretical area, and the observed proportion of simulated draws inside
the interval. The first is a rate per unit, the second and third are probabilities.
They should agree to about \(2\sqrt{p(1-p)/m}\) with \(m\) draws — for the normal
default that is roughly ±0.02 at 2,000 draws.

Watch what happens to the observed proportion when the interval is very narrow: at
\((-0.05, 0.05]\) the expected count is about 40 in 2,000 draws, so the simulation
starts to look noisy even though the theory is exact. Narrow intervals are exactly
where simulation is a poor tool and integration is a good one.

## Guided activities

1. **Area, not height.** With the normal at \(\mu=0,\sigma=1\), record the density at
   \(x=0\) and the area of \((-0.5,0.5]\). Then change \(\sigma\) to 0.5 and repeat:
   the density doubles, the area stays 0.383. Explain.
2. **Uniform sanity check.** Set the uniform on \((0,2)\): the density is 0.5
   everywhere and \(\Pr(0.5 < X \le 1.5) = 0.5\).
3. **Gamma vs exponential.** Compare gamma shape 1 with shape 3 at rate 1. Which
   quantities change, and which stay the same? Look at the mean.
4. **Tail probabilities.** For the exponential with \(\lambda = 1\), compute
   \(\Pr(X > 2) = e^{-2} = 0.135\) by hand and confirm with the lab.

## Independent challenges

1. **A density above 1.** Find parameters in the lab for which the peak density
   exceeds 1, and write a sentence a classmate could understand explaining why that is
   allowed.
2. **Interval arithmetic.** For a normal, find the interval symmetric about \(\mu\)
   that contains exactly 50 % of the probability. Compare with the interquartile range.
3. **Why the exponential is memoryless.** Show algebraically that
   \(\Pr(X > s+t \mid X > s) = \Pr(X > t)\) and check it numerically in the lab with
   \(s = 1, t = 2\).
4. **Model choice.** Times between arrivals are exponential; total time for \(k\)
   arrivals is gamma with shape \(k\). Explain the relationship using the lab's mean.

## Expected observations

| Setting | Theoretical probability | What you should see |
|---|---|---|
| Normal, \((-1, 1]\) | 0.683 | shaded area ≈ two-thirds of the curve |
| Normal, \((-2, 2]\) | 0.954 | almost the whole curve |
| Exponential \(\lambda=1\), \((0,1]\) | 0.632 | area from the origin to the first unit |
| Gamma shape 3, \((0,3]\) | 0.577 | peak away from the origin |
| Uniform \((0,2)\), \((0.5,1.5]\) | 0.500 | a rectangle, area = width × 0.5 |
| Any interval narrowed to a point | 0 | area vanishes, density does not |

## Self-assessment

<details><summary>1. Why is \(f(0) = 0.399\) not a probability?</summary>

Because probability for a continuous variable is area, and a point has zero width.
The density is a rate: multiply it by a small width \(dx\) and you get the approximate
probability \(f(0)\,dx\). The probability of the interval \((-0.1, 0.1]\) is about
0.08.
</details>

<details><summary>2. Does \(\Pr(X \le x) = \Pr(X < x)\) for a continuous variable?</summary>

Yes. The two differ by \(\Pr(X = x)\), which is zero. For a discrete variable they can
differ, and usually do.
</details>

<details><summary>3. Why can a density be larger than 1?</summary>

Because it is measured per unit of \(x\). A uniform on \((0, 0.5)\) must have density
2 so that \(2 \times 0.5 = 1\). Only probabilities are capped at 1, not densities.
</details>

<details><summary>4. What does the gamma shape parameter do?</summary>

It controls how far the mode sits from zero and how symmetric the hump becomes. At
shape 1 the distribution is exponential and decreasing; larger shapes move the mode
right and make the curve bell-like. The mean is shape / rate.
</details>

## Where this connects

- [Module 10](../modules/10-continuous-distributions/chapter.md) develops the
  density, the CDF and each family, with worked examples.
- [Practical 10](../practicals/notebooks/10-continuous-distributions.ipynb) computes
  densities, distributions and quantiles with SciPy.
- [Figures 5.1 and 14.1](../modules/10-continuous-distributions/chapter.md) in the
  module show the empirical rule and three families drawn to the same scale.
- Normal probabilities and z-scores have their own lab: [L-05](normal-and-z-scores.md).

## Next

- [Lab L-05 — The normal distribution and z-scores](normal-and-z-scores.md)
- Back to the [laboratory index](index.md)
