"""Generate the synthetic datasets used by the case studies.

Every dataset is synthetic. The generating mechanism is documented here and in
``docs/data/case-studies/README.md``; the case studies repeat the relevant part
of the mechanism next to the data description. None of these files represents
real people, institutions or measurements, and no result computed from them
should be reported as an empirical finding.

All random draws use ``numpy.random.default_rng`` with a fixed seed per
dataset, so re-running this script reproduces every file byte for byte.

Usage
-----
    python tools/generate_case_data.py            # write docs/data/case-studies/*.csv
    python tools/generate_case_data.py --check    # fail if a file differs from a fresh run

Exits 0 on success.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import pathlib
import sys

import numpy as np
import pandas as pd

OUT = pathlib.Path("docs/data/case-studies")


def _write(name: str, frame: pd.DataFrame) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    frame.to_csv(path, index=False, float_format="%.3f", lineterminator="\n")
    print(f"  {name:34s} rows={len(frame):5d}  cols={frame.shape[1]}")


# --------------------------------------------------------------------------- E01
def exam_marks() -> pd.DataFrame:
    """200 students, three assessments, with attendance driving the final mark."""
    rng = np.random.default_rng(1101)
    n = 200
    programme = rng.choice(["DS", "CS", "SE"], size=n, p=[0.5, 0.3, 0.2])
    ability = rng.normal(0, 1, n) + np.where(programme == "DS", 0.2, 0.0)
    attendance = np.clip(rng.normal(76, 13, n) + 3 * ability, 25, 100)
    study_hours = np.clip(rng.gamma(4, 1.5, n) + 0.7 * ability, 0.5, 35)
    midterm = np.clip(52 + 9 * ability + 0.14 * attendance + rng.normal(0, 7, n), 0, 100)
    final = np.clip(44 + 10 * ability + 0.18 * attendance + 1.1 * study_hours
                    + rng.normal(0, 6, n), 0, 100)
    return pd.DataFrame({
        "student_id": np.arange(2001, 2001 + n),
        "programme": programme,
        "attendance_pct": attendance.round(1),
        "study_hours_wk": study_hours.round(1),
        "midterm": midterm.round(1),
        "final": final.round(1),
    })


# --------------------------------------------------------------------------- E02
def attendance_achievement() -> pd.DataFrame:
    """150 students; attendance is correlated with marks through shared motivation."""
    rng = np.random.default_rng(1102)
    n = 150
    motivation = rng.normal(0, 1, n)
    attendance = np.clip(rng.normal(74, 12, n) + 6 * motivation, 30, 100)
    assignment = np.clip(58 + 7 * motivation + rng.normal(0, 8, n), 0, 100)
    final_mark = np.clip(45 + 8 * motivation + 0.22 * attendance + rng.normal(0, 7, n), 0, 100)
    return pd.DataFrame({
        "student_id": np.arange(3001, 3001 + n),
        "semester": rng.choice([1, 2, 3, 4], size=n),
        "attendance_pct": attendance.round(1),
        "assignment_avg": assignment.round(1),
        "final_mark": final_mark.round(1),
    })


# --------------------------------------------------------------------------- E03 / A04
def screening() -> pd.DataFrame:
    """500 patients: disease prevalence 0.12, sensitivity 0.90, specificity 0.92."""
    rng = np.random.default_rng(1103)
    n = 500
    prevalence, sens, spec = 0.12, 0.90, 0.92
    disease = rng.random(n) < prevalence
    positive = np.where(disease, rng.random(n) < sens, rng.random(n) > spec)
    return pd.DataFrame({
        "patient_id": np.arange(5001, 5001 + n),
        "age": np.clip(rng.normal(48, 15, n), 18, 90).round(0).astype(int),
        "test_result": np.where(positive, "positive", "negative"),
        "disease": disease.astype(int),
    })


# --------------------------------------------------------------------------- E04
def satisfaction() -> pd.DataFrame:
    """180 survey responses: satisfaction (1-5) depends on waiting time."""
    rng = np.random.default_rng(1104)
    n = 180
    department = rng.choice(["Registration", "Library", "IT Desk", "Finance"], size=n,
                            p=[0.3, 0.25, 0.25, 0.2])
    wait = np.clip(rng.gamma(2.5, 8, n), 1, 90)
    baseline = {"Registration": 3.2, "Library": 4.0, "IT Desk": 3.5, "Finance": 3.1}
    latent = np.array([baseline[d] for d in department]) - 0.04 * wait + rng.normal(0, 0.9, n)
    satisfaction = np.clip(np.round(latent), 1, 5).astype(int)
    return pd.DataFrame({
        "respondent_id": np.arange(6001, 6001 + n),
        "department": department,
        "wait_minutes": wait.round(1),
        "resolved_first_contact": rng.choice(["yes", "no"], size=n, p=[0.7, 0.3]),
        "satisfaction": satisfaction,
    })


# --------------------------------------------------------------------------- E05 / A07
def shaft_diameters() -> pd.DataFrame:
    """300 machined shafts on two machines; target diameter 25.00 mm, sd 0.06."""
    rng = np.random.default_rng(1105)
    n = 300
    machine = rng.choice(["M1", "M2"], size=n, p=[0.6, 0.4])
    centre = np.where(machine == "M1", 25.00, 25.05)
    spread = np.where(machine == "M1", 0.055, 0.075)
    diameter = rng.normal(centre, spread, n)
    return pd.DataFrame({
        "unit_id": np.arange(7001, 7001 + n),
        "batch": np.repeat(np.arange(1, 31), 10),
        "machine": machine,
        "diameter_mm": diameter.round(3),
    })


# --------------------------------------------------------------------------- E06
def cricket_innings() -> pd.DataFrame:
    """120 innings from six batters; runs are over-dispersed relative to Poisson."""
    rng = np.random.default_rng(1106)
    batters = {"A. Khan": 34, "B. Ali": 28, "C. Raza": 22, "D. Iqbal": 18, "E. Shah": 12, "F. Noor": 8}
    rows = []
    for index, (name, rate) in enumerate(batters.items(), start=1):
        innings = 20
        # Negative binomial: mean rate, variance rate * 1.6 (over-dispersed).
        runs = rng.negative_binomial(n=max(1, int(rate / 0.6)), p=1 / (1 + 0.6), size=innings)
        balls = np.clip((runs / rng.uniform(0.8, 1.6, innings)).round(0), 1, None).astype(int)
        for innings_no in range(innings):
            rows.append({
                "batter": name,
                "innings_no": innings_no + 1,
                "runs": int(runs[innings_no]),
                "balls_faced": int(balls[innings_no]),
                "dismissed": rng.choice(["yes", "no"], p=[0.85, 0.15]),
                "venue": rng.choice(["home", "away"], p=[0.5, 0.5]),
            })
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- E07
def response_times() -> pd.DataFrame:
    """1,200 requests: lognormal latency, faster when served from cache."""
    rng = np.random.default_rng(1107)
    n = 1200
    endpoint = rng.choice(["/search", "/product", "/checkout", "/profile"], size=n,
                          p=[0.4, 0.3, 0.15, 0.15])
    cache_hit = rng.random(n) < 0.65
    base = {"/search": 120, "/product": 180, "/checkout": 260, "/profile": 90}
    median = np.array([base[e] for e in endpoint]) * np.where(cache_hit, 0.55, 1.0)
    latency = rng.lognormal(mean=np.log(median), sigma=0.55, size=n)
    return pd.DataFrame({
        "request_id": np.arange(8001, 8001 + n),
        "endpoint": endpoint,
        "cache_hit": np.where(cache_hit, "yes", "no"),
        "latency_ms": latency.round(1),
        "status": rng.choice([200, 200, 200, 404, 500], size=n, p=[0.9, 0.03, 0.03, 0.03, 0.01]),
    })


# --------------------------------------------------------------------------- E08
def insurance_claims() -> pd.DataFrame:
    """400 motor policies; claim amounts are right-skewed with many zeros."""
    rng = np.random.default_rng(1108)
    n = 400
    vehicle_age = rng.integers(0, 15, n)
    region = rng.choice(["urban", "suburban", "rural"], size=n, p=[0.5, 0.35, 0.15])
    claim_prob = np.clip(0.08 + 0.01 * vehicle_age + np.where(region == "urban", 0.03, 0.0), 0, 0.6)
    claimed = rng.random(n) < claim_prob
    amount = np.where(claimed, rng.lognormal(mean=9.2, sigma=0.7, size=n), 0.0)
    return pd.DataFrame({
        "policy_id": np.arange(9001, 9001 + n),
        "vehicle_age_years": vehicle_age,
        "region": region,
        "policy_years": rng.integers(1, 12, n),
        "claim_amount": amount.round(2),
    })


# --------------------------------------------------------------------------- I02
def daily_sessions() -> pd.DataFrame:
    """60 days of traffic; conversions rise slowly and differ by channel."""
    rng = np.random.default_rng(1202)
    days = pd.date_range("2026-01-01", periods=60, freq="D")
    rows = []
    for channel, share, rate in [("organic", 0.5, 0.032), ("paid", 0.3, 0.041), ("email", 0.2, 0.055)]:
        visitors = rng.poisson(1800 * share * (1 + 0.004 * np.arange(60)))
        conversions = rng.binomial(visitors, rate)
        for day, v, c in zip(days, visitors, conversions):
            rows.append({"date": day.date().isoformat(), "channel": channel,
                         "visitors": int(v), "conversions": int(c)})
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- I03
def production_batches() -> pd.DataFrame:
    """40 batches; defect rate rises on the night shift and after day 25."""
    rng = np.random.default_rng(1203)
    n_batches = 40
    shift = rng.choice(["day", "night"], size=n_batches, p=[0.6, 0.4])
    inspected = rng.integers(180, 240, n_batches)
    drift = np.where(np.arange(n_batches) > 25, 0.012, 0.0)
    rate = np.clip(0.018 + np.where(shift == "night", 0.009, 0.0) + drift, 0, 1)
    defective = rng.binomial(inspected, rate)
    return pd.DataFrame({
        "batch_id": np.arange(1, n_batches + 1),
        "shift": shift,
        "inspected": inspected,
        "defective": defective,
    })


# --------------------------------------------------------------------------- I04
def forecasts() -> pd.DataFrame:
    """200 days of next-day temperature forecasts and outcomes."""
    rng = np.random.default_rng(1204)
    n = 200
    truth = 25 + 8 * np.sin(np.arange(n) / 12) + rng.normal(0, 3, n)
    forecast = truth + rng.normal(0, 2.2, n)
    rain_prob = 1 / (1 + np.exp(-(0.9 * np.sin(np.arange(n) / 9) + rng.normal(0, 0.7, n))))
    rained = rng.random(n) < rain_prob
    return pd.DataFrame({
        "day": np.arange(1, n + 1),
        "forecast_temp": forecast.round(1),
        "observed_temp": truth.round(1),
        "rain_forecast_prob": rain_prob.round(3),
        "rained": rained.astype(int),
    })


# --------------------------------------------------------------------------- I05
def packets() -> pd.DataFrame:
    """1,000 packets on two links; loss depends on packet size and link."""
    rng = np.random.default_rng(1205)
    n = 1000
    link = rng.choice(["fibre", "radio"], size=n, p=[0.65, 0.35])
    size = np.clip(rng.lognormal(mean=7.0, sigma=0.7, size=n), 200, 9000)
    logit = -4.2 + 0.00035 * size + np.where(link == "radio", 0.8, 0.0)
    lost = rng.random(n) < 1 / (1 + np.exp(-logit))
    return pd.DataFrame({
        "packet_id": np.arange(1, n + 1),
        "link": link,
        "size_bytes": size.round(0).astype(int),
        "hour": rng.integers(0, 24, n),
        "lost": lost.astype(int),
    })


# --------------------------------------------------------------------------- I06
def loans() -> pd.DataFrame:
    """800 loan applications; default falls with credit score and income."""
    rng = np.random.default_rng(1206)
    n = 800
    credit = np.clip(rng.normal(640, 75, n), 300, 850)
    income = np.clip(rng.lognormal(mean=np.log(55000), sigma=0.45, size=n), 12000, 250000)
    amount = np.clip(rng.lognormal(mean=np.log(180000), sigma=0.6, size=n), 20000, 900000)
    employment = rng.integers(0, 25, n)
    logit = (-1.2 - 0.006 * (credit - 640) + 0.9 * np.log(amount / income)
             - 0.04 * employment)
    default = rng.random(n) < 1 / (1 + np.exp(-logit))
    return pd.DataFrame({
        "application_id": np.arange(1, n + 1),
        "credit_score": credit.round(0).astype(int),
        "annual_income": income.round(0).astype(int),
        "loan_amount": amount.round(0).astype(int),
        "employment_years": employment,
        "default": default.astype(int),
    })


# --------------------------------------------------------------------------- I07
def ab_test() -> pd.DataFrame:
    """800 sessions: variant B has a small true lift; mobile converts less."""
    rng = np.random.default_rng(1207)
    n = 800
    variant = rng.choice(["A", "B"], size=n)
    device = rng.choice(["desktop", "mobile"], size=n, p=[0.45, 0.55])
    logit = -2.6 + np.where(variant == "B", 0.28, 0.0) + np.where(device == "mobile", -0.25, 0.0)
    converted = rng.random(n) < 1 / (1 + np.exp(-logit))
    return pd.DataFrame({
        "session_id": np.arange(1, n + 1),
        "variant": variant,
        "device": device,
        "converted": converted.astype(int),
        "session_seconds": np.clip(rng.lognormal(4.3, 0.8, n), 5, 1800).round(0).astype(int),
    })


# --------------------------------------------------------------------------- I08
def football_matches() -> pd.DataFrame:
    """180 matches; goals follow a Poisson model with home advantage."""
    rng = np.random.default_rng(1208)
    n = 180
    teams = ["Falcons", "Tigers", "Wolves", "Eagles", "Sharks", "Lions"]
    rows = []
    for _ in range(n):
        home, away = rng.choice(teams, size=2, replace=False)
        home_goals = rng.poisson(1.55)
        away_goals = rng.poisson(1.05)
        rows.append({"home_team": home, "away_team": away,
                     "home_goals": int(home_goals), "away_goals": int(away_goals)})
    frame = pd.DataFrame(rows)
    frame["result"] = np.select(
        [frame.home_goals > frame.away_goals, frame.home_goals == frame.away_goals],
        ["home_win", "draw"], default="away_win")
    return frame


# --------------------------------------------------------------------------- A01
def epidemic_runs() -> pd.DataFrame:
    """200 SIR simulations; beta and gamma vary, R0 = beta/gamma."""
    rng = np.random.default_rng(1301)
    rows = []
    for run in range(200):
        beta = rng.uniform(0.25, 0.55)
        gamma = rng.uniform(0.1, 0.2)
        population = 100_000
        s, i, r = population - 50, 50, 0
        peak = i
        duration = 0
        for day in range(400):
            new_infections = beta * s * i / population
            new_recoveries = gamma * i
            s -= new_infections
            i += new_infections - new_recoveries
            r += new_recoveries
            peak = max(peak, i)
            duration = day + 1
            if i < 1:
                break
        rows.append({"run": run + 1, "beta": round(beta, 3), "gamma": round(gamma, 3),
                     "r0": round(beta / gamma, 3), "peak_infected": int(peak),
                     "total_infected": int(population - s), "duration_days": duration})
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- A02
def transactions() -> pd.DataFrame:
    """2,000 transactions from 500 customers; amount depends on segment and items."""
    rng = np.random.default_rng(1302)
    n_customers = 500
    segment = rng.choice(["new", "returning", "vip"], size=n_customers, p=[0.5, 0.4, 0.1])
    spend_multiplier = {"new": 1.0, "returning": 1.3, "vip": 2.2}
    rows = []
    for customer in range(1, n_customers + 1):
        visits = rng.poisson(4) + 1
        seg = segment[customer - 1]
        for visit in range(visits):
            items = rng.integers(1, 6)
            amount = rng.lognormal(np.log(35 * spend_multiplier[seg] * items), 0.5, size=1)[0]
            rows.append({
                "customer_id": customer,
                "segment": seg,
                "transaction_no": visit + 1,
                "items": int(items),
                "amount": round(float(amount), 2),
                "category": rng.choice(["grocery", "electronics", "fashion"],
                                       p=[0.6, 0.2, 0.2]),
                "day": int(rng.integers(1, 31)),
            })
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- A03
def app_sessions() -> pd.DataFrame:
    """600 app sessions; latency is a mixture of fast and slow, crashes rise with it."""
    rng = np.random.default_rng(1303)
    n = 600
    device = rng.choice(["low-end", "mid", "high"], size=n, p=[0.35, 0.45, 0.2])
    network = rng.choice(["wifi", "4g", "3g"], size=n, p=[0.5, 0.35, 0.15])
    base = {"low-end": 420, "mid": 260, "high": 150}
    latency = np.array([base[d] for d in device]) * np.where(network == "3g", 1.9,
                                                            np.where(network == "4g", 1.25, 1.0))
    latency = latency * rng.lognormal(0, 0.45, n)
    crash_prob = 1 / (1 + np.exp(-(-3.6 + 0.004 * latency)))
    return pd.DataFrame({
        "session_id": np.arange(1, n + 1),
        "device": device,
        "network": network,
        "app_version": rng.choice(["3.1", "3.2"], size=n, p=[0.4, 0.6]),
        "latency_ms": latency.round(0).astype(int),
        "crashed": (rng.random(n) < crash_prob).astype(int),
    })


# --------------------------------------------------------------------------- A05
def model_predictions() -> pd.DataFrame:
    """500 predictions at two thresholds' worth of information, overconfident model."""
    rng = np.random.default_rng(1305)
    n = 500
    segment = rng.choice(["new", "returning"], size=n, p=[0.4, 0.6])
    logit = rng.normal(0, 1.1, n) + np.where(segment == "returning", 0.3, -0.2)
    p_true = 1 / (1 + np.exp(-logit))
    y_true = (rng.random(n) < p_true).astype(int)
    # The model is overconfident: it exaggerates the log-odds by 40%.
    logit_hat = 1.4 * logit + rng.normal(0, 0.35, n)
    prob = 1 / (1 + np.exp(-logit_hat))
    return pd.DataFrame({
        "case_id": np.arange(1, n + 1),
        "segment": segment,
        "y_true": y_true,
        "predicted_prob": prob.round(4),
    })


# --------------------------------------------------------------------------- A06
def student_outcomes() -> pd.DataFrame:
    """300 students; tutoring is chosen by motivated students, which confounds marks."""
    rng = np.random.default_rng(1306)
    n = 300
    motivation = rng.normal(0, 1, n)
    prior_gpa = np.clip(2.6 + 0.5 * motivation + rng.normal(0, 0.35, n), 0, 4)
    tutoring = (motivation + rng.normal(0, 0.9, n) > 0.3).astype(int)
    attendance = np.clip(70 + 8 * motivation + rng.normal(0, 10, n), 30, 100)
    final = np.clip(45 + 6 * prior_gpa + 3.5 * tutoring + 0.15 * attendance
                    + 4 * motivation + rng.normal(0, 6, n), 0, 100)
    return pd.DataFrame({
        "student_id": np.arange(4001, 4001 + n),
        "prior_gpa": prior_gpa.round(2),
        "motivation_score": motivation.round(2),
        "tutoring": tutoring,
        "attendance_pct": attendance.round(1),
        "final_mark": final.round(1),
    })


# --------------------------------------------------------------------------- A08
def claim_counts() -> pd.DataFrame:
    """600 policy-years; claim counts follow a Poisson with exposure."""
    rng = np.random.default_rng(1308)
    n = 600
    age = np.clip(rng.normal(42, 13, n), 18, 80)
    exposure = rng.uniform(0.25, 1.0, n)
    region = rng.choice(["north", "south", "east"], size=n)
    log_rate = -1.9 + 0.012 * (age - 42) + np.where(region == "south", 0.25, 0.0)
    claims = rng.poisson(np.exp(log_rate) * exposure)
    return pd.DataFrame({
        "policy_id": np.arange(1, n + 1),
        "age": age.round(0).astype(int),
        "region": region,
        "exposure_years": exposure.round(2),
        "claims": claims,
    })


DATASETS = {
    "exam_marks.csv": exam_marks,
    "attendance_achievement.csv": attendance_achievement,
    "screening.csv": screening,
    "satisfaction.csv": satisfaction,
    "shaft_diameters.csv": shaft_diameters,
    "cricket_innings.csv": cricket_innings,
    "response_times.csv": response_times,
    "insurance_claims.csv": insurance_claims,
    "daily_sessions.csv": daily_sessions,
    "production_batches.csv": production_batches,
    "forecasts.csv": forecasts,
    "packets.csv": packets,
    "loans.csv": loans,
    "ab_test.csv": ab_test,
    "football_matches.csv": football_matches,
    "epidemic_runs.csv": epidemic_runs,
    "transactions.csv": transactions,
    "app_sessions.csv": app_sessions,
    "model_predictions.csv": model_predictions,
    "student_outcomes.csv": student_outcomes,
    "claim_counts.csv": claim_counts,
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    changed: list[str] = []
    print(f"writing {len(DATASETS)} datasets to {OUT}")
    for name, builder in DATASETS.items():
        frame = builder()
        buffer = io.StringIO()
        frame.to_csv(buffer, index=False, float_format="%.3f", lineterminator="\n")
        text = buffer.getvalue()
        path = OUT / name
        if args.check:
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current is None or current.replace("\r\n", "\n") != text.replace("\r\n", "\n"):
                changed.append(name)
            continue
        path.write_text(text, encoding="utf-8", newline="\n")
        digest = hashlib.sha256(text.encode()).hexdigest()[:12]
        print(f"  {name:34s} rows={len(frame):5d} cols={frame.shape[1]:2d} sha256:{digest}")

    if args.check:
        if changed:
            print(f"{len(changed)} dataset(s) differ from a fresh run: {changed}")
            print("run: python tools/generate_case_data.py")
            return 1
        print("all datasets match a fresh run")
    else:
        print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
