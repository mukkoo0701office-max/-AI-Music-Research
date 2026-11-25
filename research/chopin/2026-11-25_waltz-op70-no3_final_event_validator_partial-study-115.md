# Chopin Research 115 — Waltz Op.70 No.3 — final permitted study (3/3; PARTIAL)
Date 2026-11-25 JST. Count: Research 113=1/3, 114=2/3, this study=3/3, as supported by accessible repository records; deleted/renamed history not exhaustively verified. **Close this work now; no fourth study.**

## Source audit
- IMSLP https://imslp.org/wiki/Waltzes,_Op.70_(Chopin,_Fr%C3%A9d%C3%A9ric) lists first German edition #447391 (Schlesinger, 1855, plate S.4396) and French edition #399505 (Meissonnier, ca.1855, plate J.M.3527). Catalogue page inspected; **individual score pages not visually inspected**. These are posthumous editorial witnesses, not autograph evidence.
- NIFC https://chopin.nifc.pl/en/chopin/kompozycja/26_waltz-in-d-flat-major describes contrapuntal texture and lower-voice melodic interest; this is a secondary characterization, not a verified bar-level transcription.
- Previous research 113/114 and existing `research/chopin/code/waltz_event_audit_v2.py` read. Existing v2 compares abstract motif metadata, lacks outgoing tie reciprocity and does not establish functional NCT classification.
- Original pitches, precise bars, harmonic progressions, and formal section boundaries: **NOT VERIFIED**. No invented score claims.

## Implemented original rule prototype
New standalone `research/chopin/code/two_bar_event_validator_v1.py` is a **synthetic** validator, not a replacement for the existing generator.
- Model each two-bar 3/4 phrase as six exact rational quarter-beats; each voice must tile its interval without overlap/gaps (rests explicit via pitch=None).
- Tie-in and preceding tie-out must be reciprocal and pitches identical; dangling ties fail.
- Compute contour from *attacked events*, excluding tie continuations; compare actual pitches and onset times. Reject identical phrases and simple transposition as insufficient evidence of developed variation; accept contour-preserving, nonuniform pitch variation. This is a narrow heuristic, not a general musicological definition.
- Preserve a distinction between a role-transfer *design* and actual Chopin contrapuntal evidence.

## Executed checks
Standalone Python executed in local container: **PASS 8 synthetic assertions** (one transformed motif, two rejected motifs, one valid tie, four rejected malformed sequences). No real-score regression, no NCT semantic audit, no integration tests. The code's printed count is 8. Synthetic examples are wholly original and cannot establish source fidelity.

## Unresolved technical issues / critical self-audit
- First-edition score pixels inaccessible in this run; no note-level evidence. This **fails the primary-source quality gate**.
- New validator does not detect voice exchange, chromatic spelling, suspensions/appoggiaturas, harmonic reinterpretation, vertical parallels, 16th/32nd note ornament appropriateness, or cadence-level form. No claim of their implementation.
- Signature only uses contour signs, not interval size or accent hierarchy; transformation heuristic is intentionally conservative and can reject legitimate transpositions.
- Tie validation requires both ends inside a two-bar span; cross-window ties need explicit boundary state.
- Repository high-rated example scores were not independently confirmed. No production generator changes.
- **Quality verdict: PARTIAL, NOT COMPLETE.** The 3-study cap takes precedence over perfection. Carry these limitations into a different work or cross-work infrastructure study, never a fourth Op.70 No.3 study. Future target selection must consult cumulative repository history and restore the requested Etudes > Waltzes > Nocturnes ordering wherever eligible.
