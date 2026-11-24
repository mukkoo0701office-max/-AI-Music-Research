# Chopin Research 092 — Waltz Op.64 No.1 (1/3): witness-aware phrase and ornament grammar

Date: 2026-11-24 JST. **Cumulative count: 1/3** (repository research/chopin filenames checked: no prior Op.64 No.1 study). Op.42 has 089–091 = 3/3 and is closed. **Status: PARTIAL; source inventory verified, score notes NOT verified.**

## Source evidence and limits
- Chopin's First Editions Online, Op.64 first French edition listing: https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/d7bd61db545fe29d2203e3c9ff329823/ . No.1 music-text page 2 = bars 1–30, page 3 = 31–68, page 4 = 69–97, page 5 = 98–124. This is **catalogue pagination**, not verified musical form.
- Online Chopin Variorum Edition, https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/cc73ab49cc447fb5e57d010fadb5cd32/ : lists autograph sketch, two presentation autographs and a first French impression, with differing manuscript bar distributions. Do NOT equate the autograph page bar coverage with a full edition or assume all witnesses agree.
- IMSLP catalogue https://imslp.org/wiki/Waltzes%2C_Op.64_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 : Op.64 No.1 D-flat major, Molto vivace, first published 1847; lists Bonn and BnF autograph scans and French first edition. The actual score images and pitches were **not directly inspected in this run**.
- No original bar-level pitch, ornament, harmonic function, cadence or motivic contour is asserted. A score-viewer listing alone cannot justify those claims.

## Prior work actually read
- research/chopin/2026-11-21_op10-no2_algorithm-study-07.md and -08.md; research/chopin/code/chromatic_engine_v2.py. Current make_line repeats 3-note anchors four times and checks only terminal target PC. analyze tests durations/leaps but not intermediate dissonances, cross-chord continuations, phrase development or ornament provenance. **Not patched in this run**.
- research/chopin/2026-11-24_waltz-op42_final_source_gate_crossmeter_validation_partial-study-91.md: generic phase and harmony-boundary checks are not Op.64 score evidence.
- feedback/Feedback_001_Shizukana_Kitai_Piano_Jazz_Preferences.md: user preferred functional harmonic clarity, restrained chromaticism and contrasting long line versus ornament; this is a *design preference*, not a claim about Chopin.

## Proposed ORIGINAL composition grammar (NOT a transcription)
Representation:
`WitnessEvent(source_id, impression, page, bar, beat:Fraction, duration:Fraction, spelled_pitch, voice, tie, ornament, certainty, image_anchor)`.
`Phrase(motif_id, length_bars, harmonic_goal, cadence_class, register_arc, density_arc, ornament_budget, accompaniment_pattern, reprise_flag)`.
All time positions are exact rational quarter-note units. In 3/4, bar duration = 3 quarter units. Each voice has its own event stream and rests. A grace-note ornament is separately anchored and does not consume measured time unless a source-specific timing policy explicitly assigns it duration.

Generation stages:
1. Define phrase goal and cadential target, then harmonic regions as half-open [start,end) intervals; never assume exactly one chord per bar.
2. Create a slow contour/anchor-note skeleton with meaningful 2–4-bar goal structure, rather than a repeated 3-note cell. Phrase starts may use chord third/seventh or justified appoggiatura; this is user preference and original compositional choice.
3. Transform a two-bar object by contour-preserving rhythmic displacement, register expansion, changed harmonic function or controlled ornament density. Require identifiable invariant + explicit transformation. Literal repeats must carry `reprise_flag`.
4. Expand ornaments locally: neighbor turn (anchor-upper-anchor-lower-anchor), passing chain, anticipation, appoggiatura or chromatic enclosure. Each must declare structural anchor, accentedness, metric onset, resolution target and source/ORIGINAL status. Ornament removal must recover the skeleton. Never infer a specific ornament in Op.64 No.1 from this grammar.
5. Accompaniment: independent bass and upper accompaniment layers on the three-beat clock, with optional offbeat displacement. Do not assert a particular left-hand pattern without image evidence.
6. Reconcile verticality: split held events at every harmonic boundary; test consonance/dissonance against spelled chord and local voice leading. A passing note requires stepwise approach and departure; a neighbor returns to its anchor; a suspension needs preparation/hold/stepwise resolution; an appoggiatura may be unprepared but requires appropriate accent and resolution. Unclassified cases => UNKNOWN and fail closed. Treat ninths and other extensions as explicit harmonic allowances, not automatic errors.
7. At cadence check bass function, structural soprano arrival, dissonance resolution, and phrase timing; audit register overlap and excessive texture density separately from hard contrapuntal errors.

## Test specification / falsifiability (NOT EXECUTED)
- T1: 3/4 bars with 12 sixteenths sum to 3 quarter units; 24 thirty-seconds also sum to 3; mixed subdivisions use Fractions.
- T2: event [2,4) crossing barline at 3 and chord boundary at 3.5 splits into [2,3),[3,3.5),[3.5,4).
- T3: unprepared accented dissonance labeled suspension must be rejected; correctly labeled appoggiatura may be accepted only after resolving.
- T4: passing-tone classification fails if next interval is a leap or if the note is not between surrounding structural tones.
- T5: unchanged 2-bar object without reprise flag fails the development requirement.
- T6: ornament removal reconstructs all original structural anchors, including tie status.
- T7: two editions with conflicting spelled pitches must retain two provenance-tagged events; no silent merging.
- T8: arbitrary cadence in an unverified original bar must be rejected as an evidence claim.

**No Python tests were run; no integration with existing generator; no score-derived fixture.** These are implementable specifications, not validated code.

## Critical self-audit / next eligible run
This research establishes a usable evidence inventory and proposed compositional architecture but does **not** meet the full quality gate for source-verified technique extraction. Source images and bar-level harmony/form/ornament still require direct verification. Do not convert page ranges into section boundaries. Next run Op.64 No.1 2/3 should prioritize first-edition/autograph image access and a small, anchored bar-level sample; if blocked, document it, never invent pitches. Maximum 3 runs for this work; then move on regardless of completeness. No performance/fingering research, no MP3/MusicXML/PDF deliverable.
