---
title: "M06 — Probability Fundamentals"
description: Sample spaces, events, Kolmogorov's axioms, and the rules every later probability statement is derived from.
module: 6
part: 2
level: Core
hours: 14
prerequisites: [5]
---

# M06 · Probability Fundamentals

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part II · Probability</span>
<span class="psds-chip">14 study hours</span>
<span class="psds-chip">Module 6 of 18</span>
</div>

## Introduction

Probability begins with a decision that looks trivial and is not: what are the
possible outcomes? Everything that follows — the probabilities you compute, the
distributions you derive, the simulation you run — is relative to that choice. Get
the sample space wrong and every subsequent step is faithfully wrong.

This module formalises the model. A sample space \(\Omega\) is the set of outcomes;
an event is a subset; probability is a function on events satisfying three axioms.
From those three lines, every rule you have ever used — complement, addition,
inclusion–exclusion, monotonicity — is derived, not assumed.

That derivation is the point. A student who has derived \(\Pr(A^c) = 1-\Pr(A)\) from
the axioms knows *why* probabilities cannot exceed 1. A student who has memorised it
knows only that it is usually true.

## Why this matters

The axioms look abstract and are extremely practical. Three consequences you will
use constantly:

1. **You can always compute a complement instead.** "At least one" problems are
   almost always easier as \(1 - \Pr(\text{none})\), and that identity is a theorem.
2. **Adding probabilities of non-disjoint events double-counts.** Every
   inclusion–exclusion correction comes from one axiom about disjoint unions.
3. **A probability model can be wrong even when it is internally consistent.** The
   axioms constrain the arithmetic, not the modelling. Choosing \(\Omega\) and
   assigning probabilities is a scientific act, and it can fail.

The module also introduces the three interpretations of probability — classical,
frequentist, subjective — because data scientists switch between them without
noticing, and mixing them produces incoherent arguments.

## Learning objectives

By the end of this module you can:

1. Define a sample space for a described experiment, distinguishing outcomes from
   events, and identify the event algebra (union, intersection, complement).
2. State Kolmogorov's three axioms and derive the standard consequences from them:
   \(\Pr(\emptyset)=0\), the complement rule, monotonicity, the addition rule,
   inclusion–exclusion, and Boole's inequality.
3. Compute probabilities under the classical, frequentist and subjective
   interpretations, and say which interpretation a given statement uses.
4. Translate a word problem into events, then into a computation, without ambiguity.
5. Use combinatorial counting inside the axiomatic framework for equally likely
   outcomes.
6. Apply the continuity property of probability to increasing and decreasing
   sequences of events.
7. Explain why not every subset needs to be an event (the σ-algebra idea, without
   measure theory).
8. Verify axiom-derived identities by simulation and interpret the residual
   discrepancy as Monte Carlo error.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Combinations and permutations | [M05](05-counting-and-combinatorics.md) | Units 2–3 |
| Sets: union, intersection, complement, De Morgan | [M02](02-mathematical-foundations.md) | Unit 1 |
| Summation notation | M02 | Unit 3 |

## Topic breakdown

### Unit 1 — Experiments, outcomes and sample spaces (2 h)

- Random experiment: repeatable, known set of outcomes, unpredictable result.
- Discrete, countably infinite and continuous sample spaces.
- Choosing the right granularity: coin tosses versus sequences of tosses.
- Events as subsets; \(\Omega\) (certain) and \(\emptyset\) (impossible).
- Set operations on events and their verbal translations ("and", "or", "not").
- **Worked discipline:** write \(\Omega\), then the event, then count — in that order.

### Unit 2 — The axioms (2.5 h)

- Axiom 1: \(\Pr(A) \ge 0\).
- Axiom 2: \(\Pr(\Omega) = 1\).
- Axiom 3: countable additivity for disjoint events.
- Derivations: \(\Pr(\emptyset)=0\); \(\Pr(A^c)=1-\Pr(A)\);
  \(A\subseteq B \Rightarrow \Pr(A)\le\Pr(B)\);
  \(\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)\);
  inclusion–exclusion for three events; Boole's inequality.
- Why the axioms are sufficient: what they forbid (negative probabilities, sums above
  one) and what they leave open (which model is correct).
- The σ-algebra remark: for continuous spaces, not every subset can be an event;
  this course states the fact and does not require the machinery.

### Unit 3 — Interpretations of probability (1.5 h)

- Classical: equally likely outcomes — and the circularity it hides.
- Frequentist: limiting relative frequency; why "the limit exists" is an assumption.
- Subjective/Bayesian: degree of belief, coherence, and betting odds.
- When each is appropriate; how the same sentence can be read three ways.
- The law of total probability preview and where the interpretations diverge (M07,
  M18).

### Unit 4 — Combinatorial probability (3 h)

- Equally likely outcomes: \(\Pr(A) = |A|/|\Omega|\) with \(|\Omega|\) counted
  correctly.
- Sampling with and without replacement, ordered and unordered — the four-case table.
- Occupancy problems; the birthday problem as an application.
- Verification by enumeration and by simulation.
- The classic error: treating distinguishable outcomes as identical and thereby
  changing the measure.

### Unit 5 — Conditioning preview and independence (2 h)

- Conditional probability defined (full treatment in M07).
- Independence as factorisation: \(\Pr(A\cap B)=\Pr(A)\Pr(B)\).
- Why independence is a modelling assumption, not a conclusion from data alone.
- Mutual independence for \(n\) events; a preview of the pairwise-versus-mutual gap
  (proved in M07).
- Independence versus disjointness — the most common conceptual mix-up in the course.

### Unit 6 — Continuity and limits of events (1 h)

- Increasing sequences \(A_1 \subseteq A_2 \subseteq \cdots\):
  \(\Pr(\cup A_n) = \lim_n \Pr(A_n)\).
- Decreasing sequences and their limit.
- Why this matters for infinite sample spaces and for limiting arguments in M13.

### Unit 7 — Simulation as a check (2 h)

- Simulating an experiment in Python; counting relative frequencies.
- Comparing empirical and theoretical probabilities as \(B\) grows.
- Monte Carlo error: \(\text{se} = \sqrt{p(1-p)/B}\), and reporting it honestly.
- When simulation is the only feasible method (forward link to M18).

## Important mathematical concepts

**The three axioms.**

\[ \text{(A1)}\;\Pr(A)\ge 0, \qquad
   \text{(A2)}\;\Pr(\Omega)=1, \qquad
   \text{(A3)}\;\Pr\!\left(\bigcup_{i} A_i\right)=\sum_{i}\Pr(A_i) \;\text{ for disjoint } A_i \]

**The addition rule** (a consequence, not an axiom):

\[ \Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B) \]

**Boole's inequality** — the union bound used everywhere in data science:

\[ \Pr\!\left(\bigcup_{i=1}^{n} A_i\right) \le \sum_{i=1}^{n}\Pr(A_i) \]

**Complement rule**, the workhorse of "at least one" problems:

\[ \Pr(\text{at least one}) = 1 - \Pr(\text{none}) \]

## Expected knowledge after completion

You can, without notes:

- Write the sample space and event for a described experiment, then compute the
  probability by counting.
- Derive the complement rule and the addition rule from the axioms in three lines
  each.
- Explain the difference between disjoint and independent with an example.
- Compute the probability of at least one success in \(n\) independent trials both
  directly and by complement, and show they agree.
- State Boole's inequality and use it to bound the chance of any error in 20
  independent tests.

## Connections to Data Science

- **Union bounds** justify why many algorithms tolerate a small per-item failure
  probability (Bloom filters, hashing, skip lists).
- **Independence assumptions** in naive Bayes (M07, M18) are exactly this module's
  factorisation, usually false and usually useful.
- **Simulation** is the standard first move when a probability has no closed form —
  from queueing to A/B test power.
- **Model risk** is the axiom-versus-model distinction: a coherent probability model
  can still be the wrong model for the world.

## Practical applications

| Setting | Question | Concept |
|---|---|---|
| Reliability | Probability at least one server fails in a year? | Complement rule |
| Fraud screening | Probability any of 50 alerts is a false positive? | Boole's inequality |
| Survey design | Probability a sample contains no defective item? | Combinatorial probability |
| Games and lotteries | Is the advertised odds calculation right? | Equally likely outcomes |
| Simulation studies | How close is 10,000 replications to the truth? | Monte Carlo error |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 10 | Axiom consequences and direct computation |
| ★★ Application | 6 | Model a described experiment; compute and verify |
| ★★★ Challenge | 3 | Prove a derived rule; Boole bound; show a pairwise-independent example fails mutual independence |
| Quiz | 10 items | Concepts and interpretation |
| Practical notebook | 1 | Simulate five experiments and compare with theory |
| Simulation lab | 1 | Coin and dice experiments following the eight-step protocol |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: sample spaces and events | 2.5 |
| 2 | Unit 2: axioms and derivations | 3.0 |
| 3 | Unit 3: interpretations | 1.5 |
| 4 | Unit 4: combinatorial probability | 3.0 |
| 5 | Units 5–6: independence preview, continuity | 2.0 |
| 6 | Unit 7: simulation check | 2.0 |

**Before this module:** [M05](05-counting-and-combinatorics.md). **After:**
[M07 — Conditional Probability and Bayes' Theorem](07-conditional-probability-and-bayes.md)
adds information to the model.
