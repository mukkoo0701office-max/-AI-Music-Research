# Chopin Research 047 — Étude Op.25 No.3: source provenance and rhythmic architecture (1/3)
Date: 2026-11-22. **Status: PARTIAL — primary score image not directly inspected; no pitch-level claims.**
Cumulative Op.25 No.3 count: **1/3** in the research/chopin sequence as checked against the current repository tree; earlier undocumented attempts cannot be ruled out. Op.25 No.2 closed at 3/3 in [046](2026-11-22_op25-no2_final_evidence_regression_partial-study-46.md). Next permitted Op.25 No.3 study: 2/3, unless additional earlier records are discovered.

## Evidence and source boundaries
1. [Online Chopin Variorum Edition, Op.25 source index](https://chopinonline.ac.uk/ocve/browse/acview/887542e8785ef984d8321af5ed9640f3/): the Op.25 engraver's-copy composite (A&C, 25–A&C) lists No.3 on **p.8, bars 0–20; p.9, bars 21–40; p.10, bars 41–72**. These are **index metadata, not verified score readings**.
2. [Online Chopin Variorum Edition, first French edition index](https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/81463b2d142d5d52c8dbca2bd48fde76/): first French edition lists No.3 **p.9 bars 0–16, p.10 bars 17–36, p.11 bars 37–55, p.12 bars 56–72**. The different page divisions do not establish different music or note values.
3. [NIFC facsimile publication description](https://sklep.nifc.pl/en/produkt/77085-etudes-op-25-autographs-and-copies-national-library-warsaw): Op.25 German publisher's Stichvorlage composite includes two autographs (Nos.1 and 8) and ten composer-authorised copies. **No.3 must not be called an autograph solely because it belongs to this collection**. Shelf mark Mus.217 Cim, National Library in Warsaw, per NIFC.
4. [ChopinScores German first-edition No.3](https://chopinscores.org/en/partytura/112): catalogues Breitkopf & Härtel, October 1837, F major. Score is offered in digital formats, but this run did not download or validate a score page or symbolic transcription.
**Primary-document availability is indexed; primary notation is not directly read.** No original bars, pitches, cadences, rhythmic cells, voice counts or source variants are asserted as directly verified.

## Prior work inspected, and difference from it
Read [07](2026-11-21_op10-no2_algorithm-study-07.md), [08](2026-11-21_op10-no2_algorithm-study-08.md), [046](2026-11-22_op25-no2_final_evidence_regression_partial-study-46.md), [v4 engine](code/chromatic_engine_v4.py), and [approved preferences](../../feedback/USER_PREFERENCES.md). 07/08 progressed from straight chromatic runs to 3-note-cell repetition; v4 still generates 4-note same-direction blocks and tests block starts only. 046 proposes rational clocks and harmonic boundary splitting but did not integrate them. This study adds **accent-phase-aware pattern grammar** as an explicit implementation design, not a verified characterization of No.3.

## Composition algorithm proposal — SYNTHETIC, not Chopin transcription
**Layer plan**: (A) formal destinations and 2–4 bar harmonic cadence map; (B) independent bass and harmonic rhythm; (C) singing top-voice anchor events; (D) mid-register guide-tone continuity; (E) high-density surface figuration. Generate A–D before E, never infer harmonic correctness from note-count alone.

**Time representation**: store each onset and duration as a rational number of whole notes (Python Fraction); represent beat grid and grouping separately from onset. For each layer, event = (voice, onset, duration, pitch, harmonic_window, metric_accent, structural_weight, motif_id, source_status). A slur is a phrasing edge, not a tie. Split sounding intervals at every harmony change, preserving one attack and a continuous tie group where appropriate.

**Rhythmic-pattern grammar (unverified source hypothesis)**: a two-bar gesture is described by an accent mask, melodic target sequence, contour, registral arc, articulation groups, harmonic arrival times, and density curve. Candidate transforms include (i) displacement of accent mask without moving cadence, (ii) subdivision expansion from eighths to sixteenths, (iii) swapping surface figure between voices, (iv) inversion of local contour while retaining guide-tone target, and (v) bass-target substitution constrained by a planned harmonic function. Avoid copying a fixed 3-note cell. In 2-bar continuation require at least two independent changed dimensions; preserve at least one identifiable invariant, e.g. interval contour at structural anchor notes or the accent grouping. Treat changed dimensions as measurable descriptors, not a proof of aesthetic development.

**Nonharmonic audit**: classify each note against its *sounding* harmonic window and surrounding same-voice notes. Passing candidate requires stepwise motion into and out of dissonance in the same direction; neighbor candidate returns to same pitch; suspension requires prior consonant preparation, a sustained dissonance across harmony boundary, then resolution; appoggiatura candidate is accented and resolves by step; anticipation arrives early and is subsequently consonant. If any context is absent, return UNKNOWN rather than assigning a confident label. Test simultaneous cross-voice minor seconds/ninths, dissonant bass clashes, parallel perfect intervals and overlap at actual event boundaries; musical exceptions must be reviewed, not silently banned.

**Counterpoint and hierarchy**: the fast layer may cross the structural melodic register only when its voice identity and foreground/background role remain legible. Audit guide-tone motion and low-register spacing separately from fast ornamental density. User preference for natural harmonic direction, 3rds/7ths in inner voices, smooth chromatic approaches, and an arched top line is a **user design requirement**, not a finding about Chopin's Op.25 No.3.

## Test specification (NOT EXECUTED in this study)
- Fractional bar sums for mixed eighth/sixteenth/thirty-second-note durations and tuplets; allow anacrusis only when explicitly encoded.
- Two overlapping voices at different onset clocks, including a note held across a harmonic boundary.
- Positive/negative tests for passing, neighbor, suspension, appoggiatura, anticipation, ambiguous.
- A two-bar source motif and transformed successor with two descriptor changes and one retained invariant; reject identical 3-note-cell loops.
- Verify one cadence destination against both bass target and melody anchor; compare accent phase before and after transformation.
- Full engine integration and actual original-score annotation **not performed**; do not report test passes.

## Critical audit and next steps
**Verified:** source catalogue locations, composer-authorised-copy provenance, existence of previous research and v4's limitations, proposed data contract.
**Not verified:** direct score image, any No.3 note or rhythm, actual form/harmony, voice-leading at specific bars, edition variants, executable tests, musical output quality, generator integration. **Quality gate FAIL for complete source-grounded study**; this is an evidence-bounded architecture proposal only.
For 2/3, obtain and inspect actual p.8 of the A&C and p.9 of the French edition, document precise visual bar-level readings with version tags, then implement and execute at least one of the tests above. If score access remains blocked, report that instead of inventing notes. After 3/3, advance to Op.25 No.4 regardless of completion.
