# Chopin Research 068 — Op.25 No.10, study 1/3: octave texture and formal-contrast model

Date: 2026-11-23. **PARTIAL — source-note verification gate NOT PASSED.** Cumulative count for Op.25 No.10: **1/3** (previous 067 closes Op.25 No.9 at 3/3 and names No.10 next). No earlier No.10 study was found by repository code search for `op25-no10`; this is not an exhaustive audit of all filenames/commits. Next No.10 run 2/3, subject to recount; maximum 3.

## Evidence and source hierarchy
- **Primary-source catalogue inspected, not notation:** Online Chopin Variorum Edition, *Etudes Op.25*, https://chopinonline.ac.uk/ocve/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ . The autograph/copyist Stichvorlage inventory lists No.10 on manuscript pages 28–32, bars 1–20, 21–50, 51–86, 87–114, 115–119 respectively. This is a page/bar locator, **not direct reading of any notes, harmonies or articulation**. It supports a targeted next-source inspection.
- **Secondary manuscript context, not direct witness inspection:** https://fchopin.net/etude_source/ identifies the Op.25 No.10 German-edition Stichvorlage as a Gutmann copy with Chopin corrections. This attribution must be cross-checked against the original witness before quoting any variant.
- **Secondary broad-form hypothesis only:** https://en.wikipedia.org/wiki/%C3%89tude_Op._25%2C_No._10_%28Chopin%29 describes B minor outer sections, a contrasting B major middle section and meter/texture contrast. Treat this as a testable hypothesis; **no exact section boundary, chord, pitch, tempo, or meter has been checked in primary notation**.
- **Repository actually read:** full study 067 and 065; `research/chopin/code/chromatic_engine_v4.py`. Study 067 reports its own direct examination of 065/066, but this run did not read 066 or studies 07/08 directly. No user-approved exemplar was available for direct regression.
- **Source gap:** no legible score image was opened for note-by-note inspection. Do not present the following original models as verified Chopin practice.

## Actual code defect confirmed in v4
`contour()` uses `out.extend(out[-1]+direction for _ in range(4))`. Because `extend` evaluates a generator while mutating `out`, each group forms four successive semitone steps; the entire 32-note stream is driven by only eight binary directions. The optimizer samples just eight four-note anchors against two harmonies and checks only consecutive semitone distances. It has no simultaneous octave representation, no independent bass voice, no phrase/section roles, no chord spelling, no contextual nonchord-tone classification, and no harmony-boundary held-note audit. Its `PROGRESSION` is explicitly original and unrelated to the actual étude. Thus a passed `audit()` cannot validate Chopin-like composition.

## ORIGINAL reusable compositional algorithm (hypothesis, not transcription)
**Core idea:** a large formal change should transform *texture grammar* and *harmonic trajectory* together, rather than simply transposing or slowing a three-note cell.

1. Define a section graph `A–B–A′` as an **engineering prototype**, with per-section mode, pulse grid, register envelope, harmonic rhythm, voice roles, attack density, cadence target and contrast budget. Do not assert exact source form without reading score. Require B to differ from A on at least two independent dimensions (e.g. texture and harmonic rhythm); A′ must recover one recognizable structural invariant while changing at least one development parameter.
2. Represent a chordal octave as **one event** with `spelled_pitches=(lower,upper)`, common onset and articulation, rather than two serialized notes or automatically independent counterpoint. For actual independent lines use separate `voice_id` and verify voice-leading; octave doubling alone is not parallel-octave misconduct.
3. Design a long-range structural melody and bass arrival graph before surface attacks. Create two-bar phrases with explicit contour goal, apex, cadence, tension, register, bass destination, and motif-invariant; disallow transposition-only cloning when role is DEVELOPMENT. Allow intentional reprise when marked REPRISE.
4. Generate subdivisions with exact rational durations: eighth-note triplets, sixteenths, thirty-seconds and rests are different grids. Preserve tuplet ratio, notation length, and sounding release independently. A section change may alter grouping without forcing tempo doubling.
5. Harmony/NCT: maintain spelled chords and actual bass per harmonic window. Check every note onset **and every harmony change during held notes** using half-open sounding intervals. Passing/neighbor/suspension/appoggiatura classifications require same-voice before/after context, metric accent, preparation/tie, harmonic change and resolution. Unknown evidence => UNKNOWN, not PASS; expressive dissonance can be REVIEW rather than automatically deleted.
6. Two-bar sequence: preserve a specified motive invariant but change at least two of contour destination, accent topology, harmony, bass arrival, texture, or register; validate 4–8-bar phrase coherence and section-level return rather than counting local note differences.

## Executed independent synthetic tests (NOT repository generator)
Executed Python `fractions.Fraction` test in this run: (1) two half-bar events sum exactly to one bar; (2) each synthetic simultaneous octave has 12-semitone span; (3) at half-bar boundary the prior event is inactive and the new event active; (4) a synthetic two-unit development changes at least two structural parameters. **4 assertions passed.** These MIDI pitches and parameters are invented for test purposes, not source-note evidence. No v4 execution, no integrated regression, no actual score validation.

## Required negative/regression tests (specified, NOT executed)
- Triplet-duration mismatch vs meter => REJECT; thirty-second-note overflow => REJECT.
- Simultaneous octave mistakenly serialized => REJECT; two genuine independent voices in consecutive parallel octaves => FLAG.
- Prepared suspension without step resolution => REVIEW; tied dissonance without preparation => not SUSPENSION.
- Held note crossing a harmonic boundary => re-evaluate; note ending exactly on boundary => do not re-evaluate.
- B section differs only by transposition => FAIL contrast; A′ fails to recall any A invariant => FAIL return; developmental two-bar units identical except transposition => FAIL.
- Bass duplicates every upper attack rather than defining independent arrivals => REVIEW.

## Self-audit and handoff
**PARTIAL / NOT COMPLETE.** No direct score-image transcription, no note-level harmonic/formal analysis, no verified user-approved-example comparison, no direct reread of studies 07/08, no production-code patch or production tests. The only executed tests are four synthetic assertions. For study 2/3: open OCVE manuscript page 28 (bars 1–20) and a contrasting page, record witness/page/bar and verifiable notation, compare with first French edition, then audit whether section contrast, octave event grouping and NCT model genuinely explain observed score. If inaccessible, explicitly retain unknowns. Never exceed three total No.10 runs. No fingering/performance study or user-facing media output.
