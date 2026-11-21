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


## 9. 第二次研究（累計2/3）：Levine原典譜例の直接照合と「可奏な二音」へのモデル改訂（2026-11-21）

### 9.1 検証対象・一次/二次資料の区別
**直接確認した資料**：Mark Levine, *The Jazz Piano Book* (Sher Music, 1989), Chapter 17, pp.160–165。公開閲覧可能な書籍PDFの第17章本文と図17-16〜17-24の掲載位置・説明を直接照合した（譜例そのものの全音符逐音採譜は未実施）。これは**著者の出版教則原典**であり、Powell本人の1940〜50年代の録音という意味での一次演奏資料ではない。著作権のある譜例を転載せず、以下は独自の機能モデルを示す。
- 書籍本文は、Bud Powell型を「通常2音、ときに3音」「主にroot/3rd(10th)/6th/7th」と明示。旧稿の**root+3rd+7thの3声を代表形とみなす方向は過度に一般化していた**。本改訂では2音をデフォルトとする。
- 図17-16は《Ain't Misbehavin'》冒頭の**歴史的奏法を模した編曲例**、図17-17〜19はKey FのGm7–C7–Fmaj7を同じRHビバップ旋律で異なるLH配置にした**著者の例**。これを「Powellの特定録音を採譜した音」と取り違えない。
- 図17-22〜24は《Confirmation》冒頭8小節をstride/Powell型/混合型で対照する**教則上の比較**。音数だけでなく、LHの役割と和声リズムが変化する。
- 同章はPowell型LHの低い配置がRHの中音域旋律を開放する利点を挙げる一方、現代型ルートレスとの併用を認める。つまり**二音固定が絶対規則ではない**。
- Levine本文は《Hallucinations》《Oh So Basal》などを聴取資料として指示するが、**本研究では原盤を逐音聴取・転写していない**。
原典: https://www.redemption-church.com/worship/Songs/Real%20books/Other%20stuff/Sheet%20Music%20-%20The%20Jazz%20Piano%20Book.pdf （pp.160–165、特に162–165）。
補助史料（学術研究、原録音ではない）: *Miles Davis: The Road to Modal Jazz*（UNT所蔵学位論文、pp.6–7）はPowellの左手を短いシンコペーションのアクセント、2〜4音の変動と記述。https://digital.library.unt.edu/ark:/67531/metadc3693/m2/1/high_res_d/thesis.pdf

### 9.2 第1回の実装上の誤りを訂正
旧稿のLH D2–F3–C4、G2–B♭3–F4等は、同時打鍵なら最外音間隔が2オクターブ前後あり、通常の一手での同時発音を前提にできない。これは**一人の左手コンピングのサンプルとして不適切**だった。
修正：
1. **2音LHを標準候補**とする。根音+♭7、根音+3、根音+10th（10thは一手同時を強制しない）、必要時に3rd+7th。
2. 根音とガイドトーンを**別時刻**にする場合は同時和音として数えない。
3. 3声以上の同時配置は最外音域と内部の混雑を別途検査する。12半音以下を今回の**保守的な機械的閾値**とするが、これは演奏家の実測データでも歴史的規則でもない。
4. ベーシストがrootを示していても、LHのrootを常に禁止しない。重複が音響・リズム上問題になるときに回避する。

### 9.3 二音の作編曲用モデル（独自例、下から順に）
**Key C, ii–V–I：**
- Dm7: LH D3–C4 = 1–♭7（2音、短7度）。RHはF4（♭3）等で和音の質を補える。
- G7: LH G2–F3 = 1–♭7（2音、短7度）。RHはB3（3rd）等を担う。
- Cmaj7: LH C3–B3 = 1–7（2音、長7度）。RHはE4（3rd）等を担う。
この例では**rootが跳躍**し、ガイドトーンも必ず半音でつながるわけではない。これを失敗と即断せず、右手旋律との総合的な機能連結を評価する。前稿の「F3→F3→E3、C4→B3→B3」は**3声の理想化モデル**であって、歴史的Powell型2声の代表的実演データではない。

**Key F：**
- Gm7 LH G2–F3 (1–♭7)、C7 LH C3–B♭3 (1–♭7)、Fmaj7 LH F2–E3 (1–7)。
**Key E♭：**
- Fm7 LH F2–E♭3 (1–♭7)、B♭7 LH B♭2–A♭3 (1–♭7)、E♭maj7 LH E♭2–D3 (1–7)。
上記3調は全て独自の機能例。メロディが3rdを示さない場合、**root+7thだけでは長短や属機能を十分確定できない**。3rdをRH、別の楽器、または次の発音に必ず割り当てる機能監査が必要。

**ガイドトーン優先の別モード（ベースあり、Key C）**：
- Dm7 LH F3–C4 (♭3–♭7)
- G7 LH F3–B3 (♭7–3)
- Cmaj7 LH E3–B3 (3–7)
これはrootless guide-tone shellの独自例。**歴史的なBud Powell型の典型を保証するものではなく、編曲上の機能最適化モード**として別ラベルを付ける。ii→VではF保持/C→B半音、V→IではF→E半音/B保持。低音は別楽器D2→G2→C2。

### 9.4 リズム生成はLHとRHの対話で決める
- Powell型の核心はLHを「拍の常時刻み」から解放する点。**音数の少なさだけではビバップにならない**。
- 各2小節でRHのフレーズ開始・頂点・休止・終止を抽出。LHの発音候補は(1)和声の転換、(2)RHの休符に対する応答、(3)先取りの短いアクセント。全拍一律の固定発音は禁止する。
- ベースがウォーキングを続ける場面ではLHの低いrootの同時重複を減点。ベースが休止する場合にはLHのrootを加点。
- 「シンコペーション」は弱拍の発音/強拍の休止と関係するが、具体的なPowell本人の拍位置分布をこの研究では測定していない。

### 9.5 再利用可能な生成アルゴリズム v2（設計仕様）
```text
INPUT: chord timeline, RH melody notes/onsets/rests, bass events, meter, register
for each harmonic segment:
  identify harmonic function, third, seventh, root
  choose MODE from {ROOT_SHELL, GUIDE_SHELL, ROLL_OR_SPLIT, SPECIAL_OSTINATO}
  ROOT_SHELL: candidates = {root+third, root+seventh, root+tenth}
  GUIDE_SHELL: candidates = {third+seventh} with root elsewhere
  if RH or ensemble does not supply chord third: require its event in harmonic span
  if root+tenth exceeds LH simultaneous span threshold: mark split/rolled, not block chord
  evaluate LH attack times against RH activity and bass events
  penalize persistent LH/RH collisions, low clusters, repeated metrical templates
  prefer functional voice continuity; allow deliberate root jumps and LH silence
  if ostinato/bitonality: require separate source-supported structural plan
VALIDATE: note spelling, simultaneity, hand-span, functional completeness across ensemble,
          melody/bass interaction, rhythmic variety, provenance
OUTPUT: LH event plan, RH line plan, role assignments, confidence/validation log
```
**未実装**。音域とリズムの最適化重みは未校正。ハードな3rd必須制約はsus/ペダル/意図的曖昧さに例外を設ける。

### 9.6 弦楽6声へ：同時音数ではなく役割を転写
- Vn1: RHの単旋律・動機。9th開始/倚音の解決とフレーズ呼吸を保持。
- Vn2/Va: LHの3rd/7th機能を分散。LHの短いコンピングは**必要な時だけ**和声応答に変換する。
- Vn3: 共通音の持続または休符（4分以上中心）。全拍の刻みにしない。
- Vc: ベースまたは対旋律。Cbが不在なら根音機能を担当。
- Cb: 任意のpizz根音/ウォーキング。Vcとユニゾンを常時重複しない。
- **禁則**：持続内声の平行5/8、短9度衝突、ガイドトーンの解決を別監査。ジャズ的意図的平行ブロックと古典的独立声部は区別する。

### 9.7 実行済みテストと品質ゲート
今回、Key C/F/E♭の各3和音の二音モデルについてMIDI音高差をJavaScriptで計算し、最外音が11半音以下、2音であることを検査した（**9/9通過**）。ただし、この閾値は「二音の同時距離」のみであり、運指・実演音響・全12調・作品譜例の逐音照合を意味しない。
- **直接確認済み**: Levine原典書籍PDFの章本文・譜例配置・出典、GitHubの本マスター第1回、Rootless A/B第3回、Feedback_001。
- **二次資料のみ**: UNT論文によるリズム/歴史の解説。直接原録音の聴取/採譜は未実施。
- **未検証**: 図17-16〜24の全音符の逐音転写、Powell本人の録音と譜例の照合、個別曲でのLH発音時刻の統計、生成アルゴリズム実行、弦6の音響、全12調の異名同音。
- **自己監査**: 原典を読んだことで「Bud Powell型＝root+3rd+7thの広い同時3音」という第1回の偏りを訂正できた。一方、今回の二音例も独自構成であり、本人の演奏における頻度を主張しない。右手の3rdを同じ拍に置く必要は必ずしもなく、和声スパン内の機能として確認する。

### 変更履歴・研究回数
- 2026-11-21 第1回：理論モデル・3調例・暫定アルゴリズム。
- **2026-11-21 第2回：2/3**。Levine第17章の教則原典を直接確認し、同時LH3声の過大スパンを訂正、二音モデルとリズム生成v2を追加。
- 第3回で史料・生成規則の最終監査を行い、未解決を引き継いで**必ず次のドロップ2へ移行**。第4回は行わない。


---

## 10. 第三次研究（累計3/3・最終回）：史料の射程、機能充足、イベント生成、監査（2026-11-21）

### 10.1 研究の到達点と史料の階層

**研究回数確定：3/3。以後この技法を単独テーマとして再研究しない。** 次の対象はドロップ2。既存第1・2次を保持し、以下の修正・最終監査を優先して読む。

1. **直接参照した出版教則原典**：Mark Levine, *The Jazz Piano Book* (Sher Music, 1989), Ch.17 “Stride and Bud Powell Voicings”, pp.155–166。公開されている同章の本文を直接参照した。LevineはBud Powell型を**通常2音、ときに3音**で、根音・3度（10度）・6度・7度が中心と説明し、strideとの機能的対比を行う。出版元Sher Musicの公式目次でも第17章の開始ページ155を照合できる。これは**教則著者の説明の一次資料**だが、Powell本人の録音に関する一次資料ではない。
   - 章本文: https://www.redemption-church.com/worship/Songs/Real%20books/Other%20stuff/Sheet%20Music%20-%20The%20Jazz%20Piano%20Book.pdf
   - 出版社公式目次: https://www.shermusic.com/new/sample_pages/0961470151_toc.pdf
2. **演奏一次資料**：Powellの《Body and Soul》でstrideを使う例が同章脚注で指示される。つまり「Powellはstrideを一切弾かなかった」は誤り。**今回は当該原録音を直接聴取・逐音採譜できていない**ため、具体的な和音の音高・拍位置を本人に帰属させない。
3. **ユーザー評価との照合**：リポジトリの \`feedback/Feedback_001_Shizukana_Kitai_Piano_Jazz_Preferences.md\` に記録された「自然な機能進行、ガイドトーン、低音の明瞭性、過度な意外性の回避」と一致する。ただし好評な濃い4音以上の和声と、Powell型左手の**2音中心の簡潔さ**は同義でない。**ピアノ独奏の全体響きが4音以上**でも、LH単独は2音でよい。RH旋律・対旋律・ベースを含む総和で機能を判定する。

**史料と創作モデルを厳密に分離する。** 本文の具体的音名・スコア・生成規則は研究者が作った独自例で、Powellの特定小節の採譜ではない。

### 10.2 音度構造と「2音だけではコードを決定できない」問題

- \`ROOT_THIRD\`: 1–3（または1–♭3）、根音と長短を示すが7thの種類は未確定。
- \`ROOT_SEVENTH\`: 1–7/♭7、和音の7thを示すが3rd不在なら長短が未確定。
- \`ROOT_SIXTH\`: 1–6、6th和音・経過・旋律との関係で意味が変わる。**「6thがあれば必ずドミナント」などの誤判定は禁止**。
- \`ROOT_TENTH\`: 1–10/♭10、3rdの開離配置。広い同時左手把握を強制しない。
- \`GUIDE_SHELL\`: 3–♭7（m7では♭3–♭7、maj7では3–7）、ベース奏者との協働時に有効。ただし**一般的な機能シェルと歴史的Powellの典型配置を同一視しない**。

**機能充足条件**：時点のLH和音単独ではなく、和声スパン内のベース、RH旋律、他楽器の**音高と発音時刻**を参照して3rd/7thの有無を判定する。3rdが旋律で遅延提示される場合は、先行する和声が意図的に曖昧でもよい。sus、ペダル、ブルース的な3rdの可変性は例外。

### 10.3 三調の独自配置と二つの異なる目的関数

**A: Root+7thによる歴史的スタイルを参考にした疎な左手モデル**（下から順、各例は独自作例。RHは機能補足例であってPowell採譜ではない）

| Key | ii / LH | V / LH | I / LH | RHで補う3rd |
|---|---|---|---|---|
| C | Dm7: D3–C4 | G7: G2–F3 | Cmaj7: C3–B3 | F4 / B3またはB4 / E4 |
| F | Gm7: G2–F3 | C7: C3–B♭3 | Fmaj7: F2–E3 | B♭3またはB♭4 / E4 / A3またはA4 |
| E♭ | Fm7: F2–E♭3 | B♭7: B♭2–A♭3 | E♭maj7: E♭2–D3 | A♭3またはA♭4 / D4 / G3またはG4 |

この例は**LHを二音に保つこと**を優先するため、LHの声部進行は必ずしも最短距離ではない。右手の3rdを一斉打鍵する必要はない。右手の旋律線として時間的に提示する場合は和声スパンと拍位置を検証する。

**B: 機能的ガイドトーンの最小移動モデル**（ベースが別にいる場合、LH2音）
- Key C: Dm7 **F3–C4** → G7 **F3–B3** → Cmaj7 **E3–B3**。
- Key F: Gm7 **B♭3–F4** → C7 **B♭3–E4** → Fmaj7 **A3–E4**。
- Key E♭: Fm7 **A♭3–E♭4** → B♭7 **A♭3–D4** → E♭maj7 **G3–D4**。

**注意**：Bは最小移動を示す汎用ガイドトーン配置であり、Powell本人の歴史的演奏パターンの統計的代表ではない。Bを「Bud Powell専用の正解」と分類するのは誤り。

**実行済み検査（JavaScript）**：上記3調について、音度を半音クラスに変換し、ii♭7→V3の半音下降、ii♭3→V♭7の共通音、V♭7→I3の半音下降、V3→I7の共通音を計12条件検査、**12/12通過**。これは**理論上の音高クラス検査のみ**。同音異名の全調自動綴り、リズム・音響・実際の作品譜面との一致は検査していない。

### 10.4 リズムは独立した生成対象

LHの発音イベントはコードの開始と必ずしも一致しない。RHの密度・休止・強勢と、ベースの発音を条件にする。

- \`ANTICIPATE\`: 次の和声を拍の裏で先取りする。ただし旋律が前和声の非和声音を保持する場合、先取りで強い衝突を起こす可能性があるため要検査。
- \`ANSWER\`: RHフレーズ末尾の休符にLHの短い応答を置く。単なる空白埋めではなく、次の機能への誘導が必要。
- \`SUPPORT\`: RHの長音や倚音の解決に和声的な支持を置く。
- \`REST\`: RHが密でベースも機能を示すとき、LHの無発音を許容。

**スウィング感の主因**はノートのオンセット、音価、フレーズ、アンサンブル相互作用であり、2音和音という音数からは導出できない。4分裏・2拍4拍を一律に割り当てる生成器もPowellの個性を保証しない。

### 10.5 作編曲アルゴリズム v3（設計仕様、未実装）

\`\`\`text
INPUT:
  harmony_spans, melody_events, bass_events, ensemble_roles,
  style_mode, register_limits, phrase_boundaries, provenance
FOR each harmonic span h:
  determine chord root, quality, 3rd, 6th, 7th, suspensions
  choose LH mode:
    ROOT_THIRD | ROOT_SEVENTH | ROOT_SIXTH | ROOT_TENTH_SPLIT
    | GUIDE_SHELL | REST | SOURCE_GROUNDED_OSTINATO
  produce candidate pitch sets (usually 2 LH notes)
  reject single-hand simultaneity outside conservative span limits;
    split/roll or redistribute, do not silently label as simultaneous
  compute chord_function_coverage across LH + RH + bass + strings
  allow 3rd/7th omissions only if covered elsewhere or intentional ambiguity
  enumerate attack events {ANTICIPATE, ANSWER, SUPPORT, REST}
  reject overlaps with melody accents or bass low-register collisions
  optimize:
    functional clarity + melody primacy + rhythmic interaction
    + register separation + voice-leading continuity
    - low-register masking - repetitive attack templates
  retain harmonic tension when melody's appoggiatura requires it
VALIDATE:
  spelled pitch classes, simultaneity, functional coverage,
  event chronology, melody-harmony dissonance, role ownership,
  provenance labels, independent-voice counterpoint
OUTPUT:
  LH events, orchestration roles, voice-leading graph,
  confidence/validation log and unresolved exceptions
\`\`\`

**実装優先の不変条件**：
1. 同時LH2音の外声幅は既定で11半音以下の候補を優先（音楽史上の規則ではなく保守的な配置フィルタ）。
2. 各和声スパンで、機能に必要な3rd・7thの所在を追跡し、susや意図的曖昧化を例外タグで扱う。
3. LHがrootを置かない場合、ベース・Vc・Cb等がrootを補うか、rootless意図を明示する。
4. 先取り和音の新3rd/7thと前和声の旋律持続音の不協和を監査する。
5. 音数の追加ではなく、**旋律の動機→変形→フレーズ終止**を優先してLHの発音密度を調節する。
6. 生成時は声部別のイベントと音価を保持し、単一の垂直和音集合に平坦化しない。

### 10.6 弦楽6声への移植（Powell型の本質は「疎な和声応答」）

- Vn1：RH旋律の歌唱線。9th開始や倚音解決は音楽的に必要な場合のみ用いる。
- Vn2・Va：LHのガイドトーンと短い応答を**役割分担**する。常に二人同時の長音和声に変えない。
- Vn3：全・二分・四分中心の共通音または休符。RHの密度が高い区間は休符を許す。
- Vc：根音/対旋律のいずれかを句ごとに明示。Cb不在時は低音の根拠を確保。
- Cb：任意のpizz。Vcとの常時ユニゾンは避け、必要な発音時点だけ低音を補強。
- **対位法監査**：独立した持続声部の平行5/8を検出し、意図的なジャズ的平行ブロックは別のテクスチャー型として分類。ガイドトーンの解決、倚音、短9度の密集衝突を確認する。

### 10.7 誤用・例外・未解決事項

**誤用**：
- 「Powell型＝必ず左手4音」：誤り。
- 「二音シェルなら和音の性格は常に確定」：誤り。root+7thでは3rd不在。
- 「ガイドトーン最短移動ならPowellの演奏そのもの」：誤り。一般理論と史料的実証を混同。
- 「左手の音を減らせばスウィングする」：誤り。
- 「独奏でも常にrootを消す」：誤り。編成と音域に依存。

**例外**：strideの挿入、ソロピアノ、ブルース的3rdの可変、sus/ペダル、オスティナート、LHの先行単音、特殊な反復テクスチャー。《Un Poco Loco》を通常ii–V–Iの省略シェルだけで説明しない。

**引継ぎ事項（研究上限のため本テーマでは再研究しない）**：
- Powell本人の原録音からLHの音高・拍位置を逐音採譜し教則例と照合する作業は未実施。
- Levine図17-16〜24の各音符を画像から完全照合する作業は未実施。
- 生成アルゴリズムv3は**仕様のみ**で、コード化・音響検証・MusicXML出力テスト未実施。
- 12キーの異名同音綴り、左手の実測可奏性、テンポ別の発音密度、音色・残響によるマスキングは未検証。
- これらは**次テーマの一般化した音域監査・リズム監査の仕様**に引き継ぐ。Powell型単独研究の4回目は実施しない。

### 10.8 研究履歴と最終品質判定
- 第1回（1/3）：独自理論モデル。左手3声の過大な同時音域を後に訂正。
- 第2回（2/3）：Levineの出版教則原典に照合し、LH2音中心に修正。
- **第3回（3/3）：出版社公式目次・章本文を照合し、三調の機能連結を12条件検査。生成仕様v3と歴史的根拠の限界を確定。**
- **判定：理論・設計仕様としては保存可能。Powell本人の演奏に対する実証的再現性は未検証。歴史的実演分析の「完成」とは称さない。**
- **次回対象：ドロップ2（1/3）。同一テーマ4回目は禁止。**
