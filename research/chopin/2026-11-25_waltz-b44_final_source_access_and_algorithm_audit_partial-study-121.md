# Chopin Research 121 — Waltz E major B.44 / KK IVa/12 — FINAL 3/3 (PARTIAL)
Date: 2026-11-25 JST. Purpose: reusable composition/arrangement algorithms, not performance/fingering.

## Cumulative count and stop rule
Prior files 119 (1/3) and 120 (2/3) were directly read in the connected repository. This is study **3/3** in the visible series; the historic deleted/renamed-file audit remains incomplete. **Close B.44 now, regardless of unfinished tasks. Never run a fourth B.44 study.** Next work must choose another composition after checking its count. Op.10 No.2 is already beyond the cap.

## Evidence and source-critical result
- IMSLP work catalogue https://imslp.org/wiki/Waltz_in_E_major,_B.44_(Chopin,_Fr%C3%A9d%C3%A9ric) identifies first-edition scan **#975554**, 2 pp., *Album Towarzystwa muzycznego we Lwowie* no.3, Lviv 1861, plate 343, pp.6–7. It lists 1880 Breitkopf #138636 and 1894 Mikuli/Schirmer #975553 as distinct later witnesses.
- Chopin Online https://chopinonline.ac.uk/ describes its CFEO collection of early printed witnesses, AC first-edition catalogue and OCVE source comparison. This is an institutional resource description, **not** evidence that B.44's notes were inspected.
- Attempted IMSLP first-edition image link /Special:ImagefromIndex/975554; access returned a JavaScript redirect, **not a readable score**. No source-page notes, bar-level pitches, sectional form, harmonic functions, ornamentation or cadence locations can be certified here. Earlier secondary A–B–A–C–A–B–A / tonal-region assertions remain **unverified**. The 1861 metadata is stronger than the conflicting unspecific 1871/72 claim, but first-edition physical page/title verification remains open.

## Existing implementation and defects
Read research/chopin/code/two_bar_event_validator_v1.py and studies 119/120. The v1 signature merges voices at equal onsets and drops duration, diatonic spelling, harmony and bass function. Its transformed() excludes literal transposition, a valid sequence operation, while accepting contour-similar but structurally incoherent mutations. Prior report 120 documents global harmony across witnesses and non-reciprocal ties in waltz_event_audit_v2.py. **No repository code was modified here.**

## Reusable ORIGINAL algorithm, NOT a Chopin transcription
1. **Source contract:** Every event carries witness_id, score_page, system, bar, voice, attack, duration, written pitch spelling, sounding pitch, tie-in/out, confidence. If source is inaccessible, source_fidelity=UNKNOWN and score-derived features are forbidden.
2. **Hierarchical generation:** Plan sectional return and cadential destination before elaborating events. Motif identity uses multiple anchors across two bars; surface changes may alter register, density, harmonic rhythm and texture. A three-note cell cannot alone prove thematic development.
3. **Harmony and bass:** Maintain witness-specific non-overlapping harmonic intervals; each bass arrival has a structural role and may be connected by inversions, pedals or chromatic approaches only when the destination and voice-leading justify them. Modulation requires a sustained region or cadence, not one altered pitch.
4. **Two-bar comparison:** Partition events by voice, preserve simultaneous attacks, exact rational durations, spelling and metric position. First classify exact reprise; constant semitone shift with preserved rhythm/voice = chromatic transposition; diatonic sequence additionally needs scale-degree/diatonic-step consistency and a harmonic trajectory. If evidence missing, UNCLASSIFIED. A valid rhythmic variant must document the mapping of structural anchors; no contour-only shortcuts.
5. **NCT audit:** Classify CHORD/PASSING/NEIGHBOR/SUSPENSION/RETARDATION/APPOGGIATURA/ANTICIPATION/ESCAPE/UNKNOWN. Suspension requires prepared consonance, a sustained/tied pitch across harmonic change, and contextual resolution; appoggiatura requires an attacked accented dissonance and appropriate resolution. Explicitly retain UNKNOWN for ambiguous local harmony. Treat vertical collisions and parallels as flags for review, not indiscriminate bans.
6. **Density:** Quarter-note beat=1, sixteenth=1/4, thirty-second=1/8; complete 3/4 bars with rests, exact rational coverage, reciprocal ties and no unintended overlap. Keep structural attacks distinct from embellishing attacks. Validate accent and dissonance after density expansion, not just before.
7. **Counterpoint:** Keep bass, middle and upper voice identity across changes of texture; check registral overlap, voice crossing, contrary motion opportunities, dissonance resolution and repeated perfect intervals in structural positions.

## Executed adversarial microtest (synthetic only)
A separate Python Fraction-based microtest was actually run during this study (not added to the repo). Classifier compares ordered (voice,onset,duration,pitch) and returns EXACT_REPRISE for identical events, CHROMATIC_TRANSPOSITION for constant shift, otherwise UNCLASSIFIED. **5 assertions passed**: identical sequence; +2-semitone transposition; alternating nonconstant offsets rejected; changed voice rejected; altered duration rejected. These are minimal logical checks only: they do NOT validate diatonic sequences, NCT, harmonic grammar, counterpoint, score fidelity, or the existing repository implementation. Do not report a full validator test pass.

## Quality gate / critical self-audit
**PARTIAL — primary-score note verification FAILED (access blocked).** No bar-level Chopin claims, no witnessed note transcription, no source variants, no full Python regression, no generator integration. The algorithm above is a reusable *proposal*, not a verified model of this waltz. Research is closed by the three-run rule; carry source-access, full event schema and NCT/regression needs forward as **cross-work infrastructure tasks**, never as a fourth B.44 study.

## Next target
Inventory the repository and select the next unstudied waltz or, if earlier priority studies remain under cap, follow priority Op.10/25. Never reset counters or revisit a three-run work.
