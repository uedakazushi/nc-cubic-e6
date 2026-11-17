# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v27。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎は `research/research_notes.md`、DAHA比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、LG/G2の基礎は `research/cayley_lg_connections.md`、四周期・trialityは `research/conic_period_coordinates.md`。境界力学・局所化・絡み目・正規化の現行式と次の着手は `research/boundary_pell_dynamics.md`。旧bundle・会話履歴を再開の前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先は数学的に面白くすること。優先戦略は、多様な話題との具体的接続を見つけ、検証可能な数学へ育てること。** 意外な同型・共通構造、見通し、新たな問いや方法を重視し、名称や定理数の増加を目的にしない。
正確性を犠牲にせず、数学的重要性、新規性、理解の深化、応用、実現可能性を総合して価値を最大化する。既定の分類の完遂が他の面白い接続より自動的に優先されるわけではない。
重要な方針変更は現在の理由と元の目標の達成部分・残存部分を簡潔に記し、時系列の変更履歴を蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を示す。原稿に証明があること、今回点検したこと、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。
一次文献の仮定と適用範囲を確認し、Introductionで既知結果と本稿の貢献を具体的に比較する。未確認の内容・書誌・新規性を推測で補わない。外部PDF・検索結果を大量収録しない。
原稿は日本語LuaLaTeX。公表価値ある関連分野の結果も同じ主論文の適切な位置に統合する。分割は数学的まとまりと公表上の利点で判断する。価値ある既存成果や必要証明を軽量化のために削除しない。
研究ノートは有用な着想、補題、計算、反例、本質的障害、文献比較、再取得困難な情報を保持する。日誌・会話・履歴・重複証明にせず、論文に十分な証明があれば参照する。
現行方針・ノート・論文と必要最小限の原稿、コード、入力、小証明書、再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・中間生成物を除くが、数学的内容と検証可能性は保持する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryへ保存しない**。push失敗で未保存成果の保全が必要な場合のみ緊急退避できる。既存Libraryファイルを明示指示なしに削除しない。
日付・版番号を付け、生成・検証・commit・push・Library保存を別状態で報告する。約15分または数学的区切りにmainへ通常のfast-forward保存を行い、force push、不要なPR・Actionsを使わない。PDF・ZIPをGitで追跡せず、未実行をPASSと言わない。

## II. 現在の問いと研究選択

**同じ非可換三次曲面から回復される幾何を、写像・作用・周期・局所模型で結ぶ。** 量子中心はFrickeへ、一次元表現はLG/Cayley/D4へ、対称LGはG2へつながる。trialityの指数3からG2三成分写像を説明し、有理MHS比較と整数拡大位数7,21,21を得た。
周期を固定する正entropyの自己同型gでは、境界のPell次数が成長する一方、通常のPerf(U)のDHKK entropyは零である。射の極filtrationと自然な閉包対象の成長を別々に測る必要がある。
今回、閉包の算術種数が**一つの境界点の二つのPell型cusp**に全て集中することを証明した。二枝のlinkはT(2b_n,2c_n)、正規化と一点欠損の対象増大率はlog Lambdaと2log Lambda。既知のCasals構成に明示Chebyshev morsificationを入れ、local Weinstein模型を得た。これでmirror比較の候補は具体化したが、異なる反復の模型を結ぶ関手や元の曲面との同値は未構成。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆の証明は現行原稿にある。全intrinsic H3の相対代数化・降下・大域境界は未完成で、他分野との接続の前提にしない。
達成基準は、具体的写像、変形、局所模型、格子写像、圏的対応、障害、周期式のいずれかを正確に与えること。型・名前・数値の一致だけで同一視しない。

## III. 現在有効な主要成果

### A. 非可換変形とモジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の仮定を外さない。
横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族・enhancement・smooth DM八次元表示stackを保持する。一般非被約底のintrinsic降下、全H3開性・境界は未完成で、成分定理の比較仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡五結節SNC因子、A4商の二成分、一般係数で既約六次元結節因子。中心特異性とH3境界は異なる。
AW中央特殊化、Casimir規約、Fricke係数写像、量子的Vieta、D4⊂E6。Q=q exp(hbar)の交換子は指定Goldman型括弧の9倍。Brown–Gordonの中心fiber比較を適用するが、全DでのM3/Morita型は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaには障害。一般変形・心の変更は否定しない。
固定包絡の十Poisson零点は五節点と五滑らか臨界点。四Casimir特異値、既存H3判定の可否、二次接触／一次横断、S4作用を明示。
相対Poisson臨界環は有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。算術検算と群論・基本群の通常証明を区別する。今回旧主張の独立再監査はしていない。

### C. Cayley・LG・格子と全周期

Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。Jacobi環rank5、graph(dH)はexact Lagrangian。分岐源はCayleyの閉トーラスSL2指標多様体。D4 miniversal、三枝巡回、留数対、elliptope/pillowcase、内部実sheet一意性。
U=S\Dで0→Z delta_infty→H2(U,Z)→D^perp→0、右端D4(-1)、左端原始radical。指定D4退化のMilnor包含はPicard直交補へ整数同型、外部trialityも比較する。全域の標準分裂ではない。
MHSのGr2=Q(-1)^4、Gr4=Q(-2)。無限遠の−I torus bundleとpillowcaseは別物。nearly Kählerの共通elliptopeは既知比較で圏同値は未構成。
Boalch–PalubaのG2実現でunipotent底(6,6)にD4/A2の二成分。成分交換braidと内部Hurwitzを分ける。Klein七点のS7と表現像6048、Klein群168も別。
境界周期(2pi i)²、matching対数積分、Morseの4pi arcsin sqrt(-2h)、rank二解系の無限二面体。有理非分裂例h=-1/10。
一般conic chartでcompatible標識を用い、整数D4基底の四period=(z1/z2,z2/z3,z3/z4,z3*z4)。有理MHS分裂⇔全zi捩れ。有理数係数の分裂・非分裂例を保持。W臨界値・Casimir値・被覆分岐は異なる。

### D. trialityの指数3と三成分の比較

`sec:triality-period-isogeny`。対称Hurwitzホモロジー像は外側三根S3、pure braidは自明（Goldman–Neumann）。周期は(xi,eta,eta,eta)、不変→余不変格子diag(1,3)、torus写像(xi,eta)→(xi,eta³)のkernel mu3。
S=sum_{t=eta,xi eta,xi eta²}(t+t^-1)、L=sum_{t=xi,xi eta³,xi²eta³}(t+t^-1)、lambda=(S+2)/4、h=(L+3S+4)/8。旧B²≠C² chart外の対称族には明示line sectionで別途標識を構成する。
Weyl商alpha=L、beta=S³−3SL−9S−6L−12はBP三成分写像。三持上げが共通明示開集合にある範囲で有理MHSは標識graded pieceの下で同型。Kleinとコンパニオンの整数拡大位数7,21,21。全底の標準VMHS・曲面同型・導来同値ではない。

### E. 境界Pell力学と局所化

`sec:boundary-pell-dynamics`, `sec:localization-entropy`。g=iota_v iota_w iota_u iota_wはH2・periodを固定、境界Theta(r,t)=(|r|,|t|,|r+t|)ではM=[[1,-2],[-2,5]]で作用する。Lambda=3+2sqrt2。
M^n=[[a,-b],[-b,c]]、d=b+c=1,7,41,239,...、d_(n+2)=6d_(n+1)−d_n、d²−2c²=−1。最小多項式次数であり、generic射影交点次数はn≥1で2d。指定Sを支配する有限境界blow-upでは正則自己同型にできないが、algebraic stabilityを否定しない。個別反復付値のcorner抽出は4n。
アフィン引戻しのDHKK h_tは全tで零。対象を固定してもEnd作用は非自明。極filtration F_mRは全次数、dim=(3m²+3m+2)/2。sigma^nの最小尺度倍率d_n、歪み率log Lambdaで生成空間変更に不変。像そのものの次元が増える意味ではない。
一般conic C0={v=kappa}の逆像閉包はclass cD_u+bD_v+dD_w、次数2d、算術種数delta=1+2bc−d。構造層Q_nのproper対象複雑度は2log Lambda、開制限は二項自由解消で一様有界。対象列の成長率を自己関手entropyと呼ばない。
HH0=RとHH2=R omegaではfiltered歪みlog Lambda、HP_even=H0_dR⊕H2_dRはrank6で恒等作用。filtered equivariant mirrorには線型filtration比較と特定gへの同変性が別に必要。

### F. 二cusp・トーラス絡み目・正規化欠損

新節 `papers/sections/quantum_cubic_boundary_links.tex`、`sec:boundary-torus-links`。
明示条件kappa²≠1、N_v(kappa)≠0のsmooth conicを使う。n≥1の閉包はp_wただ一つで特異、二枝のPuiseux対は(b_n,c_n)、相互交叉b_nc_n。出発無限遠のrho±=kappa±sqrt(kappa²−1)について局所パラメータはx=2^(-b)rho^(-a)s^b(1+O(s)), y=2^(-c)rho^(-b)s^c(1+O(s))。最低重み式はy^(2b)−2kappa x^c y^b+x^(2c)。解析的右同値まで主張しない。
primitive toric解消後の二点はz=y^b/x^c=rho±で横断的。z+z^-1=2kappaが出発係数を保持する。
linkはT(2b,2c)、二成分はT(b,c)、linking bc。delta_branch=(b−1)(c−1)/2、delta_total=1+2bc−b−c、mu=(2b−1)(2c−1)=2delta−1。conductorは各枝s^delta。Milnor fiberはgenus delta−1、境界2。H1 monodromy特性多項式は(T^(2bc)−1)²(T−1)/((T^(2b)−1)(T^(2c)−1))、正確な位数2bcでspectral radius1。位数の列は2log Lambdaで増えるが、これはgの力学とは別。
正規化B_n=nu_*O_P1と欠損Z_n=B_n/Q_nについて、Z_nはp_wのみ、length delta、H1(Q_n)=H0(Z_n)。任意proper生成元でB_nの対象成長率log Lambda、Z_nは2log Lambda。開制限ではB_n=Q_n、Z_n=0。
Chebyshevのepsilon^(2bc)[T_(2c)(x/epsilon^b)−T_(2b)(y/epsilon^c)]は重み付き代表のreal morsification。delta個の実nodeとdelta−1個の極値を持つ。Casalsの既知定理を適用してlocal Weinstein pairのLagrangian Milnor曲面＋mu thimble模型を得る。二handleで閉じた局所四多様体のEulerは3、元のUは6なので同一視しない。異なるnの模型間の関手・equivariant mirrorは未構成。

## IV. 優先課題と具体的着手

**第一優先：局所模型を対象・射の対応へ進める。**
Casalsの模型と明示Chebyshev divideを出発点に、まずn=1のT(4,10)についてvanishing cycle配置・thimbleの交叉・microlocal sheafの小さいquiverを計算する。正規化完全列とconductorをmirror側のどのexact triangleに対応させるかを明示する。局所モデルの存在からglobal Uのwrapped圏との同値やg作用を推論しない。

**並行して優先：反復間の対応と境界情報の保存。**
g^{-1}による(b,c)→(2b+5c,b+2c)の局所変換を、toric解消の共通細分と標識付き例外曲線z=rho±で記述する。これがexact cobordism、stop変更、代数的局所化のどれへ持ち上がるかを調べる。nごとの有限位数Milnor monodromyとnを動かす双曲型gを混同しない。

**並行して優先：三成分の有理Hodge同型の幾何学化。**
3捩れperiod差を境界線束の変更・有限被覆・代数的対応として実現できるか、Klein7/21のline配置から調べる。有理Hodge同型から曲面・圏の同値を推論しない。Spin8→G2のcharacter、捩れ位数の変化、全rank五接続も維持する。

**支える課題：非可換成分と独立監査。**
N5,M5のbranchと観測値衝突、Sklyanin方向での純粋q障害相殺、Vietaの心の変更、全H3 admissibility・intrinsic降下・全境界を継続する。公表前には旧依存定理も独立に監査する。一枝の重い計算だけに研究を固定しない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_boundary_torus_links.py
python3 computations/verify_all.py  # 全32検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回、新検証器をQ・Zの記号演算で実行しPASS。一反復の全係数先頭式、全nの帰納式の代数、24反復の整数値、n=1のJacobi次元27・conductor指数14、Milnor特性多項式、Chebyshev臨界値resultantを確認。小証明書は `computations/boundary_torus_links_certificate.json`。
全nのPuiseux型、link・conductor・Milnor理論、正規化の対象複雑度、Casals構成は本文の通常証明と一次資料への依存であり、有限検算だけの形式証明ではない。旧31検証器は今回は全再実行していない。
新節単体をLuaLaTeX wrapperで5頁に組版し、全頁画像・内部参照・overfullなしを点検。主論文全体の今回の組版、旧証明の独立再監査、global filtered mirror、新規性の網羅調査は未実施。
主論文の更新差分で既存証明本文・入力節・文献表の保持を確認する。main refと必要ファイル、実行コードとの一致を保存後に確認し、生成PDF・wrapper・画像・ログをGitへ入れず、push済み内容をLibraryへ保存しない。
