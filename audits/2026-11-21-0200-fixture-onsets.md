# 2026-11-21 02:00 JST — Fixture onset audit

Baseline: composition_db_update_20261121_0100.zip (285 entries, 41 XML files, 39 unique SHA-256).

## Verified
- Duplicate group: tests/parallel_fifths_fixture.musicxml = tests/fixtures_0700/parallel_fifths.musicxml.
- Duplicate group: audits/20261120_1500/staggered_onsets.musicxml = audits/20261120_1500/parallel_fifths.musicxml.
- Old staggered fixture: P1 onsets [0,1], P2 [0,1]; not asynchronous.
- Corrected fixture audits/20261120_1600/staggered_onsets_corrected.musicxml: P1 [0,1], P2 [0.5,2.0] in quarter-note units. **The previous report's second P2 onset of 1.5 was incorrect for this fixture.** Parser scope: simple synthetic fixtures; not general MusicXML timing.
- No new Research originals recovered; no original scores verified.
- Inherited missing-ID claim 001–093 and 112–115 (97) remains unverified; original v1.1 ZIP not independently inspected.

## Rules and next steps
Exclude the mislabeled 15:00 fixture from asynchronous tests; preserve history. Do not merge Research IDs on binary duplicate evidence. Build expectation-based six-part 15-pair tests covering ties, held notes, divisi, backup/forward, chords and sounding contrabass transposition.