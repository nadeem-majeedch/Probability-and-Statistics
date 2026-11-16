---
title: Part IV — Sampling and Limit Theorems
description: Sampling distributions, the Law of Large Numbers and the Central Limit Theorem. Modules M12–M13.
---

# Part IV — Sampling and Limit Theorems

**Modules M12–M13 · 26 study hours · Core, one advanced · Prerequisites: Parts I–III**

---

## Why this part exists

Part IV is the hinge of the course. Up to here, probability has been the subject. From
here, statistics begins, and the question changes to: *what can a sample tell me about a
population?*

The concept that makes the change possible is the **sampling distribution**. A statistic
computed from data is itself random, because the data are random, and it has its own
distribution. Once you see that, a confidence interval stops being a formula and becomes
an obvious consequence: if the sample mean varies from sample to sample with a known
spread, then an interval around it captures the population mean a known fraction of the
time.

Most students who "do not understand p-values" are missing this idea, not the
arithmetic. Then M13 explains why those distributions look the way they do — and,
crucially, when the explanation fails. Averages of heavy-tailed data do not behave, and
no sample size rescues them.

## Modules

| # | Module | Level | Hours | Focus |
|---|---|---|---|---|
| M12 | [Sampling and Sampling Distributions](../modules/12-sampling-and-sampling-distributions.md) | Core | 14 | i.i.d. samples, standard error, χ², t and F distributions, degrees of freedom |
| M13 | [Law of Large Numbers and the CLT](../modules/13-law-of-large-numbers-and-clt.md) | Advanced | 12 | Modes of convergence, WLLN, CLT, continuity correction, delta method, failures |

## What you will be able to do

- Explain, without using the word "formula", why the standard error is σ/√n and why
  halving the error costs four times the sample.
- Run a sampling experiment and overlay the theoretical distribution on the empirical
  histogram.
- Distinguish the standard deviation of the data from the standard error of an estimate.
- State the CLT with its conditions, and demonstrate its failure on a Cauchy population.
- Judge whether a normal approximation is defensible for a given dataset and sample
  size, using simulation rather than rule of thumb.

## Simulation experiments in this part

The sampling machine (histograms of x̄ and s² across thousands of samples), the running
mean for normal versus Cauchy data, and a CLT grid of four populations × four sample
sizes with Q–Q plots.

**Interactive lab:** [the Central Limit Theorem](../labs/clt.md) — five populations,
sample sizes 1–200, with the reasons for failure explained on the page.

## Common misconceptions this part removes

| Misconception | Corrected in |
|---|---|
| "The standard error is the standard deviation of the sample" | M12 |
| "The sampling distribution is the distribution of the data" | M12 |
| "The data become normal as *n* grows" | M13 |
| "*n* > 30 is always enough for the CLT" | M13 |
| "The LLN says the sample will look like the population" | M13 |

## Start

Begin with [M12 — Sampling and Sampling Distributions](../modules/12-sampling-and-sampling-distributions.md),
and open [the CLT lab](../labs/clt.md) before reading M13 Unit 3 — the theorem is easier
to state once you have watched it happen.
