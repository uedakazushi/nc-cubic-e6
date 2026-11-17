# Codex研究指示 — nc-cubic-e6

2026-11-18 / e6-connections-v30。最初に `00_research_plan.md` を読む。主論文は `papers/nc-cubic-e6.tex`。境界解析・MF・Prymは `research/boundary_analytic_moduli.md`、Pell・局所化・linkは `research/boundary_pell_dynamics.md`。全periodは `research/conic_period_coordinates.md`、LG/G2は `research/cayley_lg_connections.md`。他の基礎・文献は `research/research_notes.md`, `fricke_daha_comparison.md`, `poisson_order_notes.md`。

**最優先は数学的に面白くすること。多様な分野との具体的な接続を優先し、名称や定理数を増やすことを目的にしない。** 意外な同型・共通構造、新しい問い・方法を重視し、正確性を犠牲にしない。八次元成分分類を保持するが、その完成を他分野研究の前提にしない。
公表価値ある結果は同じ日本語LuaLaTeX主論文へ統合し、既存の価値ある成果・必要証明を削除しない。証明済み、仮定付き、未完成、予想、計算的観察を区別する。一次文献の適用範囲を確認し、原稿の証明、今回の点検、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針へ反映する。

ノートは現行の式・知識・反例・障害・文献比較を保持し、日誌・会話・履歴・重複証明を蓄積しない。現行方針・ノート・論文と最小限の計算資産で自己完結させる。旧ZIP・旧原稿・PDF・ログ・キャッシュ・中間生成物をGitへ入れない。
GitHub mainが正本。**pushした内容をLibraryへ保存しない。** push失敗で未保存成果の保全が必要な場合のみ緊急退避できる。既存Library資料を明示指示なしに削除しない。約15分または区切りで通常のfast-forward保存。force push、不要なPR・Actionsを使わず、共有変更と競合させない。生成・検証・commit・push・Library保存を分ける。全H3分類は別repo `uedakazushi/nc-cubic-moduli` が正本。

**現行の幾何学的到達点。** 重み付き模型F_nk=1の射影Milnor曲線Cは、z=y^b/x^cを保って付随楕円E_kへ写せない。必要な平方類は[x]で、a²=xの連結二次被覆tildeCを取ればz=y^b/a^(2c),eta=y^(b/2)/a^(3c)という次数2bcの写像が得られる。deckがEの逆元に対応するのでEはPrymのisogeny/Hodge因子。任意の別のC→Eの不存在を主張しない。
全n共通のCiani四次X4+Y4−2kappa X²Y²=Z4へ次数bc/2で写り、Jac(Ciani)~Ei²×D_k。D_k→E_kは(z,eta)=(r²,rT)の2isogeny。Prym内にEi×D_kが入る。楕円周期は(kappa²−1)Pi''+2kappa Pi'+Pi/4=0。これはkappa変動で、固定kappaのMilnor値monodromyやLG level hの周期とは別。

**実germについての新しい確定事項。** mu27,tau24例と主部tau27は、Hua–Keller最終版Thm5.9の通常Z-graded dg特異点圏でHH0次元24対27となりMorita非同値。この結論は一般孤立超曲面の定理の適用であり、flop/NCCRの仮定は使わない。
二周期MFの相対HH=Jacobianと整数次数付きdg圏の絶対HH0=Tjurinaを入れ替えない。strict二周期MFとZdgの全periodization/忘却比較は未構成。重み付きMFの(n,K)分類を実高重みgermへ無条件に延長しない。

最優先の次の着手は、上の二種類のdg/Hochschild構造の比較、実n1のkappa/h変動でのTjurina跳躍とJacobian積、[f]の役割。並行してb2,c5のPrym楕円因子のpullback kernel・誘導偏極・整数格子、PF monodromyとlevel2標識を調べる。高重み変形でPrym因子が残るかは別問題とする。isogeny/Hodge因子だけからMF部分圏やHMSを推論しない。

既存の閾値、link、conductor、normalization、局所Weinsteinを保持する。通常affine Perf entropyは零、射filtration率log Lambda、proper閉包対象列率2log Lambdaは別。局所MF・局所Weinstein・大域H3を区別し、mirror比較には特定gとの同変性とfiltration制御が必要。
AW/Fricke、Poisson9倍、七次元正常形・八次元形式族、N5²M5とS5×S5、Cayley/D4、Milnor–Picard、G2 D4/A2、全四period、triality三成分Hodge比較を保持。全H3開性・降下・全境界は未完成。

今回は `verify_boundary_prym.py` を実行しPASS。Q上の恒等式・指標・PF完全微分・Pell整数式、元Vietaからのmu27/tau24を再計算。被覆・norm・Hodge・dg復元を計算だけの証明としない。新節単体LuaLaTeX4頁、全頁画像・内部参照・overfullなしを点検。主論文全体の今回の組版、旧34検証器全再実行、独立査読、新規性網羅確認は未実施。保存後main ref・input・必要ファイル・実行コードのblob SHAを確認する。
