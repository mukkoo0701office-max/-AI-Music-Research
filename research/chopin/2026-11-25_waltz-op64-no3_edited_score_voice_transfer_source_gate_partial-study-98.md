# Chopin Research 098 — Waltz Op.64 No.3: voice-transfer and cadential texture grammar (1/3)
Date: 2026-11-25 JST. **Cumulative work count: 1/3** (repository research/chopin directory inspected: Op.64 No.1 092–094 and No.2 095–097 each 3/3; no prior Op.64 No.3 file found). This count is repository-scoped, not a proof of no off-repository runs.

## Evidence hierarchy and directly inspected notation
1. **Direct score-image observation, but NOT a first edition or autograph:** Wikimedia Commons PDF of a historical Kullak *instructive edition* of Op.64 (13 pp.), PDF page index 9, printed p.39, opening of Waltz No.3. https://upload.wikimedia.org/wikipedia/commons/9/94/Waltzes,_Op.64_(IA_imslp-op64-chopin-frdric).pdf . Page visibly says Moderato, A-flat-major four-flat key signature, 3/4, and shows a treble melodic line over bass-plus-chordal attacks on beats 1, 2, 3; several melody phrases cross barlines under slurs. A later line on that page visibly places bass-staff material in treble clef with an independent upper line. These are **observations of the edited witness**, not guaranteed autograph readings. Kullak's editorial tempo/metronome, fingering, pedal and expressive annotations MUST NOT be attributed uncritically to Chopin.
2. IMSLP work catalog: https://imslp.org/wiki/Waltzes%2C_Op.64_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 — composition 1846–47; publication 1847; No.3 Moderato in A-flat. It also lists an 1861 Breitkopf reprint (file #854620) and other witnesses. Bibliographic listing is **not direct score inspection**.
3. PTNA: https://enc.piano.or.jp/en/musics/23220 — secondary commentary describes ternary form, varied tonal regions, melody transferred to the left hand in the middle section, chromatic transition, and closing accelerando/rapid register sweep. These are **attributed secondary analytical assertions**, NOT independently verified bar-level findings.

## Existing repository and preferences cross-check
- Directly read studies 07/08 for Op.10 No.2, prior study 097, `research/chopin/code/chromatic_engine_v4.py`, and `feedback/USER_PREFERENCES.md`.
- v4 is an *original* 4/4, 32-sixteenth-per-two-bar chromatic contour experiment with harmony anchors only at selected grid points. It has **no score provenance, no independent voice event timeline, no nonchord-tone classification and no functional cadence/2-bar motif audit**. Its assertions in source are not newly executed in this run.
- The preferences emphasize smooth voice-leading, controlled chromatic inner lines, formal arc, and established harmony; these are design constraints, not evidence of Chopin's historical choices.
- Do not re-open Op.64 No.2: 097 explicitly closes it at 3/3.

## Original algorithmic proposal — NOT a transcription
Represent a waltz as independent structural layers, not a right-hand MIDI stream:
- `FormSection(id, tonal_center, thematic_role, cadence_goal, phrase_groups)`; allow A–B–A' as a **hypothesis** consistent with PTNA, pending first-edition score verification.
- `VoiceEvent(witness, bar, beat:Fraction, duration:Fraction, pitch_spelling, voice_id, role, tie, confidence)` and `HarmonySpan(start,end,function,bass_pc,pcs)`.
- The left-hand **role may transfer** from bass/accompaniment to principal melody in a contrasting section. When it does, the bass function must be reassigned to a distinct event stream or explicitly left absent; never silently force both roles onto the same attack.
- Build a 2-bar **structural** motive as contour/metrical accent/target-harmony/cadence intent; transformation operations include register transfer, rhythm displacement, changed accompaniment voicing, chromatic approach and cadential compression. Preserve a recognizable invariant while changing at least one structural dimension. A 3-note cell repeated unchanged is not development.
- For each sounding event, intersect its [onset,offset) with all harmony spans. A tie does not create a new attack but does create a new harmonic interpretation after a chord change. Label nonchord tones only with evidence: passing (stepwise motion between structural tones), neighbor (returns), suspension (prepared and tied across a harmonic change, resolving), appoggiatura (accented approach and resolution), anticipation, or UNKNOWN. UNKNOWN fails strict certification; intentional 9/11/13 must be specified as accepted chord extension.
- Generate **form/cadence → harmonic bass → role-bearing melody and counterline → 2-bar variation → accompaniment → ornaments → polyphonic audit**. Validate 3/4 as 3 quarter units per bar *per voice*, including rests, with rational tuplets; reject invalid overlaps, broken ties, uncontrolled low-register density and missing cadence goals.

## Falsifiable negative tests (specification only; NOT executed)
1. Same pitch under slur without tie = two attacks; under valid tie = one attack.
2. A tied note over a harmony change retains attack identity but requires new consonance/NCT evaluation.
3. Transfer melody to left hand while bass remains on same voice/onset with incompatible durations => reject or explicitly split voice identities.
4. 3/4 monophonic line with 13 sixteenths and no tuplets => reject.
5. Two-bar unchanged 3-note cell repeated mechanically => reject as developed motif; allow explicitly marked literal reprise.
6. Chromatic accented dissonance with no stepwise resolution cannot be auto-labeled passing tone.
7. End section without tonal/cadential closure cannot be silently marked closed.
8. Historical witness A vs edited witness Kullak must never be conflated; editorial marks remain provenance tagged.

## Critical self-audit / quality gate
**PARTIAL / NOT COMPLETE.** One **edited historical score image** was directly inspected (PDF p.9), not autograph or 1847 first edition. No first-edition pitch-by-pitch or bar-by-bar comparison, no source-critical variant collation, no new executable Python test, no integration into v4, and no musical quality evaluation. PTNA's middle-section left-hand melody and formal account remain secondary-source claims until independently located in score. Avoid asserting exact measure numbers, chord progressions or original pitches not directly checked. No user-facing MusicXML/PDF/audio generated.

**Next work-specific research allowance: 2/3, then 3/3 maximum**. Next time prioritize a verifiable 1847 witness and direct middle-section score image; implement and actually execute voice-transfer, NCT, and two-bar motif adversarial tests. If access fails, document failure and stop at 3/3 anyway.
