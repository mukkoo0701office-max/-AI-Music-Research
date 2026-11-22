# Chopin Research 045 — Étude Op.25 No.2 (2/3): source status and rational-time regression
Date: 2026-11-22. **Cumulative study count 2/3** (044 plus this run; repository commit search returned no additional Op.25 No.2 hits, so undiscoverable runs remain a caveat). **PARTIAL: primary-score-image gate NOT PASSED.**

## Evidence boundaries
- Directly read [study 044](2026-11-22_op25-no2_metric_normalization_partial-study-44.md), which records that studies 07/08 and chromatic_engine_v4.py were read by earlier work, **not independently re-opened in this run**.
- [Chopin Online OCVE Op.25 sources](https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/) explicitly indexes the Op.25 No.2 engraving-model copy at pp.4–7 (bars 0–69), and subsequent German edition pp.7–10. This is a **source-page index, not visual inspection**. No bar-specific pitch, harmonic, articulation, or editorial difference is asserted.
- [University of Chicago first-edition catalogue](https://chopin.lib.uchicago.edu/chopin-catalog/descriptions/25.pdf) identifies 1837 Paris/Leipzig/London editions. [Source overview](https://fchopin.net/etude_source/) reports Teichmann 2/4 manuscript with halved note values and later 2/2; this is secondary reporting, not a manuscript inspection.
- Original compositional examples below are **synthetic**, not quotations from Chopin.

## Reusable algorithm: two simultaneous clocks
Use rational sounding time per measure. In a hypothetical full 2/2 bar, 12 RH eighth-triplet attacks at k/12 whole-note units and 6 LH quarter-triplet attacks at j/6 units satisfy LH(j)=RH(2j). Thus the common onset lattice is 12 subdivisions, and this texture alone is not an independent 3:2 phase conflict. Store **notation version** and tuplet ratios; the reported 2/4 autograph analogue is obtained by scaling the written duration and onset by 1/2, not by applying a blind transformation to modern notation.

Separate:
(1) form/harmonic target and phrase destination;
(2) independent bass anchors and melodic skeleton;
(3) surface clocks, accents, ornaments and register;
(4) contextual nonchord-tone audit with preparation/resolution and harmonic boundary;
(5) two-bar motif transformation, preserving one recognizable feature while changing contour, density or destination.
Never use repeated three-note cells alone as a sufficient phrase-development criterion.

## Executed isolated regression (Python 3, fractions.Fraction)
Five assertions executed and passed on 2026-11-22:
1. each of six LH onsets matches the even-indexed RH onset;
2. 12 × (1/8 × 2/3) = one whole note;
3. 6 × (1/4 × 2/3) = one whole note;
4. 12 × (1/16 × 2/3) = one half note;
5. halving RH k/12 onsets produces k/24.
These are **arithmetic tests only**, not score verification or integration tests.

## Proposed implementation contracts and exceptions
Event fields: source_version, voice_id, onset:Fraction, duration:Fraction, written_value, tuplet_ratio, pitch, tie_id, metric_strength, harmony_id, evidence_status. Reject unequal bar totals unless an explicit pickup, rest or crossing tie explains them. Do not force a fixed 12-grid when smaller subdivisions or ornaments occur. Detect notes sustained over a harmonic boundary and classify against both harmony windows. Nonchord-tone labels require own-voice context and can remain UNKNOWN. Two-bar transformation test must compare contour and rhythm, apex and bass destination, not just count attacks.

## Critical audit / next handoff
**Passed**: source index located; mathematically sound RH/LH alignment and edition scaling independently executed; prior research 044 compared.
**Unverified**: source image visually read; primary score transcription and original nonchord-tone labels; research07/08 and v4 reinspection this run; high-rated examples cross-check; integration/regression against existing engine. Therefore no claim of full-quality completed research. Next Op.25 No.2 study **3/3 only**, then proceed to Op.25 No.3 regardless of remaining gaps; preserve unresolved items without a fourth study.
