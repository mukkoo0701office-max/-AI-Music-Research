# Chopin Research 089 — Waltz Op.42 in A-flat major: source stemma and cross-meter design (1/3)

Date: 2026-11-24 JST. **Cumulative Op.42 research count: 1/3** (directory listing inspected; no earlier Op.42 research file in research/chopin). Previous Op.34 No.3 has reached 3/3; no fourth run. **Verdict: PARTIAL / NOT VERIFIED AT SCORE-NOTE LEVEL.**

## Evidence ledger and limits
1. **Primary-edition bibliography, verified directly (not score-note reading):** University of Chicago Chopin Early Editions, Op.42 catalogue https://chopin.lib.uchicago.edu/chopin-catalog/descriptions/42.pdf . French Pacini 3708, Leipzig Breitkopf & Härtel 6419, London Wessel 3559, all dated 1840 (catalogue pp.1ff). The Chicago record explicitly notes later Leipzig reissues with numerous corrections, chiefly accidentals (catalogue section 42-BH-4); do not collapse later corrected reprints into the 1840 first impression.
2. **Critical source genealogy:** Chopin Online Annotated Catalogue https://chopinonline.ac.uk/aco/catalogue/waltz-opus-42/ distinguishes a Chopin-corrected proof of the first French edition (42–0–P), first French edition (42–1–P), and German first edition derived from the proof (42–1–B&H). This makes a linear “French first → German copy” model invalid; source branches must be represented explicitly.
3. **Score-image candidates identified, not directly inspected this run:** IMSLP https://imslp.org/wiki/Waltz_in_A-flat_major%2C_Op.42_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 lists a German first-edition scan (ID 129433) and French first-edition scan (ID 399488). Neither score image has been opened and checked note-by-note in this run. Therefore NO bar-specific pitch, harmony, exact rhythmic transcription, or variant is asserted.
4. **Secondary hypothesis ONLY:** widely circulated descriptions suggest a duple-feeling melody against triple-meter waltz accompaniment. This is a testable analytical hypothesis, NOT established by score reading here. Do not assign exact accents or phrase/bar numbers until both editions are inspected.

## Prior work / code read
- research/chopin/2026-11-21_op10-no2_algorithm-study-07.md and -08.md;
- research/chopin/code/chopin_op10_2_generativestudy.py and chromatic_engine_v2.py;
- research/chopin/2026-11-24_waltz-op34-no3_final_score_visual_polyphony_rules_partial-study-88.md.
The v1 code uses uniform 16ths plus four quarter-note middle attacks; v2 repeats a three-note cell four times, only checks the final target pitch class, and lacks event-level nonchord-tone classification and a genuine two-bar development operator. These are repository-code observations, **not evidence about Op.42**.

## Reusable ORIGINAL algorithm proposal — NOT a transcription
### A. Edition-sensitive source model
Represent witnesses as separate immutable records (witness_id, impression_id, date, plate, parent/source relation, measure map, evidence image). Example graph: corrected French proof -> German first edition; French first edition separately linked to proof with a relation requiring source verification. Keep each note reading as (witness, page, staff, bar, beat, spelled pitch, duration, glyph, certainty). If two witnesses disagree, produce a VARIANT record, not a merged synthetic “Chopin original”. Later German accidental corrections must remain distinct from first-impression evidence.

### B. Two clocks: notated triple time versus perceived accent cycle
For an **original** 3/4 passage, use rational onset times (Fraction), with accompaniment grouping bass at 0 and chords at 1,2 quarter beats *as one optional texture*, not an immutable Chopin fact. Overlay a melody accent period of 2 quarter beats across bar boundaries, yielding a 6-quarter supercycle where melody accents and 3/4 bar accents realign. This is a compositional cross-meter hypothesis. Alternative: 2+2+2 eighth-note grouping within one bar; do NOT confuse the two phenomena. A generator must label whether it uses (i) cross-bar accent cycle, (ii) within-bar hemiola, or (iii) surface syncopation.

### C. Harmony and dissonance independent of accents
Store harmony spans independent of measure boundaries. At every melodic onset and every harmony change, split sustained note intervals and classify nonchord tones: passing, neighbor, accented appoggiatura, suspension (requires consonant preparation, held-through-boundary dissonance, and stepwise resolution), anticipation, pedal, or UNKNOWN. Reject only unlicensed/unresolved conflicts, not all accented dissonances. Preserve spelled intervals and voice identity. A rhythmically displaced accent must NOT automatically count as harmonic dissonance.

### D. Phrase-level development
Two-bar motif object = {accent profile, contour, bass trajectory, harmonic function, cadential destination, register, density}. Transformation must preserve one identity-bearing feature and change at least one large-scale feature; local three-note-cell substitution alone does not count. For the cross-bar 2-beat cycle, compare six-quarter windows to avoid false segmentation at barlines. Cadential resolution may intentionally reset the accent phase; require explicit phrase-boundary metadata.

### E. Tests to implement and run (NOT RUN in this study)
1. 3/4 voice completeness, exact Fraction clocks; rests and ties accounted separately.
2. A 2-quarter accent cycle in 3/4 realigns after two bars (LCM(2,3)=6 quarter beats); a 2-eighth-note grouping is NOT equivalent.
3. Sustained note crossing a chord change triggers a new harmonic audit segment.
4. Suspension without preparation fails; unprepared appoggiatura is not automatically rejected.
5. An identical two-bar motif with only one 3-note cell changed fails development gate unless designated literal reprise.
6. Source A/B accidental disagreement yields two variant records with witness provenance, never silent overwrite.
7. Positive and adversarial tests for simultaneous independent voice durations and ties.

## Critical self-audit / handoff
**Not achieved:** original score image inspection, verified note-level cross-meter analysis, original bar-by-bar harmony/form, code integration, execution of tests, and positive score-derived evidence of the proposed cross-meter mechanism. Source catalogue is primary-edition *bibliography*, not a primary score transcription. The code/test design above is an original proposal; no claim of empirical Chopin-style accuracy. No audio, MusicXML or PDF deliverable produced.

**Next Op.42 study (2/3):** inspect first French and German 1840 score images directly; record page and bar anchors for a limited passage, verify whether perceived duple accent is truly cross-bar or intra-bar, and run the above adversarial tests before claiming an algorithm is validated. At most one further Op.42 study after that; then advance regardless of completeness.
