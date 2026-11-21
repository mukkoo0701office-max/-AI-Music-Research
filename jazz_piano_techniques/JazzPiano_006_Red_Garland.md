# JazzPiano_006 — Red Garland: block chords and approach voicings (1/3)

## 研究対象と一次資料への距離
Red Garlandの特徴的な奏法を、**右手の旋律オクターブ＋内側の完全5度（下側の旋律音から完全5度上）**、**左手の中音域ルートレス4声**、**両手のリズム同期**として分離して扱う。これは一般的な4-way-close/Shearing型locked-handsと同一ではない。

参考文献：
- Riccardo Scivales, “Billy Boy and Red Garland's block chords style” https://www.riccardoscivales.com/billy-boy-red-garlands-block-chords-style/ — 転写に基づく説明。右手オクターブ＋内部完全5度、左手ルートレス、両手同期、内部音がコード外音となる場合を記述。
- John Valerio, *Jazz Journey: A Guide for Listening*, p.264, preview https://cognella-titles-sneakpreviews.s3-us-west-2.amazonaws.com/81208-1B-URT/Valerio_SP.pdf — 単音線から厚いブロックコードへの対比と左手ルートレスの歴史的文脈。
- Mark Levine, *The Jazz Piano Book*, ch.7, https://moodle.cegepsherbrooke.qc.ca/pluginfile.php/108871/mod_folder/content/0/Jazz%20Piano%20Book%20By%20Mark%20Levine.pdf?forcedownload=1 — ルートレス左手の一般的原理。Garland独自のリズム／音色をこれだけで証明できない。
- https://files01.core.ac.uk/download/pdf/161953202.pdf — 学位論文のRed Garland節、構造と非和声音の言及。

**方法上の制約**：今回、原録音を聴取して新規に採譜したわけではない。転写研究と教育文献の記述を照合し、独自の試験モデルを実装した。歴史的な「常に／必ず」の断定は避ける。

## 1. 構造と響きの機能
右手メロディのMIDI番号をmとすると、原型はRH=(m−12,m−5,m)。中声は下の旋律音から完全5度、上の旋律音から完全4度下。旋律が半音上行すれば右手3音を同じく半音上行させる。**コードの構成音を毎回再選択するのでなく、形状の連続性が優先**されるため、右手中声がその時のコード外音になる場合がある。こうした一時的なrubを、強拍の構造的な不協和と弱拍のアプローチで区別する必要がある。

左手は3rd・7th・9th・13thを含み得る中音域のルートレス和音。コードの根音と機能を左手だけで完結させる必要はないが、ソロピアノでは別途ベース音を設計しなければ和声の曖昧さが増す。

## 2. オリジナルのii–V–Iモデル（E♭ major）
Fm9: LH A♭3–C4–E♭4–G4（56,60,63,67）
B♭13: LH A♭3–C4–D4–G4（56,60,62,67）
E♭maj9: LH G3–B♭3–D4–F4（55,58,62,65）

右手はそれぞれ3音の独自試験旋律を使い、各音をオクターブ＋5度で厚くする。LHのFm9→B♭13ではA♭、C、Gの3声が共通でE♭→Dが半音下降し、ドミナントの3rdを準備。B♭13→E♭maj9ではA♭→G、C→B♭、D保持、G→Fで進む。**3rd/7thの機能的進行と共通音**を先に設計した。

## 3. Python実行検証
コード `jazz_piano_techniques/code/red_garland_006_v1.py` を実行。
- 3和音×3旋律音＝**9アタック**。
- 全9アタックで右手のオクターブと内部完全5度、左手4音の異なるpitch class、両手の音域分離をassertで検証しPASS。
- 実装した単純な音域上の隣接半音検出は**0件**。これはすべての和声的衝突がないことを意味しない。異なるオクターブのpitch class上の♭9などは別途監査が必要。
- 初回テストでは右手が低すぎてLHと重なり、assert失敗。右手を1オクターブ上げて再試験しPASS。**音域分離は音楽的に必要な条件**として明文化。

## 4. アプローチ研究の次の課題
1. 弱拍の旋律クロマチック・アプローチ時、RHの全3音を並行移動する場合と、内声のみ半音接近させる場合を区別。
2. ガイドトーンの係留・半音解決を、LH和音ごとではなくアタックごとに監査。
3. 右手中声のコード外音を「一時的rub」「拍をまたぐ未解決」「意図的な色彩」に分類し、時間・音域・音量を加えた指標を設計。
4. ソロピアノの低音・ペダル・休符を別レイヤーに設計し、7音を常時同時発音する単調な音楽を避ける。
5. 史料の説明と、独自アルゴリズムの出力を混同しない。

**進捗 1/3。次回2/3は経過和音とクロマチック・アプローチの声部解決を実装する。**
