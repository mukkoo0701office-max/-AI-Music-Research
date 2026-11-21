# Jazz Piano 003 — Bud Powell 型の省略和音とコンピング：第1次研究
- 研究日：2026-11-21
- **研究回数：1/3（このテーマの累計上限3回）**
- ステータス：**暫定研究／一次録音の逐音照合未完了**。理論上の構成音・オクターブ配置は内部JavaScriptで検査済み。歴史的実演の逐音転写とは区別。
- 前段：JazzPiano_001 Shell、JazzPiano_002 Rootless A/B（3/3、再研究禁止）、feedback/Feedback_001を参照。
- 本稿の「Bud Powell型」は特定録音の逐音再現ではなく、**右手の単旋律を妨げない、左手の低音・3度・7度を中心とした簡潔な機能提示**という、研究上の作曲モデル。特定の和音配置を本人固有の固定形と断定しない。

## ■ 今回のテーマ：バド・パウエル・ボイシング

### 1. 本質と音楽的役割
ビバップの右手は単旋律的な8分音符列、半音アプローチ、拍の先取り、動機の圧縮・拡大を担う。左手は毎拍4〜5音を埋めるのでなく、和声の輪郭を短いアクセントで提示し、ベースと競合しない。したがって「Bud Powellボイシング＝特定の固定4音コード」と捉えると歴史的にも作編曲的にも誤る。左手に根音＋10度（または根音＋7度）、3度＋7度などの省略形を採る場合があり、編成とテンポで密度を変える。**根音＋10度は低い根音と高い3度の音程配置であり、根音＋3度の密集配置とは音響が異なる**。

機能和声の推進力：iiの♭7がVの3に半音下降し、Vの♭7がIの3に半音下降する。一方で右手の旋律が同じガイドトーンを担うなら左手で省略可能。ルートレスA/Bとの違いは**和音の固定4声を常時置くことを要求しない**点。

### 2. 音度・配置・機能
| 種類 | 音度（低→高） | 用途と制約 |
|---|---|---|
| root + 10th | 1–10（=3のオクターブ上） | ベース不在や明示的な根音が必要な場面。広い間隔を保つ |
| root + ♭7 | 1–♭7 | 属機能を暗示、3rdを旋律または他声部に委ねる |
| guide-tone shell | 3–♭7 または ♭7–3 | ベース奏者がいる場合、機能を保って中低音域を空ける |
| three-note functional | 1–3–♭7 / 1–♭7–3 | 独奏・薄いテクスチャー。和音の質に応じて3/7を変える |
| rhythmic comping | silence → short chord → silence | 発音密度・音価・弱拍位置は旋律/ベース/ドラムとの対話で決定 |

注：上表は**一般化した生成用パレット**であり、各形の歴史的使用頻度は採譜による未検証。

### 3. Key C / F / E♭：具体的な実装用例（全て独自例）
**Key C（ii–V–I）**
- Dm7: LH D2–F3–C4 = 1–♭3–♭7。RH 旋律 E4–F4–A4（9–♭3–5、単なる候補）
- G7: LH G2–F3–B3 = 1–♭7–3。RH A4–Ab4–G4（9–♭9–1、クロマチックな緊張→解決の候補）
- Cmaj7: LH C2–E3–B3 = 1–3–7。RH D4–E4（9→3、倚音解決）
- 左手の下声はD2→G2→C2。中声F3→F3→E3（保持→半音下降）、上声C4→B3→B3（半音下降→保持）。中声と上声の対応は根音の跳躍とは別の論理。

**Key F**
- Gm7: LH G2–B♭3–F4 (1–♭3–♭7)
- C7: LH C2–B♭3–E4 (1–♭7–3)
- Fmaj7: LH F2–A3–E4 (1–3–7)
- 上声 F4→E4→E4、内声 B♭3→B♭3→A3。

**Key E♭**
- Fm7: LH F2–A♭3–E♭4 (1–♭3–♭7)
- B♭7: LH B♭2–A♭3–D4 (1–♭7–3)
- E♭maj7: LH E♭2–G3–D4 (1–3–7)
- 上声 E♭4→D4→D4、内声 A♭3→A♭3→G3。

**実際の両手演奏に関する留保**：LHで根音＋中声＋上声を同時に掴むと大きすぎる場合がある。これは**作編曲上のピッチ集合**であり、左手の単一同時打鍵を保証しない。実際のピアノでは根音をベース奏者へ委ねる、低音を先行打鍵する、右手に上声を移す等の再配分が必要。実演可能性は未検証。

### 4. リズムと作品分析
- 4/4の四分音符グリッド上で「全拍和音」を避け、休符・短いアクセント・先取り・遅らせを旋律の休止と対応させる。**コードの形だけではスウィングしない**。
- モデル例：1小節の右手旋律が拍1の裏から始まり、拍2–3に長い音価を持つ場合、LHは拍2裏の短い和音と拍4の休符を候補にする。これは作曲上の設計例でありPowell本人の実演譜例ではない。
- **《Celia》**（1949年録音）には旋律とソロ導入部の短い動機・高速な接続句の関係が論じられている。Tom Clearyの分析は旋律断片の再利用を具体的に指摘するが、本稿では録音の逐音採譜をしていない。
- **《Un Poco Loco》**（1951年録音）は反復オスティナート、上部構造的な和声、対照的なソロ部を含む。これは通常のii–V–Iシェルだけに還元できない重要な**例外**。ピアニストSteve Boudreauの分析にはCmaj7/Dmaj7重層や左手オスティナートが挙げられる。これらは二次分析として扱う。
- 本テーマの狙いは、これら作品を「Bud Powell＝いつも薄い左手」と単純化せず、**通常のコンピングと特殊なオスティナート/多調的表現を別の生成モードとしてモデル化**すること。

### 5. 作曲・編曲生成規則
```text
INPUT: harmony_timeline, melody_notes, bass_role, meter, tempo, texture_density
for each harmonic span:
  determine root, 3rd, 7th and function
  candidate_LH = [root+10th, root+7th, 3rd+7th, root+3rd+7th, REST]
  if bass_role == 'walking_bass': penalize low-root doubling
  if melody already supplies guide tone: permit LH to omit that tone
  if fast melodic activity: prefer REST or short sparse comping
  if melody rests: allow a brief harmonic answer
  score candidates by functional_clarity, register_separation,
       voice_leading_continuity, melodic_noninterference, rhythmic_conversation
  avoid identical comping attack pattern in every measure
  validate note spellings, pitch range, simultaneity and voice movement
OUTPUT: independent LH event timeline + RH melodic timeline + validation log
```
- **重要**：上記は設計仕様であり実装・実音テストは未完了。コンピングの発音タイミングをランダムにするだけではスウィングにならない。
- **構造展開**：2小節動機→応答→4小節終止の中で、右手の音域・リズム密度と左手の発音頻度を反比例させる。各フレーズ終止でガイドトーンを明瞭化する。メロディの単なるアルペジオ化を避け、9th起点・倚音→解決・反復動機の変形を用いる。

### 6. 弦楽6声への転用
- Cb（省略可能）= 低音根音/ウォーキング風pizz、Vc = ベースまたは対旋律、Va/Vn2 = ガイドトーン、Vn3 = 単純な共通音または休符、Vn1 = RH旋律。
- 左手の省略和音を**全員同時の持続和音に変換しない**。短い和声応答、pizzとarcoの切替、休符を使って右手相当の旋律を生かす。
- Vn3は全・二分・四分中心、細かな8分は例外。CbなしでもVcで低音機能を確保。
- ジャズ的な平行ブロック奏法と、独立対位法における平行5度/8度の禁則を区別し、旋律を妨げる重複を削除。

### 7. 検証ログ・出典・批判的監査
**GitHub直接照合**：
- `jazz_piano_techniques/JazzPiano_002_Rootless_AB_Voicings.md` の第3回（3/3）を読み、当該技法を再研究せず次テーマへ移行。
- `feedback/Feedback_001_Shizukana_Kitai_Piano_Jazz_Preferences.md` の「自然な機能和声・ガイドトーン・過剰な転調回避」と整合。
**理論検査**：Key C/F/E♭のLH 3声の音域・昇順・ガイドトーン対応をJavaScriptで実行。Cで中声 F3→F3→E3、上声 C4→B3→B3。FとE♭も同型の音度移動。これは**理論的なピッチ配置検査**であり、左手の可奏性、音響、史料との一致を保証しない。
**資料**：
1. Bud Powell 《Celia》1949録音に関する分析と旋律断片の参照：Tom Cleary, *The Quotable Bud Powell*, https://blog.uvm.edu/tgcleary/2024/07/09/bud-powell-bard-of-bebop/ （二次分析）
2. Steve Boudreau, *Bud Powell — Un Poco Loco*, https://steveboudreaumusic.com/what-s-new/blog/3409707/bud-powell-un-poco-loco （二次分析、譜例を含むページだが本稿では原録音と逐音比較していない）
3. Bud Powell《Un Poco Loco》初期盤の音源公開ページ https://www.youtube.com/watch?v=V3FAxA3SUug （原演奏へのリンクを確認したが、音声の直接採譜は**未実施**）
4. 《Celia》採譜動画 https://www.youtube.com/watch?v=rBjdxUW2cMc （第三者採譜、原演奏と照合未実施）
**未検証・重要な限界**：原録音の実音の直接採譜、出版原譜の小節照合、本人の左手音域の統計、3声の同時可奏性、具体的コンピングの拍位置、全12キーの異名同音、生成器実行。よって「史料検証済みのバド・パウエル奏法」とは称さない。
**批判的自己監査**：上記LH配置は3声が広範囲に散るため、実際の演奏モデルとしては不適切な場合がある。**次回は実演譜面/録音で左手の配置と拍位置を照合し、可奏な2声シェルと独奏用3声を明確に分離する**。歴史的な使用頻度の断定は保留。

### 8. 履歴・研究上限
- **第1回（2026-11-21）：1/3**。理論モデル・3調の配置検査・作品例・未検証事項を記録。
- 第2回は原録音/一次譜面照合、左手可奏性の再設計、拍位置の精査を優先。
- 第3回で最終監査。**3/3後は完成度にかかわらずドロップ2へ移行**し、残課題は引継ぎ欄へ。
