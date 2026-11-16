---
title: "M18 — Bayesian Statistics and Statistical Methods for Data Science"
description: A second inferential paradigm, simulation as a general method, A/B testing, and the statistical discipline of production work.
module: 18
part: 8
level: Advanced
hours: 18
prerequisites: [7, 15, 17]
---

# M18 · Bayesian Statistics and Statistical Methods for Data Science

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--advanced">Advanced</span>
<span class="psds-chip">Part VIII · Modern statistics</span>
<span class="psds-chip">18 study hours</span>
<span class="psds-chip">Module 18 of 18</span>
</div>

## Introduction

This final module does three things that the classical sequence cannot do for itself.

It adds a **second inferential paradigm**. Bayesian statistics treats the parameter as
uncertain and applies conditional probability — the same operation as M07 — to a whole
distribution instead of a single event. Inference then becomes a posterior
distribution, and every summary you need (an estimate, an interval, a probability that
a hypothesis is true) is a summary of that distribution.

It adds **simulation as a general method**. If you can simulate a process, you can
answer questions about it: estimate an integral, approximate a probability too small
for enumeration, quantify the error of your own estimate, and design a study whose
power you can compute rather than assume.

And it turns the course towards **practice**: A/B testing, experimental design,
multiple metrics, data leakage, distribution shift, and the ethics of statistical
claims. M18 is where the previous seventeen modules stop being a curriculum and start
being a toolkit.

## Why this matters

The Bayesian paradigm is not a competitor to be chosen tribally; it is a different set
of answers to different questions. "What should I believe now?" is Bayesian; "how often
would this procedure be wrong?" is frequentist. Knowing which question you are asking
is the skill.

Simulation matters because most realistic problems have no closed form. The Monte Carlo
standard error is the honest statement of how much you know, and designing a simulation
is now a core professional skill.

Practice matters because the failure modes of deployed statistics are not mathematical:
they are peeking at experiments, optimising the wrong metric, leaking the future into
the features, and reporting a significant result that nobody can reproduce.

## Learning objectives

By the end of this module you can:

1. State the Bayesian framework and contrast it with the frequentist one in terms of
   what is random, what is fixed, and what a probability statement means.
2. Derive conjugate posteriors for Beta–Bernoulli, Gamma–Poisson and Normal–Normal.
3. Interpret posterior mean, median and mode, and explain shrinkage.
4. Construct and interpret a credible interval and state the difference from a
   confidence interval without caricature.
5. Choose a prior and conduct a sensitivity analysis.
6. Compare models with marginal likelihood and Bayes factors, and state their
   limitations.
7. Explain why most posteriors are intractable, describe MCMC at a conceptual level,
   and diagnose convergence with trace plots, \(\hat R\) and effective sample size.
8. Fit a Bayesian model in PyMC (or by conjugate updating) and report the posterior with
   uncertainty.
9. Generate random variables by inverse transform and rejection sampling, and prove
   correctness.
10. Estimate integrals and expectations by Monte Carlo, quantify the error, and apply
    variance reduction.
11. Design and analyse an A/B test: metric, unit of randomisation, minimum detectable
    effect, sample size, stopping rule, guardrails.
12. Identify peeking, multiple metrics, novelty effects, leakage and distribution shift,
    and explain their statistical consequences.
13. Write a statistical analysis plan and a reproducible report with stated limitations.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Bayes' theorem and conditional probability | [M07](07-conditional-probability-and-bayes.md) | Units 1, 4 |
| Estimation, intervals, testing | [M14](14-estimation-and-confidence-intervals.md), [M15](15-hypothesis-testing.md) | — |
| Permutation and bootstrap | [M17](17-anova-chi-square-nonparametric.md) | Unit 6 |
| Beta, gamma, normal families | [M10](10-continuous-distributions.md) | Units 3–5 |
| CLT and convergence | [M13](13-law-of-large-numbers-and-clt.md) | — |

## Topic breakdown

### Unit 1 — The Bayesian framework (2.5 h)

- What is random: parameters (Bayesian) versus data (frequentist).
- Prior, likelihood, posterior: \(p(\theta\mid y)\propto p(y\mid\theta)p(\theta)\).
- The posterior as a complete answer; summaries as decisions about what to report.
- Priors: informative, weakly informative, reference; why "non-informative" is a
  misnomer.
- Subjectivity as transparency: the prior is stated rather than hidden.
- Where the paradigms agree and where they genuinely diverge.

### Unit 2 — Conjugate updating (3 h)

- Beta–Bernoulli: prior \(a,b\); posterior \(a+\sum y_i,\ b+n-\sum y_i\).
- Gamma–Poisson: rate estimation with count data.
- Normal–Normal: precision addition; posterior mean as a precision-weighted average of
  prior and data.
- Shrinkage: the posterior mean is pulled towards the prior, more strongly when data are
  few.
- Sequential updating and equivalence of order.
- Closed-form paths in `scipy.stats`, so the module works without PyMC.

### Unit 3 — Intervals, decisions and comparison (3 h)

- Credible intervals: equal-tailed and highest posterior density.
- The correct comparison with confidence intervals, including where the numbers coincide
  and where the meanings differ.
- Posterior probabilities of hypotheses; the practical appeal and the prior
  sensitivity.
- Bayes factors and marginal likelihood; the Jeffreys scale only as a convention, with
  its criticisms.
- Decision-theoretic framing: expected loss, and why a decision needs a loss function.
- When a Bayesian analysis is worth the complexity, and when it is not.

### Unit 4 — Computation and diagnostics (3 h)

- Why integrals over posteriors are usually intractable.
- MCMC in one paragraph: construct a chain whose stationary distribution is the
  posterior; discard the transient; summarise the rest.
- Convergence diagnostics: trace plots, \(\hat R\) (target \(\approx 1.00\)), effective
  sample size, divergent transitions.
- A deliberately bad fit that fails diagnostics, and what it looks like.
- PyMC walkthrough: model specification, sampling, posterior predictive checks.
- Prior and likelihood sensitivity analysis as standard practice.

### Unit 5 — Monte Carlo as a method (3 h)

- Pseudo-random generators, seeds, and why the modern `Generator` API is preferred.
- Inverse-transform sampling: \(X=F^{-1}(U)\), with proof.
- Rejection sampling: acceptance probability and efficiency.
- Monte Carlo integration and its \(O(1/\sqrt{B})\) error; reporting the error honestly.
- Variance reduction: antithetic variates, control variates, stratified sampling,
  importance sampling for rare events.
- Designing a simulation study: what to vary, how many replications, what to report.
- Simulation-based power analysis as the general tool.

### Unit 6 — Experiments and A/B testing (2.5 h)

- The design checklist: metric, unit of randomisation, MDE, sample size, duration,
  stopping rule, guardrails, pre-registered analysis.
- Sample-size calculation for a two-proportion test; power curves.
- Peeking and sequential testing: why the naive p-value is invalid under optional
  stopping, and what to do instead.
- Multiple metrics and multiplicity; primary versus secondary outcomes.
- Novelty effects, interference between units, and network effects.
- Bayesian A/B analysis as an alternative, with its own assumptions.
- Reading a result: effect size, interval, decision, and what would change your mind.

### Unit 7 — Statistical practice and its failure modes (2 h)

- **Leakage**: target leakage, temporal leakage, preprocessing before splitting —
  demonstrated with a pipeline that looks excellent and generalises badly.
- Cross-validation correctly applied; why it is not a hypothesis test.
- Distribution shift, monitoring, and feedback loops in deployed systems.
- Metric design: proxies, gaming, and the difference between what is measured and what
  matters.
- Uncertainty communication: intervals, not point estimates, and honest language about
  what is not known.
- Ethics: privacy, group fairness, the consequences of false positives at scale.
- The capstone brief: question, plan, data, method, diagnostics, report.

## Important mathematical concepts

**Bayes' theorem for distributions.**

\[ \underbrace{p(\theta\mid y)}_{\text{posterior}}
   \;=\;
   \frac{\underbrace{p(y\mid\theta)}_{\text{likelihood}}\;
         \underbrace{p(\theta)}_{\text{prior}}}
        {\underbrace{p(y)}_{\text{evidence}}}
   \;\propto\; p(y\mid\theta)\,p(\theta) \]

**Beta–Bernoulli conjugacy.**

\[ \theta\sim\mathrm{Beta}(a,b),\quad y_i\sim\mathrm{Bern}(\theta)
   \;\Longrightarrow\;
   \theta\mid y\sim\mathrm{Beta}\!\left(a+\sum y_i,\; b+n-\sum y_i\right) \]

**Normal–Normal posterior mean** (precision-weighted):

\[ \E[\theta\mid y]=\frac{\frac{\mu_0}{\tau_0^{2}}+\frac{n\bar y}{\sigma^{2}}}
                        {\frac{1}{\tau_0^{2}}+\frac{n}{\sigma^{2}}} \]

*In words:* the posterior mean is a weighted average of the prior mean and the data
mean, weighted by how precise each is.

**Monte Carlo error.**

\[ \hat\mu_B=\frac{1}{B}\sum_{b=1}^{B} g(X_b), \qquad
   \se(\hat\mu_B)\approx\frac{s_g}{\sqrt{B}} \]

**Inverse-transform sampling.**

\[ U\sim\mathrm{U}(0,1) \;\Longrightarrow\; X=F^{-1}(U)\sim F \]

## Expected knowledge after completion

You can, without notes:

- Derive a Beta posterior from a Bernoulli sample and interpret the shrinkage.
- Explain what a credible interval says that a confidence interval does not.
- Read an MCMC trace and \(\hat R\) and decide whether the fit is usable.
- Sample from a distribution by inverse transform, and prove the method is correct.
- Compute a Monte Carlo estimate with an honest error bar.
- Design an A/B test with a pre-specified MDE and sample size, and explain why peeking
  invalidates the p-value.
- Demonstrate data leakage in a pipeline and quantify the resulting optimism.

## Connections to Data Science

- **Bayesian methods** in production: Thompson sampling for bandits, hierarchical models
  for small segments, calibration of predicted probabilities.
- **Resampling** is the default uncertainty tool when no formula exists.
- **Simulation** is how power and risk are computed for anything non-standard.
- **Experiment design** is the difference between a metric movement and a finding.
- **Leakage and shift** are the two most common reasons a model that scored well fails
  in production.

## Practical applications

| Setting | Question | Method |
|---|---|---|
| Conversion rate | How uncertain is the rate after 40 conversions? | Beta posterior |
| Two variants | Should we ship B? | A/B with MDE, power, guardrails |
| Rare-event risk | Probability of a 5-sigma loss? | Importance sampling |
| Small segment | Can we estimate this group's rate? | Hierarchical shrinkage |
| Deployed model | Is performance decaying? | Distribution-shift monitoring |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 8 | Conjugate updates; Monte Carlo error |
| ★★ Application | 8 | Bayesian analysis with priors justified; A/B design; simulation study |
| ★★★ Challenge | 5 | Prior sensitivity; MCMC diagnostics on a failing fit; importance sampling; leakage audit; capstone proposal |
| Quiz | 10 items | Paradigm comparison and practice failures |
| Practical notebook | 1 | Bayesian versus frequentist analysis of the same data |
| Capstone | 1 | Complete investigation with analysis plan, diagnostics and reproducible report |

**Capstone rubric (100 marks):** design 20, method 20, assumption audit 20,
reproducibility 20, communication 20.

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: the framework | 2.5 |
| 2 | Unit 2: conjugate updating | 3.0 |
| 3 | Unit 3: intervals and model comparison | 3.0 |
| 4 | Unit 4: computation and diagnostics | 3.0 |
| 5 | Unit 5: Monte Carlo | 3.0 |
| 6 | Unit 6: experiments | 2.5 |
| 7 | Unit 7: practice, ethics, capstone brief | 1.0 |

**Before this module:** [M17](17-anova-chi-square-nonparametric.md). **After:** the
capstone, and then the follow-on topics named in the [course roadmap](../roadmap.md).
