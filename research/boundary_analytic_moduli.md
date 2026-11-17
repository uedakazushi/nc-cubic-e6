# 境界の解析modulus・MF・二捩れ付き楕円曲線

2026-11-18 / e6-connections-v29。最初に `../00_research_plan.md` を読む。主論文の `papers/sections/quantum_cubic_boundary_thresholds.tex` と `quantum_cubic_boundary_moduli.tex` に証明を統合済み。二枝の元になる全反復・link・正規化は `research/boundary_pell_dynamics.md` と主論文 `sec:boundary-torus-links` を参照する。本ノートは現行知識をまとめ、論文の証明を重複しない。

## 1. 比較する対象と既存入力

滑らかなLG曲面U上のPell写像gと初期conic C0={v=kappa}を使う。kappa²≠1、N_v(kappa)≠0を仮定する。反復C_n=g^{-n}C0の閉包は一つの境界点p_wに二枝を持ち、互いに素のPuiseux対(b_n,c_n)、交叉b_n c_nを持つ。
実際の局所方程式をf_nk、重み付き主部をF_nkと区別する：

F_nk=y^(2b)−2kappa x^c y^b+x^(2c)、wt(x)=b、wt(y)=c。

rho±=kappa±sqrt(kappa²−1)は解消の例外曲線上の二交点。全germを主部へ解析的に置き換えない。local link、Milnor数、Newton閾値は主部から決まるが、Tjurina環や高次構造まで同じとは限らない。

## 2. Newton閾値と異なる反復の圏

前回未反映だった閾値の結果を現行主論文へ統合した。lct=(b+c)/(2bc)、減衰率log(3+2sqrt2)。0<tau<1の乗数イデアルは b(i+1)+c(j+1)>2bc tau の単項式で生成。これは境界Dを係数1で加えた対の閾値ではない。
実際のf_nkの二周期MF圏について、Dyckerhoff Cor6.5でHH even=Jac(f_nk)（代数として）、odd=0。次元はmu=(2b−1)(2c−1)、増大率2log Lambda。異なるnはHH次元でdg Morita非同値。
この圏は曲線閉包の境界特異点に付随するもので、Perf(U)、元の非可換H3圏、局所化の核と同一視していない。同じaffine曲線Gmから異なる境界圏が生じる。

## 3. 位相型が捨てるK=kappa²

単一の接線y=0と各枝のord(x)=b、ord(y)=cを使うと、同じ(b,c)型のgerm間の解析座標変換は最低重みでX=alpha x、Y=beta yとなる。cはbの倍数でないため、Yの重みc成分に純x項はない。従ってr_i=lim y^b/x^cは共通倍率を受け、二枝交換を許して

I=(r1+r2)²/(4r1r2)=kappa²

が不変。この必要条件は高重み項のある実germにも適用する。重み付き模型ではK一致は十分で、kappa↦−kappaはx↦zeta x、zeta^c=−1による右同値。
固定したU (A=B=C=0,h=1)とnで許容kappaを動かすと、同じaffine Gm、同じlink、同じ閾値で解析的に異なる無限個の境界を得る。実germの完全分類をKだけで行ったわけではない。

## 4. 重み付き模型のMFをHochschildの積で分類

Q_nk=MF(C[[x,y]],F_nk)の二周期dg Morita同値は、正確にn=mかつkappa²=(kappa')²である（`thm:weighted-boundary-Morita-classification`）。
HHの次元はnを決定し、代数としてのHHはJac(F)。重み付きEuler式によりJac=Tjurinaなので、Mather–Yauから接触同値、前節からK一致。十分性は明示的な右同値による。
同じnでlink T(2b,2c)、mu=tau、lct、HH次元が同じでも圏は連続に変わる。使うのはHHの**積**であり、次元だけではない。
安定化剰余体の通常Ext代数は二次項がないので二奇生成元の外積代数。しかし適合したminimal A-infinity模型のm_(b+c)(theta_x^c,theta_y^b)に±(-2kappa)が現れる（Dyckerhoff Thm5.9）。これは選んだ模型の係数で、A-infinity座標非依存の不変量を単独で与えるという主張ではない。MF分類の証明はHH環から行う。

## 5. 四点の楕円曲線とlevel 2

解消上の四点{0,infty,rho+,rho−}に二重被覆

E_k: eta²=z(z²−2kappa z+1)

を付随させ、O=infty、非零二捩れT=(0,0)を標識する。これは**四点配置から作った補助的な楕円曲線**であり、元の反標準楕円境界、Milnor fiberの商、MFの部分圏と同定していない。
K=kappa²が(O,T)付き同型類の完全不変量で、K∈A1\{1}は粗moduli Y0(2)の座標。Delta=64(K−1)、j=64(4K−3)³/(K−1)。J2=64(K−1)ならj=(J2+16)³/J2。
K=0と9/8はj1728が同じだがlevel2標識が異なり、同じnのMF模型も非同値。nを動かしてKを固定すれば付随楕円曲線は同じで、MFのHH次元だけが増える。

Tによる2isogenyはX=z−2kappa+z^-1、Y=eta(1−z^-2)、目標Y²=X(X²+4kappa X+4(K−1))。T平行移動は(z,eta)↦(z^-1,−eta/z²)。目標の(0,0)を標識して規格化するとK↦K/(K−1)、J2↦4096/J2。K4と4/3は2isogenousだがMF模型は非同値。これらは古典的な2捩れ商の公式の適用であり、新しい一般isogeny理論ではない。

## 6. 主部への置換を排除する実境界：mu27,tau24

A=B=C=0,h=1、初期v=2、n=1を選ぶ。曲面は滑らか、conic条件Nv=18。
p_wのchart x=U/W,y=V/W,t=T/WでP=2xy−t(x²+y²+1)−2t³。
r1=2uv−w、r2=2vr1−u、r3=2vr2−r1、Vg=2r2r3−v=g^*vとし、H=t^7(Vg(x/t,y/t,1/t)−2)。

F=Res_t(P,H)/(64x²y^5)

は局所被約曲線の単元倍。P_t(0)=−1、残り二根のH値は非零のためnormの他factorはunit。x²y^5はhomogenizationで残る境界固定成分。
先頭F20=4(y4−4x5 y2+x10)。先頭偏微分は重み18,15の正則列、filtered Koszulにより局所Jac随伴環は主部Jacでsocle重み26。従って重み>26を捨てる計算は近似でなく正確。Fは重み31まで必要（微分で最大5下がる）。
45単項式で偏微分倍の行列rank18、Fを加えたrank21。mu27,tau24。Jac基底はx^0..13、x^0..8 y、x^0..3 y²。

[F]=12x13−96x12/5−12x11/5、
[xF]=−96x13/5−12x12/5、[x²F]=−12x13/5、[x³F]=[yF]=0。

従って([F])の次元3。主部はEuler式からmu=tau27なので、実曲線は主部と接触非同値。
**注意：** 一般MFのHHはJacobian環で、Tjurinaは指定した[F]で割る。tau差だけから標識なし二周期MFの非同値を結論しない。Hua–Keller型復元や追加構造を用いるには、その入力がこの二周期圏に備わるかを確認する必要がある。未検証の復元定理を輸入しない。

## 7. 一次資料と適用箇所

- L. M. Câmara, *On the classification of quasi-homogeneous curves*, arXiv:1009.1664v1, https://arxiv.org/abs/1009.1664 。Theorem1(iii)、§4.3の非零根配置のC*商を一次本文で確認。今回の重み付き二枝分類はその具体例でもあり、実germへの必要条件を直接示した。
- J. N. Mather, S. S.-T. Yau, *Classification of isolated hypersurface singularities by their moduli algebras*, Invent. Math.69 (1982),243–251, DOI https://doi.org/10.1007/BF01399504 。原論文§1の定理を著者公開PDF https://homepages.math.uic.edu/~yau/35%20publications/Classification.pdf で確認。Tjurina環から同じ埋込み次元の孤立複素hypersurface germの接触型を復元する。一般のJacobian環だけに無条件適用しない。
- T. Dyckerhoff, *Compact generators in categories of matrix factorizations*, Duke Math. J.159 (2011),223–274, DOI https://doi.org/10.1215/00127094-1415869 ; arXiv:0904.4713v5。Corollary6.5と直前の乗法性を一次本文・該当頁画像で確認。Theorem5.9のminimal A-infinity模型も確認。Theorem6.6のhomology次元だけでなくHH cohomologyの代数構造を使う。
- J. Howald, *Multiplier Ideals of Sufficiently General Polynomials*, arXiv:math/0303203、Theorems11–12、Corollary13。Newton非退化の場合のtoric計算。実局所冪級数への適用は本文の明示ray計算で行う。

楕円曲線のj・二同種公式は本文で直接導出・記号検証し、未知の文献情報で補わない。各個別帰結の文献新規性の網羅調査は未了。

## 8. 次の着手と再現

最優先は実mu27,tau24例のJacobian環の積と指定類[F]をモデルと比較すること。n=1でkappaやhを動かす有限jetのTjurina跳躍を調べ、位相・Newton・解析・圏のどの段階に情報があるかを分離する。
並行してlevel2楕円modulusとの一致に、実際の対応やequivariant構造があるかを検討する。同じmoduli曲線というだけでHMSを主張しない。局所Weinsteinの対象とMF模型、filtered局所化を比較する際も実germと主部を分ける。
今回 `verify_boundary_thresholds.py` を再実行し、新しい `verify_boundary_analytic_moduli.py` も実行してPASS。前者は元のv28内容を現行へ統合し、後者はQとQ(sqrt2)上のEuler・Jacobian環・j/isogeny・resultant・厳密切断行列を再現する。証明書は同名のJSON。一般分類とstrictnessの理論は通常証明である。
新解析modulus節は独立LuaLaTeX wrapperで5頁に組版し、全頁画像・内部参照・overfullを点検した。全主論文の今回の組版、旧32検証器の全再実行、独立査読、新規性の網羅確認は未実施。GitHub mainへ統合し、push済み内容をLibraryに保存しない。
