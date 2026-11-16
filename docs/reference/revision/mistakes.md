---
title: Common statistical mistakes
description: The errors that cost the most marks and the most credibility, with the correction for each.
---

# Common statistical mistakes

Grouped by where they happen. Each entry gives the mistake, why it is tempting, and the fix. If
your work is being marked down and you cannot see why, one of these is usually responsible.

## Describing data

**1. Reporting the mean of skewed data as "typical".**
Income, waiting times and house prices have means far above the typical case. **Fix:** report the
median alongside, and say which question each answers.

**2. Quoting a mean without a spread.**
"Average 57" hides whether everyone scored 57 or half scored 20 and half 94. **Fix:** mean with SD,
or median with IQR.

**3. Deleting outliers without saying so.**
An outlier is information: a data-entry error, a different population, or a real extreme.
**Fix:** investigate, report the analysis with and without, and state the rule you used.

**4. Treating ordinal data as interval.**
A Likert 1–5 has no guarantee that 2→3 equals 4→5. **Fix:** medians and rank tests, or justify the
interval assumption explicitly.

**5. Confusing SD with SE.**
SD describes individuals; SE describes an estimate. **Fix:** SD in descriptive tables, SE (or a CI)
whenever you quote an estimate.

**6. Reading a histogram's height as a probability.**
Height is density or count; area is probability. **Fix:** say which, and use density when bins
differ in width.

**7. Comparing percentages without denominators.**
"Twice as many complaints" from 2 versus 1 is noise. **Fix:** report counts and rates.

## Probability

**8. The prosecutor's fallacy.**
P(evidence | innocent) is not P(innocent | evidence). **Fix:** Bayes, with a real prior.

**9. Assuming independence because it is convenient.**
Observations in a class, a clinic or a week are usually clustered. **Fix:** check the design;
standard errors change dramatically.

**10. Adding probabilities of overlapping events.**
P(A) + P(B) double-counts the overlap. **Fix:** inclusion–exclusion.

**11. Confusing "at least one" with "exactly one".**
They differ by orders of magnitude at large n. **Fix:** use the complement for "at least one".

**12. Ignoring the base rate.**
A 99 % accurate test for a 0.1 % condition yields mostly false positives. **Fix:** compute PPV at the
relevant prevalence.

## Inference

**13. Reading a p-value as P(H₀ true).**
It is P(data this extreme | H₀), not the reverse. **Fix:** phrase it correctly, every time.

**14. "Not significant" → "no effect".**
Absence of evidence is not evidence of absence; the interval may still include important effects.
**Fix:** report the interval and discuss power.

**15. "Significant" → "important".**
With n = 100,000 a 0.1-point difference is significant. **Fix:** report the effect size.

**16. Peeking and stopping when p < 0.05.**
Repeated looks inflate the false-positive rate far beyond 5 %. **Fix:** pre-specify n, or use a
sequential design.

**17. Testing many subgroups and reporting the winner.**
With 20 comparisons, one "significant" result at α = 0.05 is expected. **Fix:** pre-specify, or
correct (Bonferroni, Holm, FDR), and label exploratory findings as exploratory.

**18. One-tailed tests chosen after seeing the data.**
Halves the p-value by doubling the claim. **Fix:** fix direction beforehand, or stay two-sided.

**19. Ignoring pairing.**
Before/after measurements analysed as two independent groups lose precision and can reverse the
conclusion. **Fix:** paired test on the differences.

**20. Using a two-sample test on paired data — or the reverse.**
The design decides, not the software default.

**21. Checking assumptions after choosing the test, then switching to whatever "works".**
That is a decision informed by the data. **Fix:** state the check, the decision rule, and report the
sensitivity analysis.

**22. Treating a CI as a probability statement about the parameter.**
Frequentist intervals are about the procedure. **Fix:** "95 % of such intervals capture μ"; or use a
credible interval and say so.

**23. Believing a huge test statistic because n is huge.**
The standard error shrinks as 1/√n; almost any difference becomes detectable. **Fix:** effect size
and interval width, not p alone.

**24. Reporting p = 0.000.**
Impossible; a p-value is a probability. **Fix:** p < 0.001.

## Regression and modelling

**25. Interpreting a slope as causal.**
Regression describes association unless the design licenses more.

**26. Predicting outside the data range.**
The linear form is untested there. **Fix:** flag extrapolation.

**27. Ignoring R² while praising significance.**
A significant slope with R² = 0.03 explains almost nothing.

**28. Comparing R² across models with different outcomes.**
Log-transformed and raw outcomes are not comparable. **Fix:** compare on the original scale, or use
information criteria within the same response.

**29. Dropping predictors to raise R².**
Adjusted R² and AIC exist for this; raw R² always rises when you add terms.

**30. Confusing a prediction interval with a confidence interval.**
The prediction interval for one new case is much wider. **Fix:** state which you computed.

**31. Interpreting a logistic coefficient as a probability change.**
Coefficients are log-odds; exp(β) is an odds ratio. **Fix:** convert, and evaluate at realistic
baselines.

## Design and data handling

**32. Confusing correlation with causation.**
The classic, and still the most common in reports.

**33. Survivorship bias.**
Only successful firms, surviving patients or delivered orders appear in the data.

**34. Immortal time bias.**
Classifying people by something that happens later ("ever took the drug") guarantees a spurious
benefit.

**35. Multiple testing across the whole project.**
Every extra analysis is another chance to be wrong.

**36. Overfitting with too many predictors.**
Rules of thumb exist for a reason; cross-validate.

**37. Treating missing data as random.**
Missingness often depends on the value itself. **Fix:** report the missingness, and compare complete
cases with an imputed analysis.

## Presentation

**38. Charts with truncated axes.**
A bar chart starting at 90 exaggerates tiny differences. **Fix:** start bars at zero, or use a line
or dot plot for a non-zero baseline.

**39. Reporting 7 significant figures.**
Precision is not accuracy. **Fix:** two significant figures for estimates, matching the interval.

**40. No statement of limitations.**
Every analysis has them; omitting them suggests you did not look.
