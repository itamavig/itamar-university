"""Heat-conduction analysis, parts a and b: error budget, sigma, ODR fits, kappa.

Fit code is copied unchanged from the course Colab template (../colab/LabA_data_processing.ipynb).
Rounding helpers are copied from ../../freefall/analysis/analysis.py (checked there against
the booklet's Table 3 by test_rounding.py, copied alongside).

Outputs (paths relative to this file):
  ../report/figures/b_fit.pdf, b_res.pdf  -- part b fit on the last row + residuals
  ../report/numbers.tex                   -- one \\newcommand per reported value, already rounded
  ../colab/partb_fits.xlsx                -- the three part-b fit inputs, one sheet each, for the Colab cross-check
  results.json                            -- unrounded values
Part c: three rate fits on sensor 4 (11), P_avg (5) with error (12), corrected kappa.
  ../report/figures/c_{cool,heat,exp}_{fit,res}.pdf, ../colab/partc_fits.xlsx
"""
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from scipy.odr import Model, ODR, RealData

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
XLSX_A = ROOT / "heat conduction part a.xlsx"
XLSX_B = ROOT / "heat conduction part b.xlsx"
REPORT = ROOT / "report"
FIGURES = REPORT / "figures"
COLAB = ROOT / "colab"

G = 981.0            # cm/s^2, from the literature (user, 2026-11-05)
G_ERR = 0.0          # no error on g in this experiment (Tamir, 2026-11-10); was 10
MU0M = 0.65          # T, theory background
F2 = 1.75            # f(2), theory background
X_MM = np.array([15, 40, 65, 90, 115, 140, 165, 190], dtype=float)  # sensor positions, figure 2
X_ERR_MM = 2.0       # instructor via lab notes; the final error, not a resolution (Tamir, 2026-11-09)
T_ERR = 0.002        # K, instructor via lab notes
T_LOG_RES = 0.01     # degC, recording-software resolution (equipment list)
STEP_ROWS = 20       # 100 s at 5 s per row: stability fits 100 s and 200 s before the last row
XLSX_C = ROOT / "heat conduction part c.xlsx"
SENSOR_C = 4         # part c: one sensor from the middle of the tube (Tamir); sensor 4 at 90 mm is closest to 100 mm
SWITCH_ROW = 180     # part c: first heating row (Excel row 182, sensor 1 first rises; report-rules §6 q15)
HEAT_WIN_MIN = (3, 12)   # heating window, minutes after switch-on (user, 2026-11-14)
EXP_WIN_S = 200      # T_exp: last 200 s of part b
T_RES_S = 0.001      # logger time resolution [s] -> D(28)
T_ROOM, T_ROOM_ERR = 297.15, 1.0   # K: room temperature 24 C ± 1 K (instructor, lab notes), for (11)
L_THEO = 2.44e-8      # V^2/K^2, theory background (1)
P_FLOOR_LOG10 = -100  # p-values below 10^-100 are printed as a bound, not a number (user, 2026-11-14)


# ---------- part a: measurements and error budget ----------

def part_a_sheet():
    """The part-a sheet stacks small tables: a title row, a header row, then rows of
    (no., value, resolution). Returns {title: (values, resolution)}."""
    raw = pd.read_excel(XLSX_A, header=None)
    tables, title = {}, None
    for _, r in raw.iterrows():
        c0 = r.iloc[0]
        if isinstance(c0, str) and c0 != "no.":
            title = c0
            tables[title] = ([], None)
        elif isinstance(c0, (int, float)) and not pd.isna(c0) and title:
            vals, _ = tables[title]
            vals.append(float(r.iloc[1]))
            tables[title] = (vals, float(r.iloc[2]))
    return tables


def combined(values, res):
    """Mean, statistical error D(32)+(34), resolution error D(28), combined D(35)."""
    x = np.asarray(values, dtype=float)
    n = len(x)
    stat = x.std(ddof=1) / np.sqrt(n) if n > 1 else 0.0
    r = res / np.sqrt(12)
    return {"mean": float(x.mean()), "stat": float(stat), "res": float(r),
            "err": float(np.hypot(stat, r)), "n": n}


def part_a():
    t = part_a_sheet()
    m = combined(*t["magnet mass (m)"])
    tf = combined(*t["fall time (t)"])
    d = combined(*t["magnet height (d)"])
    dch = combined(*t["tube radius (a)"])        # the sheet's title; the values are diameters (lab notes)
    D = combined(*t["tube diameter"])
    L_vals, L_res = t["tube length"]
    L0 = {"mean": L_vals[0], "res": L_res / np.sqrt(12), "err": L_res / np.sqrt(12)}  # one reading: D(28) only
    V_vals, V_res = t["voltage"]
    I_vals, I_res = t["current (I)"]
    V = {"mean": V_vals[0], "err": V_res / np.sqrt(12)}
    I = {"mean": I_vals[0], "err": I_res / np.sqrt(12)}

    a, da = dch["mean"] / 2, dch["err"] / 2
    r, dr = d["mean"] / 2, d["err"] / 2
    w = (D["mean"] - dch["mean"]) / 2
    dw = 0.5 * np.hypot(D["err"], dch["err"])     # report (6)

    # Formula (2) in SI.
    sigma = (8 * (m["mean"] * 1e-3) * (G * 1e-2) * (a * 1e-3) ** 2 * tf["mean"]
             / (MU0M ** 2 * np.pi * (r * 1e-3) ** 4 * (L0["mean"] * 1e-2) * (w * 1e-3) * F2))
    # Report (7): sigma written in the directly measured D_ch and D (a = D_ch/2, w = (D - D_ch)/2),
    # since a and w share D_ch -- the form Tamir chose (2026-11-15). sigma ~ a^2 / w, so
    # d ln(sigma)/d D_ch = 2/D_ch + 1/(D - D_ch) and d ln(sigma)/d D = -1/(D - D_ch).
    Dc, DD = dch["mean"], D["mean"]
    terms = {"m": m["err"] / m["mean"], "g": G_ERR / G, "t": tf["err"] / tf["mean"],
             "r": 4 * dr / r, "L": L0["err"] / L0["mean"],
             "Dch": (2 / Dc + 1 / (DD - Dc)) * dch["err"], "D": D["err"] / (DD - Dc)}
    rel = float(np.sqrt(sum(v ** 2 for v in terms.values())))
    # numerical check of the two partial derivatives against formula (2) itself
    s_of = lambda dc_, D_: (dc_ / 2) ** 2 / ((D_ - dc_) / 2)
    h = 1e-6
    for k, num in (("Dch", (np.log(s_of(Dc + h, DD)) - np.log(s_of(Dc - h, DD))) / (2 * h) * dch["err"]),
                   ("D", (np.log(s_of(Dc, DD + h)) - np.log(s_of(Dc, DD - h))) / (2 * h) * D["err"])):
        assert abs(abs(num) - terms[k]) / terms[k] < 1e-6, (k, num, terms[k])
    return {"m": m, "t": tf, "d": d, "Dch": dch, "D": D, "L0": L0, "V": V, "I": I,
            "a": a, "da": da, "r": r, "dr": dr, "w": w, "dw": dw,
            "sigma": float(sigma), "sigma_err": float(sigma * rel), "sigma_rel_terms": terms}


# ---------- fit code copied from the Colab template ----------

def linear(A, x):
    return A[1] * x + A[0]


def odr_fit(fit_func, initial_guesses, x, delta_x, y, delta_y):
    model = Model(fit_func)
    odr_data = RealData(x, y, sx=delta_x, sy=delta_y)
    odr = ODR(data=odr_data, model=model, beta0=initial_guesses)
    output = odr.run()

    fit_params = output.beta
    fit_params_error = output.sd_beta
    fit_cov = output.cov_beta
    return fit_params, fit_params_error, fit_cov, output


def calc_stats(fit_func, x, y, fit_params, output):
    residuals = y - fit_func(fit_params, x)
    degrees_of_freedom = len(x) - len(fit_params)
    chi2 = output.sum_square
    chi2_red = chi2/degrees_of_freedom
    p_val = stats.chi2.sf(chi2, degrees_of_freedom)
    return residuals, degrees_of_freedom, chi2_red, p_val


# ---------- part b ----------

def part_b_rows():
    df = pd.read_excel(XLSX_B)
    t = (df["Time"] - df["Time"].iloc[0]).dt.total_seconds().to_numpy()
    T = df[[f"Sensor {i}" for i in range(1, 9)]].to_numpy(dtype=float)
    return t, T


def fit_row(T_row):
    x = X_MM * 1e-3                         # m
    dx = np.full_like(x, X_ERR_MM * 1e-3)
    dy = np.full_like(T_row, T_ERR)
    params, errors, _, output = odr_fit(linear, (T_row[0], -30.0), x, dx, T_row, dy)
    residuals, dof, chi2_red, p_val = calc_stats(linear, x, T_row, params, output)
    return {"params": params.tolist(), "errors": errors.tolist(), "chi2_red": float(chi2_red),
            "p": float(p_val), "dof": int(dof), "residuals": np.asarray(residuals).tolist(),
            "x": x.tolist(), "dx": dx.tolist(), "y": T_row.tolist(), "dy": dy.tolist()}


def kappa_from_fit(fit, A_):
    a1, da1 = fit["params"][1], fit["errors"][1]
    P = A_["V"]["mean"] * A_["I"]["mean"]
    # solid rod, same outer diameter D as part a's tube (Tamir, 2026-11-15)
    D, dD = A_["D"]["mean"] * 1e-3, A_["D"]["err"] * 1e-3
    area = np.pi / 4 * D ** 2
    kappa = -P / (area * a1)                                     # report (9)
    rel = np.sqrt((A_["V"]["err"] / A_["V"]["mean"]) ** 2 + (A_["I"]["err"] / A_["I"]["mean"]) ** 2
                  + (da1 / a1) ** 2 + (2 * dD / D) ** 2)  # report (10)
    return {"P": float(P), "A": float(area), "kappa": float(kappa), "kappa_err": float(kappa * rel)}


def part_b(A_):
    t, T = part_b_rows()
    idx = [len(t) - 1, len(t) - 1 - STEP_ROWS, len(t) - 1 - 2 * STEP_ROWS]
    fits = []
    for i in idx:
        f = fit_row(T[i])
        f["time"] = float(t[i])
        f.update(kappa_from_fit(f, A_))
        fits.append(f)
    # Stability check: N_sigma between each pair of slopes, D(51).
    pairs = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        s1, e1 = fits[i]["params"][1], fits[i]["errors"][1]
        s2, e2 = fits[j]["params"][1], fits[j]["errors"][1]
        pairs[f"{i}{j}"] = float(abs(s1 - s2) / np.hypot(e1, e2))
    room = T[0] - T[0].mean()      # first reading: all sensors at room temperature (sensor 1 rises from row 2)
    return {"fits": fits, "nsigma_slopes": pairs, "room_offsets": room.tolist()}


# ---------- part c ----------

def rows_t_T(path):
    df = pd.read_excel(path)
    t = (df["Time"] - df["Time"].iloc[0]).dt.total_seconds().to_numpy()
    T = df[[f"Sensor {i}" for i in range(1, 9)]].to_numpy(dtype=float)
    return t, T


def fit_rate(t, T, name):
    """Report (11): T = b1 t + b0 on one window; the rate is b1 [K/s]."""
    dx = np.full_like(t, T_RES_S / np.sqrt(12))      # D(28)
    dy = np.full_like(T, T_ERR)
    guess = tuple(np.polyfit(t, T, 1)[::-1])
    params, errors, _, output = odr_fit(linear, guess, t, dx, T, dy)
    residuals, dof, chi2_red, p_val = calc_stats(linear, t, T, params, output)
    return {"name": name, "params": params.tolist(), "errors": errors.tolist(), "chi2_red": float(chi2_red),
            "p": float(p_val), "dof": int(dof), "residuals": np.asarray(residuals).tolist(),
            "x": t.tolist(), "dx": dx.tolist(), "y": T.tolist(), "dy": dy.tolist(), "n": int(len(t))}


def p_avg(P_in, e, c, h):
    """Report (5)."""
    return (1 - 0.5 * (e - c) / (h - c)) * P_in


def p_avg_err(P_in, P, rel_VI, e, de, c, dc, h, dh):
    """Report (12), D(43) with P_in = VI substituted."""
    d = h - c
    return float(np.sqrt(P ** 2 * rel_VI ** 2
                         + (P_in / (2 * d)) ** 2 * (de ** 2 + ((h - e) / d * dc) ** 2 + ((e - c) / d * dh) ** 2)))


def part_c(A_, B):
    s = SENSOR_C - 1
    tc, Tc = rows_t_T(XLSX_C)
    t0 = tc[SWITCH_ROW]
    cool = fit_rate(tc[:SWITCH_ROW], Tc[:SWITCH_ROW, s], "cool")
    m = (tc >= t0 + 60 * HEAT_WIN_MIN[0]) & (tc <= t0 + 60 * HEAT_WIN_MIN[1])
    heat = fit_rate(tc[m], Tc[m, s], "heat")
    tb, Tb = rows_t_T(XLSX_B)
    mb = tb >= tb[-1] - EXP_WIN_S
    exp = fit_rate(tb[mb], Tb[mb, s], "exp")
    e, de = exp["params"][1], exp["errors"][1]
    c, dc = cool["params"][1], cool["errors"][1]
    h, dh = heat["params"][1], heat["errors"][1]
    V, I = A_["V"], A_["I"]
    P_in = V["mean"] * I["mean"]
    rel_VI = float(np.hypot(V["err"] / V["mean"], I["err"] / I["mean"]))
    P = p_avg(P_in, e, c, h)
    dP = p_avg_err(P_in, P, rel_VI, e, de, c, dc, h, dh)
    # (12) against a numerical D(43) on (5): the partial derivatives must agree.
    eps = 1e-9
    num = [(p_avg(P_in, e + eps, c, h) - p_avg(P_in, e - eps, c, h)) / (2 * eps) * de,
           (p_avg(P_in, e, c + eps, h) - p_avg(P_in, e, c - eps, h)) / (2 * eps) * dc,
           (p_avg(P_in, e, c, h + eps) - p_avg(P_in, e, c, h - eps)) / (2 * eps) * dh]
    dP_num = float(np.sqrt((P * rel_VI) ** 2 + sum(v ** 2 for v in num)))
    assert abs(dP - dP_num) / dP < 1e-5, (dP, dP_num)
    # Corrected kappa: (9) with P_avg; its error is report (15) = (10) with (dP_avg/P_avg)^2 for the V and I terms.
    # The corrected L error, report (16), comes from lorenz() with this kappa error.
    last = B["fits"][0]
    a1, da1 = last["params"][1], last["errors"][1]
    # solid rod, same outer diameter D as part a's tube (Tamir, 2026-11-15)
    D, dD = A_["D"]["mean"] * 1e-3, A_["D"]["err"] * 1e-3
    area = np.pi / 4 * D ** 2
    kappa = -P / (area * a1)
    rel = np.sqrt((dP / P) ** 2 + (da1 / a1) ** 2 + (2 * dD / D) ** 2)
    # Discussion: sensor-4 heating rate in the first and last minute of the heating window [K/min].
    mins = []
    for m0 in (HEAT_WIN_MIN[0], HEAT_WIN_MIN[1] - 1):
        mm = (tc >= t0 + 60 * m0) & (tc < t0 + 60 * (m0 + 1))
        mins.append(float(np.polyfit(tc[mm], Tc[mm, s], 1)[0] * 60))
    return {"heat_minute_rates": mins, "cool": cool, "heat": heat, "exp": exp, "P_in": float(P_in), "P_avg": float(P),
            "P_avg_err": dP, "kappa": float(kappa), "kappa_err": float(kappa * rel)}


# ---------- figures ----------

def plot_fit(res, path, title):
    x, dx = np.array(res["x"]) * 1e3, np.array(res["dx"]) * 1e3
    y, dy = np.array(res["y"]), np.array(res["dy"])
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    xf = np.linspace(x.min(), x.max(), 100)
    ax.errorbar(x, y, xerr=dx, yerr=dy, fmt=".b", ecolor="gray", label="data")
    ax.plot(xf, linear(res["params"], xf * 1e-3), c="r", alpha=0.6, label="linear fit")
    ax.set_xlabel(r"$x$ [mm]")
    ax.set_ylabel(r"$T$ [$^\circ$C]")
    ax.set_title(title)  # every graph has a title (Tamir's grading, report-rules §6.1)
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def plot_residuals(res, path, title):
    x, dx = np.array(res["x"]) * 1e3, np.array(res["dx"]) * 1e3
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    ax.errorbar(x, res["residuals"], xerr=dx, yerr=res["dy"], fmt=".b", ecolor="gray", label="residuals")
    ax.hlines(0, x.min(), x.max(), colors="r", linestyles="dashed")
    ax.set_xlabel(r"$x$ [mm]")
    ax.set_ylabel(r"$T - f(x)$ [K]")
    ax.set_title(title)  # every graph has a title (Tamir's grading, report-rules §6.1)
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def plot_rate(res, path, title):
    x, y = np.array(res["x"]), np.array(res["y"])
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    ax.errorbar(x, y, xerr=res["dx"], yerr=res["dy"], fmt=".b", ecolor="gray", label="data")
    ax.plot(x, linear(res["params"], x), c="r", alpha=0.6, label="linear fit")
    ax.set_xlabel(r"$t$ [s]")
    ax.set_ylabel(r"$T$ [$^\circ$C]")
    ax.set_title(title)  # every graph has a title (Tamir's grading, report-rules §6.1)
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def plot_rate_residuals(res, path, title):
    x = np.array(res["x"])
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    ax.errorbar(x, res["residuals"], xerr=res["dx"], yerr=res["dy"], fmt=".b", ecolor="gray", label="residuals")
    ax.hlines(0, x.min(), x.max(), colors="r", linestyles="dashed")
    ax.set_xlabel(r"$t$ [s]")
    ax.set_ylabel(r"$T - f(t)$ [K]")
    ax.set_title(title)  # every graph has a title (Tamir's grading, report-rules §6.1)
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


# ---------- course rounding (D p.24), copied from free fall ----------

def _dec(v):
    return Decimal(repr(float(v)))


def _exp(d):
    """Exponent of the most significant digit."""
    return d.adjusted()


def round_2sf(v):
    """Value without error: 2 significant figures, as a plain string."""
    d = _dec(v)
    if d == 0:
        return Decimal(0)
    q = Decimal(1).scaleb(_exp(d) - 1)
    r = d.quantize(q, rounding=ROUND_HALF_UP)
    if _exp(r) != _exp(d):  # 9.96 -> 10: re-round at the new magnitude
        r = d.quantize(Decimal(1).scaleb(_exp(r) - 1), rounding=ROUND_HALF_UP)
    return r


def round_pair(v, err):
    """Error to 2 significant figures, value to the same decimal place."""
    e = round_2sf(err)
    q = Decimal(1).scaleb(_exp(e) - 1)
    val = _dec(v).quantize(q, rounding=ROUND_HALF_UP)
    if q >= 1:  # integer place: no decimals to show
        return f"{val:f}".split(".")[0], f"{e:f}".split(".")[0]
    return f"{val:f}", f"{e.quantize(q):f}"


def tex_number(d):
    """2-sig-fig Decimal -> LaTeX; scientific notation below 1e-3."""
    if d != 0 and abs(d) < Decimal("0.001"):
        mant = d.scaleb(-_exp(d))
        return rf"{mant:f} \cdot 10^{{{_exp(d)}}}"
    return f"{d:f}"


def tex_pm(v, err):
    a, b = round_pair(v, err)
    return f"{a} \\pm {b}"


def tex_rel(v, err):
    """Relative error in percent, 2 significant figures."""
    return tex_number(round_2sf(abs(err / v) * 100)) + r"\%"


def tex_pm_sci(v, err, exp):
    """Value and error scaled by 10^exp, for large/small quantities like sigma."""
    s = 10.0 ** exp
    return rf"({tex_pm(v / s, err / s)}) \cdot 10^{{{exp}}}"


# ---------- LaTeX numbers ----------

def macros(A_, B, C=None):
    out = {}
    out["SigmaVal"] = tex_pm_sci(A_["sigma"], A_["sigma_err"], 7)
    out["SigmaRel"] = tex_rel(A_["sigma"], A_["sigma_err"])
    # Contribution of each term of (7) to sigma's relative error, in percent (results text).
    pct = lambda v: tex_number(round_2sf(v * 100)) + r"\%"
    terms = A_["sigma_rel_terms"]
    out["ATermR"] = pct(terms["r"])
    out["ATermDch"] = pct(terms["Dch"])
    rest = max(v for k, v in terms.items() if k not in ("r", "Dch"))
    out["ATermRestMax"] = pct(rest)
    assert terms["r"] > terms["Dch"] > rest, "term order changed: fix the results text"
    t_vals = part_a_sheet()["fall time (t)"][0]
    out["ATMin"], out["ATMax"] = f"{min(t_vals):.2f}", f"{max(t_vals):.2f}"
    assert A_["m"]["stat"] == 0, "mass readings no longer identical: fix the results text"
    for tag, f in zip(("Last", "Mid", "Early"), B["fits"]):
        out[f"B{tag}AZero"] = tex_pm(f["params"][0], f["errors"][0])
        out[f"B{tag}AOne"] = tex_pm(f["params"][1], f["errors"][1])
        out[f"B{tag}AOneRel"] = tex_rel(f["params"][1], f["errors"][1])
        out[f"B{tag}Chi"] = tex_number(round_2sf(f["chi2_red"]))
        out[f"B{tag}P"] = tex_number(round_2sf(f["p"]))
        out[f"B{tag}Kappa"] = tex_pm(f["kappa"], f["kappa_err"])
        out[f"B{tag}KappaRel"] = tex_rel(f["kappa"], f["kappa_err"])
    # Position error carried into temperature through the slope, |a1|·Δx, last-row fit (results text).
    last = B["fits"][0]
    out["BXErrK"] = tex_number(round_2sf(abs(last["params"][1]) * last["dx"][0]))
    out["TErr"] = "0.002"
    # Discussion: resolution error of the logger by booklet (28); it must stay between T_ERR and the
    # end-of-part-b residual scatter for the "even this is far from the scatter" sentence to hold.
    out["TResErr"] = tex_number(round_2sf(T_LOG_RES / np.sqrt(12)))
    z = residual_z(last)
    order = np.argsort(z)[::-1]
    assert set(order[:2]) == {0, 1} and z.max() < 3, "largest residuals no longer sensors 1-2 within 3: fix the results text"
    # Results text: the residual pattern repeats in all three fits (same sign at every sensor, sensors 1-2 largest).
    signs = [tuple(np.sign(f["residuals"])) for f in B["fits"]]
    assert len(set(signs)) == 1, "residual signs differ between the part-b fits: fix the results text"
    for f in B["fits"]:
        assert set(np.argsort(residual_z(f))[::-1][:2]) == {0, 1}, "sensors 1-2 no longer largest in every fit"
    out["BZOne"], out["BZTwo"] = tex_number(round_2sf(z[0])), tex_number(round_2sf(z[1]))
    out["BMidTime"], out["BEarlyTime"] = f"{B['fits'][1]['time']:.0f}", f"{B['fits'][2]['time']:.0f}"
    # Discussion: sensor offsets at room temperature (first reading of part b, before the heat spreads),
    # same sign pattern as the final fit's residuals.
    off = B["room_offsets"]
    assert tuple(np.sign(off)) == tuple(np.sign(last["residuals"])), "offset signs no longer match the residuals"
    # Discussion: share of the final fit's chi^2 coming from sensors 1-2, and the p-value range of the three fits.
    z2 = residual_z(last) ** 2
    share = (z2[0] + z2[1]) / z2.sum()
    assert share > 0.5, "sensors 1-2 no longer dominate chi^2: fix the discussion text"
    out["DShareOneTwo"] = tex_number(round_2sf(share * 100)) + r"\%"
    ps = [f["p"] for f in B["fits"]]
    out["DPMin"], out["DPMax"] = tex_number(round_2sf(min(ps))), tex_number(round_2sf(max(ps)))
    # Discussion: sensor 2's residual in the three fits (largest residual), to show the pattern repeats in size too.
    r2 = [f["residuals"][1] for f in B["fits"]]
    out["DResTwoMin"], out["DResTwoMax"] = f"{min(r2):.2f}", f"{max(r2):.2f}"
    assert max(r2) - min(r2) < 0.02, "sensor 2 residual no longer stable across fits: fix the discussion text"
    # Discussion: residual minus each sensor's room-temperature offset (final fit).
    corr = np.array(last["residuals"]) - np.array(off)
    rest = np.abs(corr[2:]).max()
    assert abs(corr[0]) > 2 * rest and abs(corr[1]) > 2 * rest, "sensors 1-2 no longer stand out after offsets: fix the discussion"
    out["DCorrOne"], out["DCorrTwo"] = f"{abs(corr[0]):.2f}", f"{abs(corr[1]):.2f}"
    assert corr[0] < 0 < corr[1], "sensor 1 negative / sensor 2 positive after offsets no longer holds: fix the discussion"
    out["DCorrRestMax"] = f"{rest:.2f}"
    # Discussion (sensors 1-2): deviation from room temperature (offset vs mean) to the final fit (residual).
    out["DOffOne"], out["DOffTwo"] = f"{abs(off[0]):.3f}", f"{abs(off[1]):.3f}"
    out["DResOne"], out["DResTwo"] = f"{abs(last['residuals'][0]):.2f}", f"{abs(last['residuals'][1]):.2f}"
    assert abs(last["residuals"][0]) > abs(off[0]) and abs(last["residuals"][1]) > abs(off[1]), "sensors 1-2 deviation no longer grows"
    assert abs(last["residuals"][1]) > abs(last["residuals"][0]), "discussion says sensor 2 deviates more than sensor 1"
    assert last["residuals"][0] < 0 < last["residuals"][1], "discussion says sensor 1 reads below the line, sensor 2 above"
    for f_ in B["fits"]:   # in every fit, sensors 1-2 change more than any of sensors 3-8
        ch = np.abs(np.array(f_["residuals"]) - np.array(off))
        assert min(ch[0], ch[1]) > ch[2:].max(), ("sensors 1-2 change no longer the largest", f_["time"])
    half = rest / (abs(last["params"][1]) * last["dx"][0])
    assert 0.4 < half < 0.6, ("discussion says sensors 3-8 leftover is about half the effective error", half)
    out["DOffsetMax"] = tex_number(round_2sf(np.abs(off).max()))
    out["BLastTime"] = f"{B['fits'][0]['time']:.0f}"  # time of the final reading, from the start of the part-b recording
    for k, v in B["nsigma_slopes"].items():
        out[f"BNsigma{'ABC'[int(k[0])]}{'ABC'[int(k[1])]}"] = tex_number(round_2sf(v))
    ns = list(B["nsigma_slopes"].values())
    assert max(ns) < 3, "slope Nsigma >= 3: fix the equilibrium bullet"
    out["DSlopeNsMin"], out["DSlopeNsMax"] = tex_number(round_2sf(min(ns))), tex_number(round_2sf(max(ns)))
    if C:
        for tag, k in (("Cool", "cool"), ("Heat", "heat"), ("Exp", "exp")):
            f = C[k]
            out[f"C{tag}Rate"] = tex_pm(f["params"][1] * 1e3, f["errors"][1] * 1e3)  # in 10^-3 K/s
            out[f"C{tag}RateRel"] = tex_rel(f["params"][1], f["errors"][1])
            out[f"C{tag}BZero"] = tex_pm(f["params"][0], f["errors"][0])   # intercept b0 [degC]
            out[f"C{tag}Chi"] = tex_number(round_2sf(f["chi2_red"]))
            out[f"C{tag}P"] = tex_p(f["chi2_red"], f["dof"])
            out[f"C{tag}N"] = str(f["n"])
        for tag, k in (("Cool", "cool"), ("Heat", "heat"), ("Exp", "exp")):
            z = residual_z(C[k])
            out[f"C{tag}FracThree"] = tex_number(round_2sf((z > 3).mean() * 100)) + r"\%"
            out[f"C{tag}MaxZ"] = tex_number(round_2sf(z.max()))
        # Discussion numbers (data observations only).
        e = np.array(C["exp"]["residuals"])
        s_res = e.std(ddof=1)                         # sample standard deviation, booklet (32)
        out["DExpRms"] = tex_number(round_2sf(s_res))
        out["DExpRatio"] = tex_number(round_2sf((s_res / T_ERR) ** 2))
        assert T_ERR < T_LOG_RES / np.sqrt(12) < s_res / 2, "resolution-error comparison changed: fix the discussion"
        # Discussion text says "p < 10^-100" for cooling and heating (typed in main.tex).
        assert all(C[k]["p"] < 1e-100 for k in ("cool", "heat")), "cool/heat p no longer < 1e-100: fix the discussion"
        out["DHeatRateStart"], out["DHeatRateEnd"] = (tex_number(round_2sf(v)) for v in C["heat_minute_rates"])
        r0, r1 = C["heat_minute_rates"]
        out["DHeatRateDrop"] = tex_number(round_2sf((1 - r1 / r0) * 100)) + r"\%"
        out["CPin"] = tex_pm(C["P_in"], C["P_in"] * np.hypot(A_["V"]["err"] / A_["V"]["mean"], A_["I"]["err"] / A_["I"]["mean"]))
        out["CPavg"] = tex_pm(C["P_avg"], C["P_avg_err"])
        out["CPavgRel"] = tex_rel(C["P_avg"], C["P_avg_err"])
        out["CKappa"] = tex_pm(C["kappa"], C["kappa_err"])
        out["CKappaRel"] = tex_rel(C["kappa"], C["kappa_err"])
    last = B["fits"][0]
    for tag, (k, dk) in (("B", (last["kappa"], last["kappa_err"])),
                         ("C", (C["kappa"], C["kappa_err"]) if C else (None, None))):
        if k is None:
            continue
        L, dL, ns = lorenz(k, dk, A_)
        out[f"{tag}Lorenz"] = tex_pm_sci(L, dL, -8)
        out[f"{tag}LorenzRel"] = tex_rel(L, dL)
        out[f"{tag}LorenzNsigma"] = tex_number(round_2sf(ns))
        assert ns > 3, (tag, ns)  # the report text says both N_sigma are above 3 (sections b, c, discussion)
    return out


def residual_z(f):
    """|residual| in units of each point's effective error sqrt(dy^2 + (b1·dx)^2), as ODR weighs it."""
    res, dx, dy = (np.array(f[k]) for k in ("residuals", "dx", "dy"))
    return np.abs(res) / np.sqrt(dy ** 2 + (f["params"][1] * dx) ** 2)


def log10_p_value(chi2, dof):
    """log10 of the chi^2 survival probability, valid where scipy's sf underflows to 0.
    p = Q(a, x) with a = dof/2, x = chi2/2, by the continued fraction of the regularized upper
    incomplete gamma function (Numerical Recipes gcf, Lentz), kept in log space; converges for x > a + 1."""
    import math
    a_, x = dof / 2.0, chi2 / 2.0
    assert x > a_ + 1, "continued fraction needs x > a + 1"
    tiny = 1e-300
    b = x + 1 - a_
    c, d = 1 / tiny, 1 / b
    h = d
    for i in range(1, 10000):
        an = -i * (i - a_)
        b += 2
        d = an * d + b
        d = tiny if abs(d) < tiny else d
        c = b + an / c
        c = tiny if abs(c) < tiny else c
        d = 1 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-15:
            break
    return (-x + a_ * math.log(x) - math.lgamma(a_) + math.log(h)) / math.log(10)


def tex_p(chi2_red, dof):
    """p-value to 2 significant figures even when it underflows (never print p = 0)."""
    l10 = log10_p_value(chi2_red * dof, dof)
    if l10 < P_FLOOR_LOG10:   # beyond this the exact exponent has no physical meaning (user, 2026-11-14)
        return rf"< 10^{{{P_FLOOR_LOG10}}}"
    e = int(np.floor(l10))
    m = round_2sf(10 ** (l10 - e))
    if m >= 10:
        m, e = round_2sf(m / 10), e + 1
    return rf"{m:f} \cdot 10^{{{e}}}"


def lorenz(kappa, dkappa, A_):
    """Report (11), (12), N_sigma vs the exact theory value by D(52).
    (12) is written in the directly measured quantities (Tamir's rule for (7), user 2026-11-15):
    kappa ~ 1/D^2 and sigma ~ D_ch^2/(D - D_ch) share D, so L ~ (D - D_ch)/(D^2 D_ch^2) and
    d ln L/dD = 1/(D - D_ch) - 2/D, |d ln L/dD_ch| = 2/D_ch + 1/(D - D_ch).
    The other terms are kappa's and sigma's own: take their squared relative errors and remove
    their D and D_ch terms, which are replaced by the two terms above."""
    sig, dsig = A_["sigma"], A_["sigma_err"]
    L = kappa / (sig * T_ROOM)
    Dc, DD, dDc, dD = A_["Dch"]["mean"], A_["D"]["mean"], A_["Dch"]["err"], A_["D"]["err"]
    terms = A_["sigma_rel_terms"]
    k_rest = (dkappa / kappa) ** 2 - (2 * dD / DD) ** 2             # P (or P_avg) and a_1 terms of (10)
    s_rest = (dsig / sig) ** 2 - terms["Dch"] ** 2 - terms["D"] ** 2  # m, t, r_m, L_0 terms of (7)
    assert k_rest > 0 and s_rest > 0
    rel = np.sqrt(k_rest + s_rest + (T_ROOM_ERR / T_ROOM) ** 2
                  + ((1 / (DD - Dc) - 2 / DD) * dD) ** 2 + ((2 / Dc + 1 / (DD - Dc)) * dDc) ** 2)
    dL = L * rel
    return float(L), float(dL), float(abs(L - L_THEO) / dL)


def write_numbers(m, path):
    lines = ["% Generated by analysis/analysis.py -- do not edit by hand.",
             "% Values are in math mode; units are written in the report text."]
    lines += [f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in m.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_a_table(A_, path):
    """Appendix: every part-a quantity used in (2), mean ± error and relative error, rounded
    by the booklet rules. Measured values: combined error D(35) (L0: resolution only, D(28));
    a, r_m, w: from the diameters (w by report (6))."""
    rows = [("m", "g", A_["m"]["mean"], A_["m"]["err"], A_["m"]["n"]),
            ("t", "s", A_["t"]["mean"], A_["t"]["err"], A_["t"]["n"]),
            ("d", "mm", A_["d"]["mean"], A_["d"]["err"], A_["d"]["n"]),
            ("D_{ch}", "mm", A_["Dch"]["mean"], A_["Dch"]["err"], A_["Dch"]["n"]),
            ("D", "mm", A_["D"]["mean"], A_["D"]["err"], A_["D"]["n"]),
            ("L_0", "cm", A_["L0"]["mean"], A_["L0"]["err"], 1),
            ("a", "mm", A_["a"], A_["da"], None),
            ("r_m", "mm", A_["r"], A_["dr"], None),
            ("w", "mm", A_["w"], A_["dw"], None)]
    lines = ["% Generated by analysis/analysis.py -- do not edit by hand.",
             r"\begin{table}[H]", r"  \centering", r"  \renewcommand{\arraystretch}{1.3}",
             r"  \begin{tabular}{|c|c|c|c|}", r"    \hline",
             r"    גודל & מספר מדידות & ערך & שגיאה יחסית \\ \hline"]
    for sym, unit, v, e, n in rows:
        cnt = str(n) if n else "מחושב"
        lines.append(f"    ${sym}$ & {cnt} & ${tex_pm(v, e)}\\U{{{unit}}}$ & ${tex_rel(v, e)}$ \\\\ \\hline")
    lines += [r"  \end{tabular}",
              r"  \caption{הגדלים ששימשו לחישוב המוליכות החשמלית לפי נוסחה~\eqref{eq:sigma}, ושגיאותיהם. $a$, $r_m$ ו-$w$ חושבו מהקטרים שנמדדו. השגיאה ב-$\sigma$ חושבה ישירות מ-$\Delta D_{ch}$ ומ-$\Delta D$, לפי נוסחה~\eqref{eq:dsigma}, ולא מ-$\Delta a$ ומ-$\Delta w$.}",
              r"  \label{tab:a-values}", r"\end{table}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _fmt(v, res=0.01):
    """Raw values shown to the instrument's resolution (the sheet stores 6.00 as 6): never rounded further."""
    dec = max(0, -int(np.floor(np.log10(res) + 1e-9)))
    assert abs(round(v, dec) - v) < 1e-9, f"{v} has more digits than its resolution {res}"
    return f"{v:.{dec}f}"


def write_raw_a(path):
    """Appendix: every part-a reading, unrounded (guide: raw data stays as measured)."""
    t = part_a_sheet()
    rows = [("m", "g", "magnet mass (m)"), ("t", "s", "fall time (t)"), ("d", "mm", "magnet height (d)"),
            ("D_{ch}", "mm", "tube radius (a)"), ("D", "mm", "tube diameter"), ("L_0", "cm", "tube length"),
            ("V", "V", "voltage"), ("I", "A", "current (I)")]
    lines = ["% Generated by analysis/analysis.py from the part-a sheet -- do not edit by hand.",
             r"\begin{table}[H]", r"  \centering", r"  \small", r"  \renewcommand{\arraystretch}{1.2}",
             r"  \begin{tabular}{|c|c|c|p{0.55\textwidth}|}", r"    \hline",
             r"    גודל & יחידות & רזולוציה & מדידות \\ \hline"]
    for sym, unit, key in rows:
        vals, res = t[key]
        lines.append(f"    ${sym}$ & $\\mathrm{{{unit}}}$ & ${res:g}$ & \\textenglish{{${', '.join(_fmt(v, res) for v in vals)}$}} \\\\ \\hline")
    lines += [r"  \end{tabular}",
              r"  \caption{המדידות הגולמיות של חלק א׳, כפי שנרשמו. $D_{ch}$ נמדד כקוטר התעלה (על החוטר), ו-$D$ כקוטר החיצוני של הצינור.}",
              r"  \label{tab:raw-a}", r"\end{table}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_raw_b(B, path):
    """Appendix: the eight sensor readings used in the three part-b fits."""
    fits = B["fits"][::-1]   # earliest first
    head = " & ".join([r"$x\ [\mathrm{mm}]$"] + [f"$T(t = {f['time']:.0f}\\U{{s}})\\ [^\\circ\\mathrm{{C}}]$" for f in fits])
    lines = ["% Generated by analysis/analysis.py from the part-b log -- do not edit by hand.",
             r"\begin{table}[H]", r"  \centering", r"  \renewcommand{\arraystretch}{1.2}",
             r"  \begin{tabular}{|c|c|c|c|}", r"    \hline", "    " + head + r" \\ \hline"]
    for i, x in enumerate(X_MM):
        lines.append("    " + " & ".join([f"{x:g}"] + [_fmt(f["y"][i]) for f in fits]) + r" \\ \hline")
    lines += [r"  \end{tabular}",
              r"  \caption{הטמפרטורות שמדדו שמונת החיישנים בשלוש המדידות של חלק ב׳ שעליהן נעשו ההתאמות, כפי שתועדו בתוכנת ההקלטה. $t$ נמדד מתחילת ההקלטה.}",
              r"  \label{tab:raw-b}", r"\end{table}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_raw_c(C, path, per_row=4):
    """Appendix: every (t, T) point of the three part-c rate fits, sensor 4, unrounded.
    Printed `per_row` pairs per table row to keep the tables short."""
    names = {"cool": "מקטע הקירור", "heat": "מקטע החימום (הדקות 3--12 לאחר הפעלת ספק הכוח)",
             "exp": "-200 השניות האחרונות של ההקלטה בחלק ב׳"}
    files = {"cool": "חלק ג׳", "heat": "חלק ג׳", "exp": "חלק ב׳"}
    out = ["% Generated by analysis/analysis.py from the part-b/c logs -- do not edit by hand."]
    for k in ("cool", "heat", "exp"):
        f = C[k]
        pts = [(f"{t:.3f}", _fmt(T)) for t, T in zip(f["x"], f["y"])]
        nrow = -(-len(pts) // per_row)
        cols = [pts[c * nrow:(c + 1) * nrow] for c in range(per_row)]
        head = " & ".join([r"$t\ [\mathrm{s}]$ & $T\ [^\circ\mathrm{C}]$"] * per_row)
        out += [r"\begin{table}[H]", r"  \centering", r"  \scriptsize", r"  \renewcommand{\arraystretch}{1.0}",
                r"  \setlength{\tabcolsep}{4pt}",
                r"  \begin{tabular}{|" + "cc|" * per_row + "}", r"    \hline", "    " + head + r" \\ \hline"]
        for r in range(nrow):
            cells = []
            for c in cols:
                cells += list(c[r]) if r < len(c) else ["", ""]
            out.append("    " + " & ".join(cells) + r" \\")
        out += [r"    \hline", r"  \end{tabular}",
                f"  \\caption{{\\relax{{הטמפרטורה שמדד חיישן 4 ב{names[k]}, {len(pts)} מדידות, כפי שתועדו בתוכנת ההקלטה. $t$ נמדד מתחילת ההקלטה ב{files[k]}.}}}}",
                f"  \\label{{tab:raw-c-{k}}}", r"\end{table}"]
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def write_colab_inputs(B, path):
    """One sheet per part-b fit, columns x, dx, y, dy as the template's choose_columns expects."""
    with pd.ExcelWriter(path) as xw:
        for tag, f in zip(("last", "minus100s", "minus200s"), B["fits"]):
            pd.DataFrame({"x [m]": f["x"], "dx [m]": f["dx"], "T [C]": f["y"], "dT [K]": f["dy"]}) \
              .to_excel(xw, sheet_name=tag, index=False)


def write_colab_inputs_c(C, path):
    """Part-c rate fits for the Colab check: one sheet each, columns x, dx, y, dy."""
    with pd.ExcelWriter(path) as xw:
        for k in ("cool", "heat", "exp"):
            f = C[k]
            pd.DataFrame({"t [s]": f["x"], "dt [s]": f["dx"], "T [C]": f["y"], "dT [K]": f["dy"]}) \
              .to_excel(xw, sheet_name=k, index=False)


def main():
    FIGURES.mkdir(parents=True, exist_ok=True)
    A_ = part_a()
    B = part_b(A_)
    plot_fit(B["fits"][0], FIGURES / "b_fit.pdf", f"Temperature vs. sensor position (final reading, t = {B['fits'][0]['time']:.0f} s)")
    plot_residuals(B["fits"][0], FIGURES / "b_res.pdf", f"Residuals of the linear fit (final reading, t = {B['fits'][0]['time']:.0f} s)")
    for tag, f in (("mid", B["fits"][1]), ("early", B["fits"][2])):   # stability fits, appendix
        plot_fit(f, FIGURES / f"b_fit_{tag}.pdf", f"Temperature vs. sensor position (t = {f['time']:.0f} s)")
        plot_residuals(f, FIGURES / f"b_res_{tag}.pdf", f"Residuals of the linear fit (t = {f['time']:.0f} s)")
    C = part_c(A_, B)
    f = C["exp"]
    assert abs(log10_p_value(f["chi2_red"] * f["dof"], f["dof"]) - np.log10(f["p"])) < 1e-6, "tiny-p check vs scipy failed"
    titles = {"cool": "cooling", "heat": "heating, 3-12 min", "exp": "end of part b, last 200 s"}
    for k in ("cool", "heat", "exp"):
        plot_rate(C[k], FIGURES / f"c_{k}_fit.pdf", f"Sensor 4 temperature vs. time ({titles[k]})")
        plot_rate_residuals(C[k], FIGURES / f"c_{k}_res.pdf", f"Residuals of the linear fit ({titles[k]})")
    write_numbers(macros(A_, B, C), REPORT / "numbers.tex")
    write_colab_inputs_c(C, COLAB / "partc_fits.xlsx")
    write_a_table(A_, REPORT / "a_table.tex")
    write_raw_a(REPORT / "raw_a.tex")
    write_raw_b(B, REPORT / "raw_b.tex")
    write_raw_c(C, REPORT / "raw_c.tex")
    write_colab_inputs(B, COLAB / "partb_fits.xlsx")
    (HERE / "results.json").write_text(json.dumps({"part_a": A_, "part_b": B, "part_c": C}, indent=2, default=float))


if __name__ == "__main__":
    main()
