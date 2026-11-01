# Pre-submission checklist — run 2026-11-01 (previous run 2026-10-29)

Against `report/main.pdf` (8 pages: cover, 6 body pages, 1 appendix page) and `report/main.tex`.
Checklist = general rules §8 (course `checklist.pdf`). ✅ pass · ❌ fail · ⚠️ pass with a note.

## Fails — none

## Fixed since 2026-10-29
| # | Item | Fix |
|---|---|---|
| G1 | Cover page complete | All fields filled 2026-11-01; station blank by the user's choice |
| P3 | Why these heights | Briefing p. 3: steps of 5 cm or 10 cm, 10–12 heights (blue sentence in the procedure) |
| G0 | No review colours left | Switched off with `\reviewfalse` (2026-11-01); PDF text checked all black, only the graphs keep their plot colours |
| D2/D3 | Reason for the overestimate (p = 0.96) | Discussion says the source is unclear and offers the height-resolution hypothesis, D(28). Hedged; the refits (no Δh → p 0.93, no Δt → p 0.10) support either |

## Notes (pass, but worth a decision)
| # | Item | Status | Detail |
|---|---|---|---|
| G3 | All formulas numbered | ⚠️ | g_theoretical = 981 ± 10 cm/s² in the theory section has no number, as in the staff file (todo 10b) |
| R | Conclusions (overestimate, parameters vs expectation) in Results | ⚠️ | Deliberately in the Discussion (user rule, general rules §4.5.11). The writing guide p. 7 says the overestimate verdict itself belongs in Results |
| R | Error bars in residual graphs | ⚠️ | Show Δh only (Colab style); captions say so |
| D | Overestimate stated three times in the parabolic discussion | ⚠️ | Bullet 1 (p-value), bullet 2 (residuals) and the paragraph after the bullets. Could merge |
| D | Improvement 3 (ruler away from the landing box) tied to a result? | ⚠️ | Linked to height calibration; the text doesn't name the result it answers (linear a₀ / height error) |
| G | Personal IDs on the cover | ✅ | details.tex and main.pdf untracked + gitignored 2026-11-01; git history never held the IDs (checked with git log -S) |

## Passes
| Area | Item | Status |
|---|---|---|
| General | Units on every value (text, tables, captions) | ✅ |
| General | Rounding per booklet (tested against Table 3 on every build; raw table unrounded, allowed) | ✅ |
| General | Formula limit: 8 of 10 numbered (3)–(10) | ✅ |
| General | Page limit: 6 body pages of 10 (cover and appendix excluded) | ✅ |
| General | All statistics addressed: χ²_red, p-value, N_σ, relative errors, residual graphs | ✅ |
| General | Instructor question answered | ✅ |
| Procedure | Instrument resolutions in the equipment list (ruler 0.1 cm, software 10⁻⁵ s) | ✅ |
| Procedure | Source for the theoretical value (g, "לפי תדריך הניסוי") | ✅ |
| Procedure | What was measured and how many times (10 heights × 10) | ✅ |
| Plan | Final indirect-error formulas numbered: (5), (7), (9) | ✅ |
| Plan | Final combined-error formula numbered: (4) | ✅ |
| Plan | Every extracted quantity numbered: (7), (9), (10) | ✅ |
| Plan | Booklet formulas cited by number, not copied; no numeric substitution | ✅ |
| Results | Axis titles + units, legends | ✅ |
| Results | Residual graph for every fit, with a different y-axis title | ✅ |
| Results | Caption under every figure and table, "איור N:" / "טבלה N:" | ✅ |
| Results | All fit parameters shown (table 1) | ✅ |
| Results | χ²_red and p-value shown | ✅ |
| Results | Each graph discussed after it appears | ✅ |
| Results | Residual scatter and distance vs errors discussed | ✅ |
| Results | No calculations or substitutions shown | ✅ |
| Discussion | Goals addressed: agreement (N_σ) and precision (relative errors), both fits | ✅ |
| Discussion | Delay source: what / how / how much (a₁, τ = 0.0086 s, formula (10)) | ✅ |
| Discussion | Every claim tied to a specific result | ✅ |
| Procedure | Every component labelled in the schematic: item 9 (optical gate) drawn in blue over figure 1, 2026-10-29 | ✅ |
| Style | No first person outside the staff theory text; no semicolons; "p-value"; no booklet page refs; no slash fractions | ✅ |
| Appendix | Table 3 has a relative-error column for each value with an error (2026-11-01) | ✅ |
