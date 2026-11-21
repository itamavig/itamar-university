# Viscosity lab report — todos

Rules: [../report-rules.md](../report-rules.md) (general) + [report-rules.md](report-rules.md) (viscosity).

## Setup
- [x] 0. Folder scaffolded from ../_template/ (2026-11-21, commit 2935357). Raw data `viscosity measurements.xlsx` in the folder since 2026-11-16
- [x] 1. Staff files from Moodle (course 03211111, section "צמיגות") into this folder — done 2026-11-21: user downloaded them, moved here; sizes match Moodle byte for byte; theory PDF 4 pages, briefing PDF 10 pages, both have a text layer; docx zip intact
  - Files: `רקע תיאורטי צמיגות תשפב.pdf` (628,644 B), `תדריך עבודה צמיגות תשפז.pdf` (838,443 B), `פורמט רקע תיאורטי צמיגות - חדש.docx` (18,338 B; saved as `theory-background-format.docx`, as in freefall/ and heat-conduction/)
  - Not files: "דוח מעבדה צמיגות" is the upload assignment (due: two weeks from the day the experiment was done, no attachments); "תוכנת Tracker" links to https://physlets.org/tracker/
  - 2026-11-21: the built-in browser pane cannot save downloads (no file in ~/Downloads, direct navigation refused, and a 127.0.0.1 receiver got no request). Waiting on the user: Claude in Chrome, or the user clicks the three links
- [ ] 2. Moodle Q&A forum "שאלות תשובות - צמיגות", read 2026-11-21: one student question (16.11.2026, 0 replies) — the briefing looks old: its exponential v(t) fit (V0, Vf) is not needed? Proposed fits: (1) mass vs volume, linear → density; (2) position vs time, linear → terminal speed; (3) speed vs R², linear → η. Re-check for a staff answer before planning the analysis
- [x] 3. Staff files read (2026-11-21). Letters as in the other experiments: T = theory PDF (תשפ"ב, 4 pp.), B = briefing (תשפ"ז, 10 Oct 2026, 10 pp.), F = theory-format docx
  - Goal (B p.1): "מציאת ערך צמיגות הגליצרין ואימות חוק סטוקס"
  - F = the theory section to copy: formulas (1) Stokes, (2) Newton, (3) v_f, (4) v(t) exponential + τ, (5) η = A·e^{B/T}, (6) t = C·e^{D/T}; T in °C per F. Its cover is an old template (סמסטר ב' תשס"ב) — we use our own cover
  - B's required analysis: part א density from a fit of m vs V (or m vs r); glycerin density from the areometer; temperature = mean of the Capstone log over 4 h. Part ב: fit א = v_f per ball from the data → v_f vs r → η, compare with B appendix א (Handbook graph, η(T), centipoise); fit ב = Colab exponential v(t) per ball → v₀, v_f → v_f vs r → η. Each fit has a "discuss pros and cons" question. B's appendix explains why τ is NOT used for η (30 ms frames vs τ ≈ 10 ms; derivative noise)
- [x] 4. Open questions from reading — answered by the user 2026-11-21:
  - [x] 4a. Fit ב (exponential v(t)) IS done: the staff never said otherwise to the user, so we follow B. (The forum question, todo 2, is another student's)
  - [x] 4b. Fit v_f vs r² (user). B says "v_f as a function of the radius"; formula (3) is linear in r²
  - [x] 4c. Temperature 23.116 ± 0.031 °C, from a group member (user didn't record it). Ran approved using it (2026-11-21)
  - [x] 4d. No calibration distance needed: the user set the axes/scale inside Tracker
  - [x] 4e. The 3 rows per category = 3 balls drawn at random, with replacement, from a pool of ~6–10 balls of that size; the dropped ball came from the same pool
  - [x] 4f. Sheet "ball x" = category x (user). Balls 3–6: distance calibration in Tracker was wrong, so their y values are not in cm. Major problem, no fix known yet; videos not kept, so no re-tracking (user, 2026-11-21) → Ran (2026-11-21): multiply the Y column of balls 3–6 by 21 cm / 1 m (Y only, not X); if it still doesn't work, write to him again. Check 2026-11-22 (sanity only, not for the report): after ×21, drop length ≈ 57 cm for all 6 balls, and mean speed / r² = 131–145 cm⁻¹s⁻¹ for all 6 (raw balls 3–6 would be 21× off)
  - [x] 4g. Ran confirmed both B typos (2026-11-21): "use what should be, not what B says" — the report uses the correct formulas (m = ρ_b·4πr³/3; buoyancy gρ_l·4πr³/3)
- [x] 5. Email sent 2026-11-21; Ran answered the same day (verbatim in instructor-questions.md); answers applied to 4c, 4f, 4g
- [x] 6. (committed on main 2026-11-22) Commit the viscosity work (todos.md, report-rules.md §2–3, instructor-questions.md, staff PDFs + theory-background-format.docx). PR #28 is merged; main is now the only working branch (2026-11-22). Branch to be decided with the user: main directly, or a viscosity branch
