# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v19。再開時は `00_research_plan.md` を最初に読む。主論文は `papers/nc-cubic-e6.tex`。現行知識は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`、`research/cayley_lg_connections.md` に主題別に整理されている。

**最優先は、研究と論文を数学的に面白くすること。優先的な研究戦略は、なるべく多様な話題との関連を発見し、具体的な数学へ育てること。** 意外な同型・共通構造、概念的な見通し、新しい問いや方法を高く評価する。名称の類似を列挙したり、定理の数を増やしたりするだけでは達成にならない。正確性はこの優先順位で犠牲にしない。

既存の八次元E6成分の完全決定は保持するが、その技術的な完遂が他の面白い接続より自動的に優先されるわけではない。大域分類を完成しなければ他分野を研究できないとは考えない。具体的な写像、方程式、局所模型、作用、圏的対応、障害のいずれかを成果として求める。

公表価値ある関連分野研究は同じ主論文に統合する。日本語LuaLaTeXを原則とする。既存の価値ある成果と必要証明を削除しない。証明済み・仮定付き・未完成・予想・計算的観察を区別し、一次文献と適用範囲を確認する。原稿に証明があること、今回点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。

研究ノートは現在有効な知識と再開に必要な式・障害・比較を記す。日誌、過去の会話、更新履歴、重複証明を蓄積しない。現行方針・主論文・ノート・最小限の計算コードと証明書だけで再開可能にする。旧ZIP・旧原稿・PDF・キャッシュ・ログ・コンパイル中間物はGitに含めない。

GitHub mainが正本。**GitHubにpushした内容はLibraryに保存しない。** push失敗で未保存成果を保全する必要がある場合のみLibraryへの緊急退避を認める。既存Libraryファイルを明示指示なしに削除しない。約15分または数学的区切りで通常のfast-forward保存を行い、PR・Actions・force pushを不要に使わない。競合したら共有変更を確認して両立させる。生成・検証・commit・push・Library保存を別々に報告する。

本リポジトリは関連するE6成分研究の正本で、全H3分類は `uedakazushi/nc-cubic-moduli` を正本とする。他側の研究と同一repoの並列編集を混同しない。

現在の新しい共通模型は、一次元表現の勾配写像Phi=(vw-u,wu-v,uv-w)とH=uvw-(u²+v²+w²)/2。そのramification divisorはCayley三次曲面で閉トーラスのSL2指標多様体。四つの特殊fiberはD4局所長さ4と単純sheet1に分かれ、三係数は加法定数を除くミニバーサル変形。trialityの位数3作用、rank5 Jacobi留数対、実pillowcase、elliptope内部の単射性が同じ模型に現れる。

最も優先する探索は、局所D4 vanishing cycleとPicard D4の比較、trialityの圏的実現、LG留数/Gauss–Manin/mirror、Cayley modular作用の表現被覆への延長、実sheetと安定性である。nearly Kähler S3×S3にも同じelliptopeが現れるが、追加の幾何学的・圏的対応は未構成として扱う。型や名称が同じというだけで同値を主張しない。

**判別式を区別する。** 原点で五重被覆はetaleだがCasimir norm N5は四重根を持つ。被覆の分岐と観測値の衝突は別現象。LGの臨界値もCasimir値そのものではない。trace判別式の基底変換と局所模型を先に用い、重い消去計算を目的化しない。

既存のAW/Fricke/Vieta、Poisson括弧9倍、相対臨界rank15、N5²M5とS5×S5、七次元正常形・八次元形式族は保持する。純粋q変形の非Casimir切断障害、固定pointed H3心へのVieta非延長を無視して同じ方法を繰り返さない。これらは一般変形や心の変更を否定しない。全H3 admissibility・intrinsic降下・全境界は未解決。

今回実行済みなのは `verify_cayley_lg_connections.py`。有理数体上の記号計算PASSは `cayley_lg_connections_certificate.json` に記録。旧23検証器は今回全再実行していない。新節の独立LuaLaTeX wrapperは5頁で組版成功したが、本文外の二参照はwrapperでは未解決であり、全主論文の組版成功とはしない。入力先・文献キー・現行ファイルの欠落を保存後に確認する。
