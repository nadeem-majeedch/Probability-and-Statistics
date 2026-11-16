# P05 · Weather data: probability and distribution analysis

**Level:** intermediate · **Suggested time:** 3 weeks · **Modules:** [M10](../modules/10-continuous-distributions/chapter.md), [M11](../modules/11-joint-distributions/chapter.md), [M13](../modules/13-law-of-large-numbers-and-clt/chapter.md), [M14](../modules/14-estimation-and-confidence-intervals/chapter.md)

[Starter notebook](notebooks/p05_weather_distributions.ipynb) ·
[Dataset](../data/projects/weather_project.csv) ·
[Reference solution](solutions/p05-solution.md)

## Real-world background

Weather records are the classic applied probability dataset: a strong seasonal cycle, a
variable that is zero on most days and heavy-tailed when it rains, and a design question that
depends on the tail rather than the average. A drainage engineer does not care about mean
rainfall; they care about the probability of exceeding a capacity.

Choosing a distribution is therefore not a technicality. A normal model for daily rainfall
implies a meaningful chance of negative rain and badly understates extremes; a gamma model
respects the lower bound and the skew, and gives different design values.

## Problem statement

Using three years of daily records from three stations, describe the temperature and rainfall
processes, fit and check distributions, quantify seasonal structure, and produce probability
statements that a drainage design can use. The analysis must distinguish the distribution of all
days from the distribution of wet days.

## Learning objectives

1. Separate a mixture (zero and positive rainfall) before fitting a distribution.
2. Fit and evaluate continuous distributions with QQ plots and information criteria.
3. Model seasonality explicitly and explain why it distorts pooled summaries.
4. Test station differences while respecting dependence in time.
5. Compute exceedance probabilities and return periods, and interpret them correctly.
6. Explain the difference between a percentile of all days and a design event.

## Dataset

`docs/data/projects/weather_project.csv` — 3,288 daily station records (1,096 days × 3
stations), 7 columns, simulated.

## Dataset description

| Column | Type | Description |
|---|---|---|
| `date` | date | Calendar date, 2023-01-01 to 2025-12-31 |
| `station` | categorical | Lahore, Murree, Karachi |
| `temp_max_c` | numeric | Daily maximum temperature |
| `temp_min_c` | numeric | Daily minimum temperature |
| `rainfall_mm` | numeric | Daily rainfall; zero on dry days |
| `humidity_pct` | numeric | Relative humidity |
| `wind_kmh` | numeric | Mean wind speed |

The simulation gives each station its own temperature offset, a shared seasonal cycle, a
rain-day probability that varies seasonally, gamma-distributed wet-day amounts, and humidity
that follows the season with noise.

## Research questions

1. What are the distributions of maximum temperature and daily rainfall, and how do they differ
   by station?
2. What proportion of days are wet, and what is the distribution of rainfall on wet days?
3. How strong is the seasonal cycle, and what happens to a pooled histogram when you ignore it?
4. Do the stations differ in mean temperature? What assumption does the test violate?
5. What is the 90th and 99th percentile of daily rainfall, and the probability of exceeding
   30 mm in a day?
6. How many exceedance days per year should a drainage design expect, and how uncertain is that
   number?

## Statistical methods required

- Descriptive statistics by station and month; skewness.
- Histograms, density estimates and QQ plots.
- Gamma and lognormal fits to wet-day rainfall; comparison by AIC or log-likelihood.
- Two-part (hurdle) model: probability of rain × amount given rain.
- One-way ANOVA across stations, with a caveat about temporal dependence.
- Confidence intervals for proportions and means; bootstrap for quantiles.

## Mathematical concepts

- Gamma density \(f(x)=\frac{1}{\Gamma(k)\theta^k}x^{k-1}e^{-x/\theta}\), mean \(k\theta\),
  variance \(k\theta^2\).
- Lognormal median \(e^\mu\), mean \(e^{\mu+\sigma^2/2}\).
- Exceedance probability \(P(X>x)=1-F(x)\) and return period \(1/P(X>x)\).
- Law of total probability for the hurdle model:
  \(P(X>x)=P(\text{wet})P(X>x\mid\text{wet})\).
- Standard error of a proportion and of a quantile (bootstrap).

## Step-by-step tasks

1. **Prepare.** Parse dates, add month and season, check for gaps and impossible values.
2. **Temperature.** Describe by station and month; plot the annual cycle; check normality of the
   residuals after removing the seasonal mean.
3. **Rainfall mixture.** Report the wet-day probability by month and the distribution of wet-day
   amounts. Explain why a single distribution for all days is wrong.
4. **Fit.** Fit gamma and lognormal models to wet-day rainfall; compare with AIC and QQ plots,
   and report the fitted parameters.
5. **Design values.** Compute the 90th and 99th percentiles of all days and of wet days, then the
   probability of exceeding 30 mm and the expected exceedances per year.
6. **Stations.** Test mean temperature differences and comment on the independence assumption
   given the shared seasonal cycle.
7. **Uncertainty.** Bootstrap the 99th percentile and compare with the plug-in estimate.
8. **Interpret.** Write the design memo: the capacity, the exceedance probability, the
   assumptions, and what would change the answer.

## Python implementation requirements

- `pandas` for dates and grouping; `matplotlib` for the seasonal plots.
- `scipy.stats.gamma.fit` and `lognorm.fit` with `floc=0`.
- `scipy.stats.f_oneway` for the station comparison.
- A bootstrap loop with a fixed seed; report the seed.
- All quantiles computed from the data, not from a normal approximation.

## Expected visualizations

| Figure | What it must show |
|---|---|
| Monthly mean temperature by station | Seasonal cycle and station offsets |
| Histogram of rainfall (all days) | The spike at zero — the mixture |
| Histogram and QQ plot of wet-day rainfall | Skew and the quality of the gamma fit |
| Exceedance curve (log scale) | Tail behaviour and design values |
| Bootstrap distribution of the 99th percentile | Uncertainty in an extreme quantile |

## Interpretation requirements

- The zero-inflation is described explicitly; "mean daily rainfall" is never presented as a
  typical wet day.
- Exceedance probabilities are stated with the time window they refer to.
- The return period is explained as an average waiting time, not a schedule.
- The station comparison acknowledges temporal dependence.
- One limitation paragraph: three stations, three years, simulated data, and a stationary
  climate assumption that real design studies must question.

## Deliverables

1. Executed notebook.
2. A four-page report with distribution fits, design values and the drainage recommendation.
3. A table of exceedance probabilities for 10, 20, 30 and 50 mm by station.
4. A short note on which distribution you chose and why.

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Data preparation | 10 | Dates parsed, seasonality defined, gaps checked |
| Mixture handling | 20 | Wet-day probability separated from amount; hurdle logic explained |
| Distribution fitting | 25 | Appropriate families, parameters reported, fit assessed |
| Exceedance and design values | 20 | Correct probabilities, return periods and intervals |
| Station comparison | 15 | Test correct, dependence caveat stated |
| Interpretation | 10 | Statements usable by an engineer and honestly qualified |

## Extension challenges

1. **Extreme value theory.** Fit a generalised Pareto distribution to exceedances over a high
   threshold and compare the 100-day return level with the empirical estimate.
2. **Temporal dependence.** Compute the autocorrelation of daily rainfall and test whether wet
   days cluster. How does clustering change the variance of the annual total?
3. **Climate shift.** Split the record in half and test whether the seasonal amplitude changed.
4. **Joint distribution.** Model temperature and humidity jointly and estimate the probability
   of a hot, humid day.
5. **Missing data.** Delete 10 % of rainfall values at random and compare three imputation
   strategies for the monthly mean.
