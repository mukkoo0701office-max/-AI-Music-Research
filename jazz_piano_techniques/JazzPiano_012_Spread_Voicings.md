# Jazz Piano 012 — Spread / Open Voicings（開離配置）
研究日: 2026-11-22 | 累計研究回数: **1/3** | 状態: **暫定研究・一次演奏資料の直接照合未達／品質ゲート未達**

## 0. 重複・先行研究監査
GitHub Contents APIで jazz_piano_techniques ディレクトリを列挙し、012 Spreadマスターが存在しないことを確認。既存 006 Red Garland と 011 Clusters を直接取得。006の「RH固定オクターブ+内側完全5度」とは異なり、spreadは広い音域への配分という配置属性であり、特定のリズムや固定形を意味しない。011の二度密集も局所的な上声に共存しうる。既存研究の二重作成を避け、この012を以後の単一マスターとする。既存の高評価研究全件の比較は未完了。

## 1. 出典と証拠階層
- The Jazz Piano Site, “Open Chord Voicings (Spread Voicings)” https://www.thejazzpianosite.com/jazz-piano-lessons/jazz-chord-voicings/open-voicings/ （本文直接確認）。開離配置を1オクターブを超える音域に広げる配置と説明し、LH=根音+10度 / RH=5度+7度、LH=根音+7度 / RH=3度+5度の例を提示。
- PianoGroove, “Two-Handed Jazz Piano Voicings” https://www.pianogroove.com/jazz-piano-lessons/two-handed-chord-voicings/ （本文直接確認）。旋律先行、根音・5度を下、3度・7度を上に分ける配置を説明。
- Piano With Jonny, “Jazz Piano Comping With Two Hand Voicings” https://pianowithjonny.com/piano-lessons/jazz-piano-comping-with-two-hand-voicings/ （本文直接確認）。開離配置、drop2、blockの包含関係と相違を教育的に説明。
上記は現代の教育的二次資料であり、**1940–60年代の録音・歴史的採譜の一次証拠ではない**。具体的演奏家への逐音帰属をしない。作品候補：Bud Powell《All the Things You Are》、Red Garland《Billy Boy》、Bill Evansのバラード伴奏。ただし当該録音のspread配置・拍位置は未照合、現段階では作品例として確定しない。

## 2. 操作的定義と分類
実音の昇順列 P=(p0,…,pn) に対し span=max(P)-min(P)。この研究では **span>12半音**を「開離」候補とする。ただし音域の広さだけではジャズ的機能を保証しない。各音を {bass,guide,colour,melody,approach} にタグ付けし、和声・音域・リズムを別レイヤーで評価する。drop2/3はclose-positionからの特定変換であり、spreadの部分集合にすぎない。USTは上部の和音構造に関する分類であり、spreadと直交する。低音に単なる完全5度を積むだけで自動的にspreadの好例とはしない。

## 3. 具体的な独自生成例（歴史的採譜ではない）
C major の ii–V–I を以下の実音に配置する。
- Dm9: LH D3(50), C4(60) / RH F4(65), A4(69), E5(76)。音度=1,♭7,♭3,5,9。span=26。
- G13: LH G2(43), F3(53) / RH B3(59), E4(64), A4(69)。音度=1,♭7,3,13,9。span=26。5度は省略。
- Cmaj9: LH C3(48), B3(59) / RH E4(64), G4(67), D5(74)。音度=1,7,3,5,9。span=26。
この例は各コードの広がりを示すが、LH根音 D3→G2→C3 の跳躍、上声 E5→A4→D5 の大きな動きがある。**最小移動の優良例とは評価しない**。ii→VのF4→F3を同一声部の解決と呼ぶこともできない。ガイドトーンは Dm7のC→G7のB（半音下降）、G7のF→Cmaj7のE（半音下降）を、オクターブ移動・声部再割当と区別して監査する必要がある。

## 4. 和声機能・時間・誤用
- 根音を弾くソロピアノと、ベーシストが根音を担うアンサンブルで、同じspreadを無条件に使い回さない。前者は低音の和声識別、後者は低域衝突回避を優先。
- V7の3度/♭7の導音・下方解決は機能的要件。9/13などの色彩音は上声の旋律・解決先に従い、全コードで固定テンションを強制しない。
- リズムは独立パラメータ：旋律のロングトーン下の遅延内声、裏拍の短い上声応答、ベース先行の分散アタック、終止直前の密度縮退を区別する。全音を全拍同時に鳴らす固定パターンは避ける。これらは**生成上の設計案**であり特定録音のリズム記述ではない。
- 低音域の短2度/長2度の長時間持続、旋律直下の無目的な倍音衝突、ガイドトーンの省略、ベースとピアノLHの重複、開離を目的化した不自然な跳躍を減点する。低音の5度禁止は普遍的禁則ではなく、文脈依存の推奨として扱う。

## 5. 作編曲アルゴリズム仕様 v1
入力 `{key, chords:[root,quality,extensions,function], melody:[pitch,onset,duration], bass, ensemble, phrase, tension_curve, register_limits}`。
1. 旋律の構造音と非和声音の準備・解決先を確定し、強拍に保持すべき旋律音をトップに固定する。
2. 低音の担当を `piano_solo|bass_player|cello_cb` から決め、根音・3度・7度の機能を割当。低音の過密を避ける。
3. 和音ごとに和声音・許容テンションから候補集合を生成。span>12の候補を抽出し、ガイドトーン、旋律音、最低音の機能タグを保持。候補は同じpitch-class集合でも実音レジスターを変えて複数生成。
4. 各声の時間的連結を動的計画法で最適化。スコア `w1*guide_resolution + w2*melody_continuity + w3*voice_motion + w4*register_collision + w5*unresolved_nct + w6*rhythmic_monotony`。各項目は符号と正規化を明示して実装すること。共通音維持・半音解決は声部ID単位で検査し、集合間の最近傍距離だけで声部進行と称しない。
5. 弦6: Vn1=主旋律、Vn2=上部ガイド/色彩、Vn3=単純な持続・限定的移動、Va=内声半音解決、Vc=機能的低音と対旋律、Cb=必要時の根音補強。Cb欠員時はVcの低音を優先し上声の密度を縮小。divisiは明示し、各声部の可奏音域・弓替え・音価を別途監査。
6. 例外処理: 倚音・係留・経過音・裏コード・借用和音は和声ラベルと実音の解決先を別々に保持。意図的な衝突は `intentional_rub` とし、自動禁則で削除しない。
7. 出力メタデータ `{pitches,spellings,register,degree,role,voice_id,attack,release,function,resolution_target,source_status,unresolved}`。音響の良否は算術テストと独立。

## 6. 検証と自己監査
- 本稿の上記3例の音度・MIDI番号・spanは理論的に手計算した。**実行済み自動テストは0件**。コードを実行していないため全調検証済みとは主張しない。
- 未検証：一次録音/原譜の逐音照合、実際の作品内での拍位置、全12調の異名同音、声部ID付き自動生成器、ピアノ手の分担の実演可能性、弦6の実音域、音響評価、高評価研究の網羅的照合。
- 本稿は理論・アルゴリズム設計の**暫定記録**。一次資料品質ゲート未達のため完成扱いしない。
- 次回（2/3）では一次録音と公開転写を照合し、声部対応を保持した12調の正例/負例テストを実行する。3/3到達後は未解決点を引き継いで必ず次テーマへ移行する。演奏練習メニュー、ユーザー向け音源・譜面は作らない。
