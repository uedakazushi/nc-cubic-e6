# Codex研究指示 — nc-cubic-e6

2026-11-18 / e6-connections-v29。最初に `00_research_plan.md` を読む。主論文は `papers/nc-cubic-e6.tex`。境界の解析modulus・閾値・MF・二捩れ楕円曲線は `research/boundary_analytic_moduli.md`、Pell・局所化・linkは `research/boundary_pell_dynamics.md`。全periodは `research/conic_period_coordinates.md`、LG/G2は `research/cayley_lg_connections.md`。他の基礎・文献は `research/research_notes.md`, `fricke_daha_comparison.md`, `poisson_order_notes.md`。

**最優先は数学的に面白くすること。多様な分野との具体的な接続を優先し、名称や定理数の増加を目的にしない。** 意外な同型・共通構造、新しい問い・方法を重視する。正確性を犠牲にしない。八次元成分分類は保持するが、その完成を他分野研究の前提にしない。

公表価値ある成果を同じ日本語LuaLaTeX主論文へ統合する。価値ある既存結果・必要証明を削除しない。証明済み、仮定付き、未完成、予想、計算的観察を区別する。一次文献の適用仮定を確認し、原稿の証明、今回の点検、計算実行、独立査読を分ける。誤りは依存する本文・方針・要約にも反映する。

ノートは現行の式・知識・反例・障害・文献比較を保持し、日誌・会話・履歴・重複証明を蓄積しない。現行方針・論文・ノートと最小限の計算資産で自己完結させる。旧ZIP・旧原稿・PDF・ログ・キャッシュ・組版中間物はGitへ入れない。
GitHub mainが正本。**pushした内容をLibraryへ保存しない。** push失敗で未保存成果を保全する必要がある場合のみ緊急退避できる。既存Library資料を明示指示なしに削除しない。約15分または区切りで通常のfast-forward保存。force push、不要なPR・Actionsを使わず、競合したら共有変更と両立させる。生成・検証・commit・push・Library保存を別状態で報告する。全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本。

**現在の核心：実germと重み付き主部を分ける。** 二枝主部F_nk=y^(2b)−2kappa x^c y^b+x^(2c)には解析的不変量K=kappa²がある。重み付き模型の二周期MFは(n,K)でdg Morita分類される。HHを次元だけでなく代数として使い、Euler式でJac=TjurinaとしてMather–Yauを適用する。一般高重みgermではこのEuler式がないので、同じ証明を流用しない。

実際のA=B=C=0,h=1、初期v=2、n=1の境界germはmu27,tau24。主部はmu=tau27なので接触非同値。元のVieta式からresultantを取り、重み18,15の正則初期列とsocle26により有限jet計算が厳密であることを保証した。**tau差だけで標識なし二周期MFの非同値を結論しない**。Tjurina環にはJacobian環中の指定類[f]が必要である。

解消上の四点0,infty,rho±から補助楕円曲線eta²=z(z²−2kappa z+1)を作り、T=(0,0)を標識。KはY0(2)粗modulusでj=64(4K−3)³/(K−1)。同じj1728のK0と9/8でもMF模型は非同値。2isogeny K↦K/(K−1)も一般にMF同値を与えない。元の反標準楕円境界、Milnor quotient、MFの部分圏と同一視しない。

最優先の次の着手は、実mu27,tau24例のJacobian積と指定類[f]をmodelと比較し、Hua–Keller等の復元定理がどの追加構造で適用できるか一次文献から確認すること。n=1のkappa,hの変動で厳密有限jetのTjurina跳躍を調べる。未検証の復元定理や楕円HMSを輸入しない。
並行して四点・level2楕円modulus・高次A-infinity積の間に実際の対応があるかを探す。同じmoduli空間というだけで圏同値を主張しない。局所Weinstein、MF、大域H3の三圏を区別してfiltered局所化を比較する。

境界閾値(b+c)/(2bc)の減衰率log Lambda、実MFのHH次元(2b−1)(2c−1)の増大率2log Lambdaを保持する。通常のaffine Perf entropyは零、射filtrationの歪みとproper閉包対象列の率は別。全H2・periodを固定するgでも境界Pell力学は正entropy。既存の二cusp、T(2b,2c)、conductor、normalization、局所Weinstein模型を削除しない。
旧成果AW/Fricke、Poisson9倍、七次元正常形・八次元形式族、N5²M5とS5×S5、Cayley/D4、Milnor–Picard、G2 D4/A2、全四period、triality三成分比較を保持。全H3開性・降下・全境界は未完成。

今回実行済みは `verify_boundary_thresholds.py` と `verify_boundary_analytic_moduli.py`。新計算はQ/Q(sqrt2)上の厳密恒等式とrank18/21、mu27/tau24。理論的分類・Morita不変性・strictnessを有限計算だけの検証としない。新節単体LuaLaTeX5頁、画像・内部参照・overfullなしを点検。主論文全体の今回の組版、既存32検証器全再実行、独立査読、新規性の網羅調査は未実施。保存後にmain ref、input、必要ファイル、実行コードのblob SHAを確認する。
