# Chopin Research 039 — Étude Op.10 No.12 (2/3): boundary-aware density and source-critical audit
Date: 2026-11-22. Status: PARTIAL; not a transcription, finished generator, or score-complete audit.

## Count / continuity
Directly fetched Research 038 (No.12 1/3) and 037 (No.11 3/3), plus `research/chopin/code/chromatic_engine_v4.py`. This run is No.12 **2/3** on the verified sequential record; other branches and unrecorded runs are not fully audited. No.11 must not be revisited. Next No.12 study is final (3/3), then Op.25 No.1 irrespective of incompleteness.

## Source and evidence
- Chopin National Edition, *Etudes: Performance and Source Commentaries*, https://www.chopin-nationaledition.com/wp-content/uploads/2013/05/etudes_commentaries.pdf : document directly opened and textual commentary read. Editorial analysis is **not** the same as reading the autograph or 1833 first-edition score.
- Manuscript locator: Fryderyk Chopin Institute catalogue https://chopin.nifc.pl/en/chopin/bibliografia/21086 (from Research 038; not re-inspected here).
- Research 038 reports variants in measures 1–10, 14–15, 27–28, 41–50, 54–56, 73–81, following National Edition source commentary. Those are **prior-study secondary editorial reports**, not independently verified manuscript pitches here. Never merge FE/FE2/A/GE readings into a synthetic original.
- Primary score image **not directly inspected in this run**. Therefore no new original-score pitch/bar-by-bar assertion or complete harmonic analysis is claimed.
- User-approved composition artifacts not directly inspected. Studies 07/08 were referenced through the documented account in 038 rather than independently retrieved this run.

## Algorithmic finding: harmonic time is independent of note density
Existing v4 is a chromatic contour experiment, not a polyphonic compositional engine. Its `contour` repeats a direction four times per direction parameter, yielding a stepwise stream; `generate_pair` evaluates harmonic membership only at a subset of attacks. It has no independent voice clock, no held-note re-evaluation at harmonic boundaries, no source provenance, and no 2-bar multi-parameter development criterion. These observations come from directly reading code, not from a claim of having executed v4.

Proposed event model (original engineering design, NOT Chopin notes):
- `PhrasePlan`: harmonic rhythm, bass goals, structural melodic arrivals, tension trajectory, cadence role, and at least 2-bar development plan.
- `VoiceEvent`: `voice_id, onset:Fraction, duration:Fraction, pitch_spelling, tie_group, slur_group, harmonic_role, source_id, evidence_grade`. A simultaneous note in a different voice must not be counted toward this voice's duration.
- `HarmonyEvent`: start/end, chord members, allowed tensions, functional resolution and explicit bass.
- `FigurationPlan`: density grid (1/16 or 1/32), register envelope, directional arcs, harmonic anchors, planned gaps, local peak, and destination. Never substitute repeating 3-note cells for phrase design.
- `SourceVariant`: edition and provenance; source pitches and editor-supplied readings remain distinct.

### Generation procedure
1. Write 2-bar structural melody and bass destinations; fix harmonic rhythm and a purposeful change of register/energy.
2. Build inner-voice common tones, semitone resolutions, and counter-motions; require independent onset/duration.
3. Fill rapid notes *within* the harmonic and voice-leading constraints using several distinct contour gestures (ascending arc, turnaround, leap-plus-recovery, sequential transposition, rest), preserving harmonic anchors. These are **proposed original gestures**, not verified quotations from Op.10 No.12.
4. Label each event CHORD, FUNCTIONAL_TENSION, PASSING, NEIGHBOR, APPOGGIATURA, SUSPENSION, ANTICIPATION, or UNRESOLVED. Passing/neighbor need same-voice neighbor context; appoggiatura needs accent and directed resolution; suspension needs preparation, actual sustain over a harmony boundary, and resolution. If evidence is absent, mark UNRESOLVED rather than guessing.
5. For any note spanning a harmony boundary, re-evaluate at that boundary even when no new note attacks. Do not confuse slurs and ties.
6. In bar 2 retain a recognisable rhythmic or intervallic identity from bar 1 but change at least two of harmonic destination, bass route, inner-voice path, peak, register, texture. Exception: justified cadential reiteration with explicit reason.
7. Validate source provenance, temporal completeness, harmony, and structural difference before rendering.

### Exceptions / failure cases
- Non-chord tones on a strong beat are not automatically errors: accented appoggiaturas can be intentional, but must resolve plausibly.
- A held pitch can become a dissonance after a chord change without a fresh attack; boundary check is mandatory.
- One chord can span many rapid notes; do not infer one chord per sixteenth.
- A sequence can deliberately repeat for rhetorical accumulation; require an explicit structural role and a nontrivial change across the phrase.
- In polyphony, overlapping different voices is legal; overlapping sequential events within one monophonic voice requires an explicit divisi/voice representation.
- Source-variant uncertainty must remain unresolved; do not automatically optimize it away.

## Executed tests (synthetic data only)
An independent Python 3 script at `/tmp/test_chopin.py` was executed during this run. It used `fractions.Fraction` and asserted **six** conditions: exact per-voice duration coverage; missing 32nd-note rejection; 32 thirty-second notes equal a 4/4 measure; a sustained pitch dissonant after a half-bar harmony change is flagged; consonant continuation is not flagged; a figuration with >3 distinct pitches is accepted. Output: `PASS 6: exact coverage, missing note rejection, 32nd subdivision, boundary alert, consonant boundary, non-3-note figuration`. These are toy structural tests; **not** a full non-harmonic-tone classifier, Chopin score audit, or integration test. The temporary script was not committed.

## Critical self-audit and handoff
No primary score-image note-by-note comparison, no original harmonic/contrapuntal analysis of specific bars, no existing v4 integration, no user-approved-artifact comparison, no source-critical variant collation, and no full-suite test coverage. Thus this remains **partial**. Next and final No.12 run (3/3): prioritize directly viewing autograph/first-edition pages, targeted source-specific passage analysis, and a committed tested module if possible. On reaching 3/3, move to Op.25 No.1 without a fourth No.12 pass.
