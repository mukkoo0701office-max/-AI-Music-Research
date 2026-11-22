# Chopin Research 052 — Op.25 No.4 final boundary audit (3/3)
Date: 2026-11-23. **PARTIAL, quality gate FAIL.** Cumulative count: **3/3** (050, 051, 052). **Closed by hard research-count cap**. Next target: **Op.25 No.5 (1/3)**. Do not reopen No.4 for a fourth run.

## Evidence and limits
- Read actual repository studies [050](2026-11-23_op25-no4_syncopation_source_boundary_partial-study-50.md) and [051](2026-11-23_op25-no4_harmonic_boundary_phase_regression_partial-study-51.md) this run. They document inspection of studies 08, 049 and Python v4; this run **did not re-fetch v4**. Their seven synthetic assertions were reported as run in 051; **not independently rerun here**.
- [Online Chopin Variorum Edition](https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/) browsed this run; browser returned the general catalogue/filter interface, **not a legible score page**. Thus no original notehead, bar-specific harmony or accent was verified.
- [NIFC institutional autograph report](https://blog.nifc.pl/en/artykul/81-a-chopin-manuscript-presentation-in-the-composer-room-of-the-fryderyk-chopin-museum-autograph-stichvorlage-of-the-etude-in-a-minor-op-25-no-4-30-september-to-31-december-2025), [OCVE source index](https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/), [CFEO](https://chopinonline.ac.uk/cfeo/browse/acview/8e377a53981012591f150675c386c67b/), and [PTNA commentary](https://enc.piano.or.jp/musics/22817) were catalogued in 050–051; **not fresh direct note-level corroboration**.
- Original Chopin facts, secondary commentary and original *synthetic algorithm* must be stored as separate provenance classes. No synthetic notes below are attributed to Chopin.

## Transferable generative specification (original hypothesis; not transcription)
1. Plan harmonic function windows, cadence and 4–8-bar bass/foreground trajectories before distributing attacks. Represent three independent event streams: bass, sustained melody, detached inner harmony. Each event has `voice, onset, duration, pitch, accent, articulation, provenance`.
2. Use exact rational times (whole note = 1). Build a sorted list of non-overlapping harmony windows `[start,end)`. At every attack, release and harmony boundary, collect sounding notes with `onset <= t < onset+duration`. Harmony lookup must satisfy **start <= t < end**, never merely `start <= t` (051 discovered this bug).
3. A sustained note that becomes non-chordal across a harmonic boundary is not a new attack. Assign candidate labels for passing, neighbor, suspension, appoggiatura, anticipation, pedal and unresolved; require preparation, metrical stress, voice motion, chord context and resolution evidence before asserting a label. Return `UNKNOWN` on missing context, not `PASS`.
4. For each two-bar successor retain at least one functional/bass or melodic anchor but transform >=2 of: syncopation phase, inner-attack density, register contour, bass motion, harmonic rhythm, melodic sustain. A transposed rhythmic clone is rejected. This is a **heuristic**, not a guarantee of musical development.
5. Counterpoint: compare simultaneous structural voice pairs at successive meaningful slices, detect repeated parallel perfect fifths/octaves and crossing; flag for context-sensitive review rather than absolute rejection. Also scan lower-register cluster density, articulation separation, unresolved accented dissonance, and cadential direction.
6. Output only after rhythmic duration, active-note boundaries, dissonance provenance, motive identity and structural arc tests pass. No exercise/fingering model.

## Adversarial acceptance fixtures (specified here, **not executed in this run**)
- Held note [0,1/2), chord windows [0,1/4), [1/4,1/2): chord membership recomputed at 1/4, without extra onset.
- Inner harmony at 1/8 against bass at 0 and melody at 0: all three voice clocks and articulation identities survive.
- 1/16 + 1/32 + 1/32 = 1/8 exactly; event [3/4,5/4) spans a barline with separate notation tie.
- Accented non-chord note without verified resolution => UNKNOWN.
- Two-bar sequence with only pitch transposition => fail; successor with independent phase and contour change plus preserved anchor => structural gate pass.
- Parallel-perfect scan includes notes held through another voice's attack; avoid spurious repeated comparisons of unchanged simultaneities.
- Edition provenance disagreement => UNVERIFIED until a legible score comparison, never silently select one edition.

## Critical self-audit and handoff
**Confirmed this run:** read 050/051; OCVE web catalogue reachable; explicit closure of cumulative study count. **Not confirmed:** direct primary-score notation, precise Op.25 No.4 harmony/form, original event-level nonharmonic-tone audit, new code execution, integration into production Python, musical quality. The proposed engine remains unimplemented; no new tests passed this run. This record is a **research closure / unresolved handoff**, not a completed scholarly analysis. Do not use it as evidence that the original score was inspected.
For Op.25 No.5 start with readable primary notation, independent source identification, and an executable minimal audit; keep prior generic rules as reusable tests, not as fresh findings about No.5.
