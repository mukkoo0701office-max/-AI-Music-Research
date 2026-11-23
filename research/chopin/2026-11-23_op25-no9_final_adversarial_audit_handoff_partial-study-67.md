# Chopin Research 067 — Op.25 No.9 final study 3/3: adversarial audit and handoff

Date: 2026-11-23. **PARTIAL / NOT SOURCE-VALIDATED**. Cumulative research count for Op.25 No.9: **3/3** (065 = 1/3, 066 = 2/3, this 067 = 3/3). **ABSOLUTE STOP:** no fourth No.9 research run. Next target: Op.25 No.10, 1/3, after checking repository history.

## Directly inspected evidence and provenance
- Authenticated GitHub full text of studies 065 and 066, both of which report direct inspection of studies 07/08 and `research/chopin/code/chromatic_engine_v4.py` in study 066. **This run did not independently fetch 07/08 or v4**, so do not misstate that as direct verification.
- IMSLP Op.25 score catalogue inspected on 2026-11-23: https://imslp.org/wiki/%C3%89tudes,_Op.25_(Chopin,_Fr%C3%A9d%C3%A9ric) . Its list identifies No.9 as G-flat major, No.10 as B minor, and contains score listings. Catalogue metadata is not a legible primary score. No score page or original note image was inspected in this run.
- OCVE primary witness lead: https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/ (carried forward, **not opened or read this run**).
- User-approved examples: not available/inspected this run. No original-score bar, pitch, cadence, harmonic or articulation fact is asserted below.

## Defects inherited from studies 065/066
Previous study 066 records 8 synthetic invariants passed, but classifier remains overly permissive; 3-note cell repetition in earlier engine, no real phrase generation, incomplete nonchord-tone contextual checks, independent bass and harmonic-boundary tests missing in production. No verified Chopin-note mapping. These are not closed by this run.

## ORIGINAL implementation specification, not an Op.25 No.9 transcription
1. Generate a phrase graph: section role, harmonic plan, cadential target, structural melody targets, bass arrival graph, and attack-density trajectory. Surface notes must realize rather than independently choose these goals.
2. Model an event as `(voice_id, onset:Fraction, duration:Fraction, release:Fraction, spelled_pitches, accent, articulation, tie_id, motif_id)`. Separate sounding release from notated duration. A simultaneous octave is a single onset event with two pitches; a rest is a duration-bearing empty-pitch event.
3. For two-bar units, retain a declared invariant and vary at least two independent structural parameters (accent topology, contour apex, bass destination, harmony, register or rhythmic grouping). A literal reprise is allowed only with explicit `REPRISE` role; merely transposed three-note looping is not accepted as development.
4. Nonchord-tone classifier must receive *previous and next same-voice notes*, chord spelling, meter/accent, tie and preparation history, and current/next harmony. Passing: two stepwise movements in same direction; neighbor: step away and return; suspension: prepared consonance tied across a new harmony and resolved by step; appoggiatura: accented dissonance resolving by step with no required preparation. These are **candidate classifications**, not absolute rules; missing context => UNKNOWN; unresolved accented dissonance => REVIEW.
5. Audit every onset **and** every harmony boundary with half-open active-note intervals `[onset, release)`; preserve pitch spelling for harmonic function. Validate each independent voice's meter sum, including explicit rests, ties and tuplets. Distinguish chordal octave doubling from independent contrapuntal strands.
6. Fail closed: unknown chord spelling, unverified harmony, ambiguous polyphonic voice assignment, or unexamined tie context must not yield PASS. A chromatic dissonance may be intentionally expressive; a REVIEW flag invites musical judgement rather than automatic deletion.

## Executed independent Python smoke tests (not the repository generator)
Executed 2026-11-23 with Python fractions.Fraction. Seven assertions passed: exact-boundary note inactive, cross-boundary note active, unaccented chromatic stepwise 60–61–62 => PASSING candidate, 60–61–60 => NEIGHBOR candidate, missing following note => UNKNOWN, accented 60–61–62 => REVIEW, thirty-two 1/32 durations sum to one whole. These examples are **synthetic MIDI-number tests, not Chopin pitches**. This deliberately minimal classifier cannot distinguish chord tones, enharmonic spelling, harmonic context or legitimate accented passing tones; a passed test is not musical validation.

## Critical negative test matrix for next implementation stage (specified, not executed)
- Tie across harmony with no consonant preparation => never SUSPENSION.
- Prepared tied dissonance with no stepwise resolution => REVIEW.
- Tuplet fractions whose total exceeds meter => REJECT.
- A rest incorrectly converted to sounding note => REJECT.
- Identical two-bar cells merely transposed despite `DEVELOPMENT` role => REJECT.
- Octave attack serialized as sequential notes => REJECT.
- Parallel octaves in true independent voices => flag; parallel octave doubling within one chordal layer => do not misclassify as contrapuntal violation.
- Harmony change during sustained note => inspect active pitch against both harmonic contexts.
- Bass goals copied directly from upper-note attacks => flag lack of structural independence.

## Quality verdict and handoff
**PARTIAL / INCOMPLETE.** Primary-source note-image access failed; no source-measure verification, no original-score harmonic audit, no independent direct reading of 07/08/v4 this run, no production Python integration, no approved-example regression. The only executed code was the seven-assertion independent smoke test. The research cap takes precedence over completeness. **Op.25 No.9 is closed at 3/3; proceed to Op.25 No.10, 1/3.** Carry the above unresolved implementation defects forward as generic engine work, **not** as a fourth No.9 study. No performance/fingering work or user-facing audio/MusicXML/PDF.
