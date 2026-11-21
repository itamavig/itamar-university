"""<Experiment> analysis: <what it computes>.

Fit code (odr_fit, calc_stats, linear) and the course rounding come from ../../labtools/.

Outputs (paths relative to this file):
  ../report/numbers.tex  -- one \\newcommand per reported value, already rounded
  results.json           -- unrounded values (read by verify_colab.py, once there is one)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # lab root, for labtools
from labtools.fit import calc_stats, linear, odr_fit  # noqa: F401  (used once the fits exist)
from labtools.rounding import round_2sf, tex_number, tex_pm, tex_rel, write_numbers  # noqa: F401

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
XLSX = ROOT / "measurements.xlsx"  # raw data as exported in the lab (same file as DATA in ../Makefile)
REPORT = ROOT / "report"
FIGURES = REPORT / "figures"


def macros(results):
    """Every reported value as LaTeX, already rounded: {macro name (letters only): string}."""
    return {}


def main():
    FIGURES.mkdir(exist_ok=True)
    results = {}
    write_numbers(macros(results), REPORT / "numbers.tex")
    (HERE / "results.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
