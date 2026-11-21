# Free-fall report — experiment-specific rules

General rules for every report: [../report-rules.md](../report-rules.md); the source letters G, C, D, E, M are defined there. This file only adds what is specific to free fall.

Sources:
- `B` = [תדריך נפילה חופשית_2026.pdf](תדריך%20נפילה%20חופשית_2026.pdf) — briefing
- `T` = [נפילה חופשית רקע תיאורטי.pdf](נפילה%20חופשית%20רקע%20תיאורטי.pdf) — theory background
- Doc = the pair's Google Doc https://docs.google.com/document/d/1MUINwf7WtN5xF8mn_HDU8LOiYBhBlKdToIahe57nC-M
- Raw data: [FreeFall_19-10-2026_14-30-49.xlsx](FreeFall_19-10-2026_14-30-49.xlsx)
- Colab notebooks, copied to [colab/](colab/) on 2026-10-26: linear = 1mQA7M1Q… , parabolic = 1Q7g2arU… . Both are the course template; they read sheets `linear` / `parabolic` of the xlsx (named `results.xlsx` in Colab, same file as ours).

## 1. Limits (user, 2026-10-26)
- **Page limit: 10** (cover + appendices excluded).
- **Numbered-formula limit: 10** (theory formulas (1), (2) excluded).

## 2. Theory (T)
- **Section text source: [theory-background-format.docx](theory-background-format.docx)** (staff file, created 2016, last edited by "Sivan"; user downloaded it from Moodle). The Doc's theory section is this file word for word. It uses h (not y), cm units, and g = 981 ± 10 cm/s² "לפי תדריך הניסוי". Formulas: (1) h = h₀ + v₀t + ½gt², (2) h = ½gt².
- (1) y = y₀ + v₀t + (g/2)t²; (2) y = (g/2)t² (positive direction down, released from rest, y₀ = 0).
- Theoretical value: **g = 9.81 ± 0.10 m/s²**, source T. Doc results are in cm → 981 ± 10 cm/s².
- Model assumptions (B asks): released from rest, only gravity (no air resistance), constant g, origin at the release point.

## 3. Equipment (B)
1. Metal ball 2. Stand 3. Ruler, resolution 0.1 cm 4. Timing software, resolution 10⁻⁵ s 5. IR optical gate 6. Metal plate + piezoelectric sensor 7. Electromagnet (solenoid).
The Doc calls the clamp "5" — see [report-gaps.md](report-gaps.md).

## 4. Measured quantities (Doc)
- Heights: 10, 15, 20, 30, 40, 45, 50, 60, 70, 80 cm (10 heights). 10 time measurements per height.
- Times exported from the software to Excel.

## 5. Error budget (B, D, M)
- h: resolution error, D(28), uniform distribution.
- t per height: mean of 10 (why: the mean is the best estimate of the expected value; stat error ∝ 1/√N). Stat error D(32)+(34); resolution error D(28); combined → **numbered**, cite D(35).
- t²: indirect error → **numbered**, cite D(39).
- g from a fit parameter: g = 2aₖ ± 2Δaₖ → **numbered** (one line per fit).

## 6. Fits
| | Linear | Parabolic |
|---|---|---|
| Function | y = a₀ + a₁x | y = a₀ + a₁x + a₂x² |
| x, y | x = t², y = h | x = t, y = h |
| Expected | a₀ = 0, a₁ = g/2 | a₀ = 0, a₁ = 0, a₂ = g/2 |
| g | g = 2a₁ ± 2Δa₁ | g = 2a₂ ± 2Δa₂ |
- Parameter meanings (parabolic): a₀ initial height, a₁ initial velocity, a₂ half the acceleration.
- **Checking a parameter expected to be 0: briefing wins (user, 2026-10-26)** — it is consistent with 0 if its relative error is ≥ 50%. (B asks "why not Nσ?" — answer if space: D(53) gives Nσ = 1/relative error, so it is the same test.)

## 7. Formula budget — (3)–(9), approved 2026-10-28
Applied: Δh (3), Δt (4, resolution term written inside, no separate Δt_res), Δ(t²) (5), linear fit (6), g lin (7), parabolic fit (8), g par (9) = 7 of 10. No words-only formulas used.
2026-10-28: + (10) V_f = Mg/b, instructor question (G: instructor-requested formulas are numbered) = 8 of 10, approved 2026-10-29.
2026-11-01: terminal velocity V_f = Mg/b made inline (unnumbered, compact, not referenced); τ = a₁/g ± √((Δa₁/g)² + (a₁Δg/g²)²) in the discussion = (10), the direct D(43) partial-derivative form (user-approved; Δτ checked three ways = 0.901896 ms). 8 of 10.

Original draft:
Theory (1)–(2) don't count. Proposal:
| # | Formula | Why numbered |
|---|---|---|
| (3) | Δt = √(Δt_stat² + Δt_res²) | final combined error (C requires) |
| (4) | Δ(t²) = 2t·Δt | final indirect error (C, M require) |
| (5) | y = a₀ + a₁x | fit function |
| (6) | g = 2a₁ ± 2Δa₁ | extracted quantity + its indirect error |
| (7) | y = a₀ + a₁x + a₂x² | fit function |
| (8) | g = 2a₂ ± 2Δa₂ | extracted quantity + its indirect error |
| (9)? | Δh = h_res/√12 | optional adapted D(28) — or words only |
| (10)? | Δt_res = t_res/√12 | optional adapted D(28) — or words only |
| ? | terminal velocity v_f = mg/b | instructor question; numbered only if referenced |
That is 6 required + up to 3 optional ≤ 10.

## 8. Instructor question (in Doc)
"A body falls under gravity plus air drag F_f = −bV. (a) Estimate the terminal velocity. (b) Describe an experiment to measure it." Doc has an answer (Hebrew) — sign issue noted in [report-gaps.md](report-gaps.md).

## 9. Results to show (M 2) — from Doc, to be regenerated in Python
- Linear: a₀, a₁ (± error, relative error), χ²_red, p-value, g, Nσ.
- Parabolic: a₀, a₁, a₂ (same), χ²_red, p-value, g, Nσ.
- Fit graph + residual graph for each (Doc's linear residuals show a parabolic trend → keep in body; parabolic residuals look random → may go to appendix with one sentence).
- Appendix: raw times per height, means, errors, t², Δ(t²) from Excel.

## 10. Physical effect to discuss (G's own free-fall example; Doc discussion is still unfinished)
Parabolic fit gave a₁ ≠ 0 → the ball already has velocity when timing starts (timing point is below the release point). Linear fit a₀ ≠ 0 → offset between ruler zero and the actual release point.

## 11. Colab notebooks — what they do (read 2026-10-26)
- Fit: `scipy.odr` (Model, RealData with sx=Δx, sy=Δy, beta0 = initial guesses). Errors = `output.sd_beta`. χ²_red = `output.sum_square / (N − K)`, p = `stats.chi2.sf(χ², N − K)`.
- Linear: columns x = t_avg², Δx = Δ(t_avg²), y = h, Δy = Δh; guesses (0, 981). Output a₀ = 0.867 ± 0.061 cm, a₁ = 501.25 ± 0.81 cm/s², χ²_red = 3.5, p = 5.3·10⁻⁴; g = 1002.5 ± 1.6 cm/s², Nσ = 2.1.
- Parabolic: x = t_avg, Δx = Δt_fin, y = h, Δy = Δh; guesses (0, 0, 490.5). Output a₀ = −0.07 ± 0.10 cm, a₁ = 8.34 ± 0.87 cm/s, a₂ = 485.0 ± 1.7 cm/s², χ²_red = 0.28, p = 0.96; g = 969.9 ± 3.4 cm/s², Nσ = 1.0.
- Δh = 0.028868 cm = 0.1/√12 (matches D(28)).
- Row numbers in the sheets skip (1, 2, 3, 5, 7…): rows 4, 6, 10, 12, 14 (25, 35, 55, 65, 75 cm) are empty template rows that were never measured. No data dropped.
- Their plots break report rules: title above the figure (G: caption below only), fit and residuals side by side 15×6 in. Our report graphs must be re-drawn.
- Units: cm and s ("sec" in labels → use "s").

## 12. Doc → report traceability (2026-10-26)
- `analysis/doc_ledger.py` splits the Doc into units (`doc/ledger.tsv`, IDs like `PLAN-07`). Every LaTeX passage carries `% src: ID ID…`: on the line above the passage, or at the end of a table row.
- A unit not carried over gets a status in the ledger with a note: `dropped`, `replaced`, `fixed` (content correction, user-approved only). `gone` = removed or edited in the Doc since the last sync.
- `make doc` = fetch the Doc + sync + check. `doc_ledger.py side PLAN` prints the Doc units next to their LaTeX for review.
- Section is done when `check` shows it at n/n and the user approved its side-by-side.

## 12. Conclusions moved out of Results — must appear in the Discussion (2026-10-28)
- Linear: a₀ not consistent with 0 (rel. error 7.1% < 50%).
- Linear: χ²_red = 3.5, p < 0.05 → χ² too large; the linear model does not describe the data (with the residual trend).
- Parabolic: a₀ consistent with 0 (140% ≥ 50%); a₁ not consistent with 0 (10% < 50%) → initial velocity.
- Parabolic: p = 0.96 > 0.95 → χ² too small → errors overestimated. Not in the Doc's discussion yet — needs an explanation.
- Both: g agrees with theory (N_σ ≤ 3) and relative error < 5% → goal 1 met for both fits.
