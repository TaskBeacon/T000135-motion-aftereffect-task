# Stimulus Mapping

All implemented stimuli are concrete fixed-pixel adaptations; no physical calibration is implied. Conditions `left` and `right` differ only in phase progression sign.

## Mapping Table

| Condition | Stage/Phase | Stimulus IDs | Participant-Facing Content | Source Paper ID | Evidence (quote/figure/table) | Implementation Mode | Asset References | Notes |
|---|---|---|---|---|---|---|---|---|
| left |adaptation|patch_0/patch_1/patch_2/patch_3/fixation|Four soft patches of vertical stripes drifting left; stationarycentralcross|Bex1999|Exp1/Fig1translation|psychopy_builtin|config/config.yaml|30s,−4cycles/s; shared phase clock; fixed512pixel total field. |
| right |adaptation|patch_0/patch_1/patch_2/patch_3/fixation|Same patches/stripes drifting right|Bex1999|Exp1/Fig1translation|psychopy_builtin|config/config.yaml|Only phase direction changes:+4cycles/s. |
| left |static_test|patch_0/patch_1/patch_2/patch_3/fixation|Stationary carrier at actual last submitted phase/cross|Bex1999|Exp1stationary test|psychopy_builtin|config/config.yaml|No illusory arrows drawn or phase reset. |
| right |static_test|patch_0/patch_1/patch_2/patch_3/fixation|Stationary carrier at actual last submitted phase/cross|Bex1999|Exp1stationary test|psychopy_builtin|config/config.yaml|Identical geometry and actual last phase to adaptation. |
| left/right |fixation/recovery|fixation|Central darkcross on gray|Bex1999|Section3.2fixation|psychopy_builtin|config/config.yaml|Timing inferred; no gaze measurement. |
| left/right |instruction/block_break/good_bye|instruction/block_break/good_bye|Chinese static motion report instructions|Bex1999|Exp1button report|psychopy_builtin|config/config.yaml|SimHei,explicitlines,no correctnessfeedback. |

Accepted implementation modes:
- `psychopy_builtin`
- `generated_reference_asset`
- `licensed_external_asset`

Decision rule:
- Participant-facing text should be configured in `config/*.yaml` stimuli and referenced via stimulus IDs.

