Use case: infographic-diagram
Asset type: TaskBeacon task flow diagram
Primary request: Create a clean, publication-ready task flow diagram as a timeline collection for the behavioral task described below.

Task: Motion Aftereffect Task
Construct: motion adaptation
Rows/conditions:
- Left adaptation: all four sinusoidal carriers drift left; patch envelopes remain stationary.
- Right adaptation: all four sinusoidal carriers drift right; patch envelopes remain stationary.

Timeline phases:
- Left adaptation: Fixation (1 s; no response; one small dark + centered on gray) -> Adaptation (30 s; no response; four soft Gaussian-windowed VERTICAL grating patches arranged left/right/above/below a small central +; all carriers drift left at4cycles/s) -> Static test (until response,30s max; the SAME four patches and central +; genuinely stationary, held at final actual phase) -> Recovery (60 s; no response; gray screen with central +).
- Right adaptation: Fixation (1 s; no response; one small dark + centered on gray) -> Adaptation (30 s; no response; identical four vertical Gaussian grating patches, all carriers drift right at4cycles/s) -> Static test (until response,30s max; same four patches and central +, genuinely stationary) -> Recovery (60 s; gray screen with central +).

Visual requirements:
- White background, landscape orientation, crisp dark text, restrained condition accent colors.
- Exactly two horizontal rows, four participant-screen snapshots per row, connected by subtle right-pointing timeline arrows.
- Each screen snapshot shows visible stimulus content rather than variable names. Gray panel backgrounds should be medium gray #808080, matching the real experiment.
- Four patches MUST be a PLUS arrangement at cardinal positions around the central cross, not four quadrants. Each patch contains about three clearly visible VERTICAL light/dark bars with soft Gaussian fading, NOT circular rings, horizontal bars, checkerboards or hard circular outlines.
- Keep the grating envelopes fixed in position. Show direction only as a small EXTERNAL annotation under the adaptation screen, "4 cycles/s left" or "4 cycles/s right". Do not draw motion arrows inside any participant-screen panel.
- Static test panels look like the adaptation panels but have no motion symbols: the perceived aftereffect is NOT an actual moving screen.
- Use thin black arrows, consistent row spacing, subtle row separators.
- Labels above each panel: "Fixation", "Adaptation", "Static test", "Recovery".
- Timing below each panel: "1 s", "30 s", "Until response / 30 s max", "60 s".
- Condition labels at the left: "Left adaptation" and "Right adaptation".
- Place a single compact footer BELOW both timelines, outside screen boxes: "SPACE: motion ceased", "N: no motion from start", "No response: censored". A separate small footer line may say "2 blocks × 4 trials · 4 per direction".
- Use short labels only; no paragraphs. Legible at normal document preview size.
- Leave the top18% completely blank white for a fixed title/subtitle/logo added later.

Accuracy constraints:
- Do not invent phases, stimuli, keys, rewards or timings. No correctness feedback, countdowns, moving fixation or whole-patch displacement.
- Do not add people, lab equipment, decorative scenes, logos or unrelated icons.
- Do not draw the task title, construct subtitle, any logo, watermark, brand mark or TaskBeacon text.
- Draw only timeline content below the blank header band.
- Preserve exact terms: Left adaptation; Right adaptation; Fixation; Adaptation; Static test; Recovery;1 s;30 s;Until response /30 s max;60 s;SPACE;N.
- No claims of calibrated visual degrees, luminance, or validated human aftereffect.

Style:
TaskBeacon scientific infographic style: clean vector-like raster image, organized spacing, gray screen boxes, restrained teal/blue row accents, blank header-safe area.


Revision request (round 2): Keep two rows and four phases, but fix participant-screen geometry. Input image1 is the ACTUAL native 1280x800 display screenshot and is the authoritative stimulus reference. Image2 is previous figure for labels/layout reference ONLY; its stimuli were geometrically distorted and must be replaced. All eight participant panels must be perfect SQUARES representing a central 512x512 pixel crop of image1 (crop x384..896, y144..656). Add one clear footer annotation "Central 512 × 512 px crop (equal x/y scale)". Never stretch a screen horizontally or vertically. In each square, the central cross is at50%,50%, and the four Gabor centers are EXACTLY (25%,50%), (75%,50%), (50%,25%), (50%,75%). Equal horizontal and vertical center distances are essential. Gaussian sigma is5%of panelwidth: soft patches, approximately3visible bars, much less bright/dark than the rejected figure. Copy the actual reference's contrast and vertical sinusoidal pattern faithfully. Fixation/recovery have only the tiny cross, no patches. If space is limited, increase overall canvas height or reduce square panel sizes uniformly, NEVER squeeze geometry. Preserve all labels, durations, keys and trial counts from the original prompt. Blank top18%white header, NO generated title/subtitle/logo. Purewhite background. All text outside gray squares. Suggested output1536x1280 with square panels~220px.
