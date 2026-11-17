# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v25。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎知識は `research/research_notes.md`、DAHA・Fricke比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、LG・G2・braid・周期の基礎は `research/cayley_lg_connections.md`、全四周期・triality・三成分Hodge比較は `research/conic_period_coordinates.md`、周期に見えない境界力学の具体式と次の着手は `research/boundary_pell_dynamics.md`。現行一式で再開し、旧bundleや会話履歴を前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先目標は数学的に面白くすること。優先的戦略は、多様な話題との具体的な関連を見つけ、検証可能な数学へ育てること。** 意外な同型・共通構造、見通し、新しい問いや方法を重視し、名称や定理の本数を増やすこと自体を目的にしない。
正確性は犠牲にしない。数学的重要性、新規性、理解の深化、応用可能性、実現可能性を総合して研究価値を最大化する。既定の分類を完走することが面白い接続より自動的に優先されるわけではない。
重要な方針変更では現時点の理由と元の目標の達成部分・残存部分を簡潔に記し、時系列の履歴を蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を示す。原稿に証明があること、今回点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。
先行研究は一次資料で確認し、仮定・適用範囲・本稿の貢献をIntroductionで比較する。未確認の内容・書誌・新規性を推測で補わず、不明点を明示する。外部PDF・検索結果を大量収録しない。
原稿は日本語LuaLaTeX。関連分野の公表価値ある成果も同じ主論文へ統合する。分割は数学的まとまりと公表上の利点が明確な場合に検討する。軽量化のために価値ある成果・必要証明を削除しない。
研究ノートは有用な着想・補題・計算・反例・本質的障害・文献比較・再取得困難な情報を保持する。日誌・会話・更新履歴・重複証明にせず、論文に十分な証明があれば参照する。
現行方針・ノート・論文と最小限の原稿・コード・入力・小証明書・再現手順を自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・組版中間物を除き、数学的内容と検証可能性は保持する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryへ保存しない**。push失敗で未保存成果の保全が必要な場合だけ緊急退避できる。既存Library資料は明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を別状態として報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行う。force push、不要なPR・Actionsを使わず、PDF・ZIPをGitで追跡しない。未実行をPASSと言わない。

## II. 現在の問いと到達基準

**同じ非可換三次曲面から回復される幾何を、写像・作用・変形・周期で結ぶ。** 量子中心はFrickeへ、一次元表現はLG・Cayley・D4へ、対称LGはG2へつながる。trialityの不変・余不変格子の指数3からG2三成分写像を説明し、三成分の有理MHS比較とKlein例の整数拡大位数7,21,21を得た。
周期に見えない正entropyの自己同型について、境界単項式付値の作用を二次元整数行列で捉え、Pell型の正確な最小次数と個別付値の抽出深さを求めた。係数に依存する周期とは対照的に、境界の漸近力学は係数に依存しない。これを境界変更・局所化した圏・wrapped幾何へ比較することを重視する。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆の証明は本文に保持。全intrinsic H3の相対代数化・降下・大域境界は未完成だが、他分野との接続の前提にはしない。
達成基準は、具体的写像・変形・局所模型・格子写像・圏的対応・障害・周期式のいずれかを正確に与えること。既知理論、明示的適用、新規性未確認の帰結を区別し、型・群名・数値の一致だけで同一視しない。

## III. 現在有効な主要成果

### A. 変形・モジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の適用範囲を外さない。
横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族・指定enhancement・smooth DM八次元表示stackを保持。一般非被約底のintrinsic降下・H3開性・全境界は未完成で、`thm:conditional-component`の比較仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般係数で既約六次元結節因子。中心特異性とH3境界は異なる。
AW中央特殊化、Casimir規約、Fricke係数写像、量子的Vieta、古典的D4⊂E6。Q=q exp(hbar)の中心交換子は指定Goldman型括弧の9倍。Brown–Gordonによるsmooth locusの中心fiber比較。全DでのM3やMorita同値は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaには障害。一般変形・心の変更を否定しない。
固定包絡の十Poisson零点は五節点と五滑らか臨界点。四Casimir特異値のA1型、既存判定下のH3可否、二次接触／一次横断、S4作用を明示。
相対Poisson臨界環は全域有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。有限体検算と群論・基本群の通常証明を区別する。今回はこれら旧主張を独立再監査したとはしない。

### C. Cayley・LG・Milnor・Picard

Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。W=H−Au−Bv−CwのJacobi環はrank5、graph(dH)はexact Lagrangian。分岐源はCayleyの閉トーラスSL2指標多様体。D4ミニバーサル変形、三枝巡回、留数対、実elliptopeとpillowcase、内部実sheet一意性を明示。
滑らかなU=S\Dで0→Z delta_infty→H2(U,Z)→D^perp→0。右端D4(-1)、左端原始radical。指定D4退化のMilnor包含はPicard直交補へ整数同型。判別群から双方の外部trialityを検出する。全域の標準分裂ではない。
MHS graded piecesはGr2=Q(-1)^4、Gr3=0、Gr4=Q(-2)。無限遠はmonodromy−IのT2束でpillowcaseとは別。nearly Kähler S3×S3の共通elliptopeは既知比較で、圏同値・計量退化は未構成。

### D. G2・braid・対数周期

Boalch–Palubaの既知G2実現を対称LGへ適用し、unipotent底(6,6)でD4とA2の二成分が現れる。三成分ラベルのA2根被覆と成分内Hurwitz B3は別作用。HurwitzはW・体積・Poissonを保ち、Chebyshev反復を持つ。
Klein七点の置換像S7（5040）と表現像G2(2)'（6048）、Klein群168を区別する。
omega=du∧dv/(uv−w−C)、原始境界周期(2pi i)²。conic matching周期は2pi i[log(u+sqrt(u²−1))]。係数零のMorse周期4pi arcsin sqrt(-2h)、rank二解局所系は無限二面体monodromy、指数化Q+Q^-1=2+8h。h=-1/10は有理MHS非分裂例（`sec:logarithmic-periods`）。

### E. 全四periodと円分性

`sec:four-D4-periods`の開条件はDisc N≠0、B²−C²≠0。compatible成分を縮約してF1標識を得る。Kはeven-sum Z4、整数基底(E1−E2,E2−E3,E3−E4,E3+E4−F)、四periodは `(z1/z2,z2/z3,z3/z4,z3*z4)`。
指数行列det2、kernel共通±1、quartic係数Jacobian16(C²−B²)。root hypertorus型判別式、有理Hodge分裂⇔全period捩れ⇔全zi捩れ。
有理係数の分裂例(1/4,1/2,1/4,1/8)は9乗根、非分裂例(-65/16,75/16,-65/16,3575/288)はzi=2,3,4,6または逆数。標識・成分選択を省略しない。Wの臨界値、Casimir値、被覆の分岐は別現象。

### F. trialityのperiod isogenyと三成分Hodge比較

`sec:triality-period-isogeny`。Goldman–Neumannの既知ホモロジー定理により対称Hurwitz像は外側三根のS3、純braidはH2で自明。K基底(c,o1,o2,o3)の周期は(xi,eta,eta,eta)。不変格子(c,s=o1+o2+o3)と余不変格子(cbar,obar)の自然写像diag(1,3)、Gram不変[[-2,3],[3,-6]]。torus制限 `(xi,eta)->(xi,eta^3)` はkernel mu3。
S=sum_{t=eta,xi eta,xi eta²}(t+t^-1)、L=sum_{t=xi,xi eta³,xi²eta³}(t+t^-1)。lambda=(S+2)/4、h=(L+3S+4)/8。
対称族は従来のB²≠C² chart外なので、別の明示line sectionと非交叉を使う。quartic=(u+1)prod_t(u+(t+t^-1)/2)、z=(-xi eta²,-xi eta,-eta,-1)、四period=(eta,xi,eta,eta)。六root character≠1、eta,xi eta,xi eta²≠−1の開条件を保持（`thm:symmetric-period-reconstruction`）。
isogenyのWeyl商はalpha=L、beta=S³−3SL−9S−6L−12、b_F=−S−2,c_F=L+3S+4としてBP底写像と一致（`thm:G2-period-isogeny-quotient`）。標数零G2群の中心isogenyと誤解しない。
regular底の三持上げ(xi,zeta^j eta)が全て明示開集合にあるとき、正規化periodは外側方向でj/3だけ異なり、三成分の有理MHSは標識graded pieceの下で同型。全底の標準VMHS同型や曲面同型は未主張（`thm:G2-companion-rational-Hodge`）。
Kleinではxi=eta=primitive7root、S=L=-1。Fricke(-1,0)と同じG2底の二コンパニオンb=(-5±sqrt21)/2,c=−3−3bの整数拡大位数は7,21,21。全て有理分裂だがKleinとコンパニオンの整数MHSは非同型（`cor:Klein-seven-twentyone-Hodge`）。他成分の有限Hurwitz軌道は未主張。
g=iota_v iota_w iota_u iota_wは全H2・periodで恒等、しかし既知力学定理からlambda1=3+2sqrt2、entropy=log(3+2sqrt2)（`prop:period-invisible-entropy`）。

### G. 境界付値・Pell次数・無理方向

主論文 `sec:boundary-pell-dynamics`。指定境界三角形の単項式付値の極次数空間はC={2max(a,b,c)=a+b+c, a,b,c≥0}で、Theta(r,t)=(|r|,|t|,|r+t|)により(R²\0)/±と同定。VietaはT_u=(2max(b,c)−a,b,c)等、gはM=[[1,-2],[-2,5]]で作用する。最大項の消去を避けるため積表示u iota_u(u)=v²+w²+2Bv+2Cw+2hを使う。
最小affine全次数d_nはd0=1,d1=7、d_(n+2)=6d_(n+1)−d_n。列1,7,41,239,1393,...。N=[[1,2],[2,5]]、(p_n,q_n)=N^n(1,1)なら三座標の次数(p_n,q_n,q_n−p_n)、q_n=d_n。最高項がu,vのみの単項式なのでgr O(U)=C[u,v,w]/(uvw)で消えず、表示上の次数だけでなく最小次数である（`thm:pell-exact-degree`）。
M^n=[[a_n,-b_n],[-b_n,c_n]]と書くとd_n=b_n+c_n、d_n²−2c_n²=−1、d_n+c_n sqrt2=(1+sqrt2)^(2n+1)。射影hyperplane Hではn≥1にH·(g^n)^*H=2d_n、n=0はH²=3。二つの次数を混同しない。
固有付値の極次数は(1,1+sqrt2,sqrt2)と(1,sqrt2−1,sqrt2)。射影境界作用はnorth–south型、有理方向に周期点なし。従って指定Sを支配する有限境界point blow-upではgを正則自己同型へ延長できない（`thm:irrational-boundary-nonregularization`）。algebraic stabilityや全ての別コンパクト化の不存在を意味しない。
nu_n=g_*^n ord(D_w)の極次数は(3,7,4),(17,41,24),(99,239,140),...。局所重み比(q_n−p_n)/p_n=[1;2...(2n−2個)...,3]で、この一つの付値の抽出に必要なcorner blow-upは最小4n回（`prop:pell-corner-depth`）。指数的な極次数と線型の抽出深さを区別する。
一般tropical線型化はJang、境界円周作用とentropyはCantat–Lorayの先行研究。本稿の明示語での最低次数・交点次数・抽出深さの具体化として位置付け、新規性の網羅確認は未了。

## IV. 優先課題と着手方法

**第一優先：境界付値の成長を局所化した圏の作用で捉える。**
今回の原始付値の無限軌道と有限blow-up非正則化を、境界のbirational correspondence、wrapped Fukaya圏、非可換局所化のどのモデルで実現できるか調べる。最初に一つのVieta involutionの局所corner chartと、境界に沿う対象の像を対応させる。全H2が恒等でも極次数がPell増大する点が試験例。圏的entropyを古典entropyの値から推測で断定しない。

**並行して優先：三成分の有理Hodge比較の幾何学。**
指数3のperiod isogenyを境界線束の3捩れ変更・代数的対応・有限被覆のどれとして実現できるか検討する。Klein/二コンパニオンのline配置とgluingから始める。有理MHS同型から曲面同型・導来同値・動機同型を推論しない。整数拡大位数7対21を有効な障害として使う。

**並行して優先：Pell方向・トーラス・算術とfolding。**
Mの二次無理固有方向と周期torusの関係を、境界付値と観測periodの違いを維持して比較する。特定語の4nという抽出深さを他のhyperbolic語と連分数へ一般化できるか調べる。Kleinの7/21、mu3による捩れ位数の変化、Spin8のcharacterと長短根isogenyも保持する。一般理論の既知部分を先に一次文献で確かめる。

**支える課題：全周期接続と非可換成分。**
四periodの対数微分から代数的de Rham基底のrank五接続を構成し、対称族の比較をglobal VMHSとする際の標識・monodromyを調べる。N5,M5のbranchと値衝突はtrace判別式で分ける。Sklyanin方向による純粋q障害相殺、Vietaの心の変更、全H3 admissibility・intrinsic降下・全境界を維持し、一枝に固定しない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_boundary_pell_dynamics.py
python3 computations/verify_all.py  # 全30検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回、新しい境界/Pell検証器を厳密実行しPASS。Vieta全係数恒等式、12個の全線型chamber上36恒等式、反復行列・Pell恒等式・連分数をn=24まで、固有方向を記号的に確認した。小証明書は `computations/boundary_pell_dynamics_certificate.json`。有限回の反復確認から全nへ外挿せず、本文の最高項帰納法・連分数帰納法で証明する。
境界付値空間の同定と不変性、最小次数、射影引戻し、非正則化は通常の証明。H2恒等性とentropyは既存の先行定理への依存。旧29検証器と旧理論の今回の全再監査は未実施。
新節単体をLuaLaTeX wrapperで4頁に組版し、4頁の画像・内部参照・overfullなしを確認した。主論文全体の今回の再組版、新規性の網羅調査、圏的entropy・非Archimedean good reductionの構成は未実施。
主論文の差分を確認し、既存の証明本文・全入力節を保持して統合する。GitHub保存後にmain refと必要ファイルを確認する。生成PDF・wrapper・画像・ログをGitへ入れず、push済み内容をLibraryへ保存しない。
