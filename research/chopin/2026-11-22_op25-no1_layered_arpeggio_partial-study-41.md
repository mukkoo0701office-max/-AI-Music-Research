# Chopin Research 041 — Étude Op.25 No.1: layered arpeggio composition (1/3)
Date: 2026-11-22. Status: PARTIAL; quality gate NOT passed.

## Count and scope
Previous GitHub study 040 explicitly closes Op.10 No.12 at 3/3 and assigns Op.25 No.1 next. The main-branch research/chopin directory was listed and showed no prior Op.25 files. This is the **first documented run (1/3)**; other branches or undocumented executions not exhaustively checked. No fourth study of Op.10 No.12.

## Source provenance / verified scope
- Chopin Online, Online Chopin Variorum Edition source index, https://chopinonline.ac.uk/ocve/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ : lists Op.25 No.1 autograph Stichvorlage pages 1–3, bars 0–19, 20–37, 38–49; separately presentation autograph pages 1–3, bars 1–15, 16–30, 31–50. **Verified index only, NOT images or notes**. The discrepancy in numbering (0–49 versus 1–50) is a reason not to transfer bar indices uncritically.
- IMSLP https://imslp.org/wiki/Etudes%2C_Op.25_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 identifies autograph/copy manuscript collection and French 1837 first edition. Verified catalogue metadata only.
- ChopinScores https://chopinscores.org/en/partytura/110 identifies 1837 Breitkopf & Härtel first edition and digital score availability. Verified catalogue metadata only.
- A digitized facsimile excerpt is described at https://s9.imslp.org/files/imglnks/usimg/7/78/IMSLP700034-PMLP01969-Chopin_Etudes_op.10_Ignaz_Friedman_1915_with_Preparatory_Studies.pdf with 6/8 and small/large note distinction, but the actual image was **not visually inspected in this run**. No individual pitches, bars or variant readings are claimed verified.
- Secondary description https://en.wikipedia.org/wiki/%C3%89tude_Op._25%2C_No._1_%28Chopin%29 describes a melodic top line over interlocking arpeggiated layers, 6-note semiquaver groupings, and inner countermelodies; these are **secondary claims pending original-score confirmation**.

## Existing repository cross-check
Read research/chopin studies 07, 08 and 040. Study 07's three independent clocks, 08's failure of repeated 3-note cells, and 040's harmonic-boundary sustained-tone audit inform the architecture. Read feedback/Feedback_001_Shizukana_Kitai_Piano_Jazz_Preferences.md: user-approved smooth voice leading and controlled color are preferences, **not historical claims about Chopin**. This run did not directly fetch or execute chromatic_engine_v4.py.

## Transferable compositional hypothesis (original algorithm, NOT a Chopin transcription)
Build an abstract **6/8 two-bar phrase plan** before filling notes:
1. Define harmonic regions H(t) with functional destination, bass trajectory B(t), and upper melodic anchors M(t). Each layer has its own rhythm clock; the melody's notated/sounding duration is not inferred from accompaniment attacks.
2. For each dotted-quarter beat, generate six sixteenth-note slots, i.e. 12 per 6/8 bar, 24 per two-bar unit. Allocate notes across independent right/left hand streams rather than assuming every attack is a melody note. A melodic anchor may sustain conceptually while ornamented arpeggios continue.
3. Choose each arpeggio's contour from a phrase-dependent grammar (rise–fall, rising extension, displaced inversion, registral contraction, reversal); prevent identical short-cell looping unless marked as intentional ostinato. Define targets at the 2-bar boundary, and require at least two dimensions (bass goal, harmony, anchor contour, range, onset density) to change across a sequence.
4. For every event store voice_id, rational onset/duration, written pitch, source/evidence status, harmony_region, attack/continuation, structural_weight and dissonance_class. Structural melody is chosen by continuity and metric/accent evidence, **not merely the highest sounding pitch**.
5. Harmonic audit: classify accented/nonaccented nonchord notes using same-voice preparation and resolution. PASSING/NEIGHBOR require stepwise motion, SUSPENSION requires preparation + tie/hold + resolution, APPOGGIATURA accent + resolution; label ambiguous cases UNRESOLVED rather than force a diagnosis. Test held tones against each harmonic boundary.
6. Texture orchestration: keep bass arrivals and upper anchors audible, vary inner arpeggiation, avoid excessive low-register clusters. These are **original arrangement guidelines**, not claims of Chopin's exact scoring.

## Formal invariants / test design
- 6/8 bar length = 3/4 whole-note; six sixteenths per dotted quarter and twelve per bar. Each voice's sounding events must fit its timeline, permitting rests and polyphonic overlap across voices.
- Separate melody anchor and figuration events; changing the arpeggio must not silently move structural melody.
- On a two-bar sequence, retain a traceable motivic invariant while changing >=2 named dimensions; avoid blind transposition of a three-note cell.
- Test cases required: 12-slot completion, one omitted slot, multiple independent voices, cross-boundary sustained dissonance, correctly resolved passing and neighbor notes, unresolved leap, and intentional repeated pattern exception.
- These are **proposed tests only**. No Python test was run, and no integration or actual score-note audit was performed.

## Critical quality gate / handoff
PASS: primary-source **catalogue and page-range identification**; explicit separation of documented metadata, secondary descriptions and original generative hypotheses; repository precedent and user feedback comparison.
FAIL: actual original score-image inspection, note-by-note verification, autograph/first-edition comparison, reliable harmonic and formal analysis of score, nonharmonic-tone classification on score, runnable generator and test execution, integration with existing Python. Therefore NOT COMPLETE. Next permitted run Op.25 No.1 **2/3**, prioritize image-based primary-source examination and executable regression tests. After 3/3 move to Op.25 No.2 regardless of unresolved items. No fingering, practice advice or deliverable audio/score files.
