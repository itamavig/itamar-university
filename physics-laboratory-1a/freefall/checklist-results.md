# Pre-submission checklist — run 2026-10-29

Against `report/main.pdf` (7 pages: cover, 5 body pages, 1 appendix page) and `report/main.tex`.
Checklist = general rules §8 (course `checklist.pdf`). ✅ pass · ❌ fail · ⚠️ pass with a note.

## Fails (must fix before submission) — 4 left (P2 fixed 2026-10-29)
| # | Item | Status | Detail |
|---|---|---|---|
| G1 | Cover page complete | ❌ | 9 red fields in `report/details.tex`: part, instructor full name, submission date, 2 IDs, track, group, sub-group, station |
| P3 | Decisions explained (why these heights, why 10 repetitions) | ❌ | Red TODO at the end of the procedure; reasons coming from the partner |
| D2/D3 | Every error source explained / reason for every unexpected result | ❌ | p = 0.96 (errors overestimated): the cause is DISC-43/44, red; the data contradicts the Δh claim (refit: no Δh → χ²_red 0.34, no Δt → 1.71) |
| G0 | No review colours left | ❌ | 28 blue `\added` passages + 2 blue equations need the pair's OK; 2 red TODOs in the body |

## Notes (pass, but worth a decision)
| # | Item | Status | Detail |
|---|---|---|---|
| G3 | All formulas numbered | ⚠️ | One display formula has no number: g_theoretical = 981 ± 10 cm/s² in the theory section, as laid out in the staff file. Theory formulas don't count toward the limit |
| R | Meaning of values / parameters vs expectation, in Results | ⚠️ | Deliberately in the Discussion (user rule, general rules §4.5.11); the checklist lists it under Results |
| R | Error bars in residual graphs | ⚠️ | Show Δh only (Colab style); captions say so, and the text refers to the fit's errors |

## Passes
| Area | Item | Status |
|---|---|---|
| General | Units on every value (text, tables, captions) | ✅ |
| General | Rounding per booklet (tested against Table 3 on every build; raw table unrounded, allowed) | ✅ |
| General | Formula limit: 8 of 10 numbered (3)–(10) | ✅ |
| General | Page limit: 5 body pages of 10 (cover and appendix excluded) | ✅ |
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
| Discussion | Delay source: what / how / how much (a₁, 8.6 ms, 0.36 mm) | ✅ |
| Discussion | Every claim tied to a specific result | ✅ |
| Procedure | Every component labelled in the schematic: item 9 (optical gate) drawn in blue over figure 1, 2026-10-29 | ✅ |
| Style | No first person outside the staff theory text; no semicolons; "p-value"; no booklet page refs; no slash fractions | ✅ |
