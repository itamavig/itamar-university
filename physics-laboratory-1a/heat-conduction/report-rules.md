# Heat-conduction report — experiment-specific rules

General rules for every report: [../report-rules.md](../report-rules.md). This file only adds what is specific to heat conduction.

Sources (copied from ~/Downloads on 2026-11-02, byte-identical):
- `B` = [הולכת חום - תדריך ניסוי.pdf](הולכת%20חום%20-%20תדריך%20ניסוי.pdf): the briefing (5 pp, 2025-02-17).
- `T` = [הולכת חום רקע תיאורטי.pdf](הולכת%20חום%20רקע%20תיאורטי.pdf): the full theory background (4 pp, Shir Aviram, Word export 2025-08-19)
- `F` = [theory-background-format.docx](theory-background-format.docx): old cover page (סמסטר ב' תשס"ב) + a condensed theory section (created 2016, last edited 2024-06-01 by Shir Aviram)
- `N` = [lab-notes.md](lab-notes.md): the user's notes from the lab, verbatim (pasted 2026-11-04). The instructor's in-lab instructions; on conflicts with B, ask the user.
- **No Google Doc** (user, 2026-11-04): the user writes this report alone, without the partner, directly in this repo. No doc ledger. The content comes from the user, sources B/T/F/N and the data.
- Raw data (measured 2026-11-02, read 2026-11-04): [heat conduction part a.xlsx](heat%20conduction%20part%20a.xlsx), [part b](heat%20conduction%20part%20b.xlsx), [part c](heat%20conduction%20part%20c.xlsx). See §5b.
- Colab notebooks: unknown whether any exist for this experiment

## 1. Limits (user, 2026-11-02)
- **Page limit: 12, cover + appendices excluded** (user confirmed 2026-11-05).
- **Numbered-formula limit: 16, including the theory formulas (1)–(5)** (user, 2026-11-05; unlike free fall, where they were excluded). Stricter than G p.1, which excludes theory formulas ("לא כולל הנוסחאות מהרקע התאורטי"); report finished, left as is (conflict C2, 2026-11-22).

## 2. Theory: F vs T (compared 2026-11-02)
- F's theory section is a **condensed copy of T**: the same sentences, the same numbered formulas (1)–(5), and nothing that T lacks.
- Free-fall precedent: the report's theory section = the staff docx word for word. If we do that here, F gives 5 numbered + 3 unnumbered display formulas (the value of L, the f and μ₀M values, P_avg before (5)).
- Only in T: section headings (מבוא, מוליכות חשמלית, חלק א, חלק ב), the eddy-current explanation, v_terminal and t = L₀/v, the units of σ, P = VI, the derivation of C and P_loss, m_cyl = 0.58 kg.
- Only in F's wording: "הביטוי בנוסחה מס׳ (3) לאחר תיקון מסדר ראשון". T says "the relation above", which is formula (4).
- Typos in both: "אובייקט חם מצד אחד ואובייקט חם מצד שני" (one side should be cold), "נחושות", "קבועה בולצמן". Only in T: "נוחל" (נוכל), "המוליכות הסגולית" (should be specific heat capacity).

### Formulas (T numbering)
- (1) κ = LσT. Wiedemann–Franz. L = (π²/3)(k_B/e)² = 2.44·10⁻⁸ V²/K² (unnumbered).
- (2) σ = 8mga²t / ((μ₀M)² π r_m⁴ L₀ w · f(d/a)). With f(d/a) ≃ f(2) ≃ 1.75 and μ₀M = 0.65 T. Comes from t = L₀/v_terminal (T only).
  - m = magnet mass, a = tube inner radius, w = tube wall thickness, r_m = magnet radius, d = magnet height, L₀ = tube length, t = fall time.
- (3) P(x)/A = −κ dT/dx.
- (4) T(x) = T(0) + (P/(κA)) x, at equilibrium with no side losses (P(x) = P = P_in). The text has a + sign. With (3) the slope should be −P/(κA) if x runs from the hot end. **Open: sign / direction of x.**
- P_avg = P_in − (P_absorb + P_loss)/2 (unnumbered).
- C = P_in / (Ṫ_heat − Ṫ_cool), P_loss = −C Ṫ_cool, P_absorb = C Ṫ_exp (T only, unnumbered).
- (5) P_avg = [1 − ½ (Ṫ_exp − Ṫ_cool)/(Ṫ_heat − Ṫ_cool)] P_in. Ṫ_exp = the rate of temperature change during the part-ב measurements.
- P_in = VI (T only).

## 3. Goal
- **Given by the staff (user, 2026-11-04), used verbatim:** "בניסוי זה נמצא את קבוע לורנץ מחוק וידמן-פרנץ ע״י מדידת המוליכות החשמלית ומוליכות החום של נחושת."
- B: examine heat conduction in copper and verify the Wiedemann–Franz law.

## 4. Equipment (B; resolutions still needed)
1. Copper tube 2. Small magnet 3. Insulated copper rod with temperature sensors along it 4. Power supply GPD-43038 5. Digital temperature/time meter 6. Aluminium pot with a heat exchanger on the lid 7. 2.5 L water 8. Cables 9. Caliper 10. Ruler 11. Electronic scale.
B's figure 1 labels parts 1, 2, 3, 6, 7, 8.

## 5. Procedure (B) — three parts
**Part א: σ from the magnet's fall through the copper tube.**
- Measure with the caliper: magnet diameter, tube inner and outer radius (w = outer − inner). Measure the tube length with the ruler. Weigh the magnet on an upturned cup (keeps the magnet away from the scale).
- Tube vertical. Drop the magnet from the top and time it with a stopwatch. **10 repetitions.**
- **Gap:** formula (2) needs the magnet height d, but B does not list measuring it.

**Part ב: κ at equilibrium.**
- Rod screwed into the pot lid (water reservoir = roughly constant temperature at one end). Power supply Ch1+ / GND to the rod (the rod is the heater resistor). Limits: **9 V, 0.7 A**. Turn on Output only with the instructor's approval.
- Reset the stopwatch (hold ~5 s), wait **~15 min (900 s)** for equilibrium, record all 8 sensors. Repeat twice at 100 s steps: **3 readings in total.**
- Sensors T1–T8 at **15, 40, 65, 90, 115, 140, 165, 190 mm** (25 mm spacing; B figure 4). **Open: which end is x = 0 (heater or water)?**
- Expected: 3 linear graphs of T vs sensor position, slopes about equal. Then κ and L.
- B calls the rod "צינור הנחושת" in parts ב and ג. It is the rod (item 3), not the tube from part א.

**Part ג: first-order correction.**
- Disconnect, take the rod off the pot lid, cover its lower end with insulation, reconnect.
- Measure the middle-of-rod temperature = mean of sensors 4 and 5:
  - First cooling: every 60 s for 7 min (8 readings).
  - Heating: power on, wait 1 min, every 20 s for 5 min (16 readings).
  - Second cooling: power off, wait 1 min, every 60 s for 7 min (8 readings).
- Expected: 3 linear graphs of T_avg vs time, the two cooling slopes about equal. Then C and P_loss from the slopes, P_avg from (5), corrected κ and L, compared with part ב.

## 5a. From the lab notes (N, 2026-11-04)
**Part א, measurements and repetitions:**
| Quantity | Repetitions |
|---|---|
| magnet mass m | 4 |
| fall time t | 10 |
| magnet "radius" | 4 |
| channel ("תעלה") "radius" | 4 |
| tube thickness w | 4 |
| tube length L₀ | 1 |
- **All the "radius" measurements are diameters.** a (and r_m) are radii, so divide by 2.
- **Magnet height d = magnet diameter** ("הקוטר שווה לאורך"). This closes gap 1: d is not measured separately. Check: d/a = 2r_m/a, so f(d/a) ≃ f(2) holds when r_m ≈ a.
- Repetition counts come from B or the instructor: the report names that source in one clause instead of justifying N (root §4.3.4; conflict C3, 2026-11-22).
- **Time is overestimated:** the stopwatch is never stopped before the magnet has finished falling. This is neglected, but it can help explain the errors (discussion).

**Part ב:**
- Measure I and V, then P_in = VI.
- The rod's area is computed from the earlier measurements ("לחשב שטח פנים של המוט לפי המדידות הקודמות"), and then κ.
- T(0) comes from the fit's intercept, not a guess.
- **T in (1) = room temperature, 24 °C = 297.15 K, error 1 K.** This closes gap 5.
- Errors: sensor position **2 mm**, temperature **0.002 K**.

**Part ג:**
- Ṫ_cool = the rate at which the metal cools, with energy only leaving the system (consistent with T's 0 = P_loss + C Ṫ_cool).

## 5b. The data files (read 2026-11-04)
**Part a (sheet `measurements`)**, each block = quantity, value, resolution:
| Block | Values | Res | Note |
|---|---|---|---|
| magnet mass m | 1.27 g ×4 | 0.01 g | |
| fall time t | 18.43–18.83 s ×10 | 0.01 s | |
| magnet height (d) | 5.99, 5.88, 5.98, 5.90 mm | 0.01 mm | N: magnet diameter = height → r_m = d/2. No separate magnet-diameter block |
| tube radius (a) | 6.01, 6.03, 6.06, 6.00 mm | 0.01 mm | **diameters** (N) → a = D/2 ≈ 3.01 mm |
| tube diameter | 19.91, 19.98, 19.95, 19.98 mm | 0.01 mm | outer diameter. Cell E41: the caliper arms were pressed against the plastic protection, assuming its edge is perpendicular to the tube |
| tube length | 20 cm ×1 | 0.1 cm | = L₀, also the rod length in parts ב/ג (sensor 8 at 190 mm) |
| current I | 0.589 A ×1 | 0.001 A | below the 0.7 A limit |
| voltage V | 8.999 V ×1 | 0.001 V | |
- **§6 Q13 settled by the data:** the 4 "w" values in N are the outer diameter. w = (D_tube − D_channel)/2 ≈ (19.96 − 6.03)/2 ≈ 6.97 mm (rough means, for orientation only).
- Check: d/a ≈ 5.94/3.01 ≈ 1.97, consistent with T's f(d/a) ≃ f(2).

**Parts b and c (sheet `Temperature Data` + `Recording Info`):** a continuous log, one row every 5 s (0.2 Hz). Columns: Time (datetime), Sensor 1–8 (°C, 2 decimals), VCC (≈ 3.25, the logger's supply voltage, not used).
- **Part b:** 542 rows, 14:55:29 → 15:40:33 (2706 s). Starts at room temperature (23.4–23.6 °C), heating from t = 0. Sensor 1 is the hottest (36.10 °C at the end), sensor 8 the coldest (29.50 °C) → **sensor 1 is at the heater end.** The center (mean of sensors 4, 5) is still rising at the end, about +0.02 to +0.05 K/min: near equilibrium, but not at it.
- **Part c:** 367 rows, 16:05:39 → 16:36:09 (1834 s). Rod at a uniform ~32.3 °C at the start.
  - Cooling: 0 → ~905 s (~15 min), center −0.11 to −0.22 K/min (noisy at 30 s steps).
  - Heating: from ~905 s to the end (~15 min), center from +1.2 K/min falling to +0.92 K/min, so not exactly linear.
  - **No second cooling phase in the file.** B asks for cooling 7 min, heating 5 min, cooling 7 min.

## 6. Open questions (not decided — ask, don't guess)
**Not in B, but the user remembers a caliper step for them (2026-11-02).** Rechecked on 2026-11-02: the full text of B and T, plus B's pages 1 and 3 as images (figures 1–4 included). B's only caliper step is "מדדו את קוטר המגנט ואת הרדיוס הפנימי והחיצוני של צינור הנחושת". The step may be in the Doc, the data sheet or the lab station. Check those when they arrive:
1. ~~The magnet height d~~ **closed by N (2026-11-04): d = magnet diameter.**
2. The rod's diameter, needed for the cross-section A in (3)–(4). N says the area comes "from the earlier measurements". Partly open, see questions 9–10.

**For the user to ask the instructor (2026-11-02):**
3. ~~Actual V and I~~ **answered by N (2026-11-04): I and V were measured, P_in = VI.** Still to check in the data that both values are recorded.
4. The sign in (4) and the direction of x (see §2). Figure 4 puts x = 0 at the left end, which has a red mark and a short stub. The figure does not say whether that end is the heater or the water.
5. ~~Which T goes into (1)~~ **answered by N (2026-11-04): room temperature, 24 °C ± 1 K.**

**Still open:**
6. Ṫ_exp: taken from the 3 part-ב readings 100 s apart, or from somewhere else?
7. Resolutions of the stopwatch, the caliper, the ruler, the scale and the temperature meter.
8. Do the theory formulas count toward the 16?

**Raised by N (2026-11-04), answered by the user the same day:**
9. **Rod = an identical tube** (the user, 2026-11-04; refined the same day while reviewing the procedure: "צינור זהה"). Parts ב/ג use a second copper tube, identical to part א's, so its area comes from the part-א measurements. Report equipment: item 1 = part-א tube, item 2 = the identical insulated tube with the sensors, item 3 = heater.
10. The area in (3)–(4) is the **cross-section** (the ring you see when the tube is cut across its length), not the surface area ("שטח פנים"). Explained to the user 2026-11-04. A = π((a+w)² − a²) = π(R² − a²). The user hasn't yet confirmed using this in the report.
11. **"החוטר"** = the thin cylinder kept inside the tube's channel to preserve it. Its diameter is assumed equal to the channel's diameter, so the channel diameter (→ a) is measured on the חוטר.
12. **"רדיוס התעלה"** = the radius of the channel inside the tube = a (measured as a diameter, divide by 2).

**Geometry (confirmed with the user 2026-11-04):** the tube is a cylinder with a coaxial cylindrical channel running between the two bases. **Correction given to the user:** the wall thickness is w = (D_tube − D_channel)/2, not D_tube − D_channel, because the wall appears on both sides of the channel.
**B is outdated on procedure (user, 2026-11-04).** For how the measurement was done and processed, the data + N + the instructor win over B (a per-conflict user decision, see root precedence line). B still describes the equipment and goals.

**Raised by the data (2026-11-04), answered the same day:**
14. Part b: **all rows are used**, not 3 readings. The instructor mentioned that some step uses only the "semi-equilibrium" part. The user isn't sure which step. **Open:** formula (4) holds only at equilibrium, so the T-vs-x fit is the step it most likely applies to. Where the semi-equilibrium starts is not decided (wait for the notebook template, or ask the instructor). No window will be picked by eye.
15. Part c: **cooling 15 min, then heating 15 min, on purpose; the whole intervals are used.** The switch-on row, found deterministically: sensor 1 (heater end) first rises at row 182 (t = 899.88 s; 30.12 → 30.19 → 30.60). **Cooling = rows 2–181 (0–894.87 s), heating = rows 182–368 (899.88–1834.29 s).** Fact for the user: the center (sensors 4, 5) lags. Its first rise is at row 186 (~920 s). B's "wait 1 min" was about this.
16. Part c: **one cooling only, by design.** (B's second cooling is outdated.)
17. Temperature: **total error 0.002 K, given by the instructor.** 0.01 °C = the logger's resolution (2 decimals). Fact for the user: a 0.01 resolution alone gives 0.01/√12 ≈ 0.0029 K by D(28), more than 0.002 K. Using the instructor's value as given; mention only if the user wants.
18. **Ṫ_exp is a rate** (K/s), not a temperature. Settled by units: P_absorb = C·Ṫ_exp must be in W, and C is in J/K. T: "קצב שינוי הטמפרטורה שהיה בזמן המדידות של חלק א" (T's part א = the briefing's part ב). Taken from the part-b log, in the (semi-)equilibrium stretch. The exact window ties to question 14. The temperature *value* at equilibrium is not used here. The T in (1) is room temperature (N).
19. **Colab:** there is a standard template to adjust slightly. The user will upload it. Proposed workflow (free-fall precedent): fit code copied verbatim into a local analysis.py, plus one Colab run as a cross-check. **Open:** whether the course requires submitting the notebook itself.

13. **Answered 2026-11-04: w came from the diameters** → **w = (D_tube − D_channel)/2**. Error by propagation from both diameters (D(39)-type, cite by number). When the data arrives, check what the 4 recorded "w" values are: the outer diameter D_tube, or the difference D_tube − D_channel. Either way the /2 applies.
