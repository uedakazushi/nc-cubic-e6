# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v25。最初に `00_research_plan.md` を読む。主論文は `papers/nc-cubic-e6.tex`。現行の境界力学は `research/boundary_pell_dynamics.md`、四周期・triality・三成分Hodge比較は `research/conic_period_coordinates.md`、LG/G2/braidの基礎は `research/cayley_lg_connections.md`。他分野は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`。

**最優先は数学的に面白くすること。多様な話題との具体的接続を優先し、名称や定理数の増加を目的にしない。** 意外な同型・共通構造、新たな問いや方法を重視する。正確性を犠牲にしない。八次元E6成分の分類は保持するが、その完成を他分野との比較の前提にしない。

公表価値ある成果は同じ日本語LuaLaTeX主論文へ統合する。価値ある旧結果・必要証明を削除しない。証明済み、仮定付き、未完成、予想、計算的観察を区別し、一次文献の仮定・適用範囲・既知性を確認する。原稿に証明があること、今回点検したこと、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。
ノートは現行知識、式、障害、反例、文献比較を保持し、日誌・会話・履歴・重複証明を蓄積しない。現行方針・論文・ノート・最小限コードと証明書だけで再開可能にする。旧ZIP・旧原稿・PDF・ログ・キャッシュ・組版中間物をGitへ入れない。

GitHub mainが正本。**pushした内容はLibraryへ保存しない。** push失敗で未保存成果の保全が必要な場合だけ緊急退避できる。既存Libraryファイルを明示指示なしに削除しない。約15分または数学的区切りで通常のfast-forward保存。不要なPR・Actions・force pushを使わず、共有変更と競合したら両立させる。生成・検証・commit・push・Library保存を別状態として報告する。全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本。

**現在の新しい到達点。** g=iota_v iota_w iota_u iota_wは全H2・periodで恒等、正entropyを持つ。この同じgの境界単項式付値はTheta(r,t)=(|r|,|t|,|r+t|)を介してM=[[1,-2],[-2,5]]で動く。一般tropical線型化はJang、境界力学はCantat–Lorayの既知理論。ここでは特定語の最小次数・極・抽出深さを明示した。
最小affine次数は1,7,41,239,...、d_(n+2)=6d_(n+1)−d_n。最高項がu,vのみなのでgr O(U)=C[u,v,w]/(uvw)でも消えず、単なる表示次数でなく最小次数である。射影hyperplaneとの交点次数はn≥1で2d_n、n=0は3。
拡大・縮小固有付値は二次無理方向で、射影境界はnorth–south型、有理方向に周期点なし。そのため指定Sを支配する有限境界point blow-upでは正則自己同型へ延長できない。**algebraic stabilityの不存在、全別コンパクト化の不存在を意味しない。**
g_*^n ord(D_w)の一つの付値の抽出に必要なcorner blow-upは最小4n回。極次数は指数増大してもこの抽出深さは線型。反復写像の全indeterminacyの解消回数と混同しない。

優先する次の着手は、一Vietaの局所corner変換をwrapped Fukaya・境界birational correspondence・非可換局所化の対象の像と比較すること。古典entropyの値から圏的entropyを推測で断定しない。一般hyperbolic語の連分数と抽出深さの比較も有望だが既知の一般理論を先に照合する。
並行して三成分の3捩れperiod差を境界線束の変更・有限被覆・代数的対応として実現できるか調べる。Klein7/21のline配置とgluingから始め、有理Hodge同型から曲面・導来同値を推論しない。

**保持すべき周期成果。** 一般conic標識で全四periodは(z1/z2,z2/z3,z3/z4,z3*z4)。対称族はB²−C²≠0 chart外なので別sectionでcompatible標識を構成し(eta,xi,eta,eta)を得る。trialityの不変→余不変はdiag(1,3)、isogeny (xi,eta)→(xi,eta³)のWeyl商はBP三成分写像。G2群の中心isogenyではない。共通の明示開集合では三成分の有理MHSは標識graded piece下で同型、Kleinとコンパニオンの整数拡大位数7,21,21。全域の標準VMHS同型や他成分の有限Hurwitz軌道は未主張。

AW/Fricke、Poisson9倍、七次元正常形・八次元形式族、N5²M5とS5×S5、D4/Cayley、G2のD4/A2、period円分性を保持する。純粋qの非Casimir障害と固定pointed心へのVieta非延長を無視して同じ方法を繰り返さない。全H3 admissibility・intrinsic降下・全境界は未完成。

今回実行したのは `verify_boundary_pell_dynamics.py`。全係数式、12 chamberの36恒等式、n=24までの整数反復と連分数を厳密確認しPASS。証明書は `boundary_pell_dynamics_certificate.json`。全n、付値不変性、射影引戻し、非正則化は通常証明であり、計算だけの形式検証ではない。新節単体LuaLaTeX4頁の画像・内部参照・overfullなしを確認。旧29検証器全再実行、全主論文の今回の組版、独立査読、網羅的新規性調査は未実施。保存後のref・input・必要ファイルと旧証明保持を確認する。
