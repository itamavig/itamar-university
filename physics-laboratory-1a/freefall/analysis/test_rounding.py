"""Check analysis.py's rounding against the data booklet's own examples (p.24-25).

Rules (booklet "עיגול ספרות"):
  - value with error: error to 2 significant figures, value to the same decimal place
  - value without error (relative error, chi2_red, p-value, N_sigma): 2 significant figures
Each case below is copied from booklet Table 3 ("original" -> "rounded").
"""
import sys

from analysis import round_2sf, round_pair, tex_number

TABLE_3 = [
    # (value, error, expected value, expected error)
    ("95432", "4520", "95400", "4500"),
    ("0.012844", "0.00683", "0.0128", "0.0068"),
    ("29541.91", "429", "29540", "430"),
    ("1301750", "48401.06", "1302000", "48000"),
    ("57.3121", "0.965", "57.31", "0.97"),
    ("8.72713", "0.94", "8.73", "0.94"),
    ("9842000", "45881", "9842000", "46000"),
    ("67210", "880", "67210", "880"),
    ("0.37311", "0.005013", "0.3731", "0.0050"),
    ("90130", "0.458", "90130.00", "0.46"),
    ("4.9164", "0.06", "4.916", "0.060"),
    ("6342", "48220", "6000", "48000"),
    # Booklet prints "0 ± 57000" here, which contradicts its own rule: rounding 734 to the
    # thousands digit drops a 7 (>= 5), so the rule gives 1000. We follow the stated rule.
    ("734", "56941", "1000", "57000"),
    ("1.43981", "0.0762", "1.440", "0.076"),
    ("999963", "2183", "1000000", "2200"),
    ("0.411607", "0.00996", "0.412", "0.010"),
]

# Values written without an error: 2 significant figures (booklet p.24 examples).
NO_ERROR = [
    ("623.84", "620"),
    ("0.0917", "0.092"),
]


def main():
    failures = 0
    for v, e, want_v, want_e in TABLE_3:
        got_v, got_e = round_pair(float(v), float(e))
        ok = (got_v, got_e) == (want_v, want_e)
        failures += not ok
        print(f"{'OK ' if ok else 'BAD'} {v} ± {e:10} booklet={want_v} ± {want_e:8} ours={got_v} ± {got_e}")
    for v, want in NO_ERROR:
        got = tex_number(round_2sf(float(v)))
        ok = got == want
        failures += not ok
        print(f"{'OK ' if ok else 'BAD'} {v:22} booklet={want:18} ours={got}")
    print("ROUNDING MATCHES THE BOOKLET" if failures == 0 else f"{failures} MISMATCH(ES)")
    sys.exit(failures != 0)


if __name__ == "__main__":
    main()
