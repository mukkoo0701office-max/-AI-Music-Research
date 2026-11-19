# Jazz Research 002 — After You've Gone：20小節ABACと終結タグの時間設計

- 研究日: 2026-11-20
- 作曲: Turner Layton／作詞: Henry Creamer（1918）
- 対象: After You've Gone
- 対象ページ: https://jazzstandard.info/score.php?id=2
- 掲載譜: https://jazzstandard.info/score_pdf/2.pdf
- 歴史的初版: https://imslp.org/wiki/After_You've_Gone_(Layton%2C_Turner)
- 1918年初版所蔵: https://levysheetmusic.mse.jhu.edu/collection/151/004
- 米国パブリックドメインの1918年版: https://commons.wikimedia.org/wiki/File:After_You've_Gone.pdf
- 前回: Jazz Research 001『All of Me』のガイドトーン連鎖と重複しない、形式・終結タグの研究
- 検証区分: 曲名、作曲年、1918年譜の所在、20小節ABAC構造は資料による確認。各小節の原譜の音高・コードは未検証。

## 1. 新規技法：標準32小節に依存しない20小節コーラスと終結タグ

掲載ページは、4小節フレーズ4つ＋4小節タグによる20小節ABAC形式と説明する。12小節ブルース形式ではない。形式は分析用の区切りとして以下を仮置きする（各区間の具体的旋律・和声内容は未検証）。

| 分析小節 | 機能（形式モデル） | 原譜検証 |
|---|---|---|
| 1–4 | A：基本動機の提示 | 旋律音・コード未検証 |
| 5–8 | B：応答・対照 | 旋律音・コード未検証 |
| 9–12 | A：回帰 | 同一／変形の程度未検証 |
| 13–16 | C：終結に向かう対照 | 旋律音・コード未検証 |
| 17–20 | タグ：終結の引き延ばし | 具体的終止進行未検証 |

上記の区分は資料の「4小節×4＋4小節タグ」の説明を研究上に展開したもの。原譜とジャズ用リードシートの小節番号が一致するかは未照合。

## 2. 和声・メロディ・対位法

- **原曲和声**：掲載ページは「ほぼ毎小節コードが変化」と述べるが、コード記号の具体的配列は未検証。ii–V–I、セカンダリードミナント、裏コード、借用和音、dimの出現は断定しない。
- **原曲旋律**：3rd、7th、9th、11th、13thに該当する実音、倚音・係留・経過音の拍位置は未検証。初版譜面と現代版で比較が必要。
- **原曲ボイシング・対位法**：初版は声楽＋ピアノ譜であることまで確認。伴奏の実際の配置、低音と内声の動きは未検証。
- **感情効果（解釈）**：4小節単位の期待を4小節タグで延ばすことで、別れの余韻や終止を先送りする感覚を演出しうる。これは応用上の解釈であり原曲の個別音符からの実証ではない。

## 3. 六声弦楽への応用：オリジナル20小節習作モデル

- **Vn1**：1–4小節に新作4小節旋律A、9–12小節に同じ輪郭を持つ変奏A'、17–20小節に短い終結動機。既存曲の旋律を転載しない。
- **Vn2**：1–4小節は3rd・7thのガイドトーン、5–8小節でVn1の末尾リズムに応答、17–20小節では9–8係留（新作例）。
- **Vn3**：四分音符以下の細かい動きを原則避け、共通音を二分音符／全音符で保持。和声変化時は衝突を確認。
- **Va**：5–8小節で半音階的な内声下降、13–16小節でVn2と反行。必要なら4–3係留を新規設計。
- **Vc**：各4小節の始点と終止を示すベース。タグでは終止を1回遅延させる独自進行を作る。
- **Cb**：Vcを常時重複せず、各セクション開始・終結点だけ低音を補強。記譜音と実音のオクターブ差に注意。

**作曲用の例（原曲の採譜ではない）**：17–20小節で ii7 → V7sus4 → V7(♭9) → Imaj9 として終結を延長する。Vn2の9–8係留、Vaの4–3係留は準備・不協和・解決の時点を確認。機能和声を先に固定し、内声を半音または全音で滑らかに接続する。

## 4. MusicXML実装規則

1. `<time><beats>4</beats><beat-type>4</beat-type></time>` は**習作用の仮定**。原曲譜面の拍子を確認してから本採譜に適用。
2. 20小節を生成し、`<direction><direction-type><words> A / B / A' / C / TAG </words></direction-type></direction>` を各セクション頭に置く。セクション境界は1,5,9,13,17小節とする（研究用形式モデル）。
3. 各パートは独立した `<part>`、`<measure number="...">`、音価総和と休符を検査する。
4. 係留には同音高の前拍からの `<tie type="start"/>` と解決前の `<tie type="stop"/>` を適用し、`<notations><tied .../></notations>` も整合させる。スラーは `<slur>` で別管理。
5. Vn3は演奏難度制約を検査。Cbは移調楽器として `<transpose><diatonic>0</diatonic><chromatic>0</chromatic><octave-change>-1</octave-change></transpose>` を設定するか、アプリ側の実音処理を統一する。
6. 禁則検査：同方向に進む声部間の連続完全5度・8度、声部交差、無準備の強拍不協和、倚音の未解決、音域外、非意図的な低音の重複を検出する。
7. 原曲の音高・コードは確認できるまで `unverified` として別の研究メタデータに残し、創作例と混同しない。

## 5. 次回の検証項目

1918年初版のコーラス開始位置を特定し、現代リードシートの20小節と照合する。各小節の旋律音を和音の度数に対応付け、倚音・係留・経過音、ガイドトーンとベースの動きを逐音記録する。現段階では未確認の音符・コードを捏造しない。

## 6. 参考資料

1. JAZZ STANDARD 557: https://jazzstandard.info/score.php?id=2
2. 掲載PDF: https://jazzstandard.info/score_pdf/2.pdf （リンク存在確認。画像取得・逐音照合は失敗）
3. IMSLP（1918年出版の初版、米国PD／地域別権利に注意）: https://imslp.org/wiki/After_You've_Gone_(Layton%2C_Turner)
4. Johns Hopkins University Levy Music Collection: https://levysheetmusic.mse.jhu.edu/collection/151/004
5. Wikimedia Commons: https://commons.wikimedia.org/wiki/File:After_You've_Gone.pdf
6. Library of Congress, Marion Harris 1918年録音: https://www.loc.gov/item/jukebox-313413/

## 7. 重複確認

Jazz Research 001『All of Me』とは異なる曲と技法を選定。リポジトリ全体の既存研究番号一覧の網羅的確認は未実施。対象パスの未存在をGitHub fetch_fileの404で確認してから新規作成。
