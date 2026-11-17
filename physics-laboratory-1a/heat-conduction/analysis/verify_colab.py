"""Check analysis.py's part-b fits against the Colab run of the course template.

Standard (as in free fall, user decision 2026-10-26): every value the report prints must
equal Colab's after course rounding. Both sides go through the same macros() from
analysis.py; kappa and the slope N_sigma are recomputed from Colab's slopes.
Colab's printed outputs are in ../colab/colab_outputs.json (transcribed 2026-11-09).
"""
import copy
import json
import sys
from pathlib import Path

from analysis import kappa_from_fit, macros, part_a, part_b, part_c, p_avg, p_avg_err
import numpy as np

HERE = Path(__file__).resolve().parent
COLAB = json.loads((HERE.parent / "colab" / "colab_outputs.json").read_text())


def main():
    A_ = part_a()
    ours = part_b(A_)
    theirs = copy.deepcopy(ours)
    worst = 0.0
    for i, f in enumerate(theirs["fits"]):
        c = COLAB[str(i)]
        f["params"] = [c["a0"][0], c["a1"][0]]
        f["errors"] = [c["a0"][1], c["a1"][1]]
        f["chi2_red"], f["p"] = c["chi2_red"], c["p"]
        f.update(kappa_from_fit(f, A_))
        for k in ("params", "errors"):
            for a, b in zip(ours["fits"][i][k], f[k]):
                worst = max(worst, abs(a - b) / abs(b))
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        s1, e1 = theirs["fits"][i]["params"][1], theirs["fits"][i]["errors"][1]
        s2, e2 = theirs["fits"][j]["params"][1], theirs["fits"][j]["errors"][1]
        theirs["nsigma_slopes"][f"{i}{j}"] = float(abs(s1 - s2) / np.hypot(e1, e2))
    # Part c: Colab's three rates replace ours; P_avg and corrected kappa recomputed from them.
    C_ours = part_c(A_, ours)
    C_theirs = copy.deepcopy(C_ours)
    for k in ("cool", "heat", "exp"):
        c = COLAB["part_c"][k]
        f = C_theirs[k]
        f["params"], f["errors"] = [c["a0"][0], c["a1"][0]], [c["a0"][1], c["a1"][1]]
        f["chi2_red"], f["p"] = c["chi2_red"], c["p"]
        for kk in ("params", "errors"):
            for a, b in zip(C_ours[k][kk], f[kk]):
                worst = max(worst, abs(a - b) / abs(b))
    e, de = C_theirs["exp"]["params"][1], C_theirs["exp"]["errors"][1]
    cc, dc = C_theirs["cool"]["params"][1], C_theirs["cool"]["errors"][1]
    h, dh = C_theirs["heat"]["params"][1], C_theirs["heat"]["errors"][1]
    P_in = C_ours["P_in"]
    rel_VI = float(np.hypot(A_["V"]["err"] / A_["V"]["mean"], A_["I"]["err"] / A_["I"]["mean"]))
    P = p_avg(P_in, e, cc, h)
    dP = p_avg_err(P_in, P, rel_VI, e, de, cc, dc, h, dh)
    C_theirs["kappa"] *= P / C_ours["P_avg"]
    C_theirs["kappa_err"] = C_theirs["kappa"] * np.sqrt((C_ours["kappa_err"] / C_ours["kappa"]) ** 2
                                                        - (C_ours["P_avg_err"] / C_ours["P_avg"]) ** 2 + (dP / P) ** 2)
    C_theirs["P_avg"], C_theirs["P_avg_err"] = P, dP
    m_ours, m_theirs = macros(A_, ours, C_ours), macros(A_, theirs, C_theirs)
    bad = [k for k in m_ours if k[0] in "BC" and m_ours[k] != m_theirs[k]]
    n = sum(1 for k in m_ours if k[0] in "BC")
    for k in bad:
        print(f"MISMATCH {k}: ours {m_ours[k]}  colab {m_theirs[k]}")
    print(f"{n - len(bad)}/{n} part-b/c report values match Colab; largest relative difference "
          f"in a fit parameter or error: {worst:.1e}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
