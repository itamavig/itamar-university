# `make` reruns the analysis (numbers.tex, figures), then builds report/main.pdf.
# New experiment: `cp -R _template <experiment>` at the lab root, then set DATA below,
# XLSX in analysis/analysis.py, and the names in report/details.example.tex.
include ../common.mk
.DEFAULT_GOAL := report/main.pdf

# Numbered-formula limit from Moodle (theory formulas excluded, rules 3.1). Checked by $(LINT).
FORMULA_LIMIT := 

# Raw data as exported in the lab. Escape spaces with a backslash: my\ data.xlsx
DATA := measurements.xlsx

report/main.pdf: report/numbers.tex report/*.tex
	cd $(LAB_ROOT) && $(LINT)
	cd report && latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex

# Every file analysis.py writes besides numbers.tex (tables, raw_*.tex) goes here as well:
# report/raw_a.tex: report/numbers.tex   -- and into main.pdf's prerequisites.
# Once there is a Colab check, add analysis/verify_colab.py as a prerequisite and a third line
# `$(PY) analysis/verify_colab.py` (see ../freefall/ and ../heat-conduction/).
report/numbers.tex: analysis/analysis.py $(LABTOOLS) $(DATA)
	cd $(LAB_ROOT) && $(PY) -m labtools.test_rounding
	$(PY) analysis/analysis.py

clean:
	cd report && latexmk -C main.tex

.PHONY: clean
