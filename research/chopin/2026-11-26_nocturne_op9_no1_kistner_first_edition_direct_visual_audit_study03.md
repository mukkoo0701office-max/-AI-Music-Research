# Chopin Nocturne Op.9 No.1 — Kistner first-edition direct visual audit (study 3/3; FINAL HANDOFF)
Date: 2026-11-26. **PARTIAL: primary image inspected; pitch-by-pitch collation incomplete.**

## Study count and decision
The current repository's immediately preceding records are study01 and study02, both dated 2026-11-26. This is visible study **3/3**; full deleted-commit history was not independently reconstructed. **Do not study Op.9 No.1 again**, even if open questions remain. Move to the next eligible work after auditing its prior count. Op.10 No.2 and No.3 are already excluded by earlier history audits.

## Primary witness DIRECTLY INSPECTED
Kistner first edition of *Nocturnes*, Op.9, **PDF page index 1 / printed page 2**, image viewed directly at https://upload.wikimedia.org/wikipedia/commons/6/6b/Chopin_Nocturnes_Op_9_Kistner_First_Edition_1832.pdf (Wikimedia Commons, University of Chicago scan, 13 pages). Metadata identifies Leipzig, Fr. Kistner, 1832 **or** 1833; the date conflict remains unresolved, and must not be silently normalized. The plate number **995** is visibly printed at the foot of the page.

### High-confidence page-specific visual observations
- Heading **NOCTURNE**, **1er**, **LARGHETTO**, metronome indication (quarter = 116 appears in the print), 6/4 meter and six-flat signature. Treat metronome typography as visually read, not independently corroborated.
- The opening melodic phrase begins with a **beamed six-note figure** above an initially silent bass staff. The next system shows the melody over continuous bass arpeggiation.
- The second notated melodic measure contains an **11** tuplet numeral; the following system begins a **22** tuplet numeral. The source image itself does **not** explicitly print modern-style 11:12 or 22:24 ratios. Those expansions are derived interpretations requiring comparison of total occupied spans and reference note value.
- The left-hand part prominently uses **six-note beamed groups** and changing pitch contours, rather than a literal identical pitch cell repeated each half-bar. Some opening groups have pedal markings and release signs.
- Long upper-voice notes, articulated repetitions, ornaments and unequal-density melodic gestures coexist with a relatively continuous lower texture. The page later marks **smorz.**, **appassionato**, **sotto voce**, and expressive dynamic shaping.
- The image contains accidentals and complex beaming, but **no complete note-by-note transcription or exact pitch/harmony analysis was performed**. Avoid attributing specific NCT classifications, harmonic functions, or variants to Chopin from this inspection.

## Generative principles — ORIGINAL MODEL, NOT VERIFIED CHOPIN NOTES
1. **Separate structural melody anchors from surface ornament**: phrase anchor (onset, duration, spelled pitch, harmonic role, confidence), then optional local ornament graph; vary density and register across phrases, and require a genuine 2-bar transformation rather than three-note-cell looping.
2. **Harmonic and bass planning precedes arpeggiation**: define harmonic spans and bass arrival targets; independently generate accompaniment contours with variable inversions, held common tones and voice-leading; audit changes in contour rather than copy a six-note cell.
3. **Tuplet rational-time contract**: explicit tuplets record count n, reference-count m, base unit, occupied span, and group ID. For n equal notes occupying m base units, each duration = m*base/n. Never infer base or total span from numeral alone.
4. **NCT audit with abstention**: classify passing, neighbor, suspension, appoggiatura only after verifying harmonic membership, approach, departure, accent, and (for suspension) preparation across a harmony change; otherwise UNVERIFIED. Chromatic exceptions need explicit evidence.
5. **Two-bar motif invariants**: compare structural anchor contour and harmonic destination independently of inserted/deleted ornaments. Require at least one documented change (register, rhythmic scaling, harmony, accent placement or ornament density); exact copies of 3-note fillers do not count as development.
6. **Counterpoint checks**: compare sustained melodic anchor against each inner/bass voice on harmonic boundaries, distinguish structural fifth/octave parallels from ornamental simultaneities, and flag unresolved dissonances rather than declaring a blanket violation.

## Executed internal synthetic checks
Ran Python 3 locally on 2026-11-26 using fractions.Fraction. **PASS: five assertions**:
- 11 equal events in 12 eighth-note reference units sum to 6 quarter units.
- 22 equal events in 24 sixteenth-note reference units sum to 6 quarter units.
- Stepwise passing-tone positive fixture passes (C-D-E over C/E anchors).
- Leaping 'passing' negative fixture is rejected.
- Returning neighbor-like C-D-C negative fixture is rejected as passing.
These are **synthetic contract tests only**, not tests against Op.9 No.1's notated tuplet time window. The preceding v2 validator was read directly; its existing limitations remain (no spelled pitch, NCT engine, tuplet group identity, or structural-anchor comparison). No repository code was modified this run.

## Source/quality limitations and handoff
The first-edition PDF **was directly viewed**, materially improving on studies 1–2. However, French Schlesinger first-edition page was not directly compared; no note-by-note alignment, exact tuplets' base-value confirmation, harmony map, or NCT score annotation was completed. Master protocol and user-rated exemplars were not re-fetched; aesthetic compliance remains unverified. Thus **partial, not completed research**. The generative rules are hypotheses and implementation contracts, not historical claims about precise notes. Preserve the unresolved items for the cross-work algorithm backlog, **not as authorization for a fourth Op.9 No.1 study**.

Sources:
- Kistner scan: https://commons.wikimedia.org/wiki/File:Chopin_Nocturnes_Op_9_Kistner_First_Edition_1832.pdf
- Earlier local research: research/chopin/2026-11-26_nocturne_op9_no1_opening_score_evidence_grammar_study01.md and research/chopin/2026-11-26_nocturne_op9_no1_validator_boundary_source_access_study02.md
- Existing validator: research/chopin/code/two_bar_event_validator_v2.py
