# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| adaptation | timing.adaptation_duration |30s every trial|Bex1999|Methods Exp1 p2231|direct|Actual phase/timing exposure independently validated; runtime requested duration alone insufficient. |
| waveform | stimuli.patch_0 through patch_3 |Four Gaussian-windowed vertical carriers in plus layout|Bex1999|Methods/Fig1caption|adapted|Translation-only subset. |
| motion | task.temporal_frequency_hz |4cycles/s,left/right|Bex1999|Methods p2231|direct|Refresh-dependent samples (~15/cycle at60Hz); source75Hz not replicated. |
| geometry | stimuli.patch_*.pos/size/sf/maskParams |centers±128px,sigma25.6px,period32px|Bex1999|2deg spacing,0.4deg sigma,2cpd|adapted|Pixel ratios only; angular extent uncalibrated. |
| amplitude | stimuli.patch_*.contrast |0.4 around gray128|Bex1999|40%contrast,calibrated55cd/m²|adapted|Digital modulation; gamma/physical contrast unmeasured. |
| outcome | task.report_keys |SPACE=ceased,N=none from start|Bex1999|Exp1button report at cessation|adapted|Explicit no-MAE category added; no accuracy. |
| test | timing.test_duration |30s maximum|Bex1999|Stationary test; no ceiling specified|inferred|Omission censored/ambiguous, never duration0. |
| repetition | task.total_blocks / trial_per_block |2×4,four/direction|Bex1999|Exp1four estimates/condition|adapted|Grouping/randomization inferred; perblockbalance. |
| fixation | timing.fixation_duration |1s|Bex1999|Section3.2central cross|inferred|Retained during adaptation/test; eyes not tracked. |
| recovery | timing.recovery_duration |60s|Bex1999|Exp1exact intertrial interval unavailable|inferred|Chosen rest; return to baseline not verified. |
| language | stimuli.*.font |Chinese/SimHei|Bex1999|Localized instructions|inferred|Participant wording in YAML. |
| render | stimuli.patch_*.type |shared procedural grating|Bex1999|Gaussian-windowed sinusoidal carrier|adapted|Phase controlled in shared framework; final actual submitted phase held static. Movie candidate rejected, not active. |
| validity | task.max_frame_gap_s |0.05s technical timing tolerance|Bex1999|Not specified by source|inferred|Excess exposure error/frame gap/transition gap, lateclose or phase discontinuity invalidates motion report. |
