# Chopin Research 077 — Waltz Op.18, study 1/3: source-witness form and generative grammar
Date: 2026-11-24. **Cumulative count: 1/3**. Next: Op.18 2/3, never exceed 3.
**Status: PARTIAL; primary score notes not independently verified.**

## Selection and previous-work check
The `research/chopin` directory listing (80 entries at read time) has no waltz study; preceding Op.25 No.12 records 074–076 explicitly close that work at 3/3 and hand off to waltzes. Op.10 No.2 studies 07/08 were directly read. The prior 076 record was directly read. This does not prove no waltz material elsewhere in the repository; the claim is limited to this research directory.
Op.18 is the first published waltz chosen as a stable, source-rich starting point, not a claim that it was Chopin's earliest composed waltz.

## Evidence register (facts vs unverified)
- **Catalogue directly checked:** Chopin Online OCVE Op.18 source listing: https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/5238e79031a187bcea1cd7bc57a24aa3/ . It lists autograph Stichvorlage A3, French first impression F1, corrected reprint F2, and page/bar coverage. A3 page 2 covers bars 1–34; F1 page 2 covers bars 1–33; their pagination differs. The catalogue is **not** a note-level verification.
- **Critical edition commentary checked as accessible text:** National Edition, Waltzes source commentary https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes_commentaries.pdf . It distinguishes early autograph AI (separate waltz-numbered sections corresponding to final-version bars 5–68, 69–116, 117–164; no coda), AII (closer to final version; no coda), final-version autograph A, and French first edition Ff1 (1834) based on A, corrected by Chopin. **Implication:** sections and coda cannot be assigned a universal formal status without a witness tag.
- **First-edition catalogue checked:** University of Chicago https://chopin.lib.uchicago.edu/chopin-catalog/descriptions/18.pdf identifies Paris Schlesinger 1599, Leipzig Breitkopf & Härtel 5545, London Wessel 1157 (1834). NIFC repository https://repozytorium.nifc.pl/islandora/walc-op-18-0 identifies a Schlesinger imprint and engraved pages 2–9.
- **NOT checked:** facsimile images at readable resolution, individual pitches, note durations, harmony, specific contrapuntal events, cadence locations, or whether every bar maps one-to-one across versions. Do not infer these from catalogue page ranges. No claims about the original work's exact chords are made here.

## Distinct compositional insight
The **witness-aware form generator** must be separated from the **waltz surface generator**. A source family can preserve a chain of dance-like episodes yet revise the grouping of episodes into one integrated work and append a coda. The formal change (episodic collection -> continuous larger-scale design) is supported by the National Edition's description of AI versus final A, but its detailed harmonic mechanics remain unverified. Thus a reusable algorithm can explicitly distinguish **episode inventory**, **ordering**, **transitions**, **reprise links**, and **coda policy**, rather than encoding 'ABA' or a fixed 8-bar repetition as the piece's verified structure.

### Original generative rules (NOT a Chopin transcription)
Inputs: `WitnessID`, `Episode(id, phrase_goal, harmonic_plan, motif, register, density)`, `Transition(source,target,bass_goal,voice_leading)`, `Cadence`, `CodaPolicy`.
1. Plan multi-episode trajectory and explicit long-range cadential destination before generating 3/4 accompaniment. Allow alternate form maps for distinct witnesses; never silently merge early and late versions.
2. Give each 2-bar unit a structural melody (anchors, tendency tones, cadence goal) and a separately specified bass trajectory; only then fill rhythmic ornaments. In an **original illustrative 3/4** pattern, bass may attack beat 1 and inner chord tones beats 2 and 3. This is a generic waltz design option, **not a verified transcription of Op.18**.
3. Transform a recurring motif across a pair of phrases by at least two nontrivial parameters (harmonic destination, contour apex, onset offset, register, phrase length, voice exchange). Exact reprise must have a formal label. Avoid the 3-note modulo-cell problem documented in Op.10 No.2 study 08.
4. Model harmonic windows independently from note attacks. Classify non-chord notes as **candidate** passing (stepwise same direction), neighbor (return), suspension (prepared, held through a harmonic boundary, resolved), appoggiatura (accented, resolved), anticipation or unknown. Chromatic passing motion is not automatically licensed by its contour: spelling, bass/harmony, metric stress and destination must also be checked.
5. Encode onset/duration using rational numbers, chord simultaneities as shared onsets, 16th/32nd ornament groups as subdivision after phrase anchors. Do not create a new chord merely because an ornament begins.
6. Score competing phrase variants on voice-leading continuity, cadence clarity, bass independence, non-chord-tone explanation, and motif transformation; retain evidence and explicit exception labels.

### Required test plan, not executed this run
- Witness IDs required for every source-grounded event; an absent image/pitch yields UNKNOWN rather than a fabricated fact.
- Every voice in a 3/4 bar sums to exactly three quarter-note units; simultaneous chord pitches do not add to duration.
- 2-bar transformation detection rejects exact modulo-cell repetition unless tagged as formal reprise.
- Held dissonance is re-evaluated at each harmony boundary, not merely at onset.
- Tests distinguish correctly resolved accented appoggiatura from unresolved accented chromatic note, and reject unsupported 'passing' labels.
- Regression must compare the generator with user-approved examples; these were **not retrieved** this run.

## Self-audit and unresolved items
**FAIL as completed source-grounded analysis:** source catalogues and critical commentary were read, but facsimile note images were not. The only historically grounded structural observation is the documented version difference in episode numbering/coda; the surface grammar above is a compositional hypothesis. No repository Python source was directly fetched in this run (07/08 document its weaknesses); no code was changed or executed, and no tests are claimed PASS. The user-approved corpus was not independently located. Next study should prioritize a legible F1 or autograph image, annotate a small passage with exact bar/page/witness, and test exceptions rather than restate generic rules. No fingering or practice, no output score/audio.
