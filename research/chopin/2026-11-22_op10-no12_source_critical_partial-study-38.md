# Chopin Research 038 — Op.10 No.12 (1/3, partial)
Date: 2026-11-22. Scope: composition algorithms, not fingering or performance exercises.

## Research count and prior work
Read GitHub studies 07 and 08 (Op.10 No.2) and 037 (Op.10 No.11). No.11 is completed at 3/3. The main-branch research/chopin directory listing contained no No.12 study; this is counted as No.12 1/3, subject to the limitation that other branches or unrecorded runs were not checked. Study 07 separated fast line, harmonic support and bass clocks; 08 introduced harmonic target checks but repeated a 3-note cell four times. Study 037 separated notated duration, harmony, and independent voices. User-approved music artifacts have not been directly compared.

## Sources and evidence grades
1. Fryderyk Chopin Institute, facsimile catalogue, autograph Stichvorlage for Op.10 Nos.11–12, Stockholm MMS 399: https://chopin.nifc.pl/en/chopin/bibliografia/21086 . Primary manuscript LOCATION verified; images NOT directly read note-by-note.
2. Chopin National Edition, Source Commentary, pp.15–16, Op.10 No.12: https://www.chopin-nationaledition.com/wp-content/uploads/2013/05/etudes_commentaries.pdf . Scholarly source comparison directly read. It is NOT direct inspection of autograph or first-edition score images.
3. Fryderyk Chopin Institute work catalogue: https://chopin.nifc.pl/en/chopin/kompozycja/171 . C minor and major-mode final chord documented in secondary analysis.

## Source-critical findings from the National Edition commentary
The editors take FE2 as principal text compared with autograph A, and consider Chopin's annotations in FED. A and FE have markedly different expression marks in bars 1–10, 41–50 and 73–81; do not merge source variants automatically.
- Bar 1: time signature in the edition is taken from A; A metronome quarter=76, changed probably in FE. The precise printed time-signature glyph has not been independently verified from manuscript image.
- Bars 2–5: A has energico and crescendo markings, with con forza in bar 5 where FE has con fuoco.
- Bars 14–15: A has d2–g2–d3 at bar 15 start; the sustained a2 appears in a version probably changed during FE proofreading. Distinguish tie from motif slur; GE omits a tie.
- Bars 27–28: RH source variants exist; editors regard FE bar 27 fourth-beat g2 as erroneous and emend to f2. This is an editorial assessment, not independent image verification.
- Bars 54–55: a2 tie was misread as a2–d3 motif slur in some German editions.
- Bar 56: later GE editions have d2 rather than c2 as first semiquaver, classified as an error by the editors.
- Bar 75: LH accidentals added in FE proof, later GE altered another accidental arbitrarily.
- Bar 80: FE has a probably erroneous minim duration for sustained RH c1.
- Bar 37: source commentary text extraction ambiguously renders an italic dynamic symbol. Do not turn it into a pitch-class alteration without inspecting the original glyph.

## Reusable generative design (NOT original Chopin pitches)
1. Plan a two-bar or longer phrase with structural melody, harmonic functions, bass destinations, inner-voice semitone resolutions, cadence role, and tension curve BEFORE expanding dense notes.
2. Separate structural melody, LH rapid figuration, independent inner voice, and harmonic timeline. Density of 16th notes must not imply equally rapid harmonic changes. Each LH figuration segment has departure bass, harmonic fill, and destination; avoid 3-note-cell repetition as a default.
3. Two-bar development retains either melodic contour or rhythmic identity while changing at least two of harmonic destination, bass trajectory, melodic arrival, texture, and tension curve. A justified cadential repetition is an exception.
4. Label each note CHORD, TENSION, PASSING, NEIGHBOR, APPOGGIATURA, SUSPENSION, ANTICIPATION or UNRESOLVED. Passing/neighbor labels need same-voice context; appoggiatura requires accent and plausible resolution; suspension requires preparation, real hold over a harmony change, and resolution. A tie is NOT a slur. Re-evaluate sustained pitches at every harmonic boundary.
5. SourceEvent fields: bar, voice, onset, pitch, duration, tie, slur, articulation, source_id, evidence_status. Keep A, FE, FE2, GE, pupil annotations, and editorial intervention distinct. Do not silently combine them.

## Original example, NOT a Chopin transcription
4/4 two-bar harmonic skeleton: Cm(add9) for 2 beats, Abmaj7 for 2 beats | Fm9 for 2 beats, G7(b9) for 2 beats. Structural melody Eb–G–Ab–B (leading to C in a following phrase); bass C–Ab–F–G. Rapid LH sixteenths should be generated only after harmonic and voice-leading checks. No untested note stream is supplied.

## Verification plan and quality gate
Required automated checks: independent voice duration totals, rational 16th/32nd timing, harmonic-boundary sustain reassessment, unresolved non-chord-tone alerts, tie/slur independence, two-bar variation, provenance separation, and non-duplication against prior work.
**Tests executed in this run: zero.** No integration into chromatic_engine_v4.py was performed. Original score images were not inspected; no original-score complete voice audit or direct comparison with user-approved artifacts was achieved. This is a PARTIAL study, not a completed implementation. Next run: No.12 (2/3), prioritize direct score-image inspection and executable checks. After No.12 (3/3), move to Op.25 No.1 regardless of completeness.
