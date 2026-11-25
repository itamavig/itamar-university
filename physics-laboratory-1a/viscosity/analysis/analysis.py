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
import fitz  # pymupdf: renders the briefing's appendix graph to read eta_theo
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
G, DG = 981.0, 10.0          # cm/s^2, instructor (Ran, 2026-11-23)
RULER_RES = 0.1              # cm, ruler resolution (user, 2026-11-22); dy = RULER_RES/sqrt(12) (Ran, 2026-11-22)
FRAME_DT = 1 / 30            # s, frame interval; dt = FRAME_DT/sqrt(12) (user, 2026-11-23)
SCALE = {1: 1.0, 2: 1.0, 3: 21.0, 4: 21.0, 5: 21.0, 6: 21.0}   # balls 3-6: y x 21 (Ran, 2026-11-21)
# Fit region per ball, first and last frame index (inclusive), read by eye from the v(t) graph
# (analysis/review/region-check.png); Claude's readings, adopted by the user 2026-11-23.
# Starts of balls 4-6 moved later (user, 2026-11-24, after Ran: residuals up to 3 sigma are normal,
# the speed is constant from some point on): while the first residuals of the fit are beyond 3 sigma
# (sigma = sqrt(dy^2 + (a1 dt)^2)), the start moves past them and the fit is redone, until none are.
# 4: 50 -> 53, 5: 45 -> 77 -> 95 -> 103 -> 106 -> 107, 6: 75 -> 96 -> 104 -> 108 -> 110.
# check_regions() asserts the result, so the numbers cannot go stale.
REGIONS = {1: (40, 171), 2: (50, 206), 3: (100, 248), 4: (53, 300), 5: (107, 395), 6: (110, 500)}
VISUAL_STARTS = {1: 40, 2: 50, 3: 100, 4: 50, 5: 45, 6: 75}   # starts as first read by eye (reported in the results)
MIN_POINTS = 50              # instructor (via the user, 2026-11-22)


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


def part_b_ball(n, track):
    """Times from the first tracked frame; heights in cm; v_i (12), dv_i (13); fit (10) of y
    against t over the region; v_f = -a1 +- da1 (14)."""
    t = np.asarray(track["t"], float); t = t - t[0]
    y = np.asarray(track["y"], float) * SCALE[n]
    dy, dt = RULER_RES / SQRT12, FRAME_DT / SQRT12
    T = t[2:] - t[:-2]
    v = -(y[2:] - y[:-2]) / T
    dv = np.sqrt(2 * dy**2 + v**2 * 2 * dt**2) / T
    i0, i1 = REGIONS[n]
    sel = slice(i0, i1 + 1)
    x, yy = t[sel], y[sel]
    assert len(x) >= MIN_POINTS, (n, len(x))
    slope0 = float((yy[-1] - yy[0]) / (x[-1] - x[0]))
    res = run_fit(linear, [float(yy[0] - slope0 * x[0]), slope0], x, np.full_like(x, dt), yy, np.full_like(yy, dy))
    res.update(x=x.tolist(), dx=[dt] * len(x), y=yy.tolist(), dy=[dy] * len(x))
    vf, dvf = -res["params"][1], res["errors"][1]
    return {"fit": res, "vf": float(vf), "dvf": float(dvf), "region": [i0, i1], "n_points": len(x),
            "t_region": [float(x[0]), float(x[-1])], "n_frames": len(t),
            "v": v.tolist(), "dv": dv.tolist(), "t_v": t[1:-1].tolist()}


def check_regions(balls):
    """No fit starts with a residual beyond 3 sigma (Ran, 2026-11-24); see REGIONS."""
    for n, b in balls.items():
        f = b["fit"]
        sigma = np.hypot(f["dy"][0], f["params"][1] * f["dx"][0])
        assert abs(f["residuals"][0]) <= 3 * sigma, f"ball {n}: first residual beyond 3 sigma, region start stale"


def viscosity_fit(groups, balls, rho_b, drho_b, rho_l, drho_l):
    """Fit (10) of v_f against r^2 (x error (14)); eta from the slope (15), in poise."""
    ns = sorted(balls)
    r = np.array([groups[n]["r"] for n in ns]); dr = np.array([groups[n]["dr"] for n in ns])
    x, dx = r**2, 2 * r * dr
    y = np.array([balls[n]["vf"] for n in ns]); dy = np.array([balls[n]["dvf"] for n in ns])
    res = run_fit(linear, [0.0, float(y.sum() / x.sum())], x, dx, y, dy)
    res.update(x=x.tolist(), dx=dx.tolist(), y=y.tolist(), dy=dy.tolist())
    a1, da1 = res["params"][1], res["errors"][1]
    eta = 2 * G * (rho_b - rho_l) / (9 * a1)
    deta = eta * np.sqrt((da1 / a1) ** 2 + (drho_b**2 + drho_l**2) / (rho_b - rho_l) ** 2 + (DG / G) ** 2)
    res.update(eta=float(eta), deta=float(deta))
    return res


T_GLYCERIN, DT_GLYCERIN = 23.116, 0.031     # deg C, group member's Capstone mean (approved by Ran)
BRIEFING = ROOT / "תדריך עבודה צמיגות תשפז.pdf"
# Reading error of eta_th: a direct estimate, not a resolution. Ran, 2026-11-25: draw straight lines
# and estimate as accurately as possible, there is no set resolution, it is an estimate. +-100 cP
# chosen by the user 2026-11-25; replaces the 500 cP grid / 100 cP eye versions (todo 10a).
READ_ERR_CP = 100.0
AXIS_X = 440                           # px at 300 dpi: the eta axis (left edge of the plot)
GRAPH_CROP = (300, 650, 2150, 2300)    # px at 300 dpi: the plot with its axis labels


def draw_reading(pix, x_T, y_curve, y_zero, path):
    """The briefing graph (p.9) with the reading drawn as straight lines (Ran, 2026-11-25): up from
    T on the temperature axis to the curve, then across to the viscosity axis."""
    from PIL import Image, ImageDraw
    img = Image.frombytes("L", (pix.width, pix.height), pix.samples).convert("RGB")
    d = ImageDraw.Draw(img)
    d.line([(x_T, y_zero), (x_T, y_curve)], fill=(220, 0, 0), width=5)
    d.line([(x_T, y_curve), (AXIS_X, y_curve)], fill=(220, 0, 0), width=5)
    img.crop(GRAPH_CROP).save(path)


def theory_eta_cp(T, draw_to=None):
    """Read eta(T) in cP off the briefing's appendix graph (p.9), by pixels instead of by eye:
    render at 300 dpi, locate the solid gridlines (T = 5..30 deg C, eta = 0..6000 cP), map
    pixels to axes linearly, and take the curve's pixel in the column of T. Same reading every
    run. Pixel positions searched near the values found on 2026-11-23."""
    page = fitz.open(BRIEFING)[8]
    pix = page.get_pixmap(dpi=300, colorspace=fitz.csGRAY)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width).astype(float)

    def centre(c, axis):
        seg = a[700:2180, c - 8:c + 9].mean(0) if axis == "v" else a[c - 8:c + 9, 440:2080].mean(1)
        w = 255 - seg
        return float((w * np.arange(c - 8, c + 9)).sum() / w.sum())

    Ts, xs = zip(*[(T0, centre(c, "v")) for T0, c in [(5, 503), (10, 808), (15, 1110), (20, 1413), (25, 1715), (30, 2018)]])
    Es, ys = zip(*[(E0, centre(c, "h")) for E0, c in [(0, 2122), (2000, 1724), (4000, 1326), (6000, 929)]])
    kx, bx = np.polyfit(Ts, xs, 1)
    ky, by = np.polyfit(Es, ys, 1)
    assert max(abs(np.array(xs) - (kx * np.array(Ts) + bx))) < 2 and max(abs(np.array(ys) - (ky * np.array(Es) + by))) < 2
    c = int(round(kx * T + bx))
    rows = np.arange(int(ky * 2000 + by) + 5, int(by) - 10)
    col = a[rows[0]:rows[-1] + 1, c - 1:c + 2].min(1)
    grid = [ky * e + by for e in range(0, 2001, 500)]
    curve = [r for r, v in zip(rows, col) if v < 120 and min(abs(r - g) for g in grid) > 4]
    assert curve and max(curve) - min(curve) < 8, curve   # one thin curve crossing, not a gridline
    if draw_to:
        draw_reading(pix, c, float(np.mean(curve)), by, draw_to)
    return float((np.mean(curve) - by) / ky)


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


def plot_track(n, track, region, path):
    """Whole track of ball n, first frame to last (user, 2026-11-24), with the fit region shaded.
    Same units as the fits: t from the first frame, y in cm (balls 3-6 scaled)."""
    t = np.asarray(track["t"], float); t = t - t[0]
    y = np.asarray(track["y"], float) * SCALE[n]
    i0, i1 = region
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    ax.axvspan(t[i0], t[i1], color="orange", alpha=0.2, label="fit region")
    ax.plot(t, y, ".b", ms=2, label="all frames")
    ax.set_title(f"Ball {n}: full track"); ax.set_xlabel(r"$t$ [s]"); ax.set_ylabel(r"$y$ [cm]")
    ax.grid(True); ax.legend(); fig.tight_layout(); fig.savefig(path); plt.close(fig)


def plot_track_residuals(n, track, b, path):
    """Residuals of the whole track from the region's fit line, extended over all frames
    (user, 2026-11-24), with the fit region shaded."""
    t = np.asarray(track["t"], float); t = t - t[0]
    y = np.asarray(track["y"], float) * SCALE[n]
    i0, i1 = b["region"]
    r = y - linear(b["fit"]["params"], t)
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    ax.axvspan(t[i0], t[i1], color="orange", alpha=0.2, label="fit region")
    ax.plot(t, r, ".b", ms=2, label="residuals")
    ax.axhline(0, color="r", ls="dashed")
    # y-axis: the residual range inside the region, padded by that range on each side, so the
    # entry frames (residuals up to ~10 cm) do not flatten the rest; they run off the top.
    rin = r[i0:i1 + 1]; span = rin.max() - rin.min()
    ax.set_ylim(rin.min() - span, rin.max() + span)
    ax.set_title(f"Ball {n}: full-track residuals"); ax.set_xlabel(r"$t$ [s]"); ax.set_ylabel(r"$y - f(t)$ [cm]")
    ax.grid(True); ax.legend(); fig.tight_layout(); fig.savefig(path); plt.close(fig)


def macros(results):
    """Every reported value as LaTeX, already rounded: {macro name (letters only): string}."""
    out = {}
    d, v = results["density_fit"], results["viscosity_fit"]
    for tag, res in (("Dens", d), ("Vf", v)):
        for k, word in enumerate(("Zero", "One")):
            out[f"{tag}A{word}"] = tex_pm(res["params"][k], res["errors"][k])
            out[f"{tag}A{word}Rel"] = tex_rel(res["params"][k], res["errors"][k])
        out[f"{tag}Chi"] = tex_number(round_2sf(res["chi2_red"]))
        out[f"{tag}P"] = tex_number(round_2sf(res["p"]))
    out["RhoB"], out["RhoBRel"] = tex_pm(d["params"][1], d["errors"][1]), tex_rel(d["params"][1], d["errors"][1])
    out["RhoL"], out["RhoLRel"] = tex_pm(results["rho_l"], results["drho_l"]), tex_rel(results["rho_l"], results["drho_l"])
    out["Eta"], out["EtaRel"] = tex_pm(v["eta"], v["deta"]), tex_rel(v["eta"], v["deta"])
    out["EtaTh"], out["EtaThRel"] = tex_pm(v["eta_th"], v["deta_th"]), tex_rel(v["eta_th"], v["deta_th"])
    out["NSigma"] = tex_number(round_2sf(v["n_sigma"]))
    out["ReadErrCP"] = f"{READ_ERR_CP:.0f}"
    out["TGly"] = tex_pm(T_GLYCERIN, DT_GLYCERIN)
    out["VisStartFour"], out["StartFour"] = str(VISUAL_STARTS[4]), str(REGIONS[4][0])
    out["VisStartFive"], out["StartFive"] = str(VISUAL_STARTS[5]), str(REGIONS[5][0])
    out["VisStartSix"], out["StartSix"] = str(VISUAL_STARTS[6]), str(REGIONS[6][0])
    assert [n for n in REGIONS if REGIONS[n][0] != VISUAL_STARTS[n]] == [4, 5, 6], "moved starts changed: revise the results text"
    out["TGlyRel"] = tex_rel(T_GLYCERIN, DT_GLYCERIN)
    out["GValue"] = tex_pm(G, DG)
    # Group 1's mass error stands out in the density fit (user, 2026-11-23): report it against the
    # largest of the other groups'. The assert keeps the text true if the data change.
    g = results["groups"]
    others = max(g[n]["dm"] for n in g if n != 1)
    assert g[1]["dm"] > 2 * others, "group 1's mass error no longer stands out: revise the results text"
    out["DmGroupOne"] = tex_number(round_2sf(g[1]["dm"]))
    out["DmOthersMax"] = tex_number(round_2sf(others))
    return out


def write_ball_table(balls, path):
    """Per-ball fit results (body): region, points, v_f, relative error, chi2_red, p."""
    rows = []
    for n, b in sorted(balls.items()):
        f = b["fit"]
        rows.append(rf"    {n} & \textenglish{{{b['region'][0]}--{b['region'][1]}}} & {b['n_points']} & ${tex_pm(b['vf'], b['dvf'])}$ & "
                    rf"${tex_rel(b['vf'], b['dvf'])}$ & ${tex_number(round_2sf(f['chi2_red']))}$ & ${tex_number(round_2sf(f['p']))}$ \\ \hline")
    path.write_text("% Generated by analysis/analysis.py -- do not edit by hand.\n" + "\n".join(rows) + "%\n", encoding="utf-8")  # % : no empty row after \input


def write_group_table(groups, path):
    """Per-group means and errors (appendix): m, d, r, V with errors."""
    rows = []
    for n, g in sorted(groups.items()):
        rows.append(rf"    {n} & ${tex_pm(g['m'], g['dm'])}$ & ${tex_pm(g['d'], g['dd'])}$ & ${tex_pm(g['r'], g['dr'])}$ & ${tex_pm(g['V'], g['dV'])}$ \\ \hline")
    path.write_text("% Generated by analysis/analysis.py -- do not edit by hand.\n" + "\n".join(rows) + "%\n", encoding="utf-8")  # % : no empty row after \input


def write_raw_table(A, path):
    """Raw part-a measurements (appendix, rules 4.5.2): unrounded, as recorded."""
    rows = []
    for n, balls in sorted(A["categories"].items()):
        for b in balls:
            rows.append(rf"    {n} & {b['no']} & ${b['mass']:.3f}$ & ${b['d']:.3f}$ \\ \hline")
    path.write_text("% Generated by analysis/analysis.py -- do not edit by hand.\n" + "\n".join(rows) + "%\n", encoding="utf-8")  # % : no empty row after \input


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
    balls = {n: part_b_ball(n, tracks[n]) for n in range(1, N_TRACKS + 1)}
    check_regions(balls)
    rho_b, drho_b = dens["params"][1], dens["errors"][1]
    visc = viscosity_fit(groups, balls, rho_b, drho_b, rho_l, drho_l)
    eta_th = theory_eta_cp(T_GLYCERIN, draw_to=FIGURES / "eta-reading.png") / 100   # P
    deta_th = READ_ERR_CP / 100                          # P, direct estimate (see READ_ERR_CP)
    n_sigma = abs(visc["eta"] - eta_th) / np.hypot(visc["deta"], deta_th)   # booklet (51)
    assert n_sigma < 3, "N_sigma >= 3: revise the results text"
    visc.update(eta_th=eta_th, deta_th=deta_th, n_sigma=float(n_sigma))
    plot_fit(visc, "Terminal velocity vs radius squared", r"$r^2$ [cm$^2$]", r"$v_f$ [cm/s]", FIGURES / "vf-fit.pdf")
    plot_residuals(visc, "Residuals: terminal velocity vs radius squared", r"$r^2$ [cm$^2$]",
                   r"$v_f - f(r^2)$ [cm/s]", FIGURES / "vf-res.pdf")
    for n, b in balls.items():
        plot_track(n, tracks[n], b["region"], FIGURES / f"ball{n}-track.pdf")
        plot_track_residuals(n, tracks[n], b, FIGURES / f"ball{n}-track-res.pdf")
        plot_fit(b["fit"], f"Ball {n}: height vs time (fit region)", r"$t$ [s]", r"$y$ [cm]", FIGURES / f"ball{n}-fit.pdf")
        plot_residuals(b["fit"], f"Ball {n}: residuals", r"$t$ [s]", r"$y - f(t)$ [cm]", FIGURES / f"ball{n}-res.pdf")
    results = {"part_a": A, "groups": groups, "density_fit": dens,
               "rho_l": rho_l, "drho_l": drho_l, "balls": balls, "viscosity_fit": visc,
               "tracks_n_rows": {n: len(t["t"]) for n, t in tracks.items()}}
    write_numbers(macros(results), REPORT / "numbers.tex")
    write_ball_table(balls, REPORT / "ball_table.tex")
    write_group_table(groups, REPORT / "group_table.tex")
    write_raw_table(A, REPORT / "raw_table.tex")
    (HERE / "results.json").write_text(json.dumps(results, indent=2))
    print(f"read: density, {len(A['categories'])} categories x 3 balls, "
          f"{N_TRACKS} tracks ({', '.join(str(len(t['t'])) for t in tracks.values())} rows)")


if __name__ == "__main__":
    main()
