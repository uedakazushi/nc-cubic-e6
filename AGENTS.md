# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v21。再開時は `00_research_plan.md` を最初に読む。主論文は `papers/nc-cubic-e6.tex`。主題別の現行知識は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`、`research/cayley_lg_connections.md`。

**最優先は数学的に面白くすること。優先的戦略は多様な話題との具体的な関連を探し、証明可能な数学へ育てること。** 意外な同型、共通構造、新しい問いや方法を重視する。名称・定理数を増やすことを目的化しない。正確性を犠牲にせず、既定の分類の技術的完遂が面白い接続より自動的に優先されるとは考えない。

公表価値ある成果は同じ日本語LuaLaTeX主論文へ統合する。既存の成果と必要証明を削除しない。証明済み・仮定付き・未完成・予想・計算的観察を区別し、一次資料の仮定と適用範囲を確認する。原稿に証明があること、今回の点検、計算実行、独立査読を混同しない。誤りは依存する本文・方針・要約にも反映する。
ノートは現行知識と必要な式・障害・比較を整理し、日誌・会話・履歴・重複証明を蓄積しない。現行方針・主論文・ノート・必須コードと証明書で再開できるようにする。旧ZIP・旧原稿・PDF・ログ・キャッシュ・組版中間物はGitに含めない。

GitHub mainが正本。**pushした内容をLibraryに保存しない。** push失敗で未保存成果を保全する場合のみ緊急退避を認める。既存Libraryファイルを明示指示なしに削除しない。約15分または数学的区切りで通常のfast-forward保存を行い、不要なPR・Actions・force pushを使わない。共有変更と両立させ、生成・検証・commit・push・Library保存を区別する。
全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本。同一repoの並列編集を混同しない。

**現在の接続。** LGのCayley分岐源、D4ミニバーサル衝突、指定退化のMilnor–Picard整数同型、外部triality、MHS重みの4+1、G2のD4/A2共通退化を保持する。
三成分のラベル三次式はz³−3Pz+QでA2 root cover。底のloopによるB3はラベルにS3を作用させる。これと、LGのW・Poisson・留数形式を保ち成分を一つずつ固定するHurwitzのB3は**違う作用**。後者はPSL2Zを経由する。
Hurwitz B1はu固定のconic pencil上でtrace2uのSL2行列に平行移動で移り、反復はChebyshevで表せる。二生成元全体の線型化ではない。
既知Klein七点軌道の置換像はS7（5040）。一つの表現の像G2(2)'≅U3(3)（6048）やKlein群168と同一視しない。七点自体・八元数/Fano実現は先行研究にある。原稿に明示した置換群の個別新規性は未確認。
境界の原始cycle delta_inftyに正規化留数形式を積分すると(2pi i)²。Hurwitzはdelta_inftyを固定しD4商に降りる。内部四周期・全Gauss–Manin系・MHS拡大分裂は未計算。

最優先の次の着手は、conic pencilと消滅点の局所模型を用いた内部一周期の還元・微分・漸近である。並行して成分交換S3、Hurwitz PSL2Z、判別群triality、七点S7を実際の比較写像で結ぶ。消滅路による基底依存性を明記し、同じ抽象群だから同じ作用とはしない。
Fano/八元数、他二成分のQ(sqrt21)、実sheetの安定性、Cayley modular作用、matrix factorization/Fukayaへの比較も具体例から探す。古典G2同型から量子代数・導来圏の同値を推測しない。

既存の七次元正常形・八次元形式族、AW/Fricke、Poisson9倍、N5²M5とS5×S5、結節因子は保持する。被覆のbranch、Casimir値衝突、W臨界値衝突を分ける。純粋qの非Casimir持上げ障害と固定pointed心へのVieta障害を無視した方法の反復はしない。一般変形や心の変更は否定されていない。全H3 admissibility・intrinsic降下・全境界は未解決。

今回実行済みは `verify_g2_braids_periods.py`。Q恒等式・有限置換群のPASSは `g2_braids_periods_certificate.json`。configuration spaceの位相、原始トーラス、解析積分、全次数漸化式は本文の通常証明。新節はLuaLaTeX4頁、内部参照・画像・overfullなしを確認。旧25検証器の全再実行と主論文全体の今回の組版は未実施。保存後にinput・必要ファイル・参照を確認する。
