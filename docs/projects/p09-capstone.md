# Capstone · Why are subscribers leaving?

**Level:** capstone · **Suggested time:** 5 weeks · **Modules:** all of M01–M18

[Starter notebook](notebooks/p09_capstone_churn.ipynb) ·
[Dataset](../data/projects/capstone_project.csv) ·
[Reference solution](solutions/p09-solution.md)

## Real-world background

A subscription business has 1,400 customers and a churn problem. The executive asks a single
question — *why are customers leaving, and what should we do?* — and expects an answer that
survives scrutiny. Nobody wants a list of twelve disconnected statistics; they want an
investigation that moves from description to probability to inference to a decision.

This capstone is that investigation. It is deliberately not a set of exercises: each section
depends on the previous one, and the final recommendation must be supported by the whole chain.

## Problem statement

Using one year of customer records, quantify the churn rate and its uncertainty, characterise
the behavioural process probabilistically, test whether acquisition channel is associated with
churn, model churn as a function of tenure, spend, support contacts and satisfaction, and
recommend a retention action with a plan to test it. The analysis must distinguish association
from causation and must state which conclusions would change under a different assumption.

## Learning objectives

1. Run an end-to-end investigation rather than a sequence of techniques.
2. Choose each method because the question requires it, and justify the choice.
3. Carry uncertainty through from a proportion to a regression coefficient.
4. Recognise confounding and mediation in an observational dataset.
5. Produce a decision-ready report with an explicit recommendation and a test design.
6. Defend the analysis in a viva: why this method, why this conclusion, what would change it.

## Dataset

`docs/data/projects/capstone_project.csv` — 1,400 customers, 10 columns, simulated.

## Dataset description

| Column | Type | Description |
|---|---|---|
| `customer_id` | identifier | Customer reference |
| `region` | categorical | North, South, East, West |
| `signup_channel` | categorical | organic, referral, paid, partner |
| `plan` | categorical | basic, plus, pro |
| `tenure_months` | integer | Months since signup, 1–60 |
| `monthly_spend` | numeric | Average monthly charge |
| `support_tickets` | integer | Tickets in the last 12 months |
| `app_sessions_month` | integer | App sessions per month |
| `satisfaction` | numeric | Survey score, 1–10 |
| `churned` | binary | 1 if the customer cancelled |

The simulation makes churn more likely with support tickets and paid acquisition, and less
likely with tenure, sessions and satisfaction. Spend is strongly determined by plan and tenure,
which makes its churn coefficient difficult to interpret causally — a deliberate trap.

## Research questions

The eight questions map onto the eight required statistical areas.

| # | Area | Question |
|---|---|---|
| 1 | Descriptive statistics | Who are the customers? Describe the base by plan, channel, tenure, spend and satisfaction |
| 2 | Probability | What is the probability a randomly chosen customer churns? What is the probability at least one of the next 20 churns? |
| 3 | Distributions | What distribution describes monthly sessions and support tickets? Is a Poisson model adequate? |
| 4 | Sampling | How variable is the churn rate across samples of 30? What does that imply for a pilot? |
| 5 | Confidence intervals | Give intervals for the churn rate, for channel differences and for the mean spend |
| 6 | Hypothesis testing | Does churn differ by channel? By plan? State hypotheses, assumptions and decisions |
| 7 | Correlation and regression | Which variables move together, and what does a logistic model add beyond pairwise correlation? |
| 8 | Interpretation | What should the business do, what would you test, and what can this dataset not tell you? |

## Statistical methods required

- Descriptive statistics by variable type, with appropriate figures.
- Probability rules, independence, and a binomial calculation.
- Distribution fitting and over-dispersion checks.
- Sampling distribution by simulation; standard error.
- Confidence intervals for proportions, differences and means.
- Chi-square tests, with effect sizes and intervals.
- Correlation matrix, logistic regression with odds ratios, linear regression for spend.
- Calibration and discrimination as a check on the churn model.

## Mathematical concepts

- Bernoulli and binomial models; \(\mathrm{Var}(\hat p)=p(1-p)/n\).
- Poisson mean–variance identity and over-dispersion.
- The sampling distribution of \(\hat p\) and the central limit theorem.
- Interval for a proportion; interval for a difference in proportions.
- Logistic model and odds ratios; \(R^2\) and residual standard error for the spend model.
- Confounding: a coefficient that changes when another variable is added.

## Step-by-step tasks

1. **Frame the decision.** Write the business question and the population in one sentence.
2. **Audit and describe.** Check the data, then build a descriptive profile by plan and channel.
3. **Quantify churn.** Estimate the rate with an interval; translate it into customers per 1,000.
4. **Model the process.** Compute the probability of at least one churn in the next 20 customers,
   and state the independence assumption.
5. **Choose distributions.** Fit and check a distribution for sessions and for tickets; test
   over-dispersion and explain the consequence.
6. **Demonstrate sampling.** Simulate 2,000 samples of size 30, plot the distribution of the
   churn rate, and compare its SD with \(\sqrt{\hat p(1-\hat p)/30}\).
7. **Test claims.** Test channel and plan differences; report rates, intervals, chi-square
   statistics, p-values and effect sizes.
8. **Correlate.** Build the correlation matrix and heatmap; identify the strongest associations
   and the pairs that are structurally related.
9. **Model.** Fit the logistic regression; report odds ratios with intervals, AUC and calibration.
10. **Second model.** Regress spend on tenure and plan; interpret and report \(R^2\).
11. **Synthesise.** Write the investigation: findings, uncertainty, confounding, recommendation.
12. **Design the test.** Propose the experiment that would establish whether the recommended
    action works: unit, assignment, metric, sample size, duration, guardrails.

## Python implementation requirements

- `pandas`, `numpy`, `matplotlib`, `scipy.stats`, `statsmodels`, `sklearn`.
- A fixed seed for every simulation; the seed reported in the notebook.
- No hard-coded numbers in the report: every figure and statistic printed by code.
- The notebook must run top to bottom in under five minutes.

## Expected visualizations

At least eight figures, including: churn by plan and channel with intervals; the distribution of
sessions with a fitted model; the simulated sampling distribution of the churn rate; a
correlation heatmap; the logistic model's calibration plot; and spend against tenure coloured by
plan.

## Interpretation requirements

- Each section answers its question and hands a result to the next section.
- Uncertainty is carried through: the churn rate has an interval, the channel difference has an
  interval, the odds ratios have intervals.
- The report distinguishes what is established (associations in this sample), what is plausible
  (mechanisms), and what is unknown (causal effects).
- The spend coefficient in the churn model is discussed as confounded by plan, not interpreted
  as "charging more causes churn".
- The recommendation includes a test design, because the analysis is observational.

## Deliverables

1. Executed capstone notebook.
2. An eight-page investigation report with the eight areas clearly addressed.
3. A two-page executive summary with three findings and one recommendation.
4. A one-page experiment design for the recommended action.
5. A ten-minute viva in which you defend two methodological choices and one limitation.

## Evaluation rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Framing and data handling | 10 | Question sharp; audit complete; decisions recorded |
| Descriptive and probabilistic work | 15 | Correct summaries; probability statements justified |
| Distributions and sampling | 15 | Model chosen and checked; simulation matches theory |
| Inference | 20 | Intervals and tests correct; assumptions checked; effect sizes reported |
| Modelling | 20 | Logistic and linear models interpreted; calibration checked; confounding discussed |
| Synthesis and recommendation | 15 | Findings cohere; recommendation follows; experiment designed |
| Reproducibility and communication | 5 | Clean run; report readable and honest |

## Extension challenges

1. **Survival view.** Treat tenure as a time-to-event outcome and estimate a Kaplan–Meier curve
   by plan. What does censoring mean here?
2. **Uplift framing.** Reframe the question from "who churns" to "who responds to an offer", and
   describe the data you would need.
3. **Cost model.** Assign a cost to a lost customer and a cost per retention offer, then compute
   the expected profit of targeting the top decile of predicted risk.
4. **Bayesian update.** With a Beta prior on the churn rate, compute the posterior after this
   sample and compare the credible interval with the confidence interval.
5. **Fairness.** Check whether the model's errors differ by region, and discuss whether the
   retention policy should use region at all.
