# Task Plot Brief

Title: Motion Aftereffect Task
Construct: motion adaptation

Evidence: stable canonical main.py, src/run_trial.py, src/utils.py, config/config.yaml, README.md; five native gates passed in validation/gates-attempt1.json before diagram production.

- Two representative rows: left adaptation and right adaptation; these exhaust the two conditions.
- Four screens per row: fixation1s → adaptation30s → static test until response/30s maximum → recovery60s.
- Gray screens; central smallcross remains during all phases. Four soft vertical Gabor patches at left/right/top/bottom cardinal positions in adaptation and static test. Envelopes stay fixed; only carrier phase drifts±4cycles/s during adaptation. Static test holds the actual last phase.
- SPACE reports cessation; N reports no apparent motion from the start; omission is censored/ambiguous. No accuracy, reward or visible feedback. Key legend outside screens only.
- Two blocks of four trials, four per direction.1s fixation,30s ceiling and60s recovery are declared adaptations; no physical calibration or human effect validation claimed.
- Final header/title/Construct subtitle/TaskBeacon mark are added only by the fixed watermark script. Blank top18% of raw image.
- At most5actual visual rounds per user instruction. No legacy plotted diagram or algorithmic final figure.
