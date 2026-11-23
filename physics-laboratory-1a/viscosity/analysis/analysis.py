"""Viscosity analysis. Done so far: part a (group means, volumes, density fit). Part b: todo.

Fit code (odr_fit, calc_stats, linear) and the course rounding come from ../../labtools/.

Outputs (paths relative to this file):
  ../report/numbers.tex  -- one \\newcommand per reported value, already rounded
  results.json           -- unrounded values (read by verify_colab.py, once there is one)
"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # lab root, for labtools
from labtools.fit import calc_stats, linear, odr_fit
from labtools.rounding import round_2sf, tex_number, tex_pm, tex_rel, write_numbers  # noqa: F401

HERE = Path(__file__).resolve().parent
HYDROMETER_RES = 0.002  # g/cm^3 (user, 2026-11-22; the sheet says 0.001)
ROOT = HERE.parent
XLSX = ROOT / "viscosity measurements.xlsx"  # raw data as exported in the lab (DATA in ../Makefile)
REPORT = ROOT / "report"
FIGURES = REPORT / "figures"
N_TRACKS = 6  # sheets "ball 1" .. "ball 6"


def part_a():
    """Sheet 'part a measurements': glycerin density, then blocks 'category N' of 3 balls each.

    Returns {"rho": {"value", "res"}, "categories": {N: [{"no", "mass", "mass_res", "d", "d_res"}]}},
    units as in the sheet's headers (g/cm^3, g, mm).
    """
    raw = pd.read_excel(XLSX, sheet_name="part a measurements", header=None)
    cells = raw.to_numpy()
    rho_row = next(i for i, r in enumerate(cells) if r[0] == "glycerin density") + 2
    assert list(cells[rho_row - 1][:3]) == ["no.", "rho (g/cm^3)", "resolution (g/cm^3)"]
    # Hydrometer resolution: the sheet says 0.001 g/cm^3, the instrument's is 0.002 (user, 2026-11-22).
    # The raw file is left as exported; the correction is made here.
    assert float(cells[rho_row][2]) == 0.001, "hydrometer resolution in the sheet changed: re-check the override"
    out = {"rho": {"value": float(cells[rho_row][1]), "res": HYDROMETER_RES}, "categories": {}}
    header = ["no.", "mass (g)", "mass res (g)", "diameter (mm)", "res diameter (mm)"]
    for i, r in enumerate(cells):
        if isinstance(r[1], str) and r[1].startswith("category "):
            assert list(cells[i + 1][1:6]) == header, f"row {i + 2}: unexpected header"
            balls, j = [], i + 2
            while j < len(cells) and not pd.isna(cells[j][1]):
                no, m, dm, d, dd = cells[j][1:6]
                balls.append({"no": int(no), "mass": float(m), "mass_res": float(dm),
                              "d": float(d), "d_res": float(dd)})
                j += 1
            out["categories"][int(r[1].split()[1])] = balls
    return out


def _num(v):
    """A cell as a float. Some cells are text with U+200E (left-to-right mark) around the
    sign and exponent, e.g. '‎-1.034445E0'; that character is the only non-numeric one."""
    if isinstance(v, str):
        v = v.replace("‎", "")
    return float(v)


def ball_track(n):
    """Sheet 'ball n': columns t, x, y (row 1 names the tracked point, row 2 the columns).
    Units are not stated in the sheet."""
    raw = pd.read_excel(XLSX, sheet_name=f"ball {n}", header=None)
    assert list(raw.iloc[1]) == ["t", "x", "y"], f"ball {n}: unexpected header {list(raw.iloc[1])}"
    data = raw.iloc[2:]
    return {"point": raw.iloc[0, 1], **{c: [_num(v) for v in data[k]] for k, c in enumerate("txy")}}


SQRT12 = np.sqrt(12)


def group_mean(values, res):
    """Mean of one group's 3 measurements and its error: statistical, booklet (32)+(34), and
    resolution, booklet (28), combined by booklet (35). Plan, part a."""
    v = np.asarray(values, dtype=float)
    stat = v.std(ddof=1) / np.sqrt(len(v))
    return float(v.mean()), float(np.hypot(stat, res / SQRT12)), float(stat)


def part_a_stats(A):
    """Per group: m, d (mm -> cm), r = d/2 +- dd/2 (7), V +- dV (8). Units: g, cm, cm^3."""
    groups = {}
    for n, balls in sorted(A["categories"].items()):
        m, dm, m_stat = group_mean([b["mass"] for b in balls], balls[0]["mass_res"])
        d, dd, d_stat = group_mean([b["d"] / 10 for b in balls], balls[0]["d_res"] / 10)
        r, dr = d / 2, dd / 2
        V, dV = 4 / 3 * np.pi * r**3, 4 * np.pi * r**2 * dr
        groups[n] = dict(m=m, dm=dm, m_stat=m_stat, d=d, dd=dd, d_stat=d_stat, r=r, dr=dr, V=V, dV=dV)
    return groups


def run_fit(fit_func, guesses, x, dx, y, dy):
    params, errors, _, output = odr_fit(fit_func, guesses, x, dx, y, dy)
    residuals, dof, chi2_red, p_val = calc_stats(fit_func, x, y, params, output)
    return {"params": params.tolist(), "errors": errors.tolist(), "chi2_red": float(chi2_red),
            "p": float(p_val), "dof": int(dof), "residuals": np.asarray(residuals).tolist()}


def density_fit(groups):
    """Fit (10) of m against V over the 6 groups; rho_b = a1 +- da1 (11). The initial slope is
    the data's own m/V ratio, so no outside value enters."""
    x = np.array([g["V"] for g in groups.values()]); dx = np.array([g["dV"] for g in groups.values()])
    y = np.array([g["m"] for g in groups.values()]); dy = np.array([g["dm"] for g in groups.values()])
    res = run_fit(linear, [0.0, float(y.sum() / x.sum())], x, dx, y, dy)
    res.update(x=x.tolist(), dx=dx.tolist(), y=y.tolist(), dy=dy.tolist())
    return res


# ---------- figures (Colab template style; title inside the plot, rules 6.1) ----------

def plot_fit(res, title, xlabel, ylabel, path):
    x, dx, y, dy = (np.asarray(res[k]) for k in ("x", "dx", "y", "dy"))
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    x_fit = np.linspace(min(x), max(x), 200)
    ax.errorbar(x, y, xerr=dx, yerr=dy, fmt=".b", ecolor="gray", label="data")
    ax.plot(x_fit, linear(res["params"], x_fit), c="r", alpha=0.6, label="linear fit")
    ax.set_title(title); ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    ax.grid(True); ax.legend(); fig.tight_layout(); fig.savefig(path); plt.close(fig)


def plot_residuals(res, title, xlabel, ylabel, path):
    x, dx, dy = (np.asarray(res[k]) for k in ("x", "dx", "dy"))
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    ax.errorbar(x, res["residuals"], xerr=dx, yerr=dy, fmt=".b", ecolor="gray", label="residuals")
    ax.hlines(0, min(x), max(x), colors="r", linestyles="dashed")
    ax.set_title(title); ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    ax.grid(True); ax.legend(); fig.tight_layout(); fig.savefig(path); plt.close(fig)


def macros(results):
    """Every reported value as LaTeX, already rounded: {macro name (letters only): string}."""
    return {}


def main():
    FIGURES.mkdir(exist_ok=True)
    A = part_a()
    assert sorted(A["categories"]) == list(range(1, 7)), sorted(A["categories"])
    assert all(len(b) == 3 for b in A["categories"].values())
    tracks = {n: ball_track(n) for n in range(1, N_TRACKS + 1)}
    groups = part_a_stats(A)
    dens = density_fit(groups)
    rho_l, drho_l = A["rho"]["value"], A["rho"]["res"] / SQRT12  # booklet (28)
    plot_fit(dens, "Ball mass vs volume", r"$V$ [cm$^3$]", r"$m$ [g]", FIGURES / "density-fit.pdf")
    plot_residuals(dens, "Residuals: mass vs volume", r"$V$ [cm$^3$]", r"$m - f(V)$ [g]",
                   FIGURES / "density-res.pdf")
    results = {"part_a": A, "groups": groups, "density_fit": dens,
               "rho_l": rho_l, "drho_l": drho_l,
               "tracks_n_rows": {n: len(t["t"]) for n, t in tracks.items()}}
    write_numbers(macros(results), REPORT / "numbers.tex")
    (HERE / "results.json").write_text(json.dumps(results, indent=2))
    print(f"read: density, {len(A['categories'])} categories x 3 balls, "
          f"{N_TRACKS} tracks ({', '.join(str(len(t['t'])) for t in tracks.values())} rows)")


if __name__ == "__main__":
    main()
