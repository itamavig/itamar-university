# Viscosity report — experiment-specific rules

General rules for every report: [../report-rules.md](../report-rules.md); the source letters G, C, D, E, M are defined there. This file only adds what is specific to this experiment: don't copy a general rule here. Where this experiment needs a different rule, name the root rule it overrides and who decided.

Sources:
- Raw data: [viscosity measurements.xlsx](viscosity%20measurements.xlsx) (in the folder since 2026-11-16). Layout: see analysis/analysis.py (`part_a`, `ball_track`).

## 1. Limits

## 2. Instructor rulings (Ran, email 2026-11-21 — instructor-questions.md)
- Glycerin temperature: 23.116 ± 0.031 °C, taken from a group member's reading. Approved by Ran.
- Balls 3–6 (sheets "ball 3"–"ball 6"): Tracker's scale was left at 1 m instead of 21 cm. Multiply their Y column by 21 cm / 1 m (Y only). Units: their raw Y is in Tracker's "m" (stick assumed 1 m, really 0.21 m), so y[m] = raw × 0.21, i.e. y[cm] = raw × 21. Balls 1–2 are already in cm (scale set to cm in Tracker), so the analysis uses y_cm = raw × 21 for balls 3–6 and raw for balls 1–2. Check: ball 3 raw span 2.73 → 57.3 cm, balls 1–2 fall ≈ 58 cm. Sheet "ball x" = ball category x (user).
- Briefing typos (p.3 m = ρ_b·4πr³, p.2 buoyancy gρ_l·4πr³, both missing /3): use the correct formulas, not B's.

## 3. User decisions (2026-11-21)
- ~~Fit ב (exponential v(t), Colab) is done, as in B: the staff never told the user otherwise.~~ Reversed 2026-11-22 (user: "apparently we don't need to do the exponential fit"): no fit ב. v_f per ball comes from the velocity data only; one v_f–r² fit, one η. Goal 1 reworded to one method.
- v_f is fitted against r² (B says "as a function of the radius"; formula (3) is linear in r²).
- No calibration distance in the report data: the scale was set inside Tracker.
- Part-a sheet: the 3 rows per category are 3 balls drawn at random, with replacement, from a pool of ~6–10 balls of that size; the dropped ball came from the same pool.
- Hydrometer resolution is 0.002 g/cm³, not the 0.001 in the data sheet (user, 2026-11-22). Equipment list fixed; analysis.py overrides the sheet (HYDROMETER_RES).
