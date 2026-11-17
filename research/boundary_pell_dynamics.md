# 境界Pell力学・局所化・トーラス絡み目

2026-11-18 / publication-v32。再開時は [研究方針](../00_research_plan.md) を最初に読む。
公表用原稿は [cubic-boundary-prym.tex](../papers/cubic-boundary-prym.tex)。完全な証明は同稿が入力する `quantum_cubic_boundary_dynamics.tex`, `quantum_cubic_localization_entropy.tex`, `quantum_cubic_boundary_links.tex` にある。H2恒等性は境界力学節でGoldman–Neumann Theorem 2から直接導く。Fricke周期と古典entropyの背景は [fricke-geometry.tex](../papers/fricke-geometry.tex) を参照する。本文の証明、文献依存、実行した検算、組版の状態は [公表準備の確認状況](publication_status.md) と [検算結果](../computations/validation.json) で区別する。

## 1. 記号と観測の区別

滑らかなU={uvw−(u²+v²+w²)/2−Au−Bv−Cw=h}、通常の三次閉包S、三角境界D=D_u+D_v+D_w。g=iota_v iota_w iota_u iota_w（右から合成）、sigma=g*、Lambda=3+2sqrt2。各Vietaは該当座標を2*(他二座標の積)−元座標−2*(対応係数)へ移す。
Goldman–Neumann Theorem 2からgはH2(U,Z)とperiodで恒等、留数形式omegaを保存する。同論文への変換は(x,y,z)=(2u,2v,2w)、(P,Q,R)=(-4A,-4B,-4C)、fiberの値-8h-2。各VietaのH2作用は-Iなので四つの積は恒等。
同じgについて、通常のPerf(U)のDHKK entropy=0、射の極filtration歪み率=log Lambda、曲線閉包の対象列の増大率=2log Lambda。正規化層はlog Lambda、一点欠損層は2log Lambdaとなる。対象列の率を自己関手entropyと呼ばない。

## 2. 境界付値・最低次数・Pell単数

u頂点の局所式T=2VZ*unitから、重み(alpha,beta)の座標極は(alpha+beta,beta,alpha)。三頂点を貼るとC={(a,b,c)≥0:2max(a,b,c)=a+b+c}\{0}。Theta(r,t)=(|r|,|t|,|r+t|)で(R²\{0})/±と同定。有理方向はcorner blow-upで抽出可能。
Vieta反射T_u=(2max(b,c)−a,b,c)（巡回）は積恒等式u*iota_u(u)=v²+w²+2Bv+2Cw+2hで検証する。直接2vw−u−2Aにmaxを適用すると先頭消去を見落とす。同重みの二平方は別Laurent単項式なので単項式付値では消えない。
Theta上のRu=[[-1,-2],[0,1]], Rv=[[1,0],[-2,-1]], Rw=diag(1,-1)、積は−M、M=[[1,-2],[-2,5]]。符号商ではMと同じ、係数非依存。
N=[[1,2],[2,5]]、(p_n,q_n)=N^n(1,1)。g^nの三座標の最低次数はn≥1で(p_n,q_n,q_n−p_n)。最高項はu,vのみの単項式でgr O(U)=C[u,v,w]/(uvw)上非零だから曲面関係で次数を下げられない。
M^n=[[a_n,-b_n],[-b_n,c_n]]、d_n=q_n=b_n+c_n。c_n=a_n+2b_n、a_nc_n−b_n²=1。d=1,7,41,239,...、d_(n+2)=6d_(n+1)−d_n、d_n²−2c_n²=−1、d_n+c_n sqrt2=(1+sqrt2)^(2n+1)。
H=[D]のgeneric引戻しはn≥1でc_nD_u+b_nD_v+d_nD_w、H交点次数2d_n。n=0のgeneric H²=3とは区別し、写像がS上のmorphismという意味ではない。

## 3. 無理固有方向と解消深さ

Mの固有線(1,−1−sqrt2)、(1,−1+sqrt2)は極でv_+=(1,1+sqrt2,sqrt2)、v_-=(1,sqrt2−1,sqrt2)。射影作用はnorth–south、有理方向には周期点がない。
指定Sを有限回境界point blow-upしても、元のD_iのstrict transformが有限境界成分として残る。正則自己同型なら付値が周期的になり矛盾。指定Sを支配するこの範囲での非正則化であり、全コンパクト化やalgebraic stabilityの不存在ではない。
g_*^n ord(D_w)の極は(3,7,4),(17,41,24),(99,239,140),...、局所原始重み(p_n,q_n−p_n)。比[1;2,...,2,3]で2は2n−2個、最小corner抽出回数4n。全indeterminacyの解消回数ではなく、一指定付値の抽出深さ。

## 4. 通常のentropyと射のfiltration

任意の非空アフィンX=Spec Rの自己射fでRはsplit generator、Lf*R≅R。delta_t(R,R)≤1、点の剰余体へのderived tensorから逆不等式を得るのでdelta=1、h_t=0（全実t）。定義の初等的帰結。対象固定とEnd環の恒等作用は異なる。非proper圏にproper用有限次元Ext公式を流用しない。
F_mR=H0(S,O(mD))/s_D^mはsectionで割って関数と読む意味で、vector-space quotientではない。三次斉次環の制限全射から全次数≤mの多項式像と一致、dim F_m=(3m²+3m+2)/2。R=colim Hom_S(O,O(mD))。
V=<1,u,v,w>の像を収める最小倍率ell(n)=d_n。全mでsigma^n F_m⊂F_(d_nm)。Feketeと生成空間の相互有限次数包含から歪み率log Lambdaは生成元・線型同値filtrationに不変。sigma^n(F1)の次元は常に4で、増えるのは極予算。
同値filtrationでsigma(G_m)⊂G_(m+C)が全mに成立すれば反復は線型なので不可能。その意味のfilter-preserving/Rees liftも排除される。
これはCôté–Kartalの静的次元growthではなく、特定自己同型が必要とする次数倍率である。

## 5. 曲線閉包の交叉とproper複雑度

C0={v=kappa}が滑らかなconic、C_n=g^-n C0、bar C_n⊂S。全n≥0で
P_n=[bar C_n]=c_nD_u+b_nD_v+d_nD_w、D.P_n=2d_n、P_n²=4b_nc_n。
delta_n=p_a=1+2b_nc_n−d_n、chi(O_barC_n)=d_n−2b_nc_n。
最初の(degree,genus)=(2,0),(14,14),(82,656),(478,23422)。C_nは同型なsmooth rational affine曲線なので種数は境界のlocal deltaの総和。
Q_n=O_barC_nのproper対象複雑度率は2log Lambda。Euler数の下界と、固定bundleを境界成分毎にO(d_n)ずつ2d_n回評価したO(d_n²)上界、DHKK saturated比較による。
j*Q_n=[R --sigma^n(v)-kappa--> R]でdelta0≤2。閉包はexact functorでないので、2log Lambdaを関手entropyとしない。もしFbar^n Q0=Q_nとなるexact関手を構成できればh0(Fbar)≥2log Lambdaが必要だが、存在は未証明。

## 6. 二枝のPuiseux型とtoric上の係数保存

公表用原稿 `thm:two-boundary-Puiseux`、`cor:boundary-trace-recovered`。
明示条件はkappa²≠1と
N_v(kappa)=(kappa²+2Bkappa+2h)(kappa²−1)+A²+C²+2kappa AC≠0。
出発conicはu²+w²−2kappa uw+2Au+2Cw+kappa²+2Bkappa+2h=0。
無限遠二点でs=1/u、w=rho/s+O(1)、rho=rho±=kappa±sqrt(kappa²−1)。

**全n≥1での逆像の先頭式：**
u_n=2^(c−1)rho^b s^(−c)(1+O(s)),
v_n=2^(b−1)rho^a s^(−b)(1+O(s)),
w_n=2^(d−1)rho^(a+b)s^(−d)(1+O(s))。
一反復は(16rho²s^-5,2rho s^-2,64rho³s^-7)。次反復で(b,c)→(b+2c,2b+5c)、rho指数もa',b'へ移り、全係数で先頭消去がない。g^{-1}の順序はi_w i_u i_w i_v（右から）。

二点はともにp_w=[0:0:1:0]へ移り、局所座標x=u/w,y=v/wでは
x=2^(-b)rho^(-a)s^b(1+O(s)), y=2^(-c)rho^(-b)s^c(1+O(s))。
gcd(b,c)=1より各枝の唯一のPuiseux対は(b,c)。ac−b²=1よりy^b/x^c→rho。二値が異なるため枝間交叉はbc、最低重み式はy^(2b)−2kappa x^c y^b+x^(2c)。開部分はsmooth、正規化の無限遠は二点だけなので、閉包の特異点はp_wのみ。
primitive重みray(b,c)を抽出したtoric変更後、二枝は例外torusのz=y^b/x^c=rho±で横断的。z+z^-1=2kappaに元のconic係数が残る。**解析的右同値を重み付き斉次代表まで証明したわけではない。**

## 7. Torus link・conductor・有限Milnor monodromy

公表用原稿 `thm:boundary-torus-link`。
linkはT(2b,2c)、二成分それぞれT(b,c)、linking=bc。
delta_branch=(b−1)(c−1)/2、delta_total=1+2bc−b−c、mu=(2b−1)(2c−1)=2delta−1。
正規化環C[[s+]]⊕C[[s−]]のconductorはs+^delta C[[s+]]⊕s−^delta C[[s−]]。各枝のconductor指数はmu_branch+他枝交叉=(b−1)(c−1)+bc。dx/f_yの位数も−deltaを与える。
Milnor fiberは二境界、genus delta−1。H1 monodromyの特性多項式は
(T^(2bc)−1)²(T−1)/((T^(2b)−1)(T^(2c)−1))。
b偶・c奇・互いに素なので(b+c)/(2bc)がprimitive固有値を与え、正確な位数2bc。各nのspectral radiusは1。位数の列の増大率2log Lambdaを、局所monodromyが正entropyを持つことと混同しない。
最初の(link,delta,mu,order)：T(4,10),14,27,20；T(24,58),656,1311,696；T(140,338),23422,46843,23660。
Milnor fibrationのtopological型を重み付き代表で計算するのであり、全germの解析的等価を使わない。

## 8. 正規化完全列が分離する成長

公表用原稿 `thm:normalization-defect-growth`。
nu_n:P1→bar C_n、B_n=nu_*O_P1、Z_n=B_n/Q_n。Z_nはp_wだけに支持されlength delta。H0(Q_n)→H0(B_n)はCの恒等、H1(B_n)=0だからH1(Q_n)=H0(Z_n)。前節の全種数は一つの点の正規化欠損となる。
任意proper split generator Eに対し、B_nの率log Lambda、Z_nの率2log Lambda。
Z_nの上界はlength個のk(p_w)からのcomposition series、下界はH0 length。
B_nの下界はHom(O(1),B_n)=H*(P1,O(−2d_n))の全次元2d_n−1。上界は固定vector bundle VについてV(mH),V∨(mH)の大域生成を使い、nu*Vの分裂次数を±2md_n以内に挟んでO(d_n)とする。DHKK proper比較を用いる。
開制限ではB_n=Q_n=O_Cn、Z_n=0。これは対象列の正確な成長率で、新しい自己関手は未構成。

## 9. Chebyshev divideと局所Weinstein模型

公表用原稿 `prop:Pell-Chebyshev-Weinstein`。
weighted代表x^(2c)−y^(2b)に対し
F_epsilon=epsilon^(2bc)[T_(2c)(x/epsilon^b)−T_(2b)(y/epsilon^c)]。
cosine extremaの格子がmu個の実Morse点で、同parityのdelta点は零levelのreal node、異parityのdelta−1点は極値。leading係数の尺度変更で元のweighted代表へ戻る。
Casals Thm1.1/Cor1.2はこのreal morsificationから、linkのmaximal-tb Legendrian近似に対応するWeinstein pair(C²,L_n)のclosed arboreal skeletonを与える。Lagrangian曲面のgenus delta−1、境界2、thimble mu個が具体的に指定される。二2-handleで閉じた四多様体のEulerは3。元のUのEuler6と違うのでglobal Uの模型と同一視しない。
異なるnの局所模型を結ぶexact functor/cobordismや、gに同変なwrapped比較は未構成。まずn=1のT(4,10)のdivide/quiverと、正規化完全列・conductorの対応を求める。

## 10. Hochschild・periodic cyclic・mirrorの必要条件

smooth affine HKRでHH0=R、HH2=R omega。omega不変なので極filtration歪みlog Lambda。HP_even=H0_dR⊕H2_dRはrank6でg恒等、HP_odd=0。無限次元filtered HHで見える成長が有限HPと通常対象entropyでは消える。
Exact同値Psi:Perf(U)≅CとL=Psi(O)を仮定して共役しても通常entropyは零。End(L)のaction filtrationと極filtrationの相互線型比較、特定gの射への同変性を別に証明できた場合だけ、射の歪み率log Lambdaが移る。Côté–Kartalの静的growth比較だけではこの仮定は従わない。
gがholomorphic symplecticを保つだけで選択Liouville構造のexact symplectomorphismとはしない。対象は可換中心曲面であり、関連する非可換曲面の圏への自己同値の持上げは未構成である。

## 11. 一次文献と確認範囲

- W. M. Goldman, W. D. Neumann, *Homological action of the modular group on some cubic moduli spaces*, Math. Res. Lett.12 (2005),575–591, DOI https://doi.org/10.4310/MRL.2005.v12.n4.a11 ; https://arxiv.org/abs/math/0402039 。Theorems 1–2で滑らかなfiberのH2=Z5とlevel2合同部分群の符号作用を確認。本文の正規化変換は上の§1。
- R. Casals, *Lagrangian skeleta and plane curve singularities*, J. Fixed Point Theory Appl.24 (2022),34, DOI https://doi.org/10.1007/s11784-022-00939-8 。公開原本文Thm1.1、Cor1.2、Example1.3後のChebyshev、§2.1 Remark2.1、§2.2 divideを確認。一般理論は既知。局所絡み目への適用に限定する。
- D. Kerner, V. Vinnikov, *On the determinantal representations of singular plane curves*, arXiv:0906.3012v1, https://arxiv.org/abs/0906.3012v1 、2009年6月版§2.2.3 Definition–Proposition2.2、(7)。conductor指数mu_i+sum intersectionを原PDFテキストで確認。
- C. Hertling, M. Mase, *The combinatorics of weight systems and characteristic polynomials of isolated quasihomogeneous singularities*, J. Algebr. Comb.56 (2022),929–954, DOI https://doi.org/10.1007/s10801-022-01138-x 。原公開本文Thm6.4(a)のMilnor–Orlik公式を確認。原Milnor–Orlik論文はTopology9 (1970),385–393。原Milnor–Orlik論文全体の確認は未了。
- G. Dimitrov, F. Haiden, L. Katzarkov, M. Kontsevich, *Dynamical systems and categories*, arXiv:1307.8418, https://arxiv.org/abs/1307.8418 。Definitions2.1,2.4、Prop2.2、Lemma2.3、Thm2.6証明Eq(9)を参照する。proper対象列の上界に比較を用いる。
- L. Côté, Y. B. Kartal, *Categorical action filtrations via localization and the growth as a symplectic invariant*, J. Reine Angew. Math.801 (2023),173–238, DOI https://doi.org/10.1515/crelle-2023-0037 ; arXiv:2108.05938v3。§5.2.2 (5.9)–(5.10)、Cor5.26、Thm5.27、§7.1.1 Cor7.1–7.2。pole/Reeb growthの比較枠組みで、個別gの同変性は追加事項。
- B. Antieau, *Periodic cyclic homology and derived de Rham cohomology*, Ann. K-Theory4 (2019),505–519, DOI https://doi.org/10.2140/akt.2019.4.505 。§3とIntroductionの古典的標数0比較。smooth C代数のmixed-complex HKRとして使用。
- S. u. Jang, *Tropical Dynamics of Markov Surfaces*, arXiv:2306.11357v2, https://arxiv.org/abs/2306.11357v2 、取得2025年12月版Lemma4.8、Thm4.10。R²/±線型化は既知。別版の題名・番号を混在させない。
- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier59 (2009),2927–2978, DOI https://doi.org/10.5802/aif.2512 、出版版§3.1。著者長稿 *Holomorphic dynamics, Painlevé VI equation and character varieties* §4.2 Remark4.5の境界blow-up/circle作用は版を区別する。

平面曲線・Milnor・Weinstein・DHKK・tropical理論自体は既知。本稿の役割は、同じPell写像でPuiseux型・link・種数・正規化欠損・対象成長を接続すること。個別適用の新規性の網羅確認は未了。

## 12. 再現と次の課題

再現コードは `computations/verify_boundary_pell_dynamics.py`, `verify_localization_entropy.py`, `verify_boundary_torus_links.py`。境界chamber、Pell行列、全係数一反復と帰納式、Hilbert値・交叉式、有限範囲の整数値、n=1模型のJacobi次元27・conductor14、monodromy多項式、Chebyshev resultantsを検算する。各証明書は同じ `computations/` 内にある。`computations/validation.json` は全36検証器の実行をPASSとして記録している。全nの主張、解析/位相、DHKK、Casalsの構成は本文の通常証明と引用した定理による。独立査読、新規性の網羅調査、原稿組版の最新状態は [公表準備の確認状況](publication_status.md) を参照する。

次はn=1 divideの交叉とmicrolocal quiver、正規化完全列の局所圏への像、反復間のtoric共通解消とexact cobordismの可能性を調べる。局所模型の存在だけでglobal mirror/g作用を主張しない。三成分Hodge比較の幾何学化は関連するFricke研究で扱う。
保存と再開の規則は [研究方針](../00_research_plan.md) に従う。
