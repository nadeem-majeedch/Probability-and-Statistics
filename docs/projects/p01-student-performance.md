# P01 · University student performance

**Level:** foundation · **Suggested time:** 2 weeks · **Modules:** [M03](../modules/03-data-and-descriptive-statistics/chapter.md), [M14](../modules/14-estimation-and-confidence-intervals/chapter.md), [M16](../modules/16-correlation-and-regression/chapter.md), [M17](../modules/17-anova-chi-square-nonparametric/chapter.md)

[Starter notebook](notebooks/p01_student_performance.ipynb) ·
[Dataset](../data/projects/student_performance_project.csv) ·
[Reference solution](solutions/p01-solution.md)

## Real-world background

Every university produces end-of-semester marks and, alongside them, a record of attendance,
study habits, prior attainment and whether students work part-time. Administrators want to know
which of these are associated with performance, because the answer shapes tutoring budgets,
timetabling and the advice given to first-year students.

The temptation is to run a correlation matrix, pick the largest number, and declare it the
cause. The professional task is harder: separate the contributions of variables that move
together, attach uncertainty to each estimate, and say what the data cannot support.

## Problem statement

A Dean's office has one semester of records for 480 students across three degree programmes. It
wants an evidence-based answer to a single question — *which factors are associated with
examination performance, how large are those associations, and what should the faculty do about
them?* — without overstating what an observational dataset can show.

## Learning objectives

By the end of the project you can:

1. audit a survey-style dataset and justify each cleaning decision;
2. choose descriptive summaries that match each variable's scale and shape;
3. read a correlation matrix critically, including what it hides;
4. fit and interpret simple and multiple linear regression, with intervals;
5. compare groups with one-way ANOVA and interpret a non-significant result correctly;
6. explain confounding and why an adjusted coefficient can differ from a raw difference;
7. write a decision-oriented report for a non-specialist reader.

## Dataset

`docs/data/projects/student_performance_project.csv` — 480 rows, 9 columns, simulated with a
fixed seed. Load it directly from the notebook; do not edit the file.

## Dataset description

| Column | Type | Description | Notes |
|---|---|---|---|
| `student_id` | identifier | Anonymous student code | Unique, not an analysis variable |
| `programme` | categorical | BSDS, BSCS, BSSTAT | Three groups, unequal sizes |
| `semester` | integer | 1–8 | Current semester of study |
| `attendance_pct` | numeric | Percentage of classes attended | 40–100, left-skewed |
| `study_hours_week` | numeric | Self-reported study hours | Right-skewed, 2–30 |
| `prior_gpa` | numeric | GPA before this semester | 1.7–4.0 |
| `part_time_job` | binary | 1 if working part-time | About 34 % of students |
| `sleep_hours` | numeric | Average nightly sleep | 4–10 |
| `exam_score` | numeric | Final examination mark out of 100 | The outcome variable |

The data are simulated so that study hours have the strongest association with marks,
attendance and prior GPA have moderate ones, and the part-time job has a small negative
association once other factors are held constant. Sleep is included as a near-null variable:
part of the exercise is resisting the urge to interpret noise.

## Research questions

1. What is the distribution of examination marks, and what is a typical mark with a 95 %
   interval?
2. How strongly is each candidate factor associated with marks, on its own?
3. Which associations survive adjustment for the other factors, and how large are they?
4. Do the three programmes differ in mean marks? If not, what should be concluded?
5. Is the part-time job associated with lower marks after adjustment, and how can the raw
   difference and the adjusted coefficient disagree in significance?
6. What would you recommend to the Dean, and what evidence would strengthen the recommendation?

## Statistical methods required

- Descriptive statistics by variable type; skewness and outlier inspection.
- Pearson correlation with a sense of its limits; scatter plots.
- Simple and multiple linear regression; coefficient intervals; residual diagnostics.
- One-way ANOVA with a post-hoc check if significant.
- Two-sample comparison of the part-time groups, adjusted and unadjusted.
- Confidence intervals for means and mean differences.

## Mathematical concepts

- Sample mean and standard deviation; median and IQR for skewed variables.
- The least-squares slope \(\hat\beta_1 = r\,s_y/s_x\) and the intercept
  \(\hat\beta_0=\bar y-\hat\beta_1\bar x\).
- The regression model \(y_i=\beta_0+\beta_1x_{i1}+\cdots+\varepsilon_i\) with
  \(\varepsilon_i\sim N(0,\sigma^2)\), and \(R^2=1-\mathrm{SSE}/\mathrm{SST}\).
- ANOVA decomposition \(\mathrm{SST}=\mathrm{SSB}+\mathrm{SSW}\) and
  \(F=\frac{\mathrm{SSB}/(k-1)}{\mathrm{SSW}/(N-k)}\).
- Standard error of a mean, \(\sigma/\sqrt n\), and the \(t\)-based interval.

## Step-by-step tasks

1. **Audit.** Report types, missing values, duplicates and ranges. Flag anything implausible
   and say what you will do about it.
2. **Describe.** Summarise `exam_score` with mean, SD, median, IQR and a histogram. Summarise
   each driver appropriately; give frequencies for `programme` and `part_time_job`.
3. **Explore.** Produce a correlation matrix of the numeric variables and scatter plots of
   score against study hours, attendance and prior GPA. Comment on shape, not just strength.
4. **Simple model.** Regress `exam_score` on `study_hours_week`. Report the slope with a 95 %
   interval and interpret it in marks per hour.
5. **Multiple model.** Add `attendance_pct`, `prior_gpa` and `part_time_job`. Compare
   coefficients with the simple model and explain any change.
6. **Diagnose.** Plot residuals against fitted values and a QQ plot. State whether the
   assumptions are plausible and what you would do if not.
7. **Groups.** Test equality of mean marks across programmes. Report the \(F\) statistic, df,
   p-value and an effect size. If non-significant, explain what that does and does not mean.
8. **Uncertainty.** Report a 95 % interval for the mean mark and for the part-time difference.
9. **Reconcile.** Explain why the unadjusted part-time difference may be non-significant while
   its adjusted coefficient is significant. Check the correlation between the job indicator and
   the other predictors.
10. **Recommend.** Write the decision memo: what the evidence supports, what it does not, and
    one feasible intervention with a way to evaluate it.

## Python implementation requirements

- `pandas` for loading, auditing and grouping; `matplotlib` for figures.
- `scipy.stats` for correlation, ANOVA and \(t\) intervals.
- `statsmodels.formula.api.ols` for regression, using `.params`, `.bse`, `.conf_int()` and
  `.rsquared`.
- No manual editing of the CSV; no hard-coded numbers in the report that the notebook does not
  produce.
- The notebook must run top to bottom on a clean kernel.

## Expected visualizations

| Figure | What it must show |
|---|---|
| Histogram of `exam_score` | Shape, centre, spread; a marked mean and median |
| Box plot by programme | Overlap between programmes and any outliers |
| Scatter of study hours vs score | Form of the relationship, with a fitted line |
| Correlation heatmap | Which predictors move together |
| Residuals vs fitted | Constant spread and no curvature |
| Coefficient plot | Estimates with 95 % intervals, one row per predictor |

## Interpretation requirements

- Every coefficient is translated into the units of the problem.
- Every estimate is accompanied by an interval.
- The difference between "associated with" and "causes" is stated explicitly.
- The non-significant programme test is interpreted as "no evidence of a difference", not
  "the programmes are equal".
- One paragraph names the specific weaknesses: self-reported study hours, one semester, one
  institution, omitted variables such as motivation and teaching quality.

## Deliverables

1. Executed notebook (`p01_student_performance.ipynb`) with all outputs visible.
2. A report of at most six pages containing: question, data, methods, results with figures,
   interpretation, limitations, recommendation.
3. A one-page decision memo addressed to the Dean, in plain language.
4. A short reproducibility note: package versions and the command used to run the notebook.

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Audit and preparation | 10 | All issues found; decisions justified |
| Description | 15 | Correct summaries for each scale; figures readable |
| Method choice | 25 | Regression and ANOVA appropriate; assumptions checked; alternatives mentioned |
| Uncertainty | 15 | Intervals everywhere; p-values interpreted correctly |
| Interpretation | 20 | Answers the Dean's question; confounding discussed; limits named |
| Reproducibility | 10 | Clean run, no hard-coded results |
| Communication | 5 | Memo is clear, short and honest |

## Extension challenges

1. **Interactions.** Test whether the association between study hours and marks differs by
   programme. Interpret the interaction term, and plot predicted lines by group.
2. **Non-linearity.** Add a quadratic term for study hours. Does it improve fit enough to
   matter, and what does the shape imply about very high study hours?
3. **Robustness.** Refit with a robust regression or after removing the most influential points
   (Cook's distance). Do the conclusions change?
4. **Model comparison.** Compare models with adjusted \(R^2\) and AIC, and explain why the
   largest \(R^2\) is not automatically the best model.
5. **Sampling.** Take 200 bootstrap resamples of the coefficient for study hours and compare
   the bootstrap interval with the classical one. Why are they similar here?
