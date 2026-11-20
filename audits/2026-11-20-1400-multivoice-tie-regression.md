# 2026-11-20 14:00 多声部タイ結合回帰試験

13:00版ZIP（222項目）を直接解析し、既存MusicXML6件と新規二声タイ合成譜1件を検査した。

| ケース | 音符要素 | 新規発音 | 判定 |
|---|---:|---:|---|
| forward_offset | 1 | 1 | 観測のみ |
| chord_shared_onset | 2 | 2 | PASS |
| cross_measure_tie | 1 | 1 | PASS |
| separate_voice_same_pitch | 2 | 2 | PASS |
| backup_voices | 2 | 2 | PASS |
| tie_two_measures | 2 | 1 | PASS |
| multivoice_ties | 4 | 2 | PASS |

期待値を明示した6件は一致。新規研究原文回収0件、原譜直接検証0件。元v1.1 ZIPは独立確認できない。未回収Research 001–093、112–115は従来報告の未照合情報。タイ処理は合成譜限定で、divisi・Cb移調・非同期発音を含む六声禁則検査には未統合。