# Chopin Research 087 — Waltz Op.34 No.3, F major: voice-boundary and edition-aware ornament audit (2/3)

Date: 2026-11-24 JST. **Cumulative work-specific research count: 2/3** (086 and this 087). Next and FINAL allowed run: 3/3, then move to next work regardless of incompleteness. Earlier 086 reported a provisional count; repository directory listing contains 086 and no other Op.34 No.3 file at time of this run. This is not an exhaustive historical commit audit.

**Quality gate: PARTIAL / NOT COMPLETE.** Primary printed score **located but not inspected at notehead level**. No claims of score-verified pitches or measure-by-measure harmonic analysis.

## Sources and witness discipline

1. Fryderyk Chopin Institute repository catalogue: https://repozytorium.nifc.pl/islandora/walc-op-34-nr-3-f-dur-0 . The catalogued Schlesinger witness, plate M.S. 2717.3, has engraved pp. 2–9; this particular copy is dated [1840–1842], and its catalogue reports pencil alterations to accidentals. **Catalogue metadata, not score-pixel verification.**
2. Early-print bibliographic concordance: https://www.chopin.pl/list.en.html . Paris Schlesinger M.S. 2717.3; Leipzig Breitkopf & Härtel 6034; London Wessel 2282. These identify distinct witnesses; they do not prove textual identity.
3. National Edition, Waltzes source/performance commentaries: https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes_commentaries.pdf . As recorded in study 086, editorial discussion flags ornament and accidental variants at bars 95/111 and later editorial intervention at 152 and 162–163. **These are reports of editors, not direct reading of original noteheads in this run.**
4. University of Chicago early-editions collection: https://www.lib.uchicago.edu/collex/collections/chopin-early-editions/ . Explains the importance of parallel-country early editions; not a direct score analysis.
5. A public-domain Op.34 scan is hosted at https://commons.wikimedia.org/wiki/File:Waltzes,_Op.34_(IA_imslp-op34-chopin-frdric).pdf . Its catalogue describes an 18-page scan. **The file was located, not visually verified as an original first impression; no page/bar pitches extracted.** The page's broad 1835 metadata must not be taken as the publication date of No.3.

## Prior code and research reviewed

Read research/chopin/2026-11-21_op10-no2_algorithm-study-07.md and -08.md; also directly read code/chopin_op10_2_generativestudy.py and code/chromatic_engine_v2.py. The first generates 4/4 straight 16ths with uniform direction and 4 quarter-note harmony/bass events; the second repeats four 3-note neighbor cells and checks only the target's pitch class against a supplied tone set. Neither models the full chromatic melody against *time-varying* harmony, multi-voice sounding durations, true two-bar transformation, or source-specific ornament variants. These are cross-work engineering defects, **not evidence that Op.34 No.3 uses any specific chromatic figure**.

## Reusable algorithm — independent compositional proposal, NOT transcription

**Data contract**: Event {voice, notated_onset: Fraction, duration: Fraction, pitch_spelling, midi, attack, tie_from_previous, tie_to_next, ornament_id, witness_id, evidence_tier}; HarmonySpan {start, end, spelled_tones, function, tonal_region, source_or_hypothesis}; Motive {contour, rhythm, anchor_targets, cadence_goal, bass_goal, density_curve, register_curve}.

1. **Separate clocks**: generate melody, accompaniment, bass and independent sustained inner lines on their own [0,3/4) bar timelines. Simultaneous events across voices do not add durations. For each voice, validate occupancy and explicitly represent rests; overlapping events *within* one monophonic voice require a chord or separate voice label.
2. **Harmony-boundary audit**: split each note's sounding interval at every harmony-span boundary. Evaluate (a) attack pitch and metric accent, (b) sounding dissonance after a chord change, (c) preparation and actual continuity, (d) resolution direction/time. A nonchord note is not automatically erroneous: passing and neighbor require contextual neighbors; a suspension requires a prepared pitch actually carried across the boundary, then resolved; an appoggiatura may be accented and unprepared, but its dissonance/resolution must be explicitly justified. Ambiguous cases remain UNKNOWN rather than forcibly relabeled.
3. **Witness-aware ornaments**: preserve notation separately from performance expansion. OrnamentRecord {source_witness, measure, kind, written_auxiliaries, onset_policy, resolution, local_accidentals, editorial_confidence}. Similar motives in different harmonic contexts are **not** automatically forced to have identical trill endings. Bars 95/111 are an *editorially reported* candidate for a targeted witness comparison, not a verified transcription here.
4. **Two-bar variation grammar**: derive bar pair B from pair A by constrained transformations of contour, metric placement, harmonic destination, bass trajectory, or register. Preserve at least one motive identity invariant (e.g., ordered accented contour), but require at least one declared phrase-level change; literal reprise is an explicit exception. Merely changing chromatic neighbor notes while repeating a 3-note cell is insufficient.
5. **High-density extension**: subdivisions of 1/16 and 1/32 use exact rational onset/duration. Preserve harmonic anchor notes, voice identities, and ornament resolution; density is a consequence of phrase trajectory rather than the objective.

## Tests actually executed (isolated synthetic Python, NOT production integration)

Ran Python Fraction-based synthetic assertions on 2026-11-24: **PASS 5 checks**: (1) concurrent bass 3/4, chord voice 3/4 and 12 sixteenths 3/4 each; (2) a stepwise returning nonchord note labeled neighbor; (3) a stepwise traversing nonchord note labeled passing_candidate; (4) tied dissonance with stepwise exit labeled suspension_candidate; (5) unsupported dissonance labeled unresolved. The fixture used arbitrary original pitches and is **not derived from Chopin's score**. These checks test only a narrow classification prototype: the suspension fixture does not yet independently validate preparation consonance or chord-boundary continuity. No existing repository generator was modified or run.

## Critical self-audit and falsification criteria

- **FAIL primary-score visual gate**: no noteheads, exact rhythms, bar numbers or voice-leading have been directly transcribed from FE/GE. The first-edition bibliographic source is verified at catalogue level only.
- **FAIL real-source harmony audit**: no harmonic reduction was tested against a bar-level score. Thus no claim of authentic Chopin harmonic grammar is warranted.
- **FAIL production integration**: current repository Python retains the three-note-cell and final-target-only weaknesses.
- **FAIL comprehensive NCT gate**: synthetic classifier labels are *candidates*; no full accent, harmonic change, preparation, release or contrapuntal dissonance policy is implemented.
- **FAIL user-preferred-output alignment**: user-rated compositions were not independently recovered; no claim of conformity to high-rated outcomes.
- No sound, MusicXML, or PDF output was produced.

## Mandatory handoff to final study (3/3 only)

Open and visually inspect legible FE score pages (ideally Schlesinger earliest impression), recording witness/printed page/bar/precise noteheads and durations for two contrasting two-bar phrases and editorially disputed 95/111 if accessible; compare GE where possible. Implement at least one executable test for note continuity across a chord boundary and another for actual two-bar transformation, then record source-linked pass/fail. If inaccessible, preserve the unresolved items and **move to the next work after study 3/3 without a fourth Op.34 No.3 run**.
