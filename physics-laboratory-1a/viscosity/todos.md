# Viscosity lab report — todos

Rules: [../report-rules.md](../report-rules.md) (general) + [report-rules.md](report-rules.md) (viscosity).

## Setup
- [x] 0. Folder scaffolded from ../_template/ (2026-11-21, commit 2935357). Raw data `viscosity measurements.xlsx` in the folder since 2026-11-16
- [x] 1. Staff files from Moodle (course 03211111, section "צמיגות") into this folder — done 2026-11-21: user downloaded them, moved here; sizes match Moodle byte for byte; theory PDF 4 pages, briefing PDF 10 pages, both have a text layer; docx zip intact
  - Files: `רקע תיאורטי צמיגות תשפב.pdf` (628,644 B), `תדריך עבודה צמיגות תשפז.pdf` (838,443 B), `פורמט רקע תיאורטי צמיגות - חדש.docx` (18,338 B; saved as `theory-background-format.docx`, as in freefall/ and heat-conduction/)
  - Not files: "דוח מעבדה צמיגות" is the upload assignment (due: two weeks from the day the experiment was done, no attachments); "תוכנת Tracker" links to https://physlets.org/tracker/
  - 2026-11-21: the built-in browser pane cannot save downloads (no file in ~/Downloads, direct navigation refused, and a 127.0.0.1 receiver got no request). Waiting on the user: Claude in Chrome, or the user clicks the three links
- [x] 2. DROPPED 2026-11-22 — user: the forum is not a reliable source, never treat it as one. Old note kept for history: Moodle Q&A forum "שאלות תשובות - צמיגות", read 2026-11-21: one student question (16.11.2026, 0 replies) — the briefing looks old: its exponential v(t) fit (V0, Vf) is not needed? Proposed fits: (1) mass vs volume, linear → density; (2) position vs time, linear → terminal speed; (3) speed vs R², linear → η. Re-check for a staff answer before planning the analysis
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

## Writing the report (draft 2026-11-22, for the user's morning review)
- [ ] 7. Goals, theory, system, equipment list, stages written in report/main.tex. Blue = Claude's text, red = waiting for the user. PDF: 4 pages (cover + 3), builds clean
  - 7a. APPROVED 2026-11-22 (user). Goals: staff goal (B p.1) split into 2 falsifiable goals — η from both fits matches theory; v_f linear in r² (Stokes)
  - 7b. Theory: F verbatim, formulas (1)–(6) numbered as in F. Red spots (fix or keep verbatim?): "שוות;" (semicolon, rule 2.4a), "הנקראת" → "הנקראות", "מהמהירות הקריטיות" → "הקריטית", "נסוני" → "ניסיוני", "צמיגיות" → "צמיגות", "אמיפריים" → "אמפיריים". Not flagged, verbatim: (1) uses u for velocity while (3)–(4) use v; (5)–(6) give T in °C
  - 7c. Equipment list (user review 2026-11-22): ruler 1 mm; temperature sensor 0.001 °C, inferred from the last digit of 23.116 per user; "דיגיטליות" → "דיגיטליים". Still red: tube length and inner diameter (not in B, T, F or the data file; user asked to add them)
  - 7d0. System paragraph APPROVED 2026-11-22 (user)
  - 2026-11-22: goals, system paragraph, figure caption and equipment list turned black (approved). Tube length/diameter stay red, blank for now (user: "for now it stays blank"; not in any staff file) — picked up in 7g
  - 7g. Tube dimensions: user to supply, or drop them, before submission
  - 7d. Schematic figure: Claude's TikZ drawing (side view), no photo in B fits
  - 7e. Stages — please confirm (red in PDF): temperature measured as B says (Capstone, mean over 4 h, one computer)? 21 cm = distance between the height markers, measured with the ruler? Also review: stage ב4 states that balls 3–6 kept Tracker's default 1 m and were corrected per the instructor
  - 7f. Not written yet: frame counts / drop length (to come from analysis.py, not typed by hand)
  - 7h. Photos (user, 2026-11-22: "photos and schematic"): IMG_8522–8524 from the user, cropped/compressed into report/figures/ (8522 rotated upright). Fig. 2 = tube + camera, fig. 3 = part א instruments; numbered labels placed by Claude. New equipment item 13: magnet + ferromagnetic needle for holding the balls (user's explanation). APPROVED and turned black 2026-11-22 (user). Not in any photo: hydrometer (6), ruler (7), temperature sensor (11)
  - 7i. Stages rewrite (user review 2026-11-22): א2 rephrased; ב2 confirmed by user — 21 cm measured once with the ruler (red removed); ב3 rephrased; ב4: "מקל הכיול" dropped (B itself only says "Calibration Stick" in English), manual corrections in Tracker added (user), mis-calibration stated as "הכיול לא עודכן" without "עקב טעות אנוש". Still blue; א3 temperature confirmation still red (7e)
  - 7j. 2026-11-22: א3 temperature method confirmed by user (red removed; 7e closed). ב4: Excel-copy sentence dropped — the analysis section shows the data is processed; the correction sentence doesn't need it
  - 7k. 2026-11-22: theory typos kept verbatim (user: "keep theory as is"; 7b closed). Tube dimensions dropped from item 1 (user); question parked in instructor-questions.md "For the next email" (7g → next Ran email). Stages approved → black. Fixed a semicolon Claude had put in stage ב4 (rule 2.4a)
- [ ] 8. Analysis plan — DRAFT in main.tex (blue), 2026-11-22. Formulas (7)–(16), 10 of 18. Waiting on the user's 5 decisions (red in PDF):
  - 8.1 Δt and Δy of the Tracker data (B step 3)
  - 8.2 velocity derivative: central or forward difference
  - 8.3 fit א: how to extract v_f (mean of v vs linear y(t)) + deterministic rule for the terminal region (B step 4)
  - 8.4 g value, its error and source (no viscosity staff file gives one)
  - 8.5 theoretical η at 23.116 °C from B appendix א graph: read directly / fit formula (5) to the marked points / linear interpolation 20–25 °C
  - Also for review (blue, Claude's choices): density fit over all 18 balls (m vs V); dropped ball's radius = category mean with stat+res error (11); τ not used for η (B appendix p.8); initial guesses for fit ב
  - Then: analysis.py (todo 9, not started)
  - 7l. 2026-11-22: formula references are clickable links (hyperref [hidelinks], no colour/font change; user). Theory "(2)", "(5)" now qref, same output. Booklet refs ("בחוברת") stay plain. Check: 12 refs in source (11 qref + 1 
ef) = 12 links in PDF, all to the right pages
  - 8.0 2026-11-22: plan intro reworded (user): test the v_f–r² relation first; only if it holds does the slope represent 2g(ρ_b−ρ_l)/(9η), so η is extracted only then — stated as a physical reason, not a choice
  - 8.6 2026-11-22: plan intro APPROVED → black. Part א rewritten per category (user): m̄, d̄ = mean of the 3 balls, error = stat (D32, D34) + resolution (D28) combined by D35, one adapted formula (7) for both. V, ΔV from r̄. Density fit now over the 6 category points (was 18 balls). Dropped ball radius = r̄ of its category (old separate formula removed). Still 10 numbered formulas
  - 8.7 2026-11-22: formula (7) (D35 combined error, written out) removed — cited in words (user; rules §3.8). Conflict in report-rules.md recorded at §3.7: plain D(35) is not written, overrides §3.7 + checklist line. Plan now (7)–(15), 9 of 18
  - 8.8 2026-11-22 (user): final combined error not written (D35 in words). Indirect errors ARE written, with this experiment's quantities (recorded in report-rules.md §3.7). Radius: r̄ = d̄/2 ± Δd̄/2 numbered as (7) — one formula for the value and its indirect error (Claude's judgement, user delegated). Plan (7)–(16), 10 of 18
  - 8.9 DONE 2026-11-22 (user: "Card + lint"): rules card = physics-laboratory-1a/CLAUDE.md; lint = labtools/lint_report.py, run by `make` before LaTeX (common.mk $(LINT), FORMULA_LIMIT in each Makefile; `make FINAL=1` also fails on blue/red). Tested: synthetic file fires all 9 checks, suppression and theory exemption work; an injected semicolon stops the viscosity build; viscosity lints clean (10/18). freefall/heat-conduction (submitted, not hooked) show 3 and 10 real hits — left as they are
  - 8.10 2026-11-22 (user): V and ΔV merged into one formula (8). m = ρ_b V numbered (9) as the fitted model (rules 3.7). Axes of all 3 fits described in words + symbol, per G p.3 (also added to report-rules §4.4.2 and the rules card). Still 10/18
  - 8.11 2026-11-22 (user): r̄² and its error merged (14), η and Δη merged (15). 9/18
  - 8.12 2026-11-22 (user): bars dropped from m, d, r — "המסה m והקוטר d של כל קבוצה יחושבו כממוצע" defines them as group means; r now matches the theory symbol in (3)
  - 8.13 2026-11-22 (user): plan part א temperature = as in the procedure (mean over 4 h), no numeric value in the plan (card rule)
  - 8.14 2026-11-22: plan part א APPROVED → black
  - 8.15 2026-11-22 (user): Tracker y origin never set and differs per video (ball tracked from varying heights) → y meaningful only relative within a video; plan uses only y differences (velocity). Tracker time starts at video start, before the drop → t shifted to first tracked frame. Both in plan part ב (blue)
