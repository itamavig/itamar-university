# Pre-submission checklist — run 2026-11-17

Against `report/main.pdf` (15 pages: cover, body on printed pages 1–11, appendices from the bottom of printed page 11) and `report/main.tex`, at commit 90d2eae.
Checklist = general rules §8 (course `checklist.pdf`). ✅ pass · ❌ fail · ⚠️ pass with a note.

## Fails
| # | Item | Detail | Fix |
|---|---|---|---|
| R6 | All fit parameters shown | ✅ fixed | b₀ row added to table 2 (macros, 65/65 Colab match) with a sentence on its meaning |

## Notes (pass, but worth a decision)
| # | Item | Status | Detail |
|---|---|---|---|
| G | Overfull line | ✅ | Fixed 2026-11-17: SI units of S/m written as a fraction; log has no overfull boxes |
| G3 | All formulas numbered | ⚠️ | Four unnumbered displays: theory section (staff text, verbatim) — L = π²/3·(k_B/e)² = 2.44·10⁻⁸ (main.tex:70), f(2) ≃ 1.75 and μ₀M = 0.65 T (main.tex:80), P(x) = P_avg = P_in − (P_absorb + P_loss)/2 (main.tex:97); instructor answer — P_{i,i+1} (main.tex:594). Limitations formulas are inline. At the 16-formula limit |
| G | Submission date | ✅ | Cover says 17.11.2026; the user got an extension to that date |
| D2 | Error source "how much" | ⚠️ | Stopwatch delay: direction stated, size explicitly unknown (delay not measured) |

## Passes
| Area | Item | Status |
|---|---|---|
| General | Units on every value (text, tables, captions) | ✅ |
| General | Rounding per booklet (test_rounding on every build; raw-data tables unrounded, allowed) | ✅ |
| General | Within formula limit (16/16) | ✅ |
| General | Within page limit (body ends on printed page 11 of 12) | ✅ |
| General | χ², p-value, Nσ, relative errors, residual graphs all addressed | ✅ |
| General | Instructor's question answered (lab-based route, approved 2026-11-17) | ✅ |
| General | No review colours left (PDF text spans checked: all black) | ✅ |
| Procedure | Instrument resolutions in the equipment list | ✅ |
| Procedure | Source for every theoretical/given value (L theory file; T, ΔT, Δx, g from the instructor; μ₀M, f(2) from theory) | ✅ |
| Procedure | Measured quantities and repetitions (table 3: m 4, t 10, d 4, D_ch 4, D 4, L₀ 1) | ✅ |
| Plan | Final indirect-error formulas numbered: (6), (7), (10), (12), (14), (15), (16) | ✅ |
| Plan | Quantities from fit parameters numbered: κ (9), rates (13), P_avg (5) | ✅ |
| Plan | Booklet formulas cited by number, not copied: (25), (28), (32), (34), (35), (43), (51), (52) | ✅ |
| Results | Axis titles + units; legends; title inside every plot (rule 6.1) | ✅ |
| Results | Residual graph for every fit; residual y-axis T − f [K] | ✅ |
| Results | Caption under every graph, "איור N" | ✅ |
| Results | χ²_red and p-value shown and their meaning stated (rule 12) | ✅ |
| Results | Each graph discussed after it appears; residual scatter vs error bars discussed | ✅ |
| Results | No calculations / substitutions shown | ✅ |
| Discussion | Goals: Nσ (4.1, 7.2) and relative errors (σ 2.0%, κ 1.7%) | ✅ |
| Discussion | Reason for every missed expectation: L (power loss ruled out, stopwatch error), part ב p-value, part ג χ² | ✅ |
| Discussion | Every claim tied to a specific result / figure | ✅ |
| Privacy | details.tex, main.pdf, review.pdf gitignored; no 9-digit IDs in tracked sources | ✅ |
