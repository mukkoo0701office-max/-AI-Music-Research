# Chopin Research 061 — Op.25 No.7 (FINAL 3/3): negative-case voice/NCT audit and handoff

Date: 2026-11-23. **PARTIAL / SOURCE-NOT-VERIFIED. Cumulative count: 3/3; STOP further Op.25 No.7 research. Next Op.25 No.8 (1/3).**

## Provenance and repetition audit
Read repository studies 059 (1/3) and 060 (2/3) in full. Their primary-source inventory identifies the Online Chopin Variorum Edition German first-edition witness, Zaleska-Rosengardt exemplar: https://chopinonline.ac.uk/ocve/browse/pageview/78070/ . Reopened the OCVE page on 2026-11-23: catalogue confirms p.3 bars 1–21, p.4 bars 22–39, p.5 bars 40–69. The accessible page exposes no legible musical notation, so **no pitches, harmonies, source variants or bar-specific voice labels were directly verified**. Do not conflate metadata access with score inspection. Earlier 059 says research 07/08/058 were read; this run re-read 059/060, not 07/08 or approved exemplar files. No assertion of full repository integration.

## Transferable algorithm: proposed, NOT asserted as a Chopin transcription
Represent each sounding event as (voice_id, role, onset Fraction, duration Fraction, spelled_pitch, harmony_id, accent, tie, phrase_goal). Determine structural roles before ornament generation; melody identity is independent of highest sounding pitch. Compose principal cantabile and answer with separate goal-directed phrase plans, and bass arrivals on a separate harmonic clock. Keep note durations exact as rational numbers, including sixteenths and thirty-seconds.

### NCT and harmonic boundary audit
- Each chord window is half-open [start,end); at every boundary, re-evaluate sustained notes against the new harmony, including spelling and functional context.
- Chord membership alone cannot classify nonchord tones. Require preceding and following voice events, metric accent, preparation, interval direction, chord spelling and resolution; otherwise UNKNOWN. Labels passing, neighbor, suspension, appoggiatura are *candidates* until sufficient context and score/human audit.
- Passing candidate: step into and out of the tone in the same direction; unaccented by default. Neighbor candidate: step away and return; accent may require appoggiatura review. A suspension requires actual held preparation across a harmonic boundary, accent and stepwise resolution; an unattacked new note is not automatically a suspension.
- Failure: unexplained accented dissonance or no resolution at a declared deadline. Exception: explicit stylistic justification can be reviewed manually, not silently accepted.
- Two-bar development retains one anchor but changes at least two independent attributes among contour, rhythm, harmonic goal, register, role; this is a heuristic, not an empirical Chopin rule. Avoid endless 3-note cell loops.
- Reduction gate removes ornamental notes and tests distinct phrase goals for principal, answer and bass; independent attack schedules alone do not prove good counterpoint.

## Executed independent Python synthetic checks (NOT original-score tests)
Ran Python 3 with fractions.Fraction and dataclasses; output: `PASS 8 synthetic assertions; source verification and repository integration NOT tested`. Eight checks: active-note start inclusion; end exclusion; passing-tone candidate; neighbor-tone candidate; missing predecessor => UNKNOWN; accented unresolved case => REVIEW; three role/onset identities; two-or-more motif feature changes. These are *minimal* unit assertions, not full regression tests. Candidate detector used integer chromatic semitones and triad pitch classes; enharmonic spelling, real suspension preparation, harmonic-window splitting, complex voice crossings and phrase reduction remain untested. No repository source files were modified; repository Python generation code was not executed.

## Critical quality decision and next target
**FAILED source-grounded completion gate**: legible primary score, two-witness comparison, note-by-note harmonic/NCT audit, real contrapuntal reduction, and generator integration are all missing. Research ends at 3/3 nonetheless. Carry forward reusable test design to **Op.25 No.8** without conducting a fourth No.7 study. Before making source-derived claims in No.8, acquire readable notation and record witness, page, bar, pitch spelling, harmonic context and verification status. Do not label synthetic tests as score validation.
