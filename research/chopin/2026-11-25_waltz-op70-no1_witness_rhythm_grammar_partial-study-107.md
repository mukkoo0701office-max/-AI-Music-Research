# Chopin Research 107 — Waltz Op.70 No.1 / WN42 — source-version rhythm grammar (PARTIAL 1/3)
Date: 2026-11-25 JST. **Cumulative work-specific run: 1/3**, based on the inspected `research/chopin` directory: no earlier Op.70 No.1 record was listed. Prior work Op.69 No.2 closed at 3/3 (research 104–106). Do not revisit any work beyond three runs.

## Source ledger and what was actually checked
1. Chopin Online OCVE source catalogue: https://chopinonline.ac.uk/ocve/browse/acview/12fd2b9b9c0b2cc3619df0bd25922231/ . The listed Op.70 No.1 French first impression has pages 2 (bars 0–28), 3 (29–64), 4 (66–97); German first impression has pages 4–6 with the same catalogue ranges. These are **catalogue descriptions**, not directly read noteheads. The omission of bar 65 in the displayed page ranges must not be silently resolved.
2. NIFC work catalogue: https://chopin.nifc.pl/en/chopin/kompozycja/57_waltz-in-g-flat-major . Describes two surviving manuscripts dated 1832 and 1833, a dance/trio design, contrasting slower lyrical trio with parallel thirds, and a D-flat-major complementary theme. These are secondary descriptive assertions; bar-level musical facts have NOT been visually verified here.
3. PTNA: https://enc.piano.or.jp/en/musics/23223 . Discusses three divergent versions (1832 autograph, 1833 autograph, Fontana-based posthumous publication), including differing dotted rhythms, sixteenth rests, and eighth-note treatment of opening pickup. This is **secondary commentary** and a useful falsifiable source-variant hypothesis, NOT a direct collation of the manuscripts.
4. IMSLP catalogue: https://imslp.org/wiki/Waltzes_Op.70_%28Chopin%2C_Frederic%29 . Confirms listing of Op.70 No.1 in G-flat major, Molto vivace, posthumous publication 1855; again catalogue only.
**Primary notation gate:** No manuscript/first-edition score image was actually opened and read at notehead level in this run. Accordingly **no bar-specific pitch, rhythm, harmony, or edition variant is certified by primary-score inspection**. The catalogue of primary witnesses was checked, not the notation. This is a quality-gate failure, not completion.

## Repository continuity and defects
Directly read `research/chopin/2026-11-21_op10-no2_algorithm-study-08.md`, `research/chopin/2026-11-25_waltz-op69-no2_final_source_access_and_validator_partial-study-106.md`, and `research/chopin/code/waltz_event_audit.py`. The current audit relies on `assert` (disabled with Python -O), accepts harmonic gaps if an event intersects some harmony, and `two_bar_transform` accepts any single-field change. These defects remain **unpatched**. Do not count source metadata edits as a musical transformation.

## Generative proposal — ORIGINAL algorithm, not claimed as Chopin transcription
- Input `WitnessRhythmProfile` keyed by witness ID, edition state, source image, bar number and verification status. For anacruses use rational offsets relative to the first full bar; never assume a universal pickup duration across witnesses.
- Define a 2-bar `Motif` containing onset/duration tuples, accent weights, contour anchors, voice-role map, harmonic goals, bass schema and ornament hierarchy. Transform by a **substantive** change in attack grouping, contour or harmonic destination while retaining at least one audible invariant. Require explicit literal-reprise flag for exact repetition.
- Model dotted-note + rest, eighth-note regularization, and syncopated pickup as **alternative hypotheses** to be selected only by witness-specific verified score readings. A posthumous editorial version is not automatically Chopin's final intention.
- Separate structural anchors from subdivisions: a 16th or 32nd note must have exact rational duration and an explicit passing/neighbor/anticipation or ornament role; enforce total bar length and voice continuity. Do not densify the trio by default: density should be phrase-role dependent.
- Nonchord-tone auditing must split held tones at harmonic boundaries without adding false attacks; distinguish chordal extensions from NCT, inspect accented approach and resolution and retain UNKNOWN if harmony/voice identity cannot be established. Pitch-class exclusion alone does not prove a dissonance.
- Model a potential lyrical contrasting section with changed voice roles (melody in parallel thirds, according to NIFC secondary description), not merely a tempo or texture preset; test independent melodic trajectories and dissonance-resolution constraints.

## Explicit checks to implement (NOT executed in this run)
1. Reject witness-free and edition-merged assertions; verify source page/bar correspondence including OCVE catalogue bar 65 gap.
2. Validate pickup plus complete-bar rational durations, rests and tied continuations; fail on gaps and overlaps in all voices and harmony timeline.
3. Reject accidental `assert`-only validation under optimized Python.
4. Reject superficial two-bar transformations (metadata-only, one-token changes), while allowing marked literal reprise.
5. Adversarial NCT tests: accented appoggiatura resolving stepwise, prepared suspension over changing harmony, chordal ninth misclassified as NCT, and unresolved UNKNOWN.
6. Compare source-specific rhythmic profiles only after direct manuscript/first-edition image inspection. No score-based regression was executed.

## Critical verdict / next handoff
**PARTIAL 1/3, score-primary quality gate NOT PASSED.** Source catalogues and prior implementation were inspected; direct primary notation comparison, executable tests, code modifications, and score-based algorithm validation were NOT performed. The substantive research insight at present is a source-aware *hypothesis* about rhythmic-version grammar, not a verified extraction from Chopin's notation. Next run may continue Op.70 No.1 (2/3), prioritizing actual first-edition and autograph images before musical assertions; stop after cumulative 3/3 regardless of completeness. No user-facing audio, MusicXML, PDF, or fingering work. Existing schedule unchanged.
