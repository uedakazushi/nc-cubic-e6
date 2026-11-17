# Cayley・LG・消滅サイクル・G2・braidと周期

2026-11-17 / e6-connections-v22。再開時は `../00_research_plan.md` を先に読む。
完全な証明は主論文が読み込む `quantum_cubic_cayley_lg.tex`、`quantum_cubic_lg_picard.tex`、`quantum_cubic_g2_braids.tex`、`quantum_cubic_log_periods.tex`（すべて `../papers/sections/`）。本ノートは現在必要な式・区別・文献・未解決の核心をまとめ、全文証明を重複させない。

## 1. 共通模型と係数の区別

一次元表現の正規化u=(1-q)x等、A=(1-q)a等から
Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。
W_{A,B,C}=H−Au−Bv−Cwの相対臨界スキームは有限平坦五重被覆、graph(dH)はT*A3内のexact Lagrangian。
一次元表現の総空間E=A3_{u,v,w}、係数底S=A3_{A,B,C}、量子代数の中心Y=Spec k[X,Y,Z,Omega]/Pを区別する。
W=hにp=-2u,r=-2v,s=-2wを入れるとFricke係数は(-4A,-4B,-4C,8h)。射影閉包はuvw−t(u²+v²+w²)/2−t²(Au+Bv+Cw)−ht³=0、無限遠三角形に沿って常に滑らか。
量子Casimir中心Omega=-D0を同じ等位面で読む際は、A=(D0a+ell_a)/(4e²)等、h=−(D0³−fD0²+D0K−L)/(8e³)、u=X/(2e)等という**別の底変更**。A=(1-q)aと同一視しない。

## 2. Cayley・トーラス・Poisson

J=Hess H=[[-1,w,v],[w,-1,u],[v,u,-1]]、det J=R=u²+v²+w²+2uvw−1。ramification divisorはCayley曲面で、x=-2u等ならx²+y²+z²−xyz−4=0。
トーラス表示u=−(r+r^-1)/2、v=−(t+t^-1)/2、w=−(rt+(rt)^-1)/2は同時反転商(Gm)²/±、閉トーラスSL2粗指標多様体。四A1点は±1三つ組で積−1。
{r,t}=rtから{u,v}=−R_w/2（巡回）。GL2(Z)単項式作用はPGL2(Z)として降り、det1でPoisson、det−1で反Poisson。分岐源上の括弧と量子中心のroot括弧9倍は違う。Cayley modular作用のE→S全体への延長は未構成。

## 3. D4 germとミニバーサル変形

Rの四節点sigma（±1、積−1）の像は−2sigma。fiberはsigmaの長さ4と−2sigmaの単純点1。
代表sigma=(-1,-1,-1)、底(2,2,2)でu=-1+x,v=-1+y,w=-1+ell−x−y、A=2+alpha等、L=ell−xy+gammaと置くと
W=−L²/2−xy(x+y)+x²y²/2−gamma xy−(alpha−gamma)x−(beta−gamma)y
  +7/2+alpha+beta+gamma+gamma²/2。
局所Jacobi基底1,x,y,xy、x²=y²=-2xy、x²y=xy²=0。三係数の非定数微分−x,−y,x+y−xyが独立で、加法定数を除くミニバーサル変形。別sheetのdet J=27。
巡回置換はHessian核で(x,y)↦(y,−x−y)。指定退化のMilnor/Picard比較は§6で構成済みだが、全域の標準分裂や圏同値ではない。

## 4. 留数代数と値衝突

係数原点の五sheetは0と四符号点eta（積+1）、全てetale。Hessian determinantは−1,4,4,4,4なのでtau(g)=−g(0)+(1/4)sum_eta g(eta)が非退化留数対を与える。基底1,u,v,w,uvwのGram determinantは−1。Frobenius代数であり、primitive form/Frobenius多様体は未構成。
Omega_E=f(uvw−u²−v²−w²)/3の原点fiber値は0と−2f/3（4回）、N5=D(D−2f/3)^4。被覆の分岐と観測値衝突は別。power basis=(任意基底)Tならdisc(power basis)=(det T)²disc(任意基底)。
Wの臨界値は−2uvw+(u²+v²+w²)/2でOmega_Eとは違う。LG Maxwell locusとCasimir値衝突を同一視しない。

## 5. 実型・elliptope

正規化多項式は実型を持つがqが実になる意味ではない。C=−Hess Hの半正定値領域は3-elliptope。det C=−R、境界はR=0と[-1,1]³の交わりで、単位円トーラス商によるSU2 pillowcase。
内部は凸でHessian負定値なのでPhiは単射。任意実係数で内部sheetは高々一つ。Dixonのnearly Kähler S3×S3のmulti-moment像と同じ凸体だが、追加の圏同値・計量退化は未構成。

## 6. Milnor–Picard整数比較とtriality

滑らかなU={W=h}の三次コンパクト化S、境界D=D1+D2+D3について
0→Z delta_infty→H2(U,Z)→K=<D_i>^perp→0、H1(U,Z)=0。
六点blow-upでD_i=L−E_(2i−1)−E_(2i)。E1,E3,E5の制限が次数ベクトルの基底なので全射。Kの基底alpha0=L−E1−E3−E5、alpha1=E1−E2、alpha2=E3−E4、alpha3=E5−E6のGramは負D4、det4。左端は原始radical、H2は自由rank5。
底(2,2,2)、h≈7/2の局所D4 Milnor fiber M_hの包含M_h→U_h→S_hはKへ入る。交叉保存と非退化性で単射、両rank4・det4なので指数1の整数格子同型。指定退化でH2(U_h)=H2(M_h)⊕Z delta_infty。全域の選択非依存な標準分裂ではない。
rho=(u,v,w)↦(v,w,u)は境界三本を回す。境界格子BのGramはdiag−1/offdiag1、判別群の三非零元は(D1+D2)/2等。unimodular Picard gluingを介してK*/Kにも同じ作用。W(D4)は判別群へ自明なのでAut(D4)/W(D4)=S3への像はorder3の外部triality。局所とPicardで一致。所在：`thm:lg-integral-picard-sequence`, `thm:lg-D4-Picard`, `cor:lg-picard-triality`。

## 7. affine D4・境界位相・混合Hodge

Goldman–Neumannの交叉形式は四外側o_iと中央cの負affine D4。primitive radical delta=o1+o2+o3+o4+2c。基底(c,o1,o2,o3,delta)はunimodularでD4(-1)⊕0へ変換。Picardではc→alpha0、o1..3→alpha1..3、o4→−2alpha0−alpha1−alpha2−alpha3。
既存コードの指定順反射積M=s_o1 s_o2 s_o3 s_o4 s_cはcharpoly=(xi−1)²(xi+1)³、M²−I=delta*(1,1,1,1,−2)、rank1かつsquare0。任意の消滅路で同じ行列という主張ではない。
無限遠はmonodromy−IのT² mapping torus、H1=Z⊕(Z/2)²。三次元mapping torusと二次元pillowcaseは別空間。
重みspectral sequenceでGr2 H²=Q(-1)^4、Gr3=0、Gr4=Q(-2)、E_c=1+4xy+(xy)²、Euler6。MHSは一般に分裂としない。§11で一つの内部周期と有理非分裂fiberを具体化したが、全四周期は未決定。

## 8. G2とD4/A2の共通退化

対称LG A=B=C=lambdaはb=-4lambda,c=8hの対称Fricke。Boalch–PalubaのG2底は
alpha=8h+2−12lambda、beta=64lambda³+48lambda²−96lambda h−12lambda−2。
最初の三monodromyを次元6のsemisimple G2共役類、第四を指定regular semisimple共役類に固定した指標多様体は三つの連結成分。LGは一成分。
regular条件では二特異曲線lambda²+2lambda−2h−1=0、−16lambda³−3lambda²+12lambda h+4h²+2h=0と追加conic16lambda²−4lambda−8h−1=0を区別する。LGの滑らかさだけでregular条件を省略しない。
第四をregular unipotent閉包にするとalpha=beta=6、成分式(b+8)(b−1)²。二成分はD4の(b,c)=(-8,28), (lambda,h)=(2,7/2)とA2の(1,1),(-1/4,1/8)。A2点はu=v=w=1/2、Hessian rank2、対角上W=1/8+t³。他三臨界点(5/4,-1,-1)の順列の値は−23/32で同fiberにない。
これは既知のBP退化定理の適用で、G2量子代数やmirror同値ではない。係数fiber重複度2と局所Milnor数2も異なる概念。

## 9. 成分交換とHurwitz：同じB3でも違う作用

`sec:g2-braids-periods`で分離した。
成分選択のchi(xi)=xi³+6xi²+3(1−alpha)xi+beta+2は、z=xi+2、P=alpha+3、Q=beta+6alpha+12でz³−3Pz+Q。A2 Cartan商h/<(23)>→h/S3、label monodromy S3、cusp complement基本群B3。
d=4P³−Q²の引戻しは−C0²S1、C0=b²+b−c−1、S1=b²−8b−4c−16。base map Jacobian3C0。S1の一般点はbranch上にある非分岐第三sheet。cusp(alpha,beta)=(-3,6)で(b,c)=(-2,1)、LG(lambda,h)=(1/2,1/8)は(1/2,-1,-1)の順列に三A1（Hessian determinant9/4）。(6,6)のD4側はC0=27で非分岐、A2側はC0=0。被覆分岐型と曲面特異型は異なる。
内部HurwitzはB1=(u,2uv−w−2lambda,v)、B2=(w,v,2vw−u−2lambda)。右から合成しB1B2=(w,u,v)、braid関係、(B1B2)³=1。体積・W・Poisson・留数形式を保存し、b,cを固定するため各成分を保存してPSL2Zを経由する。底loopのB3と同一視しない。公式はBP(19)、G2同変性はCorollary17。
u≠1でv*=w*=lambda/(u−1)へ移せばB1はM_u=[[2u,-1],[1,0]]。M_u^n=U_(n−1)(u)M_u−U_(n−2)(u)I、U_-1=0。全次数はCayley–Hamiltonで証明、既存コードはn1..7を検算。u²≠1でu=(xi+xi^-1)/2、xiがn乗根なら一生成元のn反復は恒等。二生成元同時線型化ではない。
Klein軌道(lambda,h)=(1/4,0)、(b,c)=(-1,0)のFricke七点を1=(0,0,0),2=(0,0,1),3=(0,1,0),4=(1,0,0),5=(1,1,0),6=(1,0,1),7=(0,1,1)とする。生成元p=(1 3 7 2)(4 5 6)、q=(1 2 6 4)(3 7 5)。q^-1 p q^-2 p q^-1 p³=(5 7)。推移的素数次数と互換からS7、全列挙5040。LG点は−1/2倍。
S7（5040）は七表現同値類の置換像、BP Theorem20のG2(2)'≅U3(3)（6048）は一表現の像。Kleinの168群とも別。このG2底は(-1,-1)、chi=(xi+1)(xi²+5xi+1)、他二成分はQ(sqrt21)上。d=7、alpha²−4beta−12=−7なのでregular。他成分に同じ有限軌道があるとはしない。

## 10. 境界周期の正規化

omega=Res(du∧dv∧dw/(W−h))=du∧dv/(uv−w−C)。projective u_hom=1 chartはF=VZ−t(1+V²+Z²)/2−t²(A+BV+CZ)−ht³、F_t(0)=−1/2、t=VZ a(V,Z)、a(0)=2。
omega=−dV∧dZ/(tF_t)=g(V,Z)dlogV∧dlogZ、g(0)=1。三境界節点の小トーラスはMayer–Vietorisで向きを揃えて同一の原始radical生成元となる。二重Cauchy留数でPi_infty=(2pi i)²。
Hurwitzはomegaを保ち、radicalの符号は非零周期から+と決まるのでdelta_inftyを固定する。位相的原始性と積分は通常の証明、既存コードは留数係数1の検算。

## 11. conic匹配周期、Looijenga period、有理非分裂MHS

証明は `quantum_cubic_log_periods.tex`。d=u²−1、N=(u²+2Au+2h)d+B²+C²+2uBCと置く。v0=(B+uC)/d、w0=(C+uB)/dを引いてV=v−v0、T=w−w0とするとW−h=−(T²−2uVT+V²)/2−N/(2d)。s²=dを選びa=T−(u+s)V、b=T−(u−s)Vを取ればab=−N/d、omega=(du/s)∧dlog a。z=u+s、u=(z+z^-1)/2なのでomega=dlog z∧dlog a。
Nの二つの単純根u_-、u_+を結ぶ道が±1と他の根を避けるとき、fiber円が二端で縮むmatching球面の周期は2pi i[log(u+s)]_-^+。枝と道に沿う対数、向きを指定する。u=±1ではこの座標が特異なので無条件に延長しない。単純根間の全matchingが整数D4基底になるとはまだ証明していない。

A=B=C=0、h=-r²/2、0<r<1で原点へ消える実球面を
v=sqrt(r²−u²)cos(theta)/sqrt(1−u²)、w=uv+sqrt(r²−u²)sin(theta)、−r≤u≤r
と書く。omegaの引戻しはdu∧dtheta/sqrt(1−u²)。従って
**Pi0(h)=4pi asin sqrt(−2h)**。
原点Hessian−I、自己交叉−2の原始Morse球面。臨界値は0と−1/2のみ。
Pi0とPi_inftyは2h(1+2h)y''+(1+4h)y'=0の二解。基点を実区間に取り、0周回はPi0↦−Pi0、−1/2周回はPi0↦−Pi_infty−Pi0。解列(Pi_infty,Pi0)に行列[[1,0],[0,−1]]と[[1,0],[−1,−1]]が作用し、積は[[1,0],[−1,1]]。無限二面体像で、定数解に相補的な共通不変直線はない。**このrank2解局所系と全rank5ホモロジー局所系は区別する。** 係数hの解析接続と固定fiber Hurwitzも違う。

指数化P(gamma)=exp(integral_gamma omega/(2pi i))はdelta_inftyを足しても不変。Friedman Prop3.12に境界積分1のomega/(2pi i)²を用いると、向きを整合させてD^perp→Pic0(D)=C*という線束制限に一致する。matching値はz_+/z_-であり、根と平方根の有限選択被覆上で代数的。
零係数族ではQ=exp(Pi0/(2pi i))=(sqrt(1+2h)−i sqrt(−2h))²、
**Q+Q^-1=2+8h、h=(Q−1)²/(8Q)**。
両局所monodromyともQ↦Q^-1で、積の対数translationは指数化すると消える。SL2固有値/traceやChebyshevと同じ反転商構造だが、Qを元の表現固有値に同定したわけではない。

h=−1/10ではQ=(3−4i)/5、Q+Q^-1=6/5。根の1ならこの和は有理代数的整数なので整数となり矛盾。したがって非捩れ。
**点ごとの有理MHSも非分裂：** 0→Q(-1)^4→H²(U,Q)→Q(-2)→0が分裂すれば、F²の一次元直線を境界積分1に規格化した[omega]/(2pi i)²は有理classとなる。すると全整数cycleで規格化積分が有理、Qが根の1になるので上例は矛盾。局所系非分裂とこのMHS非分裂は別の結論。一つのQが捩れでも全四方向のMHSが分裂するとは結論できない。

次の計算では三conic pencilのmatchingを組み合わせ、全四内部periodを整数基底と対応させる。四根の差だけだとrank3に留まる可能性があり、±1を巡るcycleや別pencilの寄与を欠落させない。全rank5接続、一般パラメータの拡大類、非Archimedeanモデルは未構成。

## 12. 一次文献と確認範囲

- R. Friedman, *On the geometry of anticanonical pairs*, arXiv:1502.02560v2 (2016), https://arxiv.org/abs/1502.02560v2 、§3 Proposition3.12（pp.21–23）。指数化積分と線束制限period、MHS拡大との関係を本文と原PDF該当頁画像で確認。正規化は境界積分1である。本稿の新一般理論ではない。
- M. Gross, P. Hacking, S. Keel, *Moduli of surfaces with an anti-canonical cycle*, Compos. Math.151 (2015),265–291, DOI https://doi.org/10.1112/S0010437X14007611 ; arXiv:1211.6367v5。Definition1.5（代数的period）とTheorem1.8（他のmarking/nef条件を含むTorelli）、原PDF該当頁を確認。periodだけから無条件の全モジュライ同定を輸入しない。
- J. Lai, Y. Zhou, *Mirror symmetry for log Calabi–Yau surfaces II*, Compos. Math.161 (2025),2025–2090, DOI https://doi.org/10.1112/S0010437X25007080 ; arXiv:2201.12703。§2とTheorem1.8のmirror periodのモジュライ的同定を一次本文で確認。本文§1.2.3もHMSをこの定理から結論していない点に注意。本稿でmirror同値を構成したとはしない。
- S. Karwa, J. Lai, *Non-archimedean periods for log Calabi–Yau surfaces*, arXiv:2506.01651 (2025), https://arxiv.org/abs/2506.01651 、Introduction eqs.(1)–(2)、Theorem6.14。良い還元と組合せ型の仮定の下で非Archimedean periodが代数的periodに一致することを確認。本稿の曲面にモデルを選んで適用条件を検証したわけではない。
- P. Boalch, R. Paluba, *Symmetric cubic surfaces and G2 character varieties*, J. Algebraic Geom.25 (2016),607–631, DOI https://doi.org/10.1090/jag/668 ; arXiv:1305.6594。§4.1 base discriminant、§5式(19)・Corollary17、§7 Klein七点・Theorem20を既存原稿で一次本文確認。著者版 https://webusers.imj-prg.fr/~philip.boalch/files/g2.pdf 。以前のweb screenshotはcache miss、数式は既存厳密計算で照合。
- W. M. Goldman, W. D. Neumann, *Homological action of the modular group on some cubic moduli spaces*, Math. Res. Lett.12 (2005),575–591, DOI https://doi.org/10.4310/MRL.2005.v12.n4.a11 ; arXiv:math/0402039。Theorems1–2、Proposition3、§3のaffine D4・境界を既存入力として保持。今回の全独立再監査ではない。
- P. Deligne, *Théorie de Hodge : II*, Publ. Math. IHÉS40 (1971),5–57, DOI https://doi.org/10.1007/BF02684692、§3.2 Corollary3.2.13。重みのgraded piecesの入力。拡大分裂は仮定しない。
- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier59 (2009),2927–2978, DOI https://doi.org/10.5802/aif.2512、§1.5。Cayleyとmodular作用。arXiv:0711.1579v2は別題 *Holomorphic dynamics, Painlevé VI equation and character varieties*。
- M. Mikosz, A. Weber, *Triality, characteristic classes, D4 and G2 singularities*, J. Homotopy Relat. Struct.10 (2015),995–1011, DOI https://doi.org/10.1007/s40062-014-0094-3。IntroductionのMilnor格子、Proposition3、§5。
- K. Dixon, *The multi-moment maps of the nearly Kähler S3×S3*, Geom. Dedicata200 (2019),351–362, DOI https://doi.org/10.1007/s10711-018-0375-9、Lemma3.5。共通elliptopeの比較。圏的・計量的拡張は未構成。

一般理論は既知として扱い、個別の正規化・周期式・非分裂例の既出性の網羅確認は未了。

## 13. 再現と未実行事項

今回 `computations/verify_logarithmic_periods.py` を実行しPASS。Q上の恒等式と記号的平方根でconic留数、球面の引戻し、PF作用素、指数化の二次式、monodromy行列、非捩れ例の算術を確認。小証明書は `logarithmic_periods_certificate.json`。球面構成・積分・接続・Friedman比較・有理MHSの非分裂は通常の証明であり、有限計算と区別する。
新節のLuaLaTeX wrapper4頁を組版・全頁画像点検し、内部参照解決、overfullなしを確認。主論文全体の今回の組版、旧26検証器全再実行、全旧定理の独立査読、新規性の網羅調査は未実施。既存コード・小証明書は必要な依存資産として保持する。
GitHub mainへ保存し、push済み内容をLibraryへ重複保存しない。
