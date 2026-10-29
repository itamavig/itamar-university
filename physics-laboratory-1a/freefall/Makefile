# `make` reruns the fits, checks them against Colab, then builds report/main.pdf.
PY := .venv/bin/python -W ignore::DeprecationWarning
.DEFAULT_GOAL := report/main.pdf

# Shared Drive folder "Physics Laboratory 1a" (synced by Google Drive for desktop via a shortcut).
# Found by folder ID in the shell, since the name has spaces (Make's wildcard splits on them).
DRIVE_IDDIR := $(HOME)/Library/CloudStorage/GoogleDrive-avigdori@mail.tau.ac.il/.shortcut-targets-by-id/1JX-zH0bAuzjteWiRRvmfPnFxpX9OWTHd

# raw_table.tex is written by the same analysis.py run that writes numbers.tex.
report/raw_table.tex: report/numbers.tex

report/main.pdf: report/numbers.tex report/raw_table.tex report/*.tex
	cd report && latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
	@d=$$(ls -d "$(DRIVE_IDDIR)"/*/ 2>/dev/null | head -1); \
	  test -n "$$d" || { echo "Drive folder not found: is Google Drive for desktop running and signed in?"; exit 1; }; \
	  cp report/main.pdf "$${d}freefall-report.pdf" && echo "uploaded to Drive: $${d}freefall-report.pdf"

report/numbers.tex: analysis/analysis.py analysis/verify_colab.py analysis/test_rounding.py FreeFall_19-10-2026_14-30-49.xlsx
	cd analysis && ../$(PY) test_rounding.py
	$(PY) analysis/analysis.py
	$(PY) analysis/verify_colab.py

# Re-download the shared Doc, merge new/changed units into doc/ledger.tsv, report coverage.
doc:
	$(PY) analysis/doc_ledger.py fetch
	$(PY) analysis/doc_ledger.py sync
	$(PY) analysis/doc_ledger.py check

clean:
	cd report && latexmk -C main.tex

.PHONY: clean doc
