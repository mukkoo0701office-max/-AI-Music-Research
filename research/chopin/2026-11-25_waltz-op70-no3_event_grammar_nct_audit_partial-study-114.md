# Chopin Research 114 — Waltz Op.70 No.3, study 2/3 — role-exchange event grammar (PARTIAL)
Date: 2026-11-25 JST. Target count **2/3** based on preceding Research 113 (1/3) and directory history examined; exhaustive deleted/renamed-history verification not established. Next run may study this work once more, then must move on regardless of quality. Op.10 No.2 and Op.70 No.1/2 are closed (>3, 3, 3 respectively).

## Source hierarchy and actual verification
- First French edition (Paris, Meissonnier, plate J.M.3527, ca.1855), IMSLP item #399505: https://imslp.org/wiki/Waltzes,_Op.70_(Chopin,_Fr%C3%A9d%C3%A9ric). **Catalogue entry inspected, score pages NOT inspected**. First German edition (Schlesinger, plate S.4396, 1855), IMSLP #447391 likewise identified but not inspected. These are *posthumous edition witnesses*, not extant Chopin autograph.
- Morgan Library first French edition catalogue https://www.themorgan.org/music-manuscripts-and-printed-music/133064 : identifies French first edition and absence of Fontana preface/portrait in its copy. Bibliographic metadata, not a note-level comparison.
- NIFC https://chopin.nifc.pl/en/chopin/kompozycja/26_waltz-in-d-flat-major : description of subtle counterpoint, dense thirds/fifths/sixths, and prominent low trio melody. Scholarly description, **not verified measure-by-measure**.
- National Edition Waltzes B commentary https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes-B_commentaries_poprawka2020.pdf : preceding study 113 records lost autographs and dependence on posthumous editions. No claim of direct manuscript inspection.
- University of Glasgow thesis https://theses.gla.ac.uk/83309/1/2022MonteiroMPhil.pdf lists French first edition July 1855 as source witness.
- Repo studies 07, 08 and `research/chopin/code/waltz_event_audit_v2.py` were read for comparison. Research 113 was also read. No user-approved example score was verified in this run.

**Strict boundary:** No original Chopin note pitch, bar index, melodic interval, voice-leading event or detailed A/B/C form has been directly verified against score images in this study. Everything below is an **original, testable composition design**, motivated by the descriptions, NOT an extraction of particular score notes.

## Defect inventory carried from prior research
Research 07: independent clocks for fast/medium/bass voices, but no NCT function audit. Research 08: 3-note repeated cell, no two-bar real-event sequence. Existing `waltz_event_audit_v2.py`: integer pitch only, tie_prev but no outgoing tie, consonance boolean only, motif comparison uses abstract metadata and not musical events. Study 113: role-transfer proposal without execution. Avoid claiming these deficiencies solved merely by documentation.

## Event-level generative architecture (original)
Represent every note/rest as `(witness,section,bar,voice,onset_q,duration_q,spelled_pitch,attack,tie_in,tie_out,accent,role,source_status)`. Use exact rational quarter-beat times. 3/4 bar length=3; sixteenth=1/4; thirty-second=1/8; tuplets must carry their own rational ratios. A witness identifier is compulsory for source-derived facts, and `source_status` one of `verified_score / secondary_report / synthetic / unresolved`.

1. **Global phrase plan:** choose harmonic goal and cadence, bass trajectory, and foreground voice per section. Never infer section limits or key of contrasting episode from catalogue prose alone. Preserve a foreground contour and cadence goal across 2-bar units while allowing voice transfer between registers at a formal boundary.
2. **Two-bar grammar:** plan 6 quarter-beats, chord intervals, two anchor attacks and one cadence-directed destination. Create an identifiable rhythm/contour signature from actual note events (interval signs, inter-onset durations, metrical accent positions); transform a subsequent two-bar span by rhythmic augmentation, register shift, contour inversion, harmonic recontextualization or countervoice imitation. Reject if only labels differ or if neither invariant nor audible transformation exists.
3. **Voice-role exchange:** a low melodic voice is classified by phrase continuity, nontrivial directional motion, independent accent/duration, and cadence participation; do not classify every bass note as harmonic root. Upper voices may take chordal/offbeat roles, but voice independence must be checked by event time and actual pitches. Register transfer is a structural decision, not an arbitrary octave swap.
4. **Dissonance audit:** for each attacked note intersect active harmony, classify `CHORD / PASSING / NEIGHBOR / SUSPENSION / APPOGGIATURA / ANTICIPATION / OTHER / AMBIGUOUS`. For PASSING require neighboring consonant anchors and stepwise motion in same direction; NEIGHBOR requires return to anchor; SUSPENSION requires same spelled pitch prepared by tie or continuation, dissonance on stronger position, subsequent stepwise resolution, and no new attack at tie. APPOGGIATURA requires accented dissonant attack resolving by step; ANTICIPATION requires next-harmony chord tone before boundary. A single pitch-class membership flag cannot prove a category; use AMBIGUOUS when harmonic spelling, voice continuity or metric strength is unknown. Exceptions for chromatic passing and delayed resolutions must be explicitly annotated and inspected, not silently accepted.
5. **Vertical audit:** inspect every attack and harmonic change, including sustained notes, for dissonance, registral collision, unintended parallel perfect intervals between structural outer voices, and voice crossings. Parallel intervals are context-sensitive warnings, not unconditional rejection; distinguish structural notes from embellishments.
6. **Texture density:** place 16ths/32nds only where they develop the phrase or lead to anchors, not by uniform subdivision. Reject monotonous identical 3-note cells over multiple bars unless an explicit structural repetition objective is present. Respect all per-voice event tiling, rests, and tie continuation across barlines.

## Test matrix (DESIGNED, NOT EXECUTED)
- T1: voice with low 2-quarter melodic sustain + two eighth-note steps is foreground when cadence-directed, even with upper offbeat chords.
- T2: two 2-bar event sequences identical except metadata => REJECT transformation.
- T3: two sequences preserve rhythmic accent signature and change register plus cadence destination => ACCEPT only if actual pitches and event times support it.
- T4: tie_in without preceding tie_out, or changed enharmonic spelling => REJECT; same-pitch, reciprocal tie across bar => ACCEPT.
- T5: dissonant note with missing resolution => AMBIGUOUS/REJECT asserted suspension, never PASS.
- T6: 3/4 voice total exactly 3 quarter beats with 1/8 durations => PASS; gap, overlap, or 1/8 overrun => REJECT.
- T7: harmony change during a sustained pitch triggers a fresh NCT assessment without creating a false reattack.
- T8: source claim without edition/page/system/bar evidence => UNVERIFIED, cannot be published as score fact.
- T9: chord-only root bass with no melodic continuity must not be promoted to trio foreground merely by low register.
- T10: two adjacent identical 3-note cells with no phrase justification flagged for repetition review.

## Critical self-audit / blockers
**Quality gate NOT MET**: first-edition score pixels not read; note-by-note comparison absent; no code modified or run; tests above are specifications only; production generator integration absent. Cannot certify original work's contrapuntal intervals, harmonic rhythm, precise formal design, or motivic transformation. Previous claims of 'high-quality completion' must not be inferred from a list of proposed validators.

## Next and final permitted study (3/3)
Try direct first French/German first-edition page inspection with exact page/system/bar references. If accessible, verify a limited, sharply defined excerpt of upper/inner/lower-voice role transfer; implement and actually execute a standalone regression suite for tie reciprocity, event-derived motif transform, and NCT uncertainty. If inaccessible, document failure and close the work at 3/3 without inventing pitches. Then proceed to next eligible work, respecting history and the original Etudes > Waltzes > Nocturnes priority. No user-facing media or performance-practice research.
