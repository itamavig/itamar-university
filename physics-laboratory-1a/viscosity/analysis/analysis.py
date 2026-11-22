"""Viscosity analysis. So far: reads the raw data; no analysis yet.

Fit code (odr_fit, calc_stats, linear) and the course rounding come from ../../labtools/.

Outputs (paths relative to this file):
  ../report/numbers.tex  -- one \\newcommand per reported value, already rounded
  results.json           -- unrounded values (read by verify_colab.py, once there is one)
"""
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # lab root, for labtools
from labtools.fit import calc_stats, linear, odr_fit  # noqa: F401  (used once the fits exist)
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


def macros(results):
    """Every reported value as LaTeX, already rounded: {macro name (letters only): string}."""
    return {}


def main():
    FIGURES.mkdir(exist_ok=True)
    A = part_a()
    assert sorted(A["categories"]) == list(range(1, 7)), sorted(A["categories"])
    assert all(len(b) == 3 for b in A["categories"].values())
    tracks = {n: ball_track(n) for n in range(1, N_TRACKS + 1)}
    results = {"part_a": A, "tracks_n_rows": {n: len(t["t"]) for n, t in tracks.items()}}
    write_numbers(macros(results), REPORT / "numbers.tex")
    (HERE / "results.json").write_text(json.dumps(results, indent=2))
    print(f"read: density, {len(A['categories'])} categories x 3 balls, "
          f"{N_TRACKS} tracks ({', '.join(str(len(t['t'])) for t in tracks.values())} rows)")


if __name__ == "__main__":
    main()
