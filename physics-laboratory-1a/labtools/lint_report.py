"""Deterministic checks of a lab report's main.tex against ../report-rules.md.

Run by every experiment's `make` before LaTeX (user, 2026-11-22: rule adherence without
re-reading the rules file). Checks only rules that have a fixed pattern. The judgement rules
are in ../CLAUDE.md (the rules card).

    python -m labtools.lint_report <experiment>/report/main.tex --limit 18 [--final]

Exit code 1 if any check fails, so `make` stops before building the PDF.

Scope:
  - Only the text after \\begin{document} is checked. Comments and TikZ drawings are ignored.
  - The theory section (\\section*{רקע תיאורטי} up to the next \\section*) is staff text copied
    verbatim, so the language checks skip it. Its formulas are excluded from the formula limit
    (rules 3.1).
  - Suppress a check on one line with a comment on that line: `% lint-ok: <check>` (the user must
    have approved the exception; say why in the same comment).

Checks (rule numbers from report-rules.md):
  semicolon     2.4a  no ';' in Hebrew text
  p-value       2.4b  "p-value", never "ערך p"
  first-person  2.1   no first-person past verbs (ביצענו, מדדנו, ...)
  slash         3.4a  no slash fractions in math (units in \\U{} are fine)
  booklet       3.8   booklet formulas are cited, not written: \\sqrt{12}, a stat+other combination
                      under one \\sqrt, \\sqrt{N}, N_\\sigma = ..., \\chi^2 = ...
  cite          3.4/3.8 a hard-coded "(N)" after נוסחה/משוואה must name its source in the same
                      sentence (בחוברת / קובץ / תדריך); report formulas use \\eqref
  forward-ref   3.5   no \\eqref before the formula's \\label
  limit         3.1   numbered formulas outside the theory section <= --limit
  briefing-cite (user 2026-11-22) the briefing is cited in a footnote, never inline
  footnote-mark (user 2026-11-23) footnote marker after punctuation (standard convention)
  colours       2.4c  with --final: no \\added, \\TODO, \\flagged, \\partner left
"""
import argparse
import re
import sys

THEORY_HEADING = r"\section*{רקע תיאורטי}"
HEBREW = re.compile(r"[\u0590-\u05FF]")
FIRST_PERSON = ["ביצענו", "מדדנו", "הצבנו", "קיבלנו", "חישבנו", "השתמשנו", "מצאנו", "ראינו", "הפלנו", "צילמנו"]
NUMBERED_ENVS = ("equation", "align", "gather", "multline")


def strip_comment(line):
    """Text of a line without its % comment (an escaped \\% stays)."""
    m = re.search(r"(?<!\\)%", line)
    return line[: m.start()] if m else line


def suppressed(line, check):
    m = re.search(r"(?<!\\)%.*lint-ok:\s*([\w\- ,]+)", line)
    return bool(m) and check in [c.strip() for c in re.split(r"[ ,]+", m.group(1))]


def math_spans(text):
    """Contents of inline $...$ and \\[...\\] in one line of text."""
    return re.findall(r"\$([^$]*)\$", text) + re.findall(r"\\\[(.*?)\\\]", text)


def without_math(text):
    text = re.sub(r"\$[^$]*\$", " ", text)
    return re.sub(r"\\\[.*?\\\]", " ", text)


def lint(path, limit, final):
    lines = open(path, encoding="utf-8").read().split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip().startswith(r"\begin{document}"))
    except StopIteration:
        start = 0
    errors = []

    def err(i, check, msg):
        if not suppressed(lines[i], check):
            errors.append(f"{path}:{i + 1}: [{check}] {msg}")

    in_theory = False
    in_tikz = False
    env = None          # current display-math environment name, if inside one
    env_start = 0
    env_body = []
    labels = {}         # label -> line index
    numbered = 0
    for i in range(start, len(lines)):
        raw = lines[i]
        text = strip_comment(raw)
        s = text.strip()
        if s.startswith(r"\section*"):
            in_theory = s.startswith(THEORY_HEADING)
        # TikZ code is drawing commands, not report text: skip it entirely.
        if r"\begin{tikzpicture}" in text:
            in_tikz = True
        if in_tikz:
            if r"\end{tikzpicture}" in text:
                in_tikz = False
            continue

        # --- display math environments (collect the body, check it at \end) ---
        m = re.search(r"\\begin\{(" + "|".join(NUMBERED_ENVS) + r")(\*?)\}", text)
        if env is None and m:
            env, env_star, env_start, env_body = m.group(1), m.group(2), i, []
        if env is not None:
            env_body.append(text)
            for lab in re.findall(r"\\label\{([^}]*)\}", text):
                labels[lab] = i
            if re.search(r"\\end\{" + env + r"\*?\}", text):
                body = " ".join(env_body)
                if not env_star and not in_theory:
                    numbered += max(1, body.count(r"\\")) if env != "equation" else 1
                check_formula(body, env_start, err)
                env = None
            continue

        for lab in re.findall(r"\\label\{([^}]*)\}", text):
            labels[lab] = i
        for ref in re.findall(r"\\eqref\{([^}]*)\}", text):
            if ref not in labels:
                err(i, "forward-ref", f"\\eqref{{{ref}}} before its formula appears (or label missing)")

        for span in math_spans(text):
            check_formula(span, i, err)

        if final:
            for cmd in ("added", "TODO", "flagged", "partner"):
                if "\\" + cmd + "{" in text:
                    err(i, "colours", f"\\{cmd}{{...}} left in the final report")

        if in_theory:
            continue
        plain = without_math(text)
        if HEBREW.search(plain):
            if ";" in plain:
                err(i, "semicolon", "semicolon in Hebrew text: split the sentence or use a comma")
            for w in FIRST_PERSON:
                if w in plain:
                    err(i, "first-person", f"'{w}': use impersonal phrasing")
        no_notes = re.sub(r"\\(footnote|TODO)\{[^{}]*(\{[^{}]*\}[^{}]*)*\}", " ", plain)
        if "תדריך" in no_notes:
            err(i, "briefing-cite", "cite the briefing in a \\footnote{תדריך הניסוי, עמ׳ N.}, not inline")
        if re.search(r"\\footnote\{(?:[^{}]|\{[^{}]*\})*\}[.,:]", text):
            err(i, "footnote-mark", "footnote marker goes after the punctuation: word,\\footnote{...}, not word\\footnote{...},")
        if re.search(r"ערך[\s\-־]*p\b", plain):
            err(i, "p-value", "write \\textenglish{p-value}, not 'ערך p'")
        for sentence in re.split(r"(?<=\.)\s", plain):
            for mm in re.finditer(r"(נוסח|משווא)\S*\s+\((\d+)\)", sentence):
                if not re.search(r"בחוברת|קובץ|תדריך", sentence):
                    err(i, "cite", f"hard-coded '({mm.group(2)})': name its source (בחוברת / קובץ / תדריך), or use \\eqref for a report formula")

    if numbered > limit:
        errors.append(f"{path}: [limit] {numbered} numbered formulas outside the theory section, limit {limit}")
    return errors, numbered


def check_formula(math, i, err):
    m = re.sub(r"\\U\{[^}]*\}", " ", math)                      # units may use slashes
    m = re.sub(r"\\(mathrm|text|textenglish)\{[^}]*\}", " ", m)
    m = re.sub(r"\^\{\d+/\d+\}", " ", m)                       # exponents like ^{1/2}
    if re.search(r"[\w})]\s*/\s*[\w\\{(]", m):
        err(i, "slash", "slash fraction in math: use \\frac")
    if r"\sqrt{12}" in m:
        err(i, "booklet", "\\sqrt{12} = booklet (28): cite it, don't write it")
    if re.search(r"\\sqrt\{N\}", m):
        err(i, "booklet", "\\sqrt{N} = booklet (34): cite it, don't write it")
    for sq in re.findall(r"\\sqrt\{(.*)", m):
        if "_{stat}" in sq and sq.count("^2") >= 2:
            err(i, "booklet", "stat + other error under one root = booklet (35): cite it, don't write it")
    formula_rhs = r"\s*=[^=]*\\(frac|sqrt)"     # a stated value (N_sigma = 2.1) is fine, a formula is not
    if re.search(r"N_\{?\\sigma\}?" + formula_rhs, m):
        err(i, "booklet", "N_sigma formula = booklet (51)-(53): cite it")
    if re.search(r"\\chi\^\{?2\}?(_\{?red\}?)?" + formula_rhs, m):
        err(i, "booklet", "chi^2 formula = booklet (50): cite it")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--limit", type=int, required=True, help="numbered-formula limit (Moodle)")
    ap.add_argument("--final", action="store_true", help="also fail on review colours left")
    a = ap.parse_args()
    errors, numbered = lint(a.tex, a.limit, a.final)
    for e in errors:
        print(e)
    print(f"lint: {numbered}/{a.limit} numbered formulas, {len(errors)} problem(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
