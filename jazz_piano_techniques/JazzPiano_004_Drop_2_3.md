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


---

# 第2回/最大3回：アプローチ和音とDrop 2/3の声部解決
研究日: 2026-11-21。**累計2/3**。今回は実行可能な構造検証と、論文にある生成法の適用範囲の区別に重点を置く。

## 資料照合と重要な制限
- N. Emura et al., “A modular system generating Jazz-style arrangement for a given set of a melody and its chord name sequence,” *Acoustical Science and Technology* 29(1), 2008, https://www.jstage.jst.go.jp/article/ast/29/1/29_1_51/_pdf 。図3はclose/Drop2/Drop3、表1は4-way closeにdim/chromatic/diatonic approach、Drop2にdiatonic approachを割り当てる**当該プロトタイプの適用範囲**を明記する。したがって「Drop2へdim/chromatic approachを付けることが絶対に禁止」とは解釈しないが、同論文がその組合せを実装・検証したと主張してはならない。
- Jazz arranging textbook chapter https://www.ithaca.edu/sites/default/files/2021-03/2019-book-chapter-school-jazz-arranging.pdf 。旋律をトップに固定し、Close→Drop2→Drop2+4を使い分ける際の声部配置・重複音への注意を参照。
- *Grove Music*, “Harmony, jazz” https://docdrop.org/pdf/Strunk---2021---Jazz-harmony---1.-Terminology-and-theory-l5kpy.pdf 。Drop3は比較的まれな配置であり、どの曲でもDrop2と同頻度で用いる根拠はない。
- Berklee Online, “Voice Leading for Guitar,” https://online.berklee.edu/takenote/voice-leading-for-guitar/ 。和声機能を維持するための声部連結とDrop2の関係。

## 構造実験：Cmaj7へのアプローチ
4-way close C4–E4–G4–B4 = MIDI (60,64,67,71)。
- Drop2: **G3–C4–E4–B4** = (55,60,64,71)。第2声（上からG4）を1オクターブ下降。
- Drop3: **E3–C4–G4–B4** = (52,60,67,71)。第3声（上からE4）を1オクターブ下降。
- Chromatic approach to Drop2: **F♯3–B3–E♭4–B♭4** = (54,59,63,70)。各声が(+1,+1,+1,+1)半音でDrop2へ進む。**アプローチ時点のコード名はCmaj7ではない**。目標の直前に置く非機能的な平行半音アプローチとして解釈。
- Diminished approach candidate: **B3–D4–F4–A♭4** = (59,62,65,68) はG7(♭9)の根音省略形。Drop2への**同一順位対応**では (-4,-2,-1,+3) 半音。クロマチック案のような全声半音解決にはならない。これは「dimなら自動的に滑らか」という誤解への反例。dimの転回形・オクターブ・目標Drop形・ベースを一体で探索する必要がある。
- なおG7(♭9)のdim7の構成音を正しく識別するには**B–D–F–A♭**（3rd,5th,♭7,♭9）を使用。G7(♭9)をCmaj7へ解決する際、B→C、F→Eというガイドトーンの半音解決を優先する場合は**同一順位対応に拘らず声部の再割当てを行う**。

## Python実行済み監査
コード: jazz_piano_techniques/code/drop_approach_v2.py。
実際にPythonを実行して、Close/Drop2/Drop3のpitch class保持、クロマチック案の4声半音解決、dim7の構成音、dim→Drop2の不均等な移動をassertで確認し、PASS。8小節・16和音イベントの**説明用の反復モデル**も生成して構造監査した。ただし全8小節の目標はCmaj7のままで、**前回予告したii–V–Iの実際の和声進行や音楽的な8小節作品を実装したわけではない**。この不足は明記して次回へ繰り越す。

## 次回3/3の検証条件
1. ii–V–Iまたは短調iiø–V–iの複数和音を含む8小節の**実際の和声進行**を作る。
2. 旋律トップ音を保持し、Close/Drop2/Drop3候補とdim/chromatic approachの候補を各イベントで評価。
3. 単なる4声半音平行移動だけでなく、3rd/7thの機能解決、ベースと和声の関係、内声の方向、低音の密集、アプローチの解決タイミングを監査。
4. 弦6声に転用する際、トップ旋律・ガイドトーン・ベースを役割分担させ、音域と平行完全音程を別々に検査。
5. 最大3回の上限に従い、未完があっても第3回で終了する。


---

# 第3回/3回【最終】：8小節のDrop 2/3選択とアプローチ和音の監査
研究日 2026-11-21。**累計3/3。本テーマは終了。次回はブロックコードへ進む。**

## 実行可能な生成法
各小節でコードの構成音4つとトップ旋律音を指定し、close／drop2／drop3の3候補を列挙。動的計画法で、隣接する4声の絶対音高差の総和と、低音がC3を下回ることへのペナルティ、close形への小さなペナルティを最小化する。**この目的関数は仮設であり、音楽的美しさの客観的尺度ではない**。

和声進行（8小節）：Dm7 → G7 → Cmaj7 → Am7 → Dm7 → G7 → Cmaj7 → Cmaj7。
トップ音（MIDI）：74,77,79,76,74,77,79,76。これは音楽的な完成旋律ではなく**各小節の和音構成音によるトップ音テスト**である。

## Pythonで実際に実行した結果
コード：jazz_piano_techniques/code/drop_approach_v3.py。テストPASS、最適化コスト60。
1. Dm7 drop2 (60,65,69,74) = C4 F4 A4 D5
2. G7 drop2 (62,67,71,77) = D4 G4 B4 F5
3. Cmaj7 drop2 (64,71,72,79) = E4 B4 C5 G5
4. Am7 close (67,69,72,76) = G4 A4 C5 E5
5. Dm7 close (65,69,72,74) = F4 A4 C5 D5
6. G7 close (67,71,74,77) = G4 B4 D5 F5
7. Cmaj7 drop2 (64,71,72,79) = E4 B4 C5 G5
8. Cmaj7 close (67,71,72,76) = G4 B4 C5 E5

**重要な注意**：この最適化は順位対応による移動量を計算し、声部交差・完全音程平行・和声機能の解決・トップ旋律の音価・演奏可能性を完全には検査していない。G7→Cmaj7における導音B→CやF→Eの対応は別途声部割当てで検査する必要がある。音数の多さをもって作曲完成と見なさない。

## アプローチの構造テスト
- 8小節目のCmaj7 close (67,71,72,76) に対して、半音下からの平行クロマチック・アプローチ (66,70,71,75) は各声部が+1半音で到達する。**一時的な接近和音であり、元のCmaj7の機能をそのまま持つとは限らない**。
- G7(♭9)の根音省略dim構造 (59,62,65,68) = B3 D4 F4 A♭4 を同じ最終和音へ単純な順位対応で連結すると(+8,+9,+7,+8)の大跳躍になる。これは**dim7アプローチの一般的な音楽的評価ではなく、転回・オクターブ再配置を省いた場合の失敗例**。適切な転回形を探索する必要がある。
- アプローチ和音の機能と解決を検査するには、G7(♭9)→Cmaj7でB→C、F→Eのような**声部の再割当て**を許すべきである。現行のコードはこの探索を実装していない。

## 研究全3回の統合結論
1. Drop2/3は**和音の構成音集合を保ったまま配置を変える**操作であり、単独でコードの質を高める魔法ではない。
2. アプローチ和音は旋律の目標音、到達拍、声部の解決先と一体で設計する。クロマチック平行・dim・ダイアトニックを無差別に混用しない。
3. Close、Drop2、Drop3の選択は前後の和音とトップ旋律に依存する。低音密集、楽器音域、禁則、非和声音の解決、フレーズ構造を最適化の別制約として追加すべき。
4. 弦楽6声への転用ではCb/Vcが低音の機能、Va/Vn3/Vn2が内声、Vn1が旋律。**全パートで同時に機械的な平行半音移動を続けない**。

## 未解決と終了宣言
実際の録音・譜例の直接採譜、9/11/13の置換、低域音程限界、声部対応の組合せ最適化、演奏可能性、旋律の音価を含む検査は未完了。**研究上限3/3に到達したため第4回は行わない。次回はブロックコードとアプローチの接続を研究する。**
