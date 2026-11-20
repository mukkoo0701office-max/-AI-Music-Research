# Jazz Research 009 — All of Me：セカンダリードミナント連鎖と借用ivの色彩
作成日: 2026-11-20
対象: Gerald Marks / Seymour Simons, All of Me (1931)
形式: 32小節 ABAC、4/4、一般的なC調ジャズ演奏版。ブルース形式ではない。
検証レベル: **公開コード資料の小節配置を確認／指定サイトのPDF画像・旋律の逐音照合は未検証**。以下は原典確定版ではなく、Squartetに掲載された演奏用コード進行である。

## 出典
- JAZZ STANDARD 557 楽曲ページ https://jazzstandard.info/score.php?id=10
- 掲載譜PDF https://jazzstandard.info/score_pdf/10.pdf （PDFリンクの存在は確認。画像取得失敗）
- 32小節コード https://squartet.com/en/standards/all-of-me
- 和声解説 https://nielsdalgaard.com/jazz-standards/all-of-me/
- 借用iv・ターンアラウンド https://www.learnjazzstandards.com/blog/all-of-me-jazz-standard/

## 小節別コード・機能（公開演奏版）
|小節|コード|機能・解釈|
|---|---|---|
|1|Cmaj7|Imaj7 主調提示|
|2|Cmaj7|Iの持続|
|3|E7|V7/vi：G♯を導音として導入|
|4|E7|V7/vi持続|
|5|A7|V7/ii。E7はAmに解決せずA7へ連鎖|
|6|A7|V7/ii持続|
|7|Dm7|ii7に到達|
|8|Dm7|ii7持続|
|9|E7|V7/vi 再提示|
|10|E7|属和音の持続|
|11|Am7|vi7、E7の正規解決先|
|12|Am7|vi7持続|
|13|D7|V7/V、F♯導入|
|14|D7|V7/V持続|
|15|Dm7|D7→Dm7、同根異質の転換（F♯→F）|
|16|G7|V7、次のCへの準備|
|17|Cmaj7|Imaj7 再現|
|18|Cmaj7|I持続|
|19|E7|V7/vi|
|20|E7|持続|
|21|A7|V7/ii|
|22|A7|持続|
|23|Dm7|ii7|
|24|Dm7|持続|
|25|Fmaj7|IVmaj7|
|26|Fm6|同主短調からの借用iv6、A→A♭|
|27|Em7|iii7（演奏版により異同）|
|28|A7|V7/ii|
|29|Dm7|ii7|
|30|G7|V7|
|31|C6 → E♭dim7|I6から経過dim7へ（同小節内）|
|32|Dm7 → G7|ii–Vターンアラウンド|

## 新規焦点：二種類の「期待の裏切り」
1. 第3〜7小節 E7→A7→Dm7。E7は本来Amへ向かうが、A7に接続してドミナント連鎖を形成。根音E→A→Dは完全5度下降、3rdと7thの最小移動が和声の連続性を担う。
2. 第25〜27小節 Fmaj7→Fm6→Em7。IVの3rd AをA♭へ半音下降させる借用iv。Fm6のDは6thとして保持可能で、Em7のD（♭7）と共通音になる。A→A♭→Gの内声下降を新規編曲に応用できる。Fm6→Em7ではA♭→Gが半音下降する。

## 旋律・ボイシング・リズムの検証境界
原譜の音符・拍位置は直接確認できていない。**原曲旋律の各音の3rd/7th/9th/11th/13th判定、倚音・係留・経過音、実演のボイシング、リズム・フレージングは未検証**。本研究のガイドトーンはコードから導いた新規作編曲例であり、原曲旋律の転記ではない。
参考声部連結：E7の7th D→A7の3rd C♯、A7の7th G→Dm7の3rd F（いずれも全音下降であり半音と誤記しない）。E7の3rd G♯→A7の7th Gは半音下降。Fmaj7のA→Fm6のA♭→Em7のGは半音下降の連鎖。
長い二小節単位のドミナントは緊張を蓄積し、短い終止進行で緩和する。借用ivは一瞬の陰影を付ける（感情的効果は解釈）。

## 六声弦楽への応用（独自案）
- Vn1: 旋律を新規作成。小節頭は3rd/7th/9th/13thや解決を伴う倚音を優先。原曲メロディを無断転載しない。
- Vn2: ガイドトーン3rd/7thを滑らかに接続し、第25〜27小節のA→A♭→Gを担当可能。
- Vn3: 初心者向け、全〜四分音符中心、共通音保持と限定的な順次進行。
- Va: Vn2と対位法的に交替して半音変化、9–8・4–3係留は準備と解決が確認できる新規声部にのみ適用。
- Vc: E→A→Dなど根音運動と転回形を組み合わせ、フレーズ末は滑らかな低音線。
- Cb: pizzicatoで拍頭支点、必要に応じ休止。Cbなしでも和声が成立するようVcに最低音機能を残す。

## MusicXML実装規則
- 4/4、32小節、ABACセクションラベルをdirection/rehearsalで記録。
- harmony root/kind/degreeでmaj7, dominant, minor-seventh, minor-sixth, diminished-seventhを区別。
- 各音にvoice, duration, type, pitch, octaveを記録。Cbは記譜と実音のオクターブ差をtranspose chromatic=0, octave-change=-1等で明示し、使用ソフトの挙動を検証。
- 倚音/係留/経過音は検証済みの旋律または独自作曲の音にのみ分類。タイはtieとnotations/tied、スラーはnotations/slurで分離。
- 完全5度・8度の平行、声部交差、音域、増2度、不要な密集、導音解決を検査。ジャズ特有の意図的例外は記録。
- source_status: chord_chart_verified / melody_unverified / arrangement_original を別途MarkdownまたはXMLメタデータに保存。

## 研究の独自性
Jazz 004の経過dim、005の半音長6度、006の調性着地点、007の短調下降低音、008のワルツ旋律テンションとは区別し、今回は「属和音が期待される短調主和音へ行かず次の属和音へ移る」連鎖と「借用iv6の内声半音下降」の組合せに焦点を置いた。リポジトリ全件との技法重複完全照合は未完了。
