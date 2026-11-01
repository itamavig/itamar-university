# Lab report rules — Physics Lab 1a (all experiments)

Compact English digest of the Hebrew guidelines. Reports are written in Hebrew.
Experiment-specific rules (limits, equipment, formulas, open items) live in `<experiment>/report-rules.md`, e.g. [freefall/report-rules.md](freefall/report-rules.md).

Sources (built 2026-10-26):
- `G` = [how_to_write_a_lab_report_2026.pdf](how_to_write_a_lab_report_2026.pdf) — the guide, wins on conflict
- `C` = [checklist.pdf](checklist.pdf)
- `D` = [חוברת עיבוד נתונים.pdf](חוברת%20עיבוד%20נתונים.pdf) — data-analysis booklet, cited by formula number
- `E` = [ExampleReport_2024.pdf](ExampleReport_2024.pdf) — example; layout reference only (§11 lists where it is wrong)
- `M` = instructor Tamir Moshe's email reply, 2026-10-26 (clarifies G; quoted in §3.9)
- Cover page template: [cover-page-template.docx](cover-page-template.docx)

Precedence: experiment briefing on experiment-specific choices > M > G > C > E.

---

## 1. Format (G general)
1. Page limit per experiment (Moodle); cover page + appendices don't count.
2. Every page numbered.
3. Body font size 10, line spacing 1.0. Footnotes numbered, font 8, bottom of page.
4. Hebrew body; English allowed for names/abbreviations (Python, ODR, p-value, Colab).
5. Cover page from the Moodle template. Fields: experiment name ("דו"ח מסכם בניסוי"), part ("חלק"), instructor full name, experiment date, submission date, for each of 2 students first name / last name / ID, study track, lab group no., sub-group, station no. Grader box (name, date, grade I/II, comments) stays empty.
6. PDF must render cleanly — no missing formulas, no broken RTL/LTR. Check the compiled PDF every time.
7. Paragraphs: no first-line indent; a small gap between paragraphs instead (user, 2026-10-28).

## 2. Language & style (G 3–4, 10; G Discussion)
1. Impersonal, distant phrasing: "המדידה התבצעה באמצעות…", not "ביצענו/הצבנו/מדדנו".
2. Tense per section, consistent within it: procedure = past (what was done); analysis plan = future impersonal ("יחושב", "תותאם"), except for the measurements themselves, which already happened ("נמדד") (user, 2026-10-28).
3. No slang, no spelling/grammar errors, no sentence fragments.
4. No vague value words: not "תוצאה טובה" (good relative to what?), not "הניסוי היה מוצלח".
4a. No semicolons in report text — split into sentences or use a comma (user, 2026-10-28).
4b. Write "p-value" (English, `\textenglish{p-value}`), never "ערך p" (user, 2026-10-28).
4c. **Anything Claude adds beyond the Doc is blue** (`\added{…}`), until the pair reviews it. Red `\TODO{…}` = still missing. Neither colour may remain in the submitted PDF (user, 2026-10-28).
4d. **Edits made on the partner's suggestions are green** (`\partner{…}`), until reviewed (user, 2026-10-30).
4e. Sub-list labels are (א), (ב)…; in running text a sub-item is referenced as parent number + letter, e.g. "תת-מטרה 1ב" (user, 2026-10-30).
5. Units in text: no brackets — `0.51 MeV`. Units on graph axes and table headers: square brackets — `t [s]`.
6. Lists of numbers in Hebrew text: one math block with commas, no Hebrew joiner like "ו-" before the last item — it splits the block and reads incoherently in RTL (user, 2026-10-28).

## 3. Formulas (G 6–8, G "which formulas", C, M)
1. Numbered-formula limit per experiment (Moodle). Excludes theory-background formulas. **Only explicitly written formulas count — citing a D number does not (M 3).**
2. Non-compact formula → own line + number. Inline unnumbered only if compact AND never referenced later.
3. Under every formula, define every symbol in it ("כאשר … הוא …").
4. Reference as "(3)", e.g. "ממשוואות (1) ו-(2)".
4a. No slash fractions for quantities in math (write $\frac{1}{2}g$, not $g/2$); slashes are fine in units like cm/s² (user, 2026-10-28).
4b. Δ is reserved for errors (uncertainties); never use it for a time interval or other difference — name those with their own symbol, e.g. $t_d$ (user, 2026-10-30).
5. Numbering continues from the theory background. Never reference a formula before it appears (e.g. no "(2)" in the goals) (user, 2026-10-26).
6. Typed formulas only, no screenshots. **No numeric substitution or computed values in formulas or in the analysis plan — formulas only (M 1).**
7. **DO write + number:** fit functions; the fitted-model formula; every physical quantity extracted from fit parameters; final formula of every indirect error (final form only — M: an indirect error can't be described in words, it varies case to case); final combined-error formula; instructor-requested formulas; non-uniform instrument errors (e.g. manufacturer spec).
8. **DO NOT copy D formulas verbatim — cite by number:**
   | Quantity | D formula |
   |---|---|
   | Relative error Δx/\|x\| | (25) |
   | Resolution error (uniform dist.) res/√12 | (28) |
   | Sample standard deviation | (32) |
   | Statistical error s/√N | (34) |
   | Combined error √(Δstat²+Δinst²) | (35) |
   | Indirect error, one variable | (39) |
   | Indirect error, general | (43) |
   | χ²_red | (50) |
   | p-value | no formula of its own — cite it via (50) (χ² and N−K). **Never cite a booklet page number, only formula numbers** (user, 2026-10-28) |
   | Nσ between two values | (51) |
   | Nσ vs an exact value / vs zero | (52) / (53) |
9. **Adapted D formulas (M 1)** — a D formula rewritten with *this experiment's* symbols (e.g. Δh = h_res/√12) MAY be written and numbered, with a sentence saying it is D formula (N) adapted. For simple ones it is also allowed to skip the formula and describe it in words only, e.g. "שגיאת הסרגל חושבה לפי נוסחה (28) בחוברת עיבוד הנתונים, כאשר הרזולוציה היא רזולוציית הסרגל, תחת הנחת התפלגות אחידה בין השנתות". M's suggested wording when writing it:
   > "שגיאת הסרגל בניסוי היא שגיאת רזולוציה המחושבת לפי נוסחה (28) בחוברת עיבוד הנתונים תחת ההנחה של התפלגות אחידה בין שנתות הסרגל: Δh = h_res/√12 (N)"
   **Delicate — user's rule:** words-only is for *simple* adaptations only (resolution, plain stat error). Decide per formula with the user; don't default to it.

## 4. Section order and required content
### 4.1 מטרות הניסוי (G)
Goals must be falsifiable: not "נעריך את g" but "נעריך את g ונראה שהוא תואם לערך התיאורטי בטווח הטעות המקובל".
Length: one sentence per goal, fuller than a bare "measure X" (instructor, via user 2026-11-01). Thresholds (N_σ ≤ 3, 5%) belong in the analysis plan, not the goals; "בטווח הטעות המקובל" is enough, as in G's own example.

### 4.2 רקע תיאורטי (G)
In course A1 the background is taken from the Moodle theory file. Short, relevant, every symbol defined.

### 4.3 מהלך הניסוי (G, C) — a stranger must be able to reproduce the measurements from this section alone
1. System description + equipment list **with the resolution of every measuring instrument**.
2. Schematic figure; every component labelled with its number in the equipment list.
3. Procedure: assembly, how each measurement is taken, exact quantities measured, number of repetitions, scales/ranges.
4. Explain decisions (why these values, why N repetitions, etc.).
5. Describe only what was actually done. Simple, clear, hierarchical structure.
6. Source/reference for every theoretical value.

### 4.4 תכנון עיבוד תוצאות (G, C, M) — a reader must be able to reproduce the analysis from the measurements + this section alone
1. Every analysis step and every explicit formula used (within the limit). No derivations. No computed values (M 1).
2. Each fit: fit function (numbered), what x and y are, meaning of each parameter, expected value of each parameter.
3. Extraction formula for each physical quantity from the parameters (numbered) + its error.
4. Which statistics are computed and what they mean: χ²_red D(50), p-value D p.19, residual graph, Nσ D(51), relative error D(25).
5. Fit tool: course Colab Python ODR code, inputs x, Δx, y, Δy.

### 4.5 תוצאות (G, C, M)
1. **Content per M 2:** fit graph; residual graph; fitted parameters; χ²_red; p-value; the extracted physical quantity; Nσ between it and the theoretical value, **stating the theoretical value used**. Errors, relative errors, units, rounding wherever applicable.
2. **Raw data and all Excel-computed values with errors → appendices**, not Results (M 2).
3. For each parameter: does it match its expectation? If not, say so.
4. Interpret the statistics: χ²_red ≈ 1 expected; p fine if 0.05 ≤ p ≤ 0.95; p < 0.05 → χ² too big (model wrong or errors under-estimated); p > 0.95 → χ² too small (errors over-estimated). Nσ ≤ 3 = agreement.
5. Never show calculations or numeric substitutions — results only.
6. Fit-graph paragraph (in text, after the graph): visual trend vs prediction; problem regions / outliers / unusual error bars; every parameter vs expectation, emphasis on the physical one; what the statistics mean and why.
7. Residual-graph paragraph: random or not? trend? mostly above/below zero (→ systematic error)? error-bar size vs distance from zero, and what that implies for χ². Axis scales mislead — trust the numbers, not the eye.
8. Residual graph that shows nothing → one sentence in text, graph in appendix, referenced. Residual graph that shows something → in the body, explained.
9. Outliers: fit all points first. Recording errors → drop, say so in Results. Outlier = > 3σ from fit line; drop only with a measurement-based reason (never "doesn't match expectation"); max 2 points; then show BOTH fits (corrected in Results, original in Appendix) with parameters + statistics for both.
10. Results says *what* the data shows. Discussion says *why* and what it means.
11. **Results = findings only (user, 2026-10-28):** values, observations of the graphs, and each value against the plan's threshold (e.g. "relative error below 50%", "p-value below 0.05"). No verdicts or interpretations ("not consistent with expectation", "the model does not describe", "errors overestimated") — those go to the Discussion. Note: G's own example puts "errors were overestimated" in Results; the user's rule overrides.

### 4.6 דיון (G) — ½ to 1 page; explain, don't repeat
1. Were the goals met? Agreement with theory (Nσ) and precision (relative errors).
2. Error sources — only those tied to a specific result. Over-estimation: which error, of what, why, how to re-estimate. Under-estimation: which errors too small or missing. For each source: *what* it affects (quantity / parameter / statistic; statistical vs systematic constant vs systematic non-constant), *how* (increases/decreases), *how much* (order of magnitude). An unconnected list of error sources is an error.
3. Compare methods that measured the same quantity: which is more reliable and why.
4. Physical effects observed (intended or not).
5. System limitations and strengths.
6. Improvements: same system, better method or new quantities. NOT "use a laser", "finer ruler", "more measurements".

### 4.7 שאלת מדריך (C)
The instructor's question must be answered. E puts it as its own section between Results and Discussion.

### 4.8 נספחים (G 11, M 2)
Same rules: units, captions, rounding. Only raw-data tables may stay unrounded. Raw data + Excel error calculations, normal residual graphs, with-outlier fits.

## 5. Rounding (D p.24, G)
1. Value with error: round error to **2 significant figures**, round the value to the same decimal place. Keep trailing zeros (0.0050, not 0.005).
2. Values without error (relative error, χ²_red, p-value, Nσ): 2 significant figures.
3. Round only final results; never round intermediates.
4. Scientific notation allowed when it helps.
5. Relative error < 5% counts as small in this course (D).
6. **Presentation of relative errors (user, 2026-10-26):** in running text, every value that has a relative error gets it in parentheses after the error — `g = 1002.5 ± 1.6 cm/s² (0.16%)`. In tables, relative error is its own column (G table 1 style).

## 6. Figures (G, C)
1. No title above a figure. Caption **below**, numbered: "איור 3: גובה הנפילה במטרים כתלות בזמן הנפילה בשניות".
2. Figures and graphs share one numbering ("איור"). Tables have their own ("טבלה").
3. Axis titles + units in square brackets on every graph. Legend correct.
4. Measurements = points with error bars; theory/fit = continuous line.
5. Several curves/point-sets → label each.
6. Every fit graph has a residual graph. Residual y-axis title ≠ original y-axis title (e.g. `h − f(t) [cm]`).
7. Max ½ page per figure. Every figure gets an explaining paragraph in the text.
8. **Every graph gets its own figure number and caption (user, 2026-10-26)** — fit and residual graphs are separate figures, even when placed side by side.
9. Tables: full borders, all columns centered (user, 2026-10-26). Units go in the value cells, never in the parameter/row name (user, 2026-10-26; G allows this — headers are only "a common way"). Exception (user, 2026-10-29): long data tables where a whole column shares one unit (e.g. raw data) put the unit once in the column header, wrapped in `\textenglish{}` so `t [s]` keeps LTR order.
10. Captions (figures and tables) at 9pt; G only sets body text to 10 (user, 2026-10-26).
11. Figures and tables never float away from their text: `[H]` placement (float package) (user, 2026-10-30).

## 7. Tables (G)
1. Caption **below**, numbered, no title above: "טבלה 1: …".
2. Units in the row/column headers.
3. Summary tables of final results → body. Completeness tables (raw data) → appendix.

## 8. Pre-submission checklist (C — tick every item)
General
- [ ] All values have correct units
- [ ] All values correctly rounded (incl. appendices; raw-data tables exempt)
- [ ] All formulas numbered
- [ ] Within formula limit
- [ ] Within page limit
- [ ] All statistics addressed: χ², p-value, Nσ, relative errors, residual graphs
- [ ] Instructor's question answered

Procedure
- [ ] Instrument resolutions in the equipment list
- [ ] Source for every theoretical value
- [ ] Exactly which quantities were measured and how many times

Analysis plan
- [ ] Final formula of every indirect error numbered
- [ ] Final combined-error formula numbered
- [ ] Every quantity extracted from fit parameters numbered
- [ ] D formulas cited by number, not copied (uniform dist., Nσ, std/stat error, general indirect, general weighting, relative error); no numeric substitution

Results
- [ ] Axis titles + units on all graphs; legend correct
- [ ] Residual graph for every fit
- [ ] Residual y-axis title is correct (not the original's)
- [ ] Caption under every graph, "איור N: …" style
- [ ] Label for each curve/point set when several
- [ ] All fit parameters shown (a₀, a₁, a₂…)
- [ ] Parameters checked against expectation
- [ ] χ²_red and p-value shown
- [ ] Meaning of the values explained
- [ ] Each graph discussed in the text after it appears
- [ ] Residual scatter (random?) and distance vs error bars discussed
- [ ] No calculations / number substitutions shown

Discussion
- [ ] Goals addressed: agreement with theory (Nσ) and precision (relative errors)
- [ ] Every error source explained by its effect (what / how / how much)
- [ ] Reason given for every result that missed its expectation
- [ ] Every claim tied to a specific result

## 9. Toolchain (ours)
- Reports in LaTeX (Hebrew, RTL) + Python. Content comes from the pair's Google Doc; rephrase freely, don't change content without asking.

## 10. Where the example report (E) is NOT a model
- E uses first person ("נבצע", "ביצענו") → impersonal.
- E labels graphs "גרף N" with side boxes → "איור N:" caption below.
- E's residual graphs reuse the original y-axis title → must differ.
- E shows a calculation in Results (substituted values) → don't.
- E's discussion lists error sources not tied to results → tie each to a result.
- E has rounding slips ("0.0002%", "4.35%") → 2 significant figures.
- E is fine for: cover page, equipment list with resolutions, citing D by number + page, results table layout, instructor-question section, appendix raw-data tables.
