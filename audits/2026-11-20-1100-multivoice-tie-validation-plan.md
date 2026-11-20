# 2026-11-20 11:00 — Multi-voice tie validation specification

## Evidence and scope
Verified repository source: `audits/2026-11-20-1000-tie-onset-regression.md` (blob SHA `eb9da3e9a485044dbcfffd6628a0aaec24ec5621`). This source reports 4/4 synthetic single-voice onset tests passed, **not** multi-voice verification. The underlying fixture bytes and original v1.1 database ZIP were not independently inspected in this run. No historical Research original text or original score was recovered.

## Proposed rules — UNTESTED
1. Use a stable note identity: part ID, MusicXML voice ID, staff, sounding pitch (step/alter/octave after transpose), and tie chain. Do not merge same-pitch simultaneous notes in distinct voices.
2. In each part, interpret `backup` and `forward` in divisions; `chord` notes share onset with the preceding note in that voice; measure-local positions must respect measure duration and pickup handling.
3. Match a tie continuation only if the previous active note in the same logical voice/pitch has `tie type="start"` and the next has `tie type="stop"`; verify `notations/tied` when present. A tie continuation does not count as a fresh attack.
4. Record intervals as half-open `[start,end)` in rational quarter-note units, retaining original notation provenance. Grace notes, tuplets, repeats and cross-staff notation need explicit handling or an INDETERMINATE result.
5. For pairwise parallels, compare two successive genuine attacks in both voices at compatible harmonic instants. Sustained tones and asynchronous attacks are not automatically parallel-motion violations; report INDETERMINATE if onset alignment or voice identity is ambiguous.
6. Apply instrument transposition before interval comparison, particularly Cb sounding one octave below notation when so specified. Missing transposition metadata must not be silently treated as proof of concert pitch.
7. Distinguish exact unison, octave and compound octave; keep a separate interval-class view for pitch-class comparisons. Classical voice-leading restrictions are context-dependent, so report candidate violations for musical review.

## Required synthetic regression cases — NOT EXECUTED
- Two voices on one staff, same pitch with independent ties
- Cross-measure tied continuation in one voice while another rearticulates
- `backup` and `forward` with different note lengths
- Chord member tied while another chord tone changes
- Cb octave transposition plus tie
- Divisi voice crossing and asynchronous attacks
- Untied repeated pitch versus tied continuation
- Malformed unmatched tie stop (must flag)

## Research tracking
New recovered IDs: none. Inherited, **unverified** missing-ID list: 001–093 and 112–115 (97 total). No historical-ID mapping altered, no deduplication asserted. Score/source/bar: not applicable; this is an implementation specification, not analysis of a score.

## Next step
Obtain and inspect the latest ZIP and original Research source files; implement parser against actual fixture bytes; run the eight regression cases; only then promote proposed rules to verified implementation.
