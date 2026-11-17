# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v20。再開時は `00_research_plan.md` を最初に読む。主論文は `papers/nc-cubic-e6.tex`。主題別の現行知識は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`、`research/cayley_lg_connections.md`。

**最優先は研究・論文を数学的に面白くすること。優先的戦略は多様な話題との具体的な関連を探し、証明可能な数学へ育てること。** 意外な同型・共通構造、新しい問い・方法を重視し、名称や定理数の増加を目的にしない。正確性を犠牲にしない。既存の八次元成分分類の技術的完遂が、面白い接続より自動的に優先されるわけではない。

公表価値ある成果は同じ日本語LuaLaTeX主論文へ統合する。既存の価値ある数学と必要証明を削除しない。証明済み、仮定付き、未完成、予想、計算的観察を区別する。一次文献の仮定・適用範囲・既知性を確認し、原稿に証明があること、今回点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・方針・要約にも反映する。

ノートは現行知識と再開に必要な式・障害・比較を記し、日誌・会話・履歴・重複証明を蓄積しない。現行方針・主論文・ノート・必要最小限のコードと証明書で自己完結させる。旧ZIP・旧原稿・PDF・キャッシュ・ログ・組版中間物をGitに含めない。

GitHub mainが正本。**push済み内容をLibraryへ保存しない。** push失敗で未保存成果の保全が必要な場合のみ緊急退避を認める。既存Libraryファイルを明示指示なしに削除しない。約15分または区切りで通常のfast-forward保存を行い、不要なPR・Actions・force pushを使わない。競合は共有変更を確認して両立させる。生成・検証・commit・push・Library保存を別状態として報告する。

全H3分類は別repo `uedakazushi/nc-cubic-moduli` を正本とする。並列研究と同一repoの共有変更を混同しない。

**現在の新しい到達点。** LG等位面を三角境界付き三次曲面へコンパクト化し、0→Z delta_infty→H2(U)→D4(-1)→0を得た。指定D4退化の局所Milnor fiberの包含がPicard直交補へ整数格子同型を与える。巡回置換は判別群の三非零元を回して外部trialityを検出する。これは退化を指定した比較で、全域の標準分裂ではない。混合Hodgeは重み2の4方向と重み4の1方向で、拡大分裂は未主張。

Boalch–Palubaの既知G2実現を対称LG族へ適用すると、regular範囲で各等位面はG2指標多様体の三成分の一つ。unipotent退化の底alpha=beta=6ではD4の(lambda,h)=(2,7/2)とA2の(-1/4,1/8)が同じ退化の成分となる。後者はS5被覆に用いたsimple fold。既知定理の再発見とせず、今回の具体的な接続として位置付ける。

最優先の次の着手は、G2のbraid作用をLG座標へ移し、局所/Picardのtriality・vanishing cycleと比較すること。三成分間の交換monodromyと一成分内の作用を分ける。並行して境界radicalのlog2形式period、混合Hodge拡大、Gauss–Manin、局所D4のmatrix factorization/Fukaya比較を調べる。G2量子代数や圏同値を古典同型から推測しない。

Cayleyのトーラスmodular作用、pillowcaseとelliptopeの実sheet一意性、nearly Kählerの共通凸体を保持する。後者の追加の圏的・計量的対応は未構成。被覆のbranchとCasimir値衝突、Wの臨界値衝突は区別する。重い大域消去の反復を目的化しない。

既存のAW/Fricke、root Poisson括弧9倍、N5²M5とS5×S5、七次元正常形・八次元形式族を保持する。純粋qの非Casimir切断障害と固定pointed心へのVieta非延長を無視した反復はしない。全H3 admissibility・intrinsic降下・全境界は未解決。

今回実行済みは `verify_lg_picard_g2.py` のみ。Q・整数行列のPASSは `lg_picard_g2_certificate.json`。位相・ADE・Hodge・G2定理の通常証明を計算だけの証明としない。新節単体はLuaLaTeX4頁、内部参照と画像を確認。旧24検証器全再実行と主論文全体の今回の組版は未実施。保存後にinput・参照・必要ファイルを確認する。
