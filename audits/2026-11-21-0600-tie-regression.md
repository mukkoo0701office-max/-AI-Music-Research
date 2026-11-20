# 2026-11-21 06:00 JST — Tie regression audit

Source: 05:00 ZIP (302 entries); successor ZIP contains 308 entries. Parsed 41 MusicXML/XML files. ZIP CRC passed.

## Verified structural anomalies
- audits/20261120_1300/cross_measure_tie.musicxml: P1 voice 1 C4 tie start in measure 1 has no matching stop.
- audits/20261120_1500/tied_upper_no_reattack.musicxml: P2 voice 2 G4 tie start in measure 1 has no matching G4 stop; A4 tie stop in measure 2 has no matching A4 start.

Three structural anomalies across two files. Four synthetic regression fixtures passed: valid two-measure tie, valid three-measure continuation, invalid pitch mismatch, and orphan start.

## Limits
No Research originals recovered; no source scores verified. Original v1.1 ZIP not independently verified. Previously inherited unrecovered range 001–093 and 112–115 (97 IDs) is unverified. These checks do not establish musical contrapuntal correctness.

## Next
Implement expected-output timing tests for backup/forward/chord/tie, divisi and Cb sounding pitch; then validate all 15 six-part pairs.
