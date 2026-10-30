"""Free-fall analysis: error budget, ODR fits, figures and LaTeX numbers.

Reproduces the course Colab notebooks (../colab/) locally so the report is
rebuilt from one command. Fit code is copied from the notebooks unchanged.

Outputs (paths relative to this file):
  ../report/figures/{lin,par}_{fit,res}.pdf
  ../report/numbers.tex   -- one \\newcommand per reported value, already rounded
  results.json            -- unrounded values, read by verify_colab.py
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
XLSX = HERE.parent / "FreeFall_19-10-2026_14-30-49.xlsx"
REPORT = HERE.parent / "report"
FIGURES = REPORT / "figures"

H_RES = 0.1        # ruler resolution [cm]
T_RES = 1e-5       # timing software resolution [s]
G_THEO = 981.0     # theory file: 9.81 m/s^2 [cm/s^2]
G_THEO_ERR = 10.0  # theory file: 0.10 m/s^2 [cm/s^2]


# ---------- error budget from the raw times ----------

def raw_table():
    """Raw sheet: one row per height, t1..t10 in seconds. Unmeasured heights dropped."""
    df = pd.read_excel(XLSX, sheet_name="גיליון1", header=6)
    df = df.dropna(axis=1, how="all")
    df = df.dropna(subset=["t1[sec]"]).reset_index(drop=True)
    return df


def error_budget(raw):
    times = raw[[f"t{i}[sec]" for i in range(1, 11)]].to_numpy(dtype=float)
    n = times.shape[1]
    t = times.mean(axis=1)                          # D(29)
    t_stat = times.std(axis=1, ddof=1) / np.sqrt(n)  # D(32), D(34)
    t_res = T_RES / np.sqrt(12)                     # D(28)
    dt = np.sqrt(t_stat**2 + t_res**2)              # D(35)
    t2 = t**2
    dt2 = 2 * t * dt                                # D(39): d(t^2) = 2t dt
    h = raw["h[cm]"].to_numpy(dtype=float)
    dh = np.full_like(h, H_RES / np.sqrt(12))       # D(28)
    return pd.DataFrame({"h": h, "dh": dh, "t": t, "t_stat": t_stat,
                         "t_res": t_res, "dt": dt, "t2": t2, "dt2": dt2})


def check_against_excel(budget, raw):
    """The Excel sheet computed the same budget; both must agree."""
    pairs = {"t": "t_avg[sec]", "t_stat": "Δt_stat[sec]", "dt": "Δt_fin[sec]",
             "t2": "t_avg^2[sec^2]", "dt2": "Δt_avg^2[sec^2]", "dh": "Δh[cm]"}
    for ours, col in pairs.items():
        np.testing.assert_allclose(budget[ours], raw[col].astype(float), rtol=1e-12, atol=0,
                                   err_msg=f"{ours} differs from Excel column {col}")


# ---------- fit code copied from the Colab notebooks ----------

def linear(A, x):
    return A[1] * x + A[0]


def parabolic(A, x):
    return A[2] * x**2 + A[1] * x + A[0]


def odr_fit(fit_func, initial_guesses, x, delta_x, y, delta_y):
    model = Model(fit_func)
    odr_data = RealData(x, y, sx=delta_x, sy=delta_y)
    odr = ODR(data=odr_data, model=model, beta0=initial_guesses)
    output = odr.run()
    return output.beta, output.sd_beta, output.cov_beta, output


def calc_stats(fit_func, x, y, fit_params, output):
    residuals = y - fit_func(fit_params, x)
    degrees_of_freedom = len(x) - len(fit_params)
    chi2 = output.sum_square
    chi2_red = chi2 / degrees_of_freedom
    p_val = stats.chi2.sf(chi2, degrees_of_freedom)
    return residuals, degrees_of_freedom, chi2_red, p_val


def run_fit(name, fit_func, guesses, x, dx, y, dy, g_index):
    params, errors, _, output = odr_fit(fit_func, guesses, x, dx, y, dy)
    residuals, dof, chi2_red, p_val = calc_stats(fit_func, x, y, params, output)
    g = 2 * params[g_index]
    g_err = 2 * errors[g_index]
    n_sigma = abs(g - G_THEO) / np.sqrt(g_err**2 + G_THEO_ERR**2)  # D(51)
    return {"name": name, "params": params.tolist(), "errors": errors.tolist(),
            "chi2_red": float(chi2_red), "p": float(p_val), "dof": int(dof),
            "g": float(g), "g_err": float(g_err), "n_sigma": float(n_sigma),
            "residuals": np.asarray(residuals).tolist()}


def max_residual_sigma(res, slope, x, dx, dy):
    """Largest |residual| in units of the point's error as the fit weighs it:
    sqrt(Δy² + (f'(x)·Δx)²), with Δx carried through the fitted function's slope."""
    x, dx, dy = (np.asarray(v, dtype=float) for v in (x, dx, dy))
    sigma = np.sqrt(dy**2 + (slope(res["params"], x) * dx) ** 2)
    return float(np.max(np.abs(res["residuals"]) / sigma))


def error_source_refits(res, x, dx, y, dy):
    """Which error makes chi2_red too small in the parabolic fit: refit with each error
    switched off (scaled by 1e-3, ODR needs it nonzero) and compare the statistics."""
    x, dx, y, dy = (np.asarray(v, dtype=float) for v in (x, dx, y, dy))
    no_dh = run_fit("no_dh", parabolic, (0, 0, 981 / 2), x, dx, y, dy * 1e-3, g_index=2)
    no_dt = run_fit("no_dt", parabolic, (0, 0, 981 / 2), x, dx * 1e-3, y, dy, g_index=2)
    slope = res["params"][1] + 2 * res["params"][2] * x
    res.update(chi2_red_no_dh=no_dh["chi2_red"], p_no_dh=no_dh["p"],
               chi2_red_no_dt=no_dt["chi2_red"], p_no_dt=no_dt["p"],
               time_err_cm=float(np.mean(slope * dx)), dh_cm=float(dy[0]))


# ---------- figures ----------

def plot_fit(fit_func, res, x, dx, y, dy, xlabel, fit_label, path):
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    x_fit = np.linspace(min(x), max(x), 10 * len(x))
    ax.errorbar(x, y, xerr=dx, yerr=dy, fmt=".b", ecolor="gray", label="data")
    ax.plot(x_fit, fit_func(res["params"], x_fit), c="r", alpha=0.6, label=fit_label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(r"$h$ [cm]")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def plot_residuals(res, x, dx, dy, xlabel, ylabel, path):
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    ax.errorbar(x, res["residuals"], xerr=dx, yerr=dy, fmt=".b", ecolor="gray",
                label="residuals")
    ax.hlines(0, min(x), max(x), colors="r", linestyles="dashed")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


# ---------- course rounding (D p.24) ----------

def _dec(v):
    return Decimal(repr(float(v)))


def _exp(d):
    """Exponent of the most significant digit."""
    return d.adjusted()


def round_2sf(v):
    """Value without error: 2 significant figures, as a plain string."""
    d = _dec(v)
    if d == 0:
        return "0"
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


# ---------- LaTeX numbers ----------

def macros(lin, par):
    out = {}
    for tag, res in (("Lin", lin), ("Par", par)):
        for i, word in enumerate(("Zero", "One", "Two")[:len(res["params"])]):
            v, e = res["params"][i], res["errors"][i]
            out[f"{tag}A{word}"] = tex_pm(v, e)
            out[f"{tag}A{word}Rel"] = tex_rel(v, e)
        out[f"{tag}Chi"] = tex_number(round_2sf(res["chi2_red"]))
        out[f"{tag}P"] = tex_number(round_2sf(res["p"]))
        out[f"{tag}G"] = tex_pm(res["g"], res["g_err"])
        out[f"{tag}GRel"] = tex_rel(res["g"], res["g_err"])
        out[f"{tag}Nsigma"] = tex_number(round_2sf(res["n_sigma"]))
    # Discussion estimates (order of magnitude, 2 significant figures, no error):
    # time the ball had already fallen when timing started, tau = a1/g, and the distance
    # fallen by then, a1^2/(2g), both from the parabolic fit.
    a1, g = par["params"][1], par["g"]
    out["DelayMs"] = tex_number(round_2sf(1e3 * a1 / g))
    out["DelayDistMm"] = tex_number(round_2sf(10 * a1**2 / (2 * g)))
    # N_sigma between the two fits' g, D(51). Same data, so only indicative.
    out["NsigmaFits"] = tex_number(round_2sf(
        abs(lin["g"] - par["g"]) / np.sqrt(lin["g_err"]**2 + par["g_err"]**2)))
    # Discussion of the overestimated errors (parabolic fit): refits without Δh and
    # without Δt, and the average time-error contribution slope·Δt next to Δh.
    # Only present in our own run (the Colab notebooks print no refits); main() asserts
    # they exist, verify_colab.py compares the macros both sides have.
    if "chi2_red_no_dh" in par:
        out.update(refit_macros(par))
    out["GTheo"] = tex_pm(G_THEO, G_THEO_ERR)
    out["HRes"] = "0.1"
    out["TRes"] = r"10^{-5}"
    return out


def refit_macros(par):
    out = {}
    out["ChiNoDh"] = tex_number(round_2sf(par["chi2_red_no_dh"]))
    out["PNoDh"] = tex_number(round_2sf(par["p_no_dh"]))
    out["ChiNoDt"] = tex_number(round_2sf(par["chi2_red_no_dt"]))
    out["PNoDt"] = tex_number(round_2sf(par["p_no_dt"]))
    out["TimeErrCm"] = tex_number(round_2sf(par["time_err_cm"]))
    out["DhCm"] = tex_number(round_2sf(par["dh_cm"]))
    return out


def write_raw_table(raw, path):
    """Appendix table of all measured fall times. Raw data stays unrounded (guide);
    shown with 5 decimals = the timing software's resolution of 1e-5 s. Units in the
    column headers (user, 2026-10-29: long data tables only)."""
    cols = [f"t{i}[sec]" for i in range(1, 11)]
    # \textenglish keeps "symbol [unit]" in LTR order inside the RTL table.
    head = " & ".join([r"\textenglish{$h$ [cm]}"] + [f"\\textenglish{{$t_{{{i}}}$ [s]}}" for i in range(1, 11)])
    rows = []
    for _, r in raw.iterrows():
        cells = [f"{int(r['h[cm]'])}"] + [f"{float(r[c]):.5f}" for c in cols]
        rows.append(" & ".join(cells) + r" \\ \hline")
    lines = ["% Generated by analysis/analysis.py from the raw Excel sheet -- do not edit by hand.",
             r"\begin{table}[H]", r"  \centering", r"  \small",
             r"  \setlength{\tabcolsep}{3pt}",
             r"  \begin{tabular}{|c|" + "c|" * 10 + "}", r"    \hline",
             "    " + head + r" \\ \hline"]
    lines += ["    " + row for row in rows]
    lines += [r"  \end{tabular}",
              r"  \caption{\added{זמני הנפילה שנמדדו, עשר מדידות בכל גובה, כפי שנרשמו בתוכנת המדידה.}}",
              r"  \label{tab:raw}", r"\end{table}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_numbers(m, path):
    lines = ["% Generated by analysis/analysis.py -- do not edit by hand.",
             "% Values are in math mode; units are written in the report text."]
    lines += [f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in m.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    FIGURES.mkdir(parents=True, exist_ok=True)
    raw = raw_table()
    budget = error_budget(raw)
    check_against_excel(budget, raw)

    # Fit inputs are the Excel sheets the Colab notebooks read, so the fits see
    # byte-identical numbers; check_against_excel ties them to the raw times.
    lin_sheet = pd.read_excel(XLSX, sheet_name="linear")
    par_sheet = pd.read_excel(XLSX, sheet_name="parabolic")
    xl, dxl, yl, dyl = (lin_sheet.iloc[:, c] for c in (3, 4, 1, 2))
    xp, dxp, yp, dyp = (par_sheet.iloc[:, c] for c in (3, 4, 1, 2))

    lin = run_fit("linear", linear, (0, 981), xl, dxl, yl, dyl, g_index=1)
    par = run_fit("parabolic", parabolic, (0, 0, 981 / 2), xp, dxp, yp, dyp, g_index=2)

    # The report says every residual is within 3 standard deviations of the fit's
    # error for that point (not the plotted Δh-only bars). Keep that claim true.
    lin["max_res_sigma"] = max_residual_sigma(lin, lambda A, x: A[1] + 0 * x, xl, dxl, dyl)
    par["max_res_sigma"] = max_residual_sigma(par, lambda A, x: A[1] + 2 * A[2] * x, xp, dxp, dyp)
    for res in (lin, par):
        assert res["max_res_sigma"] < 3, f"{res['name']}: a residual is beyond 3σ — fix the report text"
    error_source_refits(par, xp, dxp, yp, dyp)
    assert "ChiNoDh" in macros(lin, par), "refit macros missing from numbers.tex"

    plot_fit(linear, lin, xl, dxl, yl, dyl, r"$t^2$ [s$^2$]", "linear fit",
             FIGURES / "lin_fit.pdf")
    plot_residuals(lin, xl, dxl, dyl, r"$t^2$ [s$^2$]", r"$h - f(t^2)$ [cm]",
                   FIGURES / "lin_res.pdf")
    plot_fit(parabolic, par, xp, dxp, yp, dyp, r"$t$ [s]", "parabolic fit",
             FIGURES / "par_fit.pdf")
    plot_residuals(par, xp, dxp, dyp, r"$t$ [s]", r"$h - f(t)$ [cm]",
                   FIGURES / "par_res.pdf")

    write_numbers(macros(lin, par), REPORT / "numbers.tex")
    write_raw_table(raw, REPORT / "raw_table.tex")
    (HERE / "results.json").write_text(json.dumps({"linear": lin, "parabolic": par}, indent=2))
    budget.to_csv(HERE / "budget.csv", index=False)


if __name__ == "__main__":
    main()
