# Chopin Research 040 — Étude Op.10 No.12: final permitted study (3/3)
Date: 2026-11-22. Verdict: PARTIAL, NOT QUALITY-GATE COMPLETE.

## Research-count lock
Main-branch records 038 (1/3) and 039 (2/3) were directly fetched; this is 3/3. Do not study Op.10 No.12 a fourth time, regardless of unresolved work. Next target: Op.25 No.1 (1/3). Branches and unrecorded runs were not exhaustively enumerated.

## Evidence and source separation
Directly read GitHub studies 038, 039, 07, 08, and chromatic_engine_v4.py. Directly opened the National Edition *Etudes: Performance and Source Commentaries* (https://www.chopin-nationaledition.com/wp-content/uploads/2013/05/etudes_commentaries.pdf), notably source commentary at PDF pp. 14–15 (printed source-commentary pp. 15–16) and the Op.10 No.12 performance note at PDF p. 4. The editorial commentary identifies an autograph fair copy in Stockholm and discusses manuscript A vs French editions FE/FE2 and German GE; it is a **scholarly editorial witness**, not a direct reading of autograph/first-edition score image. No source-score image was inspected here. Source-specific pitch claims from studies 038/039 are NOT independently verified and are not repeated as original-score facts. Do not conflate A, FE, FE2, GE, editorial emendations or pupil copies.

Editorial source explicitly warns that a tie in bar 54–55 was interpreted as a motif slur in some German editions (per study 038); any transcription pipeline must retain distinct tie and slur fields, preserve provenance, and flag uncertain glyphs. This report does not claim direct visual verification of that notation.

## Transferable original compositional design — NOT Chopin transcription
The earlier v4 generator uses four repeated steps per direction, evaluates a subset of chord-tone attacks, and has no independent polyphonic event clocks, harmonic-boundary sustain checks or source-provenance fields. Its success criterion is not evidence of Chopin-like musical construction.

Build in this order: (1) phrase-level functional trajectory and cadence, with structural melodic arrivals and bass destinations; (2) independent inner-voice contrapuntal goals and sustained-tone obligations; (3) 2-bar figuration plan with density independent of harmonic rhythm; (4) pitch generation from varied contour gestures and registral targets, not a fixed 3-note cell; (5) event-level classification; (6) boundary, voice, source and phrase audit. A 2-bar repetition may be retained only with documented formal purpose; otherwise change at least two of harmony, bass, register, melodic destination, contour or density.

Event fields: voice_id, onset:Fraction, duration:Fraction, spelled_pitch, tie_id, slur_id, source_version, evidence_grade. Harmony intervals are half-open and must check every onset AND sustained pitch at every harmonic boundary. Distinguish a sounding event from notation; tied events may extend across a boundary without new attack. For nonharmonic notes classify PASSING/NEIGHBOR only from adjacent events of the same voice and harmonic context; APPOGGIATURA requires accent and resolution; SUSPENSION requires preparation, actual hold and resolution. Otherwise UNRESOLVED. No universal rule that all dissonances are forbidden.

## Actual execution, limited scope
An independent Python 3 script `/tmp/chopin40.py` was executed this run, using `fractions.Fraction`. Output: `PASS 8 synthetic assertions`. Assertions cover: complete 32nd-note coverage; detection of one missing 32nd; held-tone incompatibility after harmonic change; consonant continuation; stepwise passing tone; neighbor tone; unresolved leap; tie/slur independence. The temporary test was **not committed** and was **not** an integration test of v4. Its simplified nonharmonic classifier is not a production music-theory parser and cannot prove all voice-leading or harmonic correctness. Source-score test cases: zero.

## Critical self-audit and handoff
FAIL: direct autograph/1833 first-edition score-image comparison; original-score note-by-note harmony and contrapuntal audit; source-specific variant collation; user-approved composition comparison; implementation integration; full 2-bar developmental generator and comprehensive tests. Consequently **partial** despite three runs. Preserve unresolved items as cross-cutting generator engineering tasks, not a fourth study of this piece. Next scheduled study must begin **Op.25 No.1 (1/3)**. No fingering, practice methods, audio, MusicXML or PDF production undertaken.
