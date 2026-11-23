# `make` reruns the analysis (numbers.tex, figures), then builds report/main.pdf.
# Made from ../_template/ (2026-11-21).
include ../common.mk
.DEFAULT_GOAL := report/main.pdf

# Numbered-formula limit from Moodle (theory formulas excluded, rules 3.1). Checked by $(LINT).
FORMULA_LIMIT := 18

# Raw data as exported in the lab. Escape spaces with a backslash: my\ data.xlsx
DATA := viscosity\ measurements.xlsx

report/ball_table.tex report/group_table.tex report/raw_table.tex: report/numbers.tex

report/main.pdf: report/numbers.tex report/ball_table.tex report/group_table.tex report/raw_table.tex report/*.tex
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
