# Chopin Research 046 — Étude Op.25 No.2: final permitted study (3/3)
Date: 2026-11-22. **Status: PARTIAL / score-image quality gate FAILED.** Cumulative count **3/3**: [044](2026-11-22_op25-no2_metric_normalization_partial-study-44.md), [045](2026-11-22_op25-no2_source_clock_regression_partial-study-45.md), this 046. Earlier records report repository searches finding no additional study; undocumented runs cannot be excluded. **No fourth study of Op.25 No.2. Next: Op.25 No.3 (1/3).**

## Directly inspected materials and provenance
- GitHub research 044 and 045; historical studies [07](2026-11-21_op10-no2_algorithm-study-07.md), [08](2026-11-21_op10-no2_algorithm-study-08.md); [chromatic_engine_v4.py](code/chromatic_engine_v4.py); [user-approved feedback](../../feedback/Feedback_001_Shizukana_Kitai_Piano_Jazz_Preferences.md) all read directly this run.
- [Online Chopin Variorum Edition Op.25 source index](https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/) opened directly. HTML displays dynamically loaded source results and **does not expose score-page image content** in this environment. Prior 045 identifies a No.2 source entry, but this run could not independently inspect a page of the manuscript or first edition. [University of Chicago edition catalogue](https://chopin.lib.uchicago.edu/chopin-catalog/descriptions/25.pdf) and [source overview](https://fchopin.net/etude_source/) were referenced via prior studies, not directly read this run.
- **No bar-specific notes, original harmony, articulation or version difference verified from facsimile.** The following examples are **new synthetic compositions**, not Chopin transcriptions. The user-approved preference for natural harmonic direction and smooth guide tones is a design constraint, not source evidence.

## Source-independent compositional hypothesis (not an established account of Chopin's score)
**Architecture**: choose long-range phrase/cadence plan and harmonic destinations; separately plan bass anchors, melodic contour and inner-voice retention; only then fill fast notes. A two-bar gesture carries a traceable contour or rhythm signature while changing at least two of apex timing, register, bass target, harmonic destination and density. This is more than repeating a fixed three-note cell.

**Two rational clocks**: a hypothetical 2/2 bar contains RH 12 eighth-note triplets, each sounding 1/12 whole note, and LH 6 quarter-note triplets, each 1/6 whole note. RH onsets k/12 and LH onsets j/6 coincide at RH index 2j. This is an aligned 2:1 subdivision, **not** inherently a phase-shifting 3:2 polyrhythm. For an alternate 2/4 notational version with all durations halved, transform onsets and durations proportionally and preserve edition metadata; never claim a particular autograph bar has these values without inspection. More elaborate subdivisions must use arbitrary Fraction, not a hardcoded 12-step grid.

**Event contract**: (source_version, voice_id, onset:Fraction, duration:Fraction, pitch, written_value, tuplet_ratio, tie_group, articulation, metric_weight, harmony_window, evidence_status). Keep notation distinct from sounding time. A tie extends a note; a slur does not. Explicit rests and pickups account for bar-total exceptions. Audit overlapping sounding intervals, not just note onsets.

**Harmonic / counterpoint audit**: for every voice and every harmonic window, segment held notes at boundaries without inserting new attacks. Evaluate nonchord notes using same-voice before/after motion, accented status, preparation, dissonance and resolution; label passing, neighbor, suspension, appoggiatura, anticipation, unresolved or ambiguous. A stepwise unaccented chord-extraneous tone is only a *passing-tone candidate* until context is verified. Assess register and bass/inner/upper voice spacing; avoid blanket bans on chromatic tension. Musical decisions need separate critical review.

**Known v4 limitation, confirmed from code**: `contour` extends each chosen direction four times, `generate_pair` checks only eight block-start pitch classes, and `audit` checks length/chromatic adjacency/pair boundaries. It does not instantiate independent triplet clocks, contextual dissonance, cross-harmony sustain or real 2-bar motif transformations. The tests below are an **isolated executable laboratory**, not an integrated patch.

## Executed independent Python 3 regression, 2026-11-22
Used `fractions.Fraction`, with **7 test groups passed**:
1. All six LH onset times equal even-index RH onset times in a synthetic 2/2 bar.
2. 12 × (1/8 × 2/3) = 1 whole-note bar.
3. 6 × (1/4 × 2/3) = 1 whole-note bar.
4. Halving k/12 produces k/24 for synthetic 2/4 scaling.
5. Synthetic sustained C4 from t=1/3 to 2/3: consonant with C major until harmony boundary t=1/2, nonmember in D minor after boundary. Interval splitting checked.
6. Synthetic C4–D4–E4 eighth-triplet positions: D is a nonchord stepwise passing **candidate**, not an independently verified classification.
7. Two synthetic 12-attack gestures preserve onset count while altering pitch apex and bass target. This proves descriptor variation, **not** expressive motivic development.
These are executed assertions, not score verification or engine integration. No MusicXML/audio/PDF output.

## Critical self-audit and closure
**PASS**: 07/08, v4, approved feedback, 044/045 directly compared; exact rational clock and edition-scaling logic; synthetic boundary and 2-bar tests executed; source facts vs proposals separated; count 3/3 explicit.
**FAIL / UNKNOWN**: direct manuscript/first-edition page inspection; verified original pitch, harmony, structural form, score-based nonharmonic classifications, editorial variants; integration into existing v4; full automated regression and perceptual musical-quality evaluation. Consequently **not a completed source-grounded study**.
**Handoff only**: build a score-page provenance table and integrate rational multi-voice event schema and test fixtures into a general generator under future eligible works; **do not schedule another Op.25 No.2 study**. Next work **Op.25 No.3 (1/3)**. Existing hourly schedule unchanged.
