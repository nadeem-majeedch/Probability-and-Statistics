---
title: "M01 — Introduction to Probability and Statistics"
description: What statistics is for, how a statistical investigation works, and the vocabulary the next seventeen modules assume.
module: 1
part: 1
level: Beginner
hours: 6
prerequisites: []
---

# M01 · Introduction to Probability and Statistics

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--beginner">Beginner</span>
<span class="psds-chip">Part I · Foundations</span>
<span class="psds-chip">6 study hours</span>
<span class="psds-chip">Module 1 of 18</span>
</div>

## Introduction

Before a single formula, this module answers a question that students rarely ask
out loud: *what is statistics actually for?* Not "what is the mean", but why a
discipline built on averages and variability exists at all, and why data science
cannot be done without it.

Statistics is the study of how to learn from incomplete information. You never see
the whole population — you see a sample, with error, collected for reasons that may
not match your question. Everything that follows in this course is machinery for
making defensible statements in that situation, and for stating honestly how wrong
they might be.

This module also sets the map for the course: what probability contributes, what
inference contributes, where computation sits, and how to study the material
without an instructor.

## Why this matters

Two failure modes dominate applied work, and both are conceptual, not computational.

The first is **answering a question you did not ask**. A pipeline can compute a
p-value perfectly and still be meaningless because the sample was selected in a way
that makes the test inapplicable.

The second is **mistaking precision for knowledge**. More data narrows an interval;
it does not remove bias, and it does not turn an observational association into a
causal claim.

Both failures are prevented by the vocabulary in this module: population, sample,
parameter, statistic, estimator, bias, variability, and study design. Learning these
words precisely now saves you from the most common errors in the other seventeen
modules.

## Learning objectives

By the end of this module you can:

1. Define statistics as a discipline and distinguish its descriptive and inferential
   branches, giving an example of each.
2. Use the terms population, sample, parameter, statistic, estimator and estimate
   correctly, including which symbols belong to which.
3. Classify a variable by type and measurement scale, and state what each
   classification permits (arithmetic, ordering, averages).
4. Describe the stages of a statistical investigation, from question to
   communication, and identify where an analysis can fail at each stage.
5. Distinguish observational studies from experiments, and explain why only one
   supports causal language.
6. Name the main sources of bias and explain how each corrupts an estimate.
7. Explain the role of probability in statistical inference, in one paragraph,
   without circular definitions.
8. Identify at least five ways a published statistical claim can mislead, using real
   categories rather than vague suspicion.

## Prerequisites

**None.** School algebra is assumed; nothing else.

| Need | Where it comes from | If you are unsure |
|---|---|---|
| Arithmetic, fractions, percentages | school mathematics | — |
| Reading a two-way table | everyday experience | see Unit 2 |

## Topic breakdown

### Unit 1 — What statistics is (0.5 h)

- Descriptive statistics: summarising what is in the data.
- Inferential statistics: saying something about a population from a sample.
- Probability as the bridge: the mathematics of uncertainty that makes inference
  possible.
- Why the three are inseparable: description without inference is bookkeeping;
  inference without probability is opinion.

### Unit 2 — Populations, samples and the objects of inference (1 h)

- Population, sampling frame, sample, census.
- Parameter versus statistic; Greek letters for parameters, Roman for statistics.
- Estimator versus estimate: the rule versus the number it produced.
- Sampling variability: two samples from the same population give different
  answers — demonstrated, not asserted.
- Why "the sample mean" is a random variable (forward link to M12, where this
  becomes the central idea).

### Unit 3 — Variables and measurement scales (1 h)

- Quantitative versus categorical; discrete versus continuous.
- Nominal, ordinal, interval, ratio — and what each scale permits.
- Why averaging an ordinal scale is usually illegitimate, and when it is defensible.
- Identifier columns, dates, and text as data: common traps.
- Derived variables, and the cost of binning a continuous variable.

### Unit 4 — The statistical investigation (1.5 h)

- The workflow: question → design → collect → clean → explore → model → check →
  communicate.
- Where each stage fails, with one concrete example per stage.
- Pre-specification: why writing the plan before seeing the data protects you.
- Data provenance and documentation: what you must record to make work reproducible.
- Reproducibility as a professional standard, not a courtesy.

### Unit 5 — Study design and the limits of evidence (1 h)

- Observational study versus experiment; randomisation, control, blinding, placebo.
- Confounding, reverse causation, selection and survivorship bias.
- The causal hierarchy: association → temporal order → mechanism → counterfactual.
- Why "statistically significant" and "causally established" are different claims.

### Unit 6 — Statistical literacy and ethics (0.5 h)

- Common distortions: truncated axes, base-rate neglect, multiple comparisons,
  p-hacking, cherry-picked subgroups.
- Ethics: honest reporting, privacy, the consequences of error for real people.
- Professional standards (for example the ASA's ethical guidelines) as the reference
  point.

### Unit 7 — The course map (0.5 h)

- What each of the eighteen modules contributes, and the dependency graph.
- How to use the interactive labs, notebooks and self-assessment.
- The seven-step study protocol and what "finished" means for a module.

## Important mathematical concepts

This module is conceptual, but three notational conventions start here and are used
for the rest of the course.

**Population versus sample mean.** A parameter is a fixed unknown number; a
statistic is a random quantity computed from data.

\[ \mu \quad\text{(population mean, unknown, fixed)} \qquad
   \bar{x} \quad\text{(sample mean, known, varies by sample)} \]

**Summation notation, read aloud.** The average of \(n\) observations:

\[ \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i \]

*In words:* add up all the values, then divide by how many there are. The index \(i\)
runs from 1 to \(n\); \(x_i\) is the \(i\)-th observation.

**The two-way table** as the simplest joint summary — rows, columns, margins, and
the conditional proportions that will become conditional probability in M07.

## Expected knowledge after completion

You can, without notes:

- State the difference between descriptive and inferential statistics and give an
  example of each.
- Say what \(\mu\) and \(\bar{x}\) are, and why one has a distribution and the
  other does not.
- Classify five given variables by type and scale, and justify what arithmetic is
  legal for each.
- Explain why a large convenience sample can be worse than a small random one.
- Name four sources of bias and the direction each pushes an estimate.
- Describe the eight stages of a statistical investigation and one failure mode per
  stage.

## Connections to Data Science

Every modelling pipeline contains this module's content, usually invisibly.

- **Feature typing** is measurement-scale reasoning: one-hot encoding is the
  admission that a nominal variable has no order, and treating a coded category as
  a number is the error it prevents.
- **Train/test splits** exist because of sampling variability: a model's score is a
  statistic with a distribution, not a property of the model.
- **Data leakage** is a design failure of the kind described in Unit 4 — information
  from the future or from the target contaminating the predictors.
- **Dashboard discipline** is descriptive statistics done honestly: choosing summaries
  that do not hide the distribution.
- **Ethics review** of a model is Unit 6 applied to a system rather than an article.

## Practical applications

| Setting | Question | What this module contributes |
|---|---|---|
| A university wants to know if a new teaching method works | Causal or observational? | Design vocabulary: randomisation, control, confounding |
| A hospital reviews waiting times | What is "typical"? | Descriptive versus inferential framing; why the mean misleads with skew |
| A retailer segments customers | Can we average this rating? | Measurement scales; ordinal data |
| A news article reports a 30% rise | Is that a finding? | Base rates, selection, and the audit questions to ask |
| A team builds a churn model | Why hold out data? | Sampling variability and generalisation |

## Exercises and assessment plan

| Component | Count | What it tests |
|---|---|---|
| ★ Recall checks | 6 | Definitions used precisely, not approximately |
| ★★ Application | 5 | Classify variables; identify bias in described studies |
| ★★★ Challenge | 2 | Critique a published claim; design a study for a stated question |
| Self-assessment quiz | 10 items | Conceptual grip, with explained answers |
| Practical | 1 short notebook | Load a dataset, type every column, document its provenance |

**Mastery threshold:** 8/10 on the quiz and both ★★ exercises correct. This module
is short but everything later assumes its vocabulary.

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Units 1–2: what statistics is; populations and samples | 1.5 |
| 2 | Unit 3: variables and scales, with a real dataset | 1.5 |
| 3 | Units 4–5: the workflow and study design | 2.0 |
| 4 | Units 6–7: literacy, ethics, course map; quiz and practical | 1.0 |

**After this module:** [M02 — Mathematical Foundations](02-mathematical-foundations.md)
gives you the notation to do the arithmetic this module described.
