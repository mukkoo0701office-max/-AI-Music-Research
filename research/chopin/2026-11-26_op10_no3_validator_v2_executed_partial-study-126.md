# Chopin research 126 — Op.10 No.3: cross-work event validator implementation (PARTIAL)
Date: 2026-11-26 JST. Target: Etude Op.10 No.3. This is an **engineering-only provisional continuation**, NOT an analysis of verified original notes.

## Eligibility / cumulative count
Op.10 No.2 is closed (>=3). Prior Op.10 No.3 study: `2026-11-26_op10_no3_source_inventory_validator_contract_partial-study.md` (at least one prior study). GitHub code search returned no matches even for known files; historical total and deleted-file audit remain unavailable. **Minimum visible count including this run: 2; certified cumulative count: UNKNOWN.** Do not perform another Op.10 No.3 study until complete inventory confirms <3. If already >=3, skip immediately. No fourth run authorized.

## Read and evidence
Read existing `research/chopin/code/two_bar_event_validator_v1.py`, previous Op.10 No.3 source inventory, and research 124. V1 rejects constant transpositions, merges voices, and assumes a fixed six-quarter-note span. Source witnesses identified previously: [OCVE autograph source index](https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/9fe4d060d86d8603533171e2c9b682f6/), [NIFC engraver's manuscript catalogue](https://sklep.nifc.pl/en/produkt/77084-etudes-op-10-autograph-stichvorlage-fryderyk-chopin-museum-warsaw), [Morgan autograph sketch record](https://www.themorgan.org/music-manuscripts-and-printed-music/114339). **The notation itself was NOT inspected this run.** No Chopin bar, pitch, phrase or harmony claims are made. High-rated user work and protocol were not located or inspected.

## New executable original engineering grammar
File: `research/chopin/code/two_bar_event_validator_v2.py`. This is a synthetic prototype, not a transcription. Events have voice, rational onset/duration, pitch, chord-group, and reciprocal tie flags. The validator uses a meter-dependent exact span (e.g. two 3/8 bars = three quarter units), checks each voice separately, permits same-onset chord members with an explicit group, rejects overlaps/gaps, and checks tied pitch continuity. A voice-specific two-bar comparison distinguishes EXACT, CHROMATIC_TRANSPOSITION (constant pitch offset with unchanged rhythm), and UNCLASSIFIED (including contour-only false positives). Three-note minimum is only a *filter*, not proof of motivic identity.

## Executed tests
Executed `python two_bar_event_validator_v2.py` locally. Output: **PASS: 9 synthetic regression cases; NO Chopin score verification**. Cases: exact recurrence, +2 semitone transposition, contour-only rejection, simultaneous chord, 3/8 span, valid tie, gap rejection, ungrouped simultaneous-note rejection, invalid tie rejection. This tests the copied source code content, not an installed package or GitHub CI.

## Critical self-audit and remaining defects
1. A same-voice chord whose constituent pitches have different tie statuses is only partially supported; chord-group identity and tie matching can be ambiguous with duplicate pitches.
2. No explicit rest-vs-unknown distinction; gaps are rejected, but voice pickup/incomplete bar support is absent.
3. No pitch spelling, key, source/witness ID, editorial confidence, anchor map, ornamented return, diatonic sequence, harmonic motion or source-linked event annotation.
4. No NCT classification: suspension/appoggiatura/passing/neighbor need attack-vs-held distinction, metrical stress, harmony-boundary analysis, preparation and resolution; unknown must remain UNKNOWN.
5. No counterpoint/parallel-perfect auditing; no formal repeat graph, 16th/32nd density generator, or composer-specific evaluation.
6. The source image, scholarly harmonic analysis, existing high-rated works, and full historical study count remain unverified. Consequently **the required primary-source quality gate is NOT passed**.

## Handoff / hard stop
Do not call this completed Chopin research. Next eligible run must first establish the full historical Op.10 No.3 count. If 3+, move to Op.10 No.4 immediately; otherwise inspect actual primary score notation and test NCT + harmonic event boundaries before attributing compositional principles to Chopin. Do not spend research time producing user-facing audio or scores.
