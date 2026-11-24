# Chopin Research 103 — Waltz Op.69 No.1 / WN47 — final permitted run (3/3), PARTIAL
Date: 2026-11-25 JST. **Cumulative 3/3**: repository studies 101 (1/3), 102 (2/3), this 103 (3/3). **Do not study Op.69 No.1 again** under the three-run cap. Next target: Op.69 No.2 unless repository history already counts three runs.

## Source and evidence boundary
- IMSLP Op.69 catalogue https://imslp.org/wiki/Waltzes,_Op.69_(Chopin,_Fr%C3%A9d%C3%A9ric) directly checked: composition year 1835 for No.1; French 1855 Meissonnier first print, plate J.M.3526, IMSLP #400818, 12 pp; it also lists a 1842 holograph manuscript (BnF MS-121), IMSLP #889451. The manuscript catalogue entry is a **new witness lead**, not evidence of any specific note reading. Witness relationship to the 1835 presentation autograph mentioned in 101 requires documentary verification.
- Attempt to open the 1855 PDF via IMSLP link was redirected to automated verification. **Neither 1855 notation nor 1842 manuscript notation was directly read.** No bar-specific pitches, NCTs, cadence positions or source-specific form claims are made.
- Repository 101 and 102 and existing `research/chopin/code/waltz_event_audit.py` were read. The old validator uses pitch-class membership only, weak five-field two-bar transform, asserts (disabled with -O), and does not enforce full harmony coverage.

## Novel executed synthetic regression (not Chopin score verification)
Independent Python script executed locally on 2026-11-25, **7 synthetic cases passed**:
1. contiguous 0–1 and 1–3 harmonic spans accepted;
2. gap 1–2 rejected;
3. overlap 1–2 rejected;
4. explicit initial rest + note + same-pitch tie accepted as one attack;
5. tie on rest rejected;
6. silent unencoded voice gap rejected;
7. changed-pitch tie rejected.
Test implementation uses `fractions.Fraction` and explicit `ValueError`, not `assert` for input validation. **The code was executed locally only; not integrated into the repository's generator.** These seven cases do not verify Chopin's notation or full NCT semantics.

## Reusable generative algorithm specification (original composition, NOT transcription)
1. Build a form/phrase graph with harmonic destination and bass arrival; store edition/witness IDs separately. Generate a melody skeleton with goal notes and rhythmic salience before adding ornamental subdivisions. Require actual source page/bar identifiers before importing observations as Chopin facts.
2. Represent each independent voice as contiguous rational-time events (including explicit rests). Track onset vs continuation. For a tie, same pitch and adjacent endpoint are necessary, but not sufficient for stylistic suspension.
3. Validate harmony intervals for complete, nonoverlapping coverage of the analyzed time range. Split *analytical assessment* of a sustained note at harmony changes without adding attacks. Missing harmony labels become explicit UNKNOWN; they must not silently disappear.
4. NCT classification uses spelled pitch, local harmonic vocabulary (including declared extensions), accent, previous/next structural tones, and direction of resolution. Passing/neighbor/suspension/appoggiatura/anticipation are **candidate labels**, never inferred solely from `pitch % 12`. A held consonance becoming dissonant at a harmony boundary is only a suspension candidate if preparation, continuation and resolution are all established. If multiple analyses remain plausible, retain ambiguity and its reason.
5. Two-bar motivic generation must compare rhythmic salience, melodic contour, structural intervals, harmonic direction and cadence goal; preserve at least two musically meaningful invariants, change one controlled dimension, and test the 4–8-bar phrase destination. Metadata-only changes cannot count as development. Reprise must be explicitly marked.
6. 16th/32nd subdivisions are selected to realize directed ornamental motion and controlled density while preserving phrase landmarks; verify exact duration sums, rests, tie continuity, voice crossing and unresolved accented dissonances. No source-specific claim about Op.69 No.1's use of these devices without direct score inspection.

## Critical quality assessment
**PARTIAL / FAIL primary-score gate.** The historical catalogue has been inspected, but both relevant score images remain uninspected. No bar-located note analysis, critical comparison, verified formal reading, or actual generator integration. Seven local synthetic tests validate only elementary temporal invariants; they are not a demonstration of musical style or high-quality composition. Existing repository code is unchanged. A later *different-work* study may reuse these generic validation rules; **do not schedule a fourth Op.69 No.1 study**. Prioritize direct score image reading and real-score evidence for Op.69 No.2.
