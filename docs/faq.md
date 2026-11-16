---
title: Frequently asked questions
description: Prerequisites, programming, calculus, datasets, solutions and how the course is assessed.
---

# Frequently asked questions

## Before you start

**Do I need to know calculus?**
You need to be comfortable with the *idea* of a derivative and an integral.
Module 01 supplies the working technique — differentiation, integration, series —
at exactly the depth later modules use, and every calculus step afterwards is shown
explicitly. If your calculus is rusty, Module 01 is the fix, not a barrier.

**Do I need to be good at programming?**
No. Code appears as a way to *test* mathematics, and every line is explained.
Beginners should type the examples rather than paste them. If you already program,
read the examples and go straight to the exercises.

**What mathematics is genuinely assumed?**
Algebra: rearranging equations, fractions, exponents, logarithms, factorials.
Everything else is built in Module 01.

**Can I start in the middle?**
Yes, if you meet the prerequisites. [Where to start](index.md#where-to-start)
gives three entry paths. Do not skip Module 15 if you plan to study inference —
sampling distributions are the hinge the whole subject turns on.

## About the course

**Is this course enough for machine learning?**
It gives you the statistical foundation that machine learning assumes:
distributions, expectation, estimation, inference, regression and simulation. It
does not teach ML algorithms — that is a separate course — but Module 29 draws the
connections explicitly.

**Why are there so many derivations?**
Because a formula you cannot derive is a formula you cannot trust, debug or adapt.
Derivations are the difference between using statistics and understanding it.

**Why do you teach the Central Limit Theorem before stating it?**
Because the statement is easy to memorise and easy to misapply. Seeing the
histogram of the sample mean converge — and seeing it fail for a heavy-tailed
population — makes the conditions mean something. Try
[the lab](labs/clt.md).

**How long does the course take?**
About 270 hours in total, or roughly 10 hours per week for two 16-week semesters. A
one-semester core track of about 150 hours is described in the [syllabus](syllabus.md#schedule).

**Is there a certificate?**
No. This is an open self-study resource; there is no enrolment, no fee and no
credential.

## Study mechanics

**How do I know whether I understand a module?**
By being able to do things, not by feeling familiar. The
[what "finished" means](how-to-study.md#what-finished-means) checklist is the test:
state the objectives, reproduce the derivation, explain an assumption, score 8/10,
complete the ★ and ★★ exercises.

**Should I read solutions when I am stuck?**
Read the *first line* of the solution, then try again. Complete solutions are
provided because there is no instructor, but reading them instead of attempting
the problem is the main way students waste this course.

**Do I need to do every exercise?**
Do all ★, most ★★, and at least one ★★★ per part. The ★★★ exercises are where the
material becomes yours.

**The interactive labs are optional, right?**
They are part of the course, not decoration. Each lab exists because a specific
idea is easier to *see* than to read — coverage of confidence intervals, for
example. Skipping them costs you the intuition the later algebra assumes.

**Does my progress sync between devices?**
No. Progress is stored in your browser only — no account, no server, no tracking.
Clearing site data erases it. Keep your own written summaries as the durable record.

## Data and software

**Do I need paid software?**
No. Everything is free and open source: Python, Jupyter, NumPy, pandas, SciPy,
Matplotlib, Seaborn, statsmodels, scikit-learn. No licences, accounts or API keys
anywhere.

**Are the datasets real?**
Yes. Small, curated, openly licensed datasets are used so results are reproducible
offline. Every dataset page records its source, licence and shape. Synthetic data,
where used for teaching a specific point, is labelled as synthetic.

**Can I use my own data?**
Yes, for the projects — provided you may use it, you can document where it came
from, and it contains no personal or identifiable information.

**Why Python and not R?**
Python is the language of the surrounding data-science curriculum, and it keeps the
course to one language so that effort goes into statistics rather than syntax.
Nothing in the course depends on Python-specific behaviour; the mathematics
transfers.

## Assessment and integrity

**How is the course graded?**
By you, against complete solutions and the criteria in the
[assessment section](syllabus.md#assessment). The weighting mirrors a taught
programme so your self-marking is comparable.

**Can I use this material in my own course?**
Yes, under [CC BY-NC-SA 4.0](about/licence.md): attribution required, no commercial
use, share-alike. The code is MIT.

**How do I report an error?**
Through the repository's issue tracker. Please state the module, the section and
what you believe is wrong — errata are corrected in the open and never silently.

**I found a typo in a formula. Is it worth reporting?**
Yes. In a mathematics course a typo in a formula is a correctness bug, not a
cosmetic one.

## Reference and revision

**Where are all the formulas?**
In the [formula sheets](reference/formula-sheet.md), one page for foundations and one for
inference and modelling. Each formula gives its symbols, assumptions, when to use it and an
example.

**Is there a glossary?**
Yes — [over 160 terms](reference/glossary.md), alphabetical, each linked to the module that
teaches it.

**How do I revise efficiently?**
Start with the [quick sheets](reference/revision/quick-sheets.md), then the
[conceptual questions](reference/revision/questions.md), then the
[exam guide](reference/revision/exam-guide.md).
