# Chopin Research 070 — Op.25 No.10, final study 3/3: evidence gate and handoff

Date: 2026-11-23. **PARTIAL / SOURCE-NOTE VALIDATION FAILED.** Cumulative study count **3/3**: 068 (1/3), 069 (2/3), 070 (3/3). **CLOSED: DO NOT REVISIT Op.25 No.10 for a fourth research run. Next target Op.25 No.11 (1/3), subject to repository recount.**

## Direct evidence actually inspected
- Fetched full GitHub research 068 and 069 this run. They establish the two prior counts and disclose the lack of score-note inspection and integration. Their original octave-event and boundary models are **engineering hypotheses**, not transcriptions.
- Opened Online Chopin Variorum Edition catalogue at https://chopinonline.ac.uk/ocve/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ on 2026-11-23. Accessible HTML contained source-type legend and work filters but **no readable notation**. The manuscript page/bar locator (pp. 28–32, mm. 1–119) is inherited from study 068, **not independently reverified against score images here**.
- GitHub repository code searches for strings `研究07`, `研究08`, and `chromatic_engine_v4` returned no indexed hits; this is **not proof those files are absent**. Study 069 reports its direct inspection of `research/chopin/code/chromatic_engine_v4.py`, but this run did not independently fetch that source. User-approved examples were not directly compared.
- **No source-verified notes, chords, harmonic progressions, NCT labels, formal boundaries, or pitch spellings** can be reported for the étude.

## Non-duplicative critical audit: evidence boundary as a software requirement
The central unresolved problem is not another possible octave-pattern generator, but **provenance leakage**: a synthetic passing test can be mistakenly promoted into a statement about Chopin. Introduce these typed statuses for every research claim and fixture:
- `SOURCE_VERIFIED`: witness identifier + edition/manuscript + page + measure + readable notation excerpt or inspectable image pointer + independent transcription check.
- `SECONDARY_CLAIM`: attributed secondary reference; never a substitute for score.
- `ORIGINAL_HYPOTHESIS`: independent compositional model, without attribution to Chopin.
- `SYNTHETIC_TESTED`: model behavior demonstrated on invented fixtures only.
- `UNVERIFIED`: no direct evidence; excluded from source-derived training examples.

### Executable design contract (proposed; NOT implemented or executed)
1. Store `Claim(id, status, source_id?, page?, measure?, pitch_spelling?, confidence?, verification_log)`. A source-derived generation rule requires at least one `SOURCE_VERIFIED` claim. Missing witness/page/measure means the claim cannot receive that status.
2. `OctaveAttack(onset, release, lower, upper, voice_role)` is one simultaneous event only when upper–lower = 12 semitones, both sounding intervals coincide, and notation identifies octave doubling. Otherwise mark `REVIEW`; do not collapse independent counterpoint.
3. `HarmonicWindow(start, end, spelled_chord, bass, provenance)`: inspect every attack and all sounding events at each boundary using half-open intervals. Unknown chord or spelling yields `UNKNOWN`, never automatic consonance.
4. `NCTAssessment(note, preceding, following, harmony_before, harmony_after, metric_accent, preparation, resolution)`: passing and neighbor require directional/contextual voice evidence; suspension requires preparation, held dissonance and resolution; appoggiatura requires accent and resolution. Ambiguity yields `REVIEW`, not a fabricated label.
5. `PhraseUnit(role, motive_invariants, contour_goal, bass_arrival, harmony_path, rhythmic_grouping, texture)`: in a two-bar DEVELOPMENT unit, preserve a declared invariant and alter at least two independent structural dimensions. A reprise may repeat when explicitly designated. This is a **user-facing algorithm proposal, not an observation of the étude**.
6. Use rational `Fraction` onset/duration for 16ths, 32nds, tuplets, rests and ties; enforce complete voice-time coverage, measure sums, and no overlaps unless explicitly polyphonic.

## Mandatory negative tests before any future general-purpose engine claims
- Reject octave represented by two sequential attacks as a simultaneous octave.
- Do not flag chordal octave doubling as independent parallel octaves.
- Reassess held pitches on harmonic change without new attack; exclude pitches released at boundary.
- Reject suspension label if preparation or stepwise resolution is absent.
- Fail 32nd/tuplet overflow or uncovered voice time.
- Fail two-bar DEVELOPMENT when only literal transposition changes.
- Reject `SOURCE_VERIFIED` status without witness/page/measure and directly inspectable notation.
- Reject training extraction when all supporting claims are `ORIGINAL_HYPOTHESIS` or `SYNTHETIC_TESTED`.

**Execution status: none of the tests above were run in this study.** Prior studies 068/069 report 4 and 6 synthetic assertions respectively; these are inherited reports, not rerun or integrated evidence.

## Critical self-audit and compulsory handoff
**QUALITY GATE NOT PASSED.** No directly readable primary-score notation; no actual Op.25 No.10 pitch-level harmonic, contrapuntal or formal analysis; no direct studies 07/08 or approved-example reread; no Python production patch or integrated tests. Do not label this a completed Chopin analysis. It is a bounded research closure and provenance specification.

**Research count exhausted at 3/3.** Carry the generic provenance/NCT/phrase contracts forward to **Op.25 No.11** without performing a fourth No.10 study. Prioritize direct score images and actual note-level verification before claiming stylistic findings. No fingering/performance study or user-facing audio/MusicXML/PDF output.
