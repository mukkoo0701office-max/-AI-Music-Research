# Chopin Research 058 — Op.25 No.6 final study 3/3 (PARTIAL, CLOSED)
Date: 2026-11-23. **Cumulative count: 3/3** (056, 057, 058). No fourth study of Op.25 No.6. Next: Op.25 No.7 (1/3), subject to repository count verification.

## Source and evidence ledger
- [Chopin Online German first-edition catalogue](https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/) indexes Op.25 No.6 on pp.26–30 and page/bar spans 1–13, 14–26, 27–36, 37–47, 48–63 (metadata inherited from 056; current web viewer returned generic browse interface, not legible notation).
- [Chopin Online corrected German reprint](https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/8d3ec7a8022530d1a0025b0df6a255e6/) is a distinct witness, not an interchangeable first impression.
- [PTNA commentary](https://enc.piano.or.jp/en/musics/22819) describes G-sharp minor, alla breve and double-third writing; this is secondary commentary.
- **No first-edition noteheads, pitch spellings, bar-level harmonic functions or variants were verified visually in this study.** No exact note-level claims are made. Source gate FAILED.

## Existing repository read, not just inferred
- Read Research 056 and 057 (two-voice third-stream, half-open harmony windows, synthetic boundary tests).
- Re-read 07 and 08: 07 separates fast chromatic, middle harmonic, and slow bass clocks; 08's `chromatic_engine_v2.py` repeats a three-note figure four times and checks only the final target pitch against a chord-tone set.
- Read `research/chopin/code/chromatic_engine_v2.py` and `chromatic_engine_v4.py`. v4 brute-forces eight ±1 directional groups, tests 32-note continuity and chord-tone anchor count, but does **not** model two simultaneous independently classified upper voices, spellings, accented NCT resolution or actual contrapuntal/harmonic boundaries. Neither file was modified. The present test harness is separate, not a production integration.
- No verified user-approved reference exemplar was accessible for this run.

## Final reusable design: independent upper dyad + bass, ORIGINAL GENERATIVE HYPOTHESIS
1. Create phrase plan first (harmonic windows, two-bar anchor points, bass targets, tension-release trajectory). Use exact rational onset/duration, half-open time intervals, pitch spelling, explicit voice identity and provenance fields.
2. Generate two *distinct* upper lines U and L, each with its own goal and continuation; dyad interval is an emergent property, not a forced perpetual 3/4-semitone gap. Preserve intended thirds where musically warranted but flag chromatic and registral exceptions for contextual audit. Bass is a third slower line, not a copy of U/L attack rhythm.
3. At every attack, release and harmony change, evaluate active voices. A held tone crossing a chord change must be checked in both windows without creating an attack; release exactly on the boundary must NOT overlap the next window.
4. NCT classifier per voice: identify chord membership first, then candidate passing (stepwise same-direction), neighbor (departure/return), suspension (prepared tie and step resolution), appoggiatura (accented arrival and contextual resolution), else REVIEW or UNKNOWN. These are *candidate labels* until meter, spelling, actual harmony and surrounding notes are established. Never certify all non-chord tones by a target-only test.
5. Two-bar transformation: preserve one recognizable anchor while varying at least two independent features (contour, rhythm, accent phase, harmonic goal, register, bass relationship). A transposed clone or a single changed goal is not development by itself. Apply phrase-level constraints before ornamentation; reject mechanical three-note-cell loops.
6. Exact subdivision: represent 16ths and 32nds as fractions; audit each voice's coverage, overlap, ties and ornamental density. Separate note-count correctness from musical adequacy.
7. Critical contrapuntal scan: compare successive structural sonorities for unintended perfect-interval parallels, exposed dissonances and voice crossings; do not prohibit parallel thirds categorically. Exceptions require contextual review, not blanket acceptance/rejection.

## Executed independent tests, and limits
Ran Python 3 with `fractions.Fraction` in a separate local test script, **nine assertions passed**:
1. Held [0,1/2) overlaps the second harmony [1/4,1/2).
2. Note [0,1/4) does not overlap the next harmony [1/4,1/2).
3. Synthetic ascending chromatic approach classified PASSING_CANDIDATE.
4. Synthetic departure-and-return classified NEIGHBOR_CANDIDATE.
5. Missing continuation returns UNKNOWN.
6. Missing harmony returns UNKNOWN.
7. Changing only harmonic goal is insufficient two-bar development.
8. Changing contour and accent phase passes the minimum variation gate.
9. 1/16+1/32+1/32=1/8 exactly.
These tests exercise only a miniature **synthetic classifier**; they do not validate actual Chopin notes, suspension/appoggiatura logic, production integration, formal quality, score-level counterpoint, or user-preferred musicality. No test files committed; the nine cases are specified above for reproducibility.

## Adversarial self-critique / handoff
- Passing/neighbor predicates use semitone distance and lack diatonic spelling, beat strength, chord-change timing and voice-leading ambiguity. A chromatic approach can be harmonic or an appoggiatura: labels remain candidates.
- Two-dimension development threshold is a necessary *screen*, not proof of artistic quality.
- A dense dyad stream may obscure melodic hierarchy: add structural reduction and phrase-goal scoring, not merely more notes.
- Source-image access through the consulted catalogue viewer was insufficient for note-level verification. **Primary score comparison, real-bar NCT audit, full 2-bar sequence production implementation and regression against user-approved exemplars remain UNVERIFIED.**
- Quality gate: **PARTIAL / NOT COMPLETE**. Research limit is exhausted; do not reopen this work as a fourth study. Transfer unresolved cross-cutting implementation issues to the next composition-algorithm target without mislabeling them as Op.25 No.7 score facts.

No fingering/performance analysis, no audio, MusicXML or PDF deliverables.