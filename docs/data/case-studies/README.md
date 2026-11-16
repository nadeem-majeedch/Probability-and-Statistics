# Case-study datasets

Every file in this directory is **synthetic**. It was produced by
`tools/generate_case_data.py`, which documents each generating mechanism in code and uses a
fixed seed per dataset, so the files are reproducible byte for byte:

```bash
python tools/generate_case_data.py           # regenerate all files
python tools/generate_case_data.py --check   # verify the files match a fresh run
```

No file contains real people, institutions, measurements or transactions. No number
computed from these files is an empirical finding about the world, and none should be cited
as research. They exist to make the analytical workflow in `docs/case-studies/` runnable.

## Files

| File | Rows | Columns | Seed | Mechanisms (short) | Used by |
|---|---|---|---|---|---|
| `exam_marks.csv` | 200 | 6 | 1101 | Latent ability drives attendance, study hours, midterm and final | E1 |
| `attendance_achievement.csv` | 150 | 5 | 1102 | Motivation drives attendance, assignments and final mark | E2 |
| `screening.csv` | 500 | 4 | 1103 | Prevalence 0.12, sensitivity 0.90, specificity 0.92 | E3, I1, A4 |
| `satisfaction.csv` | 180 | 5 | 1104 | Department baseline minus 0.04 per waiting minute | E4 |
| `shaft_diameters.csv` | 300 | 4 | 1105 | Two machines: normal(25.00, 0.055) and normal(25.05, 0.075) | E5, A7 |
| `cricket_innings.csv` | 120 | 6 | 1106 | Negative-binomial runs, over-dispersed by design | E6 |
| `response_times.csv` | 1200 | 5 | 1107 | Lognormal latency; cache multiplies the median by 0.55 | E7 |
| `insurance_claims.csv` | 400 | 5 | 1108 | Claim probability rises with vehicle age; lognormal severity | E8 |
| `daily_sessions.csv` | 180 | 4 | 1202 | Binomial conversions per channel over 60 days | I2 |
| `production_batches.csv` | 40 | 4 | 1203 | Binomial defectives; night shift and post-batch-25 drift | I3 |
| `forecasts.csv` | 200 | 5 | 1204 | Seasonal truth plus forecast noise; calibrated rain probability | I4 |
| `packets.csv` | 1000 | 5 | 1205 | Logistic loss probability in size and link | I5 |
| `loans.csv` | 800 | 6 | 1206 | Logistic default in score, loan-to-income and employment | I6 |
| `ab_test.csv` | 800 | 5 | 1207 | Randomised A/B with a small true lift and device effects | I7 |
| `football_matches.csv` | 180 | 5 | 1208 | Independent Poisson goals, means 1.55 and 1.05 | I8 |
| `epidemic_runs.csv` | 200 | 7 | 1301 | SIR simulation with uniform β and γ priors | A1 |
| `transactions.csv` | 2572 | 7 | 1302 | Poisson visits, lognormal baskets, segment multipliers | A2 |
| `app_sessions.csv` | 600 | 6 | 1303 | Latency mixture by device and network; crash logistic in latency | A3 |
| `model_predictions.csv` | 500 | 4 | 1305 | Overconfident predictions: log-odds scaled by 1.4 | A5 |
| `student_outcomes.csv` | 300 | 6 | 1306 | Tutoring self-selected by motivation; true effect 3.5 marks | A6 |
| `claim_counts.csv` | 600 | 5 | 1308 | Poisson claims with exposure offset by age and region | A8 |

## Regenerating a single file

The script has one builder function per dataset and a `DATASETS` mapping of filename to
builder. Import the module and call the builder:

```python
import pandas as pd
from tools.generate_case_data import exam_marks

exam_marks()          # returns the DataFrame
exam_marks().to_csv("exam_marks_copy.csv", index=False, float_format="%.3f")
```

Regenerating the whole directory is the supported workflow: the case studies quote numbers
computed from these files, so a change to any generator requires re-running
`tools/check_case_studies.py` and updating the prose where numbers move.
