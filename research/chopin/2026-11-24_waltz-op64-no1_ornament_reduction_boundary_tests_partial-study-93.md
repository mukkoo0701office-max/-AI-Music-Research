# Chopin Research 093 — Waltz Op.64 No.1 (2/3): ornament reduction and boundary audit

Date: 2026-11-24 JST. **Cumulative Op.64 No.1: 2/3**. Prior record: [092](2026-11-24_waltz-op64-no1_source_inventory_phrase_ornament_grammar_partial-study-92.md) = 1/3. Next eligible study is **3/3 maximum**, after which move to the next work regardless of completion. **STATUS: PARTIAL / NOT SCORE-VERIFIED.**

## Source status and explicit evidence boundary
- IMSLP catalogue https://imslp.org/wiki/Waltzes%2C_Op.64_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 confirms Op.64 consists of three waltzes; No.1 is D-flat major, Molto vivace; the catalogue describes composition in 1846–47. This is metadata, **not a reading of original notes**.
- Chopin's First Editions Online https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/d7bd61db545fe29d2203e3c9ff329823/ was opened, but its dynamic filter returned a general source list rather than readable note-level images. The first French edition and autograph witnesses identified in study 092 remain **not directly inspected note by note**. No specific original pitch, harmony, turn, barline, phrase boundary or ornamental realization is asserted.
- Existing repository files actually read: study 092; study 091; Op.10 No.2 studies 07/08; `research/chopin/code/chromatic_engine_v2.py`; `feedback/Feedback_001_Shizukana_Kitai_Piano_Jazz_Preferences.md`. User preference for functional clarity and contrast between long lines and ornament is a separate design criterion, not evidence about Chopin.

## Code defect audit, verified by direct reading
`chromatic_engine_v2.py` generates 12 notes from four near-identical three-note cells, then four terminal approach notes. `analyze` checks duration, leap and last target pitch class but never validates intermediate notes against harmony or checks non-chord-tone approach/resolution. It contains no multi-bar motif object, harmony-boundary segmentation or ornament-to-skeleton mapping. Its four quarter-note accompaniment layer and one whole-note bass are specifically 4/4, and must **not** be copied into a 3/4 waltz engine. No repository generator was modified in this study.

## Original algorithmic design (NOT transcription or a claim of specific Chopin measures)
**Two clocks and two graphs:** use `Fraction` quarter units for sounding time and a separate structural-note graph for phrase development. A 3/4 bar is 3 quarter units; 12 sixteenths or 24 thirty-seconds fit exactly. A phrase consists of 2–4-bar goal arcs (structural pitches, harmonic goal, cadence, register and density) and a separate layer of timed decorations. The structural graph must survive removal of decorations.

**Two-bar sequence:** represent `Motif(contour, structural_intervals, onset_pattern, harmonic_goal, register_arc, density_arc)`. A subsequent two-bar object is linked to its parent by an explicit operation (diatonic transposition, sequence, rhythmic displacement, augmentation, register transfer, harmonic reinterpretation). Retain at least one invariant and change at least one nontrivial dimension. A literal repeat requires `reprise=True`; superficial substitution of a three-note cell is insufficient. Phrase goals should constrain the transformation, not merely a fixed semitone offset.

**Ornament grammar:** each event has `(witness_id|ORIGINAL, bar, onset, duration, spelled_pitch, voice, structural_anchor_id, role, accent, resolution_id, certainty)`. Roles include structural, passing, neighbor, anticipation, suspension, appoggiatura and unclassified. A passing tone is stepwise in and out, moving in one direction between structural tones; neighbor returns to its anchor; a suspension must have preparation/continuation and resolution, whereas an appoggiatura may be unprepared but requires a justified accent and resolution. Diatonic step must be assessed from **spelled pitches and harmonic context**, not semitone distance alone. Grace-note timing must be witness- or policy-specific, not guessed from the notation. An unknown role fails closed, not accepted as consonant.

**Verticality and harmony boundaries:** represent harmony as half-open intervals. Every sustained event crossing a boundary is split into audit segments while retaining the same tied identity. Check consonance or explicitly permitted extension against the active spelled harmony at each segment; classify unresolved dissonance with preparation, metric accent, and next structural event. Parallel perfect intervals, voice overlap and bass/harmony function are additional audits, but simplistic bans must not override valid contrapuntal context. Do not infer a cadence from edition page numbers.

**Failure modes:** rapid ornament can obscure skeleton, and removing all non-chord tones can destroy the phrase. Thus preserve provenance and distinguish dissonance requiring resolution from deliberately stable harmonic extensions; optimize phrase continuity before ornament density. Repetition diversity is a soft musical criterion, while time consistency, source attribution and resolution requirements are hard gates.

## Executed independent synthetic checks (not a Chopin fixture)
Executed Python `fractions.Fraction` assertions on 2026-11-24:
1. 12 sixteenths total three quarter units — PASS.
2. 24 thirty-seconds total three quarter units — PASS.
3. Note [2,4) split at 3 and 3.5 into three consecutive segments — PASS.
4. Two-bar abstract motif (0,2,1,3) transposes to (2,4,3,5) — PASS.
5. Structural anchors (time,pitch) recovered after removing tagged ornaments — PASS.
6. Simplified chromatic passing predicate accepts 60–61–62 — PASS.
7. Same predicate rejects neighbor 60–61–60 and leaps 60–64–67 — PASS.

These **7 synthetic invariants passed**, but the passing-tone predicate is deliberately only a coarse numeric prefilter, not a complete diatonic/metric/non-chord-tone classifier. There was no full generator integration, no automated comparison to an original witness and no subjective musical-quality validation.

## Critical quality assessment and mandatory handoff
**Not complete.** Neither the primary score's individual notes nor edition differences have been verified. No Op.64 No.1 bar-specific structural, harmonic or ornamental claim is defensible from this run. This design improves specification and tests of reusable mechanisms but does **not** prove that they are characteristic of this particular work. Study 3/3 must prioritize a readable first-edition or autograph page with stable image citation and a small verified bar-level sample, and if blocked record that explicitly. Do not run Op.64 No.1 a fourth time. Then advance to the next eligible work. No fingering/practice, MP3, PDF or MusicXML deliverable.
