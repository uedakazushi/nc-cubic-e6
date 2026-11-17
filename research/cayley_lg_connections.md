# Cayley・LG・消滅サイクル・G2・braidと周期

2026-11-17 / e6-connections-v21。再開時は `../00_research_plan.md` を先に読む。
完全な証明は主論文が読み込む `quantum_cubic_cayley_lg.tex`、`quantum_cubic_lg_picard.tex`、`quantum_cubic_g2_braids.tex`（すべて `../papers/sections/`）。本ノートは式・区別・文献・未解決の核心を現在の状態で整理し、論文の全文証明を重複させない。

## 1. 共通模型と係数の区別

一次元表現の正規化u=(1-q)x等、A=(1-q)a等から
Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。
W_{A,B,C}=H−Au−Bv−Cwの相対臨界スキームは有限平坦五重被覆、graph(dH)はT*A3内のexact Lagrangian。
一次元表現の総空間E=A3_{u,v,w}、係数底S=A3_{A,B,C}、量子代数の中心Y=Spec k[X,Y,Z,Omega]/Pを区別する。

W=hにp=-2u,r=-2v,s=-2wを入れるとFricke係数は(-4A,-4B,-4C,8h)。射影閉包はuvw−t(u²+v²+w²)/2−t²(Au+Bv+Cw)−ht³=0、無限遠の三角形に沿って常に滑らか。
量子Casimir切断Omega=-D0の中心を同じ等位面で読む際は、A=(D0a+ell_a)/(4e²)等、h=−(D0³−fD0²+D0K−L)/(8e³)、u=X/(2e)等という**別の底変更**を使う。A=(1-q)aと同一視しない。

## 2. Cayley・トーラス・Poisson

J=Hess H=[[-1,w,v],[w,-1,u],[v,u,-1]]、det J=R=u²+v²+w²+2uvw−1。ramification divisorはCayley曲面で、x=-2u等ならx²+y²+z²−xyz−4=0。
トーラス表示u=−(r+r^-1)/2、v=−(t+t^-1)/2、w=−(rt+(rt)^-1)/2は同時反転商(Gm)²/±、閉トーラスSL2粗指標多様体を与える。四A1点は±1三つ組で積−1。
{r,t}=rtから{u,v}=−R_w/2（巡回）。GL2(Z)単項式作用はPGL2(Z)として降り、det1はPoisson、det−1は反Poisson。分岐源上の括弧であり、量子代数の中心上のroot括弧9倍とは違う。Cayley modular作用がE→S全体へ延長するかは未構成。

## 3. D4 germとミニバーサル変形

Rの四節点sigma（±1、積−1）の像は−2sigma。fiberはsigmaの長さ4と−2sigmaの単純点1。
代表sigma=(-1,-1,-1)、底(2,2,2)でu=-1+x,v=-1+y,w=-1+ell−x−y、A=2+alpha等、L=ell−xy+gammaと置くと正確に
W=−L²/2−xy(x+y)+x²y²/2−gamma xy−(alpha−gamma)x−(beta−gamma)y
  +7/2+alpha+beta+gamma+gamma²/2。
局所Jacobi基底は1,x,y,xy、x²=y²=-2xy、x²y=xy²=0。三係数の非定数微分−x,−y,x+y−xyが独立なので加法定数を除くミニバーサル変形。別sheetのdet J=27。
巡回置換はHessian核で(x,y)↦(y,−x−y)。指定退化のMilnor/Picard比較は§6で構成済みだが、全域の標準分裂や圏同値ではない。

## 4. 留数代数と値衝突

係数原点の五sheetは0と四符号点eta（積+1）、全てetale。Hessian determinantは−1,4,4,4,4なのでtau(h)=−h(0)+(1/4)sum_eta h(eta)が非退化留数対を与える。基底1,u,v,w,uvwのGram determinantは−1。Frobenius代数であり、primitive form/Frobenius多様体は未構成。
Omega_E=f(uvw−u²−v²−w²)/3の原点fiber値は0と−2f/3（4回）、N5=D(D−2f/3)^4。被覆の分岐と観測値衝突は別。power basis=(任意基底)Tならdisc(power basis)=(det T)²disc(任意基底)。
Wの臨界値は−2uvw+(u²+v²+w²)/2でOmega_Eとは違う。LGのMaxwell locusとCasimir値衝突を無条件に同一視しない。

## 5. 実型・elliptope

正規化多項式は実型を持つがqが実になる意味ではない。C=−Hess Hの半正定値領域は3-elliptope。det C=−R、境界はR=0と[-1,1]³の交わりで、単位円トーラス商によるSU2 pillowcase。
内部は凸、Hessian負定値なのでPhiは単射。任意実係数で内部sheetは高々一つ。Dixonのnearly Kähler S3×S3のmulti-moment像と同じ凸体だが、追加の圏同値・計量退化は未構成。

## 6. Milnor–Picard整数比較とtriality

滑らかなU={W=h}の三次コンパクト化S、境界D=D1+D2+D3について
0→Z delta_infty→H2(U,Z)→K=<D_i>^perp→0、H1(U,Z)=0。
六点blow-upでD_i=L−E_(2i−1)−E_(2i)。E1,E3,E5の制限が次数ベクトルの基底なので全射。Kの基底alpha0=L−E1−E3−E5、alpha1=E1−E2、alpha2=E3−E4、alpha3=E5−E6のGramは負D4、det4。左端は原始radical、H2は自由rank5。
底(2,2,2)、h≈7/2の局所D4 Milnor fiber M_hの包含M_h→U_h→S_hはKへ入る。交叉保存と非退化性で単射、両rank4・det4なので指数1の整数格子同型。選択した退化に対してH2(U_h)=H2(M_h)⊕Z delta_infty。全域の選択非依存な標準分裂ではない。
rho=(u,v,w)↦(v,w,u)は境界三本を回す。境界格子BのGramはdiag−1/offdiag1、判別群の三非零元は(D1+D2)/2等。unimodular Picard gluingを介してK*/Kにも同じ作用。W(D4)は判別群へ自明なのでAut(D4)/W(D4)=S3への像はorder3の外部triality。局所とPicardで一致する。所在：`thm:lg-integral-picard-sequence`, `thm:lg-D4-Picard`, `cor:lg-picard-triality`。

## 7. affine D4・境界位相・混合Hodge

Goldman–Neumannの交叉形式は四外側o_iと中央cの負affine D4。primitive radical delta=o1+o2+o3+o4+2c。基底(c,o1,o2,o3,delta)はunimodularでD4(-1)⊕0に変換。Picardではc→alpha0、o1..3→alpha1..3、o4→−2alpha0−alpha1−alpha2−alpha3。
既存コード内の指定順反射積M=s_o1 s_o2 s_o3 s_o4 s_cはcharpoly=(xi−1)²(xi+1)³、M²−I=delta*(1,1,1,1,−2)、rank1かつsquare0。任意の消滅路で同じ行列という主張ではない。
無限遠はmonodromy−IのT² mapping torus、H1=Z⊕(Z/2)²。三次元mapping torusと二次元pillowcaseは別空間。
重みspectral sequenceでGr2 H²=Q(-1)^4、Gr3=0、Gr4=Q(-2)、E_c=1+4xy+(xy)²、Euler6。MHS拡大の分裂は未主張。境界周期は§10で明示したが内部四周期は未計算。

## 8. G2とD4/A2の共通退化

対称LG A=B=C=lambdaはb=-4lambda,c=8hの対称Fricke。Boalch–PalubaのG2底は
alpha=8h+2−12lambda、beta=64lambda³+48lambda²−96lambda h−12lambda−2。
最初の三monodromyを次元6のsemisimple G2共役類、第四を指定regular semisimple共役類に固定した指標多様体は三つの連結成分を持つ。LGは一成分。
regularの条件では二特異曲線lambda²+2lambda−2h−1=0、−16lambda³−3lambda²+12lambda h+4h²+2h=0と追加conic16lambda²−4lambda−8h−1=0を区別する。LGの滑らかさだけではregular条件を省略できない。
第四をregular unipotent閉包にするとalpha=beta=6、成分式(b+8)(b−1)²。二成分はD4の(b,c)=(-8,28), (lambda,h)=(2,7/2)とA2の(1,1),(-1/4,1/8)。A2点はu=v=w=1/2、Hessian rank2、対角上W=1/8+t³。他三臨界点(5/4,-1,-1)の順列の値は−23/32で同fiberにない。
これはBPの既知退化定理の本稿への適用で、G2量子代数やmirror同値を意味しない。係数fiberの重複度2と局所Milnor数2も異なる概念。

## 9. 成分交換とHurwitz：同じB3でも違う作用

新節 `sec:g2-braids-periods` で正確に分離した。
成分を選ぶ三次式chi(xi)=xi³+6xi²+3(1−alpha)xi+beta+2は、z=xi+2、P=alpha+3、Q=beta+6alpha+12でz³−3Pz+Q。A2 Cartanの商h/<(23)>→h/S3であり、label monodromy=S3、cusp complementの基本群=B3。
d=4P³−Q²の引戻しは−C0² S1、C0=b²+b−c−1、S1=b²−8b−4c−16。base map Jacobianは3C0。S1の一般点はbranch上にあるがそれ自身は非分岐の第三sheet。cusp(alpha,beta)=(-3,6)で(b,c)=(-2,1)、LG(lambda,h)=(1/2,1/8)は(1/2,-1,-1)の順列に三A1を持つ（Hessian determinant9/4）。(6,6)のD4側はC0=27で非分岐、A2側はC0=0。被覆の分岐型と曲面特異点型を区別する。

内部Hurwitzは
B1=(u,2uv−w−2lambda,v)、B2=(w,v,2vw−u−2lambda)。
右から合成しB1B2=(w,u,v)、B1B2B1=B2B1B2、(B1B2)³=1。体積・W・Jacobian Poisson・留数形式を保存する。b,cを固定するため三成分それぞれを保ち、PSL2Zを経由する。**底loopのB3と同一視しない。** 公式はBP(19)、G2同変性はCorollary17の適用。

u≠1でv*=w*=lambda/(u−1)へ平行移動すれば、B1はM_u=[[2u,-1],[1,0]]。
M_u^n=U_(n−1)(u)M_u−U_(n−2)(u)I、U_-1=0。全次数の証明はCayley–Hamilton、コードはn1..7を確認。u²≠1でu=(xi+xi^-1)/2、xiがn乗根なら一生成元のn回反復は恒等。二生成元の同時線型化ではない。

既知Klein軌道(lambda,h)=(1/4,0)、(b,c)=(-1,0)のFricke七点を
1=(0,0,0),2=(0,0,1),3=(0,1,0),4=(1,0,0),5=(1,1,0),6=(1,0,1),7=(0,1,1)
と並べる。二生成元はp=(1 3 7 2)(4 5 6)、q=(1 2 6 4)(3 7 5)。
q^-1 p q^-2 p q^-1 p³=(5 7)。推移的素数次数+互換でS7、全列挙も5040を確認。LG点は−1/2倍。
**群を区別：** S7（5040）は七つの表現同値類の置換像。BP Theorem20のG2(2)'≅U3(3)（6048）はFano直線・八元数から作る一つの表現の像。Klein群168も別物。七点軌道そのものは既知で、本稿のS7記述の新規性は未確認。
このG2底は(-1,-1)、chi=(xi+1)(xi²+5xi+1)、他二成分はQ(sqrt21)上。d=7、alpha²−4beta−12=−7なのでregular。別二成分に同じ軌道があるとは主張しない。

## 10. 境界周期の正規化と残る四方向

omega=Res(du∧dv∧dw/(W−h))=du∧dv/(uv−w−C)。projective u_hom=1 chartのF=VZ−t(1+V²+Z²)/2−t²(A+BV+CZ)−ht³で、F_t(0)=−1/2、t=VZ a(V,Z)、a(0)=2。
omega=−dV∧dZ/(tF_t)=g(V,Z)dlogV∧dlogZ、g(0)=1。
三角境界の節点を囲む小トーラスの類は、向きを揃えた三節点のMayer–Vietoris関係から同一の原始radical生成元delta_inftyとなる。二重Cauchy留数で
integral_delta omega=(2pi i)²。
Hurwitzはomegaを保ち、radicalの符号は非零周期で+と決まる。従ってdelta_inftyを固定しD4商へ作用する。
原始性と積分は本文の通常の位相・解析の証明で、コードは二重留数係数1だけを確認する。内部四周期・全Gauss–Manin系・MHS拡大分裂は未計算。内部の一局所cycleからconic pencilを利用してperiod微分と消滅点漸近を計算するのが次の具体的着手。

## 11. 一次文献と確認範囲

- P. Boalch, R. Paluba, *Symmetric cubic surfaces and G2 character varieties*, J. Algebraic Geom.25 (2016),607–631, DOI https://doi.org/10.1090/jag/668 ; arXiv:1305.6594。§4.1のbase discriminant、§5式(19)・Corollary17のHurwitz同変性、§7のKlein七点・Theorem20の6048表現像を今回原PDFの解析テキストで確認。著者版 https://webusers.imj-prg.fr/~philip.boalch/files/g2.pdf 。web screenshotはcache missで取得できず、数式は今回の厳密演算でも照合。定理の一般性・新規性を推測で拡張しない。
- W. M. Goldman, W. D. Neumann, *Homological action of the modular group on some cubic moduli spaces*, Math. Res. Lett.12 (2005),575–591, DOI https://doi.org/10.4310/MRL.2005.v12.n4.a11 ; arXiv:math/0402039。Theorems1–2、Proposition3、§3のaffine D4と境界plumbingを既存原稿の入力とする。今回の独立再監査ではない。
- P. Deligne, *Théorie de Hodge : II*, Publ. Math. IHÉS40 (1971),5–57, DOI https://doi.org/10.1007/BF02684692、§3.2 Corollary3.2.13。MHS graded piecesの既知入力。拡大分裂は使わない。
- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier59 (2009),2927–2978, DOI https://doi.org/10.5802/aif.2512、§1.5。Cayleyとmodular作用。arXiv:0711.1579v2は別題 *Holomorphic dynamics, Painlevé VI equation and character varieties*。
- M. Mikosz, A. Weber, *Triality, characteristic classes, D4 and G2 singularities*, J. Homotopy Relat. Struct.10 (2015),995–1011, DOI https://doi.org/10.1007/s40062-014-0094-3。IntroductionのMilnor格子、Proposition3、§5のD4変形・triality。
- K. Dixon, *The multi-moment maps of the nearly Kähler S3×S3*, Geom. Dedicata200 (2019),351–362, DOI https://doi.org/10.1007/s10711-018-0375-9、Lemma3.5。共通elliptopeの既知比較。圏的・計量的拡張は未構成。

これらの一般理論は既知として扱う。個別の正規化・格子比較・群作用の文献上の既出性の網羅確認は未了。

## 12. 再現と未実行事項

今回実行した `computations/verify_g2_braids_periods.py` はPASS。Q恒等式、七点置換群5040元、C0²S1、3A1、Chebyshev n1..7、境界二重留数を確認。小証明書は `g2_braids_periods_certificate.json`。位相・全次数漸化式・積分の証明とは区別する。
新節のLuaLaTeX wrapper4頁を組版・全頁画像点検し、内部参照とoverfullなしを確認。主論文全体の今回の組版、旧25検証器の全再実行、旧定理の独立査読、新規性の網羅調査は未実施。以前の `verify_lg_picard_g2.py` と `verify_cayley_lg_connections.py` および小証明書は現行の依存資産として保持する。
GitHub mainに保存し、push済み内容をLibraryへ重複保存しない。
