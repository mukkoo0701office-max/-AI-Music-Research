# Chopin Research 112 — Waltz Op.70 No.2, final study 3/3 (PARTIAL)
Date: 2026-11-25 JST. Prior studies: 110 (1/3), 111 (2/3), both fetched and reviewed in this run. **Cumulative count 3/3 according to these records; global history enumeration not proven. HARD STOP: do not research Op.70 No.2 a fourth time.** Next target must be a different composition after checking history.

## Sources actually checked and provenance
- National Fryderyk Chopin Institute (NIFC) autograph catalogue MC/319, https://kolekcja.nifc.pl/object-mc-319 , consulted 2026-11-25. This is the **museum's transcription and scholarly catalogue**, not direct image-based inspection. Describes presentation autograph to Madame Oury, 10 December 1842, 3/4, A with first/second endings, B with no repeat, and erasures in bars 16,43,56,72. Do not infer pitches from catalogue.
- NIFC manuscript-copy catalogue D/107, https://kolekcja.nifc.pl/object-d-107 , consulted 2026-11-25. Describes A with two endings and B without repeat; specifically contrasts printed expanded AAB AB design. Copy's authorship attribution to Marcelina Czartoryska is uncertain. These are documentary descriptions, not independent pitch-level collation.
- MC/319 catalogue includes source-edition commentary distinguishing five autographs from Fontana-related editions and 1852 Kraków Wildt printing; therefore **1855 is not the sole first printing**. The catalogue quotes source-edition commentary questioning some Fontana-derived bass prolongations; that editorial criticism is NOT a direct primary-score verification.
- Repository files fetched: research/chopin/2026-11-25_waltz-op70-no2_witness_form_grammar_partial-study-110.md; research/chopin/2026-11-25_waltz-op70-no2_repeat_graph_nct_audit_partial-study-111.md; research/chopin/code/waltz_event_audit_v2.py. Research07/08 and user's positively evaluated works not located/read in this run.

## New finding: source identity, structural form, playback traversal are different axes
Catalogue testimony supports an A section with two alternate endings and B without a repeat in MC/319 and D/107; expanded published traversal must not be projected back onto those manuscripts. Even manuscript structural bar counts, edition counts, and performed bar counts are not interchangeable. The MC/319 catalogue reproduces differing counts in its bibliography (e.g. 72 and 124); this is **not** evidence that one should assign a definitive 72-bar structural length. Keep counts witness- and counting-convention-scoped.

## Original implementation specification (not a Chopin transcription)
Use `Witness{id, provenance, source_type, edition_date, confidence}`, `StructuralBar{id, witness_id, meter, score_anchor}`, `GraphEdge{from,to,condition,source_anchor}`, `RealizedBar{structural_id, visit_index}`. For manuscript-type repeat model, `A -> E1 -> A -> E2 -> B -> END` is an **abstract section-level control graph**, not a claim about exact bar boundaries. A1 and A2 ending exclusivity must be enforced by visit count. Graph traversal must have finite termination, all nodes resolved, and no unsupported cross-witness transitions. Do not flatten repeated A into new compositional material.

For each structural bar: preserve rational onsets and durations in quarter-note units; 3/4 totals 3 per voice including explicit rests; 16th = 1/4 and 32nd = 1/8. Tie validity requires both outgoing and incoming indicators, identical spelled pitch and continuity across a barline. Preserve attack vs sustain. Keep spelled pitch (step, alteration, octave), local key, harmonic membership, accent, and previous/next same-voice attack. Non-chord-note classifier returns `PASSING/NEIGHBOR/SUSPENSION/APPOGGIATURA/OTHER/AMBIGUOUS`; never classify from pitch class alone. Chord changes under held notes are candidates, not proof of suspension. Two-bar development comparison must operate on actual timed events: retain an identifiable contour/rhythm/accent motive invariant, change at least one audible dimension (not only labels), and verify bass/harmony trajectory and voice independence; explicit literal reprises are a separate category.

## Executed limited synthetic test (NOT source fidelity)
A standalone Python 3 section-level graph test was executed in this run. It asserts traversal `['A','E1','A','E2','B']`, B occurs once, and rejects a nonterminating B loop and dangling destination. **4 assertions passed**. This test is only a small proof of graph traversal logic; the snippet was not integrated into the repository's production generator or existing `waltz_event_audit_v2.py`. Existing v2 source was read statically but not executed here. No real score notes were tested.

## Regressions required for implementation (DESIGNED, NOT EXECUTED)
1. Reject a missing/extra ending or a third A visit; compare source-specific alternative graph.
2. Reject unbounded loops, unreachable exits and cross-witness edges.
3. Keep unique structural bars distinct from repeated performance instances.
4. Check 3/4 event tiling including sixteenth/thirty-second/rest and cross-bar ties with tie-out.
5. Require full spelled-note and adjacent harmonic context for NCT; mark underdetermined labels AMBIGUOUS.
6. Reject a metadata-only two-bar 'transformation' with unchanged realized events; accept separately declared literal reprise.
7. Require source page/system/bar anchors before attributing a specific pitch, rhythm or cadence to Chopin.

## Critical quality gate and handoff
**PARTIAL / NOT COMPLETE.** No direct inspection of primary manuscript score pixels or note-by-note comparison; no verified bar/pitch transcription; no modification/integration of the existing Python generator; no executed NCT or two-bar transformation regressions; Research07/08 and high-rated exemplars not reviewed. Accordingly, no claim of source-faithful musical generation or high-quality completed analysis. Research count 3/3 is exhausted, so these deficiencies must be recorded as transferable backlog rather than used to justify a fourth study. No fingering or practice research; no user-facing audio/XML/PDF.
