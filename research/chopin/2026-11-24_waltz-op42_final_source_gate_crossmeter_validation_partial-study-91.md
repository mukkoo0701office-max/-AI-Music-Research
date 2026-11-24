# Chopin Research 091 — Waltz Op.42, final permitted study (3/3)

Date: 2026-11-24 JST. **Cumulative research count for Op.42: 3/3. No fourth Op.42 run permitted.** Previous records 089 and 090 read directly. **Status: PARTIAL, PRIMARY SCORE NOT NOTE-VERIFIED.**

## Evidence ledger / source criticism
1. Chopin Online, Annotated Catalogue of First Editions, https://chopinonline.ac.uk/aco/catalogue/waltz-opus-42/ (accessed 2026-11-24): 42–0–P is Chopin-corrected French proof sent to Breitkopf & Härtel; 42–1–B&H is derived from that proof; 42–1–P is the French first edition. Several subsequent impressions/reprints are distinguished. These are verified *catalogue relationships*, not notes or rhythms.
2. The catalogue's 42–1–B&H entry https://chopinonline.ac.uk/aco/catalogue/waltz-opus-42/421-bh/ offers links to CFEO/OCVE image viewers. The CFEO link opened a dynamic browse page, not a score image directly usable for note-level verification. **No measure-specific musical assertion is licensed.**
3. University of Chicago early-edition description https://chopin.lib.uchicago.edu/chopin-catalog/descriptions/42.pdf returned a JavaScript bot-check on this run; no new verification from its pages.
4. Prior research: 089 https://github.com/mukkoo0701office-max/-AI-Music-Research/blob/main/research/chopin/2026-11-24_waltz-op42_source_stemma_crossmeter_audit_partial-study-89.md and 090 https://github.com/mukkoo0701office-max/-AI-Music-Research/blob/main/research/chopin/2026-11-24_waltz-op42_crossmeter_adversarial_tests_partial-study-90.md. Do not repeat their unverified claims as facts.

## Existing generator inspection and reusable defects
Read `research/chopin/code/chromatic_engine_v2.py` and `research/chopin/2026-11-21_op10-no2_algorithm-study-08.md`. `make_line` repeats a 3-note anchor cell four times and checks only the final pitch class against `b.tones`; `analyze` verifies note counts, summed duration and melodic leap <=3 semitones but neither intermediate event harmony nor preparation/resolution nor two-bar formal development. This is verified code behavior, **not Op.42 evidence**. Avoid implying existing code has been patched.

## Original compositional grammar (not Chopin transcription)
- **Clock:** `Fraction` quarters, explicit 3/4 bar spans; accompaniment bar phase `t mod 3`. Separate optional melody accent cycle `t mod 2`, whose phases in consecutive 3/4 bars are [0,2,1] over 6 quarters. Do not equate this with intra-bar 2+2+2 eighth-note subdivisions or assert its exact occurrence in Op.42 without a witness image.
- **Harmony:** independent half-open harmonic intervals. Split every sounding note at each chord boundary and test each segment; classify passing/neighbor by preceding and following pitch, metrical status and stepwise motion; suspension requires preparation and held dissonance followed by step resolution; accented unprepared dissonance may be an appoggiatura, not a suspension. Ambiguous spelling or context -> UNKNOWN, never silently accepted.
- **Two-bar object:** (melodic contour, rhythm/accent phase, bass function, harmonic goal, cadence type, density, register). A nonliteral development must retain identifiable material AND alter at least one phrase-level dimension; changed 3-note cells alone are insufficient. For literal reprise, mark `reprise=True`. Reject phase reset at arbitrary barlines; allow declared formal reset.
- **Witness model:** (source ID, impression, page/staff/bar/beat, spelled note, duration, tie, certainty, image anchor). Keep contradictory witnesses separate. Never use later corrected impression as automatic proxy for 1840 first impression.
- **Algorithmic gate:** event-level time coverage per voice, tied continuation, chord-boundary splitting, classified dissonance, independent voice overlaps, phrase-level transformations, provenance completeness. A passing synthetic test does NOT certify Chopin-like results.

## Tests actually executed, 2026-11-24
Independent Python `fractions.Fraction` assertions (synthetic, not score-derived):
1. 2-quarter accent times in 6-quarter window = [0,2,4].
2. 3/4 bar positions of these accents = [0,2,1].
3. Note [1,3) split by harmony boundary at 2 -> [1,2),[2,3).
4. Prepared held dissonance with step resolution accepted by simplified suspension predicate.
5. Unprepared held dissonance rejected by that predicate.
6. Identical non-reprise two-bar object rejected by development predicate.
7. Bass-function change with preserved contour accepted.
**Result: PASS, 7 assertions.** Tests are simplified invariants only: no actual Op.42 events, full chord spelling, real contrapuntal context, integration test or source-derived fixture. Existing generator remains unchanged.

## Critical failure and mandatory handoff
**Unverified:** actual Op.42 bar/beat-level duple accent behavior; pitch, rhythm, harmony, bass, form, ornament and edition variants; full-score polyphony; true quality of generated music. Source-image access remained inadequate, so no score-derived algorithm is claimed validated. A next-work study may reuse the generic architecture, but **must not run Op.42 again**. Continue to the next eligible unstudied waltz after checking repository counts; retain this record as a closed partial study, not as a completed analysis. No practice/technique study and no MusicXML/MP3/PDF produced.
