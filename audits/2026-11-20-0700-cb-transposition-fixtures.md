# Cb transposition test — 2026-11-20 07:00 JST

Source: inherited 06:00 ZIP, verified ZIP integrity. Original v1.1 and Research originals not independently accessible.

Two synthetic MusicXML cases parsed: C4/G4 without transposition = 7 semitones; C4/G4 with Cb `<octave-change>-1</octave-change>` = C4/G3, 5 semitones. Both passed. These are **not** real score verifications or full six-part contrapuntal tests.

New Research originals: 0. Inherited unverified missing IDs: 001–093 and 112–115. No deduplication.

Implementation rule: resolve written pitches to sounding pitches using explicit transpose attributes before interval evaluation; preserve written and sounding pitches separately. Next: integrate into 15-pair six-part regression.
