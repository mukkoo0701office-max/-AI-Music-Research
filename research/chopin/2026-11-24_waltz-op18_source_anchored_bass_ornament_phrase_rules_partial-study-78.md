# Chopin Research 078 — Waltz Op.18, study 2/3: source-anchored bass sustain, ornament timing and two-bar phrase contrast
Date: 2026-11-24. **Cumulative count: 2/3** (077 = 1/3; this study = 2/3). Next and last allowed: Op.18 3/3. Status: PARTIAL — score-image note-level verification unavailable.

## Prior work and evidence boundaries
Read study 077 directly from repository; its source-family model and unresolved score verification are the starting point, not repeated as new discovery. GitHub code search returned no matches for the historical 07/08 studies or Python generator, so neither their contents nor current code was independently checked in this run. Study 077 reports that 07/08 were read in that earlier run. User-approved examples not retrieved; integration and regression unverified.

Primary/critical editorial evidence: Jan Ekier and Paweł Kamiński, *National Edition: Waltzes*, Performance and Source Commentary, https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes_commentaries.pdf (consulted 2026-11-24). Source commentary pp. 4ff identifies AI, AII, A, FE1 and subsequent corrected impressions; editorial commentary is **secondary testimony about primary witnesses**, not direct facsimile reading. Online Chopin Variorum Edition source catalogue https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/5238e79031a187bcea1cd7bc57a24aa3/ (catalogue access; no note-level reading).

### Verified statements *from editorial commentary*, not from score-image transcription
- Op.18 bars **12, 36, 44, 165, 167, 169**, left hand: editors discuss sustaining the fundamental bass; slurs supplied in parentheses emphasize this, with sustain also wherever indicated by rhythmic value (performance commentary p.2).
- Bar **118 and analogous**, right hand: editors acknowledge alternative placement of grace notes, anticipatory or on beat (p.2). This is timing flexibility, not evidence of any specific harmony or pitch class.
- Bars **133–148** and **245–258**, right hand: editors distinguish light grace-note figures from the crotchet melodic line (p.2). A generative representation must keep melodic anchors distinct from ornaments, even if ornament onsets overlap accompaniment.
- Bars **165–180**: editors describe a dialogue between contrasting pairs: 165–166 / 169–170 versus 167–168 / 171–172 (p.2). The expressive interpretation is editorial; do not assert verified exact harmonic or melodic events in those bars.
- Source commentary pp.4ff identifies early AI as separate numbered waltzes corresponding to final bars 5–68, 69–116, 117–164 without coda; AII also lacks coda; FE1 derives from final A. This is evidence for version-dependent form.

## New compositional abstraction (original algorithm, NOT a transcription)
**A. Bass sustain as independent harmonic memory.** Model each event as (voice, onset rational, duration rational, pitches, structural_role, witness, confidence). Maintain a *bass-state* with an independently sustained fundamental even when accompaniment chord attacks occur on beats 2–3. Separate actual notated sustain from inferred auditory sustain; only notated ties/durations or source-confirmed evidence can assert a held sounding event. In an original 3/4 design: bass at t=0 duration=2 quarter units, chord at t=1 duration=1, chord at t=2 duration=1. Polyphonic voices overlap legitimately; no sum across voices.

**B. Ornament onset as a choice with stable anchor.** Store (anchor_event_id, ornament_group, timing_mode=BEFORE_BEAT|ON_BEAT|UNRESOLVED, voice_role). The melody anchor and accompaniment time remain invariant when testing ornament timing alternatives; never shift the entire bar to fit grace notes. Unresolved timing stays unresolved in source facts. Distinguish written rhythmic subdivisions from grace-note zero/variable-time semantics.

**C. Two-bar contrast grammar.** Define PhrasePair(A,B) with structural melody anchors, bass trajectory, harmonic goal, registral/dynamic profile, ornament density and rhythmic onset vector. Transform A→B by changing at least two meaningful features while preserving a recognisable motif signature (interval-contour skeleton or rhythm), then optionally return A'→B'. The editorial pair dialogue at 165–172 motivates the hypothesis, but no pitches or exact harmonic moves are attributed to Chopin.

**D. Harmony-sensitive non-chord-tone audit.** For each dissonance, test its relationship to a chord window and adjacent melodic anchors: passing (directional step continuation), neighbor (departure and return), suspension (prepared pitch sustained across harmony change and resolved), appoggiatura (accented approach/resolution), anticipation, or UNKNOWN. At a harmonic boundary, recompute the classification for each still-sounding pitch. A bass pedal can be structurally independent of the upper harmony; flag a conflict, not automatically an error. Do not license chromatic notes merely from scale adjacency.

**E. Avoid shallow 3-note modulo repetition.** Require motif genealogy: motif ID, transformation type, structural goal, phrase-boundary label; reject identical 3-note cell recycling in non-reprise passages. Score output for bass-line autonomy, anchor salience, harmonic function continuity, motivic development and justified dissonance.

## Executable test specifications (NOT executed)
1. Rational onset/duration: per voice, 3/4 measures total exactly 3 quarter units; polyphonic overlap and shared chord onset accepted.
2. Sustain across beat 2: independently held bass plus chord at t=1 must not be truncated by chord attack.
3. Grace-note alternatives: BEFORE_BEAT vs ON_BEAT must preserve the same anchor and harmonic timeline.
4. Source facts: every original-work pitch assertion requires facsimile witness + bar/page; otherwise UNKNOWN.
5. 2-bar contrast: a repeated cell with unchanged goals fails except labelled reprise; a contour-preserving but bass/harmony-shifting variant passes.
6. Held-note harmony reclassification: dissonance status recalculated on each chord boundary, including bass pedals.
7. Ornament-vs-melody test: grace-note density cannot replace structural crotchet anchors.
No code was executed or modified in this run; all seven remain proposed, NOT PASSED.

## Critical self-audit / handoff for study 3/3
**FAIL as finished source-grounded composition analysis.** Direct legible autograph/FE1 score-image comparison, bar-level pitch/duration transcription, harmony analysis and current Python integration are missing. Editorial bar references provide genuine targeted evidence but cannot substitute for the notation itself. Next study should obtain a legible primary witness, inspect a limited bar passage, identify exact rhythmic/voice facts only if visible, then implement/run at least a narrow test if repository source is accessible. Mark remaining gaps, close Op.18 permanently at 3/3 and advance to next unstudied waltz. No fingering/practice, audio, MusicXML or user-facing score produced.
