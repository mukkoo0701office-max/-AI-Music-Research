# Chopin Research 051 — Op.25 No.4, harmonic-boundary and phase audit (2/3)
Date: 2026-11-23. **PARTIAL — primary notation not directly inspected.** Cumulative Op.25 No.4 count **2/3** (050, 051). Next and final study 3/3; then move to Op.25 No.5, never a fourth study.

## Evidence / provenance
- [NIFC autograph exhibition report](https://blog.nifc.pl/en/artykul/81-a-chopin-manuscript-presentation-in-the-composer-room-of-the-fryderyk-chopin-museum-autograph-stichvorlage-of-the-etude-in-a-minor-op-25-no-4-30-september-to-31-december-2025): institutional description of Paris engraver's autograph, opening Agitato and quarter=120; **report, not directly read noteheads**.
- [Chopin Online OCVE](https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/): manuscript/copy source index, No.4 pp.11–12 (bars 0–30 and 31–65); **page metadata only**.
- [Chopin Online CFEO](https://chopinonline.ac.uk/cfeo/browse/acview/8e377a53981012591f150675c386c67b/): first German edition page index, No.4 pp.16–19; **metadata only**.
- [ChopinScores 1837 Breitkopf edition](https://chopinscores.org/en/partytura/113): edition identity and machine-readable score availability advertised; underlying original notation **not retrieved or collated**.
- [Facsimile publisher description](https://www.omifacsimiles.com/brochures/chop_et25%2C4.html): reports deleted bar before bar-65 A-major resolution. Treat as a secondary description, not a directly verified score variant. Source relationships must distinguish Paris autograph from Warsaw Fontana copy.
- [IMSLP Op.25 catalogue](https://imslp.org/wiki/Etudes%2C_Op.25_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29): first French edition and copyist manuscript catalogued. **No bar-specific pitch or harmony claimed.**

## Repository continuity
Read actual studies 050, 049, 08 and `research/chopin/code/chromatic_engine_v4.py`. v4 builds four-step semitone runs, tests only selected anchor pitches, and lacks separate event clocks, harmonic-boundary inspection, vertical nonharmonic-tone context, and developmental identity constraints. This study does **not** claim v4 was modified. The study-08 three-note-cell problem remains unresolved in the production engine.

## Original algorithm specification (synthetic, not Chopin transcription)
Event schema: `(voice, onset:Fraction, duration:Fraction, pitch, articulation, accent, provenance)`, all measured in whole-note units. Harmony: sorted non-overlapping `(start,end,pitch_classes,function,source)` windows. Distinguish bass, sustained foreground, and inner reattacks regardless of staff or hand.
1. Plan 4–8 bar functional targets, bass contour, melodic anchor and register arc; only then allocate delayed inner-chord attacks. Preserve independent clocks and distinct articulation per voice.
2. Sweep every note onset, release, barline and harmonic-window boundary. At each boundary, query all *sounding* pitches (`start <= t < end`) without inventing a new attack. A sustained pitch may be consonant before and dissonant after a harmonic change.
3. Dissonance classification is contextual: candidate passing/neighbor/appoggiatura/suspension/anticipation requires voice neighbors, metric strength, harmonic membership, preparation and resolution. Without sufficient evidence return `UNKNOWN` (hard stop for verified status); a pitch-class mismatch alone is not a forbidden note.
4. Separate 2-bar structural anchors from rhythmic surfaces. Preserve at least one bass/functional anchor, change at least two of independently measured accent phase, melodic register trajectory, inner-chord density, bass contour, harmonic rhythm; reject transposition-only clones. This is a minimum anti-cloning gate, **not** proof of musical quality.
5. Counterpoint scan checks parallel perfect intervals between actual successive structural simultaneities, voice crossings, low-register density and held-tone reinterpretation; justified exceptions must be logged. Do not automatically ban all dissonance or all parallel intervals without context.
6. For 16th/32nd subdivisions use exact rational arithmetic; notation tie across barline is distinct from phrasing slur.

## Executed synthetic regression (local Python; not committed to engine)
Ran a minimal Python `dataclass` / `fractions.Fraction` prototype with **seven passing assertions**: (1) held melody remains active at delayed inner attack; (2) held melody changes chord membership at 1/4 without reattack; (3) 1/16+1/32+1/32=1/8; (4) event 3/4+1/2 ends at 5/4; (5) 2-bar successor changes phase and register while preserving bass pitch-class anchor; (6) octave-transposed rhythmic clone rejected; (7) positive event duration. All examples are invented: bass MIDI48, melody MIDI67 and inner MIDI64, with C-major to D-minor pitch-class windows. **Not original Chopin notes.**
Important failure and correction: first execution **failed** assertion (2) because a `next(... for window if start<=t)` lookup selected the *earliest* eligible harmony at 1/4. Changed lookup to reverse chronological order, then reran: **7/7 pass**. Production implementation must use a sorted interval lookup and test boundary equality explicitly. The prototype has not been merged or committed, so reproducibility is limited to this documented test specification.

## Critical audit / next study
**Confirmed:** repository text/code review; catalogue and institutional source descriptions; seven synthetic assertions after a detected/fixed boundary-lookup bug. **Not confirmed:** direct primary score image reading, first-edition note-by-note variants, actual bar-specific harmony/accents/nonharmonic tones, formal segmentation, integration into v4, and musical effectiveness. Quality gate **FAIL / partial research**, not a completed Chopin source analysis.
For 3/3 prioritize legible original notation and edition comparison; otherwise close at 3/3 with explicit unresolved issues and move to Op.25 No.5. Do not spend research time producing MusicXML, MP3 or PDF.
