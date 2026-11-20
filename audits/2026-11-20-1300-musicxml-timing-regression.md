# 2026-11-20 13:00 MusicXML timing regression

Source: locally accessible `composition_db_update_20261120_1200.zip` (212 entries). Original v1.1 and Research originals not independently verified.

Six synthetic MusicXML tests passed: backup two voices, forward offset, chord shared onset, separate voices same pitch, cross-measure raw timing, and a tie-start event fixture. These tests validate a limited event-time extractor, **not** tie merging or six-part counterpoint.

New original Research recovered: 0. Original score verified: 0. Unrecovered IDs 001–093 and 112–115 (97) are inherited unverified ledger claims. No existing research IDs were reassigned.

Artifacts produced locally: 13:00 updated ZIP, regression CSV, audit JSON, SQLite, operations Markdown, six fixture MusicXML files.

Next: tie-chain merging by part/voice/pitch, then event-based parallel fifth/octave checks across all 15 six-part pairs.
