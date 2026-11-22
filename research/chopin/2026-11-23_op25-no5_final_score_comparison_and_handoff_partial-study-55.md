# Chopin Research 055 — Op.25 No.5, final study 3/3 (PARTIAL; quality gate NOT passed)
Date: 2026-11-23. Cumulative research count: **3/3** (053, 054, 055). **CLOSED**: do not research Op.25 No.5 a fourth time. Next subject: **Op.25 No.6 (1/3)**.

## Direct score evidence and provenance
Directly viewed the PWM edited score, [PDF](https://imslp.eu/files/imglnks/euimg/e/e5/IMSLP865891-PMLP1970-Chopin_Etude_Op_25_FR.pdf), printed pp.84–85 (PDF page indices 19–20). This is NOT the 1837 first edition or autograph. Research 053 indexed first editions but did not inspect their notation. Research 054 inspected only p.85.
- p.84, beginning of No.5: printed **3/4**, one-sharp key signature, **Vivace quarter=184**, **leggiero**, **scherzando**. Right hand displays alternating short accented/altered attacks and slurred longer notes; left hand uses chordal punctuation and rests. This confirms a mixed short–long/interruptive texture in the edited score, not any exact universal wrong-note rule.
- p.85, printed bar **29**: clear textural change to a more sustained/contrapuntal upper line with repeated articulated lower chords; **p** marking. Bar 29 is NOT automatically a formal B-section boundary.
- p.85, printed bar **45**: **Più lento**, four-sharp key signature, upper flowing beamed figure with a printed triplet at the opening, and **sostenuto** lower line. The section contrasts in register, rhythm, harmonic surface, and foreground role. A four-sharp signature alone cannot establish specific harmonic functions.
- The bar 40–44 transition includes running lines and a punctuating/resting passage; specific cadence labels and pitch-by-pitch NCT types are not asserted.

## Algorithmic extraction (original proposal, not Chopin transcription)
**Hierarchy:** (1) define section-level foreground role and harmonic destinations, (2) define bass/harmonic clock and independently moving melodic clock, (3) generate rhythmic figuration, (4) verify vertical and linear dissonances, (5) vary motives across two bars and larger phrases. A surface three-note loop is insufficient.

**Event representation:** `{voice, onset:Fraction, duration:Fraction, pitch, accent, chord_window, tie_id, provenance}`. Harmony changes do not reattack held notes. Active condition `onset <= t < onset+duration`; check membership at each boundary and record contextual resolution separately.

**Dissonance labels:** passing tone requires approach and departure evidence, neighbor requires return to structural tone, suspension requires preparation/hold across harmonic change and contextual resolution, appoggiatura requires accented onset and plausible resolution. If evidence is absent use `UNKNOWN`, not an invented classification. Chromatic pitch proximity is never sufficient on its own. Editorial-score notes are not interchangeable with first-edition facts.

**Section role transformation:** A-texture short disruptions and chordal punctuation -> contrasting lyrical foreground in lower register with upper rapid subdivision; keep coherent harmonic destination. This is an independent generative model inferred from edited-score contrast, not a literal reproduction of original events.

**Motivic development:** Two-bar tuple `(attack phases, durations, contour, register, bass motion, harmonic target, cadence)`. Preserve one anchor, alter at least two independent parameters, and test 4–8 bar cadential coherence. Reject mere transposition and identical three-note cycles; treat acceptance as a candidate, not musical quality certification.

## Verification and critical audit
**This run:** directly inspected two consecutive score pages (PWM pp.84–85). Read GitHub studies 053 and 054. Their five synthetic Python assertions were previously reported executed in 054; **no Python test was executed this run**. No production generator was modified or tested. No first-edition/autograph facsimile was inspected. No reliable note-by-note harmonic, counterpoint, or NCT audit of original Chopin was performed; exact pitch claims deliberately avoided. No user-approved exemplar was compared. Consequently **quality gate FAIL / PARTIAL**, not a completed Chopin-specific implementation.

## Handoff without fourth study
For Op.25 No.6, prioritize first-edition facsimile before asserting bar-level pitches; then inspect original-score 16th/32nd division, simultaneous voices, harmonic boundary, 2-bar transformations, and production Python tests. Preserve all unverified Op.25 No.5 issues in this handoff; do not reopen this work as a fourth study.
