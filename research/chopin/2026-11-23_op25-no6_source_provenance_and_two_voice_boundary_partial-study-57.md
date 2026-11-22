# Chopin Research 057 — Op.25 No.6 study 2/3: source provenance and two-voice boundary tests (PARTIAL)
Date 2026-11-23. Cumulative Op.25 No.6 count **2/3**, following Research 056 (1/3). Next and final run 3/3; after that move to Op.25 No.7 irrespective of quality. Op.25 No.5 is closed at 3/3. Do not reopen Op.10 No.2 (>3 runs).

## Verified source catalogue, not verified score notes
- Chopin Online annotated catalogue, German first edition corrected reprint G2: https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/8d3ec7a8022530d1a0025b0df6a255e6/ . Op.25 No.6 printed pp.26–30; catalogue bar ranges 1–13,14–26,27–36,37–47,48–63. This is a **corrected reprint**, not proof of the first impression's exact reading.
- Chopin Online source overview https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/25df858864ce6c5d227d5aec3b274ded/ identifies a manuscript/copy (Stichvorlage) pp.17–20 with No.6 bars 1–19,20–35,36–51,52–63, and English first edition E1 pp.20–25 bars 1–10,11–22,23–32,33–42,43–53,54–63. These are **pagination differences**, not evidence of divergent notes.
- Research 056 records secondary PTNA commentary: G-sharp minor, alla breve, fast paired thirds and distinct accompaniment. Original manuscript/first-edition **notation images were not directly read** in this run. No exact bar-level pitches, harmonic analyses or editorial variants are claimed.

## Previously documented work inspected
Read actual repository Research 056, 07, 08. Research 07's three-clock prototype is not a verified musical analysis. Research 08 reports the 3-note-cell repeated four times and target-tone-only chord audit; these are inherited known limitations, not proof that its current code still has the same behavior. Production Python file was not fetched or run; no claim of integration. No user-approved composition exemplar inspected.

## Generative rules (independent original proposal, NOT claims about Chopin's exact notes)
1. Plan 4–8 bar harmonic/phrase destinations first. For each two-bar span assign two distinct foreground melodic trajectories U and L, plus slower bass B. Each U/L event has Fraction onset/end, spelled pitch, independent voice identity, accent phase, harmony-window ID, preparation and continuation context. Never infer that simultaneous thirds alone imply independent linear coherence.
2. Build two-bar trajectory A with start, high/low point and cadential target. Build B by preserving one recognizable anchor while varying **at least two** of contour, density, accent phase, register, harmonic destination, or bass rhythm. A transposition-only copy is permitted as a deliberate sequence *candidate*, not counted as developed composition without harmonic/formal justification.
3. A dyad may contain chord-tone + passing tone, two chord tones, or two different non-chord-tone functions. Evaluate each voice independently with a three-state result PASS/FAIL/UNKNOWN; missing continuation or missing reliable harmony -> UNKNOWN. A chromatic interval differing from a diatonic third is not automatically an error; require notation/source confirmation for statements about Chopin.
4. Harmony intervals use half-open [start,end). An event sustained across a boundary must be checked against both harmonies without fabricating a new onset. Separate onset-level accent dissonance from sustained dissonance newly exposed by a chord change.
5. Audit bass/inner voice at all onset, release, and harmony-change instants; detect unwanted vertical collisions and structural parallels with contextual exceptions. Consecutive thirds are not categorically prohibited.
6. For dense 16th/32nd streams use exact rational timing, check per-voice duration and continuity, and prevent melodic anchor erasure by ornamental fill.

## Actually executed synthetic Python tests
Executed in local Python with fractions.Fraction (NOT repository production code): (a) 1/16+1/32+1/32=1/8 PASS; (b) held [0,1/2) overlaps both [0,1/4),[1/4,1/2) PASS; (c) altered 3-note sequences remain distinguishable PASS; (d) distinct 2-bar arrays distinguish an exact duplicate PASS. **Four synthetic assertions passed.** They do not test NCT classification, parallel intervals, original score, nor actual generative quality. The checks are intentionally minimal, and therefore the quality gate remains FAIL/PARTIAL.

## Adversarial cases to implement (NOT tested)
- Chord boundary exactly at note release must not overlap the prior note.
- Accented chromatic lower voice resolves while upper voice remains an unresolved appoggiatura: independent labels, no shared verdict.
- Bass attack under sustained paired upper voices triggers a vertical scan.
- Voice crossing with explicit exchange ID must not be silently normalized.
- Repeated 3-note cells with transposed pitch but unchanged accent, contour, and harmonic role should be rejected as development.
- Same pitch-class different spelling must preserve enharmonic function rather than collapse to MIDI integer alone.

## Critical self-audit / handoff
Direct first-edition notehead comparison: **NOT DONE**. Comparison against manuscript/English first edition: **NOT DONE**. Existing generator code fetched or integrated: **NOT DONE**. NCT classifier and 2-bar sequence algorithm production tested: **NOT DONE**. Research therefore is a provenance-aware algorithm specification plus minimal synthetic timing tests, not a completed score-grounded analysis. Final 3/3 must prioritize a legible source image and real repository code tests; then close Op.25 No.6 with unresolved issues recorded even if still partial. No fingering/performance work, audio, MusicXML, or PDF deliverables.
