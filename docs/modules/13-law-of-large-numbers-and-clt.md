---
title: "M13 — Law of Large Numbers and the Central Limit Theorem"
description: Convergence in probability, why averages stabilise, and why their distributions become normal — and when neither holds.
module: 13
part: 4
level: Advanced
hours: 12
prerequisites: [12]
---

# M13 · Law of Large Numbers and the Central Limit Theorem

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--advanced">Advanced</span>
<span class="psds-chip">Part IV · Sampling and limits</span>
<span class="psds-chip">12 study hours</span>
<span class="psds-chip">Module 13 of 18</span>
</div>

## Introduction

Two limit theorems carry the weight of classical statistics, and they answer different
questions.

The **Law of Large Numbers** says the average converges to the mean: with enough data,
your estimate stops moving. It is a statement about *where* a statistic goes.

The **Central Limit Theorem** says the *distribution* of the average becomes normal,
regardless of the population's shape. It is a statement about the *shape* of the
sampling distribution, and therefore about how to build intervals and tests.

Conflating the two produces the most common error in applied statistics: believing
that "the data become normal as \(n\) grows". They do not. The data keep the shape they
always had; it is the *average* whose distribution becomes normal.

Both theorems have conditions, and this module is as much about the conditions as the
conclusions. The Cauchy distribution has no mean, the sample average of a Cauchy
never settles, and no amount of data fixes it — a fact that matters for anyone working
with heavy-tailed quantities.

## Why this matters

The CLT is the reason a t-test works on non-normal data, why binomial proportions have
normal approximations, and why regression coefficients have t statistics. Without it,
classical inference would apply only to normal populations.

The LLN is the reason simulation works at all: a Monte Carlo estimate is justified by
the same convergence. Every "run it a million times" claim in this course rests here.

And the failure modes are practically important: infinite-variance data (network
traffic, financial returns, some latency distributions) break both theorems, and
practitioners who assume otherwise produce confident nonsense.

## Learning objectives

By the end of this module you can:

1. State the weak law of large numbers and prove it for finite variance using
   Chebyshev's inequality.
2. Distinguish convergence in probability, almost sure convergence, convergence in
   distribution and convergence in mean square, and separate them with examples.
3. Explain what the strong law adds to the weak law, and why the difference matters.
4. State the CLT precisely, including the i.i.d. and finite-variance conditions, and
   prove it in the case where moment generating functions exist.
5. Compute approximate probabilities for sums and means, including continuity
   corrections for discrete variables.
6. Judge when a normal approximation is defensible, using simulation across
   distributions and sample sizes.
7. Explain the role of skewness in the sample size required, and state the practical
   rule of thumb with its caveats.
8. Apply the CLT to proportions and derive the standard error of a proportion.
9. State the delta method and find the asymptotic distribution of a smooth function of
   an estimator.
10. Demonstrate a failure: the Cauchy sample mean does not converge.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Chebyshev, MGFs, moments | [M08](08-random-variables-and-expectation.md) | Units 6 |
| Sampling distributions, standard error | [M12](12-sampling-and-sampling-distributions.md) | Unit 2 |
| Normal distribution and standardisation | [M10](10-continuous-distributions.md) | Unit 4 |
| Limits and series (for the proof) | [M02](02-mathematical-foundations.md) | Units 5, 8 |

## Topic breakdown

### Unit 1 — Modes of convergence (2.5 h)

- Convergence of a sequence of random variables: what has to converge to what.
- Convergence in probability: \(\Pr(|X_n-X|>\epsilon)\to 0\).
- Almost sure convergence: the exceptional set has probability zero.
- Convergence in distribution: CDFs converge at continuity points.
- Convergence in mean square: \(\E[(X_n-X)^2]\to 0\).
- Implication diagram, with counterexamples for the arrows that do not exist.
- Why statisticians care: each mode justifies a different practical claim.

### Unit 2 — The Law of Large Numbers (3 h)

- Weak law: \(\bar{X}_n \xrightarrow{p} \mu\).
- Proof by Chebyshev for finite variance — short, and worth knowing by heart.
- Strong law: \(\bar{X}_n \to \mu\) almost surely; what the stronger claim buys.
- What the LLN does **not** say: the data do not become normal, and the sample does not
  become representative.
- The Cauchy counterexample: no mean, no convergence, no fix.
- Simulation: running averages for normal, exponential and Cauchy samples.

### Unit 3 — The Central Limit Theorem (3.5 h)

- Statement: \(\sqrt{n}(\bar{X}_n-\mu)/\sigma \xrightarrow{d} N(0,1)\).
- Proof sketch via MGFs: the product rule, the Taylor expansion, and the
  \((1+x/n)^n\to e^x\) limit.
- CLT for sums: \(\sum X_i\) is approximately \(N(n\mu, n\sigma^2)\).
- Continuity correction for discrete sums; the binomial example, with and without it.
- Rate of convergence and the role of skewness; Berry–Esseen stated, not proved.
- When it fails: infinite variance, strong dependence, and very heavy skew.

### Unit 4 — Judging the approximation (2 h)

- A simulation grid: four parent distributions × four sample sizes × many
  replications, with Q–Q plots against normal.
- Reading the grid: at what \(n\) does each parent become acceptable?
- Why "\(n>30\)" is a heuristic with a specific origin and specific exceptions.
- Skewness and required \(n\): the practical relationship.
- The consequence for inference: what a bad approximation does to coverage and error
  rates (forward links to M14, M15).

### Unit 5 — Applications (1.5 h)

- CLT for proportions: \(\hat{p}\approx N(p,\,p(1-p)/n)\), and when the approximation
  fails (small \(p\), small \(n\)).
- The delta method: for smooth \(g\), \(\sqrt{n}(g(\bar{X})-g(\mu))\to
  N(0, g'(\mu)^2\sigma^2)\).
- Justifying Monte Carlo error: \(\hat{p}\pm 1.96\sqrt{\hat{p}(1-\hat{p})/B}\).
- Why so much of classical inference is asymptotic rather than exact.

## Important mathematical concepts

**Weak law.**

\[ \bar{X}_n \xrightarrow{\;p\;} \mu \qquad\text{as } n\to\infty \]

**Chebyshev bound used in the proof.**

\[ \Pr\big(|\bar{X}_n-\mu|\ge\epsilon\big)\le \frac{\sigma^{2}}{n\epsilon^{2}}\to 0 \]

**Central Limit Theorem.**

\[ \frac{\sqrt{n}\,(\bar{X}_n-\mu)}{\sigma} \xrightarrow{\;d\;} N(0,1) \]

**Continuity correction** for a sum of discrete variables:

\[ \Pr(S_n \le s) \approx \Phi\!\left(\frac{s+0.5-n\mu}{\sqrt{n}\sigma}\right) \]

**Delta method.**

\[ \sqrt{n}\big(g(\bar{X}_n)-g(\mu)\big) \xrightarrow{\;d\;}
   N\!\left(0,\; \left[g'(\mu)\right]^{2}\sigma^{2}\right) \]

## Expected knowledge after completion

You can, without notes:

- Prove the weak law under finite variance.
- State the CLT with its conditions and explain what each condition excludes.
- Compute a binomial probability by normal approximation with a continuity correction
  and compare it to the exact value.
- Explain why the data do not become normal, using a concrete simulation.
- Give an example where the CLT fails and say why no sample size rescues it.

## Connections to Data Science

- **Monte Carlo error bars** are the CLT applied to a simulation.
- **A/B test asymptotics** are CLT-based; knowing the conditions tells you when a
  permutation test (M17) is the better tool.
- **Bootstrap consistency** depends on these limit theorems; the bootstrap fails in the
  same heavy-tailed cases.
- **Confidence in aggregate metrics** is a sampling-distribution claim, not a statement
  about the data.
- **Heavy-tailed telemetry** (latency, file sizes) is where practitioners most often
  violate the assumptions silently.

## Practical applications

| Setting | Question | Concept |
|---|---|---|
| Simulation study | How precise is this estimate? | CLT for Monte Carlo |
| Conversion rate | Is the normal approximation adequate at 0.4%? | Small-\(p\) failure |
| Audit | How many samples for a stated precision? | \(\sqrt{n}\) law |
| Financial returns | Why do confidence intervals misbehave? | Infinite variance |
| Derived metric | Standard error of a ratio? | Delta method |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 6 | Approximation computations |
| ★★ Application | 6 | Simulation grid; continuity correction; proportion approximations |
| ★★★ Challenge | 4 | Chebyshev proof of the WLLN; MGF proof of the CLT; Cauchy failure; delta method |
| Quiz | 10 items | Statements, conditions, and what each theorem does not claim |
| Practical notebook | 1 | The CLT grid, with a written judgement per cell |
| Simulation lab | 1 | [CLT lab](../labs/clt.md): five populations, sample sizes 1–200 |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: modes of convergence | 2.5 |
| 2 | Unit 2: the law of large numbers | 3.0 |
| 3 | Unit 3: the CLT | 3.5 |
| 4 | Unit 4: judging the approximation | 2.0 |
| 5 | Unit 5: applications | 1.5 |

**Before this module:** [M12](12-sampling-and-sampling-distributions.md). Use the
[CLT lab](../labs/clt.md) before reading Unit 3 — the theorem is easier to state once
you have watched it happen. **After:** [M14 — Estimation and Confidence
Intervals](14-estimation-and-confidence-intervals.md).
