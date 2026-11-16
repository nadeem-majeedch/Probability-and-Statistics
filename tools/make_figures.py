"""Generate every statistical figure used in the course chapters.

All figures are original, produced here from Python with fixed seeds, so the
repository contains no third-party images and every picture is reproducible:

    python tools/make_figures.py           # rewrite docs/assets/images/figures/*.svg
    python tools/make_figures.py --check   # fail if any file is missing

Design rules (kept identical across the course):

* one palette, one font, one grid style — see ``style()``;
* vector SVG so a phone can zoom without blurring, and files stay small;
* no chart junk: no 3-D, no shadows, no gradients, no unlabelled axes;
* annotation carries the teaching point ("mode < median < mean"), because the
  caption and the annotation together explain the figure.

The captions live in the chapters, next to the figure, not in the image.
"""

from __future__ import annotations

import pathlib
import re
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
from scipy import stats

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/assets/images/figures"

# One palette for the whole course.
INK = "#1b2a41"
ACCENT = "#b23a48"
TEAL = "#2a7f8f"
GOLD = "#b58a1f"
GREY = "#8c95a3"
BAND = "#dfe6ee"
FILL = "#9db4c0"


def style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.titlesize": 11.5,
        "axes.labelsize": 11,
        "axes.edgecolor": INK,
        "axes.labelcolor": INK,
        "axes.titlecolor": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": BAND,
        "grid.linewidth": 0.8,
        "axes.axisbelow": True,
        "xtick.color": INK,
        "ytick.color": INK,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "legend.frameon": False,
        "legend.fontsize": 9.5,
        "figure.dpi": 110,
        "savefig.dpi": 110,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.18,
        "svg.fonttype": "none",   # keep text as text: smaller files, selectable
        "svg.hashsalt": "psds-course",
    })


def save(fig: plt.Figure, name: str) -> None:
    path = OUT / name
    fig.savefig(path, format="svg", metadata={"Date": None})
    plt.close(fig)
    print(f"  {name:34} {path.stat().st_size / 1024:6.1f} KB")


# --------------------------------------------------------------------------- M03
def fig_centre() -> None:
    rng = np.random.default_rng(11)
    x = rng.lognormal(mean=3.4, sigma=0.55, size=600)
    mean, med = x.mean(), np.median(x)
    counts, edges = np.histogram(x, bins=60)
    mode = 0.5 * (edges[:-1] + edges[1:])[np.argmax(counts)]
    top = counts.max()

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.hist(x, bins=60, color=FILL, edgecolor="white", linewidth=0.4,
            label="600 simulated incomes")
    for value, colour, label in [
        (mode, GOLD, f"mode {mode:.1f}"),
        (med, TEAL, f"median {med:.1f}"),
        (mean, ACCENT, f"mean {mean:.1f}"),
    ]:
        ax.axvline(value, color=colour, linewidth=2.4)
    ax.set_ylim(0, top * 1.35)
    labels = [
        (mode, GOLD, f"mode ≈ {mode:.1f}", 60, 62),
        (med, TEAL, f"median = {med:.1f}", 60, 52),
        (mean, ACCENT, f"mean = {mean:.1f}", 60, 42),
    ]
    for value, colour, text, x_text, y_text in labels:
        ax.annotate(text, xy=(value, top * 0.62), xytext=(x_text, y_text),
                    fontsize=9.5, color=colour, fontweight="bold",
                    arrowprops=dict(arrowstyle="-", color=colour, lw=0.9))
    ax.annotate("long right tail: it pulls the mean right",
                xy=(x.max() - 6, top * 0.10), xytext=(x.max() - 62, top * 0.42),
                fontsize=9, color=INK,
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.1))
    ax.set_xlabel("monthly income (thousands)")
    ax.set_ylabel("number of people")
    ax.set_title("Right skew: mode < median < mean", pad=12)
    fig.tight_layout()
    save(fig, "fig-03-01-centre.svg")


def fig_spread() -> None:
    rng = np.random.default_rng(3)
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    for y, sd, label in [(1, 2.0, "A: SD = 2"), (0, 20.0, "B: SD = 20")]:
        xs = rng.normal(70, sd, 25)
        ax.scatter(xs, np.full(25, y) + rng.normal(0, 0.045, 25), s=26,
                   color=TEAL if y else ACCENT, alpha=0.85, label=label)
        ax.add_patch(Rectangle((70 - sd, y - 0.22), 2 * sd, 0.44, color=BAND,
                               zorder=0))
        ax.text(8, y + 0.30, f"±1 SD = {sd:.0f}", ha="left", va="center",
                fontsize=9, color=GREY)
    ax.axvline(70, color=INK, linewidth=1.6, linestyle="--")
    ax.text(70, 1.55, "both means = 70", ha="center", fontsize=10, color=INK)
    ax.set_yticks([1, 0], ["A", "B"])
    ax.set_ylim(-0.7, 1.8)
    ax.set_xlabel("value")
    ax.set_title("Identical centre, different spread")
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    save(fig, "fig-03-02-spread.svg")


def fig_hist_bins() -> None:
    rng = np.random.default_rng(7)
    x = np.concatenate([rng.normal(60, 9, 400), rng.normal(82, 6, 120)])
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.3), sharey=True)
    for ax, bins, note in zip(axes, (4, 44), ("4 bins: shape hidden",
                                              "44 bins: shape, but noisy")):
        ax.hist(x, bins=bins, color=FILL, edgecolor="white", linewidth=0.4)
        ax.set_title(note)
        ax.set_xlabel("exam mark")
    axes[0].set_ylabel("frequency")
    fig.suptitle("Bin width changes the story, not the data", fontsize=11.5, y=1.02)
    fig.tight_layout()
    save(fig, "fig-03-03-histogram-bins.svg")


def fig_boxplot() -> None:
    rng = np.random.default_rng(5)
    x = np.concatenate([rng.normal(50, 8, 120), [18, 96, 101]])
    q1, med, q3 = np.percentile(x, [25, 50, 75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    inside = x[(x >= lo) & (x <= hi)]

    fig, ax = plt.subplots(figsize=(7.4, 2.9))
    ax.boxplot(x, orientation="horizontal", widths=0.42, patch_artist=True,
               boxprops=dict(facecolor=BAND, edgecolor=INK),
               medianprops=dict(color=ACCENT, linewidth=2.2),
               whiskerprops=dict(color=INK), capprops=dict(color=INK),
               flierprops=dict(marker="o", markersize=5, markerfacecolor=GOLD,
                               markeredgecolor=INK, alpha=0.9))
    for value, label, y, ha in [(q1, f"Q1 = {q1:.1f}", 1.30, "right"),
                                (med, f"median = {med:.1f}", 1.46, "center"),
                                (q3, f"Q3 = {q3:.1f}", 1.30, "left")]:
        ax.annotate(label, xy=(value, 1.10), xytext=(value + (-0.8 if ha == "right" else 0.8 if ha == "left" else 0), y),
                    ha=ha, va="bottom", fontsize=9.5, color=INK,
                    arrowprops=dict(arrowstyle="-", color=GREY, lw=0.9))
    ax.annotate(f"whiskers reach the last point inside\nQ1 − 1.5·IQR = {lo:.1f},  Q3 + 1.5·IQR = {hi:.1f}",
                xy=(inside.max(), 1), xytext=(inside.max() - 22, 0.55),
                fontsize=8.8, color=GREY)
    ax.annotate("flagged outliers", xy=(101, 1), xytext=(101, 0.55), ha="center",
                fontsize=9, color=GOLD,
                arrowprops=dict(arrowstyle="->", color=GOLD, lw=1.1))
    ax.set_yticks([])
    ax.set_xlabel("test score")
    ax.set_ylim(0.25, 1.55)
    ax.set_title("A boxplot is a five-number summary with a rule for outliers")
    fig.tight_layout()
    save(fig, "fig-03-04-boxplot.svg")


# --------------------------------------------------------------------------- M04
def fig_bins_m04() -> None:
    rng = np.random.default_rng(19)
    x = rng.gamma(2.0, 12, 900)
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.3))
    for ax, bins, note in zip(axes, (3, 30), ("too few bins", "well chosen bins")):
        ax.hist(x, bins=bins, color=FILL, edgecolor="white", linewidth=0.4,
                density=True)
        ax.set_title(note)
        ax.set_xlabel("waiting time (min)")
    axes[0].set_ylabel("density")
    for ax in axes:
        axes[0].legend([], frameon=False)
    fig.suptitle("Same 900 observations, two bin choices", fontsize=11.5, y=1.02)
    fig.tight_layout()
    save(fig, "fig-04-01-bins.svg")


def fig_anscombe() -> None:
    x123 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
    y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
    y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
    y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
    x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
    y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

    datasets = [(x123, y1, "I"), (x123, y2, "II"), (x123, y3, "III"), (x4, y4, "IV")]
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 6.0), sharex=True, sharey=True)
    for ax, (xv, yv, tag) in zip(axes.ravel(), datasets):
        slope, intercept, r, *_ = stats.linregress(xv, yv)
        xs = np.linspace(3, 20, 50)
        ax.plot(xs, intercept + slope * xs, color=ACCENT, linewidth=1.8)
        ax.scatter(xv, yv, s=34, color=INK, zorder=3)
        ax.set_title(f"Data set {tag}")
        ax.text(0.04, 0.93, f"r = {r:.4f} | slope = {slope:.3f}",
                transform=ax.transAxes, fontsize=8.8, color=GREY, va="top")
    for ax in axes[1]:
        ax.set_xlabel("x")
    for ax in axes[:, 0]:
        ax.set_ylabel("y")
    fig.suptitle("Anscombe's quartet: identical statistics, four different datasets",
                 fontsize=11.5, y=1.00)
    fig.tight_layout()
    save(fig, "fig-04-02-anscombe.svg")


def fig_truncated() -> None:
    labels = ["A", "B", "C", "D"]
    values = [94.2, 95.1, 95.8, 96.4]
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.5), sharex=True)
    axes[0].bar(labels, values, color=TEAL, width=0.6)
    axes[0].set_ylim(0, 100)
    axes[0].set_title("zero baseline: differences look small")
    axes[1].bar(labels, values, color=ACCENT, width=0.6)
    axes[1].set_ylim(93, 97)
    axes[1].set_title("truncated axis: differences look huge")
    for ax in axes:
        ax.set_xlabel("group")
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("score (%)")
    fig.suptitle("The same four values, two honest-looking charts", fontsize=11.5, y=1.02)
    fig.tight_layout()
    save(fig, "fig-04-03-truncated-axis.svg")


# --------------------------------------------------------------------------- M09
def fig_binomial() -> None:
    n = 20
    k = np.arange(n + 1)
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 3.1), sharey=True)
    for ax, p in zip(axes, (0.2, 0.5, 0.8)):
        ax.vlines(k, 0, stats.binom.pmf(k, n, p), color=TEAL, linewidth=2)
        ax.plot(k, stats.binom.pmf(k, n, p), "o", color=TEAL, markersize=4.5)
        ax.set_title(f"p = {p}")
        ax.set_xlabel("successes k")
        ax.set_ylim(0, stats.binom.pmf(k, n, p).max() * 1.34)
        ax.text(0.03, 0.97, f"mean = {n*p:.0f}\nvariance = {n*p*(1-p):.1f}",
                transform=ax.transAxes, fontsize=9, color=GREY, va="top")
    axes[0].set_ylabel("P(X = k)")
    fig.suptitle("Binomial(n = 20): the mean moves, the spread is widest at p = 0.5",
                 fontsize=11.5, y=1.03)
    fig.tight_layout()
    save(fig, "fig-09-01-binomial.svg")


def fig_poisson() -> None:
    k = np.arange(0, 22)
    fig, ax = plt.subplots(figsize=(7.4, 3.7))
    for lam, colour in [(1, TEAL), (4, GOLD), (10, ACCENT)]:
        ax.plot(k, stats.poisson.pmf(k, lam), "o-", color=colour, markersize=4,
                linewidth=1.6, label=f"λ = {lam}: mean = variance = {lam}")
    ax.set_xlabel("events in one unit of exposure")
    ax.set_ylabel("P(X = k)")
    ax.set_title("Poisson: one parameter sets both centre and spread")
    ax.legend()
    fig.tight_layout()
    save(fig, "fig-09-02-poisson.svg")


# --------------------------------------------------------------------------- M10
def fig_families() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 3.1))
    x_n = np.linspace(-4, 4, 400)
    axes[0].plot(x_n, stats.norm.pdf(x_n), color=TEAL, linewidth=2)
    axes[0].fill_between(x_n, stats.norm.pdf(x_n), color=TEAL, alpha=0.15)
    axes[0].set_title("normal: symmetric, unbounded")
    axes[1].set_title("exponential: memoryless wait")
    x_e = np.linspace(0, 6, 400)
    axes[1].plot(x_e, stats.expon.pdf(x_e, scale=1), color=GOLD, linewidth=2)
    axes[1].fill_between(x_e, stats.expon.pdf(x_e, scale=1), color=GOLD, alpha=0.15)
    x_g = np.linspace(0.01, 12, 400)
    for a, b, colour, lab in [(2, 1, TEAL, "shape 2"), (5, 1, ACCENT, "shape 5")]:
        axes[2].plot(x_g, stats.gamma.pdf(x_g, a, scale=b), color=colour,
                     linewidth=2, label=lab)
    axes[2].set_title("gamma: waits for r events")
    axes[2].legend()
    for ax in axes:
        ax.set_xlabel("x")
        ax.set_ylabel("density")
    fig.suptitle("Three continuous families, three shapes of uncertainty",
                 fontsize=11.5, y=1.03)
    fig.tight_layout()
    save(fig, "fig-10-01-families.svg")


def fig_empirical() -> None:
    x = np.linspace(-4, 4, 600)
    y = stats.norm.pdf(x)
    fig, ax = plt.subplots(figsize=(7.4, 3.9))
    ax.plot(x, y, color=INK, linewidth=2)
    shades = [(3, "#eef2f6", "99.7 % within 3σ"),
              (2, "#dbe4ec", "95 % within 2σ"),
              (1, FILL, "68 % within 1σ")]
    for width, colour, _ in shades:
        ax.fill_between(x, y, where=np.abs(x) <= width, color=colour, alpha=0.9)
    handles = [Rectangle((0, 0), 1, 1, facecolor=colour, alpha=0.9,
                         edgecolor=GREY, linewidth=0.5) for _, colour, _ in shades]
    labels = [label for _, _, label in shades]
    ax.legend(handles, labels, loc="upper left", fontsize=9.2, title="area under the curve",
              title_fontsize=9.2)
    for tick in (-3, -2, -1, 0, 1, 2, 3):
        ax.axvline(tick, color="white", linewidth=0.8, alpha=0.8)
        ax.text(tick, -0.018, f"{tick:+d}σ" if tick else "μ", ha="center",
                fontsize=9, color=GREY)
    ax.set_ylim(0, 0.44)
    ax.set_yticks([])
    ax.set_xlabel("standard deviations from the mean")
    ax.set_title("The empirical rule for normal data")
    fig.tight_layout()
    save(fig, "fig-10-02-normal-empirical.svg")


def fig_zscore() -> None:
    x1 = np.linspace(40, 100, 500)
    x2 = np.linspace(200, 800, 500)
    fig, (ax_raw, ax_z) = plt.subplots(1, 2, figsize=(9.0, 3.4))

    ax_raw.plot(x1, stats.norm.pdf(x1, 70, 8), color=TEAL, linewidth=2,
                label="test A: mean 70, SD 8")
    ax_raw.plot(x2, stats.norm.pdf(x2, 500, 100), color=ACCENT, linewidth=2,
                label="test B: mean 500, SD 100")
    ax_raw.axvline(82, color=TEAL, linestyle=":", linewidth=1.2)
    ax_raw.axvline(650, color=ACCENT, linestyle=":", linewidth=1.2)
    ax_raw.text(88, 0.043, "82", fontsize=9, color=TEAL)
    ax_raw.text(600, 0.0042, "650", fontsize=9, color=ACCENT)
    ax_raw.set_yticks([])
    ax_raw.set_xlabel("raw score, two unrelated scales")
    ax_raw.set_title("Before: the scales cannot be compared")
    ax_raw.legend(loc="upper right", fontsize=8.6)

    z = np.linspace(-3.6, 3.6, 400)
    ax_z.fill_between(z, stats.norm.pdf(z), where=z >= 1.5, color=ACCENT, alpha=0.25)
    ax_z.plot(z, stats.norm.pdf(z), color=INK, linewidth=2)
    ax_z.axvline(1.5, color=ACCENT, linewidth=1.6)
    ax_z.annotate("82 and 650 both land at z = +1.5" + chr(10) + "P(Z > 1.5) = 0.067",
                  xy=(1.5, 0.10), xytext=(-3.45, 0.185), fontsize=9.2, color=ACCENT,
                  arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax_z.set_yticks([])
    ax_z.set_xlabel("standard score z = (x - mean) / SD")
    ax_z.set_title("After: both tests share one z scale")

    fig.suptitle("Standardisation puts different scales on one axis", fontsize=11.5, y=1.02)
    fig.tight_layout()
    save(fig, "fig-10-03-zscore.svg")


# --------------------------------------------------------------------------- M12
def fig_sampling() -> None:
    rng = np.random.default_rng(23)
    pop = rng.gamma(2.2, 18, 40000)
    fig, axes = plt.subplots(1, 3, figsize=(9.4, 3.1), sharey=False)
    axes[0].hist(pop, bins=45, color=GREY, edgecolor="white", linewidth=0.3)
    axes[0].set_title("population\nskewed, mean 39.6")
    for ax, n in zip(axes[1:], (5, 40)):
        means = rng.choice(pop, size=(4000, n)).mean(axis=1)
        ax.hist(means, bins=40, color=TEAL if n == 40 else GOLD,
                edgecolor="white", linewidth=0.3, density=True)
        ax.set_title(f"means of samples of n = {n}\nSD of means = {means.std():.1f}")
        grid = np.linspace(means.min(), means.max(), 200)
        ax.plot(grid, stats.norm.pdf(grid, means.mean(), means.std()), color=ACCENT,
                linewidth=1.8)
    for ax in axes:
        ax.set_xlabel("value")
    axes[0].set_ylabel("frequency / density")
    fig.suptitle("The sampling distribution is narrower, and more normal, than the population",
                 fontsize=11.2, y=1.03)
    fig.tight_layout()
    save(fig, "fig-12-01-sampling-distribution.svg")


# --------------------------------------------------------------------------- M13
def fig_clt() -> None:
    rng = np.random.default_rng(31)
    pops = {
        "uniform": rng.uniform(0, 10, 200000),
        "exponential": rng.exponential(3, 200000),
        "bimodal": np.concatenate([rng.normal(4, 0.8, 100000),
                                   rng.normal(8, 0.8, 100000)]),
    }
    fig, axes = plt.subplots(3, 3, figsize=(8.6, 6.4))
    for row, (name, pop) in enumerate(pops.items()):
        for col, n in enumerate((1, 5, 40)):
            ax = axes[row, col]
            means = rng.choice(pop, size=(1600, n)).mean(axis=1)
            ax.hist(means, bins=22, color=FILL, edgecolor="white", linewidth=0.25,
                    density=True)
            ax.set_title(f"{name}, n = {n}", fontsize=10)
            ax.set_yticks([])
            if col == 0:
                ax.set_ylabel("density")
    fig.suptitle("Central limit theorem: every population shape turns into a bell for the mean",
                 fontsize=11.2, y=1.00)
    fig.tight_layout()
    save(fig, "fig-13-01-clt.svg")


# --------------------------------------------------------------------------- M14
def fig_coverage() -> None:
    rng = np.random.default_rng(4)
    true_mu = 50.0
    n = 30
    reps = 100
    ses = 10 / np.sqrt(n)
    ests = rng.normal(true_mu, ses, reps)
    lo, hi = ests - 1.96 * ses, ests + 1.96 * ses
    misses = (lo > true_mu) | (hi < true_mu)
    order = np.argsort(ests)

    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    for i, idx in enumerate(order):
        colour = ACCENT if misses[idx] else TEAL
        ax.plot([lo[idx], hi[idx]], [i, i], color=colour, linewidth=1.4,
                solid_capstyle="round")
    ax.axvline(true_mu, color=INK, linestyle="--", linewidth=1.5)
    ax.plot([], [], color=INK, linestyle="--", linewidth=1.5, label="true mean μ = 50")
    ax.plot([], [], color=TEAL, linewidth=1.4, label="interval covers μ")
    ax.plot([], [], color=ACCENT, linewidth=1.4, label="interval misses μ")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_yticks([])
    ax.set_xlabel("interval for μ")
    ax.set_title(f"100 independent 95 % intervals: {misses.sum()} miss the true value")
    fig.tight_layout()
    save(fig, "fig-14-01-ci-coverage.svg")


def fig_ci_width() -> None:
    ns = np.arange(5, 205, 5)
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    for level, colour in [(0.90, GOLD), (0.95, TEAL), (0.99, ACCENT)]:
        z = stats.norm.ppf(0.5 + level / 2)
        ax.plot(ns, 2 * z * 10 / np.sqrt(ns), color=colour, linewidth=2,
                label=f"{int(level*100)} % interval")
    ax.set_xlabel("sample size n (σ = 10)")
    ax.set_ylabel("interval width")
    ax.set_title("Width falls as 1/√n — quadruple n to halve it")
    ax.annotate("n = 100\nwidth ≈ 3.9", xy=(100, 3.92), xytext=(118, 6.4),
                fontsize=9, color=GREY,
                arrowprops=dict(arrowstyle="->", color=GREY))
    ax.legend()
    fig.tight_layout()
    save(fig, "fig-14-02-ci-width.svg")


# --------------------------------------------------------------------------- M15
def fig_h0h1() -> None:
    fig, ax = plt.subplots(figsize=(7.6, 3.9))
    x = np.linspace(-4, 6, 700)
    h0 = stats.norm.pdf(x, 0, 1)
    h1 = stats.norm.pdf(x, 2.5, 1)
    crit = stats.norm.ppf(0.95)
    ax.plot(x, h0, color=TEAL, linewidth=2, label="H₀: no effect (μ = 0)")
    ax.plot(x, h1, color=ACCENT, linewidth=2, label="H₁: effect of 2.5 units")
    ax.fill_between(x, h0, where=x >= crit, color=ACCENT, alpha=0.35)
    ax.fill_between(x, h1, where=x < crit, color=TEAL, alpha=0.25)
    ax.axvline(crit, color=INK, linestyle="--", linewidth=1.4)
    ax.text(crit + 0.1, 0.25, "critical value\nz = 1.645", fontsize=9, color=INK)
    ax.annotate("α = 0.05\nfalse positive", xy=(1.95, 0.055), xytext=(3.85, 0.30),
                fontsize=9.5, color=ACCENT,
                arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax.annotate("β ≈ 0.20\nmissed effect", xy=(1.4, 0.07), xytext=(0.2, 0.28),
                fontsize=9.5, color=TEAL,
                arrowprops=dict(arrowstyle="->", color=TEAL))
    ax.set_yticks([])
    ax.set_xlabel("test statistic")
    ax.legend(loc="upper left")
    ax.set_title("Two worlds, one decision rule: α and β are areas, not opinions")
    fig.tight_layout()
    save(fig, "fig-15-01-h0-h1.svg")


# --------------------------------------------------------------------------- M16
def fig_correlation() -> None:
    rng = np.random.default_rng(53)
    specs = [(-0.9, "strong negative"), (0.0, "none"), (0.45, "moderate positive"),
             (0.95, "strong positive")]
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.8), sharex=True, sharey=True)
    base = rng.normal(0, 1, 70)
    for ax, (target, label) in zip(axes.ravel(), specs):
        noise = rng.normal(0, 1, 70)
        y = target * base + np.sqrt(max(1 - target ** 2, 1e-9)) * noise
        r = np.corrcoef(base, y)[0, 1]
        ax.scatter(base, y, s=20, color=TEAL, alpha=0.85)
        ax.set_title(f"{label}: r = {r:.2f}", fontsize=10)
    for ax in axes[1]:
        ax.set_xlabel("x")
    for ax in axes[:, 0]:
        ax.set_ylabel("y")
    fig.suptitle("Correlation measures linear association — and nothing else", fontsize=11.2, y=1.0)
    fig.tight_layout()
    save(fig, "fig-16-01-correlation.svg")


def fig_regression() -> None:
    rng = np.random.default_rng(59)
    x = rng.uniform(0, 10, 40)
    y = 3 + 1.8 * x + rng.normal(0, 2.2, 40)
    slope, intercept = np.polyfit(x, y, 1)
    grid = np.linspace(0, 10, 100)
    resid_sd = (y - (intercept + slope * x)).std(ddof=2)
    se_mean = resid_sd * np.sqrt(1 / len(x) + (grid - x.mean()) ** 2 / ((x - x.mean()) ** 2).sum())
    se_pred = resid_sd * np.sqrt(1 + 1 / len(x) + (grid - x.mean()) ** 2 / ((x - x.mean()) ** 2).sum())

    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    ax.fill_between(grid, intercept + slope * grid - 1.96 * se_pred,
                    intercept + slope * grid + 1.96 * se_pred, color=BAND,
                    label="95 % prediction interval")
    ax.fill_between(grid, intercept + slope * grid - 1.96 * se_mean,
                    intercept + slope * grid + 1.96 * se_mean, color=FILL, alpha=0.7,
                    label="95 % confidence band for the mean")
    ax.plot(grid, intercept + slope * grid, color=ACCENT, linewidth=2,
            label=f"fit: ŷ = {intercept:.2f} + {slope:.2f}x")
    ax.scatter(x, y, s=26, color=INK, zorder=3, label="observations")
    i = 5
    ax.plot([x[i], x[i]], [y[i], intercept + slope * x[i]], color=TEAL, linewidth=1.6)
    ax.annotate("residual", xy=(x[i], (y[i] + intercept + slope * x[i]) / 2),
                xytext=(x[i] + 1.15, y[i] - 3.2), fontsize=9, color=TEAL,
                arrowprops=dict(arrowstyle="->", color=TEAL))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("The line is a mean; the wide band is where a new point may fall")
    ax.legend(loc="upper left", fontsize=8.6)
    fig.tight_layout()
    save(fig, "fig-16-02-regression.svg")


# --------------------------------------------------------------------------- M17
def fig_anova() -> None:
    rng = np.random.default_rng(67)
    groups = {"method A": rng.normal(66, 5, 18),
              "method B": rng.normal(72, 5, 18),
              "method C": rng.normal(77, 5, 18)}
    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    for i, (name, vals) in enumerate(groups.items()):
        ax.scatter(np.full(len(vals), i) + rng.normal(0, 0.05, len(vals)), vals,
                   s=22, color=TEAL, alpha=0.75)
        ax.plot([i - 0.28, i + 0.28], [vals.mean()] * 2, color=ACCENT, linewidth=3)
        ax.text(i + 0.34, vals.mean() + 1.5, f"mean {vals.mean():.1f}", fontsize=9,
                color=ACCENT, va="bottom")
    grand = np.concatenate(list(groups.values())).mean()
    ax.axhline(grand, color=INK, linestyle="--", linewidth=1.2)
    ax.text(2.42, grand, "grand mean", fontsize=9, color=INK, va="bottom")
    within = np.mean([v.std(ddof=1) for v in groups.values()])
    ax.annotate("between-group spread:\nmeans differ by ~5.5 marks",
                xy=(1.5, 74), xytext=(0.35, 86), fontsize=9, color=GREY,
                arrowprops=dict(arrowstyle="->", color=GREY))
    ax.annotate(f"within-group SD ≈ {within:.1f}", xy=(0.15, 60), fontsize=9, color=GREY)
    ax.set_xticks(range(3), list(groups))
    ax.set_ylim(55, 92)
    ax.set_ylabel("exam mark")
    ax.set_title("ANOVA compares the spread of group means with the spread inside groups")
    fig.tight_layout()
    save(fig, "fig-17-01-anova.svg")


# --------------------------------------------------------------------------- M18
def fig_bayes() -> None:
    fig, ax = plt.subplots(figsize=(7.4, 3.7))
    x = np.linspace(0.001, 0.999, 600)
    prior = stats.beta.pdf(x, 2, 8)
    post = stats.beta.pdf(x, 9, 21)
    lik = stats.binom.pmf(7, 20, x)
    lik = lik / lik.max() * prior.max() * 0.9

    ax.plot(x, prior, color=GREY, linewidth=2, label="prior Beta(2, 8): mean 0.20")
    ax.plot(x, lik, color=GOLD, linewidth=1.8, linestyle="--",
            label="likelihood (scaled): 7 of 20")
    ax.plot(x, post, color=ACCENT, linewidth=2.4,
            label="posterior Beta(9, 21): mean 0.30")
    ax.fill_between(x, post, where=(x > 0.18) & (x < 0.44), color=ACCENT, alpha=0.15)
    ax.annotate("95 % credible\ninterval", xy=(0.40, 3.2), xytext=(0.50, 4.0),
                fontsize=9, color=ACCENT,
                arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax.set_xlabel("conversion rate θ")
    ax.set_ylabel("density")
    ax.set_title("Bayesian updating: the posterior is prior and evidence, combined")
    ax.legend(loc="upper right", fontsize=8.6)
    fig.tight_layout()
    save(fig, "fig-18-01-bayes.svg")


# --------------------------------------------------------------------------- M05
def fig_counting_tree() -> None:
    mains = ["burger", "chicken", "veg"]
    sides = ["fries", "salad"]
    drinks = ["water", "juice"]

    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    ax.set_xlim(0, 6.2)
    ax.set_ylim(0, 12.6)
    ax.axis("off")

    xs = [0.35, 1.55, 2.75, 3.85]
    leaf_y = 11.4
    step = 0.94
    for i, main in enumerate(mains):
        y1 = 10.2 - i * 3.9
        ax.plot([xs[0], xs[1]], [5.9, y1], color=INK, linewidth=1.2)
        ax.scatter([xs[1]], [y1], s=46, color=TEAL, zorder=3)
        ax.text(xs[1] - 0.12, y1 + 0.45, main, ha="right", fontsize=10.5,
                color=INK, fontweight="bold")
        for j, side in enumerate(sides):
            y2 = y1 + (1.05 if j == 0 else -0.55)
            ax.plot([xs[1], xs[2]], [y1, y2], color=GREY, linewidth=1.0)
            ax.scatter([xs[2]], [y2], s=34, color=GOLD, zorder=3)
            ax.text(xs[2] + 0.08, y2 + 0.20, side, fontsize=9.2, color=INK)
            for k, drink in enumerate(drinks):
                ax.plot([xs[2], xs[3]], [y2, leaf_y], color=GREY, linewidth=0.9,
                        linestyle=":")
                ax.scatter([xs[3]], [leaf_y], s=24, color=FILL, edgecolor=INK,
                           linewidth=0.6, zorder=3)
                ax.text(xs[3] + 0.12, leaf_y, f"{main} + {side} + {drink}",
                        va="center", fontsize=8.6, color=INK)
                leaf_y -= step

    ax.text(xs[0] - 0.05, 6.15, "start", fontsize=10, color=INK, fontweight="bold")
    for x, label in [(xs[1], "3 mains"), (xs[2], "× 2 sides"), (xs[3] + 0.55, "× 2 drinks")]:
        ax.text(x, 0.55, label, ha="center", fontsize=9.5, color=GREY)
    ax.text(5.05, 6.0, "multiply along\nthe branches\n\n3 × 2 × 2 = 12\n\n"
                       "each leaf is one\nreachable combo",
            fontsize=9.6, color=ACCENT, va="center")
    ax.set_title("Counting tree: 3 mains × 2 sides × 2 drinks = 12 orders", pad=8)
    fig.tight_layout()
    save(fig, "fig-05-01-counting-tree.svg")


# --------------------------------------------------------------------------- M08
def fig_pmf_pdf_cdf() -> None:
    n, p = 6, 0.4
    k = np.arange(0, n + 1)
    pmf = stats.binom.pmf(k, n, p)
    cdf = np.cumsum(pmf)

    lam = 0.8
    x = np.linspace(0, 8, 500)
    pdf = stats.expon.pdf(x, scale=1 / lam)
    cdf_c = stats.expon.cdf(x, scale=1 / lam)

    fig, axes = plt.subplots(2, 2, figsize=(8.8, 6.2))

    ax = axes[0, 0]
    ax.vlines(k, 0, pmf, color=TEAL, linewidth=2.2)
    ax.plot(k, pmf, "o", color=TEAL, markersize=5)
    ax.axvline(2, color=ACCENT, linewidth=1.2, linestyle="--")
    ax.annotate(f"P(X = 2) = {pmf[2]:.3f}", xy=(2, pmf[2]), xytext=(3.0, pmf.max() * 0.85),
                fontsize=9.5, color=ACCENT,
                arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax.set_title("PMF (discrete): height is probability")
    ax.set_xlabel("k = number of successes")
    ax.set_ylabel("P(X = k)")

    ax = axes[0, 1]
    ax.step(k, cdf, where="post", color=TEAL, linewidth=2.2)
    ax.scatter(k, cdf, s=22, color=TEAL, zorder=3)
    ax.set_ylim(0, 1.05)
    ax.set_title("CDF (discrete): heights accumulate")
    ax.set_xlabel("k")
    ax.set_ylabel("P(X ≤ k)")

    ax = axes[1, 0]
    ax.plot(x, pdf, color=TEAL, linewidth=2)
    ax.fill_between(x, pdf, where=(x >= 1) & (x <= 3), color=ACCENT, alpha=0.3)
    ax.set_title("PDF (continuous): area is probability")
    ax.set_xlabel("x")
    ax.set_ylabel("density f(x)")
    ax.annotate(f"P(1 < X ≤ 3) = {stats.expon.cdf(3, scale=1/lam) - stats.expon.cdf(1, scale=1/lam):.3f}",
                xy=(2, 0.03), xytext=(3.4, 0.45), fontsize=9.5, color=ACCENT,
                arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax.annotate("height ≈ 0.36 is a density,\nnot a probability", xy=(1.0, pdf[np.argmin(abs(x-1))]),
                xytext=(2.6, 0.72), fontsize=9, color=GREY,
                arrowprops=dict(arrowstyle="->", color=GREY))

    ax = axes[1, 1]
    ax.plot(x, cdf_c, color=TEAL, linewidth=2.2)
    ax.axhline(1, color=GREY, linewidth=1, linestyle=":")
    ax.set_ylim(0, 1.05)
    ax.set_title("CDF (continuous): a smooth rising curve")
    ax.set_xlabel("x")
    ax.set_ylabel("F(x) = P(X ≤ x)")

    fig.suptitle("Two kinds of random variable, three ways to describe them",
                 fontsize=11.5, y=1.00)
    fig.tight_layout()
    save(fig, "fig-08-01-pmf-pdf-cdf.svg")


# --------------------------------------------------------------------------- M11
def fig_bivariate() -> None:
    rho = 0.8
    sx, sy = 1.0, 1.2
    cov = [[sx ** 2, rho * sx * sy], [rho * sx * sy, sy ** 2]]
    mvn = stats.multivariate_normal(mean=[0, 0], cov=cov)

    gx = np.linspace(-3.2, 3.2, 90)
    gy = np.linspace(-3.6, 3.6, 90)
    X, Y = np.meshgrid(gx, gy)
    Z = mvn.pdf(np.dstack([X, Y]))

    fig = plt.figure(figsize=(7.6, 6.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[4, 1.1], height_ratios=[1.1, 4],
                          hspace=0.08, wspace=0.06)
    ax_top = fig.add_subplot(gs[0, 0])
    ax_main = fig.add_subplot(gs[1, 0], sharex=ax_top)
    ax_right = fig.add_subplot(gs[1, 1], sharey=ax_main)

    ax_main.contourf(X, Y, Z, levels=9, cmap="Blues", alpha=0.85)
    ax_main.contour(X, Y, Z, levels=5, colors="white", linewidths=0.7)
    ax_main.axvline(1.2, color=ACCENT, linewidth=1.6, linestyle="--")
    line_x = np.linspace(-3.2, 3.2, 50)
    ax_main.plot(line_x, rho * sy / sx * line_x, color=ACCENT, linewidth=1.8)
    cond_mean = rho * sy / sx * 1.2
    ax_main.annotate(f"conditional mean line\nE[Y | X = 1.2] = {cond_mean:.3f}",
                     xy=(1.2, cond_mean), xytext=(-2.9, 2.6), fontsize=9, color=ACCENT,
                     arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax_main.annotate("contours tilt upward:\nρ = 0.8", xy=(1.9, 1.2), xytext=(1.4, -2.9),
                     fontsize=9, color=INK,
                     arrowprops=dict(arrowstyle="->", color=INK))
    ax_main.set_xlabel("X")
    ax_main.set_ylabel("Y")

    ax_top.plot(gx, stats.norm.pdf(gx, 0, sx), color=TEAL, linewidth=2)
    ax_top.fill_between(gx, stats.norm.pdf(gx, 0, sx), color=TEAL, alpha=0.15)
    ax_top.set_title("marginal f_X: integrate out y", fontsize=9.5)
    ax_top.axis("off")

    ax_right.plot(stats.norm.pdf(gy, 0, sy), gy, color=GOLD, linewidth=2)
    ax_right.fill_betweenx(gy, stats.norm.pdf(gy, 0, sy), color=GOLD, alpha=0.15)
    ax_right.set_title("marginal f_Y", fontsize=9.5)
    ax_right.axis("off")

    fig.suptitle("One joint density, two marginals, one conditional slice",
                 fontsize=11.5, y=0.95)
    save(fig, "fig-11-01-bivariate.svg")


FIGURES = [
    fig_centre, fig_spread, fig_hist_bins, fig_boxplot,
    fig_bins_m04, fig_anscombe, fig_truncated,
    fig_binomial, fig_poisson,
    fig_families, fig_empirical, fig_zscore,
    fig_sampling, fig_clt, fig_coverage, fig_ci_width, fig_h0h1,
    fig_correlation, fig_regression, fig_anova, fig_bayes,
    fig_counting_tree, fig_pmf_pdf_cdf, fig_bivariate,
]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    if "--check" in sys.argv:
        referenced = set()
        pattern = re.compile("assets/images/figures/([A-Za-z0-9._-]+[.]svg)")
        for md in (ROOT / "docs").rglob("*.md"):
            referenced.update(pattern.findall(md.read_text(encoding="utf-8")))
        on_disk = {p.name for p in OUT.glob("*.svg")}
        missing = sorted(referenced - on_disk)
        unused = sorted(on_disk - referenced)
        print(f"{len(referenced)} figure(s) referenced, {len(on_disk)} on disk")
        if missing:
            print("missing files:", missing)
            return 1
        if unused:
            print("on disk but never referenced:", unused)
            return 1
        if len(referenced) < 20:
            print(f"WARNING: only {len(referenced)} figures referenced")
            return 1
        print("Every referenced figure exists, and every file is used.")
        return 0

    style()
    print(f"writing {len(FIGURES)} figures to {OUT.relative_to(ROOT)}/")
    for fn in FIGURES:
        fn()
    total = sum(p.stat().st_size for p in OUT.glob("*.svg"))
    print(f"\n{len(FIGURES)} figures, {total / 1024:.0f} KB total")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
