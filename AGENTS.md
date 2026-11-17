# Codex研究指示 — nc-cubic-e6

2026-11-17 / v18。再開時は `00_research_plan.md` を最初に読み、主題に応じて `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`、`papers/nc-cubic-e6.tex` を読む。

このリポジトリは楕円E6量子化成分の独立した正本であり、全H3分類は `uedakazushi/nc-cubic-moduli` を正本とする。分類側のCodexと同じリポジトリを並列編集しない。

面白さ・数学的価値・正確性・新規性・実現可能性を総合して方針を更新する。関連分野との類似を列挙するだけでなく、明示的な同型、変形、圏的対応または障害を証明する。公表価値ある関連分野研究は同じ主論文に統合する。証明済み・追加仮定付き・未解決・計算的観察を区別し、一次文献を確認する。誤りは本文・方針・ノートに反映し、作業日誌を蓄積しない。日本語LuaLaTeXを原則とし、既存の数学的成果と必要証明を保持する。

再開用の一式は現行方針・ノート・主論文と必須検証コードで自己完結させる。旧ZIP・旧原稿・PDF・キャッシュ・生成物はGitに含めない。研究区切りではGitHub mainを正本にcommit/pushし、**push済み内容はLibraryへ保存しない**。push失敗で未保存成果を保全する必要がある場合のみLibraryへの緊急退避を認める。既存Libraryファイルを明示指示なしに削除しない。

約15分ごと、または数学的な区切りで整理し、PR・Actions・force pushを使わずmainへ通常のfast-forwardでpushする。競合したらfetchして共有変更と両立させる。生成・検証・commit・pushを区別し、未実行の検証をPASSと言わない。

現在確定した関連分野成果は、AW/Fricke/Vieta、D4⊂E6、Q=q exp(h)からの正確なPoisson括弧9倍、相対Poisson臨界schemeの有限平坦次数15、一次元表現の有限平坦次数5、Casimir臨界値判別式N5²M5、およびN5とM5の独立な幾何学的S5×S5 monodromyである。Brown–Gordonから固定Fricke sliceのsmooth locus上の中心fiber代数は同型。全DでM3・有限globaldimになることは別途未確認。

**既知の障害を繰り返さない。** G=Omega+beta X+gamma Y+delta Z+epsilonは、beta=gamma=delta=0以外では指定した純粋q変形の平坦商に一次で持ち上がらない。Vietaのsigma(z)はPBW次数2、sigma(Z)は次数6なので固定pointed H3心に延長しない。これらは一般H3変形や導来対応の非存在ではない。

さらに固定包絡a=b=c=0では、総中心のPoisson零点が五節点と五滑らかCasimir臨界点に分かれ、A1中心切断のH3可否と二次接触／一次横断を区別できた。VietaとA4は二つの四点集合にS4を作用させる。既存H3判定に依存する部分と独立検算を区別する。次は一般a,b,cでの零点schemeと七次元結節因子への接続を調べる。

最優先は、既に確定した二つの独立なS5の分岐divisorの具体式と交叉を効率的なresultant/trace計算で求め、Painlevé VIのtrace判別式との比較を完成すること。一般a,b,cでの局所orderとH3 admissibilityは未完成。続いて、同時Sklyanin方向による障害の相殺を既存8変数族から抽出し、affine modular作用を境界の双有理変更・導来圏の心の変更で実現すること。次にCasimirごとのAzumaya locusと表現論、skein/DAHA特殊化・cluster/mirror比較、全H3 admissibility・intrinsic降下・全境界へ進む。固定包絡の五SNC結節因子と七次元族の既約六次元因子も保持し、中心特異性をH3境界と混同しない。

今回新規に実行したのは `verify_companion_s5.py` に対応する二素数の厳密計算で、結果は `companion_s5_certificate.json` に記録。既存五検証器は `computations/connections_validation.json` に保存された前回のPASSであり、`verify_all.py` の全23件を今回実行したとはしない。主論文の入力節・検算依存・既存証明を欠落させない。
