"""Generate the synthetic datasets for the project-based learning section.

Every dataset is written to ``docs/data/projects/`` with a fixed seed, so the
files are reproducible byte-for-byte. None of the data describe real people,
institutions or matches; they are simulated with documented mechanisms so that
the statistical structure is known and the intended analyses have something to
find.

Usage
-----
    python tools/generate_project_data.py           # write the files
    python tools/generate_project_data.py --check   # verify they are current
"""

from __future__ import annotations

import argparse
import hashlib
import io
import pathlib

import numpy as np
import pandas as pd

OUT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "data" / "projects"


def rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def clip(x, lo, hi):
    return np.clip(x, lo, hi)


# ---------------------------------------------------------------------------
# P01 — university student performance
# ---------------------------------------------------------------------------
def student_performance(seed: int = 1101) -> pd.DataFrame:
    g = rng(seed)
    n = 480
    programme = g.choice(["BSDS", "BSCS", "BSSTAT"], n, p=[0.45, 0.35, 0.20])
    semester = g.integers(1, 9, n)
    attendance = clip(g.normal(78, 9.5, n), 40, 100)
    study = clip(g.lognormal(mean=np.log(10.5), sigma=0.38, size=n), 2, 30)
    prior_gpa = clip(g.normal(3.05, 0.42, n), 1.7, 4.0)
    part_time = g.random(n) < 0.34
    sleep = clip(g.normal(6.9, 1.05, n), 4, 10)
    score = (
        8.0
        + 0.22 * attendance
        + 1.60 * study
        + 5.00 * prior_gpa
        - 3.0 * part_time
        + 0.35 * (sleep - 6.9)
        + g.normal(0, 7.0, n)
    )
    exam = np.round(clip(score, 0, 100), 1)
    return pd.DataFrame(
        {
            "student_id": [f"S{1000 + i}" for i in range(n)],
            "programme": programme,
            "semester": semester,
            "attendance_pct": np.round(attendance, 1),
            "study_hours_week": np.round(study, 1),
            "prior_gpa": np.round(prior_gpa, 2),
            "part_time_job": part_time.astype(int),
            "sleep_hours": np.round(sleep, 1),
            "exam_score": exam,
        }
    )


# ---------------------------------------------------------------------------
# P02 — diagnostic accuracy
# ---------------------------------------------------------------------------
def diagnostics(seed: int = 1202) -> pd.DataFrame:
    g = rng(seed)
    n = 1600
    age = clip(g.normal(52, 14, n), 18, 90)
    sex = g.choice(["F", "M"], n)
    severity = clip(g.poisson(3.2, n), 0, 10)
    logit = -3.6 + 0.025 * age + 0.22 * severity
    disease = (g.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
    biomarker = 50 + 16 * disease + 0.12 * age + g.normal(0, 7, n)
    test_positive = (biomarker > 66).astype(int)
    return pd.DataFrame(
        {
            "patient_id": [f"PT{2000 + i}" for i in range(n)],
            "age": np.round(age, 0).astype(int),
            "sex": sex,
            "symptom_severity": severity,
            "biomarker": np.round(biomarker, 2),
            "test_positive": test_positive,
            "disease": disease,
        }
    )


# ---------------------------------------------------------------------------
# P03 — e-commerce experiment
# ---------------------------------------------------------------------------
def ecommerce(seed: int = 1303) -> pd.DataFrame:
    g = rng(seed)
    n = 12000
    variant = g.choice(["A", "B"], n)
    device = g.choice(["mobile", "desktop", "tablet"], n, p=[0.58, 0.34, 0.08])
    channel = g.choice(["organic", "paid", "email", "social"], n, p=[0.34, 0.28, 0.18, 0.20])
    base = np.where(variant == "B", 0.108, 0.085)
    base = base * np.where(device == "mobile", 0.86, np.where(device == "desktop", 1.18, 1.0))
    base = base * np.where(channel == "email", 1.25, np.where(channel == "paid", 1.05, 1.0))
    converted = (g.random(n) < clip(base, 0.01, 0.6)).astype(int)
    session = clip(g.lognormal(np.log(6.5), 0.55, n), 0.4, 90)
    pages = clip(g.poisson(5.5 + 0.4 * session, n), 1, 40)
    revenue = np.where(
        converted == 1,
        np.round(g.lognormal(np.log(38), 0.45, n), 2),
        0.0,
    )
    return pd.DataFrame(
        {
            "user_id": [f"U{500000 + i}" for i in range(n)],
            "variant": variant,
            "device": device,
            "channel": channel,
            "session_minutes": np.round(session, 1),
            "pages_viewed": pages,
            "converted": converted,
            "revenue": revenue,
        }
    )


# ---------------------------------------------------------------------------
# P04 — manufacturing quality
# ---------------------------------------------------------------------------
def manufacturing(seed: int = 1404) -> pd.DataFrame:
    g = rng(seed)
    n = 900
    line = g.choice(["L1", "L2", "L3"], n, p=[0.45, 0.35, 0.20])
    shift = g.choice(["day", "night"], n, p=[0.6, 0.4])
    temperature = g.normal(70, 3.4, n)
    pressure = g.normal(2.4, 0.22, n)
    batch_size = g.integers(380, 640, n)
    line_effect = np.where(line == "L1", 0.0, np.where(line == "L2", 0.32, 0.66))
    rate = np.exp(
        0.55
        + 0.055 * (temperature - 70)
        + 0.9 * (pressure - 2.4)
        + line_effect
        + 0.12 * (shift == "night")
        + g.normal(0, 0.28, n)  # extra-binomial variation between batches
    )
    defects = g.poisson(rate)
    return pd.DataFrame(
        {
            "batch_id": [f"B{3000 + i}" for i in range(n)],
            "line": line,
            "shift": shift,
            "temperature_c": np.round(temperature, 2),
            "pressure_bar": np.round(pressure, 2),
            "batch_size": batch_size,
            "defect_count": defects,
        }
    )


# ---------------------------------------------------------------------------
# P05 — weather
# ---------------------------------------------------------------------------
def weather(seed: int = 1505) -> pd.DataFrame:
    g = rng(seed)
    dates = pd.date_range("2023-01-01", "2025-12-31", freq="D")
    frames = []
    stations = {"Lahore": 1.5, "Murree": -8.0, "Karachi": 3.0}
    for station, offset in stations.items():
        n = len(dates)
        doy = dates.day_of_year.to_numpy()
        seasonal = 27 + 9.5 * np.sin(2 * np.pi * (doy - 100) / 365.25)
        temp_max = seasonal + offset + g.normal(0, 3.2, n)
        temp_min = temp_max - (9 + g.normal(0, 1.6, n)) + (2.5 if station == "Karachi" else 0)
        rain_prob = 0.18 + 0.20 * np.sin(2 * np.pi * (doy - 200) / 365.25) ** 2
        rain = np.where(g.random(n) < rain_prob, g.gamma(1.4, 6.0, n), 0.0)
        humidity = clip(58 + 14 * np.sin(2 * np.pi * (doy - 200) / 365.25) + g.normal(0, 7, n), 15, 100)
        wind = clip(g.gamma(2.0, 4.0, n), 0.2, 60)
        frames.append(
            pd.DataFrame(
                {
                    "date": dates.strftime("%Y-%m-%d"),
                    "station": station,
                    "temp_max_c": np.round(temp_max, 1),
                    "temp_min_c": np.round(temp_min, 1),
                    "rainfall_mm": np.round(rain, 1),
                    "humidity_pct": np.round(humidity, 1),
                    "wind_kmh": np.round(wind, 1),
                }
            )
        )
    return pd.concat(frames, ignore_index=True)


# ---------------------------------------------------------------------------
# P06 — credit risk
# ---------------------------------------------------------------------------
def credit_risk(seed: int = 1606) -> pd.DataFrame:
    g = rng(seed)
    n = 2000
    score = clip(g.normal(655, 68, n), 320, 850)
    income = np.round(g.lognormal(np.log(52000), 0.5, n), 0)
    loan_amount = np.round(clip(g.lognormal(np.log(18000), 0.6, n), 2000, 120000), 0)
    term = g.choice([12, 24, 36, 48, 60], n, p=[0.1, 0.22, 0.34, 0.18, 0.16])
    dti = clip(18 + 0.00022 * loan_amount - 0.02 * (score - 655) + g.normal(0, 6, n), 2, 75)
    logit = (
        -1.9
        - 0.010 * (score - 655)
        + 0.052 * (dti - 30)
        - 0.000012 * (income - 52000)
        + 0.004 * (term - 36)
    )
    default = (g.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
    region = g.choice(["urban", "semi-urban", "rural"], n, p=[0.5, 0.32, 0.18])
    return pd.DataFrame(
        {
            "loan_id": [f"LN{70000 + i}" for i in range(n)],
            "credit_score": np.round(score, 0).astype(int),
            "annual_income": income.astype(int),
            "loan_amount": loan_amount.astype(int),
            "term_months": term,
            "dti_pct": np.round(dti, 1),
            "region": region,
            "defaulted": default,
        }
    )


# ---------------------------------------------------------------------------
# P07 — cricket
# ---------------------------------------------------------------------------
def cricket(seed: int = 1707) -> pd.DataFrame:
    g = rng(seed)
    n = 260
    venues = ["Lahore", "Karachi", "Multan", "Rawalpindi", "Faisalabad"]
    teams = ["Lions", "Eagles", "Falcons", "Tigers", "Wolves", "Hawks"]
    rows = []
    for i in range(n):
        home = teams[g.integers(0, len(teams))]
        away = teams[g.integers(0, len(teams))]
        while away == home:
            away = teams[g.integers(0, len(teams))]
        venue = venues[g.integers(0, len(venues))]
        toss_winner = home if g.random() < 0.5 else away
        decision = "bat" if g.random() < 0.62 else "field"
        home_runs = int(clip(g.normal(166, 27), 78, 260))
        away_runs = int(clip(g.normal(156, 27), 70, 260))
        if home_runs == away_runs:
            home_runs += 1
        rows.append(
            {
                "match_id": f"M{9000 + i}",
                "home_team": home,
                "away_team": away,
                "venue": venue,
                "toss_winner": toss_winner,
                "toss_decision": decision,
                "home_runs": home_runs,
                "away_runs": away_runs,
                "home_won": int(home_runs > away_runs),
            }
        )
    frame = pd.DataFrame(rows)
    frame["margin_runs"] = (frame["home_runs"] - frame["away_runs"]).abs()
    return frame


# ---------------------------------------------------------------------------
# P08 — model prediction uncertainty
# ---------------------------------------------------------------------------
def model_uncertainty(seed: int = 1808) -> pd.DataFrame:
    g = rng(seed)
    n = 2400
    segment = g.choice(["new", "casual", "loyal", "at_risk"], n, p=[0.28, 0.34, 0.24, 0.14])
    version = g.choice(["v1", "v2"], n)
    base = g.beta(2.2, 5.0, n)
    base = np.where(segment == "at_risk", base * 1.8, base)
    base = np.where(segment == "loyal", base * 0.55, base)
    base = clip(base, 0.01, 0.97)
    # v1 is systematically over-confident; v2 is calibrated.
    predicted = np.where(version == "v1", clip(base * 1.25, 0.01, 0.99), base)
    truth = np.where(
        version == "v1",
        clip(base * 1.25 + g.normal(0, 0.16, n), 0.005, 0.995),
        base,
    )
    outcome = (g.random(n) < truth).astype(int)
    drift = np.round(g.normal(0, 1, n), 2)
    return pd.DataFrame(
        {
            "case_id": [f"C{40000 + i}" for i in range(n)],
            "segment": segment,
            "model_version": version,
            "predicted_prob": np.round(predicted, 4),
            "outcome": outcome,
            "feature_drift": drift,
        }
    )


# ---------------------------------------------------------------------------
# P09 — capstone: subscription churn
# ---------------------------------------------------------------------------
def capstone(seed: int = 1909) -> pd.DataFrame:
    g = rng(seed)
    n = 1400
    region = g.choice(["North", "South", "East", "West"], n, p=[0.3, 0.26, 0.24, 0.2])
    channel = g.choice(["organic", "referral", "paid", "partner"], n, p=[0.32, 0.24, 0.29, 0.15])
    plan = g.choice(["basic", "plus", "pro"], n, p=[0.46, 0.36, 0.18])
    tenure = np.round(clip(g.gamma(2.4, 8.0, n), 1, 60), 0)
    base_spend = np.where(plan == "basic", 24, np.where(plan == "plus", 42, 68))
    spend = np.round(base_spend + 0.28 * tenure + g.normal(0, 6, n), 2)
    tickets = g.poisson(np.where(plan == "basic", 1.55, np.where(plan == "plus", 1.15, 0.85)), n)
    sessions = clip(g.poisson(16 - 0.06 * tenure + 2.2 * (plan != "basic"), n), 0, 80)
    satisfaction = clip(
        8.1 - 0.75 * tickets + 0.05 * sessions - 0.7 * (channel == "paid") + g.normal(0, 1.2, n),
        1,
        10,
    )
    logit = (
        -0.55
        + 0.42 * tickets
        - 0.075 * sessions
        - 0.46 * (satisfaction - 7)
        + 0.55 * (channel == "paid")
        + 0.30 * (channel == "partner")
        - 0.030 * tenure
        + 0.25 * (plan == "basic")
        + np.where(region == "East", 0.45, 0.0)
    )
    churn = (g.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
    return pd.DataFrame(
        {
            "customer_id": [f"CUST{10000 + i}" for i in range(n)],
            "region": region,
            "signup_channel": channel,
            "plan": plan,
            "tenure_months": tenure.astype(int),
            "monthly_spend": spend,
            "support_tickets": tickets,
            "app_sessions_month": sessions,
            "satisfaction": np.round(satisfaction, 1),
            "churned": churn,
        }
    )


DATASETS = {
    "student_performance_project.csv": student_performance,
    "diagnostics_project.csv": diagnostics,
    "ecommerce_experiment_project.csv": ecommerce,
    "manufacturing_project.csv": manufacturing,
    "weather_project.csv": weather,
    "credit_risk_project.csv": credit_risk,
    "cricket_project.csv": cricket,
    "model_uncertainty_project.csv": model_uncertainty,
    "capstone_project.csv": capstone,
}


def render(name: str) -> str:
    frame = DATASETS[name]()
    buffer = io.StringIO()
    frame.to_csv(buffer, index=False, lineterminator="\n")
    return buffer.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    if args.check:
        changed = []
        for name in DATASETS:
            text = render(name)
            path = OUT / name
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current is None or current.replace("\r\n", "\n") != text.replace("\r\n", "\n"):
                changed.append(name)
        if changed:
            print("out of date:", ", ".join(changed))
            return 1
        print("all project datasets match a fresh run")
        return 0

    print(f"writing {len(DATASETS)} datasets to {OUT.relative_to(OUT.parents[2])}")
    for name in DATASETS:
        text = render(name)
        (OUT / name).write_text(text, encoding="utf-8", newline="")
        frame = DATASETS[name]()
        digest = hashlib.sha256(text.encode()).hexdigest()[:10]
        print(f"  {name:36s} rows={len(frame):5d} cols={frame.shape[1]:2d} sha256:{digest}")
    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
