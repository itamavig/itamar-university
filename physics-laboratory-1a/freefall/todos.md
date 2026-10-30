# Free-fall lab report — todos

Rules: [../report-rules.md](../report-rules.md) (general) + [report-rules.md](report-rules.md) (free fall). Doc gaps: [report-gaps.md](report-gaps.md).

- [x] 1. Read all guideline files, write compact rules (2026-10-26)
- [x] 2. Get cover template, Doc, limits, instructor email; split rules into general + free fall (2026-10-26)
- [x] 3. Get the two Colab notebooks as .ipynb files — saved in colab/ (2026-10-26)
- [x] 4. Formula budget approved with the analysis plan: (3)–(9), no words-only formulas (2026-10-28)
- [ ] 5. Cover-page details: experiment date, submission date, instructor full name, IDs, track, group, sub-group, station
- [x] 6. LaTeX toolchain: XeLaTeX + polyglossia, Times New Roman for Hebrew; skeleton in report/ with cover, numbers.tex, figures, results table; `make` builds all (2026-10-26)
- [x] 7a. Doc ledger + check script (analysis/doc_ledger.py, `make doc`); theory, results table and figures tagged (2026-10-26)
- [ ] 7. Fill sections from the Doc in Doc order, rephrase only; per section: tag, check n/n, show side-by-side for approval. Done: THEO, GOAL, SETUP, EQUIP (except EQUIP-05), PROC, PLAN, RES, QUEST (approved 2026-10-29), DISC (approved 2026-10-29, DISC-43/44 red for the pair), appendix raw-times table (2026-10-29). All sections written.
- [x] 8. Local script analysis/analysis.py → report/figures/*.pdf + report/numbers.tex; verify_colab.py compares to notebook outputs (2026-10-26)
- [x] 8b. Verification standard = option 1 (user, 2026-10-26): local script runs the fits; check passes when every rounded report value equals Colab's. verify_colab.py: 23/23 match
- [x] 8a. Skipped row numbers = heights 25/35/55/65/75 cm never measured (empty template rows); no data dropped
- [ ] 9. Raise the content issues in report-gaps.md with the partner
- [x] 9a. Optical gate decided 2026-10-29: it starts the timing (briefing + DISC-36); item 9 in the list, setup and procedure updated in blue. Was: decide the optical gate (EQUIP-05) — was it used? It's in the briefing's list but not in the schematic or the Doc's procedure. Stays `todo` in the ledger so `make doc` keeps flagging it. Also in report-gaps.md.
- [ ] 9b. **Before submitting:** no blue (`\added`) or red (`\TODO`) text left — review each blue passage with the partner, then drop the macro.
- [x] 9c. Auto-upload of the PDF to the shared Drive folder on every rebuild (2026-10-29; overwrite = new version, verified)
- [ ] 10. Run the checklist (general rules §8) against the compiled PDF — first run 2026-10-29: 5 fails, see checklist-results.md. Re-run after fixes.
- [x] 10a. Optical gate drawn in figure 1 as a blue overlay (TikZ over the image, in an LTR block), label 9 (2026-10-29)
- [ ] 10b. Decide: number the theory's g_theoretical display formula or leave it as in the staff file

## Partner's notes (2026-10-30) — one by one, edits in green (`\partner{}`)
- [x] P1. (approved 2026-10-30: goal 1 split into (א)–(ד), (א)–(ב) = initial height and velocity match zero, green sentence in the comparison referencing 1א/1ב) Goals: verify the model (parameters vs expected values, fit statistics), not only g
- [x] P2. (approved 2026-10-30: "עמוד אלומיניום עם שנתות", list + setup) Equipment item 3: replace "מדורג" with clearer wording
- [x] P3. (approved 2026-10-30: timing sentence removed, gate added to the parts sentence) Setup paragraph: drop the timing sentence that repeats procedure step (ה); keep component roles and h (guide)
- [x] P4. (approved 2026-10-30: motor calibration run with an anemometer, u = a_w·t_d (Δ reserved for errors), average of repeated runs) Instructor question ב: how the estimate is taken (repeat + average + error) and how the wind's acceleration is known
- [x] P5. (approved 2026-10-30: 7 sentences reworded in green, 3/4/6 in the user's chosen wording) Discussion: smoothing pass for stiff wording, meaning unchanged
- [x] P6. (approved 2026-10-30: chronological height-then-time refit argument, numbers from analysis.py) Discussion: rewrite DISC-43/44 — time error as main cause of the overestimate (data: no Δt → χ²_red 1.7)
- [x] P7. (approved 2026-10-31: numbered list of 4; item 4 camera tracking is the user's, green, flagged vs guide's 'no sophisticated means') Improvement suggestions: expand, each tied to a result (guide forbids "more measurements", "finer ruler")
- [ ] P8. Ask Tamir: g in m/s²? (user/partner task; switch in analysis.py if yes)
- [ ] P9. Compare with other reports from the Drive (user/partner task; guide wins on conflicts)
