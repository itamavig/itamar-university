"""Code shared by every experiment in physics-laboratory-1a.

  rounding.py       -- course rounding (data booklet p.24) and the LaTeX it produces, numbers.tex writer
  fit.py            -- ODR fit and fit statistics, as in the course Colab notebooks
  colab.py          -- comparing the report's rounded values with Colab's
  test_rounding.py  -- rounding.py against the booklet's Table 3; run as `python -m labtools.test_rounding`

Experiment scripts live two levels down (<experiment>/analysis/*.py) and put the lab root on
sys.path before importing from here:

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # lab root, for labtools
"""
