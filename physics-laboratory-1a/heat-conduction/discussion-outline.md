# Discussion outline (todo 13) — draft 2026-11-14, not in the report yet

Basis tags: [theory] staff theory, [Tamir], [data] plain observation of our data, [mine] Claude's own physics (must be labelled as ours in the report).
⚠ = depends on Tamir's answers to the new-briefing email (todo 17).

## 1. Were the goals met (rules 4.6.1)
- Uncorrected L = (2.421 ± 0.064)·10⁻⁸, Nσ 0.30 → agrees. Corrected L = (2.255 ± 0.060)·10⁻⁸, Nσ 3.1 → borderline disagreement. ⚠ A (solid rod?) and T (mean metal T?) can shift L by ~10%.
- Precision: σ 2.0%, κ 1.7%, L 2.6%.

## 2. Error sources tied to results (4.6.2)
- σ: the r_m term is 1.9 of 2.0% [data]. Lab notes: the stopwatch tends to overestimate t → σ ∝ t overestimated, systematic constant [lab notes/instructor].
- Part ב: χ²_red ≈ 2, p near 0.05, same residual sign pattern in all three fits [data].
  **New data finding:** at t = 0 (all sensors at room temperature) the sensors' readings minus their mean are −0.044, +0.096, −0.064, +0.076, −0.074, +0.036, −0.034, +0.006 K — the SAME alternating sign pattern as the fit residuals [data]. Suggests fixed sensor offsets (calibration) of ~0.1 K, comparable to the residuals. Only row 0 is usable (sensor 1 is already heating at row 2), and the logger resolution is 0.01 K, so this is one noisy reading. Sensor 1's residual (−0.15 K) is larger than its offset.
  Remaining hypotheses for sensors 1–2 [mine]: non-1D flow near the heater; position offset (~5 mm ↔ 0.19 K). ⚠ new briefing §2.2.3: "one sensor is in a different environment" — may be the staff's explanation.
- Part ג fits χ² 140 / 1200 / 25:
  - Ṫ_exp residuals look random, rms 0.0097 K; (0.0097/0.002)² = 23.4 ≈ χ²_red 25 → the whole χ² is explained by ΔT = 0.002 K being ~5× smaller than the actual scatter (logger resolution 0.01 °C) [data].
  - Cooling/heating residuals are arches: the rates are not constant [data]; Tamir said deviations from linearity can explain problems. The theory assumes constant P_loss [theory], but the heating slope falls from 1.18 to 0.94 K/min [data].
- The correction moves L away from theory (0.30σ → 3.1σ) [data]. Possible reasons: the constant-P_loss assumption [theory vs data]; the heating-window choice affects C. ⚠ Ṫ_exp method (new briefing part 4: non-linear fit).

## 3. Compare methods (4.6.3)
- κ uncorrected vs corrected; the three stability fits (κ 479.6–482.1, slope Nσ ≤ 0.22) [data].

## 4. Physical effects observed (4.6.4)
- 3-minute transient after switch-on, then all sensors heat at ~the same rate [data].
- Steady state reached in part ב (slopes stable over 200 s) [data].

## 5. Limitations / strengths (4.6.5)
- Only one cooling phase (instructor's procedure); the old briefing's second cooling would test equal losses [briefing 2025].
- Logger resolution 0.01 °C vs ΔT 0.002 K [data]. Strength: 8 sensors recorded simultaneously.

## 6. Improvements (4.6.6)
- Record all sensors at a uniform temperature for a few minutes before heating, to measure each sensor's offset and correct for it (follows from the t = 0 finding) [data → proposal].
- Add a second cooling phase after heating to test the constant-P_loss assumption.
- C sanity check vs m_rod = 0.58 kg [theory 2025] needs copper's c with a source — optional.
