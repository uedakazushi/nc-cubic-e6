# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v24。最初に `00_research_plan.md` を読む。主論文は `papers/nc-cubic-e6.tex`。現行の四周期・triality・三成分Hodge比較は `research/conic_period_coordinates.md`、LG/G2/braidの基礎は `research/cayley_lg_connections.md`。他の分野は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`。

**最優先は数学的に面白くすること。多様な話題との具体的接続を優先し、名称や定理数の増加を目的にしない。** 意外な同型・共通構造、新しい問いや方法を重視する。正確性を犠牲にしない。八次元E6成分の分類は保持するが、完成を他分野との比較の前提にしない。

公表価値ある関連分野成果は同じ日本語LuaLaTeX主論文へ統合する。価値ある旧結果・必要証明を削除しない。証明済み、仮定付き、未完成、予想、計算的観察を区別し、一次文献の仮定・適用範囲を確認する。原稿に証明があること、今回点検したこと、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。

ノートは現在有効な知識、式、障害、反例、文献比較を保持し、日誌・会話・履歴・重複証明を蓄積しない。現行の方針・論文・ノート・最小限コードと証明書だけで再開可能にする。旧ZIP・旧原稿・PDF・ログ・キャッシュ・コンパイル中間物をGitへ入れない。

GitHub mainが正本。**push済み内容はLibraryへ保存しない。** push失敗で未保存成果の保全が必要な場合だけ緊急退避できる。既存Libraryファイルは明示指示なしに削除しない。約15分または数学的区切りで通常のfast-forward保存。不要なPR・Actions・force pushを使わない。共有変更と競合したら確認して両立する。生成・検証・commit・push・Library保存を別状態で報告する。全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本。

**現在の到達点。** 全四periodは一般conic標識で(z1/z2,z2/z3,z3/z4,z3*z4)。対称族は従来のB²−C²≠0 chartの外なので、明示line sectionで別途compatible標識を構成した。そのperiodは(eta,xi,eta,eta)。Hurwitzのホモロジー像は外側三根S3で、pure braidは自明（Goldman–Neumannの既知定理の適用）。
trialityの不変格子→余不変格子はdiag(1,3)。period isogeny (xi,eta)→(xi,eta³)のWeyl商はBoalch–PalubaのG2三成分写像に正確に一致する。torusのisogenyであり、標数0のG2群の中心isogenyではない。
三torus持上げ(xi,zeta^j eta)が全て明示開集合にあるregular底では、三Fricke成分の有理MHSは標識graded pieceの下で同型。外側の正規化log差j/3を境界cycleの有理持上げで吸収する。globalな標準VMHS同型、曲面同型、導来同値ではない。
Kleinではxi=eta=primitive7root、四periodが全て7乗根。同じG2底の二コンパニオンは外側21乗根となり、整数Hodge拡大類の位数は7,21,21。全て有理分裂だが整数MHSの差は残る。他二成分の有限Hurwitz軌道を推論しない。
g=iota_v iota_w iota_u iota_w（対称時B1² B2^-2）は全H2・periodで恒等、しかしCantat–Lorayの既知定理でentropy log(3+2sqrt2)。アフィンH2と射影双有理degreeを区別する。

**優先する次の着手。** 三成分の3捩れperiod差を境界線束の変更・有限被覆・代数的対応として実現できるか調べる。まずKlein7/21のline配置とboundary gluingを比較し、有理Hodge同型から幾何・圏の同値を無断で結論しない。
並行してgの境界blow-up/down列・cluster tropical作用を構成し、ホモロジーに見えない正entropyを何が検出するかを調べる。圏的entropyは未計算。その他のtorsion periodでmu3が整数拡大位数をどう変えるか、Spin8→G2のcharacter解釈、全rank五接続とglobal標識monodromyも有望。

既存のAW/Fricke、Poisson括弧9倍、七次元正常形・八次元形式族、N5²M5とS5×S5、D4/Cayley、G2のD4/A2、periodの円分分裂を保持する。純粋qの非Casimir切断障害、固定pointed心へのVieta非延長を無視した反復はしない。全H3 admissibility・intrinsic降下・全境界は未完成。

今回実行したのは `verify_triality_period_isogeny.py`。整数格子・Q-Laurent・Q(zeta21)の厳密演算PASSを `triality_period_isogeny_certificate.json` に記録。通常の幾何・Hodge・entropy証明の形式検証とはしない。新節単体LuaLaTeX5頁の画像・内部参照・overfullなしを確認。旧28検証器の今回の全再実行、主論文全体の今回の組版、独立査読、網羅的新規性調査は未実施。更新後のmain ref、input、必要ファイルと旧証明の保持を確認する。
