# 研究方針：量子三次曲面・Fricke幾何・境界Prymの公表

2026-11-18 / publication-v33。**研究再開時は本書を最初に読む。**

GitHub main を正本とする。公表用原稿は日本語LuaLaTeXの三論文に分ける。研究ノートと計算資産を含む現在の一式から再開でき、旧版・会話履歴の取得を必要としない。

## I. 恒常的な研究原則と保存許可

以下は今回の論文構成とは独立した一般原則である。

1. 数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化する。目標・方針は柔軟に変更する。重要な変更には現在の理由と、元の目標の達成部分・残存部分を記すが、変更履歴は蓄積しない。分野間の接続は実際の写像・構造・障害で示し、名称や定理数を増やすことを目的にしない。
2. 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。主要主張の仮定、依存結果、証明の所在、未解決点を示す。原稿に証明があること、今回点検したこと、計算したこと、独立査読を区別する。誤りがあれば依存する本文・要約・方針も訂正する。
3. 公表前に一次文献を調べ、既知結果の仮定・範囲と本研究の貢献をIntroductionで具体的に比較する。書誌情報・文献内容・新規性を推測で補わない。文献PDFや検索出力の大量収録はしない。
4. 価値ある結果は十分な証明とともに現行論文に保持する。日本語LuaLaTeXを標準とし、著者欄は空欄とする。原稿は現在の成果を理解する順に構成し、数学的なまとまりと公表上の利点に応じて分割・統合する。未解決箇所を完成結果として扱わない。
5. ノートは現在有効な式、着想、補題、反例、失敗した方法の本質的障害、文献比較を整理する。日誌・会話・更新履歴にしない。再取得困難な情報は簡潔に残し、本文に十分な証明がある場合はその所在を参照する。
6. 再開に必要な目標・達成基準・主要到達点・核心・具体的な次の着手は本書に集約する。詳細は論文とノートに置き、ファイル名、記法、主張の状態を現行版で一致させる。
7. 継続用bundleは現行方針・ノート・論文・PDFと、理解・検証・再生成に必要な原稿、文献情報、コード、入力、小証明書だけで構成する。旧版、旧ZIP、バックアップ、変更履歴、ログ、キャッシュ、組版中間物を除く。軽量化のために数学的内容や検証可能性を削らない。固定容量・ページ数を目標にしない。
8. **研究の区切りで、ユーザーに再確認せず現行bundleを保存する許可がある。** 本研究では最新のユーザー指示に従い、GitHubの正本に加えて研究継続用bundleをLibraryへ保存する。既存Libraryファイルの削除は別操作であり、明示指示なく行わない。日付・版番号を付け、生成・検証・commit・push・保存を区別して報告する。配布前に入力、参照、ZIP整合性、必要な組版と計算を確認する。

GitHubは通常のfast-forwardで、約15分または作業の区切りにmainへ保存する。force push、不要なPR・Actionsを使わない。PDF・ZIP・ログをGitで追跡しない。

## II. 現在の目標と論文構成

目標は、三乗根量子三次曲面から得られた成果を、中心結果・仮定・既知理論との関係が読者に分かる三論文として公表できる状態へ進めることである。

| 原稿 | 中心結果 | 最優先の公表課題 |
|---|---|---|
| papers/nc-cubic-e6.tex | 七次元PBW正常形、条件付きHH²=8・HH³=0、八変数形式表示、R(1,3)中心切断との同定、反標準再構成、結節中心、AOU無限位数部分との比較 | H3/order認識の外部入力を監査し、証明範囲を固定する |
| papers/fricke-geometry.tex | AW/Frickeの規約、次数15と5の被覆、N5²M5とS5×S5、LG/D4、全四period、triality isogeny | 二五次被覆・整数周期の新規性と既知Fricke/DAHA理論との比較 |
| papers/cubic-boundary-prym.tex | Pell反復、境界二枝、局所化の成長、模型MF、実germ、Milnor二重被覆のPrymと偏極 | 境界からPrymまでの定理列と一次資料の最終監査 |

構成変更の理由は、従来の総合原稿で量子変形論・指標多様体・境界特異点という三つの中心結果が埋もれていたためである。既存の定理と証明は、現在の三論文のいずれかに保持する。共通の記法と文献データは papers/shared/ に置く。

元の「八次元E6成分を完全に決定する」という目標は、**R(1,3)型包絡の中心三次商と同じ一般表示成分の研究**として保持する。包絡7次元に切断1次元を加える比較を、別の曲面成分の探索と混同しない。固定三捩れの曲面7次元はこの一般8次元族の特殊部分である。指定局所order模型のHochschild計算、選んだ点の形式表示・適合したAbel変形、代数的表示stackまで到達している。**全intrinsic H3モジュライの相対代数化・開性・降下・全境界は未完成**である。この未解決問題を第二・第三論文の公表の前提にしない。

## III. 主要到達点・仮定・証明の所在

### A. 正常形と形式変形

- lem:e6-r13-cyclic-chart, prop:e6-r13-generic-envelope, cor:e6-r13-same-presentation：交代係数非零の巡回potentialをJacobian型へ規格化し、八変数族の一般包絡と中心切断をR(1,3)表示に同定する。最高三次のHesse判別条件を全係数で記す。共通開部分と指定点の局所表示成分の結論であり、全intrinsic成分の無条件同定ではない。証明は papers/sections/e6_r13_comparison.tex、厳密恒等式は verify_r13_comparison.py。ambient原稿は既に7+1を正しく記載しており、本比較のために変更しない。

- thm:normal：固定位数三、中央境界、対角非零という範囲で七次元正常形を得る。PBW、低次中心、残余A4群を直接計算する。対角係数零や非中央境界は含めない。
- thm:HH8：滑らかな三次中心C、D∈|−K_C|の滑らかさ、Dに沿う k[[s,w]]⋊μ3 への局所Morita模型を仮定し、HH²の7+1分解とHH³=0を証明する。局所模型への具体族の適用は ass:order の入力である。
- lem:central-lift, thm:eight-formal-central-lift：中心のrank跳躍を低次補正の単元minorで処理し、八変数同時形式族を構成する。
- thm:intrinsic-formal-eight と表示stack：適合したenhancement、Abel変形、反標準環の再構成の比較を明記する。一般dg変形のheart、任意の非被約底のH3開性・降下と混同しない。
- lem:generic-D：独立な超越的中心値については中心局所化でH3性を得る。固定した数値中心値でのH3性を同じ議論で結論しない。
- thm:conditional-component：全モジュライの成分判定は相対比較の追加仮定付きである。
- lem:anticanonical-quadratic-hull, prop:aou-infinite-order-exclusion：飽和反標準環R=B/(G), deg G=3からQ(R)=Bを回復する。唯一の中心一次直線で割ったpoint schemeは、本七次元族ではP²、AOU §9の無限位数Sklyanin側では楕円曲線。従って指定構造対象を保つexact同値はない。有限位数AS曲面、別の構造対象、任意の導来同値、八次元横断族の非AS性は未判定。

詳細は research/research_notes.md。同梱する旧来の入力断片は補助資料であり、それが存在することと、その全依存証明の自己完結性・独立監査を区別する。

### B. Fricke・Poisson・周期

- thm:aw-casimir-exact：AW表示とCasimirの正確なスカラー。spherical DAHAとのMorita同値は未主張。
- thm:relative-critical-flat, thm:critical-discriminant-quintics, thm:paired-quintic-S5：相対次数15と5、Δ15=N5²M5、同時幾何群S5×S5。有限体分解型だけで幾何群を証明したとはしない。
- Cayley分岐源、四sheet衝突のD4、Milnor包含からPicard格子への整数比較を保持する。中心の座標、一次元表現の座標、LG値h、Casimir値Dは異なる。
- thm:four-integer-D4-periods, thm:four-period-rational-split：指定conic開集合上の四周期 (z1/z2,z2/z3,z3/z4,z3*z4) と捩れ性による有理Hodge分裂。
- thm:G2-period-isogeny-quotient, thm:G2-companion-rational-Hodge：指数3のperiod isogenyと既知G2底写像。共通開集合の有理MHS比較、Klein整数拡大の位数7,21,21。全底の標準VMHSや曲面・導来圏の同値ではない。

詳細は research/fricke_daha_comparison.md, poisson_order_notes.md, cayley_lg_connections.md, conic_period_coordinates.md。

### C. 境界・局所圏・Prym

- thm:pell-exact-degree：g=ι_vι_wι_uι_w、Λ=3+2√2、最低次数1,7,41,…。射影交点次数2d_n、有限境界blow-upでの非正則化、個別付値の抽出深さ4nを区別する。
- 通常affine Perf entropyは零。射の極filtrationはlogΛ、proper曲線閉包・正規化欠損の対象列は2logΛ。関手entropyと対象列の成長を区別する。
- 許容conicの境界は二つのPuiseux(b_n,c_n)枝、交叉b_nc_n、link T(2b_n,2c_n)。Newton閾値・conductor・Milnor数を本文で計算する。
- 重み付き模型 F=y^(2b)−2κx^c y^b+x^(2c) の二周期MFは(n,κ²)で分類される。実germへの無条件延長はしない。具体的な実germのμ=27,τ=24と主部τ=27は、Hua–Kellerの通常Z-graded dg圏のHH⁰で区別する。二周期の相対HH=Jacと混同しない。
- 指定した z=y^b/x^c を保つMilnor曲線からの楕円写像には平方類[x]の障害がある。a²=xの二次被覆では次数2bcの写像を構成でき、Prymに可変楕円因子が入る。任意の別の楕円写像の不存在は主張しない。
- Ciani中間曲線、巡回次数bcと2bc、楕円引戻しの核となる標識二捩れ、theta線束の制限次数bc、Prym型 (1^(b−1),2^(2bc−b−c)) を保持する。楕円上の偏極isogenyの次数は(bc)²である。
- 可変楕円は既知の極端有理楕円曲面X411、周期は (κ²−1)Π''+2κΠ'+Π/4=0。j写像の次数6とBelyi分岐を計算する。整数直積分裂、実高重みgermへのPrym移行、MF部分圏・HMSは未構成。

詳細は research/boundary_pell_dynamics.md, boundary_analytic_moduli.md。

## IV. 次の課題と具体的な着手

1. **公表範囲を固定する。** 三論文それぞれのIntroductionと主定理を突き合わせ、既知理論の適用を貢献として過大に述べていないか確認する。全分類の完成を待たずに公表できる定理列を確定する。
2. **第一論文の外部認識を監査する。** ass:recognition, ass:order の各項から、同梱入力断片の証明と文献へ一つずつ辿る。飽和性、有限大域次元、局所order、Serre作用の適用範囲を別々に確認する。全H3の開性・降下を無断で仮定から除かない。
3. **既出性比較を完結する。** 第一論文はPymのR(1,3)中心拡大、Etingof–Ginzburg、CMR、Rains、AOU/VdB。表示族の一致は今回の比較節で証明したので未解決へ戻さず、H3開性・相対降下とAS認識を別に調べる。第二論文はAW/DAHA、既知Fricke判別式、Goldman–Neumann、Friedman、Boalch–Paluba。第三論文はMarkov境界力学、準斉次特異点の分類、Prym/Ciani分解、Miranda–Persson。必要な係数変換・同一性を実際に計算し、未確認箇所をIntroductionへ反映する。
4. **重点的な証明点検。** 二五次被覆の独立な幾何S5、整数D4標識とtrialityの全開条件、Prymの分岐と整数偏極を、計算証明書とは別に通読する。
5. **次の研究として保持する。** n=1の実germでTjurina跳躍と[f]を調べ、Z-gradedと二周期の比較を進める。b=2,c=5のPrym補因子の整数偏極、X411の整数monodromy、有限位数AS部分との比較も有力である。いずれも投稿準備を際限なく拡張する前提にしない。

## V. 再現・検証・保存

~~~sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_sources.py
python3 computations/verify_r13_comparison.py
python3 computations/verify_all.py
make papers
make bundle
~~~

verify_sources.py は三原稿の入力・ラベル・引用を検査する。verify_all.py は36検証器の実行結果、実行時刻、使用ソースのhashを computations/validation.json に記す。比較検算の結果は r13_comparison_certificate.json に別記する。既存36検証器の保存済PASSと今回の新検算を区別し、変更のないコードのhashを照合する。計算は数学的主張の全体を独立に検証するものではない。

組版は標準のTeX Live日本語環境、LuaLaTeX、latexmkを用いる。三主原稿はそれぞれdocumentclassとTeX root指定を持つ。ルートからの make papers、papers/からの latexmk -lualatex、およびlatexmk -cdで同じ build/ にPDFとSyncTeXを出力する。現行の生成・検証・監査範囲は **research/publication_status.md** に集約する。最新ソース以外の旧PDFを配布しない。

bundleは scripts/build_bundle.py で現在の必要ファイルを選んで作成し、三PDF・入力ソース・計算資産の欠落、ZIP整合性を検査する。GitにはTeX・ノート・再現資産だけを保存する。
