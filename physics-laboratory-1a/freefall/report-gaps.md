# Free-fall lab report — gaps in "מהלך הניסוי" and "תכנון עיבוד תוצאות"

Checked 2026-10-26 against:
- [how_to_write_a_lab_report_2026.pdf](../how_to_write_a_lab_report_2026.pdf)
- [checklist.pdf](../checklist.pdf)
- [ExampleReport_2024.pdf](../ExampleReport_2024.pdf)

Report: Google Doc "Lab report - freefall, Lior Beinhorn and Itamar Avigdori".
The text export of the Doc drops equations, so equation images were counted separately.

## תכנון עיבוד תוצאות

### Numbered formulas that are missing
The background section has (1) and (2), so numbering continues from (3).

- [x] **Fit functions.** — Resolved in report 2026-10-28 (approved 2026-10-28): (6), (8). `y=a1x+a0` and `y=a0+a1x+a2x²` are only inline text. Give each its own numbered line and define every variable under it.
- [x] **Getting g from the fit.** — Resolved in report 2026-10-28 (approved 2026-10-28): (7), (9). `g=2a1` is inline and not numbered. The parabolic fit has no g formula at all; add `g=2a2`.
- [x] **Indirect error of t².** — Resolved in report 2026-10-28 (approved 2026-10-28): (5). There is one equation image here, but it has no number.
- [x] **Combined error of t** — Resolved in report 2026-10-28 (approved 2026-10-28): (4). (resolution + statistical). Right now it only cites "(35)". The checklist requires this one as a numbered formula.
- [x] **Error of g.** — Resolved in report 2026-10-28 (approved 2026-10-28): inside (7), (9). `delta(g)=2*delta(a1)` is inline, and its closing parenthesis is missing. Add the a2 version as well.

### Placeholders that must NOT be filled as written
The guide says these are referenced from the data-analysis booklet by number only, never written out.

- [x] The note to insert the resolution formula with h_res — Resolved in report 2026-10-28 (approved 2026-10-28): note dropped; written as adapted (3) per instructor email.: delete the note and keep "(28)".
- [x] The note to attach the N_sigma formula — Resolved in report 2026-10-28 (approved 2026-10-28): note dropped; (51) cited.: delete the note and keep "(51)".
- [x] The note to optionally insert formulas for the statistical error — Resolved in report 2026-10-28 (approved 2026-10-28): note dropped; (32),(34) cited.: delete it. Only the combined error formula goes in.

### Text that is still unfinished
- [x] Theoretical g value, plus its source — Resolved in report 2026-10-28 (approved 2026-10-28): 981 ± 10 cm/s², briefing via theory file. (the checklist asks for a source for every theoretical value).
- [x] "סעיף (?)" in the parabolic model. — Resolved in report 2026-10-28 (approved 2026-10-28): refers to (3),(4).
- [x] "נוסחה (?)" for the p-value. — Resolved in report 2026-10-28 (approved 2026-10-28): cited via formula (50), no page numbers.

### Content that is missing
- [x] The linear model has no residual-graph step. — Resolved in report 2026-10-28 (approved 2026-10-28): residual check now applies to both fits. Only the parabolic model has one.
- [x] The parabolic model doesn't say that its N_sigma — Resolved in report 2026-10-28 (approved 2026-10-28): Nσ paragraph covers g from each fit. is computed from the g that comes out of a2.
- [x] The list numbering restarts partway through. — Resolved in report 2026-10-28 (approved 2026-10-28): restructured into subsections.
- [x] χ² and p-value are listed twice — Resolved in report 2026-10-28 (approved 2026-10-28): merged into one list. in the parabolic part (items 3 and 5).
- [x] The p-value is described two ways. — Resolved in report 2026-10-28 (approved 2026-10-28): kept the correct definition; 'closeness to 1' moved to χ²_red. "Closeness of χ² to 1" is wrong; item 5.2 has the correct definition.

## מהלך הניסוי

- [x] **The diagram doesn't match the equipment list.** Resolved 2026-10-26: equipment list renumbered to the schematic's 1–8 (clamp = 5). The text says "התופסן (5 באיור)", but item 5 in the equipment list is the optical gate, and the clamp isn't listed. The numbers in the diagram must match the equipment list.
- [x] **The optical gate is listed but never used** — Resolved 2026-10-29: it starts the timing (user decision, per briefing and DISC-36); report updated in blue. in the procedure. Remove it or explain what it's for.
- [x] **No definition of what "height" means.** Resolved 2026-10-26: taken from the schematic legend (ball base to sensor). Say from which point to which point it's measured (the bottom of the ball, the plate surface, and so on).
- [ ] **No reasons for your choices.** Explain why these heights, why 45 cm, and why 10 repetitions.
- [ ] **Formatting:**
  - Steps 3–5 are indented under step 2.
  - Use impersonal wording ("המדידה התבצעה", not "הצבנו" or "ביצענו").
  - Use one tense throughout ("מכוונים" is present tense, the other steps are past tense).

## Not checked
- [ ] The formula limit for this experiment is on Moodle. Count the numbered formulas against it once they're in.

## Found 2026-10-26 (second read of the Doc)
- [ ] **Instructor question, sign.** Doc writes `M*g = Ff = -b*V_final` → `V_final = -M*g/b`. With the positive direction down, at terminal velocity mg − bV = 0, so V_final = mg/b (positive, downward). Needs a fix in content — ask partner.
- [x] **p-value citation.** — Resolved in report 2026-10-28 (approved 2026-10-28): cited via formula (50), no page numbers. Doc says "עמוד 18" in one place and "נוסחה (?)" in another. In the booklet the p-value is defined on printed page 19, with no formula number. Cite "עמוד 19".
- [ ] **Formula (?) placeholders in Results** for g and N_sigma — fill with our numbers once the formula budget is approved.
- [ ] **Discussion is cut off** mid-sentence after the linear-fit χ² paragraph.
- [ ] **Results section title.** Doc calls it "עיבוד התוצאות"; the guide calls it "תוצאות".

## Found 2026-10-29 (discussion)
- [x] **DISC-43/44 claim vs data.** Resolved 2026-10-30 (P6): replaced by the refit argument. The Doc says the error overestimate comes mainly from the height resolution error. Refit: without Δh, χ²_red = 0.34 (p = 0.93); without Δt, 1.71. The time error dominates. In the report in red, for the pair to rewrite.
- [x] **"Least Squares" in DISC-24.** The course fit is ODR; replaced in blue.

## Excel review (2026-11-01) — no effect on the report's numbers
- [ ] Column S "Δt/t %" holds a ratio (0.0014), not a percent (0.14%). Label or formula mismatch; the report doesn't use this column.
- [ ] Δt_stat uses `/SQRT(10)` hard-coded; the template asked for COUNT(...) so it adapts to the number of measurements. Correct for this data (10 per height), fragile if a row ever has fewer.
- [ ] Sheets `linear`/`parabolic` hold pasted values, not formulas: they won't follow edits to the raw times. Today they equal the computed columns exactly (checked).
- [ ] Leftover template example formulas in M27:M32 of the first sheet.
