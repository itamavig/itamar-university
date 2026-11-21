# `make` reruns the analysis (numbers.tex, figures), checks it against Colab, then builds report/main.pdf.
include ../common.mk
.DEFAULT_GOAL := report/main.pdf

# a_table.tex is written by the same analysis.py run that writes numbers.tex.
report/a_table.tex report/raw_a.tex report/raw_b.tex report/raw_c.tex: report/numbers.tex

report/main.pdf: report/numbers.tex report/a_table.tex report/raw_a.tex report/raw_b.tex report/raw_c.tex report/*.tex
	cd report && latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex

report/numbers.tex: analysis/analysis.py analysis/verify_colab.py $(LABTOOLS) colab/colab_outputs.json heat\ conduction\ part\ a.xlsx heat\ conduction\ part\ b.xlsx
	cd $(LAB_ROOT) && $(PY) -m labtools.test_rounding
	$(PY) analysis/analysis.py
	$(PY) analysis/verify_colab.py

clean:
	cd report && latexmk -C main.tex

.PHONY: clean
