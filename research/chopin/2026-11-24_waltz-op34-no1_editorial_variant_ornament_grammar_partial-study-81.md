# Chopin Research 081 — Waltz Op.34 No.1 (2/3): edition-grounded ornament, variant and voice-leading constraints

Date: 2026-11-24. **Cumulative research of this work: 2/3** (080 + 081). Next and last permitted: 3/3. **Status: PARTIAL; editorial evidence verified, facsimile note-level audit NOT performed.**

## Source and provenance ledger
1. Directly read prior repository study 080: `research/chopin/2026-11-24_waltz-op34-no1_witness_map_generation_gates_partial-study-80.md`. It explicitly lacks primary-score-image verification. Read prior 079 (Op.18 3/3), for witness-aware alignment and non-chord-tone policy. Repository code search for 07/08 returned no hits; the previously cited `code/chopin_op10_2_generativestudy.py` returned 404 at that path. Thus **no claim of checking historical Python or user-approved outputs**.
2. Directly read Jan Ekier and Paweł Kamiński, *National Edition, Waltzes: Performance and Abridged Source Commentary*, PDF pp. 1, 4–5: https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes_commentaries.pdf . This is a scholarly secondary/critical report **of primary witnesses**, NOT an examination of original facsimile noteheads. OCR/text extraction loses some accidentals and superscripts: precise pitch spellings below are deliberately withheld where ambiguous.
3. Cross-checked bibliographical distinction of FFE original/corrected impression, GFE and EFE in Chopin Online *Annotated Catalogue of First Editions*: https://chopinonline.ac.uk/aco/catalogue/waltz-opus-34-no-1/ . OCVE listing https://chopinonline.ac.uk/ocve/browse/acview/93b0c463a648827618856c32a8875947/ did not expose directly readable score images in the fetched text.

## Source-grounded historical/editorial observations (NOT original note transcription)
- Source commentary: earlier autograph **AI** dated 15 September 1835 (original lost, photocopy preserved); final autograph **A** adds a coda and changes melodic-rhythmic and harmonic details. FE first Paris edition 1838 derives from A; GE1 derives from earlier FE proofs; EE1 also derives from FE with adjustments. The editors choose A, incorporating probable authorially accepted FE changes and pupil-copy annotations (PDF p.4).
- **Bars 26 and 186, R.H.**: editors report a chromatic alteration added in FE proofs at 26, extended editorially to analogous 186; A/AI preserve a variant. A grace-note slur may denote arpeggiation or a conventional sign; FE engraving position can falsely suggest a tie. Exact pitch spelling needs facsimile confirmation (p.4).
- **Bars 29 and 189**: grace-note placement relative to barline differs due to an apparent engraving error in 189; GE2 propagates that position to both. Barline placement must not silently change the metrical anchor (p.4).
- **Bars 62 and analogues, L.H.**: GE1 repeats the first chord on beat 2 by error; a copy-and-paste accompaniment algorithm would reproduce a documented source mistake (p.4).
- **Bars 67, 71 and analogues**: final A and first editions distinguish mordents; some later editions replace them with trills. Richer ornamentation in earlier AI is not license to substitute ornaments globally (pp.4–5).
- **Bar 83 and analogues**: deletions associated with changes in upper-voice note count/rhythm were mistaken for a tie in FE (p.5). Therefore parse graphical tie evidence separately from duration and voice count.
- **Bars 163–164 and 167–168**: annotations in a pupil's copy are interpreted editorially as optional octave extension of passages, corroborated in part by AI; represent this as a variant with explicit register envelope, not a mandatory transposition (p.5).
- **Bars 262 and 264**: source variants illustrate melody chromaticism potentially independent of the accompanying harmony. Editors explicitly reject treating absence of a natural as necessarily a mistake. A non-chord tone classifier must not force every melodic chromaticism into the nearest chord member (p.5).
- **Bars 272–273**: FE lineage lacks a tie reported in the editorial commentary; held-sound validation is witness-dependent. **Bars 303–304**: A once had two extra bars between them, subsequently deleted; remnants of an expression sign caused a print error. This is a concrete distinction between *revision history* and the *final sounding form* (p.5).

## Original generative rules (hypotheses, NOT claims about exact Chopin notes)
### A. Multi-layer score representation
`Event = {witness,local_bar,voice,onset:Fraction,duration:Fraction,pitch_spelling,notation_kind,source_image_ref,evidence_tier}`. Independent objects: `StructuralVoice`, `Ornament`, `HarmonyWindow`, `EditorialVariant`, `FormNode`. Source-derived note claims require a readable image or reliable diplomatic transcription; editorial prose only licenses editorial claims.

### B. Grace and ornament scheduling
Each grace event has `anchor_event_id`, `notation_side_of_barline`, `performance_offset_policy` (before/on beat/undetermined), and `witness`. The *structural beat* remains fixed under ornament realization. Never equate an arpeggio slur with a sustain tie. Distinguish mordent/trill/grace group as different token types. Allow user-defined original ornament variation but prohibit silently relabeling it as original-source fact.

### C. Two-bar motive grammar
Plan two bars as `(cadence_goal, bass_trajectory, melody_anchor_contour, accent_profile, ornament_budget, registral_apex)`. Transform by preserving >=1 salient identity dimension (rhythmic contour or melodic skeleton) while changing >=1 other (harmonic destination, register, countermelody, or ornamental placement). If a genuine reprise is tagged, literal repetition is permitted. Detect short 3-note loops that repeat without changes in harmonic/phrase function. **Do not treat the editor's bar-26/186 analogy as proof of complete identity.**

### D. Harmony and non-chord tones
First assign bass anchors and harmonic spans, then melodic skeleton, then elaboration. At every onset AND harmony boundary evaluate active held tones. Label PASSING only for stepwise directional connection; NEIGHBOR for return; SUSPENSION only with an independently evidenced tie/sustain and resolution; APPOGGIATURA only with accent/approach/resolution evidence. If chromatic melody clashes with a chord, retain `CHROMATIC_INDEPENDENT` or `UNRESOLVED` when context warrants; do not 'correct' automatically. A documented source variant may replace the harmony classification, not overwrite it.

### E. Voice integrity and cadence
Generate left-hand bass + middle chord voices independently; bar occupancy uses exact rational times for eighths, sixteenths and thirty-seconds. Cross-voice dissonance tests include sustained notes and register. Cadence planning must precede density changes; coda is a formal graph node, not simply more notes. Revision-history deleted bars must not be inserted into final-form metrical sums.

## Tests specified (NOT executed in this run)
1. Grace-note notated before vs after barline with identical anchor -> unchanged metrical sum; distinguish historical witness.
2. Slur drawn between same pitch events -> NOT a tie unless tie token confirmed.
3. Beat-2 chord copying from beat 1 -> reject when a witness-specific chord change is required.
4. Variant chromatic melody at 262/264 -> keep both possibilities; do not force diatonic correction.
5. Hold across harmony boundary -> re-evaluate dissonance and resolution.
6. Two-bar sequence preserving contour but changing cadence target -> accepted; three-note loop without structural development -> flagged.
7. Deleted revision-history bars -> absent from final-form event graph.
8. Sixteenth/thirty-second subdivision -> exact rational occupancy, including simultaneous independent voices.

## Critical self-audit and handoff
**Failed finished-quality gate**: direct score-image reading and note-by-note transcription unavailable; detailed functional harmony and exact pitch claims unverified; historical Python code not found at cited path; no test executed, no generator integration, no user-approved work compared. This document advances *source-specific, falsifiable constraints* rather than claiming a verified complete analysis. On **3/3**, seek facsimile access and run actual fixtures; after that, move to Op.34 No.2 regardless of completeness. No fourth study of Op.34 No.1.
