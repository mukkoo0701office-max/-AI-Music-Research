# Chopin Research 123 — Waltz A-flat B.21 / WN28: source correction and event-grammar audit (2/3, PARTIAL)
Date: 2026-11-26 JST. Research purpose: composition algorithms, excluding fingering/practice.

## Count and selection
Previous B.21 study: research/chopin/2026-11-26_waltz-b21_wn28_source_meter_grammar_partial-study-122.md (1/3). This study is 2/3 by visible records; historical deleted-file history not exhaustively audited. Op.10 No.2, B.56 and B.44 already reached the three-study ceiling and must not be revisited. Study 3/3, if no further prior studies are found, is the last permitted B.21 study.

## Sources and provenance (accessed 2026-11-26)
1. Chopin National Edition, *Waltzes*, Series B, critical commentary, https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes-B_commentaries_poprawka2020.pdf . The commentary identifies the A-flat WN28 waltz as 3/8 and explicitly states that an erroneous 3/4 signature in a transmitted witness is corrected to 3/8. This is an editorial judgment based on primary witnesses, NOT direct independent autograph-note verification. Crucial: a generator must preserve `notated_meter` and `editorial_meter` separately; it must not silently normalize the original witness.
2. IMSLP B.21 work page https://imslp.org/wiki/Waltz_in_A-flat%2C_P1-13_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 catalogs a holograph manuscript (library of Stanisław Moniuszko Music Society, 12/Ch; uploaded 2025) and 1902 Breitkopf & Härtel first edition (plate Klav.Bibl. 23183 II). These are **identified primary-score artifacts**, but their individual notes were NOT inspected in this run. The manuscript listing explicitly warns of differences from other sources. Catalog dating (1827) and National Edition's 1829–30 chronology should remain source-attributed rather than conflated.
3. Earlier repository baselines: studies 07 and 08 for Op.10 No.2, study 122 for B.21, and `research/chopin/code/two_bar_event_validator_v1.py`. The latter defaults to a six-quarter two-bar span, merges simultaneous voices in its signature, and uses pitch contour to define transformed motifs. No runtime test was performed this run.

## Critical finding: meter is an editorial decision, not a harmless metadata field
A 3/4 witness notation cannot be used uncritically as evidence of six quarter-note beats over two bars when the National Edition corrects it to 3/8. The algorithm must record (a) raw witness meter, (b) edited meter, (c) editorial authority and (d) whether note values have been renotated, without automatically multiplying or halving event durations. A mismatch between written durations and meter should yield SOURCE_CONFLICT until resolved against score images. This corrects study 122's implicit assumption that every witness is straightforwardly 3/8.

## Implementable original generation rules (NOT claims about Chopin's notes)
Event schema: `{witness_id, editorial_layer, bar, voice_id, onset:Fraction, duration:Fraction, pitch_spelling, tie_id, harmony_id, structural_role, nct_role, confidence}`. Separate `sounding_pitch` from `pitch_spelling` to preserve chromatic function.
1. Meter-aware clock: `bar_length = numerator*4/denominator` quarter units. 3/8 => 3/2; 2 bars => 3. Each voice's union of note/rest intervals must cover each bar without gaps or overlaps. Simultaneous notes of a chord must share a distinct chord/event group, not be mistaken for sequential events.
2. Surface density: sixteenth = 1/4 quarter, thirty-second = 1/8 quarter. A 3/8 bar may have 6 sixteenths or 12 thirty-seconds; any mix must sum exactly to 3/2, including rests and tied continuations. Subdivision does not imply a Chopin-specific accent hierarchy.
3. Two-bar motif: first extract voice-specific structural anchors (metrical weight, harmony arrival, phrase goal). Define transformation classes EXACT, TRANSPOSED (constant diatonic interval with spelling-aware chromatic check), SEQUENCE (repeated interval/rhythm relation plus independently planned harmonic displacement), ORNAMENTED_RETURN (anchor conservation plus inserted/deleted subordinate events), and UNCLASSIFIED. Similar up/down contour alone is insufficient. Compare two distinct windows, not arbitrary flattened simultaneous notes. Require at least two meaningful anchors; never infer sequence from 3-note cell repetition.
4. Non-chord tone audit: annotate harmony per event intersection. Passing = non-chord pitch with stepwise approach/exit in same direction; neighbor = stepwise departure and return; suspension = tied/prepared consonance held across harmony change with contextual resolution; appoggiatura = re-attacked dissonance and resolution. If either harmonic function, spelling, or voice continuity is unknown, return UNKNOWN. A tie by itself does not prove suspension. Re-evaluate at harmonic changes during held tones.
5. Counterpoint and bass: generate bass harmonic goals and cadence trajectories before accompaniment; inner voices must have independent identity. Flag direct/parallel perfect intervals and unprepared accented clashes for review, not unconditional rejection; style-sensitive exceptions need evidence.

## Adversarial test contract (specified; NOT executed)
T1: 3/8 two-bar single voice [12 sixteenths] accepted, 24 sixteenths rejected; mixed subdivisions with equal total accepted.
T2: Two simultaneous notes in different voices remain distinct; same-onset chord tones are not treated as temporal successors.
T3: Contour-preserving but nonuniform intervals => not TRANSPOSED or SEQUENCE.
T4: A genuine constant transposition => TRANSPOSED, not ornamented deformation.
T5: Tied unprepared dissonance => not automatically SUSPENSION.
T6: Mid-tie harmony change triggers another NCT evaluation.
T7: Unverified 3/4 witness plus 3/8 editorial reading => SOURCE_CONFLICT, not silent duration conversion.
T8: Missing score evidence => UNKNOWN for specific original bars/pitches.

## Quality gate / next action
**PARTIAL, NOT COMPLETE**. Primary score images and bar-by-bar pitches were not directly examined. No original-work chord, pitch, form boundary, or NCT labels are asserted. No code changed or tests executed; proposed rules remain unvalidated specifications. Next (last) B.21 study: directly inspect manuscript and 1902 print if accessible, verify the meter discrepancy in context, implement Fraction-based voice-aware validator, execute adversarial tests and record outcomes. Regardless of outcome, stop at cumulative 3/3 and move to another work.