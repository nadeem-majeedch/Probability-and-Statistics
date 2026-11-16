---
title: How to study this course
description: A seven-step self-study protocol, a weekly rhythm, and what to do when you get stuck.
---

# How to study this course

This course is written for independent study, which means the responsibility for
learning sits with you — and so does the method. What follows is the method that
makes self-study work. It is not decoration; students who skip steps 3 and 7 are
the students who "understand" a module and then cannot use it a month later.

## The seven-step protocol

Use this for every module. It takes about three hours for a typical module.

### 1. Skim first (10 minutes)

Read the learning objectives and the summary at the end. Do not try to understand
anything yet. You are building a frame: *what is this module for, and where does it
end?*

### 2. Read the concept, not the equations (20 minutes)

Read the "idea in plain language" section and stop before the algebra. Then close
the page and say the idea out loud in your own words. If you cannot, reread — do
not push forward into notation with a fuzzy concept.

### 3. Derive with a pencil (30 minutes)

Cover the derivation and reproduce it line by line on paper. This is the step
almost everyone skips, and it is the one that produces competence.

When you get stuck, do not immediately uncover the page. Write down precisely
where you stopped and what you expected to see. *Then* uncover it and find the
difference. That difference is the thing you are learning.

### 4. Run the code (20 minutes)

Type the Python demonstration; do not paste it. Then change one parameter and
**predict the output before running it**. A prediction that is wrong teaches you
more than ten that are right.

### 5. Do the exercises (45 minutes)

Start at ★ and work upward. Attempt every problem before reading its solution. If
you are stuck for more than fifteen minutes, read only the *first line* of the
solution, then try again.

### 6. Quiz yourself (10 minutes)

Aim for 8 out of 10. Below that, return to step 3 for the sections you missed —
not to the quiz. Quizzes diagnose; derivations cure.

### 7. Write a five-line summary (10 minutes)

Without looking at the page, write: the central result, the formula, one
assumption, one way it fails, and one thing you can now do. This is the highest-value
ten minutes in the protocol.

## A weekly rhythm

| Day | Work | Time |
|---|---|---|
| Mon–Tue | Module *n*: steps 1–3 | 2 h |
| Wed | Module *n*: steps 4–6 | 1.5 h |
| Thu | Module *n*: step 7, then exercises ★★ | 1.5 h |
| Fri | Module *n+1*: steps 1–3 | 2 h |
| Sat | Module *n+1*: steps 4–7, plus one ★★★ exercise | 2.5 h |
| Sun | Review both modules; update your summary sheet | 1 h |

Ten hours a week covers Semester 1 comfortably. If you have less time, cut
★★★ exercises before you cut derivations.

## Using the interactive labs

Labs exist to build intuition that prose cannot. They are not illustrations to
click through.

1. Read the instructions and the mathematics on the page **before** touching a
   control.
2. Note the default state and predict what the figure will look like when you
   change a parameter.
3. Move one control at a time. Watch the readout, not only the picture.
4. Answer the "Try this" questions in writing.
5. Return to the module text and check whether your prediction was right.

Fourteen laboratories are available now, listed in the
[laboratory index](labs/index.md). Each is tied to a module and to a notebook, and
each can be explored before the module is read — that is the point of teaching these
ideas empirically first. The sequence runs from
[random events](labs/probability.md) and
[conditional probability](labs/conditional-probability.md) through the
[distributions](labs/discrete-distributions.md), the
[law of large numbers](labs/law-of-large-numbers.md), the
[CLT](labs/clt.md), [confidence intervals](labs/confidence-intervals.md) and
[p-values](labs/p-values.md), to [Bayes updating](labs/bayesian-updating.md),
[power](labs/power-and-errors.md) and [ANOVA](labs/anova.md).

## What to do when you are stuck

Work down this ladder; do not jump to the last rung.

1. **Reread the last paragraph slowly.** Most confusion is one unparsed sentence.
2. **Check the prerequisites.** The module states exactly which earlier sections it
   needs; a gap there is the usual cause.
3. **Name the symbol you do not recognise.** Look it up in
   [notation](reference/notation.md) (published with Module 03). Undefined symbols
   are the second most common cause.
4. **Specialise.** Put in numbers: *n* = 2, *p* = 0.5, a die instead of a
   distribution. Concrete cases expose what the general statement means.
5. **Simulate it.** Write twenty lines of code that generate the situation and look
   at the output. Simulation resolves most conceptual disputes with yourself.
6. **Write the question you would ask.** Formulating it precisely often answers it.
7. **Move on and return.** Some ideas (sampling distributions, p-values) genuinely
   need a night's sleep. Continue to the next section and come back.

## How to use the solutions

Solutions are complete on purpose — this course has no instructor to fill in the
gap. That makes them dangerous.

- Read the first line, then stop and try again.
- Never copy a solution into notes as if it were your own reasoning.
- After reading a solution, close it and reproduce it from memory. If you cannot,
  you have read it, not learned it.
- When your answer differs, decide *which step* differs. "I got a different
  number" is not a diagnosis; "I used *n* instead of *n* − 1" is.

## Reference and revision

Keep the [formula sheet](reference/formula-sheet.md) open while you read a chapter, and the
[glossary](reference/glossary.md) open while you write. Before a test, the
[revision pack](reference/revision/index.md) compresses each part to a page; the
[common mistakes](reference/revision/mistakes.md) page is the most useful single page in it.

## Tracking your progress

Each module page has a **Mark complete** control. It stores your progress in your
own browser (`localStorage`) — there is no account, no server and no tracking. The
consequence: progress does not follow you between devices or browsers, and
clearing site data erases it. Use the summary sheets you write in step 7 as your
durable record.

## What "finished" means

A module is finished when all of the following are true:

- [ ] You can state every learning objective in your own words.
- [ ] You can reproduce the central derivation on a blank page.
- [ ] You can explain the main formula's assumptions and one failure mode.
- [ ] You scored at least 8/10 on the quiz.
- [ ] You completed the ★ and ★★ exercises.
- [ ] You wrote the five-line summary.

Anything less is progress, not completion. That is fine — record where you stopped
and why. A course of eighteen modules is a long project, and honest bookkeeping beats
optimistic clicking.

## Study environment

- Use a notebook and pencil for derivations; typing algebra does not build the same
  recall.
- Keep one file per module of your own summaries — a "cheat sheet" you wrote is
  worth ten you downloaded.
- Run code in the project environment described in [setup](setup.md), so that your
  results are reproducible and match the text.
- Work in blocks of 45 minutes with a real break. Statistics rewards sustained
  attention and punishes fragmentation.
