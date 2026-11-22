# Physics Lab 1a — rules card

Loaded into every session here. The full rules are `report-rules.md` (+ `<experiment>/report-rules.md`);
this card holds the judgement rules, and `labtools/lint_report.py` (run by `make`) checks the
pattern rules: semicolons, "p-value", first person, slash fractions, written-out booklet formulas,
booklet citations, briefing citations in footnotes, forward references, formula limit, colours (`make FINAL=1`). Fix lint failures,
don't suppress them without the user's yes (`% lint-ok: <check> (why)`).
Read a section of `report-rules.md` only when writing something this card doesn't cover.

**Sources.** Staff files (theory, briefing, theory-format docx), the instructor's replies, and the user.
Never the Moodle forum. Rules outrank past reports as templates. Where sources or rules conflict, ask the user (C4).

**Colours.** Claude's text is blue `\added{}` until the user approves; red `\TODO{}` = waiting for the user.

**Formulas (§3).**
- Booklet formulas are cited by number in words, never written: (25) relative, (28) resolution,
  (32)+(34) statistical, (35) combined, (39)/(43) indirect, (50) χ², (51)–(53) Nσ.
- Indirect errors ARE written and numbered, in their final form, with this experiment's quantities.
- Number: fit functions, every quantity extracted from fit parameters (with its error).
- Under every formula define every symbol. Δ only for errors. No numeric values in the plan.

**Each section.**
- Procedure: past tense, impersonal, what was actually done; N from the briefing/instructor → name the source.
- The briefing is cited in a footnote (`\footnote{תדריך הניסוי, עמ׳ N.}`), never inline. Only where the text gives no reason
  of its own (e.g. a briefing-given N), not for definitions or self-explained steps.
- Analysis plan: future impersonal. Per fit: x, y, each parameter's meaning and expected value,
  in words with the symbol (G p.3: "ציר ה-x הוא ציר הזמן t", "הפרמטר a0 מתאר את ..."). The fitted model is numbered.
  Source for every theoretical value. Statistics: χ²_red, p-value, residuals, Nσ ≤ 3, relative error.
- Results: findings only (values, graph observations, thresholds); say what each p-value means for χ²_red.
- Discussion: why. Every error source tied to a specific result (what / how / how much).

**Working.** Explain every analysis choice and its basis. Analysis uses only the staff theory and booklet
tools. No invented facts. A mismatch with theory means our result is off, not the theory.
