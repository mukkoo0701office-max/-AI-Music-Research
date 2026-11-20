# Jazz Research 011 — All The Things You Are：転調する反復句と内声の連続性
日付: 2026-11-20
対象: Jerome Kern, *All the Things You Are* (1939)
形式: 36小節 8+8+8+12、4/4、非ブルース
検証: JAZZ STANDARD 557 掲載の1ページ譜面を画像で直接確認。1939年原典・実演の音価/和声/ボイシングとの一致は未検証。以下の小節番号は掲載版に準拠。

## 出典
- 楽曲 https://jazzstandard.info/score.php?id=12
- 掲載譜 https://jazzstandard.info/score_pdf/12.pdf
- 和声異版 https://squartet.com/en/standards/all-the-things-you-are
- 異版比較 https://betterbasslessons.com/walking-bass-lines/all-the-things-you-are

## 主題技法
8小節単位の類似した機能進行を異なる調性で再提示し、終結部のみ12小節へ拡張する。移調による既視感と新しい調性の色彩を両立させる。A1: A♭→C、A2: E♭→G、B: G→E、終結A3: A♭へ帰還。実際の旋律の厳密な移調一致は逐音検算未了。

## 掲載譜の小節別コードと機能
1 Fm7 (A♭:vi)、2 B♭m7 (ii)、3 E♭7 (V)、4 A♭maj7 (I)、5 D♭maj7 (IV)、6 Dm7→G7 (C:ii–V)、7–8 Cmaj7 (I)。
9 Cm7 (E♭:vi)、10 Fm7 (ii)、11 B♭7 (V)、12 E♭maj7 (I)、13 A♭maj7 (IV)、14 Am7♭5→D7 (Gへの前属→属。半減七は掲載譜表記)、15–16 Gmaj7 (I)。
17 Am7 (G:ii)、18 D7 (V)、19–20 Gmaj7 (I)、21 F♯m7♭5 (掲載譜表記)、22 B7、23 Emaj7、24 C+7 (F minorのV7変化形として解釈可能)。
25 Fm7、26 B♭m7、27 E♭7、28 A♭maj7、29 D♭maj7、30 G♭7 (掲載譜)、31 Cm7、32 B° (dim)、33 B♭m7、34 E♭7、35 A♭maj7、36 (Gm7♭5→C7♯9) リピートへのターンアラウンド。
注意: 30小節は他のコード資料ではD♭m7/D♭m(maj7)、21小節はF♯m7の版もある。30小節のG♭7は原典の唯一の正解ではない。24小節のC+7も異版あり。

## 旋律と度数：直接確認できた冒頭の限定的な例
掲載譜はト音記号、調号A♭長調（4♭）。1小節の長音はCで、Fm7の5th。2小節の長音はFでB♭m7の5th、後続のCは9th。3小節のB♭反復はE♭7の5th。4小節のB♭はA♭maj7の9th、Cは3rd、B♭は9th。5小節のA♭反復はD♭maj7の5th。これらは掲載画像からの読み取りであり、原典照合済みという意味ではない。
9–36小節の全旋律音の逐音度数表、倚音・係留・経過音の分類は未完了。コードのテンション音を直ちに倚音と呼ばず、強拍位置・準備・解決・音価を照合すること。

## ボイシング・対位法・リズム
掲載譜は単旋律とコード記号であり、実際のピアノ/弦楽ボイシングは未記載。以下は独自応用。
- A1→A2: 和声機能の反復を保ち、トップ声の音域と内声の配置を変えて転調を聴かせる。
- 25–35: D♭maj7→G♭7→Cm7→B°→B♭m7→E♭7→A♭maj7。30小節の版差を前提に、半音接続可能な3rd/7thを選ぶ。
- リズム: 掲載譜は4/4で全音符・2分音符・4分音符・3連符を含む。音価の長短と転調位置の対比を設計に活用。
- 感情効果: 同じ和声的輪郭が調を変えて再来することで親近感と浮遊感が同居し、最後の12小節拡張で帰着感を増す（解釈）。

## 六声弦楽への新規作曲応用
Vn1: 原曲を転載せず、9th/3rdから始まる独自カンタービレ。Vn2: 3rd/7thの半音連結。Vn3: 2分・全音符主体の共通音。Va: 4–3/9–8係留を準備・解決込みで独自設計。Vc: 4度進行と半音アプローチの低音。Cb: pizzicato、各句の和声支点のみ、欠員でも成立する書法。
模倣用8小節（原曲旋律ではない）: vi7→ii7→V7→Imaj9→IVmaj9→ii7/V7（新調）→Imaj9→I6/9。次句は別調へ機能形を移調し、最終句を4小節拡張。

## MusicXML規則
- 6 parts: Vn1,Vn2,Vn3,Va,Vc,Cb。4/4、各小節番号を明示。
- chord symbol は harmony/root/root-step, root-alter, kind, degree を使用。半減七は half-diminished、dim7 は diminished-seventh、augmented dominantは augmented-seventh等で表記を確認。
- 移調する句は独立した harmony と notes を記述。転調は key の fifths を変更し、臨時記号の enharmonic spelling を声部進行に合わせる。
- suspension は preparation / suspension / resolution の3点をチェック。タイは tie と tied の両方、フレーズは slur を使い分ける。
- 完全5度/8度の平行、声部交差、無理な音域、短2度の不必要な密集を検査。Cbは記譜と実音の1オクターブ差を明記。
- 各観察に verified_score / secondary_chart / compositional_proposal / unverified のラベルを付け、版差を保持。

## 重複管理
既知のJazz 006〜010とは別曲。研究011として作成。リポジトリ全体の技法重複について完全監査は未実施。
