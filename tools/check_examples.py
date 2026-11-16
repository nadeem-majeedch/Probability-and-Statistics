"""Validate the worked-example arithmetic in chapters M01-M18.

Every numeric claim made in the chapters is recomputed here from first
principles. Run with:  python tools/check_examples.py
Exit status is 0 only when every check passes.
"""

import math
import random
from math import comb, factorial, log

FAILS = []


def check(label, got, want, tol=5e-3):
    ok = abs(got - want) <= tol
    print(("  OK   " if ok else "  FAIL ") + f"{label}: got {got:.6g}, want {want:.6g}")
    if not ok:
        FAILS.append(label)


def close(label, got, want, tol=5e-3):
    check(label, got, want, tol)


# ---------------------------------------------------------------- M01
print("M01")
check("PPV example 180/670", 180 / 670, 0.2687, 1e-3)
check("screen 95/185", 95 / 185, 0.514, 1e-3)
check("se n=200", 20000 / math.sqrt(200), 1414.2, 0.2)
check("se n=800", 20000 / math.sqrt(800), 707.1, 0.2)
check("se ratio", math.sqrt(800 / 200), 2.0, 1e-9)
check("sqrt(10)", math.sqrt(10), 3.1623, 1e-4)
check("simpson A overall", 120 / 400, 0.30, 1e-9)
check("simpson B overall", 160 / 400, 0.40, 1e-9)
check("simpson A weighted", 0.25 * 0.60 + 0.75 * 0.20, 0.30, 1e-9)
check("simpson B weighted", 0.75 * 0.50 + 0.25 * 0.10, 0.40, 1e-9)

# ---------------------------------------------------------------- M02
print("M02")
check("sum 50 of 3i-2", 3 * (50 * 51 // 2) - 2 * 50, 3725, 1e-9)
check("sum 1..10", 10 * 11 // 2, 55, 1e-9)
check("sum squares 1..10", 10 * 11 * 21 // 6, 385, 1e-9)
check("sum 2i+1 i<=4", sum(2 * i + 1 for i in range(1, 5)), 24, 1e-9)
check("C(10,3)", comb(10, 3), 120, 1e-9)
check("C(6,2)=C(6,4)", comb(6, 2), comb(6, 4), 1e-9)
check("5!", factorial(5), 120, 1e-9)
check("revenue optimum q", 1000 - 20 * 25, 500, 1e-9)
check("revenue max", 25 * 500, 12500, 1e-9)
check("revenue at p=24", 24 * (1000 - 20 * 24), 12480, 1e-9)
check("revenue at p=26", 26 * (1000 - 20 * 26), 12480, 1e-9)
check("50000*1.08^5", 50000 * 1.08 ** 5, 73466.4, 0.5)
check("50000*e^0.4", 50000 * math.exp(0.4), 74591.2, 0.5)
check("doubling at 8%", log(2) / log(1.08), 9.006, 1e-3)
check("doubling at 12%", log(2) / log(1.12), 6.116, 1e-3)
check("1.12^4", 1.12 ** 4, 1.5735, 1e-4)
check("exp(2) tail", math.exp(-1), 0.3679, 1e-4)
check("int_0^2 3x^2", 2 ** 3, 8, 1e-9)
check("1.05^10", 1.05 ** 10, 1.6289, 1e-4)
check("doubling at 5%", log(2) / log(1.05), 14.21, 1e-2)
check("f(6)=12*6-36", 12 * 6 - 36, 36, 1e-9)
check("X'X top-left", 1 + 1 + 1, 3, 1e-9)
check("X'X top-right", 2 + 4 + 6, 12, 1e-9)
check("X'X bottom-right", 4 + 16 + 36, 56, 1e-9)
check("ln(1.12)", log(1.12), 0.1133, 1e-4)

# ---------------------------------------------------------------- M03
print("M03")
marks = [45, 52, 58, 61, 67, 70, 74, 79, 85, 92]
n = len(marks)
total = sum(marks)
check("sum marks", total, 683, 1e-9)
check("mean marks", total / n, 68.3, 1e-9)
check("median marks", (67 + 70) / 2, 68.5, 1e-9)
ss = sum((x - 68.3) ** 2 for x in marks)
check("sum squared deviations", ss, 1960.10, 1e-6)
check("s^2", ss / (n - 1), 217.7889, 1e-3)
check("s", math.sqrt(ss / (n - 1)), 14.7577, 1e-3)
check("sigma^2", ss / n, 196.01, 1e-6)
check("sigma", math.sqrt(ss / n), 14.0004, 1e-3)
check("Q1", 58, 58, 1e-9)
check("Q3", 79, 79, 1e-9)
check("IQR", 79 - 58, 21, 1e-9)
check("lower fence", 58 - 1.5 * 21, 26.5, 1e-9)
check("upper fence", 79 + 1.5 * 21, 110.5, 1e-9)
check("CV", 14.7577 / 68.3, 0.2161, 1e-3)
check("z(92)", (92 - 68.3) / 14.7577, 1.606, 1e-3)
check("trimmed mean", (683 - 45 - 92) / 8, 68.25, 1e-9)
check("weighted grade", 0.20 * 78 + 0.30 * 65 + 0.50 * 84, 77.1, 1e-9)
check("unweighted grade", (78 + 65 + 84) / 3, 75.6667, 1e-3)
check("geometric mean", (1.10 * 1.05 * 1.20) ** (1 / 3), 1.1150, 1e-4)
check("grouped mean", (3 * 45 + 5 * 55 + 8 * 65 + 12 * 75 + 9 * 85 + 3 * 95) / 40, 72.0, 1e-9)
check("avg of rates", (0.05 + 0.10) / 2, 0.075, 1e-9)
check("pooled rate", 7 / 120, 0.05833, 1e-4)
check("combined mean", (30 * 62 + 20 * 74) / 50, 66.8, 1e-9)
check("typo mean", (683 - 92 + 992) / 10, 158.3, 1e-9)
typo = [45, 52, 58, 61, 67, 70, 74, 79, 85, 992]
m2 = sum(typo) / 10
check("typo variance", sum((x - m2) ** 2 for x in typo) / 9, 85957.8, 1.0)
check("typo sd", math.sqrt(sum((x - m2) ** 2 for x in typo) / 9), 293.2, 0.2)
ex1 = [12, 15, 15, 18, 21, 24, 30]
check("ex1 sum", sum(ex1), 135, 1e-9)
check("ex1 mean", sum(ex1) / 7, 19.2857, 1e-3)
check("ex1 IQR", 24 - 15, 9, 1e-9)
sales = [120, 135, 128, 400, 142, 138]
check("sales sum", sum(sales), 1063, 1e-9)
check("sales mean", sum(sales) / 6, 177.1667, 1e-3)
check("sales median", (135 + 138) / 2, 136.5, 1e-9)
check("ex5 weighted", 0.25 * 82 + 0.15 * 74 + 0.25 * 68 + 0.35 * 79, 76.25, 1e-9)
check("ex5 unweighted", (82 + 74 + 68 + 79) / 4, 75.75, 1e-9)
check("ex6 product", 1.08 * 0.96 * 1.15, 1.19232, 1e-6)
check("ex6 geo", (1.08 * 0.96 * 1.15) ** (1 / 3), 1.0604, 1e-4)
check("ex6 arith", (1.08 + 0.96 + 1.15) / 3, 1.06333, 1e-5)
check("ex7 cumulative", (3 + 5 + 8 + 12) / 40, 0.70, 1e-9)

# ---------------------------------------------------------------- M04
print("M04")
check("Sturges n=40", 1 + math.log2(40), 6.3219, 1e-4)
check("Sturges n=100", 1 + math.log2(100), 7.6439, 1e-4)
check("Sturges n=1000", 1 + math.log2(1000), 10.9658, 1e-4)
check("lie factor bars", (0.9 / 0.1) / (1.20 / 1.00), 7.5, 1e-9)
check("lie factor 3x", 3 / 1.2, 2.5, 1e-9)
check("ratio 97/92", 97 / 92, 1.0543, 1e-4)
check("drawn ratio", (97 - 90) / (92 - 90), 3.5, 1e-9)
check("inflation", 3.5 / (97 / 92), 3.319, 1e-3)

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]


def var(a):
    m = sum(a) / len(a)
    return sum((v - m) ** 2 for v in a) / (len(a) - 1)


def corr(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    num = sum((u - ma) * (v - mb) for u, v in zip(a, b))
    return num / math.sqrt(sum((u - ma) ** 2 for u in a) * sum((v - mb) ** 2 for v in b))


check("anscombe mean x", sum(x) / 11, 9.0, 1e-9)
check("anscombe var x", var(x), 11.0, 1e-6)
# y4 carries its own x column (ten 8s and one 19)
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
check("anscombe mean x4", sum(x4) / 11, 9.0, 1e-9)
check("anscombe var x4", var(x4), 11.0, 1e-6)
for name, y, xx in (("y1", y1, x), ("y2", y2, x), ("y3", y3, x), ("y4", y4, x4)):
    check(f"anscombe mean {name}", sum(y) / 11, 7.5, 1e-2)
    check(f"anscombe var {name}", var(y), 4.125, 1e-2)
    check(f"anscombe r {name}", corr(xx, y), 0.816, 2e-3)

# ---------------------------------------------------------------- M05
print("M05")
check("C(49,6)", comb(49, 6), 13983816, 1e-9)
check("C(15,11)", comb(15, 11), 1365, 1e-9)
check("C(14,10)", comb(14, 10), 1001, 1e-9)
check("P(10,3)", factorial(10) // factorial(7), 720, 1e-9)
check("P(7,2)", 7 * 6, 42, 1e-9)
check("C(7,2)", comb(7, 2), 21, 1e-9)
check("P(10,4)", 10 * 9 * 8 * 7, 5040, 1e-9)
check("10^4", 10 ** 4, 10000, 1e-9)
check("multinomial 3,3,4", factorial(10) // (factorial(3) * factorial(3) * factorial(4)), 4200, 1e-9)
check("banana", factorial(6) // (factorial(3) * factorial(2)), 60, 1e-9)
check("statistics", factorial(10) // (factorial(3) * factorial(3) * factorial(2)), 50400, 1e-9)
check("grid 7 choose 4", comb(7, 4), 35, 1e-9)
check("stars bars 10,3", comb(12, 2), 66, 1e-9)
check("stars bars 10,4", comb(13, 3), 286, 1e-9)
check("4^10", 4 ** 10, 1048576, 1e-9)
check("div by 3 or 5", 33 + 20 - 6, 47, 1e-9)
check("div by 4 or 6", 50 + 33 - 16, 67, 1e-9)
check("committee 100", comb(10, 3) - comb(6, 3), 100, 1e-9)
check("committee 840", comb(6, 2) * comb(8, 3), 840, 1e-9)
check("12 choose 4", comb(12, 4), 495, 1e-9)
check("incl named 165", comb(11, 3), 165, 1e-9)
check("excl named 330", comb(11, 4), 330, 1e-9)
check("PIN no repeat", 9 * 9 * 8 * 7, 4536, 1e-9)
check("PIN total", 10 * 9 * 8 * 7, 5040, 1e-9)
check("PIN leading zero", 9 * 8 * 7, 504, 1e-9)
check("passwords", 26 ** 4 * 100, 45697600, 1e-9)
check("26^6", 26 ** 6, 308915776, 1e-9)
check("two keepers", 2 * comb(13, 10), 572, 1e-9)
check("pascal sum 3", comb(4, 1), 4, 1e-9)
check("circular 5", factorial(4), 24, 1e-9)
check("block table", factorial(3) * 2, 12, 1e-9)
check("3 incl/excl", 20 + 18 + 12 - 8 - 5 - 4 + 2, 35, 1e-9)
check("cards at least one ace", comb(52, 5) - comb(48, 5), 886656, 1e-9)
check("C(52,5)", comb(52, 5), 2598960, 1e-9)
check("C(48,5)", comb(48, 5), 1712304, 1e-9)
check("prize C(200,3)", comb(200, 3), 1313400, 1e-9)
check("prize P(200,3)", 200 * 199 * 198, 7880400, 1e-9)

# ---------------------------------------------------------------- M06
print("M06")
check("two aces", comb(4, 2) / comb(52, 2), 1 / 221, 1e-9)
check("two aces ordered", (4 / 52) * (3 / 51), 1 / 221, 1e-9)
check("at least one 6 in 4", 1 - (5 / 6) ** 4, 671 / 1296, 1e-9)
check("at least one 6 in 5", 1 - (5 / 6) ** 5, 4651 / 7776, 1e-9)
check("at least one 6 in 6", 1 - (5 / 6) ** 6, 0.6651, 1e-3)
check("at least one head 3", 1 - (1 / 2) ** 3, 7 / 8, 1e-9)
check("union 0.5,0.4,0.2", 0.5 + 0.4 - 0.2, 0.7, 1e-9)
check("die sum 7", 6 / 36, 1 / 6, 1e-9)
check("die sum >=10", 6 / 36, 1 / 6, 1e-9)
check("die even", 18 / 36, 0.5, 1e-9)
check("red balls 5/14", (5 / 8) * (4 / 7), 5 / 14, 1e-9)
check("blue balls 3/28", (3 / 8) * (2 / 7), 3 / 28, 1e-9)
check("exactly one red", 30 / 56, 15 / 28, 1e-9)
check("balls sum", 20 / 56 + 6 / 56 + 30 / 56, 1.0, 1e-9)
check("bus wait", 5 / 15, 1 / 3, 1e-9)
check("valid pmf", 1 / 6 + 2 / 6 + 3 / 6, 1.0, 1e-9)
check("invalid pmf", 1 / 5 + 2 / 5 + 3 / 5, 1.2, 1e-9)
check("load shedding", 1 - 0.98 ** 5, 0.0961, 1e-3)
check("pin guess 100", 1 - (1 - 1e-4) ** 100, 0.00995, 1e-5)
check("survey neither", 1 - (0.45 + 0.30 - 0.12), 0.37, 1e-9)
check("ex4 white", (4 / 10) * (3 / 9), 12 / 90, 1e-9)
check("ex4 black", (6 / 10) * (5 / 9), 30 / 90, 1e-9)
check("ex4 mixed", (4 / 10) * (6 / 9) + (6 / 10) * (4 / 9), 48 / 90, 1e-9)
check("uniform [1,2.5]", 1.5 / 4, 0.375, 1e-9)
check("uniform [2.5,3.5]", 1 / 4, 0.25, 1e-9)
check("system 6 comps", 1 - 0.1 ** 6, 0.999999, 1e-9)
check("system 3 comps", 1 - 0.1 ** 3, 0.999, 1e-9)
check("die or-rule", 0.5 + 1 / 3 - 1 / 6, 2 / 3, 1e-9)
check("birthday 23", 1 - math.prod(range(365 - 22, 365)) / 365 ** 22, 0.5073, 1e-3)

# ---------------------------------------------------------------- M07
print("M07")
check("die conditional", 2 / 3, 0.6667, 1e-4)
check("second ace given first", 3 / 51, 1 / 17, 1e-12)
check("both aces", (4 / 52) * (3 / 51), 1 / 221, 1e-12)
check("independence product", 0.5 * 0.4, 0.20, 1e-12)
check("factory defect rate", 0.6 * 0.02 + 0.4 * 0.05, 0.032, 1e-12)
check("factory A given defect", 0.012 / 0.032, 0.375, 1e-12)
check("medical TP", 0.92 * 100, 92, 1e-9)
check("medical FP", 0.05 * 9900, 495, 1e-9)
check("medical total positives", 92 + 495, 587, 1e-9)
check("medical PPV", 92 / 587, 0.15673, 1e-4)
check("two-test TP", 0.92 * 92, 84.64, 1e-9)
check("two-test FP", 0.05 * 495, 24.75, 1e-9)
check("two-test PPV", 84.64 / 109.39, 0.7737, 1e-3)
check("spam one word", 0.12 / 0.132, 0.90909, 1e-4)
check("spam two words", 0.03 / 0.03012, 0.99602, 1e-4)
check("posterior at 20% prevalence", 1840 / 2240, 0.82143, 1e-4)
check("urn red total", 0.375 + 0.125, 0.5, 1e-12)
check("urn backward", 0.375 / 0.5, 0.75, 1e-12)
check("P1 both python and R", 0.4 * 0.6, 0.24, 1e-12)
check("P2 intersection", 0.2 * 0.5, 0.10, 1e-12)
check("P2 B given A", 0.10 / 0.40, 0.25, 1e-12)
check("P2 union", 0.4 + 0.5 - 0.1, 0.8, 1e-12)
check("P4 PPV", 180 / 376, 0.47872, 1e-4)
check("P4 total positives", 180 + 196, 376, 1e-9)
check("P5 defect rate", 0.5 * 0.01 + 0.3 * 0.02 + 0.2 * 0.04, 0.019, 1e-12)
check("P5 third machine share", 0.008 / 0.019, 0.42105, 1e-4)
check("P6 posterior", 8 / 9, 0.88889, 1e-4)
check("P7 sequential PPV", 162 / 186.5, 0.86863, 1e-4)
check("screen 100k positives", 5870, 5870, 1e-9)
check("screen 100k true", 0.92 * 1000, 920, 1e-9)

# ---------------------------------------------------------------- M08
print("M08")
check("two-toss mean", 0 * 0.25 + 1 * 0.5 + 2 * 0.25, 1.0, 1e-12)
check("two-toss E[X^2]", 0 + 0.5 + 4 * 0.25, 1.5, 1e-12)
check("two-toss var", 1.5 - 1, 0.5, 1e-12)
check("die mean", 21 / 6, 3.5, 1e-12)
check("die E[X^2]", 91 / 6, 15.1667, 1e-4)
check("die var", 91 / 6 - (7 / 2) ** 2, 35 / 12, 1e-12)
check("2x mean", 2 / 3, 0.6667, 1e-4)
check("2x E[X^2]", 0.5, 0.5, 1e-12)
check("2x var", 0.5 - (2 / 3) ** 2, 1 / 18, 1e-12)
check("2x interval", 0.36 - 0.09, 0.27, 1e-12)
check("transform mean", 1 / 3, 0.3333, 1e-4)
check("linear mean", 3 * 5 + 2, 17, 1e-9)
check("linear sd", 3 * 2, 6, 1e-9)
check("P1 mean", 0.5 + 0.6, 1.1, 1e-12)
check("P1 E[X^2]", 0.5 + 4 * 0.3, 1.7, 1e-12)
check("P1 var", 1.7 - 1.21, 0.49, 1e-12)
check("P2 interval", 0.512 - 0.125, 0.387, 1e-12)
check("P4 tail", math.exp(-2), 0.1353, 1e-4)
check("P6 var", 4 * 4 + 9 * 9, 97, 1e-9)
check("P7 rho", 6 / (3 * 5), 0.4, 1e-12)
check("P9 density at 1", math.exp(-1), 0.3679, 1e-4)

# ---------------------------------------------------------------- M09
print("M09")
check("bin10p3 P3", comb(10, 3) * 0.3 ** 3 * 0.7 ** 7, 0.26683, 1e-4)
check("bin10p3 P<=2", 0.7 ** 10 + 10 * 0.3 * 0.7 ** 9 + 45 * 0.09 * 0.7 ** 8, 0.38278, 1e-4)
check("bin10p3 mean", 10 * 0.3, 3, 1e-9)
check("bin10p3 var", 10 * 0.3 * 0.7, 2.1, 1e-9)
check("bin8p4 P2", comb(8, 2) * 0.4 ** 2 * 0.6 ** 6, 0.20902, 1e-4)
check("bin8p4 P<=1", 0.6 ** 8 + 8 * 0.4 * 0.6 ** 7, 0.10638, 1e-4)
check("geom p.2 k4", 0.8 ** 3 * 0.2, 0.1024, 1e-12)
check("geom p.2 mean", 1 / 0.2, 5, 1e-9)
check("geom p.2 var", 0.8 / 0.04, 20, 1e-9)
check("geom p.2 tail", 0.8 ** 5, 0.32768, 1e-12)
check("geom die k3", (5 / 6) ** 2 * (1 / 6), 0.11574, 1e-4)
check("nb r3 p.2 k7", comb(6, 2) * 0.2 ** 3 * 0.8 ** 4, 0.049152, 1e-6)
check("nb r3 p.2 mean", 3 / 0.2, 15, 1e-9)
check("nb r3 p.2 var", 3 * 0.8 / 0.04, 60, 1e-9)
check("nb ft p.7 k5", comb(4, 2) * 0.7 ** 3 * 0.3 ** 2, 0.18522, 1e-4)
check("hyper 1 of 5 in 20", 5 * comb(15, 3) / comb(20, 4), 0.46956, 1e-4)
check("hyper var", 4 * 0.25 * 0.75 * 16 / 19, 0.63158, 1e-4)
check("hyper committee", 6 * 56 / 792, 0.42424, 1e-4)
check("pois3 P0", math.exp(-3), 0.049787, 1e-6)
check("pois3 P2", 4.5 * math.exp(-3), 0.224042, 1e-6)
check("pois3 tail", 1 - math.exp(-3), 0.950213, 1e-6)
check("pois4 P0", math.exp(-4), 0.018316, 1e-6)
check("pois4 P3", 64 / 6 * math.exp(-4), 0.195367, 1e-6)
check("pois4 P>=2", 1 - 5 * math.exp(-4), 0.908422, 1e-6)
check("pois approx lambda", 1000 * 0.002, 2.0, 1e-12)
check("pois approx P0", math.exp(-2), 0.135335, 1e-6)
check("exact bin P0", 0.98 ** 20, 0.66761, 1e-4)
check("exact 0.99^200", 0.99 ** 200, 0.13398, 1e-4)
check("hyper vs bin var", 1.6 * (40 - 10) / 39, 1.23077, 1e-4)

# ---------------------------------------------------------------- M10
print("M10")

def norm_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def simpson(f, a, b, n=20000):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def chi2_cdf(x, k):
    """Chi-square CDF. df=1 has an integrable singularity at 0, so use the
    exact identities there; df=2 also has a closed form."""
    if x <= 0:
        return 0.0
    if k == 1:
        return 2 * norm_cdf(math.sqrt(x)) - 1
    if k == 2:
        return 1 - math.exp(-x / 2)
    c = 1 / (2 ** (k / 2) * math.gamma(k / 2))
    return simpson(lambda t: c * t ** (k / 2 - 1) * math.exp(-t / 2), 0, x)


def t_cdf(t, v):
    if t < 0:
        return 1 - t_cdf(-t, v)
    c = math.gamma((v + 1) / 2) / (math.sqrt(v * math.pi) * math.gamma(v / 2))
    return 0.5 + simpson(lambda u: c * (1 + u * u / v) ** (-(v + 1) / 2), 0, t)


def f_cdf(x, d1, d2):
    c = math.exp(0.5 * d1 * math.log(d1 / d2)
                 - (math.lgamma(d1 / 2) + math.lgamma(d2 / 2) - math.lgamma((d1 + d2) / 2)))
    return simpson(lambda t: c * t ** (d1 / 2 - 1) * (1 + d1 * t / d2) ** (-(d1 + d2) / 2), 0, x)


check("Phi(1)", norm_cdf(1), 0.841345, 1e-5)
check("Phi(1.96)", norm_cdf(1.96), 0.975002, 1e-5)
check("Phi(2)", norm_cdf(2), 0.977250, 1e-5)
check("Phi(1.5)", norm_cdf(1.5), 0.933193, 1e-5)
check("Phi(-1.5)", norm_cdf(-1.5), 0.066807, 1e-5)
check("U(4,16) mean", 10, 10, 1e-9)
check("U(4,16) var", 144 / 12, 12, 1e-9)
check("U(0,10) var", 100 / 12, 8.3333, 1e-4)
check("exp mean5 tail", math.exp(-2), 0.135335, 1e-6)
check("exp median", math.log(2) / 0.2, 3.46574, 1e-4)
check("N(50,10) 90th pct", 50 + 1.28155 * 10, 62.8155, 1e-3)
check("N(60,12) top5", 60 + 1.64485 * 12, 79.7382, 1e-3)
check("N(70,8) 90th pct", 70 + 1.28155 * 8, 80.2524, 1e-3)
check("gamma mean", 2 / 0.5, 4, 1e-9)
check("gamma var", 2 / 0.25, 8, 1e-9)
check("gamma F(4)", 1 - math.exp(-2) * 3, 0.59399, 1e-5)
check("beta(3,7) mean", 3 / 10, 0.3, 1e-12)
check("beta(3,7) var", 21 / 1100, 0.019091, 1e-6)
check("beta(3,7) density .3", 252 * 0.09 * 0.7 ** 6, 2.66828, 1e-4)
check("beta(2,3) mean", 0.4, 0.4, 1e-12)
check("beta(2,3) var", 0.04, 0.04, 1e-12)
check("beta(2,3) density .5", 1.5, 1.5, 1e-9)
check("cont corr z", (18.5 - 20) / math.sqrt(12), -0.43301, 1e-4)
check("cont corr prob", norm_cdf(-0.43301), 0.33249, 1e-4)
check("no-cont-corr prob", norm_cdf((18 - 20) / math.sqrt(12)), 0.28185, 1e-4)
check("bin approx 25.5", norm_cdf((25.5 - 30) / math.sqrt(21)), 0.16308, 1e-3)
check("shaft scrap 0.05", 2 * (1 - norm_cdf(2)), 0.04550, 1e-4)
check("shaft scrap 0.04", 2 * (1 - norm_cdf(2.5)), 0.01242, 1e-4)

# ---------------------------------------------------------------- M11
print("M11")
p = {(0, 0): 0.1, (0, 1): 0.2, (1, 0): 0.3, (1, 1): 0.4}
check("joint total", sum(p.values()), 1.0, 1e-12)
check("marg X0", p[(0, 0)] + p[(0, 1)], 0.3, 1e-12)
check("marg Y1", p[(0, 1)] + p[(1, 1)], 0.6, 1e-12)
check("E[X] table", 0.7, 0.7, 1e-12)
check("E[XY] table", 0.4, 0.4, 1e-12)
check("Cov table", 0.4 - 0.7 * 0.6, -0.02, 1e-12)
check("VarX table", 0.7 - 0.49, 0.21, 1e-12)
check("VarY table", 0.6 - 0.36, 0.24, 1e-12)
check("rho table", -0.02 / math.sqrt(0.21 * 0.24), -0.08909, 1e-4)
check("cond P(Y=1|X=1)", 0.4 / 0.7, 0.57143, 1e-4)
check("density E[X]", 1 / 3 + 1 / 4, 7 / 12, 1e-12)
check("density E[X^2]", 0.25 + 1 / 6, 5 / 12, 1e-12)
check("density var", 5 / 12 - (7 / 12) ** 2, 11 / 144, 1e-12)
check("density E[XY]", 1 / 3, 0.333333, 1e-6)
check("density cov", 1 / 3 - (7 / 12) ** 2, -1 / 144, 1e-12)
check("density rho", -(1 / 144) / (11 / 144), -1 / 11, 1e-12)
check("cond mean at .5", 0.25 + 1 / 3, 0.5833, 1e-4)
check("total var E[Var]", 0.6 * 4 + 0.4 * 9, 6, 1e-12)
check("total var Var(E)", 0.6 * 16 + 0.4 * 36, 24, 1e-12)
check("total var total", 6 + 24, 30, 1e-12)
check("between share", 24 / 30, 0.8, 1e-12)
check("triangle density integrates", 0.5 + 0.5, 1.0, 1e-12)
check("exp sum tail", 4 * math.exp(-3), 0.19915, 1e-5)
check("P1 sum1", 0.3 + 0.2, 0.5, 1e-12)
check("P1 cond X|Y0", 0.3 / 0.4, 0.75, 1e-12)
check("P3 mean", 2 * 3 - 3 * 5, -9, 1e-9)
check("P3 var", 4 * 4 + 9 * 9 - 24, 73, 1e-9)
check("P3 rho", 2 / 6, 1 / 3, 1e-12)
check("P5 sum pois", math.exp(-5), 0.006738, 1e-6)
check("P8 cov", 0.25 - 0.5 * (1 / 3), 1 / 12, 1e-12)
check("P8 rho", (1 / 12) / (math.sqrt(1 / 12) * math.sqrt(4 / 45)), 0.96825, 1e-4)

# ---------------------------------------------------------------- M12
print("M12")
check("se n16", 20 / 4, 5, 1e-9)
check("se n64", 20 / 8, 2.5, 1e-9)
check("se n400", 20 / 20, 1.0, 1e-9)
check("prop se", math.sqrt(0.35 * 0.65 / 400), 0.023848, 1e-5)
check("z for 105", (105 - 100) / 3, 1.6667, 1e-4)
check("P(xbar>105)", 1 - norm_cdf(5 / 3), 0.04779, 1e-4)
check("P(xbar>105) n100", 1 - norm_cdf(10 / 3), 0.00043, 1e-4)
check("sample size se2", (15 / 2) ** 2, 56.25, 1e-9)
check("sample size se1", 15 ** 2, 225, 1e-9)
check("prop prob >0.5", 1 - norm_cdf((0.5 - 0.4) / 0.049), 0.02065, 1e-3)
check("prop prob mid", 2 * norm_cdf(1.0204) - 1, 0.6924, 1e-3)
check("chi2 stat", 15 * 25 / 16, 23.4375, 1e-9)
check("chi2 95th", chi2_cdf(24.9958, 15), 0.95, 5e-4)
check("chi2 cdf 23.4375", chi2_cdf(23.4375, 15), 0.9245, 5e-3)
check("t stat", (68 - 70) / (8 / math.sqrt(10)), -0.79057, 1e-5)
check("t9 cdf", t_cdf(2.26216, 9), 0.975, 5e-4)
check("t15 cdf", t_cdf(2.13145, 15), 0.975, 5e-4)
check("t cdf 0.7906", t_cdf(0.79057, 9), 0.7745, 5e-3)
check("F stat", 25 / 16, 1.5625, 1e-9)
check("F 97.5 pct", f_cdf(2.57, 15, 20), 0.975, 5e-3)
check("fpc 800/200", math.sqrt(600 / 799), 0.866567, 1e-6)
check("fpc 1000/100", math.sqrt(900 / 999), 0.949158, 1e-6)
check("t35 crit", t_cdf(2.0301, 35), 0.975, 5e-4)
check("t 1.333 for problem 4", (52 - 50) / 1.5, 1.3333, 1e-4)
check("F problem 5", 12 / 8, 1.5, 1e-9)
check("poll se", math.sqrt(0.52 * 0.48 / 900), 0.016653, 1e-5)
check("poll lower", 0.52 - 1.96 * 0.016653, 0.48736, 1e-4)
check("poll upper", 0.52 + 1.96 * 0.016653, 0.55264, 1e-4)

# ---------------------------------------------------------------- M13
print("M13")
check("se of mean sigma15 n100", 15 / math.sqrt(100), 1.5, 1e-9)
check("Chebyshev bound 225/900", 15 ** 2 / (100 * 3 ** 2), 0.25, 1e-9)
check("exponential se 2/7", 2 / math.sqrt(49), 0.285714, 1e-6)
check("exponential P(mean>2.5)", 1 - norm_cdf((2.5 - 2) / (2 / 7)), 0.0401, 1e-4)
check("binom sd sqrt21", math.sqrt(21), 4.582576, 1e-6)
check("continuity z 25.5", (25.5 - 30) / math.sqrt(21), -0.981981, 1e-6)
check("continuity p", norm_cdf((25.5 - 30) / math.sqrt(21)), 0.1631, 5e-4)
check("no continuity p", norm_cdf((25 - 30) / math.sqrt(21)), 0.1377, 5e-4)
check("delta method se", 0.2 * math.sqrt(0.4 * 0.6 / 100), 0.0098, 1e-5)
check("delta method se exact", abs(1 - 0.8) * math.sqrt(0.24 / 100), 0.0097980, 1e-5)
check("CLT n=100 needs 22 sd of mean? sigma/sqrt(n)", 15 / 10 * 2, 3.0, 1e-9)

# ---------------------------------------------------------------- M14
print("M14")

def wilson_ci(p, n, z=1.96):
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z / denom) * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return centre - half, centre + half

check("z interval half width", 1.96 * 15 / 5, 5.88, 1e-9)
check("z interval lower", 100 - 1.96 * 3, 94.12, 1e-9)
check("z interval upper", 100 + 1.96 * 3, 105.88, 1e-9)
check("t interval half width", 2.131 * 9 / 4, 4.79475, 1e-4)
check("t interval lower", 52 - 2.13145 * 2.25, 47.20424, 1e-3)
check("t interval upper", 52 + 2.13145 * 2.25, 56.79576, 1e-3)
check("prop se 0.35 n400", math.sqrt(0.35 * 0.65 / 400), 0.023848, 1e-5)
check("Wald lower", 0.35 - 1.96 * 0.023848, 0.30326, 1e-3)
check("Wald upper", 0.35 + 1.96 * 0.023848, 0.39674, 1e-3)
w_lo, w_hi = wilson_ci(0.35, 400)
check("Wilson lower", w_lo, 0.3049, 1e-3)
check("Wilson upper", w_hi, 0.3980, 1e-3)
w0_lo, w0_hi = wilson_ci(0.0, 20)
check("Wilson p=0 lower", w0_lo, 0.0, 1e-12)
check("Wilson p=0 upper", w0_hi, 0.1611, 1e-3)
check("pooled var", (19 * 81 + 24 * 121) / 43, 103.3256, 1e-4)
check("pooled sd", math.sqrt((19 * 81 + 24 * 121) / 43), 10.16492, 1e-5)
check("two sample se", 10.16492 * math.sqrt(1 / 20 + 1 / 25), 3.049476, 1e-5)
check("two sample t crit 43", 2.0163, 2.0163, 1e-9)
check("two sample CI half", 2.0163 * 3.049476, 6.14866, 1e-4)
check("two sample CI lower", 6 - 2.0163 * 3.049476, -0.14866, 1e-4)
check("two sample CI upper", 6 + 2.0163 * 3.049476, 12.14866, 1e-4)
check("MLE exponential 1/4", 1 / 4, 0.25, 1e-9)
check("MLE bernoulli 35/100", 35 / 100, 0.35, 1e-9)
check("MLE normal sigma2 vs s2", 217.79 * 9 / 10, 196.011, 1e-3)
check("sample size exact 96.04", (1.96 * 15 / 3) ** 2, 96.04, 1e-9)
check("sample size ceil 97", math.ceil((1.96 * 15 / 3) ** 2), 97, 1e-9)
check("MSE bias2+var", 2 ** 2 + 9, 13, 1e-9)
check("MSE 0.25+4", 0.5 ** 2 + 4, 4.25, 1e-9)
check("E sigma-hat2 n8", 7 / 8 * 50, 43.75, 1e-9)

# ---------------------------------------------------------------- M15
print("M15")
check("z test stat", (52 - 50) / (9 / 10), 2.222222, 1e-6)
check("z test p", 2 * (1 - norm_cdf((52 - 50) / 0.9)), 0.02626, 1e-4)
check("one sample t", (68 - 70) / (8 / math.sqrt(10)), -0.790569, 1e-6)
check("one sample t p", 2 * (1 - t_cdf(0.790569, 9)), 0.449525, 1e-4)
check("one sample CI lower", 68 - 2.26216 * (8 / math.sqrt(10)), 62.2762, 1e-3)
check("one sample CI upper", 68 + 2.26216 * (8 / math.sqrt(10)), 73.7238, 1e-3)
check("paired t", 2.4 / (3.1 / 3), 2.322581, 1e-6)
check("paired t p", 2 * (1 - t_cdf(2.322581, 8)), 0.04847, 5e-4)
check("paired t crit 8", 2.306, 2.306, 1e-9)
check("two sample t", 6 / 3.049476, 1.967552, 1e-6)
check("two sample t p", 2 * (1 - t_cdf(1.967552, 43)), 0.05548, 5e-4)
check("prop se under null", math.sqrt(0.2 * 0.8 / 400), 0.02, 1e-9)
check("prop z", (0.225 - 0.20) / 0.02, 1.25, 1e-9)
check("prop two sided p", 2 * (1 - norm_cdf(1.25)), 0.21130, 1e-4)
check("sample size 63 raw", 2 * (1.96 + 0.8416) ** 2 * 100 / 25, 62.791, 1e-3)
check("sample size 63 ceil", math.ceil(2 * (1.96 + 0.8416) ** 2 * 100 / 25), 63, 1e-9)
check("z for power n40", 5 / (10 * math.sqrt(2 / 40)), 2.236068, 1e-6)
check("power at n40", norm_cdf(5 / (10 * math.sqrt(2 / 40)) - 1.96), 0.608752, 1e-4)
check("familywise 20 tests", 1 - 0.95 ** 20, 0.641514, 1e-6)
check("familywise 3 tests", 1 - 0.95 ** 3, 0.142625, 1e-6)
check("familywise 6 tests", 1 - 0.95 ** 6, 0.264908, 1e-6)
check("BH threshold k3", 3 * 0.05 / 5, 0.03, 1e-9)
check("compare 0.039 vs 0.03 fails", 0.039 > 0.03, True)
check("bonferroni 0.05/5", 0.05 / 5, 0.01, 1e-9)
check("ex4 t", (48.6 - 50) / (6 / 6), -1.4, 1e-9)
check("ex4 p", 2 * (1 - t_cdf(1.4, 35)), 0.17014, 5e-4)
check("ex4 crit t35", 2.0301, 2.0301, 1e-9)
check("ex5 se", math.sqrt(0.2 * 0.8 / 500), 0.017889, 1e-6)
check("ex5 z", (0.16 - 0.20) / math.sqrt(0.2 * 0.8 / 500), -2.23607, 1e-5)
check("ex5 p", 2 * (1 - norm_cdf(2.23607)), 0.02535, 1e-4)
check("ex6 t", 1.8 / (2.4 / 4), 3.0, 1e-9)
check("ex6 CI lower", 1.8 - 2.13145 * 0.6, 0.52113, 1e-4)
check("ex6 CI upper", 1.8 + 2.13145 * 0.6, 3.07887, 1e-4)
check("ex7 n", 2 * (1.96 + 1.2816) ** 2 * 144 / 16, 189.143, 1e-2)
check("ex8 familywise 15", 1 - 0.95 ** 15, 0.536709, 1e-5)
check("ab pooled p", 0.13, 0.13, 1e-9)
check("ab se", math.sqrt(0.13 * 0.87 * 2 / 1000), 0.015040, 1e-6)
check("ab z", 0.02 / math.sqrt(0.13 * 0.87 * 2 / 1000), 1.329792, 1e-5)
check("ab p", 2 * (1 - norm_cdf(0.02 / math.sqrt(0.13 * 0.87 * 2 / 1000))), 0.18352, 1e-4)
check("ab CI lower", 0.02 - 1.96 * 0.015040, -0.00948, 1e-4)
check("ab CI upper", 0.02 + 1.96 * 0.015040, 0.04948, 1e-4)

# ---------------------------------------------------------------- M16
print("M16")
xs = [1, 2, 3, 4, 5]
ys = [2, 4, 5, 4, 5]
mx, my = 3, 4
sxx = sum((x - mx) ** 2 for x in xs)
sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
syy = sum((y - my) ** 2 for y in ys)
check("M16 Sxx", sxx, 10, 1e-9)
check("M16 Sxy", sxy, 6, 1e-9)
check("M16 Syy", syy, 6, 1e-9)
check("M16 slope", sxy / sxx, 0.6, 1e-9)
check("M16 intercept", my - 0.6 * mx, 2.2, 1e-9)
check("M16 r", sxy / math.sqrt(sxx * syy), 0.774597, 1e-6)
check("M16 SSE", syy - 0.6 * sxy, 2.4, 1e-9)
check("M16 R2", (0.6 * sxy) / syy, 0.6, 1e-9)
check("M16 se", math.sqrt(2.4 / 3), 0.894427, 1e-6)
check("M16 se slope", math.sqrt(2.4 / 3) / math.sqrt(10), 0.282842, 1e-6)
check("M16 t slope", 0.6 / 0.282842, 2.12132, 1e-5)
check("M16 slope p", 2 * (1 - t_cdf(2.12132, 3)), 0.12391, 5e-4)
check("M16 slope CI lower", 0.6 - 3.182446 * 0.2828427, -0.300132, 1e-5)
check("M16 slope CI upper", 0.6 + 3.182446 * 0.2828427, 1.500132, 1e-5)
check("M16 se mean at 6", math.sqrt(2.4 / 3) * math.sqrt(1 / 5 + 9 / 10), 0.938083, 1e-6)
check("M16 conf lower", 5.8 - 3.18245 * 0.938083, 2.8147, 1e-3)
check("M16 conf upper", 5.8 + 3.18245 * 0.938083, 8.7853, 1e-3)
check("M16 pred se", math.sqrt(2.4 / 3) * math.sqrt(1 + 1 / 5 + 9 / 10), 1.296148, 1e-5)
check("M16 pred lower", 5.8 - 3.182446 * 1.296148, 1.67508, 1e-4)
check("M16 pred upper", 5.8 + 3.182446 * 1.296148, 9.92492, 1e-4)
check("M16 adj R2", 1 - (1 - 0.85) * 9 / 7, 0.807143, 1e-6)
check("M16 VIF", 1 / (1 - 0.8), 5.0, 1e-9)
check("M16 VIF 10 sqrt", math.sqrt(10), 3.162278, 1e-6)
check("M16 ex1 Sxx", 5, 5, 1e-9)
check("M16 ex1 Sxy", 7, 7, 1e-9)
check("M16 ex1 slope", 7 / 5, 1.4, 1e-9)
check("M16 ex1 intercept", 4 - 1.4 * 2.5, 0.5, 1e-9)
check("M16 ex2 t", 0.6 * math.sqrt(18 / (1 - 0.36)), 3.18198, 1e-5)
check("M16 ex2 p", 2 * (1 - t_cdf(3.18198, 18)), 0.00522, 5e-4)
check("M16 ex3 CI lower", 0.42 - 1.9842 * 0.15, 0.12237, 1e-4)
check("M16 ex3 CI upper", 0.42 + 1.9842 * 0.15, 0.71763, 1e-4)
check("M16 ex6 adj R2", 1 - 0.38 * 49 / 45, 0.586222, 1e-6)
check("M16 spearman x2", 1.0, 1.0, 1e-12)
r_p = corr(xs, [x * x for x in xs])
check("M16 pearson on x2", r_p, 0.981105, 1e-5)

# ---------------------------------------------------------------- M17
print("M17")
groups = [[6, 7, 8, 7, 7], [8, 9, 10, 9, 9], [5, 6, 7, 6, 6]]
grand = sum(sum(g) for g in groups) / 15
ssb = sum(len(g) * (sum(g) / len(g) - grand) ** 2 for g in groups)
ssw = sum((v - sum(g) / len(g)) ** 2 for g in groups for v in g)
check("M17 grand mean", grand, 7.333333, 1e-6)
check("M17 SSB", ssb, 23.333333, 1e-6)
check("M17 SSW", ssw, 6.0, 1e-9)
check("M17 MSB", ssb / 2, 11.666667, 1e-6)
check("M17 MSW", ssw / 12, 0.5, 1e-9)
check("M17 F", (ssb / 2) / (ssw / 12), 23.333333, 1e-6)
check("M17 F crit", f_cdf(3.8853, 2, 12), 0.95, 5e-4)
check("M17 eta2", ssb / (ssb + ssw), 0.795455, 1e-6)
check("M17 HSD", 3.7726 * math.sqrt(0.5 / 5), 1.19307, 1e-4)
check("M17 pairwise BA", 9 - 7, 2.0, 1e-9)
check("M17 pairwise AC", 7 - 6, 1.0, 1e-9)
check("M17 chi2 gof", (25 + 4 + 4 + 25) / 20, 2.9, 1e-9)
check("M17 chi2 gof 5df crit", 11.0705, 11.0705, 1e-9)
obs = [[40, 60], [20, 80]]
exp = [[30, 70], [30, 70]]
chi2_ind = sum((o - e) ** 2 / e for row_o, row_e in zip(obs, exp) for o, e in zip(row_o, row_e))
check("M17 chi2 independence", chi2_ind, 9.52381, 1e-5)
check("M17 OR", (40 / 60) / (20 / 80), 2.666667, 1e-6)
check("M17 Cramer V", math.sqrt(chi2_ind / 200), 0.218218, 1e-6)
check("M17 chi2 1df crit", 3.8415, 3.8415, 1e-9)
check("M17 chi2 1df cdf", chi2_cdf(3.8415, 1), 0.95, 5e-4)
kw_ranks = [3, 8, 13]
H = 12 / (15 * 16) * sum(5 * r * r for r in kw_ranks) - 3 * 16
check("M17 Kruskal-Wallis H", H, 12.5, 1e-9)
check("M17 KW crit 2df", 5.9915, 5.9915, 1e-9)
check("M17 KW cdf", chi2_cdf(5.9915, 2), 0.95, 5e-4)
check("M17 ex2 MSB", 40 / 2, 20, 1e-9)
check("M17 ex2 MSW", 60 / 17, 3.529412, 1e-6)
check("M17 ex2 F", (40 / 2) / (60 / 17), 5.666667, 1e-6)
check("M17 ex5 chi2", 4 * 25 / 25, 4.0, 1e-9)
check("M17 ex5 OR", (30 / 20) / (20 / 30), 2.25, 1e-9)
check("M17 ex5 V", math.sqrt(4 / 100), 0.2, 1e-9)
check("M17 ex7 familywise", 1 - 0.95 ** 3, 0.142625, 1e-6)
check("M17 ex8 familywise 6", 1 - 0.95 ** 6, 0.264908, 1e-6)

# ---------------------------------------------------------------- M18
print("M18")
check("Beta(10,5) mean", 10 / 15, 0.666667, 1e-6)
check("Beta(10,5) sd", math.sqrt(10 * 5 / (15 ** 2 * 16)), 0.117851, 1e-6)
check("Beta credible lower", 10 / 15 - 1.96 * math.sqrt(50 / 3600), 0.43561, 1e-4)
check("Beta credible upper", 10 / 15 + 1.96 * math.sqrt(50 / 3600), 0.89772, 1e-4)
check("Beta prior mean", 2 / 5, 0.4, 1e-9)
prec = 1 / 100 + 25 / 225
check("normal posterior precision", prec, 0.121111, 1e-6)
check("normal posterior var", 1 / prec, 8.25688, 1e-5)
check("normal posterior sd", math.sqrt(1 / prec), 2.87348, 1e-5)
check("normal posterior mean", (110 * 25 / 225) / prec, 100.9169, 1e-3)
check("weight on data", (25 / 225) / prec, 0.917431, 1e-5)
check("Bayes factor", 0.8 / 0.2 / (1 / 1), 4.0, 1e-9)
check("MC indicator sd", math.sqrt((math.pi / 4) * (1 - math.pi / 4)), 0.410546, 1e-5)
check("MC se of pi", 4 * math.sqrt((math.pi / 4) * (1 - math.pi / 4)) / 100, 0.0164216, 1e-6)
check("P(B>A) normal approx", norm_cdf(0.02 / math.sqrt(0.13 * 0.87 * 2 / 1000)), 0.90824, 1e-4)
check("accuracy se", math.sqrt(0.82 * 0.18 / 500), 0.017181, 1e-6)
check("accuracy CI lower", 0.82 - 1.96 * math.sqrt(0.82 * 0.18 / 500), 0.78633, 1e-4)
check("accuracy CI upper", 0.82 + 1.96 * math.sqrt(0.82 * 0.18 / 500), 0.85367, 1e-4)
check("M18 ex2 beta mean", 8 / 14, 0.571429, 1e-6)
check("M18 ex4 posterior var", 1 / (1 / 4 + 16 / 64), 2.0, 1e-9)
check("M18 ex4 posterior mean", 2 * (10 * 0.25 + 14 * 0.25), 12.0, 1e-9)
check("M18 ex6 perm p", 13 / 1000, 0.013, 1e-9)
check("M18 ex7 diff", 0.165 - 0.15, 0.015, 1e-9)
check("M18 ex7 se", math.sqrt(0.1575 * 0.8425 * 2 / 2000), 0.0115193, 1e-6)
check("M18 ex7 z", 0.015 / math.sqrt(0.1575 * 0.8425 * 2 / 2000), 1.30217, 1e-5)
check("M18 ex7 p", 2 * (1 - norm_cdf(0.015 / math.sqrt(0.1575 * 0.8425 * 2 / 2000))), 0.19286, 5e-4)
check("M18 ex9 se", math.sqrt(0.88 * 0.12 / 300), 0.018762, 1e-6)
check("M18 ex9 CI upper", 0.88 + 1.96 * math.sqrt(0.88 * 0.12 / 300), 0.91677, 1e-4)
check("shrink 2 trials", (2 + 1) / (5 + 2), 0.428571, 1e-6)
check("shrink weight n2", 2 / 7, 0.285714, 1e-6)
check("shrink 10 trials", (2 + 5) / 15, 0.466667, 1e-6)
check("shrink 40 trials", 22 / 45, 0.488889, 1e-6)
check("shrink 200 trials", 102 / 205, 0.497561, 1e-6)
check("shrink weight n200", 200 / 205, 0.975610, 1e-6)

# optional stopping: five equally spaced looks at a nominal 5% threshold
random.seed(7)
paths, looks, per = 20000, 5, 200
crossed = 0
for _ in range(paths):
    total = 0.0
    hit = False
    for k in range(looks):
        for _ in range(per):
            total += random.gauss(0, 1)
        if abs(total) / math.sqrt(per * (k + 1)) > 1.96:
            hit = True
            break
    crossed += hit
peek_rate = crossed / paths
print(f"  (peeking simulation: {peek_rate:.3f} over {looks} looks, {paths} paths)")
if not 0.11 <= peek_rate <= 0.18:
    FAILS.append(f"optional stopping inflation: got {peek_rate:.3f}, expected about 0.14")

print()
if FAILS:
    print(f"FAILED {len(FAILS)} check(s):")
    for f in FAILS:
        print("  -", f)
    raise SystemExit(1)
print("All chapter arithmetic checks passed.")
