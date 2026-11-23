# Chopin Research 074 — Étude Op.25 No.12, study 1/3: source witness map and two-bar arpeggio grammar
Date: 2026-11-24. **Cumulative count for Op.25 No.12: 1/3 (074).** Previous No.11 CLOSED at 3/3 (071–073). **Status: PARTIAL / quality gate NOT passed.**

## Sources and verification
- Chopin Online, *Online Chopin Variorum Edition*, autograph/copy Stichvorlage witness (A&C), Op.25 No.12: p.39 measures 1–20, p.40 21–40, p.41 41–60, p.42 61–83. Catalogue: https://chopinonline.ac.uk/ocve/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ . **Directly checked catalogue listing; page images NOT visually inspected.** These page/measure ranges are catalogue metadata, not transcribed pitch facts.
- Chopin First Editions Online, Op.25 first-edition witness catalogue: p.48 measures 1–14, p.49 15–29, p.50 30–44, p.51 45–59, p.52 60–71, p.53 72–83. https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/81463b2d142d5d52c8dbca2bd48fde76/ . **Directly checked catalogue, not facsimile.**
- Secondary general account: https://en.wikipedia.org/wiki/%C3%89tude_Op._25%2C_No._12_%28Chopin%29 describes C-minor work with rising/falling arpeggios and a C-major resolution. Treat this as a **secondary hypothesis pending direct score confirmation**, not as verified measure-specific harmonic analysis.
- Directly fetched previous repository research 073 and original Python generator `research/chopin/code/chopin_op10_2_generativestudy.py`. The exact guessed paths `research/chopin/研究07.md` and `研究08.md` returned 404; their actual locations and user-approved output examples were not directly recovered.

## Confirmed existing-code limitations
The fetched generator hardcodes 16 chromatic sixteenths per bar, cycles chord-tone pitches with `tones[j%3]`, assigns four quarter-note bass notes, and checks only `len(BARS)==8`. It has no structural bass/upper arpeggio coordination, event-level nonchord-tone audit, harmonic boundary handling, phrase-level two-bar development, or source provenance. These are facts about the **existing code**, not claims about Op.25 No.12.

## Original reusable composition model — HYPOTHESIS, not transcription
Represent each phrase as:
`Phrase2(harmonic_windows, bass_targets, structural_top_targets, registral_arc, density_arc, motive_invariant, cadence_goal, provenance)`.
Each event: `(onset:Fraction, duration:Fraction, voice, written_pitch, sounding_pitch, harmony_window_id, role, source_ref)`.
1. **Plan harmony and bass before figuration**. Select harmonic windows and voice-leading targets; preserve a structural top line independent of the ornamental attack count. A changing harmony may coexist with an invariant figuration grammar.
2. **Generate a multi-anchor arpeggio arc**, not a 3-note loop. For each two-bar unit, specify at least two turning points, an arrival pitch/register and a bass-directed harmonic destination. Populate the arc with spelled chord tones plus explicitly justified NCT candidates. Avoid forced chromatic scalar motion as a surrogate for harmony.
3. **Transform across two bars**: preserve one named invariant (e.g. attack-grid family or directional gesture), change two independent dimensions (register apex, bass goal, harmonic destination, rhythmic grouping, voice distribution, articulation density). Reprise may repeat but must be tagged.
4. **Exact time**: encode 16ths/32nds as rational values, with tuplets as exact fractions. Verify each independent voice's measure occupancy and chord simultaneity; never count a simultaneous chord as serial attacks. Distinguish a sounding sustained pitch from an attack.
5. **NCT audit**: at each onset and each harmonic boundary, use spelled harmony and same-voice neighbors. Passing candidate requires stepwise same-direction approach/exit; neighbor requires return; suspension requires preparation and tie/persistence across boundary plus resolution; appoggiatura requires accent and contextual resolution. Unknown harmony yields UNKNOWN, never guessed consonance.
6. **Critical tests**: reject all-16th modulo-three repetitions with no phrase goal, mismatched voice duration, leaps mislabeled as passing, fabricated source pitch labels, and a harmony transition that fails to re-evaluate held tones.

### Explicitly synthetic example
Two 4/4 bars: bar A bass C2→G2, harmony Cm→G7; bar B bass A♭2→G2, harmony A♭maj7→G7(b9). Upper figuration follows low→high→mid→high register targets with 16th subdivisions; in bar B, change peak, bass goal and chord spelling while retaining contour grammar. **This is an invented compositional test case, NOT a claim about Chopin's score or harmony.** The illustrative progression is not validated as aesthetically successful.

## Executed synthetic checks
Independent Python `fractions.Fraction` assertions executed on 2026-11-24: (1) sixteen 16ths fill one whole-note bar, (2) thirty-two 32nds fill one bar, (3) eight 16ths + four 8ths fill one bar, (4) stepwise 60→62→64 over chord {60,64} is a passing **candidate**, (5) 60→67→69 rejected as passing, (6) unknown harmony returns UNKNOWN. **6 assertions passed.** These are small synthetic unit checks, **not a run of the repository generator**, not a source parser, and not proof of musical quality.

## Quality gate and adversarial self-audit
**FAILED / PARTIAL.** No primary score image was directly read, so no note-by-note, exact harmonic, motivic, formal or voice-leading claims about the actual piece are made. No source-image comparison, no complete measure-by-measure analysis, no actual generator patch, no integration/regression run, no direct crosscheck with user-approved outputs. Catalogue coverage through m.83 is metadata, not evidence that all measures were inspected. Synthetic tests do not validate Chopin style.

**Handoff:** Next Op.25 No.12 research **2/3** must prioritize first-edition facsimile visual inspection of a bounded passage, compare with another witness where possible, record only directly observed pitches/durations and build a parser-backed NCT/harmony test. After 3/3 close this piece regardless of remaining deficiencies and move to waltzes if Op.10 and Op.25 sequence is already closed. No fingering/practice research or user-facing media.
