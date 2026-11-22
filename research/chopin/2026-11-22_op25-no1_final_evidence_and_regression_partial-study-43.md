# Chopin Research 043 — Étude Op.25 No.1, final permitted study (3/3)
Date: 2026-11-22. Status: PARTIAL, quality gate NOT PASSED. **Study count: 3/3; do not revisit this piece in another study. Next Op.25 No.2 (1/3).**

## Provenance and study count
Directly read repository studies [041](2026-11-22_op25-no1_layered_arpeggio_partial-study-41.md) and [042](2026-11-22_op25-no1_voice_clocks_audit_partial-study-42.md); both are marked 1/3 and 2/3 respectively. Main branch contains those two Op.25 No.1 records; other undocumented runs are not independently excluded. This is final allowed 3/3 under the user's cap.

Also directly read [07](2026-11-21_op10-no2_algorithm-study-07.md), [08](2026-11-21_op10-no2_algorithm-study-08.md), [chromatic_engine_v4.py](code/chromatic_engine_v4.py), and [user-approved feedback](../../feedback/Feedback_001_Shizukana_Kitai_Piano_Jazz_Preferences.md). The feedback's smooth guide-tone motion is a user preference, NOT evidence about Chopin.

## Primary source status
Online Chopin Variorum Edition work/source catalogue https://chopinonline.ac.uk/ocve/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ was directly loaded on 2026-11-22. It identifies Études Op.25 as a source category and first-edition abbreviation types (FFE, GFE etc.), but score results are dynamically loaded and **no primary facsimile page was directly inspected**. Prior 041 identifies autograph manuscript ranges with conflicting bar numbering, which remains unverified at the image level. Thus **no measure-specific pitch, harmonic claim, original note values, or source variants are asserted**. Catalogue access is not score verification.

## Code inspection: concrete limitations of existing v4
The existing Python module is a 4/4-style 32-event/two-bar chromatic laboratory with eight direction blocks of four semitone steps. `contour` extends four repeated directions per block; `generate_pair` scores only pitch-class membership of eight block-start anchors against a pair of harmonies, with `harmonies[k//4]` assigning four blocks to each harmony. This does **not** implement a 6/8 12-sixteenth grid, independent voice streams, contextual nonharmonic-tone classification, or real two-bar motivic sequence transformation. `audit()` checks length, chromatic adjacency, and pair-boundary jumps, but does not check source-based music, harmonic boundaries of sustained tones, or voice collisions. Do not claim it validates Op.25 No.1.

## Original compositional algorithm (hypothesis, not transcription)
1. First generate a two-bar 6/8 structural skeleton: independent bass goals B(t), upper melodic anchor M(t), harmonic regions H(t), and a figuration stream F(t). Represent rational onset and sounding duration; each bar lasts 3/4 whole note, twelve 16th slots or twenty-four 32nd slots.
2. Build arpeggio contours as variable-length gestures, not fixed 3-note cells. Candidate operators: expand registral span, displace apex, invert direction, compress range, change attack spacing, or suppress attacks. The structural melody is linked to selected existing sounding events rather than counted as a second sounding note.
3. Sequence operator on bar 2: retain at least one traceable feature (interval shape, rhythmic contour, or registral goal), transform at least two of harmony destination, bass motion, attack density, apex timing, and anchor shape. Explicitly allow purposeful ostinato. A mere change-count heuristic cannot prove musical quality.
4. For each nonchord note, check local same-voice approach, accent, preparation, resolution and competing harmonic interpretations. Classify PASSING, NEIGHBOR, SUSPENSION, APPOGGIATURA, ANTICIPATION or UNRESOLVED. Distinguish tie (sounding continuation) from slur (phrasing). Do not force ambiguous tones into one category.
5. Split held notes at every harmonic change for evaluation without creating artificial note attacks. Preserve separate written/sounding event models. Check bass/inner/upper spacing and pitch range; register-dependent clashes require musical review, not blanket prohibition.
6. Formal layer: plan a longer tension arc and cadence before generating dense notes. Two-bar operators should support varied continuation rather than mechanically transposed copies. These rules are transferable *proposals*, not verified Chopin-specific patterns.

## Executed regression checks (independent Python, not integrated into v4)
On 2026-11-22, executed a short Python `fractions.Fraction` script in the runtime; **seven assertions passed**:
- 12 × 1/16 = 6/8; 24 × 1/32 = 6/8; 11 × 1/16 is incomplete.
- Synthetic C-major -> G7 boundary at 3/8: held C starting at 1/4 and lasting 1/4 changes from chord member to nonmember; held G remains a member on both sides. Both segments were checked by overlap rather than onset alone.
- Two synthetic 8-unit rhythm profiles each total eight units; a pair of synthetic two-bar gesture descriptors changes at least two dimensions.
These checks verify arithmetic, a limited pitch-class boundary test, and a simple variation heuristic **only**. They do not test accent-based classification, score correspondence, musical taste, or integration. No score or audio output was produced.

## Critical audit and unresolved handoff
PASS: main-branch study count and direct comparison with 041/042, 07/08, v4, and approved feedback; explicit v4 limitations; executable independent rational-time checks; provenance separation.
FAIL: actual autograph/1837 first-edition score-image inspection; verified measure-by-measure structure and harmony; all-voice source audit; detailed appoggiatura/suspension tests; v4 integration and full regression suite. **Do not call this completed or historically score-grounded.**
Handoff to future general-engine work: build voice-event schema, source-image concordance and test fixtures. This must **not** trigger a fourth Op.25 No.1 study. Next target **Op.25 No.2 (1/3)**. Existing hourly schedule unchanged.
