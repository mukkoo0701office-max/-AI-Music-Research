# Chopin Research 096 — Waltz Op.64 No.2: witness-dependent attacks and harmony-boundary audit (2/3)

Date: 2026-11-24 JST. **Cumulative count 2/3**, based on repository study 095 (1/3) and current study. This is not an exhaustive audit of all off-repository logs. Next study is final 3/3; never undertake a fourth.

## Evidence ledger
- Directly read repository study 095 and study 093; study 095 records direct reading of research 07/08, chromatic_engine_v2.py/v4.py and user feedback. **These code files were not re-fetched in this pass**, so their reported defects are inherited from the audited predecessor, not independently reverified here.
- Directly inspected Henle critical commentary PDF, printed p.107, https://www.henle.de/media/cd/c4/c0/1697725757/0348-1697725756-sync.pdf . It identifies A1 as draft-like, A2 as engraving model for French first edition F, with A2/F editorial basis. It reports: bar 27–28 C-sharp2 tie in A1 but not A2 (also 155–156); 66–67 E2 tie in German D but absent A1/A2/F, with further analogues; bars 42 and 45 lower-staff chord variants; bar 92 poco ritenuto only F; inconsistent phrase markings at 8–12 and 136–140. **These are the editor's textual claims, not firsthand reading of the manuscript or printed score image.** In the German commentary cis2/e2 denote octave-indexed pitches; avoid translating into MIDI without octave convention.
- No legible primary score image was obtained this pass. Therefore NO note-level claim is certified by direct primary witness comparison. Source authenticity and melodic/harmonic interpretation remain OPEN.

## Algorithmic finding (original implementation proposal, NOT a Chopin transcription)
The decisive unit is a **witness-qualified event graph** rather than a sequence of pitches. Store source_id, page/bar anchor, voice, onset/duration as rational quarters, spelled pitch+octave, attack_id, tie_to_previous, slur_group, ornament_kind, uncertainty and editorial lineage. A tie merges attacks across contiguous equal spelled pitches; a slur never does. An editorial witness must not silently inherit another witness's tie.

### Reusable generation rules
1. Build a two-bar structural skeleton with cadence target and harmonic route before any ornament. A transformation object must preserve at least one phrase invariant (cadential function, contour or metric anchor) and change a substantive parameter (rhythm, diatonic sequence, registral arch or accompaniment). Mere repeated 3-note cells fail the structural diversity check unless explicitly tagged as reprise.
2. Each independent voice has its own event schedule. Split *audit intervals* of sustained notes at every harmony boundary, but never split their attack identity. Nonchord tones require a labelled role and a verifiable preparation/resolution trajectory; UNKNOWN fails closed. Suspensions require prepared consonance before a new harmony and appropriate resolution; accented appoggiaturas are different and need not be tied from the previous chord. Passing/neighbor roles require diatonic spelling and contextual metrical verification, not only semitone arithmetic.
3. Source-specific ties and phrase slurs are distinct from editorial corrections. Store alternative readings without adjudicating by harmonic attractiveness. A grace-note realization needs an explicit timing policy; absent source evidence, keep its attack time unspecified.
4. For 3/4, a bar is exactly 3 quarter units: twelve 16ths or twenty-four 32nds. Sum sounding durations per monophonic voice, account for rests and tuplets, and detect cross-bar continuity; do not double-count tied continuations.

### Executed synthetic tests (2026-11-24, Python fractions.Fraction; **not Chopin-derived fixtures**)
A standalone local Python script executed and passed six assertions:
- equal-pitch contiguous tie merges two written events into one attack;
- absent tie preserves two attacks;
- held interval [2,4) splits into [2,3),[3,4) for harmonic auditing;
- twelve 16ths total 3 quarter units;
- twenty-four 32nds total 3 quarter units;
- an invalid tie between different spelled pitches is rejected.
These checks establish only small invariants. They do NOT verify ornament classification, harmonic spelling, real-score alignment, two-bar musical sequence, voice-leading, or integrated generator behavior. No repository Python generator was changed.

## Critical self-audit / exceptions
- Current toy tie merger assumes previous contiguous event belongs to same voice and merges only adjacent entries; a production implementation must group by voice, handle overlapping chords, enharmonic distinctions, cross-bar rests and tie chains, and distinguish notational versus sounding pitch.
- Counting note durations alone cannot verify a polyphonic 3/4 measure; audit each voice and rest coverage separately.
- Henle editorial comments are useful source-critical testimony but **cannot satisfy the primary-score direct-comparison quality gate**. Any bar-specific claims above are explicitly *attributed to Henle*, not independently verified.
- A dissonance classification engine must permit context-dependent stable extensions and editorial uncertainty without falsely declaring consonance.
- The six synthetic tests do not prove stylistic resemblance to Chopin or aesthetically successful original composition.

## Quality gate and handoff
**PARTIAL / NOT COMPLETE.** Direct primary-score note comparison FAILED (no legible source image inspected). Real-score event fixtures, generator integration, full harmony/voice-leading tests and musical quality review are NOT DONE. Study 3/3 should prioritize readable A2/F image comparison for a short documented passage; if still inaccessible, log the unresolved source gate and advance to the next work, not a fourth study. No performance/fingering research or user-facing score/audio/XML produced.
