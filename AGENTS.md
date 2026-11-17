# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v27。最初に `00_research_plan.md` を読む。主論文は `papers/nc-cubic-e6.tex`。境界Pell・局所化・絡み目・正規化は `research/boundary_pell_dynamics.md`、四period/trialityは `research/conic_period_coordinates.md`、LG/G2は `research/cayley_lg_connections.md`。その他は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`。

**最優先は数学的に面白くすること。多様な分野との具体的接続を優先し、名称や定理数の増加を目的にしない。** 意外な同型・共通構造、新しい問いや方法を重視する。正確性を犠牲にしない。八次元成分分類は保持するが、完成を他分野研究の前提にしない。

公表価値ある成果は同じ日本語LuaLaTeX主論文へ統合し、既存の価値ある結果・必要証明を削除しない。証明済み、仮定付き、未完成、予想、計算的観察を区別する。一次文献の仮定・適用範囲・書誌を確認し、原稿の証明、今回の点検、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。
ノートは現行知識・式・障害・反例・文献比較を保持し、日誌・会話・履歴・重複証明を蓄積しない。現行一式だけで再開できるようにし、旧ZIP・旧原稿・PDF・ログ・キャッシュ・コンパイル中間物をGitに含めない。

GitHub mainが正本。**push済み内容をLibraryへ保存しない。** push失敗で未保存成果の保全が必要な場合のみ緊急退避を認め、既存Libraryファイルを明示指示なしに削除しない。約15分または数学的区切りで通常のfast-forward保存を行う。不要なPR・Actions・force pushを使わず、競合は共有変更と両立させる。生成・検証・commit・push・Library保存を別状態で報告する。全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本。

**現在の新しい局所模型。** 滑らかなconic C0={v=kappa}をg^-nで動かすと、閉包はn≥1で一つの境界頂点p_wに二つのPuiseux対(b_n,c_n)の枝を持つ。M^n=[[a,-b],[-b,c]]、M=[[1,-2],[-2,5]]。次反復は(b,c)→(b+2c,2b+5c)。各枝の局所パラメータはx=2^-b rho^-a s^b(1+O(s)), y=2^-c rho^-b s^c(1+O(s))で、rho±=kappa±sqrt(kappa²−1)。toric例外曲線のz=y^b/x^c=rho±に元の係数が残る。
linkはT(2b,2c)、二成分T(b,c)、linking bc。delta=1+2bc−b−c、mu=2delta−1、conductorは両枝s^delta。Milnor fiberはgenus delta−1、境界2、H1 monodromyの位数2bc。各nの有限位数作用とnを動かす双曲型gを混同しない。
正規化層B_n=nu_*O_P1のproper対象増大率log Lambda、欠損Z_n=B_n/O_barC_nはp_wに支持され長さdelta、率2log Lambda。開制限ではB_nは二項自由解消、Z_n=0。対象列の率であって自己関手entropyではない。
Chebyshev実morsificationはdelta個の零level nodeとdelta−1個の極値を持つ。Casalsの既知定理からlocal Weinstein pairのMilnor Lagrangian曲面とmu thimbleを得る。二handleで閉じる局所四多様体のEuler3と元のUのEuler6を混同しない。局所模型の存在からglobal mirrorやgのwrapped作用を推論しない。

**次の優先課題。** n=1のT(4,10) divideの交叉・thimble配置・microlocal sheafのquiverを具体的に計算し、正規化完全列/conductorに対応するexact triangleを探す。反復間のtoric共通解消と標識付き例外曲線を比較し、exact cobordism・stop変更・局所化関手のどれが構成できるか判定する。まず対象と射を特定し、個数だけから圏同値を言わない。
並行して三成分の3捩れperiod差の幾何学化、Klein7/21、Spin8→G2 character、全rank五接続を保持する。有理Hodge同型から曲面・圏同値を推論しない。

**解決済みの障害を繰り返さない。** 通常のPerf(U)のDHKK entropyは零。正の古典entropyをそのまま移すのではなく、射のpole/action filtrationの線型比較とgへの同変性が必要。閉包列の2log Lambdaを自己関手entropyと呼ばない。holomorphic symplectic保存とexact Liouville自己同型も別。
既存のAW/Fricke、Poisson9倍、七次元正常形・八次元形式族、N5²M5とS5×S5、D4/Cayley、G2、全periodと円分性を保持する。純粋qの非Casimir切断障害、固定pointed心へのVieta非延長を尊重する。全H3 admissibility・intrinsic降下・全境界は未完成。

今回実行済みは `verify_boundary_torus_links.py`。Q・Zの記号計算PASSは `boundary_torus_links_certificate.json`。全係数先頭式、帰納式、24反復、n1 Jacobi27・conductor14、MilnorとChebyshevを検算した。解析/位相・全nの証明・DHKK・Casalsを有限検算による形式証明としない。新節単体LuaLaTeX5頁の全画像・内部参照・overfullなしを確認。旧31検証器の今回全再実行、主論文全体の今回の組版、独立査読、新規性網羅調査は未実施。保存後にmain ref、入力先、必要ファイル、実行コードとの一致と旧証明の保持を確認する。
