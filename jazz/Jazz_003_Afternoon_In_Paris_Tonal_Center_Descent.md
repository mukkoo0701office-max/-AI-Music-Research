# Jazz Research 003 — Afternoon in Paris：主和音の短調化による全音下降する調性中心

- 研究日：2026-11-20
- 作曲：John Lewis（1949）
- 対象：https://jazzstandard.info/score.php?id=1
- 掲載PDF：https://jazzstandard.info/score_pdf/1.pdf
- 比較資料：https://squartet.com/en/standards/afternoon-in-paris
- 別版：https://jazzstandardslibrary.com/tunes/afternoon-in-paris/
- 形式：32小節AABA、通常C、4/4、medium swing。ブルース形式ではない。
- 検証区分：原サイトで曲目と形式を確認。PDFは1ページの存在まで確認したが画像表示失敗。以下のコードは外部コード資料に基づく一般的な演奏版であり、原サイト掲載譜との一致は未検証。原曲の旋律音・音価・係留・倚音・経過音は未検証。

## 1. 新技法：長調トニックを同主短調化し、次の調のiiに転換

A冒頭の一般的なコード例（研究上必要な短い引用）：

| 小節 | コード | 機能 |
|---|---|---|
| 1 | Cmaj7 | CのImaj7 |
| 2 | Cm7–F7 | B♭のii–V |
| 3 | B♭maj7 | B♭のImaj7 |
| 4 | B♭m7–E♭7 | A♭のii–V |
| 5 | A♭maj7 | A♭のImaj7 |
| 6 | Dm7–G7(#9) | Cのii–V、#9は版差に注意 |
| 7 | Cmaj7 | Cへ回帰 |
| 8 | Dm7–G7 | 次のAへ接続 |

Cmaj7→Cm7ではE→E♭、B→B♭が半音下降し、CとGは共通音。Cm7をB♭のiiとして再解釈し、F7→B♭maj7へ進む。B♭maj7→B♭m7ではD→D♭、A→A♭、B♭とFは共通音。B♭m7をA♭のiiに読み替えてE♭7→A♭maj7に進む。**C→B♭→A♭という全音下降の調性中心**が、同根音の短調化を接続点として成立する。単なる半音装飾ではなく機能の再解釈である。

## 2. ガイドトーン・ボイシング・ベース

- Cm7→F7→B♭maj7：Cm7のE♭(3rd)はF7のE♭(7th)として保持可能。Cm7のB♭(7th)→F7のA(3rd)、F7のE♭(7th)→B♭maj7のD(3rd)は半音下降。
- B♭m7→E♭7→A♭maj7にも同型の3rd/7th連結を適用できる。
- G7(#9)のB(3rd)とB♭(#9)は半音関係。両音を同時に配置する場合は音域と音量、解決方向を吟味する。これは原曲の実際のボイシングを示すものではない。
- 低音の機能モデルは C→C/F→B♭→B♭/E♭→A♭→D/G→C。実際の録音のベース採譜ではない。
- AABAの9–16、17–24、25–32小節の細部は資料間の反復括弧・コード割付差があり、原譜未照合につき確定しない。
- 感情的効果：同一根音の長3度が短3度へ落ちることで柔らかな陰りが生じ、そのまま新しい長調に着地して色彩を更新する。これは和声からの解釈である。

## 3. 旋律と非和声音：未検証

PDFの音符画像を取得できなかったため、原曲旋律の3rd・7th・9th・11th・13th、倚音・係留・経過音、リズムと拍位置は断定しない。検証時は全音符について pitch、chord_degree、beat、nonchord_tone_type、preparation、resolution を記録する。作曲への独自応用として、Cmaj9の9th Dから新作旋律を始め、Cm9に変わってもDを共通の9thとして保持し、内声E→E♭の半音下降を聴かせる方法が考えられる。これは原曲メロディではない。

## 4. 六声弦楽の新規8小節習作

- Vn1：3rd/9thなどから始める新作歌唱旋律。原曲旋律は転載しない。
- Vn2：Cmaj7→Cm7のB→B♭、Cm7→F7のB♭→Aなどガイドトーン。
- Vn3：Cmaj7→Cm7のGなど共通音を全音符・二分音符中心で保持。8分音符は原則避ける。
- Va：E→E♭、D→D♭の半音下降。係留を創作する場合は準備と解決を検査。
- Vc：C→B♭→A♭の調性中心、ii–Vの根音移動を示す。
- Cb：句頭と到達点をpizzで選択的に補強し、Vcの常時重複を避ける。記譜音と実音はオクターブ違い。

## 5. MusicXML実装規則

1. 6つの独立した `<part>`、32小節、標準版の4/4を作る。これは原サイトPDFの採譜ではない。
2. コードは `<harmony>` のroot/kind/degreeに格納。m2/4/6/8の2和音の拍分割は原譜未確認なので習作では各2拍と仮定し、仮定を明記。
3. セクション A1/A2/B/A3 と tonal_center:C/Bb/Ab を `<direction><direction-type><words>` で記録する。
4. 声部連結は共通音・半音・全音を優先。ただし原曲旋律の保存が最優先。平行完全5度・8度、音域外、非意図的な強拍不協和、声部交差を検査。
5. タイは `<tie>` と `<notations><tied>` を対応させ、スラーは `<slur>` と区別。非和声音分類は逐音検証後に付与。
6. Cbには必要に応じ `<transpose><diatonic>0</diatonic><chromatic>0</chromatic><octave-change>-1</octave-change></transpose>` を設定し、再生側の二重移調を防ぐ。
7. 検証済み資料と創作例は別メタデータに保存する。

## 6. 重複・出典・限界

Jazz 001『All of Me』の連鎖ドミナント、Jazz 002『After You've Gone』の20小節タグと異なる、**同主短調化をピヴォットとする全音下降の調性中心**を研究。GitHubのJazz 002本文を参照したが、全研究の網羅的重複照合は未完了。掲載PDFはリンク確認のみで画像閲覧に失敗したため、旋律音・実際の非和声音・原曲配器は未検証。

- https://jazzstandard.info/score.php?id=1
- https://jazzstandard.info/score_pdf/1.pdf
- https://squartet.com/en/standards/afternoon-in-paris
- https://jazzstandardslibrary.com/tunes/afternoon-in-paris/
- https://nielsdalgaard.com/es/jazz-standards/afternoon-in-paris/
