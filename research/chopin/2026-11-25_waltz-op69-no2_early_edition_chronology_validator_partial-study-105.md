# Chopin Research 105 — Waltz Op.69 No.2 / WN19 — PARTIAL 2/3
Date: 2026-11-25 JST. **Cumulative run 2/3**: research 104 = 1/3, this = 2/3. Research 103 confirms Op.69 No.1 exhausted at 3/3. Do not count a third run without a distinct execution.

## Newly checked scholarly source and correction
Chopin Online early-editions heading, directly read as PDF text: https://chopinonline.ac.uk/media/documents/Op.69.heading_IG2hTjM.pdf (lines 3–12). Publication chain for No.2: Cracow Wildt from 1852; London Wessel 1853–60; Ewer from 1854; Paris J. Meissonnier fils 1855–April 1856; Berlin A.M. Schlesinger 1855–64. These are *publication metadata*, NOT direct score-note readings. Compare IMSLP https://imslp.org/wiki/Waltzes,_Op.69_(Chopin,_Fr%C3%A9d%C3%A9ric), which identifies a Żywny manuscript copy dated 1829, BJ Muz. Rkp. 2201 I, scan #774821; 1854 Ewer scan #97198; 1855 Meissonnier #400818. The 1829 item is a **copy**, not an autograph. Early publication is plural, not one generic posthumous edition. The chronology should be conditioned on printing/state, not presumed identical musical text.

## Existing code and research audit
Read research 104 and code/waltz_event_audit.py and prior 103. Existing code relies on assert (which Python -O removes), tests harmonic intersection rather than continuous nonoverlapping coverage, and treats pitch-class membership as sufficient for consonance; its two_bar_transform accepts a one-field metadata-only difference. Research 104 specified witness separation but had no executable regression. Do not conflate source cataloguing with a primary notation comparison.

## New executable synthetic regression — actually run locally
A standalone Python 3 test using fractions.Fraction and explicit ValueError was executed 2026-11-25 JST. **Six synthetic cases passed**:
1. Complete 0–1–3 harmony coverage, same-pitch tie, one attack accepted.
2. Harmony gap 1–2 rejected.
3. Harmony overlap 1–2 rejected.
4. Changed-pitch tie rejected.
5. Rest-to-rest tie rejected.
6. Unencoded silent voice gap rejected.
Core algorithm: check harmonic intervals form a contiguous partition [0,end]; each voice is a contiguous event partition including explicit rests; tied continuation requires adjacent same sounding pitch and is not a fresh attack. These tests validate temporal representation only. They are not score fidelity or NCT analysis. Script was executed locally, **not committed or integrated** into existing repository generator.

## Compositional algorithm extension (original model; NOT Chopin note claims)
Represent an early-source witness as (repository ID, edition/printing state, scan/page, measure, verification status). Keep musical events and uncertain source readings separately. For original composition, build cadence and bass trajectory before melodic anchors; subdivide selected intervals into 16ths/32nds using directed neighbor/passing/turn patterns. Require rational duration conservation, metrically salient structural anchors, and voice-specific event partitions. A two-bar variation must preserve at least two *musical* invariants (rhythmic stress, contour, phrase goal, bass direction) and vary one substantive dimension. Witness metadata cannot be a motivic variation. NCT classification must inspect spelling, harmony vocabulary including extensions, metrical accent, preparation, approach and resolution; unresolved cases remain UNKNOWN. Held notes across harmonic changes are analytically re-evaluated without generating attacks.

## Quality gate / critical self-audit
**PARTIAL; PRIMARY SCORE GATE FAILED.** Scholarly early-edition *heading* directly read, but no 1829 manuscript copy, 1852 Wildt, 1854 Ewer or 1855 Meissonnier notation page was directly inspected; no measure-level pitches, voice-leading, formal section or Chopin-specific NCT is asserted. Six synthetic tests passed but no source-based or integrated generator tests. No verified compositional style discovery yet. Final allowed run 3/3 must prioritize actual scan inspection, page/bar-specific evidence and implementation integration; if inaccessible, explicitly record failure and move to the next work after 3/3. No fingering/practice, audio, XML or user PDF produced. Schedule unchanged.
