# Chopin Nocturne Op.9 No.1 — opening evidence and generative grammar (study 1/3, provisional)
Date: 2026-11-26. Status: **partial, score-level quality gate not passed**.

## History / eligibility
Read the preceding history-integrity audit (2026-11-26_study_count_integrity_audit_op10no3_handoff.md), which inventoried >=6 Op.10 No.3 studies and found no nocturne studies in the current tree. Thus Op.10 No.3 is excluded. This is **Nocturne Op.9 No.1, visible study 1/3**; total historical count remains subject to deleted-commit review. No extra étude study performed.

## Source hierarchy and direct observation
- Primary witness **identified, not note-checked**: German Kistner first edition, Leipzig [1833], plate 995, IMSLP #86550, https://imslp.org/wiki/Nocturnes%2C_Op.9_%28Chopin%2C_Frederic%29 ; scan also https://commons.wikimedia.org/wiki/File:Chopin_Nocturnes_Op_9_Kistner_First_Edition_1832.pdf . The scan's bibliographic date is inconsistently stated 1832/1833; do not silently collapse.
- French M. Schlesinger first edition metadata: https://chopinscores.org/en/partytura/3 (20 Dec 1832). German Kistner metadata: https://chopinscores.org/en/partytura/23 (Jan 1833).
- **Directly inspected score image**: page 1 of *Pierre Gouin, Éditions Outremontaises (2005)*, https://s9.imslp.org/files/imglnks/usimg/c/c9/IMSLP127747-WIMA.9680-Chopin_Nocturne_no1.pdf . This is a modern derivative edition, NOT a primary witness. All notation observations below are edition-specific pending first-edition collation.
- PTNA secondary commentary: https://enc.piano.or.jp/en/musics/21882 ; commentary calls form three-part with expanded middle section. This is secondary, not an independently audited formal analysis.

### Visible notation facts (Gouin p.1 only)
6/4, six-flat signature, Larghetto; opening melodic line is not a three-note repeated cell. Bar 1 upper line contains a group of six beamed eighths followed by sustained/staccato notes over the remainder of the system; bass enters after an initial rest, then plays six-eighth arpeggio units. Bar 2 has a long melodic tone, then a **11:12** beamed upper flourish; bar 3 includes **22:24**; the bass accompaniment maintains two groups of six eighths per full 6/4 bar. Bars 4–9 juxtapose long upper tones, repeated articulated notes, and short connecting groups, against the repeating but pitch-varied arpeggio substrate. The printed notation includes ties/slurs, dots, hairpins and pedal. **Do not infer specific pitches or harmonic functions from this inventory**; no systematic note-by-note first-edition comparison was made. The score has an initial upbeat-like bass-rest asymmetry that must be preserved rather than normalized away.

## Generative design (ORIGINAL ALGORITHM, not attributed notes)
Represent all events as rational quarter-note positions with explicit tuplet ratio and nested voice IDs. Six quarter units/bar. Three layers:
1. **Melody skeleton**: phrase anchors with structural onset, target pitch-class, tension and release; generate variable-length long-tone spans, then optionally ornament between anchors. Do not force a three-note cell or equal subdivision.
2. **Accompaniment**: two 6-eighth-note spans per 6/4 bar as a *candidate* pattern, each generated from harmonic target, inversion, register trajectory, and bass-leading constraint; allow controlled departures, changed pitch content and different chord spans. This is a model inspired by directly viewed modern edition, not an asserted universal Chopin rule.
3. **Ornament events**: assign a local rational time window to an n:m tuplet. Preserve duration sum exactly: if window is D and ratio n:m means n equal events occupy m reference units, event duration D/n. For a 11:12 or 22:24 group, verify actual window from notation, never assume the whole bar is filled. Grace notes may be non-metrical and must be stored separately from timed attacks.

### Non-chord-tone verification contract
For each proposed passing tone, neighbor, appoggiatura or suspension record {event, harmonic context, previous stable event, next stable event, metrical accent, preparation, resolution, voice}. An NCT is **UNVERIFIED** until all relevant fields are grounded; passing requires stepwise entry/exit; neighbor returns to anchor; appoggiatura has accented dissonance resolving by step; suspension requires preparation/consonance, held-over dissonance and resolution. Chromatic exceptions require separate labelled rationale. Pedal resonance is not itself proof of vertical harmonic membership.

### Two-bar transformation contract
Store phrase anchors and contour separately from ornaments. Transform two-bar skeleton via register, harmonic recontextualization, onset shift, augmentation/diminution and selected approach-tone insertion; preserve a checkable invariant (anchor contour or interval signature) and document any deliberate change. Reject trivially repeating 3-note cells as a substitute for phrase architecture. Bass line and inner voices are independently evaluated for functional coherence, voice overlap, and forbidden parallels in *structural* voices, not blanket parallel bans on ornamentation.

## Audit / acceptance tests to implement (NOT EXECUTED)
- Rational-grid sum: every full 6/4 voice has six quarter units; distinguish partial opening measures; test 11:12 and 22:24 as bounded windows.
- Negative fixtures: incorrectly sized tuplets, unresolved suspensions, passing-tone leaps, dangling ties, crossed structural voices, unmotivated repeated 3-note cells.
- Positive fixtures: independent 2-bar melodic transformation with changed ornament density and continuous harmonic bass.
- Separate tests of symbolic grammar from score fidelity; synthetic tests cannot certify Chopin analysis.

## Unresolved / quality gate
1. First-edition scan **not directly inspected**. No bar-level pitch or harmony attribution is certified.
2. Research 07/08 and the master protocol / user-approved works were not re-read in this run; preceding audit says 07/08 read, but that is not equivalent to fresh verification.
3. No code executed; existing validator_v2 is only a synthetic time/tie/transposition validator, not NCT or score-fidelity proof.
4. Need compare French/German first editions, annotate a limited bar range from image with explicit source/page, then run real negative fixtures.
**This is an incomplete study, not a completed high-quality Chopin analysis.**