# Task Logic Audit — Motion Aftereffect Task

Written from the user source and primary-paper methods before task code, 2026-08-31.

## 1. Paradigm Intent

Measure the reported persistence of apparent motion in a physically stationary texture after directional visual adaptation. The supplied Harris, Morgan & Still (1981), Nature, DOI 10.1038/293139a0 establishes the historic context; its observer-motion/visual–vestibular question is not the question implemented here. The publisher abstract and author-deposited abstract were read. Its scanned full text was located but not successfully rendered/read locally; no exact method parameters are attributed to its unread pages.

The direct operational source is Bex, Metha & Makous (1999), Vision Research 39, 2229–2238, DOI 10.1016/S0042-6989(98)00329-0, original-paper Methods/Experiment 1, p.2231, Fig.1 caption, and discussion section 3.2. The complete Methods/Experiment 1 text was read from the author-deposited full-text transcription (ResearchGate publication 12954675); the UCL PDF text was indexed and readable, but live downloads now return404. Source failure is retained, not represented as a downloaded PDF.

Only the translation subset is selected. Factors: adapting motion left/right. Outcome: button-reported static MAE duration, explicit no-MAE reports, and censored/missing reports. No threshold, nulling speed, recovery curve, clinical interpretation, vestibular manipulation, rotation/radiation comparison or normative benchmark.

## 2. Block/Trial Workflow

### Block Structure

Behavioral profile: 2 blocks ×4 trials; left/right equally represented per block, four observations per direction overall. Browser diagnostic profile: one block ×4 trials, same human timings. Native QA and simulation use four trials to exercise cessation, no-motion and missing branches; their explicit scaling/shortened timings are synthetic, not evidence that shortened adaptation induces MAE. Built-in BlockUnit.generate_conditions with label conditions and TaskSettings.resolve_condition_weights; null weights mean equal allocation. Seed135031, same-across-sub default; shared block seeds govern shuffling, with no task-local condition generator or hidden factor randomness.

### Trial State Machine

1. fixation: central cross on uniform gray, 1s, no responses.
2. adaptation: four stationary Gaussian envelopes in a plus arrangement; vertical sinusoidal carriers all drift horizontally in the assigned direction at4cycles/s for30s, central cross remains stationary. No response; adaptation must be validated from actual phase/flip or RAF submission evidence, not merely a requested stage duration.
3. static_test: same envelopes and same final carrier phase, immediately stationary. SPACE reports that apparent motion has ceased; N reports no apparent motion at any time. Up to30s; absent response is censored/ambiguous nonresponse, never automatically0 or a valid duration estimate. Response terminates test.
4. recovery: uniform gray fixation for60s, no response; this is an inferred washout duration, not an established return to baseline.

Instructions and inter-block rest require SPACE. No correctness/reward feedback. No countdown during adaptation/test. No nulling staircase and no top-up substitution: Experiment2's10s top-ups/1s test are not imported into Experiment1.

## 3. Condition Semantics

`left` and `right` select identical textures and amplitude envelopes, differing only in sign of carrier phase progression. These tokens are never participant labels. Four patches lie left/right/above/below the central fixation cross; all carriers have vertical stripes and translate coherently. Background and fixation remain stationary. Config owns Chinese instructions/key meanings and procedural grating specifications; actual phases are logged.

## 4. Response and Scoring Rules

SPACE: duration is static_test RT in seconds, labelled subjective stop-report latency including motor latency. N: no-MAE report, duration0 by explicit response meaning, with actual RT separately retained. Missing: duration null, test deadline and censoring flag retained; cannot distinguish persistent MAE from noncompliance. No objectively correct key, no reward, no hit-rate construct. Summary separates directions and excludes censored and technically invalid observations from finite means; reports censoring/no-MAE counts. `motion_valid` requires exposure within50ms of requested duration, no frame or static-transition gap greater than50ms, no runtime late-close and preservation of the actual final phase. Invalid reasons and raw reports are retained. These engineering limits are inferred, not psychophysically validated acceptance thresholds. Framework default hit fields must not be treated as perceptual accuracy.

## 5. Stimulus Layout Plan

The total field spans512×512pixels; four256pixel patches have centers ±128px on x/y, Gaussian sigma25.6px, carrier period32px, uniform8-bit gray128, nominal digital modulation0.4. These preserve Bex's geometry ratios (2° spacing,0.4° sigma,2cycles/degree) but are fixed-pixel adaptations, not angular calibration. No claim of photometrically calibrated40% contrast: monitor gamma and luminance are unmeasured. Central stationary cross12px, no texture motion at fixation. Chinese instruction paragraphs explicitly line-broken, SimHei24px, wrap1100px on1280×800 window. Windows with either dimension below600pixels are rejected to avoid silent rescaling. Real render capture is required; the local front-buffer/OS screenshot limitation is disclosed separately.

## 6. Trigger Plan

Proposed mock acquisition codes: experiment1; fixation10; adaptation20; static_test30; stopped31; no-MAE32; timeout39; recovery40; experiment-end99. Responses/onsets/timeouts flow through StimUnit. This is software event logging, not EEG hardware verification.

## 7. Architecture Decisions (Auditability)

Canonical T is authored first. Main mode-aware orchestration uses public PsyFlow. Trial is a thin four-phase sequence. Pure scoring may live in a focused helper. Initial MovieStim strategy was rejected after five real bounded canaries: noAudio constructor override, two broken public frame-rate getters, paused decoder first-frame timeout, and final-PTS failure after30s. The valid generated MP4/finalPNG materials and all failures are retained as feasibility evidence, not used as completed acquisition.

The revised strategy, approved before task implementation, is a narrow shared-runtime opt-in drifting GratingStim/Gabor primitive. Native StimBank typegrating maps to public PsychoPy GratingStim; show.phase_drift_hz updates its public phase in the framework draw loop from a common monotonic clock. Web uses shared canvas Gabor rendering and the same optional show operation, with common stageRAF time. Both use the target equation: normalized gray=0.5+0.5*C*Gaussian(x,y)*cos(2*pi*(sf*x-phase)), where positive phase drifts right. Carrier period32px, Gaussian sigma25.6px, patchsize256px (5sigma to each edge), four centers±128px. Native texsin at texturecenter0.5 is the cosine peak; subtracting phase from texturecoordinates yields the same sign. Gaussian maskParams.sd=5 corresponds to edge5sigma. Alpha/texture interpolation/pixel-grid differences require actual image comparison, not a byte-identical claim. Static test reuses the actual final phase; no phase reset and no codec transition.

Native anticipated-flip phase times and actual flip timestamps, and webRAF phase times/intervals, must be retained and validated independently of requested duration. Refresh is not assumed to be the source75Hz. No task-local draw or timing loop; new shared branches must be independently reviewed and published before final task validation. Default existing paths remain unchanged. Software evidence does not establish hardware luminance/onset or perceptual MAE.

## 8. Inference Log

- Translation-only, plus arrangement: selected subset of Bex Fig.1 and Experiment1, not full replication.
- Pixel geometry/digital gray values/refresh-dependent frame sampling: documented display adaptation; physical degrees/cd/m²/contrast cannot be asserted. Unlike the rejected60fps MP4 candidate, the procedural grating does not impose a60fps movie grid. At a60Hz display4cycles/s has approximately15refresh samples per cycle; actual gaps and phase increments are retained.
- SPACE/N distinction: explicit no-effect response added to avoid guessing that fast stop presses imply zero effect.
- 30s test ceiling: inferred bounded acquisition; censoring semantics preserve ambiguity. Original Experiment1 reports pressing at cessation but does not specify this ceiling.
- 60s recovery,1s fixation,2×4-block organization,seed,key choice,Chinese wording: inferred implementation values. Recovery is not verified washout.
- Eye fixation is instructed, not eye-tracked. Synthetic testing cannot establish that a human experiences the MAE.
