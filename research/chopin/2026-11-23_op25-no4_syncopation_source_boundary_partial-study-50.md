# Chopin Research 050 — Op.25 No.4, source-bound syncopation architecture (1/3)
Date: 2026-11-23. **PARTIAL; primary score notation not directly inspected.** Cumulative count **1/3**; previous target Op.25 No.3 closed at 3/3 in study 049. Next: Op.25 No.4 (2/3), maximum 3 runs.

## Source provenance and boundary
- Fryderyk Chopin Institute, 2025-10-10, exhibition report on autograph engraver's copy: https://blog.nifc.pl/en/artykul/81-a-chopin-manuscript-presentation-in-the-composer-room-of-the-fryderyk-chopin-museum-autograph-stichvorlage-of-the-etude-in-a-minor-op-25-no-4-30-september-to-31-december-2025 . This authoritative institutional description reports an autograph intended for Paris publisher, with engraver marks, three written sides, opening **Agitato**, quarter=120, and revisions to notes, slurs, dynamics and pedalling. These are **reported manuscript facts**, NOT direct examination of its notation.
- Chopin Online OCVE source index: https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/ . The indexed copyist source locates No.4 on p.11 (bars 0–30), p.12 (31–65). Index metadata only; note readings unverified.
- IMSLP Op.25 catalogue: https://imslp.org/wiki/Etudes%2C_Op.25_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 . Lists French first edition 1837 and Warsaw copyist source (No.4 copied by Julian Fontana). This copy is **not the same object** as the Paris engraver's autograph held by BnF. Do not conflate them.
- PTNA explanatory commentary: https://enc.piano.or.jp/musics/22817 (2019-08-07). Secondary: A minor, 2/2, Agitato, on-beat bass versus offbeat chords; from bar 9, upper melodic voice legato against detached inner voices. The bar-9 boundary is **secondary report**, not independently verified.
- First-edition encoded score project: https://chopinscores.org/en/partytura/113 (German Breitkopf & Härtel first edition, 1837); encoded score access advertised, but no underlying note events independently downloaded/verified this run.
**No specific original pitch, harmonic sequence, cadence, or score-derived note event is asserted.**

## Existing repo examined
Study 049 explicitly closed Op.25 No.3 after 3/3; study 08 demonstrates why three-note-cell repetition is insufficient; actual `research/chopin/code/chromatic_engine_v4.py` uses `contour` with four chromatic steps per direction, checks only every fourth fast note for chord membership, has no bass/inner voice event clock, accent mask, held-tone audit or real contrapuntal dissonance tests. This research adds a different architecture rather than mislabelling v4 as a validated Chopin generator.

## Composition algorithm hypothesis (entirely synthetic, NOT a transcription)
Define an event as `(voice, onset: Fraction, duration: Fraction, pitch, articulation, accent, harmonic_window, source_status)`. Separate structural `bass`, `melody`, `inner_chord` voices; right/left hand assignment is secondary to voice identity. Represent 2/2 bar as one whole note; quarters at offsets 0,1/4,1/2,3/4 and eighth offbeats at 1/8,3/8,5/8,7/8. **Do not assume every original chord falls at these offsets**: this is a synthetic design grid.

1. Compose 4–8 bar harmonic/cadential targets and independent bass skeleton before rhythm; assign upper melodic destination tones and register curve.
2. Generate bass anchors at strong metric positions; place compact inner chord attacks at selected delayed/offbeat positions with controlled density. Phase-offset is the transformation variable, not a mechanical alternating template.
3. Sustain upper melodic tones over inner-chord reattacks; permit separate articulation per voice even at the same onset. Do not merge all right-hand notes into one chord event.
4. For a two-bar successor preserve at least one melodic/functional anchor while transforming >=2 of: offbeat phase, chord spacing, bass contour, melodic sustain duration, register or harmonic rhythm. Reject cloned 3-note cells and transformations that change only transposition.
5. Mark passing, neighbor, appoggiatura, suspension, anticipation as **candidate** until neighboring voice notes, metrical stress, preparation/resolution, current harmony, and harmony-change crossings are examined. Unclassified dissonance remains UNKNOWN and blocks 'validated' status.
6. Scan every onset and harmony boundary, including currently sounding held tones, for vertical clashes, voice crossings, parallel perfect intervals, and unresolved accented dissonances; log context-sensitive exceptions.
7. Preserve a distinct event-level source provenance: `original_verified`, `secondary_report`, `synthetic`, `unverified`. A synthetic example can never be promoted to a primary-score fact.

## Concrete adversarial tests required before implementation acceptance
A: bass onset 0, inner chord 1/8, melody 0 held 1/2: preserve all three independent clocks; classify overlap at 1/8.
B: melody 0 held 1/2 with harmony change 1/4: evaluate harmony twice, but do not invent a new attacked note at 1/4.
C: inner chord at 1/8 plus bass at 0 with coincident upper melody: articulation may differ across voices.
D: event at 3/4 duration 1/2 crosses barline: enforce exact Fraction and notation tie separate from phrasing slur.
E: an accented upper non-chord tone lacking resolution must remain UNKNOWN, not automatically passing.
F: exact 2-bar rhythmic copy with only transposition fails developmental gate.
G: compare autograph, French first edition and German first edition before promoting any score-specific claims.

## Critical audit / unresolved
**Actually checked:** repository studies 049, 08 and v4 source; source catalogue descriptions and institutional/secondary commentary. **Not performed:** original score image inspection, note-by-note original harmony, first-edition variant comparison, executable test of the proposed new architecture, v4 integration, original-music output. Thus quality gate **FAIL / partial research**. The listed tests are *specified*, not executed. Next research should prioritize directly legible score pages and executable counterexample fixtures; do not imply that a source index proves any note reading.
