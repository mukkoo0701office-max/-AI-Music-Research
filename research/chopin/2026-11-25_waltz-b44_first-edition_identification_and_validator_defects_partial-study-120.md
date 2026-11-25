# Chopin Research 120 — Waltz E major B.44 / KK IVa/12 — study 2/3 (PARTIAL)
Date: 2026-11-25 JST. Composition/arrangement algorithms only. No performance or fingering study.

## Counter and scope
The repository research/chopin directory was inspected. Existing B.44 study 119 is present, and no other B.44-named study was found in the directory listing. This run is **provisionally 2/3**, not an exhaustive deleted/renamed Git history audit. Op.10 No.2 is already above the three-study ceiling and must not be resumed. The earlier instruction to prioritize Op.10/25 conflicts with the established run sequence now at B.44; preserve the historical count and do not silently reset it.

## Source identification (verified metadata, NOT verified musical notes)
- IMSLP catalogue https://imslp.org/wiki/Waltz_in_E_major%2C_B.44_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 lists a **first-edition scan** #975554, 2 pages, *Album Towarzystwa muzycznego we Lwowie*, no.3, Lviv 1861, plate 343, pages 6–7. It also identifies an 1880 Breitkopf edition (#138636) and 1894 Mikuli/Schirmer (#975553). These are identifiable historical witnesses, not interchangeable urtexts.
- IMSLP gives composition ca. 1829 and first publication 1861. Musopen https://musopen.org/music/4409-waltz-in-e-major-b-44/ instead claims first printing 1871/72. **Source conflict:** a specifically identified 1861 print is stronger evidence than the undetailed Musopen date, but physical scan/title-page verification remains open. The conflict must not be silently erased.
- Wikipedia https://en.wikipedia.org/wiki/Waltz_in_E_major_(Chopin) asserts A–B–A–C–A–B–A and E/G# minor/A tonal regions. These are **unverified secondary hypotheses** until the score's repeat marks, cadences, and phrase boundaries are read.
- No note-level score image or autograph was directly inspected this run. Therefore **zero B.44 pitches, bar numbers, modulations, NCT labels or motives are claimed as score facts**.

## Repository baseline actually read
- research/chopin/2026-11-21_op10-no2_algorithm-study-07.md: three-clock density architecture; weak chromatic turning and absent NCT audit.
- research/chopin/2026-11-21_op10-no2_algorithm-study-08.md: 3-note cells, pitch-class target assertions, absent two-bar sequence and vertical audits.
- research/chopin/code/two_bar_event_validator_v1.py: event-level two-bar validator, synthetic tests only.
- research/chopin/code/waltz_event_audit_v2.py: harmony-span and tie audit, synthetic tests only.

## Critical code review: concrete defects (static analysis, NOT executed)
1. two_bar_event_validator_v1.signature sorts by onset only, merges simultaneous notes from different voices, and omits duration, diatonic intervals and harmonic roles. Thus a multivoice pattern can appear to retain a contour even when voice assignment changes.
2. transformed() rejects an exact transposition (constant semitone shift) even though transposition is a valid transformation; it also accepts some arbitrary changes if sign contour remains, which does not prove a coherent sequence.
3. waltz_event_audit_v2.audit partitions voices by (witness,voice) but uses a single global harmony timeline. Contradictory witness-specific harmonies cannot be represented without accidental cross-witness analysis.
4. Its tie_prev check verifies preceding pitch, but not whether the previous event has an explicit tie-out. It can accept an invented continuation. The two_bar_event_validator_v1.py implementation DOES check reciprocity; reuse that stronger contract.
5. NCT segment boolean checks chord membership only. A note becoming dissonant under a harmony change is not automatically a suspension: preparation, sustained tie, metrical status and stepwise resolution must all be inspected.
6. two_bar_transform compares metadata tuples and does not read note events. Its 'transformation' verdict is not evidence of an actual melodic transformation.

## Proposed implementation contract — ORIGINAL ALGORITHM, not a Chopin transcription
Event=(witness, voice, onset:Fraction, duration:Fraction, diatonic_pitch, chromatic_pitch, attacked, tie_in, tie_out, harmony_id, accent, provenance).
- Separate structural events (cadential goals, harmonic spans, motive anchors) from elaboration events (passing/neighbor/appoggiatura/suspension/anticipation).
- First verify source witness and chronological note identity. If score transcription is missing, label score_fidelity=UNKNOWN; synthetic tests cannot change this.
- Every 3/4 bar spans exactly 3 quarter units per active voice, with explicit rests. Sixteenth=1/4 and thirty-second=1/8 of a quarter. Validate no gaps/overlaps, tie reciprocity, no impossible tie over rests, and simultaneous voices without losing their identity.
- Two-bar signature preserves voice, attack positions, durations, diatonic intervals, semitone intervals, metric accents, harmony roles and bass cadence. Classify EXACT_REPRISE, TONAL_SEQUENCE, CHROMATIC_TRANSPOSITION, RHYTHMIC_VARIANT, HARMONIC_VARIANT, CADENTIAL_VARIANT, or UNCLASSIFIED. A sequence needs coherent transposition of structural anchors plus contextual harmonic direction; matching three-note cells alone is insufficient.
- NCT classifier should emit CHORD, PASSING, NEIGHBOR, SUSPENSION, RETARDATION, APPOGGIATURA, ANTICIPATION, ESCAPE, or UNKNOWN. Require context from prior and next *sounding* event in the same voice, harmonic span at attack and at resolution, metric accent, and explicit tie/attack status. Never coerce UNKNOWN to a consonance.
- For repeated A sections, preserve a motive identifier but permit register, voicing, texture and cadence mutations; do not assume the published A-B-A-C-A-B-A plan before score inspection.
- Vertical sonority, crossing, parallels and unresolved accented dissonances are review flags, not unconditional prohibitions.

## Adversarial test plan — NOT EXECUTED
T1 identical diatonic contour with changed chromatic interval under tonal transposition -> TONAL_SEQUENCE; T2 literal chromatic transposition -> CHROMATIC_TRANSPOSITION; T3 voice swapped at simultaneous onset -> not same voice-specific motif; T4 same three-note cell repeated with no harmonic development -> reject developed-sequence label; T5 tie-in without tie-out -> error; T6 suspension without preparation or step resolution -> UNKNOWN/invalid suspension; T7 1/8-quarter overrun -> error; T8 conflicting harmony witnesses -> isolate by witness; T9 unresolved accented dissonance -> flag; T10 incomplete witness transcription -> UNKNOWN score fidelity.

## Quality gate and handoff
**PARTIAL / NOT COMPLETE.** Source bibliographic metadata identified, prior code read and concrete defects statically identified. No first-edition page image was inspected, no pitch-by-pitch source verification, no Python tests executed, and no generator integration. The next **and last** permitted B.44 study (3/3) must inspect #975554 score images if accessible, explicitly cite page/system/bar for every asserted note, and run adversarial tests; if blocked, record unresolved work and move to the next composition. Never do B.44 study 4.
