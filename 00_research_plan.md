# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v26。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎は `research/research_notes.md`、DAHA比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、LG・G2の基礎は `research/cayley_lg_connections.md`、四周期・trialityは `research/conic_period_coordinates.md`。境界力学・局所化・entropyの現行式と次の着手は `research/boundary_pell_dynamics.md`。旧bundle・会話履歴を再開の前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先は数学的に面白くすること。優先戦略は多様な話題との具体的な接続を探し、検証可能な数学へ育てること。** 意外な同型・共通構造、見通し、新しい問い・方法を重視する。名称や定理の本数を増やすことを目的にしない。
正確性を犠牲にせず、数学的重要性、新規性、理解の深化、応用、実現可能性を総合して価値を最大化する。既定の分類の完遂が面白い接続より自動的に優先されるわけではない。
重要な方針変更は現時点の理由と元の目標の達成部分・残存部分を簡潔に整理し、時系列の履歴を蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を明記する。原稿に証明があること、今回点検したこと、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。
一次文献の仮定と適用範囲を確認し、Introductionで既知結果と本稿の貢献を比較する。未確認の内容・書誌・新規性を推測で補わない。外部PDFや検索結果を大量収録しない。
原稿は日本語LuaLaTeX。関連分野の公表価値ある成果も同じ主論文の適切な箇所へ統合する。分割は数学的まとまりと公表上の利点で判断し、軽量化のために価値ある内容・必要証明を削除しない。
研究ノートは有用な着想、補題、計算、反例、本質的障害、文献比較、再取得困難な情報を保持し、日誌・会話・更新履歴・重複証明にしない。論文に証明があれば参照する。
現行方針・ノート・論文と必要最小限の原稿、コード、入力、小証明書、再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・組版中間物を除き、数学的内容と検証可能性は保持する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryへ保存しない**。push失敗で未保存成果の保全が必要な場合だけ緊急退避できる。既存Libraryファイルを明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を別状態で報告する。約15分または数学的区切りにmainへ通常のfast-forward保存を行う。force push、不要なPR・Actionsを使わず、PDF・ZIPをGitで追跡しない。未実行をPASSと言わない。

## II. 現在の問いと研究選択の理由

**同じ非可換三次曲面から回復される幾何を、写像・作用・変形・周期で結ぶ。** 量子中心はFrickeへ、一次元表現はLG・Cayley・D4へ、対称LGはG2へつながる。trialityの指数3による周期isogenyからG2三成分写像を説明し、有理MHS比較と整数拡大位数7,21,21を得た。
周期を固定する正entropyの写像gについて、境界のPell次数と無理固有付値を得た。今回、その成長を圏へ移すと**通常のPerf(U)のDHKK entropyは零**となることを確認した。構造層という生成元を固定するためであり、射の作用が自明という意味ではない。
従って「正の古典entropyがそのまま通常のアフィン圏entropyになる」という目標は採らない。代わりに、極filtration付きの射ではlog Lambda、自然な曲線閉包の対象複雑度では2log Lambda、局所化後の対象では有界、という相違を説明し、filtered・equivariantなmirror比較へ進む。Lambda=3+2sqrt2。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆の証明は現行原稿にある。全intrinsic H3の相対代数化・降下・大域境界は未完成だが、他分野との接続の前提にしない。
達成基準は具体的写像、変形、局所模型、格子写像、圏的対応、障害、周期式のいずれかを正確に与えること。既知理論、明示的適用、新規性未確認の帰結を区別し、型・名前・数値の一致から同一視しない。

## III. 現在有効な主要成果

### A. 変形・モジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の仮定を外さない。
横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値のH3性は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族・指定enhancement・smooth DM八次元表示stackを保持。一般非被約底のintrinsic降下・H3開性・全境界は未完成で、`thm:conditional-component`の比較仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般低次係数での既約六次元結節因子。中心特異性とH3境界は異なる。
AW中央特殊化、Casimir規約、Fricke係数写像、量子的Vieta、古典的D4⊂E6。Q=q exp(hbar)の交換子は指定Goldman型括弧の9倍。Brown–Gordonによるsmooth locusの中心fiber比較。全DでM3やMorita同値になることは未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaには障害。一般変形や心の変更は否定しない。
固定包絡の十Poisson零点は五節点と五滑らか臨界点。四Casimir特異値のA1型、既存H3判定での可否、二次接触／一次横断、S4作用を明示。
相対Poisson臨界環は有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。算術検算と群論・基本群の通常証明を区別する。今回これら旧主張を独立再監査したとはしない。

### C. Cayley・LG・Milnor・Picard

Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。LG Jacobi環はrank5、graph(dH)はexact Lagrangian。分岐源はCayleyの閉トーラスSL2指標多様体。D4ミニバーサル変形、三枝巡回、留数対、elliptope/pillowcase、内部実sheet一意性を明示。
滑らかなU=S\Dで0→Z delta_infty→H2(U,Z)→D^perp→0。右端D4(-1)、左端原始radical。指定D4退化のMilnor包含がPicard直交補へ整数同型。判別群から双方の外部trialityを検出する。全域の標準分裂ではない。
MHSのGr2=Q(-1)^4、Gr3=0、Gr4=Q(-2)。無限遠はmonodromy−IのT2束でpillowcaseとは別。nearly Kähler S3×S3の共通elliptopeは既知比較で、圏同値・計量退化は未構成。

### D. G2・braid・全period

Boalch–PalubaのG2実現を対称LGへ適用し、unipotent底(6,6)でD4とA2の二成分。成分交換のA2三次根被覆と成分内Hurwitz B3を区別。Klein七点の置換像S7と表現像G2(2)'（6048）、Klein群168は別。
omega=du∧dv/(uv−w−C)、境界周期(2pi i)²、matching周期2pi i[log(u+sqrt(u²−1))]。係数零のMorse周期4pi arcsin sqrt(-2h)、指数化Q+Q^-1=2+8h、rank二解局所系は無限二面体。有理MHS非分裂例h=-1/10。
conic chart Disc N≠0、B²−C²≠0ではcompatible成分をF1へ縮約し、整数D4基底(E1−E2,E2−E3,E3−E4,E3+E4−F)の四periodは(z1/z2,z2/z3,z3/z4,z3*z4)。有理MHS分裂⇔全period捩れ⇔全zi捩れ。有理数係数の円分分裂例・非分裂例を保持。標識、被覆分岐、Wの臨界値、Casimir値を混同しない。

### E. trialityの指数3と三成分Hodge比較

`sec:triality-period-isogeny`。対称Hurwitzのホモロジー像は外側三根S3、pure braidは自明（Goldman–Neumann）。K基底(c,o1,o2,o3)のperiodは(xi,eta,eta,eta)。不変格子→余不変格子diag(1,3)、双対torus制限(xi,eta)→(xi,eta³)のkernelはmu3。
S=sum_{t=eta,xi eta,xi eta²}(t+t^-1)、L=sum_{t=xi,xi eta³,xi²eta³}(t+t^-1)、lambda=(S+2)/4、h=(L+3S+4)/8。対称族は旧conic chart外なので明示line sectionでcompatible標識を別証明し、四period=(eta,xi,eta,eta)を実現する。
Weyl商はalpha=L、beta=S³−3SL−9S−6L−12で、Boalch–Paluba三成分写像と一致。三持上げが共通の明示開集合にある範囲で有理MHSは標識graded pieceの下で同型。Kleinとコンパニオンの整数拡大位数は7,21,21。全底の標準VMHS同型、曲面同型、導来同値ではない。

### F. 境界付値とPell次数

`sec:boundary-pell-dynamics`。g=iota_v iota_w iota_u iota_wは全H2・periodを固定するが、Lambda=3+2sqrt2の双曲型作用を境界に持つ。Theta(r,t)=(|r|,|t|,|r+t|)、M=[[1,-2],[-2,5]]。
M^n=[[a_n,-b_n],[-b_n,c_n]]、d_n=b_n+c_nは1,7,41,239,...、d_(n+2)=6d_(n+1)−d_n。これは最小多項式次数で、d_n²−2c_n²=−1。generic射影交点次数はn≥1で2d_n。
無理な二固有方向のため有理境界付値に周期点はなく、指定Sを支配する有限境界blow-upでは正則自己同型へ延長できない。algebraic stabilityや全コンパクト化の不存在は主張しない。個別付値g_*^n ord(D_w)の最小corner抽出回数は4n。

### G. 局所化が消す複雑度と三つの成長率

新節 `papers/sections/quantum_cubic_localization_entropy.tex`、`sec:localization-entropy`。
任意の非空アフィンXの自己射fについてLf*はPerf(X)の生成元O_Xを固定し、DHKK h_t=0（全実t）。residue fieldへのexact関手でdelta_t(O,O)=1を確認する初等的帰結。**対象の固定とEnd環の恒等作用を区別する。**
F_mR=H0(S,O(mD))/s_D^mは最小次数filtrationに一致し、dim F_m=(3m²+3m+2)/2。V=<1,u,v,w>の像を収める最小倍率ell(n)=d_n、歪み率log Lambda。有限生成空間の変更と線型同値なfiltrationで率は不変。全mでsigma(G_m)⊂G_(m+C)となる一様な加法shiftは存在しない。これはCôté–Kartalの静的次元growthではなく、特定写像の反復が必要とする極次数の倍率である。
C0={v=kappa}を一般の滑らかなconic、C_n=g^-n C0とする。閉包のclass P_n=c_nD_u+b_nD_v+d_nD_w、次数2d_n、P_n²=4b_nc_n、算術種数1+2b_nc_n−d_n。全C_nは同じ滑らかな有理affine曲線なので、種数は境界のdelta不変量の総和。最初の(degree,genus)は(2,0),(14,14),(82,656),(478,23422)。
Q_n=O_{closure(C_n)}に対し、任意のproper split generator Eでlim log delta0(E,Q_n)/n=2log Lambda。下界はEuler数、上界は固定bundleの境界成分ごとのO(d_n²)cohomology評価とDHKK saturated比較。一方j*Q_nは[R→R]なのでdelta0(R,j*Q_n)≤2。**Q_nを一関手の反復像としたわけではなく、2log Lambdaを自己関手entropyと呼ばない。**
HH0(R)=RとHH2(R)=R omegaのfiltered歪みはlog Lambda。HP_even=H0_dR⊕H2_dRはrank6で恒等作用、HP_odd=0。HKRの一般理論自体は既知。
Exact同値でg*を移した関手の通常entropyはなお零。射のaction filtrationにlog Lambdaを移すには、両方向の線型filtration比較と特定gへの同変性が追加で必要。Côté–Kartalの静的growth比較だけではこの仮定を自動的に満たさない。元の非可換H3圏の自己同値も未構成。

## IV. 優先課題と具体的着手

**第一優先：filtered局所化を実際のmirror作用へ移す。**
同じgを覆うHMSを形式的に仮定するだけでなく、境界localizationに適合したmirrorの対象LとEnd(L)を選び、極次数がReeb/action filtrationへどう移るかを一Vietaの局所模型で計算する。通常のPerf(U)のentropyは零と決定済みで、正値の再発見を目指さない。holomorphic symplectic形式保存と選択したLiouville構造のexact自己同型を混同しない。

**並行して優先：境界曲線の局所特異性から成長を精密化する。**
閉包の算術種数の指数増大を、境界の各枝のPuiseux型、intersection multiplicity、linkの型で説明する。n=1,2の局所展開とnormalizationの端点を先に求め、Pell重み・連分数と比較する。種数公式だけから二枝やtorus knot型を結論しない。対象複雑度の2log Lambdaが、resolutionやstopped categoryでどう分解されるかを調べる。

**並行して優先：三成分の有理Hodge同型の幾何学化。**
3捩れperiod差を境界線束の変更・有限被覆・代数的対応として構成できるか、Klein7/21のline配置から調べる。有理Hodge同型から曲面や圏の同値を推論しない。Spin8→G2のcharacter、torsion位数の変化、全rank五接続の構成も維持する。

**支える課題：非可換成分と未監査部分。**
N5,M5のbranchと観測値衝突を分離し、Sklyanin方向の純粋q障害相殺、Vietaの心の変更、全H3 admissibility・intrinsic降下・全境界を継続する。公表前には旧依存定理も独立に監査する。一枝の重い計算だけに研究を固定しない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_localization_entropy.py
python3 computations/verify_all.py  # 全31検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回実行した新検証器はQ[A,B,C,h]と整数行列でPASS。一反復、Hilbert値、交叉恒等式、n=0..24のPell行列・種数を確認。証明書は `computations/localization_entropy_certificate.json`。全nの理論、DHKK entropy・proper比較、正規化種数、HKR/巡回比較は本文の通常証明と一次文献への依存で、有限検算のみの形式証明ではない。旧30検証器は今回全再実行していない。
新節を一時的LuaLaTeX wrapperで5頁に組版・画像点検した。内部参照は解決、前節のPell定理は抜粋用の参照名で表示し、overfullはない。主論文全体の今回の再組版、全旧証明の独立再監査、filtered mirror構成、新規性の網羅調査は未実施。
主論文の差分を確認し、旧証明本文・入力節・文献表を保持して新節を統合した。保存後にmain refと必要ファイル、実行コードとの一致を確認する。生成PDF・wrapper・画像・ログをGitに入れず、push済み内容をLibraryへ保存しない。
