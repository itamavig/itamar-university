"""Comparing the report's values with the course Colab notebook's.

Standard (user decision 2026-10-26, free fall): every value the report prints must equal
Colab's after course rounding. Unrounded values can't match bit for bit (ODR stops at a
machine-dependent point). Each experiment's verify_colab.py gets Colab's results its own way,
runs both sides through its own macros(), and passes the two {macro name: LaTeX} dicts here.
"""


def compare_macros(ours, colab, keys):
    """The keys, in the given order, whose rounded value differs between ours and Colab's."""
    return [k for k in keys if ours[k] != colab[k]]
