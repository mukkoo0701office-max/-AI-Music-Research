# Chopin Research 053 — Op.25 No.5, study 1/3 (PARTIAL; quality gate FAIL)
Date: 2026-11-23. Cumulative Op.25 No.5 research count: **1/3**. Previous Op.25 No.4 closed 3/3 in research 052; do not revisit. Next: Op.25 No.5 2/3.

## Directly inspected sources and provenance
- [Chopin First Editions Online: Breitkopf & Härtel Op.25 Nos.1–6](https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/8d3ec7a8022530d1a0025b0df6a255e6/) indexes No.5 on printed pages 20–25, with bar ranges **0–20, 21–44, 45–64, 65–84, 85–105, 106–138**. These are *catalogue ranges*, not an independent verification of the noteheads, meter or section boundaries. The site rendered a filter/catalogue interface rather than readable facsimile.
- [IMSLP Op.25](https://imslp.org/wiki/Etudes%2C_Op.25_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29) indexes manuscript Mus.217 Cim (Nos.4–6 in Julian Fontana's copy), 1837 French first edition Schlesinger M.S.2427, and a later B&H impression. A copyist manuscript is not Chopin's autograph; later impressions must not be conflated with 1837 first printing.
- [ChopinScores Op.25 No.5](https://chopinscores.org/en/partytura/114) identifies a B&H first edition and provides encoded score download options, but this run did not inspect its notation.
- [Noctave edition notes](https://noctavepiano.com/en/sheet-music/chopin-etude-op25-5/) describe E minor 3/4, a scherzando outer idea with short–long chord/note displacement, and a contrasting E-major Più lento with left-hand melody and right-hand triplets. **Secondary/editorial description only**; its own edition reports editorial repairs and substitutions. These details remain unverified against a legible primary score in this run.
- Read repository studies [07](2026-11-21_op10-no2_algorithm-study-07.md), [08](2026-11-21_op10-no2_algorithm-study-08.md) and [052](2026-11-23_op25-no4_final_source_limit_and_algorithm_handoff_partial-study-52.md). 08's repeated three-note cells and missing NCT audits are known failures; 052 specifies exact boundary semantics. Production Python was **not fetched or executed** this run.

## Proposed generative model (original algorithm, NOT Chopin transcription)
**Structural hypothesis to verify from score:** outer sections may juxtapose metrically displaced short attacks with a more continuous lyrical middle. Do not label an ABA form as fact until formal boundaries are inspected.

Represent each event as (voice, onset:Fraction, duration:Fraction, pitches, stress, articulation, harmonic_window_id, provenance). Separate three clocks: foreground line, chordal interruptions, bass/harmonic support. For a contrasting section swap *foreground assignment* to bass/inner voice while upper voice becomes subdivided figuration; retain a common harmonic destination across the change.

**Expressive wrong-note test:** a dissonant attack is meaningful only if its surrounding voice-leading explains it. At each event and harmony boundary, compute active pitches using `onset <= t < onset+duration`; classify accented neighbor, appoggiatura, suspension, passing, anticipation, or UNKNOWN. A short note followed by a longer adjacent note is not by itself evidence of a specific nonchord-tone category. Store preparation, metric accent, adjacent interval, target chord, resolution time and voice continuity. Reject automatic labeling without these fields. Do not enforce a universal 'every dissonance resolves by step' rule: pedal, chromatic prolongation and intentional unresolved colors need separate documented exceptions.

**Two-bar development:** choose a 2-bar motive M with (attack phase, duration pattern, melodic contour, interval class, bass function, register, tension trajectory). Successor M' must preserve at least one identifiable anchor and transform >=2 independent parameters, with an explicit harmonic destination; mere transposition or three-note repetition fails. Phrase-level changes may span 4–8 bars and must be measured at cadence points, not only barlines.

**Section transformation:** generate a harmonic skeleton and independent bass line first; choose foreground voice; apply 16th/32nd or triplet subdivisions only where the beat grid and phrasing warrant. Validate rational-duration sums, ties across bars, simultaneous vertical intervals, voice crossing, lower-register congestion, and sustained dissonance on harmony change. Separate structural-note and ornament audits.

## Executable acceptance tests specified, NOT run
1. `Fraction(1,16)+Fraction(1,32)+Fraction(1,32)==Fraction(1,8)`.
2. Sustained pitch crossing harmony windows recomputes membership without inventing reattack.
3. Short accented dissonance with missing resolution evidence yields UNKNOWN.
4. Two-bar transposed clone rejected; changed rhythm and contour with common functional anchor accepted as *candidate*, not quality-certified music.
5. Triplet subdivision uses rational thirds; no floating-point rounding or collision with bass-clock onset.
6. Contrasting middle section transfers melody between voices without destroying independent clocks.
7. Source-specific bar and note assertions require scanned edition ID and page; absent facsimile => UNVERIFIED.

## Critical quality gate / next run
**Verified:** actual GitHub prior research 07, 08, 052 read; first-edition catalogue bar/page indexing and manuscript/edition metadata located; secondary editorial description identified. **Not verified:** actual noteheads in primary facsimile, exact original rhythmic figures or harmonies, bar-by-bar form, original nonharmonic-tone classifications, Python test execution, production integration, and user-approved musical quality. Consequently this is **partial source/protocol research**, not completed analysis. Next run (2/3) should retrieve a legible first-edition scan of pp.20–25, transcribe only small attributable observations with bar/page evidence, run adversarial Python tests, and compare encoded variants without treating them as authoritative. After 3/3 move to Op.25 No.6 regardless of completion.
