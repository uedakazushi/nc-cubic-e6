# 境界の解析modulus・MF・楕円曲線・Milnor被覆のPrym

2026-11-18 / e6-connections-v30。最初に `../00_research_plan.md` を読む。完全な証明は主論文の `quantum_cubic_boundary_thresholds.tex`, `quantum_cubic_boundary_moduli.tex`, `quantum_cubic_boundary_prym.tex`。元の全反復・link・正規化は `research/boundary_pell_dynamics.md` と `sec:boundary-torus-links` にある。本ノートは現行の具体式・区別・文献・次の着手を保持する。

## 1. 実germと重み付き模型

滑らかなLG曲面U、Pell写像g、初期conic C0={v=kappa}を使う。kappa²≠1、N_v(kappa)≠0。C_n=g^{-n}C0の閉包は一つの境界点に二枝、Puiseux対(b_n,c_n)、相互交叉b_nc_nを持つ。bは偶数、cは奇数で互いに素。
実際の局所方程式f_nkと重み付き主部F_nkを区別する：F_nk=y^(2b)−2kappa x^c y^b+x^(2c)、wt(x)=b、wt(y)=c。rho±=kappa±sqrt(kappa²−1)は解消例外曲線上の二交点。
全germを主部へ解析的に置き換えない。link・Milnor数・Newton閾値は主部から決まるが、Tjurina環や高次構造は同じとは限らない。

## 2. 閾値と異なる反復の圏

lct=(b+c)/(2bc)、減衰率log Lambda。0<tau<1の乗数イデアルは b(i+1)+c(j+1)>2bc tau の単項式で生成。これは境界Dに係数1を加えた対の閾値ではない。
実f_nkの二周期MFについて、Dyckerhoff Cor6.5でHH even=Jac(f_nk)（代数として）、odd=0。mu=(2b−1)(2c−1)、増大率2log Lambda。異なるnはHH次元でdg Morita非同値。この圏をPerf(U)、非可換H3圏、局所化の核と同一視していない。

## 3. 位相型が忘れるK=kappa²

単一接線y=0と枝のord(x)=b、ord(y)=cより、解析座標変換は最低重みでX=alpha x、Y=beta yとなる。bがcを割らないので重みcの純x項はない。r_i=lim y^b/x^cは共通倍率だけを受け、二枝交換を許してI=(r1+r2)²/(4r1r2)=kappa²が不変。これは高重み項のある実germにも適用する必要条件。
重み付き模型ならK一致は十分で、符号kappa↦−kappaはx↦zeta x、zeta^c=−1による右同値。固定U(A=B=C=0,h=1)とnで許容kappaを動かすと、同じaffine Gm・link・閾値で解析的に異なる無限個の境界を得る。実germの完全分類をKだけで行ったわけではない。

## 4. 模型MFをHochschildの積で分類する

Q_nk=MF(C[[x,y]],F_nk)の二周期dg Morita分類はnとK一致と同値（`thm:weighted-boundary-Morita-classification`）。HHの次元がnを決め、代数としてのHHはJac(F)。Euler式によりJac=TjurinaなのでMather–Yauが接触型を復元し、Kが一致する。十分性は右同値。一般の高重みgermではEuler式を使えない。
固定nでlink、mu=tau、lct、HH次元が同じでも連続な圏的modulusがある。安定化剰余体の通常Ext代数は二奇生成元の外積代数だが、適合minimal A-infinity模型ではm_(b+c)(theta_x^c,theta_y^b)=±(-2kappa)（Dyckerhoff Thm5.9）。これは模型に依存した係数であり、単独の座標非依存不変量としない。

## 5. 四点の二捩れ楕円曲線

解消上の四点{0,infty,rho+,rho−}からE_k:eta²=z(z²−2kappa z+1)、O=infty、T=(0,0)を作る。Kは(O,T)付き同型類の完全不変量で、K∈A1\{1}は粗moduli Y0(2)。Delta=64(K−1)、j=64(4K−3)³/(K−1)、J2=64(K−1)ならj=(J2+16)³/J2。
K=0と9/8はj1728が同じでもlevel2標識とMF模型が異なる。nを動かしてKを固定すればEは同じだがMFのHH次元は増える。
Tによる2isogenyはX=z−2kappa+z^-1、Y=eta(1−z^-2)、目標Y²=X(X²+4kappa X+4(K−1))。T平行移動は(z,eta)↦(z^-1,−eta/z²)、目標の(0,0)を標識するとK↦K/(K−1)、J2↦4096/J2。K4と4/3はisogenousだがMF模型は非同値。
これは元の反標準楕円境界やMF部分圏の同定ではない。**Milnor曲線との具体的関係は§7のKummer被覆を介して構成した。** 元のMilnor曲線から指定zを保つ写像はむしろ障害を持つ。

## 6. 実境界のmu27,tau24と整数次数付きdg復元

A=B=C=0,h=1、初期v=2、n=1。曲面は滑らか、conic条件Nv=18。
p_wのchartでP=2xy−t(x²+y²+1)−2t³。r1=2uv−w、r2=2vr1−u、r3=2vr2−r1、Vg=2r2r3−v=g^*v、H=t^7(Vg(x/t,y/t,1/t)−2)と置く。
F=Res_t(P,H)/(64x²y^5)は局所被約方程式の単元倍。P_t(0)=−1、他二根でHは非零なのでnormの他factorは単元、x²y^5は境界固定成分。
先頭F20=4(y4−4x5y2+x10)。初期偏微分は重み18,15の正則列なので、filtered KoszulによりJacのsocle重み26。Fの重み31jetで偏微分後の計算に十分。45単項式の偏微分行列rank18、Fを加えたrank21、mu27,tau24。
Jac基底はx^0..13、x^0..8y、x^0..3y²。
[F]=12x13−96x12/5−12x11/5、[xF]=−96x13/5−12x12/5、[x²F]=−12x13/5、[x³F]=[yF]=0。([F])は次元3。主部mu=tau27なので接触非同値。

**現在確定した圏的帰結：** Hua–Keller最終版Thm5.9の通常のZ-graded dg特異点圏S_fについて、絶対HH^0(S_f)=Tjur(f)。従ってこの実境界と主部はHH0次元24対27によりdg Morita非同値。異なるKの実germも、Tjurina復元と前節の解析的不変量により、この整数次数付き圏が区別する。
二周期MFの相対HH=Jacと絶対Zdg HH0=Tjurを入れ替えない。periodizationや基礎環忘却の全比較は未構成で、一般strict二周期MFの分類をtauだけで結論したわけではない。3fold flop/NCCRの存在を仮定するHua–Kellerの後続定理は使っていない。

## 7. Milnor二次被覆のPrymにE_kを実現する

CはF_nk=1の滑らかな射影模型。z=y^b/x^c、Q=z²−2kappa z+1。x^(2c)Q=1。
bp+cq0=1を選びt=x^p y^q0と置くとx=t^b z^-q0、y=t^c z^p、t^(2bc)=z^(2cq0)/Q。Q二根で単純極なので連結次数2bc。z=0,infty,rho±上の点数2c,2b,1,1からg(C)=2bc−b−c。
xはx=0,y^(2b)=1の2b点で単純零点、二無限遠点で極位数b。
Eへの持上げに必要な平方はzQ=y^b/x^(3c)=x*(y^(b/2)/x^((3c+1)/2))²。xは非平方なので**同じzを引き戻すC→Eはない**。任意の別の楕円写像の不存在ではない。

a²=xを加えたtildeCでは
q:(a,y)↦(z=y^b/a^(2c),eta=y^(b/2)/a^(3c))
が次数2bcの有限写像。pi:tildeC→Cは2b点で分岐、無限遠はb偶数なので非分岐。
g(tildeC)=4bc−b−2c−1、Prym次元2bc−c−1。deck delta(a,y)=(-a,y)はEの[-1]に対応し、q*EはPrymに入る。q_*q^*=[2bc]、e=q^*q_*/(2bc)は有理冪等射。Eはisogeny因子、H1(E,Q)は反不変H1の有理Hodge直和因子。整数・偏極付き積分解は未主張。

## 8. 共通Ciani四次と可変楕円周期

全nで共通のgenus3 Ciani曲線Ck:X4+Y4−2kappa X²Y²=Z4へ、(X,Y)=(a^c,y^(b/2))という次数bc/2の写像がある。alpha(X,Y)=(-X,Y)、beta(X,Y)=(X,-Y)の三商は
alpha商 q²=1+(K−1)Y4、beta商 q²=1+(K−1)X4（両j1728）、
alpha beta商 Dk:T²=r4−2kappa r²+1（r=Y/X,T=1/X²）。
三つの非自明指標のHodge成分が各1次元なのでJac(Ck)~Ei²×Dk。delta↔alphaの等変性からPrym(tildeC/C)にEi×Dkにisogenousな二次元部分が入る。
Dk→Ekは(z,eta)=(r²,rT)の非分岐次数2、deck(r,T)↦(-r,-T)。原点を適合させれば2isogenyで、j(Dk)=64(K+3)³/(K−1)²=j(E_{K/(K−1)})。既存のlevel2対応が共通genus3曲線を通る商として実現された。
n1ではgC13、gtilde27、Prym14、Cianiへの次数5、Eへの次数20。

Eのomega=dz/etaの周期Piは(kappa²−1)Pi''+2kappa Pi'+Pi/4=0。P=zQとして、作用素をomegaに作用させるとd_z[z²(1−z²)/(2P^(3/2))]。従ってこれは完全微分から得る厳密PF式。q=(1−kappa)/2でGauss(1/2,1/2;1)。pullback/traceがGauss–Maninに適合しPrymのrank2部分にも同じ式。
これはkappaという解析modulusの変動であり、固定kappaのMilnor値monodromyや元のLG level hのarcsine方程式とは違う。高重み実germへこのPrym構成が解析的に残るとは未証明。

## 9. 一次文献と確認箇所

- L. M. Câmara, *On the classification of quasi-homogeneous curves*, arXiv:1009.1664v1, https://arxiv.org/abs/1009.1664 。Theorem1(iii)、§4.3の非零根配置のC*商。重み付き二枝分類の既知一般論と実germへの必要条件を分ける。
- J. N. Mather, S. S.-T. Yau, *Classification of isolated hypersurface singularities by their moduli algebras*, Invent. Math.69(1982),243–251, DOI https://doi.org/10.1007/BF01399504 。§1の定理を著者公開PDFで確認。Tjurina環から同じ埋込み次元の接触型を復元し、一般Jacobian環だけに適用しない。
- T. Dyckerhoff, *Compact generators in categories of matrix factorizations*, Duke Math. J.159(2011),223–274, DOI https://doi.org/10.1215/00127094-1415869 ; arXiv:0904.4713v5。Cor6.5のcohomology代数とThm5.9のminimal A-infinity模型。homology次元公式だけを使っていない。
- J. Howald, *Multiplier Ideals of Sufficiently General Polynomials*, arXiv:math/0303203、Thms11–12、Cor13。局所適用は本稿の明示toric ray計算。
- D. Mumford, *Prym Varieties I*, in *Contributions to Analysis*, Academic Press(1974),325–350。§§1–3、特に印刷頁331のP=ker(1+delta)^0、norm/pullback。著者PDF https://www.dam.brown.edu/people/mumford/alg_geom/papers/1974a--PrymVar-I-NC.pdf の該当頁画像を確認。
- E. W. Howe, F. Leprévost, B. Poonen, *Large torsion subgroups of split Jacobians of curves of genus two or three*, Forum Math.12(2000),315–364; arXiv:math/9809210。§4.1のgenus3三楕円分解を著者PDF https://math.mit.edu/~poonen/papers/large.pdf と該当頁画像で確認。本稿の三商は直接式を示す。
- Z. Hua, B. Keller, *Cluster categories and rational curves*, Geom. Topol.28(2024),2569–2634, DOI https://doi.org/10.2140/gt.2024.28.2569 ; https://arxiv.org/abs/1810.00749v6 。最終preprint Thm5.9、pp36–37を本文と頁画像で確認。一般孤立超曲面の通常Zdg enhancementの絶対HH0をTjurina環と同定する。後続のflop/NCCR定理とは仮定が異なる。

一般Prym理論、Ciani分解、超幾何、dg復元は既知。本稿の位置付けは明示写像と入力例の接続。個別帰結の網羅的な新規性調査は未了。

## 10. 次の着手と検証状態

実germについてはZdg圏の区別が解決したので、相対二周期HHと絶対Zdg HHの比較、[f]の役割、n1でのkappa/h変動のTjurina跳躍を調べる。未確認の比較を結論に使わない。
Prym側はb2,c5でq*のkernel・誘導偏極・整数格子を計算し、PFのmonodromyをlevel2標識と比較する。高重みの変形で楕円factorが残るか、stable reduction/極限Hodgeにのみ残るかを別問題にする。同じ有理Hodge因子からMF部分圏/HMSを推論しない。
今回 `verify_boundary_prym.py` を実行しPASS。Q上の代入・j・指標・完全微分とPell整数式、元Vietaから独立のmu27/tau24計算を含む。証明書は `boundary_prym_certificate.json`。全nの幾何、norm理論、dg復元は通常の証明と文献入力。
新Prym節は独立LuaLaTeX4頁、全頁画像・内部参照・overfullなしを確認。主論文全体の今回の組版、旧34検証器全再実行、独立査読、新規性の網羅確認は未実施。mainへの統合差分で既存証明・文献を保持。pushした内容はLibraryへ保存しない。
