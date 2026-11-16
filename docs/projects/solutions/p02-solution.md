# P02 · Reference solution — Diagnostic accuracy and Bayes

[Project brief](../p02-diagnostics-bayes.md) · [Dataset](../../data/projects/diagnostics_project.csv) ·
[Starter notebook](../notebooks/p02_diagnostics_bayes.ipynb)

## How to approach it

Build the 2×2 table first, by hand, before writing any code. Every quantity in this project is a
ratio of four numbers, and the errors come from confusing which ratio is which. Then do the
Bayesian calculation twice — once from the table and once from the formula — because they must
agree, and the agreement is the check.

The intellectual core is that a test can be *good* and a positive result can still be *weak
evidence*, because prevalence controls how many healthy people are available to generate false
positives.

## Results you should obtain

| Quantity | Value |
|---|---|
| n | 1,600 |
| Prevalence (95 % CI) | 16.9 % (15.0 %, 18.7 %) |
| True positives / false negatives | 223 / 47 |
| False positives / true negatives | 99 / 1,231 |
| Sensitivity | 0.826 |
| Specificity | 0.926 |
| PPV | 0.693 |
| NPV | 0.963 |
| LR+ / LR− | 11.1 / 0.188 |
| AUC (biomarker) | 0.951 |
| Mean biomarker, diseased vs healthy | 73.08 vs 56.16 |

## Worked key step: Bayes by hand

At the observed prevalence \(\pi=0.169\), with \(se=0.826\) and \(sp=0.926\),

\[
\mathrm{PPV}=\frac{se\cdot\pi}{se\cdot\pi+(1-sp)(1-\pi)}
=\frac{0.826\times0.169}{0.826\times0.169+0.074\times0.831}
=\frac{0.1396}{0.1396+0.0615}=0.694,
\]

which matches the table (223/322 = 0.693; the small difference is rounding).

Now change only the prevalence:

| Prevalence | PPV | What it means |
|---|---|---|
| 1 % | 10.1 % | Nine in ten positives are false |
| 5 % | 37.0 % | Most positives still false |
| 16.9 % (observed) | 69.3 % | Two in three positives are true |
| 30 % | 82.7 % | Four in five positives are true |

The arithmetic is the same; only the prior changed. This is the entire content of "base-rate
neglect": sensitivity describes the test, PPV describes the test *in a population*.

## Threshold and cost analysis

The laboratory threshold of 66 is not obviously optimal. Evaluating alternatives:

| Threshold | Sensitivity | Specificity | PPV | Missed per 1,000 | False alarms per 1,000 |
|---|---|---|---|---|---|
| 60 | 0.956 | 0.713 | 0.403 | 7.5 | 238.8 |
| 64 | 0.900 | 0.877 | 0.597 | 16.9 | 102.5 |
| 66 (lab) | 0.826 | 0.926 | 0.693 | 29.4 | 61.9 |
| 72 | 0.537 | 0.982 | 0.858 | 78.1 | 15.0 |

With a missed case costing five times a false alarm, the expected cost per 1,000 patients at
prevalence 16.9 % is

the expected cost per 1,000 patients is 5 × missed cases + false alarms,

giving 276 at threshold 60, **187 at 64**, 209 at the laboratory's 66, and 406 at 72. The
optimum sits just below the laboratory threshold: lowering it much further trades a handful of
extra detections for a flood of false positives, because specificity falls steeply while
sensitivity is already high. The exact optimum depends on the cost ratio, which is why the
report must state it.

## Discrimination beyond the table

The AUC of 0.951 says the biomarker ranks a random diseased patient above a random healthy one
95 % of the time. It is impressive and it is **not** the same as the PPV: a test can rank
perfectly and still have a modest PPV at low prevalence. The ROC curve also shows that the
laboratory's threshold sits on a steep part of the curve, where a small shift buys a large
change in sensitivity.

## Who should be tested

The logistic model gives

\[
\operatorname{logit}P(D)=\hat\beta_0+0.0252\,\text{age}+0.2555\,\text{severity},
\]

so each additional severity point multiplies the odds of disease by \(e^{0.2555}=1.29\), and
each additional year of age by \(1.026\). A 20-year-old with severity 1 has a very low
probability; a 70-year-old with severity 6 has a high one. Testing everyone regardless of prior
probability wastes the test's specificity on the healthiest patients.

## Patient communication

> "Your test came back positive. In people like you — with your age and symptoms — about one in
> three who test positive actually have the condition. The test is good at picking up the
> disease when it is there, but because the disease is uncommon, many positive results come from
> people who are healthy. The next step is a confirmatory test, which will settle it."

The number must match the patient's own prior probability, not the headline PPV. That is why the
age- and severity-specific estimate matters.

## Common mistakes

1. **Reporting "94 % accurate".** Accuracy depends on prevalence; at 1 % prevalence, a test with
   these characteristics would be right about 92 % of the time while most positives are false.
2. **Interpreting PPV without a prevalence.** The same test has PPV 0.10 and 0.83 at different
   prevalences.
3. **Using a 0.5 threshold by default.** The threshold should follow from the relative costs.
4. **Reading the AUC as a probability of correct classification.** It is a ranking probability
   between a random positive and a random negative.
5. **Ignoring the reference standard.** If the "confirmed diagnosis" is itself imperfect, both
   sensitivity and specificity are biased.

## Marking notes

A strong report computes the table correctly, presents PPV as a function of prevalence, justifies
a threshold with explicit costs, and writes a patient paragraph that a non-statistician could
understand without being misled. A weak report equates sensitivity with the probability of
disease given a positive test.
