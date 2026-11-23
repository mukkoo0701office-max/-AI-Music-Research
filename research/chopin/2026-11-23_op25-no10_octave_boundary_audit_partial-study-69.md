# Chopin Research 069 — Op.25 No.10, study 2/3: octave-event and boundary audit

Date: 2026-11-23. **PARTIAL / NOT SOURCE-VALIDATED**. Cumulative count **2/3**: research 068 is 1/3, this is 2/3. Next study may be 3/3 only, then advance to Op.25 No.11 irrespective of completeness. Repository code search for `op25-no10` returned no hits (not an exhaustive historical count); 068 was fetched directly.

## Provenance and limitations
- Directly read GitHub research 068, 067 and `research/chopin/code/chromatic_engine_v4.py`. Study 068 describes 067/065 and cites research 07/08 indirectly; **07/08 and user-approved examples were not independently fetched in this run**.
- Opened Online Chopin Variorum Edition catalogue https://chopinonline.ac.uk/ocve/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ on 2026-11-23. Its accessible HTML renders catalogue navigation and source-type key but **not legible manuscript note images**. Study 068's manuscript page/bar inventory (No.10 pages 28–32, bars 1–119) is an inherited locator, not verified pitch-level evidence in this run.
- **No Chopin pitch, chord, section boundary or nonchord-tone identification is claimed verified.** The following is original engineering design, not transcription or an attribution of precise compositional choices to Chopin.

## Direct code audit: why v4 is not a usable octave/phrase generator
- `contour(start,directions)` appends four semitone steps per direction; eight binary choices drive 32 serial pitches. It has neither simultaneous pitch sets nor per-voice events.
- `generate_pair` checks every fourth note against two original chord pitch-class sets, not every attack and held-note boundary; its local stepwise constraint does not audit harmony, NCT or structural two-bar development.
- `audit` verifies local semitone motion and pair junctions but lacks bass targets, voice identity, phrase roles, rhythmic durations, formal return, and user-approved exemplars. Its `PROGRESSION` is original, **not Op.25 No.10 harmony**.
- Do not treat v4's passing assertions as evidence for the compositional technique of the source work.

## Original compositional model (implementable contract)
1. **Hierarchy**: `FormSection(role, mode_plan, texture, harmonic_windows, cadence_goal, motif_invariants)` -> `Phrase(two_bar_role, apex, bass_goal, harmonic_path, density_curve)` -> `VoiceEvent(voice_id, onset:Fraction, release:Fraction, notated_duration:Fraction, spelled_pitches, articulation, tie_id, metric_weight)`. Store pitch spelling, not only MIDI numbers.
2. **Octave semantics**: a chordal octave is one simultaneous attack with two pitches 12 semitones apart; octave doubling is not two independent contrapuntal voices. A bass strand has its own events and harmonic arrival points. True independent octave strands must be evaluated separately for contrapuntal parallels.
3. **Boundary sweep**: for each harmony change `t`, inspect events satisfying `onset <= t < release`. A note released at `t` is inactive; a new event at `t` is active. Classify each pitch against both adjacent spelled harmonic contexts where sustained. Never infer suspension from a tie alone.
4. **NCT candidate rules**: PASSING needs same-voice previous/next pitches with directional steps; NEIGHBOR returns to previous pitch; SUSPENSION needs consonant preparation, carried sounding pitch into changed harmony and step resolution; APPOGGIATURA needs accented dissonance and resolution evidence. Unknown harmony, ambiguous voice, or absent neighbors => UNKNOWN, never PASS. Accented passing tones and unresolved expressive dissonances may require REVIEW rather than rejection.
5. **Subdivisions**: rational durations distinguish 16ths (1/16 whole), 32nds (1/32 whole), and triplet eighths (1/12 whole). Verify event/rest coverage per voice, actual tuplet ratios, ties and sounding releases; never conflate faster attack density with tempo increase.
6. **Development rather than 3-note looping**: declare motif invariant (rhythmic signature, interval class, contour or harmonic function), then vary at least two of accent pattern, bass arrival, contour apex, harmonic target, register, texture and attack grouping in each DEVELOPMENT two-bar unit. REPRISE is a distinct role and can intentionally repeat. Validate phrase-level goal arrival, not just edit distance.
7. **Formal contrast hypothesis**: an A–B–A′ graph is a design prototype, not verified source form. Require contrasting B texture and harmonic pacing, and a transformed return of an A invariant. Source score must determine whether this model actually fits Op.25 No.10.

## Executed synthetic regression (independent Python, NOT repository integration)
Python `fractions.Fraction` and immutable event dataclass were run locally on 2026-11-23. **Six assertions passed**:
1. two synthetic simultaneous octaves have exactly 12-semitone internal spans;
2. at time 1/2 the old octave is inactive and new octave active;
3. boundary sweep at 1/2 returns new octave and a sustained independent bass;
4. 32 events of 1/32 whole-note each total one whole note;
5. three triplet eighths (1/12 whole each) total one quarter;
6. bass released exactly at 3/4 is inactive at 3/4.
Synthetic test pitches (60,72), (62,74), (55) are **invented**, not Chopin notes. This tests interval arithmetic and half-open boundaries only, not harmonic/NCT accuracy or musical quality.

## Negative tests still required (NOT executed)
- A serialized octave masquerading as two attacks must fail.
- Two true independent voices in repeated parallel octaves must be flagged, but chordal doubling must not be falsely rejected.
- A tied pitch not prepared consonantly must not be labelled suspension.
- An unprepared accented chromatic event must not be automatically labelled passing.
- A note spanning a harmony change must be reassessed even if no new attack occurs.
- A 32nd/tuplet group exceeding its bar or missing rests must fail duration audit.
- A two-bar DEVELOPMENT segment copied with transposition alone must fail structural variation.
- A section B differing only in key but not texture/harmonic pacing must fail contrast gate.
- A bass copied from every octave attack without independent goals must be flagged.

## Self-criticism / next and final No.10 run
**PARTIAL / NOT COMPLETE**: score-image note-level verification, harmonic and formal analysis of actual Op.25 No.10, direct reread of research 07/08, user-approved exemplar comparison, production-code patch and integrated regression remain undone. The six executed synthetic assertions are not a Chopin-style validation. In 3/3, prioritize readable primary score image, actual evidence with witness/page/bar, and cross-check source claims; if inaccessible, close with explicit unknowns and move to Op.25 No.11. Never research No.10 a fourth time. No performance/fingering work, MP3, MusicXML or PDF output.
