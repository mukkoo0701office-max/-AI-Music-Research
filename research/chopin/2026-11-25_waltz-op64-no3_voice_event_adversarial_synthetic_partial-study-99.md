# Chopin Research 099 — Waltz Op.64 No.3: voice-event adversarial audit (2/3)

Date: 2026-11-25 JST. **Cumulative research count: 2/3** (098 plus this study; repository-scoped, off-repository executions not independently exhausted). **Do not exceed 3/3.** Next permitted study of this piece: final 3/3 only.

## Source audit / historical claims
- Directly retrieved study 098 and study 097 from this repository, plus `research/chopin/code/chromatic_engine_v4.py` and `feedback/USER_PREFERENCES.md`.
- IMSLP catalogue, https://imslp.org/wiki/Waltzes,_Op.64_(Chopin,_Fr%C3%A9d%C3%A9ric), explicitly lists an **1847 French first edition** (Brandus, plate 4743), scan #400823, 10 pages for No.3; and Kullak's **1880 instructive edition**, #82854. Catalogue metadata was verified in this run, **but the 1847 score image was NOT read note-by-note**. The earlier study 098 reports direct observation of a Kullak-edition page only. An edited witness must not be treated as an autograph.
- Consequently: **no newly verified original measure-level pitches, chords, ornaments, tie variants or left-hand melodic transfer** in this run. Prior PTNA left-hand-transfer/form interpretation is secondary and remains unverified against first edition. All algorithm examples below are **original synthetic designs**, not Chopin transcriptions.

## Defect assessment: actual v4 source inspection
`chromatic_engine_v4.py` generates 32 chromatic notes per two-bar unit, using eight direction blocks, four notes per block. Its `contour` uses `out.extend(out[-1]+direction for _ in range(4))`: each extension uses the current last element as the generator advances, yielding four successive semitone steps, not a fixed three-note cell. Nevertheless, it is **only a sign-controlled monotonic four-step block grammar** and lacks independent voices, actual 3/4 metric, score provenance, harmony-spanning dissonance checks and meaningful two-bar thematic/cadential development. The source `audit()` checks only semitone adjacency, count, and pair-boundary jumps. **Its source was read, not executed here.** Do not misstate the implementation as a literal 3-note loop.

## Original reusable grammar (not a historical transcription)
`WrittenEvent(witness_id, voice_id, onset:Fraction, duration:Fraction, spelled_pitch, tie_from_previous, slur_id, role)`. Separate written-note, attack, and sounding-interval graphs. A valid tie must continue the identical pitch contiguously; slurs do not merge attacks. A tied sounding interval intersecting two `HarmonySpan` objects produces **one attack but two harmonic assessments**. The source/witness ID is mandatory and edition readings must never be silently merged.

For 3/4, represent a bar as exactly three quarter-note units per **independent voice**, rests included. A chord consists of simultaneous events, not multiple successive duration claims. Do not assume 16th/32nd notes are a proxy for complexity: develop density from formal purpose and counterpoint. Ornament placement occurs after structural melody and cadence, with metric/duration constraints and explicit grace-note policy.

`RoleAssignment(section, voice_id, role, interval)` allows melody to move between registers or hands; role transfer is conditional, not asserted as verified in Op.64 No.3. During transfer, require explicit continuation or rest for bass/accompaniment, and avoid incompatible overlapping monophonic events.

Two-bar `Motive` should encode at least contour, metric salience, harmonic targets, cadence role and voice distribution. Transformation must preserve one musically meaningful invariant and alter one significant parameter; exact repetition is allowed only as marked reprise. **This is a provisional engineering heuristic, not a claim that all Chopin phrases follow a fixed invariant rule.** Re-audit dissonances after reharmonization, particularly accented chromatic approaches, suspensions and cross-boundary ties. UNKNOWN NCT classifications fail strict acceptance; a designated extension requires harmony-specific authorization.

## Executed synthetic tests (NOT Chopin-score validation)
Ran a separate Python/Fraction in-session harness with **8 assertions**:
1. Valid 3/4 event coverage passes.
2. Two contiguous identical tied pitches yield one attack.
3. Same pitches without tie yield two attacks.
4. Sustained interval across I/V boundary receives two harmonic-span labels.
5. Changed harmony with preserved contour passes a minimal two-bar development predicate.
6. Unchanged contour/harmony fails that predicate unless marked literal reprise.
7. Overfull 13-sixteenth bar rejected.
8. Overlapping monophonic voice events rejected.

These are **synthetic unit tests only**, not tests of the existing v4 generator or score fidelity. The minimal motive predicate does **not** establish musical quality, and the span test establishes intersection only, not accurate dissonance labels. The negative-test harness intentionally raises and catches assertion failures. No new test source committed; reproducibility requires porting the harness into repository tests in a subsequent authorized study.

## Critical quality gate
**PARTIAL / NOT COMPLETE**. First-edition PDF notes were not directly compared; no original pitches/bars certified; no formal analysis verified against a primary witness; no v4 integration; no repository CI tests; no original generated music assessed. The main improvement over 098 is a falsifiable synthetic attack/rhythm/voice-event audit and a more precise correction of the actual v4 contour mechanism. User preferences favor smooth independent voice-leading and restrained chromaticism, but cannot serve as evidence of Chopin's choices.

## Final permitted handoff (3/3 maximum)
Attempt direct legible inspection of Brandus 1847 No.3 scan #400823 and cross-check with Kullak while separating editorial annotations. Implement a **small** repository test module for attack/tie, rational 3/4 duration, harmony-boundary NCT and two-bar transformations; run it and report actual results. If primary source access fails, mark unresolved and **close the work at 3/3 regardless**. Afterward move to the next eligible work, not a fourth study. No performance/fingering research or user-facing audio/XML/PDF.
