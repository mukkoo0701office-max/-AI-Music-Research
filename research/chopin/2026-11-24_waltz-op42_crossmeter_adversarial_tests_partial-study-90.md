# Chopin Research 090 — Waltz Op.42: cross-meter adversarial tests (2/3)

Date: 2026-11-24 JST. **Cumulative Op.42 count: 2/3**. Prior research 089 (1/3) was read. This is a **PARTIAL / NOT SCORE-VERIFIED** study, not a completed Chopin analysis.

## Source ledger (explicit confidence)
- IMSLP score catalogue: https://imslp.org/wiki/Waltz_in_A-flat_major%2C_Op.42_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 identifies German first edition #129433 (Breitkopf & Härtel, plate 6419, 1840, 10 pages), French first edition #399488 (Pacini, plate 3708, 12 pages), and English first edition #690968 (Wessel, plate 3559). **Catalogue metadata checked, not music notes.**
- Chopin Online critical first-edition catalogue: https://chopinonline.ac.uk/aco/catalogue/waltz-opus-42/ identifies Chopin-corrected French proof 42–0–P and German first edition 42–1–B&H derived from it; separate French first edition 42–1–P. **Source genealogy checked; no specific pitch variant claimed.**
- Direct attempt to open IMSLP German first-edition scan through the score link returned a bot-verification page. **Primary score images not inspected.** Therefore no claim about exact bars, melody accents, harmony, or engraving variants.
- Prior study: research/chopin/2026-11-24_waltz-op42_source_stemma_crossmeter_audit_partial-study-89.md.
- Existing research 07/08 and code/chopin_op10_2_generativestudy.py, code/chromatic_engine_v2.py were read directly. v2 repeats a three-note cell and tests only a terminal pitch class, not every event's dissonance; this is an implementation finding, not a claim about Op.42.

## Original reusable composition specification (NOT transcription)
### Two competing accent grammars
Model notated meter as quarter-beat rational clock; accompaniment accents at global times 0,3,6,... and melody accents with period 2 quarters at 0,2,4,6,... . The relative alignment traverses all three quarter positions within two bars (6 quarters); this is cross-bar 2-quarter periodicity, not an assertion that Chopin's Op.42 does so in any specific measure. Intra-bar eighth-note 2+2+2 grouping instead has attacks at offsets 0,1,2 quarters in each bar, and should never be conflated with a 2-quarter cross-bar period. A generator chooses an explicit accent-mode enum and resets phase only at declared formal boundaries.

### Multi-voice harmonic audit
Represent each note as (voice, rational onset, rational end, spelled pitch, tie status), each harmony as a half-open interval. Split sustained notes at every harmonic boundary before evaluating consonance. Passing and neighbor labels require melodic context; suspension requires preparation, held dissonance and stepwise resolution; an unprepared accented appoggiatura is distinct. Unknown labels remain unresolved, not silently converted to consonance. Store rhythmic accents separately from harmonic status. Check each independent voice's timeline for coverage, ties, rests, and overlap rules.

### Phrase development and provenance
Two-bar object stores contour, cadence goal, bass function, harmonic rhythm, accent phase, texture density. Reprise may preserve all fields if explicitly marked; otherwise require at least one preserved identity feature and one structural change (bass, cadence, accent mode, or harmonic rhythm). Reject changes confined to an arbitrary three-note cell as evidence of meaningful development. Store source readings with edition/impression identifiers and image anchors; never collapse differences into a synthetic 'original'.

## Actually executed internal Python checks (synthetic fixtures, not Chopin-derived)
Used Python fractions.Fraction, with seven assert checks in a single execution:
1. Two-quarter accent sequence over 6 quarter beats equals [0,2,4].
2. Its 3/4 bar-position sequence equals [0,2,1].
3. One-quarter spacing over a single 3/4 bar equals [0,1,2] (distinct from cross-bar periodicity).
4. A sustained event [1,3) split at harmonic boundary 2 becomes [1,2), [2,3).
5. Suspension fixture with preparation, hold, step resolution passes.
6. Unprepared suspension fixture fails.
7. Different French/German hypothetical readings preserve two separate witness records; plus motif comparison asserts identical non-reprise fails and bass-changed variant passes (two extra assertions).
**Execution result: PASS.** These fixtures test only simplified invariants; they do not validate the actual work, full voice coverage, enharmonic spelling, or the existing GitHub generator. No repository code was modified.

## Critical audit and next handoff
**Unverified:** whether Op.42's melodic cross-meter is cross-bar or local hemiola, exact edition note variants, actual harmonic/formal segmentation, note-by-note dissonance audit, and integration with existing generator. The inability to inspect the first-edition scan is a primary-evidence quality gate failure; do not call this a completed study. Next and **final permitted** Op.42 study (3/3): seek accessible original score scans, anchor any assertions to witness/page/bar, attempt real event-level audits, and document unresolved issues. After 3/3 move to the next unstudied work regardless of completeness. No music/audio/PDF deliverables.
