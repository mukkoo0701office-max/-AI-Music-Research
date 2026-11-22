# Chopin Research 056 — Étude Op.25 No.6, study 1/3 (PARTIAL; primary notation not yet inspected)
Date: 2026-11-23. Cumulative count for **Op.25 No.6: 1/3** (this record). Op.25 No.5 is CLOSED at 3/3 (053–055); do not reopen it. Next target: Op.25 No.6 study 2/3. No performance or fingering research.

## Sources and verification boundary
- [Chopin Online, German first-edition exemplar, Op.25 Nos.1–6](https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/) indexes No.6 on printed pp.26–30, with bar ranges **1–13, 14–26, 27–36, 37–47, 48–63**. These are catalogue/page metadata, **not direct score-note verification**. Another corrected reprint is separately indexed [here](https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/8d3ec7a8022530d1a0025b0df6a255e6/).
- [IMSLP Op.25](https://imslp.org/wiki/Etudes%2C_Op.25_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29) identifies the 1837 Schlesinger French first edition and a manuscript source containing No.6 copied by **Julian Fontana**; the latter is **not an autograph by Chopin**.
- [ChopinScores, No.6, B&H first edition](https://chopinscores.org/pl/partytura/115) identifies a German first-edition score and advertises PDF, MEI and MusicXML export. These were **not downloaded or verified against a facsimile**.
- [PTNA Piano Music Encyclopedia](https://enc.piano.or.jp/en/musics/22819), commentary by Shiori Imazeki (2019), identifies G-sharp minor, alla breve, Allegro; a rapidly ornamented double-third foreground and a separate left-hand accompaniment. This is **secondary commentary** and does not establish any precise original bar-level pitch, interval sequence or harmony.
- Directly read GitHub [Research 055](2026-11-23_op25-no5_final_score_comparison_and_handoff_partial-study-55.md), [053](2026-11-23_op25-no5_source_form_and_dissonance_protocol_partial-study-53.md) and [052](2026-11-23_op25-no4_final_source_limit_and_algorithm_handoff_partial-study-52.md). These warn against false NCT classification, repeated three-note cells and improper harmony-window membership. **Studies 07/08 and production Python were not re-fetched this run**; earlier notes about their defects are inherited, not independently retested. No user-approved exemplar was retrieved.

## Distinctive research question
How can a two-note-per-attack, rapidly subdivided foreground form an independently coherent **pair of melodic trajectories**, while a slower bass/harmonic stream establishes phrase-level direction? A double-third label alone cannot justify treating every event as a diatonic third or as two homorhythmic chord tones. Source-confirmed exceptions must be sought in actual notation.

## Original generative algorithm — NOT a transcription of Chopin
Represent a paired foreground event as `(t: Fraction, d: Fraction, upper_pitch, lower_pitch, upper_voice_id, lower_voice_id, articulation, stress, harmony_window, source_tag)`. Track each pitch spelling and melodic continuity separately, not just an interval class; ensure lower_pitch < upper_pitch unless an explicitly flagged voice exchange occurs. **Do not hard-code 3 semitones or 4 semitones for every event**: chromatic spelling, suspensions and changing harmony require interval exceptions with evidence.

1. **Structure first:** specify 4–8-bar phrase destinations, cadential pressure and bass trajectory; allocate harmonic windows with exact half-open bounds `[start,end)`.
2. **Two-voice skeleton:** create two distinct but coordinated contour paths, with anchor tones, contrasting local motion and a target at each 2-bar boundary. Reject a pitch-transposed clone of a 3-note loop; preserve one anchor and change at least two independent dimensions (contour, rhythm, accent phase, register, harmonic destination).
3. **Subdivision:** derive 16th/32nd attack grids as exact rational fractions of the whole note. Distinguish *ornamental neighbor/passing motion* from *structural two-voice counterpoint*; the same apparent dyad may require two separate linear classifications.
4. **Bass independence:** generate the bass from harmonic goals rather than doubling the paired upper attack grid; sample all sounding voices at attacks, releases and harmony boundaries.
5. **Dissonance audit:** classify each pitch against the active chord and its own voice context, with explicit preparation, metrical weight, continuation and resolution; output `UNKNOWN` when these are unavailable. A held tone crossing a chord boundary must not acquire a fictitious new onset.
6. **Counterpoint audit:** flag simultaneous structural perfect intervals, consecutive parallels, crossings, unresolved accented tones and lower-register congestion for contextual review. Avoid labeling a series of parallel thirds as a general contrapuntal failure.
7. **Formal gate:** check whether the paired texture changes density, contour, harmonic rhythm and foreground role across phrase boundaries; continuous motion alone is not evidence of development.

### Proposed executable tests (NOT executed)
- Exact-time: 1/16 + 1/32 + 1/32 == 1/8 using `fractions.Fraction`; no float drift.
- Distinct-voice: upper and lower contours remain separately addressable under dyadic attacks.
- Harmony boundary: active dyad `[0,1/2)` evaluated against windows `[0,1/4)`, `[1/4,1/2)` without reattack.
- Chromatic exception: a non-third or altered-third event is *flagged for source/context review*, not automatically silently rewritten to a diatonic third.
- NCT negative: absent voice continuation or harmonic context => UNKNOWN, never PASS.
- Two-bar sequence: transposition-only clone rejected; an anchored contour+phase variation admitted only as a candidate.
- Vertical scan: independently moving bass attacks are included even when upper dyad is held.
- Source gate: any exact Chopin pitch/bar assertion lacking edition + page + readable image => UNVERIFIED.

## Critical audit and unresolved handoff
**Confirmed in this run:** GitHub 052/053/055 content; institutional first-edition catalogue page ranges; source-type distinction; secondary account of double thirds and independent accompaniment. **Not confirmed:** direct first-edition noteheads, edition variants, specific original harmonies/NCTs, bar-level form, user-approved reference quality, any newly executed Python test or production integration. Therefore **quality gate FAIL / PARTIAL**, not a finished Op.25 No.6 analysis.

**Study 2/3 priority:** directly inspect legible pp.26–27 of a named 1837 edition; compare a few bounded passages with another source; test whether each moving dyad really comprises two continuous melodic strands, identify genuine exceptions, and run the adversarial tests on the existing Python implementation. Study 3/3 must close the subject regardless of incompleteness. Do not manufacture note-level evidence.
