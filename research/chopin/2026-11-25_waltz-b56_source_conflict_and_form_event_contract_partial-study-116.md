# Chopin Research 116 — Waltz in E minor B.56 / KK IVa/15 — source conflict and event grammar (1/3, PARTIAL)
Date: 2026-11-25 JST. Scope: composition/arrangement algorithms, not performance technique.

## Cumulative count and selection
Repository directory inspected: Op.10 and Op.25 études have prior studies, with Op.25 No.12 final record 76; Op.18, 34, 42, 64, 69 and 70 waltzes each have three studies. Op.70 No.3 records 113–115 and is closed (3/3). No B.56-named record was present in the directory listing, so **provisional count 1/3**; Git commit history/renamed files not exhaustively audited. Do not exceed three total studies. Next candidate B.56 (2/3). This continues the previously established waltz sequence after Op.70; do not reopen Op.10 No.2.

## Evidence ledger — provenance before pitches
- IMSLP work catalogue https://imslp.org/wiki/Waltz_in_E_minor%2C_B.56_(Chopin%2C_Fr%C3%A9d%C3%A9ric) identifies B.56, E minor, circa 1830, and gives **first publication 1868**; its scans include later edited editions. **Catalogue inspected; no individual score image directly read in this run.**
- A Wikimedia Commons scan https://commons.wikimedia.org/wiki/File:Waltz_in_E_minor,_B.56_(IA_imslp-in-e-minor-b56-chopin-frdric).pdf is catalogued as an **1868 publication**, 5 pages; exact publisher and music text not verified.
- Other accounts, e.g. https://en.wikipedia.org/wiki/Waltz_in_E_minor_(Chopin), report **May 1851** as publication date. **Conflict unresolved; do not present either as an established first-edition date.** Seek library catalogue imprint, publisher plate, and earliest physical witness.
- Henle HN771 description (via https://www.ficksmusic.com/products/chopin-waltz-in-e-minor-op-posth-kk-iva15-henle) says the autograph is lost; this is a retailer's quotation of edition information, not firsthand archive confirmation.
- The reported introduction–A–B–A–B–A–C–A'–coda is a **secondary analytical hypothesis**, not a bar-verified formal graph; do not hard-code it as fact.
- Original note pitches, voice assignments, exact bar boundaries, harmonic rhythm, ornament spellings, repeat signs, and edition variants: **UNVERIFIED**.

## Reusable composition model (original design, NOT a transcription)
Separate form graph, harmonic timeline, and three event streams. Form nodes contain source confidence, sectional role, return relationship, cadence target and optional contrasting episode. A return may preserve a phrase skeleton while changing register, ornament density, inner-voice activity or harmonic support; demand a measurable difference from a literal copy.
Each event is (witness, bar, voice, onset:Fraction, duration:Fraction, written_pitch, sounding_pitch, attack, tie_in/out, ornament_parent, role, harmony_id, provenance). A note may not be asserted as a Chopin fact without source image/page/bar and independent transcription review.
For 3/4 bars, sum per-voice durations exactly 3 quarter units including explicit rests; attack-based motif comparison must omit tie continuations. Sixteenth = 1/4 quarter unit, thirty-second = 1/8. Cross-bar ties carry boundary state. Do not impose a 3-note cell as the default generator: plan 2-bar contour and phrase-level harmonic goal first, then allocate variable-length gestures and ornaments.
Harmony spans are half-open intervals [start,end), cover all sounding events, and may change inside a bar. NCT classifier must inspect metrical accent, preparation, approach interval, resolution interval and whether the next note belongs to the same voice. Passing = weak-beat stepwise between consonances; neighbor = departure/return; suspension = tied preparation plus downward resolution; appoggiatura = accented dissonance with resolution. Unclassified events are explicit UNKNOWN, never silently chord tones.
Two-bar development comparator must test contour, interval sizes, rhythm, cadence location and register, and distinguish exact copy, transposition, sequence and genuine modification. Preserve legitimate sequential transposition rather than rejecting it as non-development; report type.
Bass and inner voice require independent goals and voice-leading checks. Consecutive perfect intervals are warnings conditioned on contrapuntal context, not universal automatic rejection.

## Adversarial tests to implement, not executed
1. Reject 3/4 voice with 23/8 or 25/8 quarter-beat total over two bars; accept exactly 6.
2. Reject a tied continuation with changed pitch or missing tie partner; allow a cross-window tie with explicit state.
3. Classify a weak stepwise passing tone and an accented appoggiatura differently; UNKNOWN when harmony timing missing.
4. Distinguish exact repeat, transposed sequence and rhythmically varied return.
5. Reject harmony timeline gaps/overlaps; permit documented simultaneous polychord layers.
6. Reject 32nd-note ornament whose onset/duration overruns parent span.
All are proposed fixtures; **no Python execution or generator integration claimed**.

## Prior work and critique
Read research/chopin/2026-11-21_op10-no2_algorithm-study-07.md and -08.md: three independent layers are useful, but 3-note cells repeated four times are shallow; NCT, cross-voice verticals and two-bar sequences remained unverified. Read research/chopin/2026-11-25_waltz-op70-no3_final_event_validator_partial-study-115.md and code/two_bar_event_validator_v1.py: exact Fraction timing and tie reciprocity exist; motif signature reduces intervals to contour signs, and cross-window ties, NCT semantics and harmony are not handled. Reuse concepts without falsely treating the prototype as a validated B.56 generator. User-approved finished arrangements not independently inspected.

## Quality verdict and handoff
**PARTIAL / fails primary-score gate**. Score catalogue and edition descriptions were accessible, but original notation pages were NOT directly inspected; therefore no bar-specific claims. Publication chronology is contradictory. No executable tests performed. No production code changed. Next permitted B.56 study: verify earliest witness and inspect score pixels, establish a 2-bar event fixture with explicit edition provenance, run tests against it, and update cumulative count to 2/3. If source access remains blocked, record that limitation without inventing notes. After 3/3 move on regardless of completeness.
