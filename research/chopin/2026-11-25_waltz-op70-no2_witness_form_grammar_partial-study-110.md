# Chopin Research 110 — Waltz Op.70 No.2 (study 1/3, PARTIAL)
Date 2026-11-25 JST. Prior Op.70 No.1 studies 107–109 exhausted 3/3. GitHub search for op70-no2 returned no existing records; 1/3 count is provisional pending full history enumeration.

## Sources and verification
- OCVE witness catalogue https://chopinonline.ac.uk/ocve/browse/acview/12fd2b9b9c0b2cc3619df0bd25922231/ lists five presentation autographs A1–A5 of Op.70 No.2, approximately 52 bars. This is catalogue metadata, NOT score-note inspection.
- Juilliard working manuscript catalogue https://juilliardmanuscriptcollection.org/waltz-for-piano-op-70-no-2-in-f-minor/ describes a circa 52-bar autograph, dated 1841, with four bars crossed out.
- NIFC presentation manuscript https://kolekcja.nifc.pl/object-mc-319 dated 10 December 1842.
- NIFC copy https://kolekcja.nifc.pl/object-d-107 documents A-section alternative endings and B without repeat, contrasting with expanded posthumous editions. This is catalogue-level evidence only.
- PTNA https://enc.piano.or.jp/en/musics/23224 describes an F-minor to A-flat-major two-part design and differing opening notes among witnesses. Its commentaries differ on dating; do not conflate date of composition with dates of witnesses.
- Facsimile bibliography https://ci.nii.ac.jp/ncid/BB26576056 records 2016 manuscript facsimile with Jim Samson commentary. Actual facsimile images NOT inspected.

## Reusable compositional algorithm (original proposal, not Chopin transcription)
1. WorkPlan: A minor-key region -> B relative-major region; specify phrase and cadence targets. Actual chord sequence and pitches remain UNKNOWN.
2. WitnessPlan: preserve witness_id, source_type, date_claim, page_anchor, opening_variant and repeat_graph independently; never merge source variants into a fictitious authoritative text.
3. PhrasePlan: two-bar motive represented by accent profile, directed contour, harmonic goal, duration, register and bass role. Transformation must preserve meaningful invariants and change audible material (rhythm, sequence, register, countervoice), not only metadata. Avoid repetitive three-note cells.
4. VoicePlan: independently planned bass and middle voice; label passing/neighbor/suspension/appoggiatura only after spelled harmony, metric stress, preparation and resolution have been checked. Otherwise label UNKNOWN.
5. Realization: rational beat arithmetic for sixteenth/thirty-second divisions, distinct attack vs held tone, exact ornament duration conservation.
6. EditionRealization: repeat and alternative-ending traversal belongs to a separate graph, not to the underlying invented compositional material.

## Validation design — NOT EXECUTED
Reject source-note claims without a page/witness anchor. Reject harmony gaps, voice-duration mismatch, tie pitch mismatch, and incorrect subdivision sums. Reject confident nonchord-tone labels without full voice-leading context. Reject metadata-only two-bar transformations. Compare distinct repeat-graph traversals without counting repeated A/B as new compositional sections.

## Critical audit / next action
Primary-score image not directly examined; no note-level original claims. Python code was not changed or executed; no generator integration or successful tests are claimed. Research07/08 and preferred output were not fetched in this run, so compatibility is UNVERIFIED. Next study (2/3) must inspect a witness score image and execute synthetic event tests. Quality gate: PARTIAL / NOT COMPLETED. No fingering or practice research.
