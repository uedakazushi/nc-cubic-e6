# Cayley・LG・消滅サイクル・G2の接続

2026-11-17 / e6-connections-v20。再開時は `../00_research_plan.md` を先に読む。
完全な証明は主論文中の `../papers/sections/quantum_cubic_cayley_lg.tex` と `../papers/sections/quantum_cubic_lg_picard.tex`。本ノートは現在必要な式・区別・文献・次の着手をまとめ、全文証明を重複させない。

## 1. 共通模型と空間・係数の区別

正規化u=(1-q)x等、A=(1-q)a等により、一次元表現の係数写像は
Phi=(vw-u,wu-v,uv-w)=grad H、H=uvw−(u²+v²+w²)/2。
W_{A,B,C}=H−Au−Bv−Cwの相対臨界スキームはこの有限平坦五重被覆。graph(dH)はT*A3内のexact Lagrangianである。
一次元表現の総空間E=A3_{u,v,w}、係数底S=A3_{A,B,C}、元の量子代数の中心Y=Spec k[X,Y,Z,Omega]/Pは異なる。u,v,wは中心生成元ではなく、A,B,CはFricke係数でもない。

**LG等位面との明示的比較：** W=hにp=-2u,r=-2v,s=-2wを入れるとFricke係数は(-4A,-4B,-4C,8h)。射影閉包はuvw−t(u²+v²+w²)/2−t²(Au+Bv+Cw)−ht³=0、無限遠は常に滑らかな三角境界。
元の量子Casimir切断Omega=-D0の中心をこの等位面として読む際は、A=(D0a+ell_a)/(4e²)等、h=−(D0³−fD0²+D0K−L)/(8e³)、u=X/(2e)等という**別の底変更**を使う。A=(1-q)aと同一視しない。

## 2. Cayleyの出現とPoisson構造

Hessian J=[[-1,w,v],[w,-1,u],[v,u,-1]]、det J=R=u²+v²+w²+2uvw−1。ramification divisor R=0はCayley三次曲面。変数x=-2u等でx²+y²+z²−xyz−4=0となる。
トーラス表示はu=−(r+r^-1)/2、v=−(t+t^-1)/2、w=−(rt+(rt)^-1)/2。同時反転商(Gm)²/±、閉トーラスSL2粗指標多様体となる。四A1点はu,v,w=±1、積−1。
{r,t}=rtから{u,v}=−R_w/2（巡回）。GL2(Z)単項式作用はPGL2(Z)として降り、det1でPoisson、det−1で反Poisson。これは**分岐源**上の構造であり、元の量子代数の**中心**上のroot-of-unity括弧9倍とは違う。
Cayleyのmodular作用が五重被覆E→S全体と底の作用へ延びるかは未構成。

## 3. D4の局所変形とtriality

Rの四節点sigma（±1、積−1）の像は−2sigma。fiberはsigma上の長さ4と−2sigma上の単純点1に分かれる。
代表sigma=(-1,-1,-1)、底(2,2,2)でu=-1+x,v=-1+y,w=-1+ell-x-y、A=2+alpha等、L=ell-xy+gammaとすると

W=−L²/2−xy(x+y)+x²y²/2−gamma xy−(alpha−gamma)x−(beta−gamma)y
  +7/2+alpha+beta+gamma+gamma²/2。

二変数g=-xy(x+y)+x²y²/2はD4 germ。局所Jacobi基底1,x,y,xy、x²=y²=-2xy、x²y=xy²=0。三係数の非定数微分−x,−y,x+y−xyが独立なので加法定数を除くミニバーサル変形。別sheetのdet J=27。
巡回置換はHessian核で(x,y)↦(y,−x−y)となり三枝を回す。
**指定した退化におけるPicard格子との幾何学的同定は§6で構成済み。** 全域で選択非依存な標準同定や非可換圏の同値は主張しない。

## 4. 留数対と二種類の判別式

係数原点では五sheetは0と四符号点eta（積+1）、全てetale。Hessian determinantは−1,4,4,4,4。
tau(h)=−h(0)+(1/4)sum_eta h(eta)は非退化留数対を定め、基底1,u,v,w,uvwのGram determinantは−1。これはFrobenius代数であって、primitive form/Frobenius多様体の構成ではない。
同じ原点でOmega_E=f(uvw−u²−v²−w²)/3は0と−2f/3（4回）を取り、N5=D(D−2f/3)^4。したがって値の衝突は被覆の分岐と異なる。
一般にpower basis=(任意基底)Tならdisc(power basis)=(det T)²disc(任意基底)。観測量がsheetを区別しなくなる因子が追加される。
Wの臨界値は−2uvw+(u²+v²+w²)/2で、Omega_Eとは異なる。LG Maxwell locusをCasimir値衝突と同一視しない。

## 5. 実型とelliptope

正規化した実多項式を考える。q自身が実であるという意味ではない。
C=-Hess H=[[1,-w,-v],[-w,1,-u],[-v,-u,1]]の半正定値領域は3-elliptope。det C=-R、その境界はR=0と[-1,1]³の交わり。単位円トーラス表示でSU2トーラスcharacter varietyのpillowcaseとなる。
内部は凸でHessianが負定値だから、線分積分によりPhiは単射。任意の実係数に対し内部sheetは高々一つ。
Dixonは同じelliptopeをnearly Kähler S3×S3のmulti-moment像と同定する。共通凸体の同定を超えた圏同値・計量退化・同一fibrationは未構成。

## 6. MilnorとPicardを結ぶ整数写像

U={W=h}が滑らかでSを射影閉包、D=D1+D2+D3を境界とする。
対(S,D)のcohomology完全列、Poincaré双対性、Pic(S)=H²(S,Z)から

0 → Z delta_infty → H2(U,Z) → K=<D1,D2,D3>^perp → 0、H1(U,Z)=0。

六点blow-upのD_i=L−E_(2i−1)−E_(2i)ではE1,E3,E5の制限が次数ベクトルの標準基底なので全射。Kの基底alpha0=L−E1−E3−E5, alpha1=E1−E2, alpha2=E3−E4, alpha3=E5−E6のGramは負D4、det4。左端は原始radical、H2(U)は自由rank5。
(A,B,C)=(2,2,2)、h≈7/2の局所D4 Milnor fiber M_hについて、包含M_h→U_h→S_hのH2写像はKへ入る。交叉保存と非退化性で単射、両rank4・det4なので指数1、**整数格子同型**となる。これにより指定した退化でH2(U_h)=H2(M_h)⊕Z delta_infty。抽象的な同型の存在でなく実際の包含で得た比較。ただし退化・Milnor近傍の選択を外した標準分裂ではない。

rho=(u,v,w)↦(v,w,u)は不変Milnor球を保ち、境界三本を回す。境界格子BのGramはdiag−1/offdiag1で、B*/B=(Z/2)²の三非零元は(D1+D2)/2等。rhoがこれらを巡回し、unimodular Picard gluingからK*/Kにも同じ作用。W(D4)は判別群へ自明なので、rhoのAut(D4)/W(D4)=S3への像はorder3、すなわち**外部triality**。局所MilnorとPicardで一致する。
証明箇所：`thm:lg-integral-picard-sequence`, `thm:lg-D4-Picard`, `cor:lg-picard-triality`。

## 7. affine D4・境界・混合Hodge

Goldman–Neumannの交叉行列は四外側o_iと中央cからなる負affine D4。primitive radicalはdelta=o1+o2+o3+o4+2c。基底(c,o1,o2,o3,delta)はunimodularでD4(-1)⊕0へ直す。Picard表示ではc→alpha0、o1..3→alpha1..3、o4→−2alpha0−alpha1−alpha2−alpha3。
コード内の指定順序の反射積M=s_o1 s_o2 s_o3 s_o4 s_cはcharpoly=(xi−1)²(xi+1)³、M²−I=delta*(1,1,1,1,−2)、rank1かつsquare0。この行列計算を任意の消滅路で同じ行列になるという主張にしない。原稿ではaffine格子と境界を主に用いる。
無限遠はmonodromy−IのT² mapping torusでH1=Z⊕(Z/2)²。pillowcaseに同じ−Iが現れるが、三次元mapping torusと二次元quotientは別空間。
Deligne weight spectral sequenceでGr2 H²(U)=Q(-1)^4、Gr3=0、Gr4=Q(-2)。E_c=1+4xy+(xy)²、Euler6。MHSの拡大の分裂は未主張。次はlog2形式のperiodと拡大類を調べる。証明：`prop:lg-mixed-hodge`。

## 8. 同じG2退化に現れるD4とA2

Boalch–Palubaの対称Fricke族はb=-4lambda,c=8hとして本稿のA=B=C=lambdaのLG族に一致する。G2底不変量は
alpha=8h+2−12lambda、beta=64lambda³+48lambda²−96lambda h−12lambda−2。
最初の三monodromyを次元6のsemisimple G2共役類、第四を指定regular semisimple共役類に固定した四穴球面G2指標多様体は**三つの連結成分**を持ち、それぞれが一つのsmooth symmetric Fricke。LG等位面は一成分であり全体ではない。
regularの範囲では、対称三次の二特異条件lambda²+2lambda−2h−1=0、−16lambda³−3lambda²+12lambda h+4h²+2h=0と、追加conic16lambda²−4lambda−8h−1=0を区別する。単にLG fiberが滑らかというだけでG2 regular semisimple条件を省略しない。

第四をregular unipotent共役類の閉包にするとalpha=beta=6。
底のb方程式は(b+8)(b−1)²で、二成分は
D4: (b,c)=(-8,28) ↔ (lambda,h)=(2,7/2)、
A2: (b,c)=(1,1) ↔ (lambda,h)=(-1/4,1/8)。
前者は今回の四sheet衝突。後者は以前S5被覆の互換を検出したsimple foldの係数である。後者の点u=v=w=1/2ではHessian rank2、対角上W=1/8+t³だから曲面特異点はA2。他の三臨界点(5/4,-1,-1)の順列の値−23/32はこのfiberとは違う。
**同じ例外群の退化が、もともと別々に現れたD4衝突とA2衝突をまとめる。** これはBoalch–Palubaの既知の成分定理の本稿への適用であり、G2型量子代数との同型やmirror同値を意味しない。係数fiber重複度2とMilnor数2も異なる概念。

## 9. 一次文献と確認範囲

- W. M. Goldman, W. D. Neumann, *Homological action of the modular group on some cubic moduli spaces*, Math. Res. Lett. 12 (2005), 575–591, DOI https://doi.org/10.4310/MRL.2005.v12.n4.a11 ; arXiv:math/0402039。Theorems1–2、Proposition3、§3の交叉行列・境界を著者PDFで確認。PDF screenshotは取得エラーで未確認だが、本文数式と今回の整数行列計算を照合した。
- P. Deligne, *Théorie de Hodge : II*, Publ. Math. IHÉS 40 (1971), 5–57, DOI https://doi.org/10.1007/BF02684692 。§3.2、Corollary3.2.13のspectral sequence、原PDFの該当頁画像を確認。
- P. Boalch, R. Paluba, *Symmetric cubic surfaces and G2 character varieties*, J. Algebraic Geom. 25 (2016), 607–631, DOI https://doi.org/10.1090/jag/668 ; arXiv:1305.6594v2。§4、Corollary11（3成分）、Remark12（alpha=beta=6のD4と二重成分）、§6（triality）を原論文本文で確認。web screenshotはキャッシュ取得エラー。作用の完全な比較・量子化の対応は未了。
- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier59 (2009), 2927–2978, DOI https://doi.org/10.5802/aif.2512、§1.5。Cayley商とmodular作用の既知結果。arXiv:0711.1579v2は別題 *Holomorphic dynamics, Painlevé VI equation and character varieties*。
- M. Mikosz, A. Weber, *Triality, characteristic classes, D4 and G2 singularities*, J. Homotopy Relat. Struct.10 (2015), 995–1011, DOI https://doi.org/10.1007/s40062-014-0094-3 。IntroductionのD4 Milnor交叉形式、Proposition3、§5のminiversal変形・trialityを確認。ADEの標準Milnor格子を本稿で再証明したとはしない。
- K. Dixon, *The multi-moment maps of the nearly Kähler S3×S3*, Geom. Dedicata200 (2019), 351–362, DOI https://doi.org/10.1007/s10711-018-0375-9、Lemma3.5。共通elliptopeの既知比較。追加の圏的対応は未構成。

各一般理論は既知として扱う。今回の個別適用・格子比較の網羅的な新規性調査は未完了。

## 10. 再現と次の着手

`computations/verify_lg_picard_g2.py` を実行してPASS。Q上の恒等式と整数格子、G2の二特異値を確認。証明書は `lg_picard_g2_certificate.json`。有限行列の計算と、位相完全列・ADE入力・Hodge理論・G2定理は別の状態。
新節をLuaLaTeX wrapperで4頁に組版・画像点検し、overfullを修正。主論文全体の今回の再組版、旧24検証器の全再実行、旧定理の独立査読は未実施。
次の具体課題はG2のbraid式と局所/Picard作用の比較、三成分交換のmonodromy、境界radicalのlog2形式period、混合Hodge拡大、局所D4の圏的比較。既知の古典同型だけから量子代数やFukaya圏の同値を主張しない。
GitHub mainを正本に保存し、push済み内容をLibraryへ重複保存しない。
