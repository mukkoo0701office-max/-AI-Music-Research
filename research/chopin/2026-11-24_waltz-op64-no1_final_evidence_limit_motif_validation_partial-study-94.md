# Chopin Research 094 — Waltz Op.64 No.1 (FINAL 3/3): evidence limits and falsifiable compositional grammar

Date: 2026-11-24 JST. **Cumulative Op.64 No.1 = 3/3, CLOSED.** Prior repository records: [092](2026-11-24_waltz-op64-no1_source_inventory_phrase_ornament_grammar_partial-study-92.md), [093](2026-11-24_waltz-op64-no1_ornament_reduction_boundary_tests_partial-study-93.md). Do not perform a fourth study on this work; next eligible work is Op.64 No.2, subject to history audit.

## Evidence and provenance
- IMSLP work catalogue (accessed 2026-11-24): https://imslp.org/wiki/Waltzes%2C_Op.64_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 ; three waltzes, composition dated 1846–47; No.1 marked Molto vivace, D-flat major. This is **catalogue metadata, not score verification**.
- Chopin's First Editions Online https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/d7bd61db545fe29d2203e3c9ff329823/ was opened again. The public page exposed a generic dynamic filter and no legible first-edition score image. Thus **zero note-level facts, ornaments, measure-specific harmonic analyses or edition variants are verified in this study**. Earlier 092's pagination is unverified as musical form.
- Repository studies 092 and 093 were fetched and read in full; 093 reports that it read studies 07/08, `chromatic_engine_v2.py` and user feedback. **Those three files were not directly fetched again in this run**; avoid presenting inherited defect descriptions as fresh code review.
- Original compositional design below is NOT a transcription of Chopin or an inference about his actual note choices.

## Algorithmic specification: structural-first generative model
Represent score time in exact `Fraction` quarter-note units. A 3/4 bar spans [3n,3n+3). Store independent event streams per voice, including rests, ties, grace anchors, source witness, original/composed flag, image citation and certainty. Represent harmony as a separate set of half-open intervals; split sustained sounding intervals at every harmonic boundary for audit without splitting their structural identity.

Stage A: construct 2–4-bar harmonic and cadential goals, a bass-functional plan, register trajectory and density arc. Stage B: construct two-bar motif objects containing structural pitch contour, inter-onset distances, harmony-goal relations, and voice roles. Stage C: develop a motif with an explicit transform and a traceable invariant (e.g. preserve contour while shifting rhythmic placement or changing the harmonic goal). Unaltered repeats require explicit reprise status. Stage D: ornament structural anchors with tagged passing, neighbor, anticipation, suspension or appoggiatura events; retain anchor identity so removal of ornamental events recovers the structural line. Stage E: independently generate accompaniment and bass on the 3/4 clock; do not import the 4/4 accompaniment of the earlier chromatic engine. Stage F: perform vertical and melodic audits at every sounding event and harmony boundary.

## Hard validation gates and exception policy
1. Every measured voice fills its bar exactly (including rests); grace notes have explicit witness/policy timing and must not silently add beats.
2. Every passing tone must have contextual stepwise arrival and departure with consistent direction between structural anchors; spelled pitch and key context matter. A neighbor returns to its anchor. A suspension needs preparation, continuation and appropriate resolution; an appoggiatura can be unprepared but requires an accented dissonance and convincing resolution. Do not call all chromatic tones passing tones.
3. Chord extensions are allowed only when specified by active harmony; otherwise an unclassified dissonance is UNKNOWN, not PASS. Held pitches must be re-evaluated across harmonic boundaries.
4. Motif transformation must preserve an identifiable invariant and alter a nontrivial property unless flagged as reprise. A three-note cell repeated four times is not evidence of meaningful phrase development.
5. Keep source-backed assertions separate from original examples. Never assign a pitch, cadence or section boundary to Op.64 No.1 without a legible anchored witness.

## Independent executable synthetic checks, run 2026-11-24
Python `fractions.Fraction` checks actually executed:
- 12 sixteenths and 24 thirty-seconds each fill three quarter units — PASS (2 assertions).
- A note spanning [2,4) splits at 3 and 3.5 into exactly [2,3), [3,3.5), [3.5,4) — PASS.
- A verbatim four-anchor motif without reprise is rejected — PASS.
- A changed motif retaining an interval invariant is accepted by a deliberately simple validator — PASS.
- Filtering tagged ornaments preserves the ordered structural anchor IDs — PASS.

**Six synthetic assertions passed.** These tests do NOT establish robust interval spelling, dissonance resolution, orchestration, musical quality, source fidelity, or integration. The motif validator is an intentionally weak prefilter: matching a single adjacent interval is insufficient for musical development and requires a richer future implementation.

## Critical self-audit and handoff
**Status: PARTIAL / SOURCE GATE FAILED.** No directly readable primary-score page; no original bar-specific event fixture; no note-by-note source comparison; no edition variant audit; no integration into existing Python generator. The proposed rules are general-purpose design hypotheses rather than demonstrated distinctive techniques of Op.64 No.1. No fingering or practice research, and no MusicXML/PDF/MP3 outputs.

**Close Op.64 No.1 permanently at 3/3 regardless of completeness.** Transfer unresolved cross-work engineering needs (witness image ingestion, non-chord-tone spelled-pitch classifier, two-bar transformation validator, regression tests) to the next eligible work without reopening this work. Research priority remains études before waltzes before nocturnes, but follow the existing historical ledger to avoid fourth passes.
