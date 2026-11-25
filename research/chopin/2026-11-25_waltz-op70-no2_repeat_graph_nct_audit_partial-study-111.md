# Chopin Research 111 — Waltz Op.70 No.2, study 2/3 (PARTIAL)
Date: 2026-11-25 JST. Research 110 explicitly records study 1/3. GitHub commit search for "op70" returned 110 and Op.70 No.1 studies, but is not an exhaustive repository history audit; cumulative count **provisional 2/3**. Never undertake a fourth study.

## Source provenance / what was actually checked
1. NIFC museum catalogue, manuscript MC/319, https://kolekcja.nifc.pl/object-mc-319 (accessed 2026-11-25). The catalogue directly states an autograph presentation copy dated **10 December 1842**, meter **3/4**, A section marked **1. Volta / 2 Volta**, and **no B-section repeat** (unlike editions). This is *curatorial textual description*, not independent visual note-by-note score collation. It reports corrections at bars **16, 43, 56, 72**; these are **catalogue assertions** only, not personally verified pitches or rhythmic values.
2. OCVE browse page https://chopinonline.ac.uk/ocve/browse/acview/12fd2b9b9c0b2cc3619df0bd25922231/ was accessible, but its dynamic listing did not expose usable score images. No claim of note-level inspection.
3. Prior local repo note: research/chopin/2026-11-25_waltz-op70-no2_witness_form_grammar_partial-study-110.md. Its witness-aware model is retained, not repeated as a new discovery.
4. Existing Python: research/chopin/code/waltz_event_audit_v2.py read directly. It has rational timing, voice coverage, tie checks, harmony coverage, and a coarse two-bar transform predicate. This run did not execute or modify it.
5. Research07/08 and high-rated exemplar artefacts were **not located** using repository search; compatibility remains unverified.

## Novel finding: repeat traversal is not composition structure
NIFC's MC/319 catalogue identifies two alternate A endings and an unrepeated B. A source-faithful model therefore needs a **witness-scoped control-flow graph**, rather than treating repeats as a flat sequence of generated measures. A generic *proposed* graph (not a transcription of exact measure boundaries) is:
A_body -> A_ending_1 -> A_body -> A_ending_2 -> B_body -> exit.
The two endings are distinct events with their own witness anchors. B must not be repeated when realizing witness MC/319. An edition that repeats B needs a separate graph with independent documentary evidence; no universal repeat topology can be inferred from one source. **Do not confuse traversed length with the number of unique composed bars**. Catalogue references to bar 72 do not establish how any modern edition numbers its bars.

## Implementable rules (original algorithms, NOT facts about the notes of Chopin)
- `WitnessGraph(witness_id, nodes, directed_edges, repeat_limits, endings)`: validate all targets, bounded traversal, exclusive first/second endings, reachability of exit; refuse unsupported edition merging.
- `Event(witness_id, structural_bar_id, traversal_instance, voice, onset: Fraction, duration: Fraction, pitch_spelling, attack, tie)`: keep source identity and playback occurrence separate. For a 3/4 bar in quarter-note units, enforce duration sum 3 in each voice, explicit rests, no gaps/overlap, and legal 1/4 (sixteenth) and 1/8 (thirty-second) fractions. Ornament allocations must conserve elapsed time unless explicitly grace/non-metrical.
- `HarmonySpan(start,end,spelled_chord,local_key,source_status)`: complete coverage and no overlap. A note outside pitch-class membership is a **candidate**, never an automatically proven appoggiatura, suspension, neighbor or passing tone.
- NCT classification requires prior/current/next attacks in same voice, preparation and resolution, accent position, spelling, and harmony on both sides of any chord change. Suspension: prepared pitch tied/held into dissonance and resolved (usually stepwise); appoggiatura: accented dissonance approached without required preparation and resolved; passing: connects two structural tones stepwise; neighbor: leaves and returns to same structural tone. Mark AMBIGUOUS when evidence does not discriminate; do not treat every sustained tone crossing a harmony change as suspension.
- Two-bar transformation: compare actual normalized note-event sequences (durations, contour, attack placement, bass movement, harmonic trajectory), not only five metadata fields. Require an invariant motive signature and at least one perceptually meaningful change; separately allow verbatim reprise. Reject arbitrary repeated 3-note cells as sufficient phrase design.

## Audit of existing validator (static inspection, NOT executed)
- `audit` checks exact harmony continuity and voice event tiling, but its `segments` only reports membership; it does **not** identify or verify NCT type.
- `two_bar_transform` compares tuple metadata; two audibly identical realizations with different labels can pass, and meaningful transformations of realized notes can fail.
- `Event.pitch` is an integer MIDI-like value, losing enharmonic spelling needed for voice-leading/NCT classification.
- `Event.tie_prev` checks pitch equality with preceding event but does not enforce the previous event's tie-out, and ties after a rest are rejected through pitch mismatch. Add explicit outgoing tie state and per-witness source bar IDs.
- No edition-specific repeat-graph traversal is implemented.
- Existing synthetic tests in that file are **not run in this study**; previously reported results cannot be presented as this run's results.

## Proposed regression tests (DESIGNED, NOT RUN)
1. A1->A2 endings: first traversal only ending 1, second only ending 2.
2. MC/319 B traversal exactly once; another edition's repeat must be separately sourced.
3. Reject unbounded repeat cycle and unreachable exit.
4. Distinguish structural bar count from played bar count.
5. Reject a sixteenth+thirty-second pattern whose durations fail to sum to three quarter beats.
6. Reject a tie with missing previous tie-out.
7. Retain enharmonic spelling, test identical pitch classes with different diatonic motion.
8. Passing-note candidate with missing next attack -> AMBIGUOUS, not PASSING.
9. A tied chord-change dissonance without step resolution -> not automatically SUSPENSION.
10. Metadata-only two-bar edit with identical event stream -> reject transformation.
11. Preserve witness IDs through realization and reject cross-witness accidental merges.
12. Mark all claimed source notes without page/staff/bar image anchors UNVERIFIED.

## Critical self-assessment and handoff
This is an **incremental, catalogue-grounded algorithmic audit**, not a completed Chopin score analysis. No original score image or pitches were directly inspected; no Python was executed, no integration performed, and research07/08 and preferred examples remain unread. Next and **last** study (3/3) should prioritize visual primary-score collation and executable graph/NCT tests, record outstanding failures, then move on regardless of completeness. No fingering or performance-practice research.
