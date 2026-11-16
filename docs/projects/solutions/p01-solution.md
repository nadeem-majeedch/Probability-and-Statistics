# P01 · Reference solution — University student performance

[Project brief](../p01-student-performance.md) · [Dataset](../../data/projects/student_performance_project.csv) ·
[Starter notebook](../notebooks/p01_student_performance.ipynb)

!!! note "One defensible analysis, not the only one"
    The numbers below come from the supplied dataset. A different choice of transformations,
    outlier handling or model specification can produce slightly different values and still be
    correct. What matters is that the reasoning supports the numbers.

## How to approach it

The Dean's question is about association, not prediction, so the analysis should be organised
around **effect sizes with intervals**, not around a hunt for small p-values. The natural order
is: describe the outcome, look at each candidate driver alone, then adjust for the others,
because variables that move together can produce misleading simple associations.

The trap is `study_hours_week`. It correlates strongly with marks (about 0.70), which tempts a
causal reading: "make students study more". An observational dataset cannot support that, and the
report must say so.

## Results you should obtain

| Quantity | Value |
|---|---|
| n | 480 |
| Mean mark (95 % CI) | 57.13 (56.20, 58.07) |
| SD, median, IQR | 10.41, 56.50, 13.32 |
| Correlation with marks: study hours | 0.699 |
| Correlation with marks: prior GPA | 0.231 |
| Correlation with marks: attendance | 0.217 |
| Correlation with marks: sleep | 0.019 |
| Multiple regression \(R^2\) / adjusted | 0.590 / 0.586 |
| Residual SD | 6.69 |
| Coefficient: study hours | 1.656 (1.519, 1.794) |
| Coefficient: attendance (%) | 0.265 (0.199, 0.330) |
| Coefficient: prior GPA | 5.170 (3.703, 6.636) |
| Coefficient: part-time job | −2.037 (−3.297, −0.777) |
| Programme means | BSCS 58.20, BSDS 56.45, BSSTAT 56.75 |
| ANOVA | \(F=1.43\), df (2, 477), \(p=0.241\) |
| Raw part-time difference | 57.60 vs 56.26, \(t=1.35\), \(p=0.179\) |

## Worked key step: the multiple regression

The fitted model is

\[
\widehat{\text{score}} = 3.04 + 0.265\,\text{attendance} + 1.656\,\text{study}
+ 5.17\,\text{GPA} - 2.04\,\text{part-time}.
\]

Interpretation, coefficient by coefficient:

- **Study hours:** one extra hour per week is associated with 1.66 more marks (95 % CI 1.52 to
  1.79), holding the other variables fixed. This is the largest standardised effect.
- **Attendance:** ten percentage points more attendance is associated with about 2.65 more
  marks. The interval excludes zero but the effect is modest.
- **Prior GPA:** one GPA point is associated with about 5.2 more marks, a strong association
  with prior attainment.
- **Part-time job:** about 2 marks lower, adjusted. The interval excludes zero.

The model explains 59 % of the variance. That is high for social data, and it is high because
study hours and prior GPA are both strong and measured with little noise in the simulation.

## The interesting contradiction

The raw difference between part-time and other students is −1.34 marks and is **not**
significant (\(p=0.179\)); the adjusted coefficient is −2.04 and **is** significant. Students
with and without a job are almost identical on study hours (11.33 vs 11.02) and attendance
(78.4 vs 77.8), so this is not confounding in the usual sense.

What changed is the **residual variance**. The total SD of marks is 10.41, but the residual SD
after adjustment is 6.69. The same 2-mark difference is now measured against much less noise, so
its standard error shrinks and it becomes detectable. This is a general lesson: an adjusted
coefficient is not just "the effect after removing confounders"; it is also a more precise
estimate, because the covariates explain variance that would otherwise mask the effect.

## What the data do and do not show

**Supported:** study hours, prior GPA and attendance are positively associated with marks; the
association with study hours is the strongest; the three programmes do not differ detectably in
mean marks; sleep shows no association.

**Not supported:** that increasing study time would raise marks by 1.66 per hour. Students
choose their study hours, and the choice is entangled with motivation, ability and course load.
A randomised study-support programme would be needed to estimate a causal effect.

**Also worth saying:** the programme test is non-significant (\(p=0.241\)), which means no
evidence of a difference at this sample size, not proof of equality. The confidence intervals for
the programme means overlap substantially.

## Common mistakes

1. **Reporting \(r=0.70\) as "49 % of the variation" without saying what that means.** It means
   study hours alone explain about 49 % of the variance in marks; the multiple model raises this
   to 59 %.
2. **Dropping the part-time variable because the raw test was non-significant.** The adjusted
   coefficient is significant and the variable belongs in the model.
3. **Interpreting the intercept as a baseline student.** The intercept (3.04) is the predicted
   mark at zero attendance, zero study and zero GPA — far outside the data. It is meaningless on
   its own and its p-value should not be interpreted.
4. **Treating `programme` as ordered.** It is nominal; dummy coding is required.
5. **Omitting diagnostics.** The residual plots matter: a funnel shape would undermine the
   standard errors.

## Marking notes

A strong report (85+) does all of the following:

- states that the design is observational before presenting any coefficient;
- reports intervals alongside every estimate, including the programme means;
- notices and explains the raw-versus-adjusted part-time discrepancy rather than ignoring it;
- checks residual assumptions and reports what was found;
- recommends something feasible (a study-skills programme with random assignment) and explains
  how it would be evaluated.

A weak report runs the regression, quotes \(p<0.05\), and concludes that attendance causes
higher marks.
