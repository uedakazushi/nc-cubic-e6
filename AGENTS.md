# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v23。最初に `00_research_plan.md` を読む。主論文は `papers/nc-cubic-e6.tex`。現在の四周期・分裂判定は `research/conic_period_coordinates.md`、基礎的なLG/G2/braid/対数周期は `research/cayley_lg_connections.md`。他の既存研究は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`。

**最優先は数学的に面白くすること。多様な話題への具体的接続を優先し、名称の類似や定理数の増加を目的にしない。** 意外な同型・共通構造、新しい方法と問いを重視する。正確性を犠牲にせず、分類の完遂を他分野との比較の前提にしない。

公表価値ある成果は同じ日本語LuaLaTeX主論文へ統合する。既存の数学と必要証明を削除しない。証明済み・追加仮定付き・未完成・予想・計算的観察を区別し、一次文献と仮定・適用範囲を確認する。証明を書いたこと、今回点検したこと、計算したこと、独立査読を混同しない。誤りは依存する本文・要約・方針も更新する。

ノートは現行知識と具体式・障害・再開手順を保持し、日誌・履歴・重複証明にしない。旧ZIP・旧原稿・PDF・キャッシュ・ログ・中間物をGitに含めない。自己完結した現行の一式を保つ。
GitHub mainが正本。**push済み内容をLibraryに保存しない。** push失敗で未保存成果を保全する場合だけ緊急退避を認める。既存Library資料を明示指示なしに削除しない。約15分または数学的区切りで通常のfast-forward保存を行い、不要なPR・Actions・force pushは使わない。生成・検証・commit・push・Library保存を区別する。全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本である。

**現在解決した課題。** conic開集合Disc N≠0,B²−C²≠0の有限標識被覆上で、F1への縮約から整数D4基底alpha=(E1−E2,E2−E3,E3−E4,E3+E4−F)を得た。選択成分の境界座標zi+zi^-1=2uiに対し、全四指数化periodは(z1/z2,z2/z3,z3/z4,z3z4)。境界periodと合わせて全H2基底への積分をlogで表す。compatible markingを選ぶことと、平方根の符号を任意に取ることを混同しない。

有理MHS分裂は全四periodの捩れ性、さらに全ziの捩れ性と同値。Q上のsmooth分裂例(1/4,1/2,1/4,1/8)は9乗根、非分裂例(-65/16,75/16,-65/16,3575/288)はzi=2,3,4,6の逆数選択。整数拡大の自明性・量子q³=1・有限braid軌道とは別条件。古典的D4 torus・Friedman比較の一般理論を新規と呼ばない。

最優先の着手は四period上のHurwitzとtrialityの作用。保存されるconic pencilでEiの像と格子変換を計算し、pencilを変えるtrialityではF1標識間の遷移を先に求める。標識のWeyl作用、固定fiberの自己同型、底loopの解析接続、別のS5被覆を分ける。
並行して円分的periodと境界線束の位数・Kummer型Hodge拡大・mirror torusを比較する。全四periodが局所座標になったのでrank五の代数的de Rham接続の具体化へ進めるが、現段階でその行列は未構成。

旧成果の七次元正常形・八次元形式族・結節因子・二五次S5×S5・Poisson/DAHA・Milnor/Picard・G2・braidを保持する。全H3 admissibility・intrinsic降下・全境界は未解決。純粋qの非Casimir障害と固定pointed心のVieta障害を無視した反復をしない。被覆branch、Casimir値衝突、W臨界値衝突も区別する。

今回実行済みは `verify_conic_period_coordinates.py`。Q・整数格子・Laurent演算のPASSは同名証明書に記録。縮約・gluing・period比較・MHS判定の通常証明は有限計算とは別。旧27検証器の今回は全再実行をしていない。新節単体のLuaLaTeX4頁を画像点検し、内部参照・overfullなしを確認。主論文全体の今回の再組版・独立査読・新規性の網羅調査は未実施。
ファイル更新は完全な内容を用い、既存証明の欠落がないことを差分で確認する。mainへの到達、input、必須ファイル、コードの一致を保存後に検査する。
