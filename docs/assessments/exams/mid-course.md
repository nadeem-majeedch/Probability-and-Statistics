# Mid-course revision assessment

**Covers:** Modules 01–09. **Time:** 75 minutes. **Total:** 100 marks.
**Instructions:** closed book; a calculator is allowed. Answer all multiple-choice questions,
then the written questions. Do not look at the answer key until you have finished.

| Section | Items | Marks | Suggested time |
|---|---|---|---|
| A. Multiple choice | 20 | 40 | 30 min |
| B. Short answers | 3 | 15 | 12 min |
| C. Numerical | 6 | 33 | 25 min |
| D. Scenario | 2 | 12 | 8 min |

## Section A — Multiple choice (2 marks each)

```quiz
Q1. Which quantity is a statistic rather than a parameter?
A) The mean height of all students at a university
B) The mean height of 40 students selected at random
C) The proportion of defective items in a whole production run
D) The standard deviation of a complete census
* B
Why: A statistic is computed from a sample; the others describe whole populations. The word "selected" is the clue.

Q2. A postcode such as "54000" is measured on which scale?
A) Ordinal
B) Interval
C) Ratio
D) Nominal
* D
Why: Postcodes are labels with no order or arithmetic meaning; sorting them numerically would be meaningless.

Q3. Which summary of spread is expressed in the same units as the data?
A) Variance
B) Standard deviation
C) Coefficient of variation
D) \(R^2\)
* B
Why: The square root of the variance restores the original units; the CV is unit-free and variance is in squared units.

Q4. A dataset of 15 observations has its 8th smallest value equal to 22. Which statement must be true?
A) The mode is 22
B) The 75th percentile is 22
C) The mean is 22
D) The median is 22
* D
Why: With \(n=15\) the median is the 8th ordered value. Nothing follows about the mean, mode or other percentiles.

Q5. If \(P(A)=0.5\), \(P(B)=0.4\) and \(P(A\cap B)=0.1\), then \(P(A\cup B)\) is
A) 0.7
B) 0.2
C) 0.9
D) 0.8
* D
Why: \(0.5+0.4-0.1=0.8\). Forgetting to subtract the intersection gives 0.9.

Q6. How many distinct arrangements does the word LEVEL have?
A) 20
B) 120
C) 60
D) 30
* D
Why: Five letters with L twice and E twice give \(5!/(2!2!)=120/4=30\).

Q7. In a class, 60 % study mathematics and 30 % study both mathematics and physics. The
A) 0.50
B) 0.90
C) 0.18
D) 0.30
* A
Why: \(0.30/0.60=0.5\). Multiplying instead of conditioning on mathematics gives the wrong 0.18.

Q8. Events \(A\) and \(B\) have \(P(A)=0.2\), \(P(B)=0.6\), \(P(A\cap B)=0.12\). They are
A) independent
B) mutually exclusive
C) complementary
D) negatively associated
* A
Why: \(P(A)P(B)=0.12=P(A\cap B)\). They can occur together, so they are not mutually exclusive.

Q9. A test is 95 % sensitive and 90 % specific, and prevalence is 2 %. The PPV is closest to
A) 5 %
B) 95 %
C) 50 %
D) 16 %
* D
Why: Per 1,000: 19 true positives and 98 false positives, giving 19/117 ≈ 16 %. Sensitivity alone does not determine PPV.

Q10. For Bernoulli trials with \(p=0.25\), the variance of the count of successes in one trial is
A) 1
B) 0.25
C) 0.1875
D) 0.0625
* C
Why: \(p(1-p)=0.25\times0.75=0.1875\). The value 0.0625 is \(p^2\).

Q11. For independent variables with variances 5 and 7, the variance of their sum is
A) 2
B) 74
C) 12
D) 35
* C
Why: Variances add for independent variables, giving 12. Multiplying gives the variance only in special cases.

Q12. A binomial model is inappropriate when
A) the number of trials is fixed
B) the probability of success changes between trials
C) trials are independent
D) there are two outcomes
* B
Why: Constant \(p\) is required; changing success probability signals dependence or a mixture, so another model is needed.

Q13. Events occur at 6 per hour. The expected count in 10 minutes is
A) 60
B) 6
C) 1
D) 0.6
* C
Why: The mean scales with exposure: \(6\times(10/60)=1\).

Q14. A geometric variable with \(p=0.25\) has mean
A) 4
B) 3
C) 0.75
D) 0.25
* A
Why: The expected number of trials to the first success is \(1/p=4\).

Q15. A normal variable has mean 70 and SD 5. The z-score of 77.5 is
A) 7.5
B) 1.0
C) 1.5
D) 2.5
* C
Why: \((77.5-70)/5=1.5\). Dividing by 5 rather than the variance is essential.

Q16. An exponential distribution has rate 0.25 per minute. Its mean is
A) 16 minutes
B) 0.25 minutes
C) 4 minutes
D) 2 minutes
* C
Why: Mean \(=1/\lambda=4\) minutes. The rate is not the mean.

Q17. Surveying only shoppers in one mall to estimate city-wide spending creates
A) coverage bias
B) measurement error
C) a Type I error
D) sampling error only
* A
Why: The sampling frame omits most of the population, producing systematic bias that no sample size removes.

Q18. Assigning treatments at random protects chiefly against
A) confounding by unmeasured variables
B) measurement error
C) non-response
D) random sampling error
* A
Why: Randomisation balances confounders in expectation, supporting causal inference; it does not affect measurement or coverage.

Q19. The probability of at least one failure in 4 independent trials with failure probability 0.1
A) 0.4
B) 0.3439
C) 0.6561
D) 0.0001
* B
Why: \(1-0.9^4=1-0.6561=0.3439\). The value 0.6561 is the probability of no failures.

Q20. If \(\ln X\sim N(2,0.09)\), the median of \(X\) is
A) 2
B) \(e^2\)
C) \(e^{2.045}\)
D) 0.09
* B
Why: The median transforms to \(e^\mu=e^2\). The mean would be \(e^{\mu+\sigma^2/2}\), slightly larger.
```

## Section B — Short answers (5 marks each)

**S1.** Explain why a census can still produce a biased estimate.

<details><summary>Model answer</summary>
A census removes sampling error but not coverage error (people who are missed), non-response,
measurement error or processing errors. If the missed group differs systematically — for example,
people in temporary housing — the census total is biased even though everyone listed was measured.
</details>

**S2.** State the conditions for a Poisson model and give one reason they may fail for website
visits.

<details><summary>Model answer</summary>
Events occur independently at a constant rate, with the count proportional to exposure. Website
visits cluster around campaigns and times of day, so the rate is not constant and arrivals are
not independent; the variance then exceeds the mean, requiring a negative binomial or
time-varying model.
</details>

**S3.** Distinguish \(E[X^2]\) from \((E[X])^2\), and explain which one enters the variance.

<details><summary>Model answer</summary>
\(E[X^2]\) is the average of the squared values; \((E[X])^2\) squares the average. The variance
is their difference, \(E[X^2]-(E[X])^2\), so \(E[X^2]\) enters positively. Using the squared mean
in its place understates the variance.
</details>

## Section C — Numerical problems (5–6 marks each)

**N1.** A sample of 12 waiting times (minutes) is 3, 4, 4, 5, 6, 7, 8, 9, 10, 12, 15, 30. Compute
the mean, median, and identify the effect of the largest value.

<details><summary>Worked solution</summary>
Sum \(=113\), mean \(=113/12=9.42\). With \(n=12\) the median is \((7+8)/2=7.5\). Removing
30 gives mean \(83/11=7.55\): the single value raises the mean by about 1.9 minutes while the
median would move only slightly — evidence of right skew.
</details>

**N2.** In a population of 5,000, a stratified sample of 400 is drawn from strata of sizes 2,500,
1,500 and 1,000. Give the stratum sample sizes.

<details><summary>Worked solution</summary>
Sampling fraction \(400/5{,}000=0.08\). Allocations: \(2{,}500(0.08)=200\);
\(1{,}500(0.08)=120\); \(1{,}000(0.08)=80\). Total 400.
</details>

**N3.** A committee of 4 is chosen from 9 people. How many committees contain a particular person?

<details><summary>Worked solution</summary>
Fix that person, then choose 3 from the remaining 8: \(\binom{8}{3}=56\). Equivalently,
committees containing the person are \(\binom{9}{4}-\binom{8}{4}=126-70=56\).
</details>

**N4.** Two machines produce 70 % and 30 % of output with defect rates 1 % and 4 %. A defective
item is found. Find the probability it came from the second machine.

<details><summary>Worked solution</summary>
Defect probability \(=0.7(0.01)+0.3(0.04)=0.007+0.012=0.019\). Posterior
\(=0.012/0.019=0.632\). The smaller machine produces most defects because its rate is four
times higher.
</details>

**N5.** \(X\sim\mathrm{Binomial}(12,0.4)\). Compute \(P(X=5)\) and the mean.

<details><summary>Worked solution</summary>
\(\binom{12}{5}=792\); \(0.4^5=0.01024\); \(0.6^7=0.02799\); product
\(792\times0.01024\times0.02799=0.227\). Mean \(=12(0.4)=4.8\).
</details>

**N6.** A normal variable has mean 200 and SD 25. Find the probability of a value above 240, and
the 10th percentile.

<details><summary>Worked solution</summary>
\(z=(240-200)/25=1.6\), \(P=1-0.9452=0.0548\). The 10th percentile is
\(200-1.2816(25)=200-32.04=167.96\).
</details>

## Section D — Scenario (6 marks each)

**P1.** A university wants to estimate the proportion of students who use the gym weekly. It can
survey 500 students. Compare a social-media poll with a random sample of enrolled students, and
state the main threat to each.

<details><summary>Outline answer</summary>
The social-media poll is a convenience sample: only followers see it, and the keenest respond, so
selection and non-response bias contaminate the estimate and no valid margin of error exists. The
random sample has a known design and a quantifiable standard error
(\(\sqrt{p(1-p)/500}\approx0.022\) at \(p=0.5\)), but non-response must be managed with reminders
and reported; if respondents differ from non-respondents, bias remains.
</details>

**P2.** A retailer finds that customers enrolled in its loyalty scheme spend 40 % more. List two
alternative explanations and describe a design that would test the causal claim.

<details><summary>Outline answer</summary>
Selection: heavy spenders choose to enrol. Confounding: enrolled customers also receive
promotions or shop in richer areas. A randomised encouragement trial — invite a random half to
enrol and compare spending by assigned group (intent-to-treat) — separates the scheme's effect
from self-selection, provided enrolment uptake is measured.
</details>

## Answer key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|
| 1 | B | 6 | C | 11 | A | 16 | B |
| 2 | D | 7 | C | 12 | B | 17 | B |
| 3 | B | 8 | A | 13 | B | 18 | B |
| 4 | D | 9 | C | 14 | B | 19 | B |
| 5 | D | 10 | B | 15 | B | 20 | B |

**Marking guide:** 40 marks for Section A, 15 for B, 33 for C, 12 for D. A total of 70+ indicates
secure foundations; below 50, revisit Modules 03, 05 and 07 before continuing.
