# Shared by every experiment's Makefile: `include ../common.mk` at the top.
# LAB_ROOT is this folder, found from the include itself, so it works from any experiment.
LAB_ROOT := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

# One venv for the whole lab, built from $(LAB_ROOT)/requirements.txt (see the comment there).
PY := $(LAB_ROOT)/.venv/bin/python -W ignore::DeprecationWarning

# The shared Python package: a change there reruns every experiment's analysis.
LABTOOLS := $(wildcard $(LAB_ROOT)/labtools/*.py)

# Rule lint (labtools/lint_report.py), run before LaTeX: stops the build on a broken report rule.
# Each experiment sets FORMULA_LIMIT (Moodle). `make FINAL=1` also fails on blue/red left in.
LINT = $(PY) -m labtools.lint_report $(CURDIR)/report/main.tex --limit $(FORMULA_LIMIT) $(if $(FINAL),--final)
