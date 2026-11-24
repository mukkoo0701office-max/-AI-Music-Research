# Chopin Research 085 — Waltz Op.34 No.2 (FINAL 3/3): evidence ceiling, polyphonic audit contract and handoff

Date: 2026-11-24 JST. **Cumulative work-specific study count: 3/3**: studies 083, 084, 085. **STOP: do not conduct a fourth Op.34 No.2 study. Next target Op.34 No.3, subject to repository count verification.** Status: **PARTIAL / high-quality source extraction gate NOT passed**.

## Source provenance and scope
Directly fetched and read repository studies 083 and 084 and both original Python files: `research/chopin/code/chopin_op10_2_generativestudy.py` and `research/chopin/code/chromatic_engine_v2.py`. Prior 083–084 document historical score-image inspection of Kullak's edited engraving, not an original first edition. In this run consulted:
- Online Chopin Variorum Edition (OCVE), https://chopinonline.ac.uk/ocve/browse/acview/93b0c463a648827618856c32a8875947/ : source inventory lists **Op.34 No.2 autograph engraver's copy (A-Stichvorlage)**, three pages covering bars 1–40, 41–88 and 89–125. This is a **new source-location finding**, not a claim of reading those image pixels. The OCVE browsing page's text interface did not expose a legible individual manuscript image for note-by-note verification in this run. Important distinction: an engraver's-copy source listing does not imply that the complete autograph survives; Henle says a complete autograph does not survive.
- Annotated Catalogue of Chopin's First Editions, https://chopinonline.ac.uk/aco/catalogue/waltz-opus-34-no-2/ : French first impression `34/2–1-Sm`, German `34/2–1-B&H`, English `34/2–1-W`; later impressions must not be counted as independent original witnesses.
- National Edition Waltzes source and performance commentary, https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes_commentaries.pdf : previous study 083 documents editorial observations about sustained LH minims in opening and ornament/tie variants. **Editorial statements only until original noteheads are checked**.
- Henle work description https://www.henle.de/Waltz-a-minor-op.-34-no.-2/HN-659 : first French edition corrections in certain copies; incomplete autograph survival.
- Kullak edited-score scan https://s9.imslp.org/files/imglnks/usimg/f/fc/IMSLP82141-PMLP02370-FChopin_Waltzes_Op34.pdf , printed p.14, inspected in study 084; edited witness only.

No specific first-edition or autograph pitch, bar-level chord, tie, ornament note or formal boundary is asserted from unseen score pixels. **No first-edition note-by-note comparison was completed.**

## Verified defects of existing code (actual source inspection)
1. `chopin_op10_2_generativestudy.py`: eight bars in 4/4; 16 successive chromatic semiquavers per bar; RH harmony quarter notes; LH root/fifth quarter-note oscillation. It has no independent simultaneous sustained LH voice, no harmonic-boundary sounding-set audit and no source witness metadata.
2. `chromatic_engine_v2.py`: four repeated three-note neighbor cells + four-note approach per 4/4 bar. Its sole harmony check is that the **last** upper target belongs to the bar's `tones` pitch-class set. This does not check accented dissonances, intermediate chromatic notes, carried-over tones or resolution across a harmonic boundary. Its per-bar note count and leap assertions are necessary but insufficient.
3. Neither implementation supports witness-qualified alternative ornament spellings, independent 3/4 voice clocks, 2-bar harmonic-cadence transformations, or explicit nonchord-tone uncertainty. No edits to these production files were made in this run.

## Reusable ORIGINAL composition grammar (hypotheses, NOT claims about Chopin's actual notes)
`FORM -> SECTION[phrase_plan] -> 2-BAR PAIR[goal1,goal2] -> HARMONIC SPANS -> VOICE EVENTS -> ORNAMENT VARIANTS -> AUDIT`.
- A phrase plan contains `section_id, tonal_region, cadence_goal, density_curve, register_curve, motive_identity`. Two-bar pair B must preserve a recognizable contour/rhythm/interval invariant of pair A while changing at least one consequential property (cadence, bass goal, register, voice assignment, harmonic rhythm); exact reprise requires explicit `reprise=true`. Do not enforce variation on a literal refrain.
- Event: `{voice, staff, onset:Fraction, duration:Fraction, pitch, attack, tie_group, witness, source_class, bar, confidence}`. A tie joins same-pitch continuation without new attack; slur does not. Rests occupy a voice's rhythmic ledger. Multiple voices on one staff have separate clocks.
- For 3/4: each active voice independently covers `3/4` with notes/rests; an onset may be at any rational subdivision including 1/16 or 1/32. **Do not sum concurrent voice durations across voices.** Grace notation has separate zero-meter occupancy and an optional execution-time policy.
- Harmony event `{start,end,pitch_classes,function,tonal_context,confidence}`; at each note onset, note release and chord boundary compute sounding notes with half-open interval `onset <= t < onset+duration`. An intentionally accented dissonance is not automatically a defect.
- Contextual NCT candidate labels: `passing` (stepwise between anchors), `neighbor` (departure/return), `appoggiatura` (accented nonchord onset resolving by step), `suspension` (consonant preparation, uninterrupted tied/sustained onset across boundary, dissonance then step resolution), `anticipation`, `unknown`. These are *candidates* pending meter, local harmony, spelling and source verification. Do not certify suspension by pitch-class membership alone. A chromatic ornament may change its function with local chord context.
- Ornament variants retain `witness_id, glyph, grace_count, written_value, attachment, source_confidence, editorial_policy`. Do not collapse a source's two grace notes into another's mordent or infer a fixed execution length from notated grace values.
- Failure gates: missing/overlapping voice occupancy unless explicitly polyphonic, unresolved tie target, impossible notated beat sum, accidental context inconsistency, missing witness attribution, unclassified dissonance flagged for human audit, untransformed repeated 3-note cells over two bars, unsupported original-score assertions.

## Executed internal synthetic checks (2026-11-24)
Executed Python using `dataclasses` and `fractions.Fraction`; output: **PASS 6 synthetic assertions**:
1. Three independent concurrent voices each total exactly 3/4.
2. At quarter-note 1/4, active notes from overlapping bass/inner/upper voices correctly returned.
3. At 1/2, inner voice reattack replaced its preceding sustained note while bass remained held.
4. `3/4 == 12*(1/16) == 24*(1/32)`.
5. A held synthetic C (MIDI 60) over a synthetic E-major harmony is outside chord classes while its subsequent B (MIDI 59) is in the chord; this only checks a candidate resolution, **not a certified suspension**.
6. A synthetic gapped voice has duration total different from 3/4 and is rejected.

Fixtures are entirely invented, not quotations/transcriptions of Chopin. These tests were run as an independent script in the execution environment; **the repository's original scripts were not run or modified**, and no reusable module was committed. No audio, XML or PDF output was produced.

## Critical self-audit and unresolved handoff
**FAIL: full source-backed extraction.** OCVE now provides a more promising *autograph engraver's-copy* locator than the previously used edited score, but no readable autograph/first-edition note image was obtained for direct pitch-level verification. Consequently detailed source-grounded harmonic analysis, voice-leading attribution and specific 2-bar phrase transcription remain unverified. User-approved high-scoring composition exemplars were not independently retrieved in this run. Synthetic arithmetic is not evidence of expressive quality or original-score fidelity. Do not label this as complete or source-note-verified.

**Mandatory transition:** Op.34 No.2 cumulative count is now **3/3**. No fourth study even if deficiencies persist. Carry the unverified source-image comparison and generalized multi-voice audit module to cross-work engineering backlog, not another Op.34 No.2 research run. Next research target **Waltz Op.34 No.3**, after checking its historical count. Maintain hourly schedule.
