---
title: Part VIII — Modern Statistics
description: Bayesian inference, Monte Carlo, experiments and statistical practice. Module M18.
---

# Part VIII — Modern Statistics

**Module M18 · 18 study hours · Advanced · Prerequisites: Parts I–VII**

---

## Why this part exists

The classical sequence ends with a set of procedures. This part asks what to do when the
procedures do not fit: when you have prior information, when the model has no closed
form, when the question is "what should we ship", or when the analysis has to survive
contact with production.

Three strands, deliberately joined. **Bayesian inference** applies conditional
probability to a whole distribution rather than a single event, so the answer to a
question is a posterior you can summarise as you choose. **Simulation** replaces closed
forms with computation: sample the process, average the outcome, report the Monte Carlo
error. **Practice** turns the toolkit outwards — experiment design, A/B testing,
leakage, shift, and the ethics of claims made at scale.

The capstone lives here. It is the moment the course asks you to run a complete
investigation: question, design, data, method, diagnostics, report.

## Module

| # | Module | Level | Hours | Focus |
|---|---|---|---|---|
| M18 | [Bayesian Statistics and Statistical Methods for Data Science](../modules/18-bayesian-and-data-science-methods.md) | Advanced | 18 | Priors and posteriors, conjugacy, credible intervals, MCMC, Monte Carlo, A/B testing, leakage, ethics, capstone |

## What you will be able to do

- Derive a conjugate posterior and explain shrinkage in one sentence.
- Say what a credible interval claims that a confidence interval does not, without
  caricaturing either.
- Read MCMC diagnostics and decide whether a fit is usable.
- Sample from a distribution by inverse transform and prove the method correct.
- Design an A/B test with a pre-specified MDE, sample size and stopping rule, and explain
  why peeking invalidates the p-value.
- Detect data leakage in a pipeline and quantify the optimism it creates.
- Deliver a reproducible capstone with an analysis plan, diagnostics and honest
  limitations.

## Simulation experiments in this part

Beta–Bernoulli updating as a picture; MCMC on a known posterior; inverse-transform and
rejection sampling validated against theory; a leakage demonstration where the
cross-validated score is excellent and the held-out score is not.

## Common misconceptions this part removes

| Misconception | Corrected in |
|---|---|
| "Bayesian and frequentist answers always differ" | M18 |
| "A flat prior is objective" | M18 |
| "The posterior mean is the most probable value" | M18 |
| "Monte Carlo is exact if you run enough samples" | M18 |
| "Checking an experiment daily is harmless" | M18 |
| "Cross-validation is a hypothesis test" | M18 |

## Start

Begin with [M18 — Bayesian Statistics and Statistical Methods for Data Science](../modules/18-bayesian-and-data-science-methods.md),
and read the capstone brief in Unit 7 before your first session so the module has a
destination.
