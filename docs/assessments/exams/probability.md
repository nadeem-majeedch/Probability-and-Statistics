# Probability examination

**Covers:** Modules 05–13. **Time:** 90 minutes. **Total:** 100 marks.
**Instructions:** closed book; calculator allowed. Show working for Section C. The answer key is
at the end.

| Section | Items | Marks | Suggested time |
|---|---|---|---|
| A. Multiple choice | 20 | 40 | 30 min |
| B. Short answers | 3 | 15 | 15 min |
| C. Numerical | 6 | 33 | 30 min |
| D. Scenario | 2 | 12 | 15 min |

## Section A — Multiple choice (2 marks each)

```quiz
Q1. The number of ways to select a president and a treasurer from 12 people is
A) 144
B) 24
C) 66
D) 132
* D
Why: Order matters for distinct offices: \(12\times11=132\). The value 66 is the unordered pair count.

Q2. A committee of 5 is chosen from 11. The number of possible committees is
A) 55,440
B) 55
C) 11
D) 462
* D
Why: \(\binom{11}{5}=462\). The larger number counts ordered selections.

Q3. The coefficient of \(x^2y^2\) in \((x+y)^4\) is
A) 4
B) 6
C) 8
D) 16
* B
Why: \(\binom{4}{2}=6\). The sum of all coefficients is \(2^4=16\).

Q4. For events with \(P(A)=0.6\), \(P(B)=0.5\), \(P(A\cup B)=0.8\), \(P(A\cap B)\) is
A) 0.3
B) 0.2
C) 0.1
D) 0.4
* A
Why: Rearranging the addition rule gives \(0.6+0.5-0.8=0.3\). Since \(P(A)P(B)=0.3\) as well, these events happen to be independent, which is a coincidence of the chosen numbers.

Q5. \(P(A\mid B)=0.4\), \(P(B)=0.5\). Then \(P(A\cap B)\) is
A) 0.9
B) 0.2
C) 0.8
D) 0.1
* B
Why: Multiply: \(P(A\cap B)=P(A\mid B)P(B)=0.4\times0.5=0.2\). Adding would exceed the bounds.

Q6. A biased coin has \(P(H)=0.7\). The probability of exactly two heads in three tosses is
A) 0.441
B) 0.189
C) 0.147
D) 0.343
* A
Why: \(\binom{3}{2}(0.7)^2(0.3)=3\times0.49\times0.3=0.441\). The value 0.343 is three heads.

Q7. A screening programme has prevalence 0.5 %, sensitivity 100 %, specificity 95 %. The PPV is
A) 5 %
B) 100 %
C) 50 %
D) 9 %
* D
Why: Per 10,000: 50 true positives and about 498 false positives, so \(50/548\approx9\) %. Perfect sensitivity does not prevent many false positives.

Q8. If \(A\) and \(B\) are independent, then \(P(A\cup B)\) equals
A) \(P(A)+P(B)\)
B) \(P(A)+P(B)-P(A)P(B)\)
C) \(P(A)P(B)\)
D) \(1-P(A)P(B)\)
* B
Why: Independence gives \(P(A\cap B)=P(A)P(B)\), so the union is \(P(A)+P(B)-P(A)P(B)\).

Q9. A Poisson variable has mean 2.5. Its variance is
A) 1.58
B) 2.5
C) 6.25
D) 5
* B
Why: Poisson mean equals variance, so 2.5. The value 1.58 is the standard deviation.

Q10. The probability of at least two successes in 5 independent trials with \(p=0.3\) is
A) 0.8369
B) 0.4718
C) 0.5282
D) 0.1631
* B
Why: \(P(0)=0.7^5=0.16807\) and \(P(1)=5(0.3)(0.7^4)=0.36015\), so \(P(\ge2)=1-0.52822=0.4718\). The complement is far quicker than summing the tail.

Q11. A geometric random variable with \(p=0.4\) has \(P(X\le2)\) equal to
A) 0.16
B) 0.64
C) 0.24
D) 0.84
* B
Why: \(P(X=1)=0.4\), \(P(X=2)=0.6(0.4)=0.24\); the sum is 0.64.

Q12. Sampling 4 items without replacement from 15 containing 5 defectives, \(P(X=0)\) is
A) 0.396
B) 0.527
C) 0.153
D) 0.316
* C
Why: \(\binom{10}{4}/\binom{15}{4}=210/1{,}365=0.1538\). The binomial with \(p=1/3\) would give 0.198, so ignoring the finite population would overstate the chance of a clean sample.

Q13. For \(X\sim\mathrm{Uniform}(2,8)\), \(P(3<X<5)\) is
A) 2/3
B) 1/6
C) 1/3
D) 1/2
* C
Why: Width 2 over total width 6 gives \(2/6=1/3\).

Q14. For \(Z\sim N(0,1)\), \(P(|Z|>1.645)\) is about
A) 0.01
B) 0.05
C) 0.10
D) 0.90
* C
Why: Each tail is 0.05, so the two-sided probability is 0.10. The value 0.05 is the one-sided figure.

Q15. An exponential variable with mean 8 has \(P(X<8)\) equal to
A) 0.632
B) 0.368
C) 0.125
D) 0.5
* A
Why: \(P(X<8)=1-e^{-1}=0.632\). The median would be \(8\ln2=5.545\), so 8 exceeds the median.

Q16. If \(\mathrm{Cov}(X,Y)=6\), \(\sigma_X=3\), \(\sigma_Y=5\), the correlation is
A) 0.6
B) 2.0
C) 0.5
D) 0.4
* D
Why: \(6/(3\times5)=0.4\). Correlation divides by both standard deviations.

Q17. \(X\) and \(Y\) are independent with variances 2 and 8. The variance of \(3X-Y\) is
A) 26
B) 10
C) 14
D) 18
* A
Why: \(9(2)+8=26\). Independence removes the covariance term, but the coefficient is squared.

Q18. A sample of 100 has \(\sigma=20\). The standard error of the mean is
A) 20
B) 0.5
C) 2
D) 0.2
* C
Why: \(20/10=2\). Dividing by \(n\) instead of \(\sqrt n\) gives the wrong 0.2.

Q19. The CLT states that for large \(n\), the distribution of the sample mean is approximately
A) exponential
B) exactly the population distribution
C) normal with mean \(\mu\) and variance \(\sigma^2/n\)
D) normal with variance \(\sigma^2\)
* C
Why: The mean stays \(\mu\), and the variance shrinks by \(1/n\). The population distribution itself is unchanged.

Q20. A \(t\) distribution with 5 degrees of freedom, compared with the standard normal, has
A) the same density
B) bounded support
C) thinner tails
D) thicker tails
* D
Why: Few degrees of freedom mean a noisy variance estimate, so extreme values are more likely than under the normal.
```

## Section B — Short answers (5 marks each)

**S1.** Derive \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\) and explain the role of the subtracted term.

<details><summary>Model answer</summary>
Split \(A\cup B\) into the disjoint events \(A\cap B^c\), \(A^c\cap B\) and \(A\cap B\). Their
probabilities sum to the union. Also \(P(A)=P(A\cap B^c)+P(A\cap B)\) and similarly for \(B\), so
adding the two gives the union plus twice the intersection. Subtracting once corrects the
double count.
</details>

**S2.** Explain why a Poisson process has a memoryless waiting time.

<details><summary>Model answer</summary>
With a constant rate, the probability of no event in an interval of length \(t\) is
\(e^{-\lambda t}\), regardless of what happened before. Conditioning on having waited \(s\)
therefore leaves the residual distribution unchanged, which is the memoryless property behind
both the exponential and geometric distributions.
</details>

**S3.** State the central limit theorem and explain why it does not make the data normal.

<details><summary>Model answer</summary>
For i.i.d. observations with mean \(\mu\) and finite variance, the standardised sample mean tends
to \(N(0,1)\). It concerns the distribution of the average over repeated samples, not the
observations themselves, which retain their original shape. This is why normal-based inference
can work on skewed data once \(n\) is large.
</details>

## Section C — Numerical problems (5–6 marks each)

**N1.** A bag has 4 red and 6 blue balls. Two are drawn without replacement. Find the probability
that they are different colours.

<details><summary>Worked solution</summary>
\(P(RB)+P(BR)=\frac{4}{10}\cdot\frac{6}{9}+\frac{6}{10}\cdot\frac{4}{9}
=\frac{24}{90}+\frac{24}{90}=0.533\). Equivalently \(1-P(\text{same})=1-(12+30)/90=0.533\).
</details>

**N2.** A test has sensitivity 0.92 and specificity 0.96. Prevalence is 3 %. Compute the PPV and
NPV.

<details><summary>Worked solution</summary>
Per 10,000: 300 diseased → 276 positive; 9,700 healthy → 388 false positives. PPV
\(=276/664=0.416\). True negatives \(=9{,}700-388=9{,}312\); total negatives
\(=9{,}312+24=9{,}336\); NPV \(=9{,}312/9{,}336=0.9974\).
</details>

**N3.** \(X\sim\mathrm{Poisson}(3.5)\). Compute \(P(X\le1)\).

<details><summary>Worked solution</summary>
\(P(0)=e^{-3.5}=0.0302\); \(P(1)=3.5e^{-3.5}=0.1057\). Sum \(=0.1359\).
</details>

**N4.** A normal variable has mean 60 and SD 8. Find \(P(50<X<70)\).

<details><summary>Worked solution</summary>
\(z\) values \(-1.25\) and \(1.25\); \(\Phi(1.25)=0.8944\), so the probability is
\(0.8944-0.1056=0.7888\). About 79 % of values fall in this range.
</details>

**N5.** A sample of 64 has mean 21 and \(s=4\). Compute the 95 % interval using
\(t_{0.975,63}\approx2.00\).

<details><summary>Worked solution</summary>
\(\mathrm{SE}=4/8=0.5\); margin \(=2.00(0.5)=1.0\); interval \(20.0\) to \(22.0\).
</details>

**N6.** In 400 trials, 120 succeed. Compute the standard error of the proportion and a 95 %
interval.

<details><summary>Worked solution</summary>
\(\hat p=0.3\); \(\mathrm{SE}=\sqrt{0.3(0.7)/400}=0.0229\); interval
\(0.3\pm1.96(0.0229)=0.255\) to \(0.345\).
</details>

## Section D — Scenario (6 marks each)

**P1.** A factory tests each item twice using two independent checks. Sensitivity is 0.9 and
false-positive rate 0.05 for each, and an item is accepted only if both tests pass. Compute the
probability that a defective item passes both, and comment.

<details><summary>Outline answer</summary>
Independent errors: \(P(\text{both negative}\mid\text{defective})=(1-0.9)^2=0.01\). So only 1 %
of defectives slip through, at the cost of rejecting many good items: the false-rejection rate is
\(1-(0.95)^2=9.75\) % per item. The design is stringent but expensive; the choice depends on the
relative costs of escapes and false rejects.
</details>

**P2.** A monitoring system averages 50 sensor readings per minute. The individual readings have
mean 20 and SD 3 but a right-skewed distribution. Can the average be treated as normal for
control limits, and what would you check?

<details><summary>Outline answer</summary>
By the CLT, the average of 50 readings has mean 20 and standard error
\(3/\sqrt{50}=0.424\), and is approximately normal despite the skew, so 3-sigma limits around
20 ± 1.27 are reasonable. Check the skewness, look for autocorrelation between readings (which
would invalidate the independence assumption), and verify the false-alarm rate empirically with a
QQ plot or simulation.
</details>

## Answer key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|
| 1 | D | 6 | A | 11 | A | 16 | A |
| 2 | D | 7 | C | 12 | B | 17 | A |
| 3 | B | 8 | B | 13 | A | 18 | A |
| 4 | A | 9 | B | 14 | B | 19 | B |
| 5 | B | 10 | A | 15 | B | 20 | B |
