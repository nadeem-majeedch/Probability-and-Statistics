---
title: Examination preparation guide
description: How the paper is built, what each topic is worth, a four-week plan, answering technique and the traps that cost the most marks.
---

# Examination preparation guide

Marks are lost in three places: not knowing the method, applying it to the wrong problem, and
reporting the answer without interpretation. This guide addresses all three.

## What the paper tests

The course assesses four things, roughly in this proportion:

| Capability | Share | What it looks like |
|---|---|---|
| Method selection and computation | 40 % | "Carry out the appropriate test" — the choice is part of the mark |
| Interpretation | 30 % | "State what this means in context" — numbers alone earn little |
| Concepts and reasoning | 20 % | "Explain why", "what would change if" |
| Assumptions and limitations | 10 % | "State the assumptions", "comment on validity" |

A paper that is 80 % computation rewards practice; this one rewards practice *and* explanation.

## Topic weights

| Area | Modules | Typical weight | Priority |
|---|---|---|---|
| Descriptive statistics and visualisation | M03–M04 | 10 % | medium |
| Probability and counting | M05–M07 | 15 % | high |
| Random variables, expectation, distributions | M08–M11 | 20 % | high |
| Sampling distributions and the CLT | M12–M13 | 15 % | **highest** |
| Confidence intervals and hypothesis tests | M14–M15 | 25 % | **highest** |
| Correlation and regression | M16 | 10 % | medium |
| ANOVA, chi-square, nonparametric | M17 | 10 % | medium |
| Bayesian and computational methods | M18 | 5 % | low |

If you have one evening, spend it on M12–M15. If you have a week, work outward from there.

## The four-week plan

**Week 1 — rebuild the foundations.** Modules 03–11. Reconstruct every formula on the
[foundation formula sheet](../formula-sheet.md) from memory, then check. Do two worked examples per
distribution by hand. Keep an error log from day one.

**Week 2 — sampling and inference.** Modules 12–15. This is where most marks live. Simulate: draw
1,000 samples of size 5, 30 and 200 and look at the three histograms of the mean. Compute a
confidence interval by hand, then a p-value, then check that the interval and the test agree.

**Week 3 — modelling and comparisons.** Modules 16–18. Run one regression and interpret every
coefficient in a sentence. Run one ANOVA and one chi-square test. Do one bootstrap and compare its
standard error with the formula.

**Week 4 — examination conditions.** Past papers under time, no notes. Then mark yourself against
the rubric, not against the answer. Re-read the error log the night before; do not learn anything
new.

## What to memorise, and what to look up

**Memorise:** definitions of mean, variance, covariance, correlation; the probability rules; Bayes'
theorem; expectation and variance rules; the binomial, Poisson, normal and exponential formulas with
means and variances; standard error formulas; the structure of a confidence interval; the structure
of a test statistic; SST = SSR + SSE; the chi-square statistic.

**Look up (and be told you may):** t, z, chi-square and F tables; specific critical values; long
derivations you have seen once.

**Derive rather than memorise:** the variance shortcut, the pooled variance, the \(t\)-statistic for a
correlation, the least-squares slope. If you can derive them you cannot forget them.

## Answering technique

1. **State the model before computing.** "Let X be the number of successes; X ~ Binomial(n, p)."
   This earns method marks even when the arithmetic slips.
2. **Write the formula, then substitute.** An examiner can award partial credit for a correct formula
   with wrong numbers; not for a bare wrong number.
3. **Keep units and context in the final sentence.** "2.3 percentage points" not "2.3".
4. **Report intervals, not just point estimates.** If the question asks for an estimate, the interval
   is usually worth an extra mark.
5. **Answer the question asked.** "Is there evidence?" wants a conclusion about evidence, not a
   verdict about truth.
6. **State assumptions explicitly.** Two marks often sit there.
7. **If time is short, write the method and the interpretation.** Both are markable; a half-finished
   calculation is not.

## Traps that cost the most marks

| Trap | What to do instead |
|---|---|
| Using a two-sample test on paired data | check the design first |
| Reading p = 0.03 as "3 % chance the null is true" | p is P(data \| null) |
| Saying "proves" or "no effect" | "provides evidence", "insufficient evidence" |
| Forgetting to check expected counts ≥ 5 for chi-square | compute them and say so |
| Using \(z\) when \(\sigma\) is estimated | use \(t\) |
| Reporting R² as "the model is 90 % accurate" | R² is variance explained in-sample |
| Dropping the "per unit" in a slope | always give the units |
| Assuming a normal population because n > 30 | the CLT helps the *mean*, not the data |
| Ignoring a multi-part question's second half | "comment on" is a mark, not decoration |
| Leaving the answer without a sentence of interpretation | the last sentence is often a whole mark |

## A 90-second checklist before submitting

- Did I answer every part of every question?
- Does every number have units or a context?
- Is every p-value accompanied by an effect size or interval?
- Did I state assumptions and check the ones that matter?
- Is any conclusion stronger than the evidence?
- Are the significant figures sensible — two or three, not seven?

## The night before

Read the error log, the [common mistakes](mistakes.md) page, and the [quick sheets](quick-sheets.md).
Sleep. Cramming new material at that point displaces the material you already know, and the paper
rewards clear thinking more than recall.
