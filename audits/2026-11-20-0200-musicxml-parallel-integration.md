# MusicXML parallel-motion fixture audit — 2026-11-20 02:00 JST

Source: composition_db_update_20261120_0100.zip, tests/fixtures_0700/*.musicxml.

Six synthetic two-part cases parsed directly from MusicXML:
- parallel_fifths: P5 detected, pass
- parallel_octaves: P8 detected, pass
- parallel_thirds: no violation, pass
- oblique_fifths: no violation, pass
- contrary_fifths: no violation, pass
- parallel_unisons: P8-equivalent detected, pass

All six expected classifications matched. Implementation compares simultaneous two-voice pitch transitions; both voices must move in the same direction and retain a perfect interval class (0 or 7 semitones). Unisons and octaves currently share the P8 class. This is a fixture-only test, not validation of complete six-part MusicXML, ties, divisi, asynchronous onsets, or score-level voice leading.

New recovered research originals: none. Score verification: none. Previously recorded missing IDs 001–093 and 112–115 are inherited, not independently checked. Original v1.1 baseline not independently accessed.

Next: asynchronous/divisi integration and source recovery.