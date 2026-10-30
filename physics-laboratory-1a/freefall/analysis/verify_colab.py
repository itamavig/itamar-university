"""Check analysis.py against the outputs printed in the Colab notebooks.

Standard (user decision 2026-10-26): every value the report prints must equal
Colab's after course rounding. Both sides go through the same macros() from
analysis.py. Unrounded values differ around the 7th significant digit because
ODR stops at its default tolerance at a machine-dependent point; the largest
relative difference is printed for information only.

Expected values are read from the saved .ipynb outputs, not typed by hand.
"""
import json
import re
import sys
from pathlib import Path

from analysis import G_THEO, G_THEO_ERR, macros

HERE = Path(__file__).resolve().parent
COLAB = HERE.parent / "colab"


def colab_text(name):
    nb = json.loads((COLAB / name).read_text())
    out = []
    for cell in nb["cells"]:
        for o in cell.get("outputs", []):
            out.append("".join(o.get("text", "")))
            out.append("".join(o.get("data", {}).get("text/plain", "")))
    return "\n".join(out)


def colab_results(name, g_index):
    """Colab's printed outputs in the same shape as results.json."""
    text = colab_text(name)
    params = re.findall(r"a\[(\d)\]: (\S+) ± (\S+) \(", text)
    params = sorted((int(i), float(v), float(e)) for i, v, e in params)
    a = [v for _, v, _ in params]
    da = [e for _, _, e in params]
    # Same formulas as the notebooks' g / N_sigma cells (the linear one doesn't print g).
    g, g_err = 2 * a[g_index], 2 * da[g_index]
    n_sigma = (abs(g - G_THEO) / (g_err**2 + G_THEO_ERR**2) ** 0.5)
    printed_n_sigma = float(re.findall(r"np\.float64\((\S+)\)", text)[-1])
    assert abs(n_sigma - printed_n_sigma) < 1e-12, "N_sigma formula differs from the notebook"
    return {"params": a, "errors": da,
            "chi2_red": float(re.search(r"Chi Squared Reduced = (\S+)", text).group(1)),
            "p": float(re.search(r"P-value = (\S+)", text).group(1)),
            "g": g, "g_err": g_err, "n_sigma": n_sigma}


def max_rel_diff(ours, theirs):
    pairs = list(zip(ours["params"] + ours["errors"] + [ours["g"], ours["g_err"]],
                     theirs["params"] + theirs["errors"] + [theirs["g"], theirs["g_err"]]))
    return max(abs(a - b) / abs(b) for a, b in pairs)


def main():
    ours = json.loads((HERE / "results.json").read_text())
    colab = {"linear": colab_results("freefall_experiment_linear.ipynb", g_index=1),
             "parabolic": colab_results("freefall_experiment_parabolic.ipynb", g_index=2)}

    m_ours = macros(ours["linear"], ours["parabolic"])
    m_colab = macros(colab["linear"], colab["parabolic"])
    failures = 0
    # Macros from our own refits have no Colab counterpart; they're listed, not compared.
    only_ours = sorted(set(m_ours) - set(m_colab))
    for key in sorted(set(m_ours) & set(m_colab), key=list(m_ours).index):
        ok = m_ours[key] == m_colab[key]
        failures += not ok
        print(f"{'OK ' if ok else 'BAD'} {key:14} colab={m_colab[key]:24} local={m_ours[key]}")

    for fit in ("linear", "parabolic"):
        print(f"info: {fit} largest unrounded relative difference = "
              f"{max_rel_diff(ours[fit], colab[fit]):.1e}")
    if only_ours:
        print("not in Colab (local refits/estimates): " + ", ".join(only_ours))
    print("ALL REPORTED VALUES MATCH" if failures == 0 else f"{failures} MISMATCH(ES)")
    sys.exit(failures != 0)


if __name__ == "__main__":
    main()
