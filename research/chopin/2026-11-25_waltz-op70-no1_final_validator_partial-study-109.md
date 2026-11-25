# Chopin Research 109 — Waltz Op.70 No.1, FINAL 3/3 (partial, primary-score gate failed)
Date: 2026-11-25 JST. Cumulative count **3/3**: research 107, 108, 109. **Never study Op.70 No.1 a fourth time**; advance to the next unstudied work. This final entry closes the work despite outstanding defects.

## Evidence and provenance
- Read existing research 107 and 108 and `research/chopin/code/waltz_event_audit.py` directly from GitHub. Previous work already documents source catalogues: [OCVE](https://chopinonline.ac.uk/ocve/browse/acview/12fd2b9b9c0b2cc3619df0bd25922231/), [NIFC](https://chopin.nifc.pl/en/chopin/kompozycja/57_waltz-in-g-flat-major), [PTNA](https://enc.piano.or.jp/en/musics/23223), [IMSLP](https://imslp.org/wiki/Waltzes_Op.70_%28Chopin%2C_Frederic%29).
- **No original score page was inspected note by note in this run**. Therefore manuscript-specific rhythm, melody, bass, voice leading and edition differences remain hypotheses, not verified primary evidence. No new Chopin-specific pitch or bar claim is made.
- Source-code inspection confirms the old validator used `assert` for input validation, allowed harmony gaps and one-field metadata-only motif changes. These are code-level observations, not claims about Chopin.

## Implemented original validator
Added [waltz_event_audit_v2.py](code/waltz_event_audit_v2.py), an independent synthetic validator, without modifying the existing generator.
1. Uses explicit `ValueError` rather than `assert` for invalid events and harmonic timelines, including continuity and endpoint validation.
2. Maintains exact rational event durations, voice continuity and explicit rest events; rejects overlapping, missing, empty-witness, and out-of-range events.
3. Validates ties for pitch continuity and predecessor presence, and counts continuation as no new attack.
4. Splits held-note assessment at harmony boundaries without creating attacks.
5. Requires a two-bar transformation to retain a musical invariant and change at least two musical dimensions; metadata-only variants fail. Literal reprise must be explicitly tagged.
6. Parameterized start/end permits pickups or partial bars if the caller provides the correct span. It does **not** infer witness-specific pickups.

## Execution record
Executed locally in CPython both `python waltz_event_audit_v2.py` and `python -O waltz_event_audit_v2.py`. Both returned `PASS: 12 synthetic cases` (one valid case, seven invalid cases, four transformation assertions). These checks exercise synthetic fixtures **only**, not original notation or full integration. The code's test harness still uses asserts for its *own expected outcomes*, while production input validation uses explicit errors.

## Critical audit / remaining defects
- The `pcs` boolean is **not** a valid nonchord-tone classifier: ninths, spelling, voice function, metric accent, preparation and resolution are unmodeled. Do not label a false boolean as a proven NCT; `UNKNOWN` is required for musical classification.
- `two_bar_transform` uses coarse feature counts and cannot verify phrase-goal coherence, genuine melodic transformation or meaningful structural invariants. It can pass musically weak variations.
- Rest/tie, source provenance and harmony assessment are simplified; no per-event source-image anchor, multiple simultaneous pitches within one voice, tuplets, notated ornaments, 16th/32nd density audit, or complete multivoice counterpoint verification.
- No manuscript or first-edition score image was directly collated; no source-fidelity regression. The existing production generator was not changed.
- The former 107–108 rhythm hypotheses about editions remain unverified and must not be promoted to facts.

## Algorithmic handoff (not executed)
Use phrase/cadence goals -> voice-role and bass plan -> two-bar structural motif -> source-aware ornament/density realization. Only then classify each note by spelled harmony, admitted extensions, metrical stress, preparation/resolution and voice context. Unknown or unverified source readings must remain `UNKNOWN`. Preserve source witness IDs and image anchors independently; compare actual editions only after image inspection. Test 16th/32nd subdivision with rational conservation and accented appoggiatura/suspension behavior, not mere event counts. Apply this reusable infrastructure in **the next work**, never as a fourth Op.70 No.1 run.

## Quality gate
**PARTIAL / NOT COMPLETED** as a Chopin primary-score study. Genuine improvement: independently executed synthetic validation and a committed reusable code module. Primary-source score gate, musical NCT analysis, production integration and Chopin-based validation all FAILED or remain UNTESTED. No fingering, practice, user-facing audio, PDF or MusicXML production.
