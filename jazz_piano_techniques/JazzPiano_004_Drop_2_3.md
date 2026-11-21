# Jazz Piano 004 — Drop 2 / Drop 3 voicings, with approach-harmony design
研究日: 2026-11-21。**第1回/最大3回**。優先度：コード／ボイシング／アプローチ／声部進行。

## 根拠資料
- Barry Nettles & Richard Graf, *The Chord Scale Theory & Jazz Harmony* (1997), https://djvu.online/file/betNTplepgXqK 。4-way closeを基礎としたDrop 2、Drop 3、Drop 2+4、および9th/13thへの置換を記述。
- John H. L. Hansenほか, “A modular system generating Jazz-style arrangement for a given set of a melody and its chord name sequence,” *Acoustical Science and Technology* 29(1), 2008, https://www.jstage.jst.go.jp/article/ast/29/1/29_1_51/_pdf 。4-way close、Drop 2、dim/chromatic/diatonic approachを分岐させ、低音の音程制限を監査する生成アルゴリズムを提示。
- Evan Rogers, *Big Band Arranging: Voicings Part 1*, https://www.evanrogersmusic.com/blog-contents/big-band-arranging/voicings-part1 。Drop 3がDrop 2より少用であること、Drop 2+4の使いどころと音程・音域上の注意点を説明。
- Piano With Jonny, *Drop 2 Piano Voicings*, https://pianowithjonny.com/piano-lessons/drop-2-piano-voicings-the-complete-guide/ 。旋律トップを保持したままDrop 2を作る手順。

## 定義：トップノートを維持すること
4声を低い順に x1<x2<x3<x4 とする。
- Close: [x1,x2,x3,x4]
- Drop 2: sort([x1,x2,x3-12,x4])
- Drop 3: sort([x1,x2-12,x3,x4])
- Drop 2+4: sort([x1-12,x2,x3-12,x4])
トップ音x4は保持。**和音の音名集合を変えずに音域と内声配置を変える**操作である。音程の広がりと和声の豊かさを同一視しない。

## Pythonで実行した構造検証（MIDI番号）
コード: jazz_piano_techniques/code/drop_2_3_audit_v1.py
- Dm9（D/F/A/C、9thは今回は未採用）: Close (65,69,72,74) = F4 A4 C5 D5。Drop2 (60,65,69,74) = C4 F4 A4 D5。Drop3 (57,65,72,74) = A3 F4 C5 D5。
- G13（B/E/F/A、3rd/13th/♭7/9）：Close (76,77,81,83) = E5 F5 A5 B5。Drop2 (69,76,77,83) = A4 E5 F5 B5。Drop3 (65,76,81,83) = F4 E5 A5 B5。**E–Fの短2度が残るため、この配置を無条件に推奨しない。** この例は機械的なドロップ処理が響きの良さを保証しない反例でもある。
- Cmaj9（C/E/G/B、9thは今回は未採用）：Close (76,79,83,84) = E5 G5 B5 C6。Drop2 (71,76,79,84) = B4 E5 G5 C6。Drop3 (67,76,83,84) = G4 E5 B5 C6。
- 全例について4音のpitch class保持、トップ音保持、Closeの1オクターブ以内の密集条件をPython実行でassertし、PASS。

**注意：** Dm9とCmaj9の例は、各々9thを省いたm7／maj7の4音配置であり、実際の発音音からはDm7／Cmaj7と記すべき。コード名の9は元の和声文脈を示すだけで、実音に9thがあると誤解しない。G13の実音には9th Aと13th Eが含まれる。

## アプローチ和音を別モジュールとして設計
1. **クロマチック・アプローチ**：目標となる4声の各音を半音上または下から接近。全声部を機械的に同方向へ動かすと機能和声が不明瞭になるため、低音の根音と旋律の解決先を別々に監査。
2. **ディミニッシュ・アプローチ**：目標和音の直前にdim7由来の和音を置く。例えばG7(♭9)の根音Gを除くB–D–F–A♭はBdim7に相当する。**dim7の異名同音・根音解釈と声部の解決先を明示する**。
3. **ダイアトニック・アプローチ**：目標音へ全音階的に進む内声を配置。和音の機能とメロディの拍位置が整合する場合に優先。
4. アプローチ和音は**目標和音への解決のための一時的な和音**。各音をコードスケール内に収めることより、強拍の目標音・係留・倚音の意味を優先する。

## 作編曲への実装設計
- 入力：旋律（各音の拍位置・音価）、コード列、和声リズム、楽器音域、ベース有無。
- 生成：旋律トップを固定→4声Closeを構成→Drop 2／3候補を列挙→必要な9/13を5thやrootと置換→隣接和音間の移動コストとガイドトーン解決を比較。
- アプローチ：旋律の到達点に向け、chromatic／diminished／diatonicの候補を別途列挙。目標和音と同じ強さで毎拍コードを変えない。
- 監査：最低音と次低音の間隔、低域での短2度、各声部の音域、平行完全音程、非和声音の解決、トップ旋律の保全。意図的なジャズの平行進行と不注意な禁則を区別。
- 弦6声：Cbに低音の和声機能、Vc/Va/Vn3/Vn2にDrop 2/3の各声部、Vn1にトップ旋律。低声を機械的にCbへ押し込まず、Cb欠席時のVcによる機能維持を検査。

## 未達と次回（2/3）
今回のPythonは**構造変換だけ**を検証した。連続和音の最適声部進行、低音の音程限界、実際のアプローチ和音の生成、4声旋律ハーモナイズ、原譜の採譜は未実装・未検証。次回は8小節のii–V–Iを対象に**Drop2／Drop3とchromatic/dimアプローチの実音と解決を比較**する。3回で必ず終了。
