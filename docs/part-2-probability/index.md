---
title: Part II — Probability
description: Counting, probability fundamentals, conditional probability and Bayes' theorem. Modules M05–M07.
---

# Part II — Probability

**Modules M05–M07 · 38 study hours · Core · Prerequisite: Part I**

---

## Why this part exists

Probability is a mathematical model of uncertainty, and models are built from axioms,
not from formulas. This part builds it in the order that makes the axioms feel
inevitable.

Counting comes first (M05) for a practical reason: when outcomes are equally likely,
probability *is* counting, and you can compute exact answers by hand. That gives you a
laboratory in which to test the axioms before they become abstract. M06 then states
Kolmogorov's three axioms and derives everything else — complement, addition,
inclusion–exclusion, continuity. Nothing is asserted that cannot be derived from those
three lines.

M07 is the conceptual payoff, and the part of probability that data science uses
daily. Conditional probability formalises "information changes probabilities", and
Bayes' theorem shows how to reverse a conditional — the operation behind diagnostic
testing, spam filtering, naive Bayes and every Bayesian model in M18.

The single most consequential idea in this part is that **P(A|B) ≠ P(B|A)**. Doctors,
courts and classifiers have all gone wrong by ignoring it.

## Modules

| # | Module | Level | Hours | Focus |
|---|---|---|---|---|
| M05 | [Counting and Combinatorics](../modules/05-counting-and-combinatorics.md) | Beginner | 10 | Multiplication rule, permutations, combinations, multinomial, inclusion–exclusion |
| M06 | [Probability Fundamentals](../modules/06-probability-fundamentals.md) | Core | 14 | Sample spaces, axioms, derived rules, interpretations, combinatorial probability |
| M07 | [Conditional Probability and Bayes' Theorem](../modules/07-conditional-probability-and-bayes.md) | Core | 14 | Conditioning, total probability, independence, Bayes, base rates, naive Bayes |

## What you will be able to do

- Decide whether order matters in a counting problem, and justify the choice.
- Derive the standard probability rules from three axioms.
- Use a tree diagram to apply the law of total probability, and check it numerically.
- Compute a positive predictive value from sensitivity, specificity and prevalence — and
  explain why a 99% accurate test can be wrong most of the time it fires.
- Distinguish independence from conditional independence, with counterexamples for both
  directions.

## Simulation experiments in this part

Coin tossing, dice sums, card draws without replacement, Monty Hall, and diagnostic
screening — each following the standard eight-step protocol: theory, experiment,
expected result, code, output, comparison, why they differ, and a modification task.

## Common misconceptions this part removes

| Misconception | Corrected in |
|---|---|
| "Mutually exclusive means independent" | M06, M07 |
| "P(A ∪ B) = P(A) + P(B) always" | M06 |
| "P(A\|B) = P(B\|A)" | M07 |
| "Independence of pairs implies mutual independence" | M07 |
| "A 99% accurate test means a 99% chance you have the disease" | M07 |

## Start

Begin with [M05 — Counting and Combinatorics](../modules/05-counting-and-combinatorics.md).
