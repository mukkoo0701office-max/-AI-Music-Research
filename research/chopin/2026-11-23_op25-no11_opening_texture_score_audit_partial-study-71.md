# Chopin Research 071 — Op.25 No.11, study 1/3: opening and texture handoff

Date: 2026-11-23. Status: **PARTIAL — primary-edition note verification pending**. Cumulative count **1/3** (prior 068–070 concern Op.25 No.10; its 3/3 closure is respected). Next: Op.25 No.11 study 2/3.

## Sources and provenance
- **Directly inspected visual notation**, page 1 of a modern, unattributed derivative score (NOT an authenticated first edition): https://pianistforum.com/wp-content/uploads/2022/11/Chopin-Etude-Op.-25-No.-11-Winter-Wind.pdf . Page shows mm.1–12. It is evidence for **that edition's layout**, not automatically for Chopin's autograph.
- Noctave https://noctavepiano.com/en/sheet-music/chopin-etude-op25-11/ states its transcription derives from NIFC first French edition Henry Lemoine 1837, source kern/025-1b-LE-011.krn version 95dfb10. **Metadata read; underlying first-edition scan / kern not directly compared**. Do not elevate it to SOURCE_VERIFIED note claims.
- Prior repository studies 07/08 fetched and read: three-layer time architecture, the shallow 3-note cell and lack of NCT audit. Study 070 fetched: provenance gate and closure of No.10. Original Python generator `research/chopin/code/chopin_op10_2_generativestudy.py` fetched: 16 semiquavers per 4/4 bar with monotone chromatic traversal, quarter-note harmonic layer, quarter-note bass, no vertical/NCT audit. User-approved musical examples were not directly examined.

## Visually verified in the modern derivative page
1. Measures 1–4 carry **Lento** and a restrained opening: upper melodic single-note line in mm.1–2, then chordal upper texture in mm.3–4. Upper staff dynamic p then pp; mm.2 and 4 include fermatas; m.4 rit. Bass enters in mm.3–4. This is a **texture/role transformation**, not a claim about every exact pitch.
2. Measure 5 begins **Allegro con brio**, f risoluto. High, fast upper-staff beamed notes include a printed sextuplet bracket; lower staff features bass and chordal attacks. Measure 6 maintains the busy upper figuration while the lower staff has more sustained chords. This supports a **layered attack-density contrast** in the inspected derivative score.
3. Measures 7–8 continue rapid upper events with distinct contour/range and lower sustained/moving harmonic supports; mm.9–10 present ascending/descending runs, while lower events have different attack rhythms. The texture is not accurately described by a fixed 3-note loop.
4. No exact original-edition pitch, local chord symbol, bar-level harmonic function, or non-chord-tone identity has been established. The derivative has 8va, tuplets, and multi-staff notation; a naive linear 16-note-per-bar model would miss tuplets, simultaneous attacks, and octave displacement.

## Proposed original generative algorithm (NOT a transcription)
`Section = (tempo_zone, phrase_function, role_map, harmonic_windows, density_envelope, register_envelope, motive_invariants)`.
- **Section A (announcement)**: generate sparse upper melodic statement, then redistribute its invariant interval/rhythmic contour into a chord-supported texture, with optional bass entry. Preserve identifiable phrase arrival.
- **Section B (high-density)**: promote the structural theme to the lower/chordal layer and generate an independent high-density ornamental stream in the upper layer. Separate `structural_voice` from `figuration_voice`; do not infer structural priority from note count.
- Use `Fraction` onset/duration, explicit tuplets, 8va sounding-pitch conversion, ties, rests, simultaneous chord events, and independent voice clocks. Compute attack density per half-bar and distinguish it from harmonic rhythm.
- Generate 2-bar `PhraseUnit` as target-harmony, bass-goal, register curve, and motive transformations. Preserve one declared invariant (e.g. contour or accent grouping); transform at least two of register, subdivision, harmonic destination, bass motion, voice distribution. Literal transposition alone is not sufficient for DEVELOPMENT.
- NCT audit at **each sounding onset and harmony boundary**: classify passing only with directed stepwise context; neighbor only with return; suspension only with preparation, tie/hold across changed harmony, and resolution; appoggiatura only with accent and resolution. Ambiguous: REVIEW. Enforce voice-leading across all layers, not just endpoints.
- Chord spellings and harmonic functions must be source-derived or explicitly tagged ORIGINAL_HYPOTHESIS. No hard-coded claim that the invented harmonic model reproduces Chopin.

## Verification contracts and negative fixtures (specified, NOT run)
1. Sparse-to-dense transition must alter density and role-map; failure if merely repeat 3-note cells.
2. Six-in-the-time-of-four tuplets must sum to the notated duration exactly; fail if 6 ordinary 16ths are counted as an entire quarter without correct time modification.
3. Octave markings must affect sounding MIDI but not overwrite written pitch provenance.
4. A held note changing harmonic role must be reassessed at boundary without a new attack.
5. Reject suspension label without preparation or resolution; reject passing-tone label on leap.
6. Two-bar DEVELOPMENT must pass invariant-preservation and two independent transformations.
7. Disallow SOURCE_VERIFIED for any pitch or chord unless edition witness + page + bar + readable notation and independent comparison are attached.

## Critical self-audit / next handoff
**Quality gate NOT PASSED.** One modern score image was inspected directly, but first-edition/autograph score has not been inspected; no barwise verified pitch/harmony/NCT transcription; no tests executed; no integration into existing Python generator; no approved-example crosscheck. This is a bounded *partial* study, not completed Chopin analysis. Study 2/3 should inspect NIFC/OCVE original witness and verify a small exact span before implementing a source-grounded event extractor. No performance/fingering research or user-facing media.
