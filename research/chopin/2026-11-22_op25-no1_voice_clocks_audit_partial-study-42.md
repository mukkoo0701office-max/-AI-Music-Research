# Chopin Research 042 — Op.25 No.1: independent voice clocks and dissonance audit (2/3)
Date: 2026-11-22. Status: PARTIAL / quality gate NOT PASSED.

## Scope and count
GitHub research/chopin directory listing showed one prior Op.25 No.1 record, study 041. This is documented run **2/3**. Op.10 No.12 closed at 3/3; no return to it. Next and final permitted study of Op.25 No.1 is 3/3; then move to Op.25 No.2 regardless of incompleteness. Count is based on main-branch research records, not exhaustive execution logs.

## Evidence ledger
- [DIRECT TEXT READ] Study 041 in this repository: 6/8, multi-layer arpeggio, independent structural melody, proposed nonharmonic-tone audit; explicitly no original score image inspection or executed tests.
- [DIRECT TEXT READ] Study 08 in this repository: v2's three-note-cell repetition, target-note-only harmony check, and unimplemented two-bar sequence were acknowledged limitations. Do not infer that its earlier tests validate the new proposal.
- [DIRECT WEB READ] Online Chopin Variorum Edition source-browser page https://chopinonline.ac.uk/ocve/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ exposes the Etudes Op.25 collection and source categories. Its dynamically loaded score images were NOT accessible in this inspection; no bar-specific pitch or harmony is claimed.
- [PREVIOUS STUDY'S CATALOGUE CLAIM, NOT RE-VERIFIED IMAGE] Study 041 reports distinct autograph page/bar enumerations (0–49 vs 1–50). Treat edition-specific measure IDs as opaque until image concordance.
- [ORIGINAL ALGORITHMIC HYPOTHESES] All rules and hypothetical examples below are new compositional design, not transcriptions or proven features of Chopin's bars.

## Problem decomposition: three clocks, not one repeated cell
Plan a two-bar 6/8 phrase with independent:
1. harmonic regions H(t), including change points and a functional destination;
2. bass trajectory B(t), whose attacks may be sparse;
3. melody anchor trajectory M(t), whose notes may be sustained across multiple figuration attacks.
A fourth event stream F(t) is the arpeggiated texture. Never infer melody solely from highest sounding note: prefer voice continuity, recurrence, duration, metrical prominence and editorial voice evidence. Keep explicit provenance on every extracted score event.

Use rational time in units of one whole note: each 6/8 bar lasts 3/4; a sixteenth lasts 1/16, so 12 slots/bar and 24/two bars. An eighth is 1/8, and 32nds are 1/32. A 6/8 bar has 24 possible 32nd slots. This is a timing model, not a claim that every original bar uses all slots.

## Generative grammar (original)
First generate a phrase skeleton (2 bars) with target harmony, bass destination, upper anchor(s), and one contour transformation. Then allocate each arpeggio gesture to a variable-length set of slots, not hard-coded three-note cells. Candidate contours: upward expansion, return, inversional shift, registral compression, delayed apex, or gap/rest. The second bar must preserve an identifiable interval/contour/rhythmic relation while changing at least two independently recorded features: e.g. bass goal and anchor shape, or harmony and register. Repetition is permitted when explicitly marked as intentional ostinato; a change counter alone does not prove musical development.

For each event record (voice, pitch, onset Fraction, duration Fraction, articulation, tie link, harmony ID, accent, structural weight, origin=[score-verified|secondary|original], source location, dissonance status). Preserve separate sounding and notated timelines where necessary. If melody is a conceptual line extracted from notes also assigned to figuration, represent references to shared events rather than double-counting attacks.

## Nonharmonic tone audit
At every note onset AND every harmonic boundary crossed by a held note, compute pitch-class membership in the explicitly defined harmony (including selected extensions). A nonmember is not automatically an error: inspect the same voice's preparation, metrical accent, melodic approach and resolution.
- PASSING: stepwise entry and stepwise continuation in same direction, typically between stable pitches.
- NEIGHBOR: stepwise departure from and return to a reference pitch.
- SUSPENSION: prepared consonance retained/tied into a new harmony, dissonant after boundary, then stepwise resolution; do not conflate notated tie with slur.
- APPOGGIATURA: accented dissonance with subsequent stepwise resolution; preparation not required.
- ANTICIPATION: early arrival of a subsequent harmony's tone, with continuity into that harmony.
- UNRESOLVED: insufficient local evidence, ambiguous segmentation, altered harmony interpretation, or unresolved leap.
Classification must allow multiple candidates; no blanket prohibition of accented dissonance. Vertical clashes are contextual, not simply pitch-class mismatches. Harmonic labels are hypotheses until independently checked against source.

## Explicit synthetic regression scenarios (NOT score facts)
A. 6/8 bar with 12 consecutive sixteenths in one voice: exact 3/4 duration; remove one and require a rest or flag incomplete coverage.
B. Two voices may overlap without being a duration error; within each monophonic voice overlapping sounding notes require an explicit tie or polyphonic subvoice designation.
C. A held C across a synthetic change from C major to G7 is a chord member on both sides; a held F across C major to G7 changes from dissonant (unless C11 explicitly admitted) to G7 seventh; audit both regions, not just onset.
D. In a synthetic C-major context, E–F–G can be passing F, E–F–E can be upper neighbor F, and G–F–E can be passing F; the actual classification still depends on accent and harmony duration.
E. Two-bar sequence with identical 3-note cells and only transposition is flagged as shallow by a heuristic, but can be allowed with an explicit compositional justification.
F. 32nd subdivision: 24 equal events in 6/8 total 3/4; 23 without rest is incomplete.

## Validation contract / implementation integration
Required program checks: Fraction arithmetic and per-voice coverage; tie continuity; onset and cross-boundary harmonic audit; two-bar motif relation plus diversity metrics; pitch range; melodic anchor persistence under figuration changes; event provenance; tests with expected failures. For code integration, inspect and adapt research/chopin/code/chromatic_engine_v4.py before claiming integration. Do not silently reuse v2's limited target-note assertion as a full dissonance classifier.

## Critical self-audit
PASS: direct comparison with repository study 041 and study 08; source-browser access verified; precise original generator specification; exception handling and falsifiable test cases.
FAIL: original score-image access and direct measure/pitch verification; autograph/first-edition comparison; original-work harmonic/formal analysis; direct inspection of current v4 code; test execution; integration. No code was executed in this run, and synthetic scenarios are *specified*, not reported as passed. This is **partial research**, not a quality-gate completion.

## Handoff
Op.25 No.1 study 3/3: first seek actual original score facsimile and record verifiable page/bar observations with edition IDs; inspect v4 code and run executable tests if feasible. Regardless of remaining issues, close Op.25 No.1 at 3/3 and proceed to Op.25 No.2. No fingering or practice research; no audio, PDF or MusicXML deliverables.
