# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v22。再開時は `00_research_plan.md` を最初に読む。主論文は `papers/nc-cubic-e6.tex`。現行知識は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`、`research/cayley_lg_connections.md`。

**最優先は研究・論文を数学的に面白くすること。優先的戦略は多様な話題との具体的な関連を探し、証明可能な数学へ育てること。** 意外な同型、共通構造、見通し、新しい問いや方法を重視する。名称や定理数を増やすことを目的にせず、正確性を犠牲にしない。八次元成分分類の完遂は保持するが、面白い接続より自動的に優先させない。

公表価値ある成果は同じ日本語LuaLaTeX主論文へ統合し、既存の数学と必要証明を削除しない。証明済み、仮定付き、未完成、予想、計算的観察を区別する。一次文献の仮定・適用範囲・既知性を確認し、原稿の証明、今回の点検、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。
ノートは現行知識と式・障害・比較を記し、日誌・会話・更新履歴・重複証明を蓄積しない。現行方針・主論文・ノート・必須コード・小証明書で自己完結させる。旧ZIP・旧原稿・PDF・キャッシュ・ログ・組版中間物をGitに含めない。

GitHub mainが正本。**push済み内容をLibraryへ保存しない。** push失敗で未保存成果の保全が必要な場合のみ緊急退避を認める。既存Libraryファイルを明示指示なしに削除しない。約15分または数学的区切りで通常のfast-forward保存を行い、不要なPR・Actions・force pushを使わない。競合は共有変更を確認して両立させる。生成・検証・commit・push・Library保存を別状態で報告する。
全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本であり、並列研究を混同しない。

**現在の新成果。** conic pencil上でomega=dlog z∧dlog aとなり、単純根間のmatching周期は2pi i log(z_+/z_-)。A=B=C=0のMorse球面はPi0=4pi asin sqrt(−2h)、境界周期Pi_infty=(2pi i)²。二解は2h(1+2h)y''+(1+4h)y'=0を満たし、rank2解局所系のmonodromyは無限二面体群で非分裂。これは全rank5ホモロジー作用の決定ではない。
指数化Q=exp(Pi0/(2pi i))はQ+Q^-1=2+8h。Friedman Proposition3.12によりLooijenga対の境界線束制限と比較できる。h=−1/10のQ=(3−4i)/5は非捩れで、当該fiberの有理MHSが非分裂と証明した。局所系非分裂と一fiberのMHS非分裂を区別する。

次の最優先は、三conic pencilのmatching cycleを組み合わせて内部D4の整数基底と全四periodを明示すること。四根の差だけで全rank4を得たと推測せず、u=±1の退化や他pencilのcycleを確認する。球面の交叉を既存Milnor–Picard比較と合わせ、指数化periodを境界線束のgluingから独立に照合する。
並行してFriedman/Gross–Hacking–Keel、Lai–Zhou mirror period、Karwa–Lai非Archimedean periodの適用条件を確認し、具体的比較を探す。良い還元モデルやSYZ・mirror同値を今回構成したとはしない。

保持する構造：Cayleyのトーラス指標多様体、D4ミニバーサル変形、指定退化でのMilnor–Picard整数同型、外部triality、重み4+1、G2退化内のD4/A2、二種類のB3、Chebyshev、Klein軌道S7、境界周期。成分交換braid、固定fiber Hurwitz、今回のh解析接続はそれぞれ異なる。G2三成分全体と一LG等位面も区別する。
被覆のbranch、Casimir値衝突、Wの臨界値衝突は別現象。固定pointed H3心へのVieta非延長や純粋qの非Casimir障害を無視した方法を反復しない。一般変形・心の変更は否定されていない。
既存の七次元正常形・八次元形式族、AW/Fricke、root括弧9倍、N5²M5とS5×S5を保持する。全H3 admissibility・intrinsic降下・全境界は未完成で、今回の旧結果独立再監査はしていない。

今回実行済みは `verify_logarithmic_periods.py`。厳密PASSは `logarithmic_periods_certificate.json`。球面構成・積分・接続・Hodge証明を有限計算だけの証明としない。新節単体はLuaLaTeX4頁、全頁画像・内部参照・overfullなしを確認。旧26検証器全再実行、主論文全体の今回の組版、独立査読、新規性の網羅調査は未実施。保存後にinput・参照・必要ファイル・GitHub refを確認する。
