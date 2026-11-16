---
title: Glossary
description: Over 160 probability and statistics terms, defined in plain language, each linked to the module that teaches it.
---

# Glossary

Plain-language definitions, alphabetical, with the module that develops each idea. Symbols follow
the [notation page](notation.md); every formula is on the [formula sheet](formula-sheet.md).

If a definition here and a chapter disagree, the chapter is right — report the glossary.

## A

**Accuracy.** The proportion of all predictions that are correct; misleading when classes are
imbalanced. [M01](../modules/01-introduction-to-statistics.md)

**AIC (Akaike information criterion).** A model-fit score that penalises extra parameters, used to
compare models fitted to the same data; lower is better. [M18](../modules/18-bayesian-and-data-science-methods.md)

**Alternative hypothesis.** The claim a test is designed to detect, usually "there is an effect".
[M15](../modules/15-hypothesis-testing.md)

**ANOVA (analysis of variance).** A test comparing three or more means by splitting total variation
into between-group and within-group parts. [M17](../modules/17-anova-chi-square-nonparametric.md)

**Arithmetic mean.** The sum divided by the count; the balance point of the data.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Assumption.** A condition a method relies on for its guarantees to hold, such as independence or
normality; violations change what the output means. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Autocorrelation.** Correlation between a series and its own past values, which shrinks the
effective sample size and invalidates ordinary standard errors.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Axioms of probability.** The three rules — non-negativity, total mass one, countable additivity —
from which every probability result follows. [M06](../modules/06-probability-fundamentals.md)

## B

**Bar chart.** A plot of counts or summaries by category; bars need not start at zero when they
show a mean, but must when they show a count. [M04](../modules/04-data-visualization.md)

**Bayes factor.** The ratio of how likely the data are under two hypotheses; evidence as a
multiplier on prior odds. [M18](../modules/18-bayesian-and-data-science-methods.md)

**Bayes' theorem.** The rule that turns a prior belief and a likelihood into a posterior
probability. [M07](../modules/07-conditional-probability-and-bayes.md)

**Bernoulli distribution.** One binary trial with success probability p; the building block of the
binomial. [M09](../modules/09-discrete-distributions.md)

**Beta distribution.** A distribution on the interval from 0 to 1, the natural prior for a
probability. [M10](../modules/10-continuous-distributions.md)

**Bias.** A systematic departure of an estimator's average from the true value; distinct from
variance and not fixed by increasing n. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Bimodal.** Having two distinct peaks, usually a sign that two populations are mixed.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Binary variable.** A variable with exactly two categories, coded 0 and 1.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Binomial coefficient.** The number of ways to choose r items from n ignoring order, written
n choose r. [M05](../modules/05-counting-and-combinatorics.md)

**Binomial distribution.** The count of successes in n independent trials with the same success
probability. [M09](../modules/09-discrete-distributions.md)

**Block design.** An experiment grouped into homogeneous blocks so that nuisance variation can be
removed. [M17](../modules/17-anova-chi-square-nonparametric.md)

**Bootstrap.** Resampling with replacement from the observed data to estimate the sampling
distribution of a statistic. [M18](../modules/18-bayesian-and-data-science-methods.md)

**Box plot.** A display of median, quartiles, whiskers and flagged outliers.
[M04](../modules/04-data-visualization.md)

## C

**Categorical variable.** A variable whose values are labels rather than numbers on a scale.
[M03](../modules/03-data-and-descriptive-statistics.md)

**CDF (cumulative distribution function).** F(x) = P(X ≤ x), giving the probability of being at or
below x. [M08](../modules/08-random-variables-and-expectation.md)

**Central limit theorem (CLT).** For large n, the sample mean is approximately normal whatever the
population shape, provided the variance is finite. [M13](../modules/13-law-of-large-numbers-and-clt.md)

**Chi-square distribution.** The distribution of a sum of squared standard normals; the reference
for variance and categorical tests. [M17](../modules/17-anova-chi-square-nonparametric.md)

**Chi-square test.** A test comparing observed counts with expected counts, for goodness of fit or
independence in a table. [M17](../modules/17-anova-chi-square-nonparametric.md)

**Cluster sampling.** Sampling whole groups rather than individuals; efficient but with larger
standard errors than simple random sampling. [M12](../modules/12-sampling-and-sampling-distributions.md)

**Coefficient of determination (R²).** The proportion of variation in the outcome explained by the
model. [M16](../modules/16-correlation-and-regression.md)

**Coefficient of variation (CV).** Standard deviation divided by the mean; a unitless measure of
relative spread. [M03](../modules/03-data-and-descriptive-statistics.md)

**Cohort study.** A study following a defined group forward in time, comparing outcomes by
exposure. [M01](../modules/01-introduction-to-statistics.md)

**Collinearity.** Strong correlation among predictors, which inflates standard errors and makes
individual coefficients unstable. [M16](../modules/16-correlation-and-regression.md)

**Combination.** A selection where order does not matter. [M05](../modules/05-counting-and-combinatorics.md)

**Complement.** The event that A does not happen, with probability 1 − P(A).
[M06](../modules/06-probability-fundamentals.md)

**Conditional probability.** P(A | B), the probability of A given that B occurred.
[M07](../modules/07-conditional-probability-and-bayes.md)

**Confidence interval.** A range produced by a procedure that captures the true parameter in 95 % of
repeated samples; the interval either contains it or not. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Confidence level.** The long-run capture rate of the interval procedure, usually 95 %.
[M14](../modules/14-estimation-and-confidence-intervals.md)

**Confounding.** A third variable associated with both exposure and outcome, which distorts the
observed relationship. [M16](../modules/16-correlation-and-regression.md)

**Contingency table.** A cross-tabulation of counts by two categorical variables.
[M17](../modules/17-anova-chi-square-nonparametric.md)

**Continuous variable.** A variable that can take any value in an interval, at least in principle.
[M10](../modules/10-continuous-distributions.md)

**Control group.** The comparison group that does not receive the treatment.
[M01](../modules/01-introduction-to-statistics.md)

**Correlation.** The strength and direction of linear association between two variables, between
−1 and 1. [M16](../modules/16-correlation-and-regression.md)

**Covariance.** The average product of deviations from the means; its sign gives the direction of
association, and its size depends on units. [M11](../modules/11-joint-distributions.md)

**Coverage probability.** The proportion of repeated intervals that contain the true parameter; the
property the confidence level describes. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Cramér's V.** An effect size for association in a contingency table, between 0 and 1.
[M17](../modules/17-anova-chi-square-nonparametric.md)

**Credible interval.** A Bayesian interval with the interpretation people wrongly give confidence
intervals: 95 % posterior probability the parameter lies inside. [M18](../modules/18-bayesian-and-data-science-methods.md)

**Critical value.** The boundary of the rejection region for a test statistic, set by the
significance level. [M15](../modules/15-hypothesis-testing.md)

**Cross-validation.** Estimating out-of-sample performance by fitting on part of the data and
testing on the rest. [M18](../modules/18-bayesian-and-data-science-methods.md)

## D

**Data.** Recorded observations, ideally with their context, collection method and limitations.
[M01](../modules/01-introduction-to-statistics.md)

**Degrees of freedom.** The number of independent pieces of information left after estimating
parameters; it sets the shape of t, chi-square and F distributions.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Density.** The function whose area over an interval gives probability for a continuous variable;
it is not itself a probability and may exceed 1. [M10](../modules/10-continuous-distributions.md)

**Dependent variable.** The outcome being explained or predicted; also called the response.
[M16](../modules/16-correlation-and-regression.md)

**Descriptive statistics.** Summaries of the observed data with no claim beyond them.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Deviation.** The difference between an observation and a summary such as the mean.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Discrete variable.** A variable taking separated values, usually counts.
[M09](../modules/09-discrete-distributions.md)

**Dispersion.** How spread out the values are; measured by range, SD, IQR and similar.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Distribution.** The complete pattern of probabilities over the possible values of a variable.
[M08](../modules/08-random-variables-and-expectation.md)

**Dummy variable.** A 0/1 indicator used to put a categorical predictor into a regression.
[M16](../modules/16-correlation-and-regression.md)

## E

**Effect size.** A standardised measure of how large an effect is, independent of sample size.
[M15](../modules/15-hypothesis-testing.md)

**Empirical rule.** For normal data, about 68 %, 95 % and 99.7 % of values lie within 1, 2 and 3
standard deviations of the mean. [M10](../modules/10-continuous-distributions.md)

**Estimator.** The rule used to guess a parameter from data; a random variable because the sample
is random. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Estimate.** The number an estimator produced on one sample.
[M14](../modules/14-estimation-and-confidence-intervals.md)

**Event.** A subset of the sample space to which a probability is assigned.
[M06](../modules/06-probability-fundamentals.md)

**Expectation.** The probability-weighted average of a random variable; the long-run mean.
[M08](../modules/08-random-variables-and-expectation.md)

**Experiment.** A procedure with a set of possible outcomes; in design, a study where the
researcher assigns the treatment. [M01](../modules/01-introduction-to-statistics.md)

**Exponential distribution.** The waiting time between events in a memoryless Poisson process.
[M10](../modules/10-continuous-distributions.md)

**Explanatory variable.** A variable used to explain or predict the outcome; also called the
predictor. [M16](../modules/16-correlation-and-regression.md)

**Extrapolation.** Predicting outside the range of observed predictor values, where the fitted
relationship is untested. [M16](../modules/16-correlation-and-regression.md)

## F

**F distribution.** The distribution of a ratio of two scaled chi-square variables; the reference
for ANOVA and variance comparisons. [M17](../modules/17-anova-chi-square-nonparametric.md)

**Factor.** A categorical explanatory variable in an experiment or ANOVA.
[M17](../modules/17-anova-chi-square-nonparametric.md)

**Factorial.** n! = n(n−1)···1, the number of orderings of n distinct items; 0! = 1.
[M05](../modules/05-counting-and-combinatorics.md)

**False negative.** A missed true effect: failing to detect what is there; related to Type II
error. [M15](../modules/15-hypothesis-testing.md)

**False positive.** A detected effect that is not real; related to Type I error.
[M15](../modules/15-hypothesis-testing.md)

**Finite population correction.** The factor √((N−n)/(N−1)) applied to a standard error when
sampling a substantial fraction of a finite population.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Fitted value.** The prediction a model makes for an observed case.
[M16](../modules/16-correlation-and-regression.md)

**Frequency.** The count of observations in a category or bin.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Frequentist.** The interpretation of probability as a long-run relative frequency, and of
inference as the behaviour of procedures over repeated samples.
[M14](../modules/14-estimation-and-confidence-intervals.md)

## G

**Gamma distribution.** A flexible right-skewed distribution for positive quantities; includes the
exponential and chi-square as special cases. [M10](../modules/10-continuous-distributions.md)

**Gaussian distribution.** Another name for the normal distribution.
[M10](../modules/10-continuous-distributions.md)

**Geometric distribution.** The number of trials until the first success.
[M09](../modules/09-discrete-distributions.md)

**Geometric mean.** The n-th root of the product of n positive values; the right average for
growth rates. [M03](../modules/03-data-and-descriptive-statistics.md)

**Goodness of fit.** How well a model or distribution matches the observed data; also the name of
the chi-square test for a claimed distribution. [M17](../modules/17-anova-chi-square-nonparametric.md)

## H

**Harmonic mean.** n divided by the sum of reciprocals; the right average for rates.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Histogram.** A bar plot of counts or densities over bins of a quantitative variable.
[M04](../modules/04-data-visualization.md)

**Hypergeometric distribution.** The count of successes when sampling without replacement from a
finite population. [M09](../modules/09-discrete-distributions.md)

**Hypothesis test.** A procedure that measures compatibility between data and a null hypothesis,
with a stated error rate. [M15](../modules/15-hypothesis-testing.md)

## I

**Independence (events).** A and B are independent when P(A ∩ B) = P(A)P(B).
[M06](../modules/06-probability-fundamentals.md)

**Independence (observations).** Observations carry no information about each other; violated by
clustering, pairing and time series. [M12](../modules/12-sampling-and-sampling-distributions.md)

**Independent variable.** A predictor in a model; also, in design, the variable the researcher
manipulates. [M16](../modules/16-correlation-and-regression.md)

**Indicator variable.** A 0/1 variable marking membership of a category.
[M16](../modules/16-correlation-and-regression.md)

**Inference.** Drawing conclusions about a population or a parameter from a sample, with
quantified uncertainty. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Interquartile range (IQR).** Q3 − Q1, the span of the middle half of the data.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Interval estimate.** A range of plausible values for a parameter, such as a confidence interval.
[M14](../modules/14-estimation-and-confidence-intervals.md)

## J

**Jackknife.** Estimating uncertainty by leaving out one observation at a time; a precursor to the
bootstrap. [M18](../modules/18-bayesian-and-data-science-methods.md)

**Joint distribution.** The distribution of two or more variables considered together.
[M11](../modules/11-joint-distributions.md)

## K

**Kruskal–Wallis test.** A nonparametric test comparing three or more independent groups by
ranks. [M17](../modules/17-anova-chi-square-nonparametric.md)

**Kurtosis.** A measure of tail weight; 3 for a normal, higher for heavy tails.
[M08](../modules/08-random-variables-and-expectation.md)

## L

**Law of large numbers (LLN).** The sample mean converges to the population mean as n grows, for
finite-mean populations. [M13](../modules/13-law-of-large-numbers-and-clt.md)

**Least squares.** Choosing parameters to minimise the sum of squared residuals; the fitting rule
behind ordinary regression. [M16](../modules/16-correlation-and-regression.md)

**Level of significance.** The Type I error rate a test is allowed, usually 0.05.
[M15](../modules/15-hypothesis-testing.md)

**Likelihood.** The probability or density of the observed data viewed as a function of the
parameter. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Linear regression.** Modelling the mean of an outcome as a linear function of predictors.
[M16](../modules/16-correlation-and-regression.md)

**Logistic regression.** Modelling the log-odds of a binary outcome as a linear function of
predictors; coefficients exponentiate to odds ratios.
[M16](../modules/16-correlation-and-regression.md)

**Lognormal distribution.** The distribution of a variable whose logarithm is normal; right-skewed
and common for incomes and sizes. [M10](../modules/10-continuous-distributions.md)

## M

**Mann–Whitney U test.** A nonparametric test comparing two independent groups by ranks; also
called the Wilcoxon rank-sum test. [M17](../modules/17-anova-chi-square-nonparametric.md)

**Margin of error.** Half the width of a confidence interval; the “±” in a poll.
[M14](../modules/14-estimation-and-confidence-intervals.md)

**Marginal distribution.** The distribution of one variable after summing or integrating out the
others. [M11](../modules/11-joint-distributions.md)

**Matched pairs.** A design in which each observation in one group is tied to a specific
observation in the other. [M15](../modules/15-hypothesis-testing.md)

**Mean absolute deviation.** The average absolute distance from the mean; a robust-ish spread
measure in original units. [M03](../modules/03-data-and-descriptive-statistics.md)

**Median.** The middle value of sorted data; the 50th percentile, resistant to outliers.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Moment generating function (MGF).** E[exp(tX)], which generates moments and identifies
distributions. [M08](../modules/08-random-variables-and-expectation.md)

**Monte Carlo method.** Solving a problem by repeated random simulation.
[M18](../modules/18-bayesian-and-data-science-methods.md)

**Mode.** The most frequent value, or the peak of a density.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Multiple regression.** Regression with more than one predictor; coefficients are partial effects.
[M16](../modules/16-correlation-and-regression.md)

**Mutually exclusive.** Events that cannot occur together, so P(A ∩ B) = 0.
[M06](../modules/06-probability-fundamentals.md)

## N

**Negative binomial distribution.** The number of trials until r successes, or a count model that
allows variance to exceed the mean. [M09](../modules/09-discrete-distributions.md)

**Negative predictive value (NPV).** Among those who test negative, the proportion who do not have
the condition. [M07](../modules/07-conditional-probability-and-bayes.md)

**Nominal data.** Categories with no order, such as blood group or country.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Nonparametric test.** A test whose validity does not depend on a distributional family, usually
working with ranks. [M17](../modules/17-anova-chi-square-nonparametric.md)

**Normal distribution.** The symmetric bell-shaped distribution defined by mean and variance; the
limit of the CLT. [M10](../modules/10-continuous-distributions.md)

**Null hypothesis.** The default claim a test tries to disprove, usually "no effect" or "no
difference". [M15](../modules/15-hypothesis-testing.md)

## O

**Observational study.** A study where the researcher observes rather than assigns exposure, so
causal claims need extra care. [M01](../modules/01-introduction-to-statistics.md)

**Odds.** p / (1 − p), the ratio of the probability of an event to its complement.
[M06](../modules/06-probability-fundamentals.md)

**Odds ratio.** The ratio of odds in two groups; the natural effect measure in logistic regression.
[M16](../modules/16-correlation-and-regression.md)

**One-tailed test.** A test that rejects only in one direction, at the cost of missing effects in
the other. [M15](../modules/15-hypothesis-testing.md)

**Ordinal data.** Ordered categories where the gaps are not equal, such as Likert responses.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Outlier.** An observation far from the rest; worth investigating, not automatically deleting.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Overdispersion.** Variance greater than the mean in count data, which breaks Poisson standard
errors. [M09](../modules/09-discrete-distributions.md)

## P

**p-value.** The probability of data at least as extreme as observed, assuming the null hypothesis
is true; not the probability that the null is true.
[M15](../modules/15-hypothesis-testing.md)

**Parameter.** A numerical characteristic of a population, usually unknown and denoted by a Greek
letter. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Pearson correlation.** The standard correlation coefficient for linear association.
[M16](../modules/16-correlation-and-regression.md)

**Percentile.** The value below which a given percentage of observations fall.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Permutation.** An arrangement where order matters; also, in testing, a relabelling of the data.
[M05](../modules/05-counting-and-combinatorics.md)

**Permutation test.** A test that builds the null distribution by randomly relabelling outcomes.
[M18](../modules/18-bayesian-and-data-science-methods.md)

**Placebo.** A treatment with no active ingredient, used to separate the effect of expectation.
[M01](../modules/01-introduction-to-statistics.md)

**PMF (probability mass function).** P(X = x) for a discrete random variable.
[M08](../modules/08-random-variables-and-expectation.md)

**Point estimate.** A single number used to estimate a parameter.
[M14](../modules/14-estimation-and-confidence-intervals.md)

**Poisson distribution.** The count of rare events in a fixed exposure, with variance equal to the
mean. [M09](../modules/09-discrete-distributions.md)

**Population.** The complete set about which inferences are wanted.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Positive predictive value (PPV).** Among those who test positive, the proportion who truly have
the condition. [M07](../modules/07-conditional-probability-and-bayes.md)

**Posterior distribution.** The distribution of a parameter after seeing data, proportional to
prior times likelihood. [M18](../modules/18-bayesian-and-data-science-methods.md)

**Power.** The probability of detecting an effect that is really there; 1 − Type II error rate.
[M15](../modules/15-hypothesis-testing.md)

**Prediction interval.** A range for a single future observation, wider than a confidence interval
for the mean. [M16](../modules/16-correlation-and-regression.md)

**Prevalence.** The proportion of a population that has a condition at a point in time.
[M07](../modules/07-conditional-probability-and-bayes.md)

**Prior distribution.** Belief about a parameter before seeing the data.
[M18](../modules/18-bayesian-and-data-science-methods.md)

**Probability.** A number between 0 and 1 measuring how likely an event is, obeying the axioms.
[M06](../modules/06-probability-fundamentals.md)

**Probability distribution.** A rule assigning probabilities to all possible values of a random
variable. [M08](../modules/08-random-variables-and-expectation.md)

## Q

**Q–Q plot.** A plot comparing sample quantiles with theoretical quantiles to check distributional
fit. [M04](../modules/04-data-visualization.md)

**Qualitative data.** Non-numeric data, such as categories or text.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Quantile.** A generalised percentile: the value below which a given fraction of the distribution
lies. [M03](../modules/03-data-and-descriptive-statistics.md)

**Quantitative data.** Numeric data on which arithmetic makes sense.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Quartile.** The 25th, 50th or 75th percentile, splitting data into four parts.
[M03](../modules/03-data-and-descriptive-statistics.md)

## R

**Random sample.** A sample drawn by a mechanism giving every unit a known chance of selection.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Random variable.** A numerical outcome of a random procedure; capital letters by convention.
[M08](../modules/08-random-variables-and-expectation.md)

**Randomisation.** Assigning treatments by chance, which is what licenses causal interpretation.
[M15](../modules/15-hypothesis-testing.md)

**Range.** Maximum minus minimum; sensitive to a single outlier.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Regression to the mean.** Extreme values tend to be followed by less extreme ones when the
measurement is noisy. [M16](../modules/16-correlation-and-regression.md)

**Rejection region.** The set of test-statistic values that lead to rejecting the null hypothesis.
[M15](../modules/15-hypothesis-testing.md)

**Relative risk.** The ratio of risks in two groups; comparable to an odds ratio when the outcome
is rare. [M07](../modules/07-conditional-probability-and-bayes.md)

**Residual.** Observed minus fitted value; the raw material of model diagnostics.
[M16](../modules/16-correlation-and-regression.md)

**Robust.** Insensitive to outliers or mild assumption violations.
[M03](../modules/03-data-and-descriptive-statistics.md)

**ROC curve.** A plot of sensitivity against 1 − specificity across thresholds; its area summarises
discrimination. [M07](../modules/07-conditional-probability-and-bayes.md)

## S

**Sample.** The subset of a population that was actually observed.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Sample space.** The set of all possible outcomes of a random procedure.
[M06](../modules/06-probability-fundamentals.md)

**Sampling distribution.** The distribution of a statistic over repeated samples of the same size.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Sampling error.** The difference between a statistic and the population value, arising from which
units happened to be selected. [M12](../modules/12-sampling-and-sampling-distributions.md)

**Scatter plot.** A plot of one variable against another, the first check for relationships.
[M04](../modules/04-data-visualization.md)

**Sign test.** A test of paired differences based only on how many are positive.
[M17](../modules/17-anova-chi-square-nonparametric.md)

**Significance level.** The Type I error rate chosen before the test, conventionally 0.05.
[M15](../modules/15-hypothesis-testing.md)

**Simple random sampling.** Every unit and every combination has an equal chance of selection.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Skewness.** Asymmetry of a distribution; positive means a long right tail.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Slope.** The change in the fitted outcome per one-unit change in the predictor.
[M16](../modules/16-correlation-and-regression.md)

**Spearman correlation.** Correlation of ranks, measuring monotone association.
[M16](../modules/16-correlation-and-regression.md)

**Standard deviation.** The square root of variance, in the units of the data.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Standard error.** The standard deviation of an estimator's sampling distribution.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Standard normal distribution.** N(0, 1), the reference distribution for z-scores.
[M10](../modules/10-continuous-distributions.md)

**Statistic.** A number computed from a sample, such as the mean or a test statistic.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Stratified sampling.** Sampling separately within homogeneous groups, which reduces variance.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Sum of squares.** A sum of squared deviations; the currency of ANOVA and regression.
[M17](../modules/17-anova-chi-square-nonparametric.md)

## T

**t distribution.** A symmetric distribution with heavier tails than normal, used when the standard
deviation is estimated. [M14](../modules/14-estimation-and-confidence-intervals.md)

**t-test.** A test for one or two means using the t distribution.
[M15](../modules/15-hypothesis-testing.md)

**Test statistic.** A summary of the data whose distribution under the null hypothesis is known.
[M15](../modules/15-hypothesis-testing.md)

**Time series.** Data ordered in time, where consecutive observations are usually dependent.
[M12](../modules/12-sampling-and-sampling-distributions.md)

**Total probability (law of).** P(B) = Σ P(B | Aᵢ)P(Aᵢ) over a partition of the sample space.
[M07](../modules/07-conditional-probability-and-bayes.md)

**Treatment.** The condition assigned in an experiment.
[M01](../modules/01-introduction-to-statistics.md)

**Trimmed mean.** The mean after discarding a fixed fraction of the smallest and largest values.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Two-tailed test.** A test that rejects for departures in either direction.
[M15](../modules/15-hypothesis-testing.md)

**Type I error.** Rejecting a true null hypothesis; its rate is the significance level.
[M15](../modules/15-hypothesis-testing.md)

**Type II error.** Failing to reject a false null hypothesis; its complement is power.
[M15](../modules/15-hypothesis-testing.md)

## U

**Unbiased estimator.** An estimator whose average over repeated samples equals the parameter.
[M14](../modules/14-estimation-and-confidence-intervals.md)

**Uncertainty.** The quantified incompleteness of a conclusion, expressed as an interval, a
standard error or a posterior. [M14](../modules/14-estimation-and-confidence-intervals.md)

**Uniform distribution.** Constant density over an interval; the basis of random number generation.
[M10](../modules/10-continuous-distributions.md)

**Unit of analysis.** The entity each observation describes, not necessarily each row.
[M12](../modules/12-sampling-and-sampling-distributions.md)

## V

**Variable.** A characteristic that varies across units and takes values in a defined set.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Variance.** The average squared deviation from the mean; the core measure of spread.
[M08](../modules/08-random-variables-and-expectation.md)

**Variance inflation factor (VIF).** How much a coefficient's variance is inflated by collinearity;
above about 5 signals trouble. [M16](../modules/16-correlation-and-regression.md)

**Variation.** The total variability in a set of observations, decomposed by ANOVA into parts.
[M17](../modules/17-anova-chi-square-nonparametric.md)

**Venn diagram.** A set diagram for events, useful for unions, intersections and complements.
[M06](../modules/06-probability-fundamentals.md)

## W

**Weighted mean.** An average in which observations carry different weights.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Wilcoxon signed-rank test.** A nonparametric test for paired differences using signed ranks.
[M17](../modules/17-anova-chi-square-nonparametric.md)

**Winsorising.** Replacing extreme values with a percentile rather than deleting them.
[M03](../modules/03-data-and-descriptive-statistics.md)

**Within-group variation.** Variability inside groups; the denominator of the F ratio in ANOVA.
[M17](../modules/17-anova-chi-square-nonparametric.md)

## Z

**z-score.** (x − mean)/SD; a value's distance from the mean in standard deviations.
[M03](../modules/03-data-and-descriptive-statistics.md)

**z-test.** A test using the standard normal distribution, valid when the population SD is known
or n is large. [M15](../modules/15-hypothesis-testing.md)

**Zero-inflated model.** A model mixing a point mass at zero with a count distribution, for data
with more zeros than the count model allows. [M09](../modules/09-discrete-distributions.md)
