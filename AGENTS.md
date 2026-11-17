# Codex研究指示 — nc-cubic-e6

2026-11-17 / e6-connections-v26。最初に `00_research_plan.md` を読む。主論文は `papers/nc-cubic-e6.tex`。境界Pell・局所化・entropyは `research/boundary_pell_dynamics.md`、四period・trialityは `research/conic_period_coordinates.md`、LG/G2は `research/cayley_lg_connections.md`。その他は `research/research_notes.md`、`research/fricke_daha_comparison.md`、`research/poisson_order_notes.md`。

**最優先は数学的に面白くすること。多様な分野との具体的接続を優先し、名称や定理数の増加を目的化しない。** 意外な同型・共通構造、新しい問い・方法を重視する。正確性を犠牲にしない。八次元成分分類は保持するが、その完成を他分野との比較の前提にしない。

公表価値ある成果は同じ日本語LuaLaTeX主論文へ統合し、価値ある旧結果・必要証明を削除しない。証明済み、仮定付き、未完成、予想、計算的観察を区別する。一次文献の仮定と適用範囲を確認し、原稿に証明があること、今回点検したこと、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。

ノートは現行知識・式・反例・障害・文献比較を保持し、日誌・会話・履歴・重複証明を蓄積しない。現行方針・論文・ノート・必要最小限のコードと証明書で自己完結させる。旧ZIP・旧原稿・PDF・ログ・キャッシュ・組版中間物をGitへ入れない。
GitHub mainが正本。**pushした内容はLibraryに保存しない。** push失敗で未保存成果を保全する必要がある場合のみ緊急退避できる。既存Library資料を明示指示なしに削除しない。約15分または区切りで通常のfast-forward保存。force push、不要なPR・Actionsを使わず、共有変更と競合したら両立させる。生成・検証・commit・push・Library保存を別状態で報告する。全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本。

**現在の確定した区別。** g=iota_v iota_w iota_u iota_wは全H2・periodを固定するが境界付値ではM=[[1,-2],[-2,5]]で動く。最小次数d_n=1,7,41,...、Lambda=3+2sqrt2。無理固有方向、有理方向に周期点なし、指定Sの有限境界blow-upで非正則化、一付値のcorner深さ4nを保持する。

**通常のアフィン圏entropyの正値を目指さない。** 任意の非空affine自己射はPerf(X)の生成元O_Xを固定し、DHKK h_t=0である。これは生成元のEnd環の作用が恒等という意味ではない。Exact同値で移したmirror関手の通常entropyも零。
極filtration F_mR=H0(S,O(mD))/s_D^mは最小多項式次数、dim F_m=(3m²+3m+2)/2。特定gの射歪み倍率ell(n)=d_n、率log Lambda。有限生成元・線型同値filtrationで不変。一様な加法shiftによる保存は不可能。sigma^n(F1)の次元は4のままで、指数増大するのは必要な極次数である。

C0={v=kappa}の反復逆像は全て同じsmooth rational affine曲線。閉包class P_n=c_nD_u+b_nD_v+d_nD_w、次数2d_n、算術種数1+2b_nc_n−d_n。特異性は境界にのみあり、種数はlocal delta総和。proper split generatorから閉包構造層を作るDHKK複雑度率は2log Lambda、開曲面へ制限すれば[R→R]で複雑度≤2。**閉包列を自己関手の反復像と示したわけではなく、2log Lambdaを自己関手entropyと呼ばない。** 個別Puiseux型も未分類。
HH0とHH2のfiltered歪みはlog Lambda、HP_even rank6は恒等、HP_odd=0。これらは可換中心曲面での結論で、元の非可換H3圏の自己同値ではない。

**次の優先着手。** Côté–Kartalの局所化filtrationを具体化し、一Vietaのmirror対象LとEnd(L)を指定して、poleとReeb/actionを両方向に線型比較できるか、特定gへの同変性があるかを調べる。静的growth関数の比較だけでは十分でない。holomorphic symplectic保存からLiouville exact自己同型を推論しない。
並行して閉包曲線のnormalizationの端点、Puiseux型、枝間交叉、linkをn=1,2で調べ、Pell連分数との関係を証明する。種数公式の数値一致だけから二枝・torus knot型を結論しない。
三G2成分の3捩れperiod差を有限被覆・境界線束の変更・代数的対応へ移す問題、Klein7/21、Spin8/G2、全rank五接続も維持する。

旧成果AW/Fricke、Poisson9倍、七次元正常形・八次元形式族、N5²M5とS5×S5、Cayley/D4、Milnor–Picard、G2 D4/A2、全四period、triality isogenyを保持する。純粋q変形障害と固定pointed心へのVieta非延長を無視した反復をしない。全H3 admissibility・intrinsic降下・全境界は未完成。

今回実行したのは `verify_localization_entropy.py`。全係数一反復、Hilbert値、交叉式、n=0..24の整数行列・種数がPASS。証明書は `localization_entropy_certificate.json`。DHKK・proper比較・HKR・normalizationは通常証明と先行理論であり、有限計算だけの形式検証ではない。新節単体LuaLaTeX5頁、画像・内部参照・overfullなしを点検。主論文全体の今回の組版、旧30検証器全再実行、独立査読、網羅的新規性調査は未実施。保存後にmain ref、input、必要ファイル、実行コードとの一致を確認する。
