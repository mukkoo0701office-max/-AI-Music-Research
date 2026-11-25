# Chopin Research 108 — Waltz Op.70 No.1 / WN42 — witness-aware rhythmic parsing and adversarial audit (PARTIAL 2/3)
Date: 2026-11-25 JST. **Cumulative study of this work: 2/3** (107=1/3, 108=2/3). Never exceed three runs. The earlier Op.10 No.2 study has already exceeded its cap and must not resume.

## Evidence ledger: observed vs inferred
- **Directly read repository**: research 107, research 106, research 08 and `research/chopin/code/waltz_event_audit.py`. The source-version claims in research 107 remain *hypotheses* until direct image collation.
- **OCVE browser** https://chopinonline.ac.uk/ocve/browse/acview/12fd2b9b9c0b2cc3619df0bd25922231/ was opened. The publicly rendered page exposed work filters and first-edition abbreviations, **not readable Op.70 No.1 notation**. Thus no notes, bar-specific rhythms or edition differences were directly verified here.
- **NIFC catalogue** https://chopin.nifc.pl/en/chopin/kompozycja/57_waltz-in-g-flat-major returned a JavaScript-only shell in this access route; it was **not** a directly inspected score.
- Prior 107 cites PTNA https://enc.piano.or.jp/en/musics/23223 for edition-specific dotted-note/pickup differences, but this run does not promote those secondary assertions to manuscript readings.
- **Primary-score gate FAILED**. No musical fact below is presented as an Op.70 No.1 note-by-note transcription.

## Code audit: defects reproduced by inspection, not runtime regression
`waltz_event_audit.py` uses `assert` for user-data validation (removed under `python -O`); a held event need only intersect *some* harmony, so a harmony gap can go unnoticed. It treats pitch class in a triadic set as an NCT classifier, disregarding extensions, spelling, accent, voice context and preparation/resolution. Its `two_bar_transform` accepts any one-field difference, even a superficial harmonic label change. It does not enforce an explicit complete harmony partition or source-version provenance per harmonic claim. These are source-code findings; no existing generator was modified in this run.

## ORIGINAL compositional model (not a claim about Chopin's actual bars)
Represent each source reading as `(work, witness_id, witness_type, edition_state, page, bar, staff, voice, onset:Fraction, duration:Fraction, spelled_pitch, attack, tie, image_verified)`. A manuscript copy is distinct from an autograph; a first edition is distinct from either. All claims of original pitches require `image_verified=True` with page reference. Unverified events may be used as synthetic test fixtures but never as primary evidence.

**Structural layer:** first assign a phrase-level harmonic itinerary and cadential destination; then map a two-bar motif with accent pattern, contour skeleton, bass goal, melodic register and role of each voice. Permit a contrasting section to reallocate roles and change density, rather than merely changing tempo. **Surface layer:** subdivide a selected anchor interval into 16ths/32nds with rational time, endpoint conservation and explicit passing/neighbor/appoggiatura/anticipation hypothesis; allow sparse texture and literal reprises. Avoid automatic fourfold three-note-cell replication.

**Transform gate:** a two-bar transformation requires (a) at least one audible invariant such as contour, metric stress or rhythmic cell, (b) at least one substantial musical change such as contour direction, onset-grouping or harmonic destination, and (c) preserved phrase-goal coherence. Changing witness metadata, chord-symbol spelling alone or one incidental note cannot pass. Literal reprise is explicitly flagged, never confused with development.

**NCT gate:** partition each sounding note at every harmony boundary *without inventing a new attack*. Determine whether the spelled note is a chord tone, accepted extension, or candidate NCT; only then classify passing/neighbor/suspension/appoggiatura with attack weight, prior preparation and next resolution. Return UNKNOWN for ambiguous harmony or unresolved voice assignment. A chordal ninth cannot be rejected simply because it is outside a root-position triad.

## Executable acceptance criteria for future implementation (NOT run)
1. `python -O` must reject the same invalid input as normal Python; use explicit ValueError/typed errors.
2. Reject gaps/overlaps in every voice and in the full harmony timeline, including last endpoint; preserve rests and tied continuation.
3. Preserve exact 3/4 duration with rational fractions, separately accounting for pickup and incomplete final bar; do not impose full-bar starts on anacrusis.
4. Reject changed-pitch ties and ties from rests; avoid counting a tie continuation as a new attack.
5. For an accented appoggiatura, require a context-dependent resolution; distinguish a prepared suspension across a changing harmony from a reattack.
6. Treat ninth as accepted extension only if explicitly admitted in the harmonic vocabulary; otherwise return UNKNOWN rather than asserting an NCT.
7. Reject two-bar changes consisting solely of edition labels or a single superficial token; permit tagged literal reprise.
8. Reject a supposed manuscript-vs-print variant lacking two independently verified source-image anchors.
9. Compare generation quality against phrase-goal, harmonic continuity and independent bass/inner-voice trajectories, not merely event counts.

## Critical verdict / handoff
**PARTIAL 2/3.** Primary notation was not directly accessible through the checked routes. No source-based musical discovery, code change, Python execution or score-fidelity regression is claimed. The output is a detailed *implementation specification and defect audit*, not a completed Chopin extraction. Final permitted study of Op.70 No.1 is 3/3; prioritize primary score-image access and one actually executed validator patch/test. After that, move to the next unstudied work regardless of quality. Keep existing hourly schedule. No fingering, practice, user-facing audio, MusicXML or PDF.
