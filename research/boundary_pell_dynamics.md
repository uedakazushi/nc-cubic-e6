# 境界Pell力学・局所化・三つの成長率

2026-11-17 / e6-connections-v26。最初に `../00_research_plan.md` を読む。
証明は主論文の `quantum_cubic_boundary_dynamics.tex` と `quantum_cubic_localization_entropy.tex`。前提のH2恒等性と古典entropyは `quantum_cubic_triality_isogeny.tex` の `prop:period-invisible-entropy`。本ノートは現行の式・注意・文献・次の着手を整理する。

## 1. 同じ写像の異なる観測

滑らかなU={uvw−(u²+v²+w²)/2−Au−Bv−Cw=h}、通常の三次閉包S、三角境界D=D_u+D_v+D_w。g=iota_v iota_w iota_u iota_w（右から合成）、sigma=g*、Lambda=3+2sqrt2。各Vietaは該当座標を2*(他二座標の積)−元座標−2*(対応係数)へ移す。
Goldman–Neumannの既知定理からgはH2(U,Z)で恒等、留数形式omegaと全periodを固定する。今回は旧H2証明全体を独立再監査したわけではない。
現在の比較は、通常のPerf(U)のDHKK entropy=0、射のpole filtration歪み率=log Lambda、自然な曲線閉包列のproper対象複雑度率=2log Lambda。第三の値は自己関手のentropyではない。対象、射、filtration、閉包を分けることが必要である。

## 2. 境界付値と最小次数（保持する既存証明）

u頂点の局所式T=2VZ*unitで、重み(alpha,beta)の座標極次数は(alpha+beta,beta,alpha)。三頂点を貼るとC={(a,b,c)≥0,2max(a,b,c)=a+b+c}\{0}。Theta(r,t)=(|r|,|t|,|r+t|)により(R²\{0})/±と同定。有理方向はcorner blow-upで抽出可能。
Vietaの反射T_u=(2max(b,c)−a,b,c)（巡回）。積恒等式u*iota_u(u)=v²+w²+2Bv+2Cw+2hを使い、直接maxによる先頭消去の見落としを避ける。同重みの二平方は別Laurent単項式であり、単項式付値では消えない。
Theta上のRu=[[-1,-2],[0,1]], Rv=[[1,0],[-2,-1]], Rw=diag(1,-1)、合成は−M、M=[[1,-2],[-2,5]]。符号商ではMと同じで、係数非依存。

N=[[1,2],[2,5]]、(p_n,q_n)=N^n(1,1)。n≥1のg^n三座標の最小次数は(p_n,q_n,q_n−p_n)。最高項はu,vだけの単項式で、gr O(U)=C[u,v,w]/(uvw)上非零だから曲面関係で次数を下げられない。
M^n=[[a_n,-b_n],[-b_n,c_n]]、d_n=q_n=b_n+c_nは1,7,41,239,1393,8119,...、d_(n+2)=6d_(n+1)−d_n。d_n²−2c_n²=−1、d_n+c_n sqrt2=(1+sqrt2)^(2n+1)。
H=[D]のgeneric引戻しはn≥1で(g^n)*H=c_nD_u+b_nD_v+d_nD_w、交点次数は2d_n。n=0ではH²=3なのでこの式をgeneric Hへ適用しない。写像がS上のmorphismという意味でもない。

## 3. 固有付値・非正則化・抽出深さ

Mの固有線は(1,−1−sqrt2)、(1,−1+sqrt2)。極次数でv_+=(1,1+sqrt2,sqrt2)、v_-=(1,sqrt2−1,sqrt2)。射影作用はnorth–south型で有理方向に周期点がない。
有限境界point blow-up後も元のD_iのstrict transformは残る。正則自己同型なら有限個の境界成分を置換するため付値は周期的となり矛盾。従って指定Sを支配する有限境界blow-up上には正則自己同型へ延長できない。全ての別コンパクト化やalgebraic stabilityの不存在は主張しない。
nu_n=g_*^n ord(D_w)の極次数は(3,7,4),(17,41,24),(99,239,140),...、局所原始重みは(p_n,q_n−p_n)。比は[1;2,...,2,3]（2は2n−2個）なので最小corner抽出回数は4n。これは一付値の抽出回数であり、g^nの全indeterminacy解消回数ではない。

## 4. 通常の圏的entropyが零となる理由

任意の非空アフィンX=Spec Rの自己射fで、RはPerf(R)のsplit generator、Lf*R≅R。DHKK三角塔のdelta_t(R,R)≤1。任意の点pへのderived tensorでdelta_t(k(p),k(p))=1≤delta_t(R,R)となるのでdelta=1、h_t(Lf*)=0（全実t）。この命題は定義の初等的帰結で、新しい一般理論とはしない。
非proper圏にproper用の有限次元Ext公式を流用しない。対象Rを固定しても、そのEnd環Rにはsigmaが非自明に作用する。従って関手は恒等とは限らない。
**方法上の障害：** Perf(U)に共役なmirror関手の通常entropyも零である。正の古典entropyだけからwrapped圏の通常entropyの正値を結論してはならない。

## 5. 極filtrationと射の歪み

F_mR=H0(S,O(mD))/s_D^m（sectionで割って関数と読む、vector space quotientではない）。三次hypersurfaceの斉次制限の全射により、これは全次数≤mの多項式像。dim F_m=(3m²+3m+2)/2、R=colim Hom_S(O,O(mD))。
V=<1,u,v,w>に対しell_V(n)=min{r≥1:sigma^n V⊂V^r}=d_n。全mでsigma^n(F_m)⊂F_(d_nm)となり、m=1が倍率の最小性を与える。
一般の有限次元生成空間V,V'はV⊂(V')^a、V'⊂V^bで比較でき、ellの比は定数ab以内。ell(n+m)≤ell(n)ell(m)から極限が存在し、指数率log Lambdaは生成元・線型同値なfiltrationに依存しない。これは特定写像の歪みであり、Côté–Kartalの静的growth関数そのものではない。
もし同値filtration Gでsigma(G_m)⊂G_(m+C)が全mに成り立てば反復でO(n)となるので不可能。filter-preservingまたはgraded Rees自己同型のliftもその意味で排除される。
sigma^n(F1)自体は次元4のままで、dim F_(d_n)~(3/2)d_n²は像を収める極予算の大きさ。像の次元が増大すると誤記しない。

## 6. 閉包の算術種数とproper対象の成長

kappaを一般に選びC0={v=kappa}が滑らかな既約affine conicとなるようにする。C_n=g^-n C0は同型なsmooth rational affine曲線。S内の閉包をbar C_nとする。
境界v座標の極はTheta(M^n*(0,1)), Theta(M^n*(1,0)), Theta(M^n*(1,-1))の第二成分。従って**全n≥0**で
P_n=[bar C_n]=c_nD_u+b_nD_v+d_nD_w、H.P_n=2d_n、P_n²=4b_nc_n。
p_a(bar C_n)=1+2b_nc_n−d_n、chi(O_barC_n)=d_n−2b_nc_n。
最初の(degree,genus)は(2,0),(14,14),(82,656),(478,23422)。normalizationはP1、U内は滑らかなので、算術種数は境界のlocal deltaの総和に等しい。個別のPuiseux型はまだ分類していない。

Q_n=O_barC_n、任意のsplit generator E of Perf(S)に対しlim log delta0(E,Q_n)/n=2log Lambda。下界はtotal Hom(O,Q_n)≥|chi(Q_n)|と三角塔の劣加法性。上界はDHKK saturated比較（Thm2.6証明Eq9）を用いる。E∨を固定bundleの有界複体にし、P_nを2d_n個の境界成分に分ける。途中のTについて|T.D_i|=O(d_n)、B|D_iは固定splittingなので一段のcohomology=O(d_n)。全段を足してO(d_n²)、Hypercohomologyも同じ。この通常証明を有限検算だけの結果としない。
一方j*Q_n=[R --sigma^n(v)-kappa--> R]なのでdelta0(R,j*Q_n)≤2。
**閉包操作はexact functorでない。** Q_nが一関手の反復像とは示しておらず、2log Lambdaは対象列の増大率。もしexact FbarでFbar^n Q0≅Q_nが成立するならh0(Fbar)≥2log Lambdaが必要となるが、liftの存在は未証明。

## 7. Hochschild・periodic cyclic・wrapped比較

smooth affine HKRからHH0(R)=R、HH2(R)=R omega。omega不変なので両者の極filtration歪み率はlog Lambda。古典mixed-complex HKR/de Rham比較ではHP_even=H0_dR⊕H2_dR（rank6）、HP_odd=0、g作用は既存H2恒等性から恒等。無限次元filtered HHで見える成長が有限HPと通常対象entropyで消える。

Exact同値Psi:Perf(U)≅Cを仮定してL=Psi(O)、Phi=Psi Lg* Psi^-1とすれば通常h_t(Phi)=0。End(L)のaction filtrationとpole filtrationが相互に線型比較され、特定gの射への作用が共役する場合に限り、射歪みのlog Lambdaが移る。
Côté–Kartalの静的growth比較だけから個別関手への同変性や一様filtered比較は従わない。本稿ではこのgに対するfiltered equivariant HMSは未構成。holomorphic symplectic形式を保つことから、選択Liouville構造のexact symplectomorphismを推論しない。また本節は可換な中心曲面で、元の非可換H3圏の自己同値ではない。

## 8. 一次文献と適用範囲

- G. Dimitrov, F. Haiden, L. Katzarkov, M. Kontsevich, *Dynamical systems and categories*, arXiv:1307.8418, https://arxiv.org/abs/1307.8418 。Definitions2.1,2.4、Proposition2.2、Lemma2.3、Theorem2.6の証明Eq(9)を一次PDFで確認。後者は対象によらない定数で三角塔複雑度とtotal Extを比較し、proper部分の上界にのみ使用。
- L. Côté, Y. B. Kartal, *Categorical action filtrations via localization and the growth as a symplectic invariant*, J. Reine Angew. Math. 801 (2023), 173–238, DOI https://doi.org/10.1515/crelle-2023-0037 ; arXiv:2108.05938v3。§5.2.2 (5.9)–(5.10)、Cor5.26、Thm5.27、§7.1.1 Cor7.1–7.2を一次本文と該当PDF画像で確認。pole-orderとReeb-lengthのgrowth比較を既知の枠組みとして使う。
- B. Antieau, *Periodic cyclic homology and derived de Rham cohomology*, Ann. K-Theory4 (2019), 505–519, DOI https://doi.org/10.2140/akt.2019.4.505 。§3とIntroductionの古典的標数零比較への参照を確認。今回必要なのはsmooth C代数のmixed-complex HKR。PDF screenshotは取得エラーで、本文式を確認。
- S. u. Jang, *Tropical Dynamics of Markov Surfaces*, arXiv:2306.11357v2, https://arxiv.org/abs/2306.11357v2 。取得版2025年12月、Lemma4.8とTheorem4.10。R²/±線型化は既知。別版題名と節番号を混在させない。
- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier59 (2009),2927–2978, DOI https://doi.org/10.5802/aif.2512 。出版版§3.1、著者長稿 *Holomorphic dynamics, Painlevé VI equation and character varieties* §4.2 Remark4.5の境界blow-up/circle作用とentropyを参照。版の番号を区別する。

DHKK・局所化filtration・HKR・tropical線型化の一般理論は既知。今回の独自の位置付けは、明示的なPell写像に三つの異なる測定を適用し、境界種数と局所化による複雑度消失を正確に比較したこと。各帰結の文献新規性の網羅調査は未了。

## 9. 未解決の具体課題と再現

第一の課題は一Vietaの境界localizationとmirrorの射のaction filtrationを明示し、特定gへの同変性を検証すること。第二はC_nのnormalizationの二端点を追い、局所Puiseux型・枝間交叉・linkを求めること。
有用な未証明の観察として、p_a=2bc−b−c+1は「互いに素の重み(b,c)を持つ二枝、各delta=(b−1)(c−1)/2、相互交叉bc」の総和と一致する。しかし数値の一致だけで二枝の型や集中点を決定したことにはならない。n=1,2で局所展開を行うのが具体的着手である。

`verify_boundary_pell_dynamics.py` のv25検算は保存済み。今回実行したのは `verify_localization_entropy.py` のみで、全係数一反復、Hilbert値、交叉式、n=0..24の整数行列・種数を厳密確認してPASS。小証明書は `localization_entropy_certificate.json`。全nの証明、圏論、正規化種数、HKRは通常証明として分ける。
新節単体を日本語LuaLaTeX5頁に組版し全頁を画像点検。内部参照は解決、外部Pell定理は抜粋用参照名を表示、overfullなし。主論文全体の今回の組版、旧30検証器全再実行、旧証明の独立査読、新規性網羅調査は未実施。
GitHub mainが正本。push済み内容をLibraryに保存しない。
