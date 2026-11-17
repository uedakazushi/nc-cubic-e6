# conic標識・D4周期・triality・三成分のHodge構造

2026-11-17 / e6-connections-v24。再開時は `../00_research_plan.md` を先に読む。
完全な証明は主論文が直接読む `../papers/sections/quantum_cubic_four_periods.tex` と `quantum_cubic_triality_isogeny.tex`。積分は `quantum_cubic_log_periods.tex`、位相は `quantum_cubic_lg_picard.tex`。本ノートは現在必要な式、適用範囲、障害、先行研究を整理する。全rank五の代数的接続行列の構成や旧非可換分類の独立再監査とは区別する。

## 1. 一般conic標識と全四周期

W=uvw−(u²+v²+w²)/2−Au−Bv−Cw、U={W=h}、omega=du∧dv/(uv−w−C)、境界周期=(2pi i)²。
N(u)=(u²+2Au+2h)(u²−1)+B²+C²+2uBC。
一般chartはDisc N≠0, B²−C²≠0。全smooth locusの必要条件ではなく、対称B=Cにはそのまま適用しない（§4で別に扱う）。

D1={u_hom=t=0}はconic pencilの二重切断。四有限根と無限遠D2+D3が特異fiber。D1,D2に交わらずD3に交わるline section sを取り、各fiberのsと交わらない成分E1..E4、E5=D2を縮約してF1を得る。
Picard基底s,F,E1..E5でs²=-1,sF=1,F²=0,Ei²=-1。他は0。
D1=2s+2F−ΣEi、D2=E5、D3=F−E5。
四平方根の符号を独立自由と仮定せず、compatible成分選択から来る標識を使う。

K=D^perp={bF+Σ_(i=1)^4 ciEi:2b+Σci=0}はeven-sum Z4、形式−Σci²。
整数基底alpha=(E1−E2,E2−E3,E3−E4,E3+E4−F)。Gram負D4、det4。
D1のz=w/vに対しEiの交点ziはzi+zi^-1=2ui。一般fiberの二交点のz積は1。
境界gluingから
P(alpha)=(z1/z2,z2/z3,z3/z4,z3*z4)。
Friedmanの比較によりP=exp(integral omega/(2pi i))。alphaの整数持上げgammaと原始delta_inftyがH2の基底、内部周期は2pi i log P modulo (2pi i)²Z。
指数行列det2、kernel共通±1。係数→quartic係数のJacobian16(C²−B²)。Disc N=prod_(i<j)(zi−zj)²(zi*zj−1)²/[2^12(prod zi)^6]。有限標識被覆上で四periodは局所座標になる（`thm:four-integer-D4-periods`, `cor:conic-period-torus`）。

## 2. 円分性とHodge分裂

一般chartで有理MHS分裂⇔全P(alpha_i)がroots of unity⇔全ziがroots of unity。
F²を境界periodで正規化した線が有理であることと、整数基底上の全評価が有理であることを用いる。HodgeのF¹は全空間なので、その有理線は商Q(-2)へのsectionを与える。
有理分裂と整数拡大の自明性は別。root-of-unity period、量子化パラメータq³=1、有限braid軌道も別条件。

Q上の分裂例(A,B,C,h)=(1/4,1/2,1/4,1/8)：N=(2u+1)(8u³−6u+1)/16、16z⁴N((z+z^-1)/2)=(z⁹−1)/(z−1)。全ziは9乗根、Nはsquare-free、N(1)=9/16,N(-1)=1/16。
Q上の非分裂例(-65/16,75/16,-65/16,3575/288)：N=(u−5/4)(u−5/3)(u−17/8)(u−37/12)。ziは2,3,4,6またはその逆数で非捩れ。捩れ性は成分逆転に不変なので、特定符号組を無断でcompatibleと同定する必要はない。
証明は `thm:four-period-rational-split`, `prop:rational-cyclotomic-examples`。

## 3. Hurwitzの有限ホモロジー像と指数3

Goldman–Neumann Theorems1–2、§2を適用すると、対称LG族のH2をaffine D4（外側o1..4、中央c）で標識でき、B1は(o2 o3)、B2は(o1 o3)、o4,cは固定。符号は+で、像S3、pure braidはH2で自明。lambda=0の臨界点をo1=(1,-1,-1),o2=(-1,1,-1),o3=(-1,-1,1),o4=(1,1,1),c=0と取ると公式からこの置換が分かる。smooth symmetric baseで平行移動する。
radicalはdelta=o1+o2+o3+o4+2c。商Kの整数基底c,o1,o2,o3について、omegaを保存する固定fiber作用から三外側periodが等しい。中央xi、外側etaと置く。

sigma=(o1 o2 o3)ならK^sigma=Zc⊕Zs(s=Σoi)、K_sigma=Zcbar⊕Zobar。自然写像diag(1,3)、Gram固定=[[-2,3],[3,-6]]。
T=Hom(K_sigma,C*)→T_I=Hom(K^sigma,C*)は(xi,eta)↦(xi,eta³)、kernel mu3。
D4正根制限はeta,xi eta,xi eta²が各3回、xi,xi eta³,xi²eta³が各1回。実ベクトル空間のfoldingで不変/余不変の整数差を消さない。
所在 `prop:hurwitz-homology-S3`, `prop:triality-index-three`。

## 4. 対称族にも実際のperiod標識を構成する

S=sum_{t=eta,xi eta,xi eta²}(t+t^-1)、L=sum_{t=xi,xi eta³,xi²eta³}(t+t^-1)。
lambda=(S+2)/4、h=(L+3S+4)/8 と置くと、対称quarticは
N=(u+1)prod_{t=eta,xi eta,xi eta²}[u+(t+t^-1)/2]。
六root character≠1、eta,xi eta,xi eta²≠−1の開集合を使う。四根相異なり、対応Uはsmooth。

**従来chartの範囲外を別証明。** 対称族はB=Cなのでu=-1に退化fiberがあり、二成分v+w=−lambda±sqrt(lambda²+2lambda−1−2h)は境界で交わる。両境界zは−1だが、局所curveは別で各々D1を横断する。

z=(-xi eta²,-xi eta,-eta,-1)の選択の適合性を、line section
k=−xi eta²、m=(k+k^-1)/2、ell=−(eta+1)(xi eta+1)/2、v=ku+ell,w=m
で確認した。これはW=lambda族の等位面上の直線。
第一～三選択成分w=zi v−2lambda zi/(zi−1)とsectionの非交叉を表す値は、共通分母2xi eta²を除いて
(xi eta²−1)(xi eta³−1)(xi²eta³−1)、
(xi eta−1)(xi eta²−1)(xi²eta³−1)、
(eta−1)(xi eta²−1)(xi eta³−1)。
全て開条件で非零。u=-1ではsectionと交わらない成分をE4、無限遠E5=D2を選ぶ。五本を縮約してF1になり、境界gluingは四番目でも有効。
従って四periodは(eta,xi,eta,eta)。この証明によりxi,etaは形式的なroot変数ではなく実際のLooijenga periodである（`thm:symmetric-period-reconstruction`）。

## 5. period isogenyのWeyl商とG2三成分

W(G2)はr_c:(xi,eta)↦(xi^-1,xi eta)、r_o:(xi,eta)↦(xi eta³,eta^-1)で作用。
y=(eta,xi eta,(xi eta²)^-1)、prod y=1とすると置換S3と同時反転。e1=Σy,e2=Σy^-1、S=e1+e2、L=e1e2−3だからT/W=Spec C[S,L]。
T_Iにはy'=(xi,xi eta³,(xi²eta³)^-1)。alpha=Σ(y'+y'^-1)=L、beta=Σ_(i≠j)y'_i/y'_j=Σ(y_i³+y_i^-3)=S³−3SL−9S−6L−12。
Fricke b_F=−S−2,c_F=L+3S+4として
alpha=c_F+2+3b_F、beta=−b_F³+3b_F²+3b_Fc_F+3b_F−2。
これがBoalch–Paluba式(12)と一致する。**既知の3成分底写像の次数3を、period格子の指数3で説明する可換図式**である。
表現論的にもtriality固定G2⊂Spin8で8→1⊕7、28→14⊕7⊕7。chi7=1+S、chi14=2+S+Lからb_F=−(chi7+1)、c_F=chi14+2chi7となりBP Remark19と一致。
これはtorus isogenyであって、標数0のG2群に非自明な中心isogenyを構成したのではない。Langlandsや量子群・圏同値は未構成（`thm:G2-period-isogeny-quotient`）。

## 6. 三成分の有理同型と整数7/21の差

regular G2底のtorus持上げを取ると三Fricke成分は(xi,zeta^j eta),j=0,1,2に対応する。**三つとも§4の明示開集合に入る範囲**で四periodは中央xi、外側zeta^j eta。
正規化対数は外側でj/3、中央で0だけずれ、枝で整数を加える。整数H2の持上げを有理的にj delta_infty/3だけ変更するとF²とweight graded piecesが一致する。したがって成分の有理MHSは標識の下で同型。有理分裂可否は同時。全域の標準VMHS同型や代数的曲面同型ではない（`thm:G2-companion-rational-Hodge`）。

Klein例：xi=eta=primitive7root epsでS=L=−1。Fricke(b,c)=(-1,0)、G2(alpha,beta)=(-1,-1)。G2判別二因子7,-7でregular。全rootと補助開条件は非零。
Kleinの四periodは全てepsなので、整数MHS拡大類の位数は正確に7。
他二成分はb=(-5±sqrt21)/2,c=−3−3b、中央eps・外側zeta epsまたはzeta²eps、整数拡大類の位数は正確に21。
整数拡大は四つの正規化logのC/Z類で、位数はperiod位数のlcm。7対21は整数graded pieceの基底変更でも不変なので、Kleinとコンパニオンの整数MHSは非同型。全て有理分裂なので有理MHSは同型。
この算術はQ(zeta21)で厳密に確認した（`cor:Klein-seven-twentyone-Hodge`）。Klein七点braid軌道とG2実現は既知。他二成分に同じ有限軌道があるとは主張しない。

## 7. ホモロジーに見えない正entropy

一般係数でもiota_u=(2vw-u-2A,v,w)と巡回式はVieta involutionで体積を反転しWを保つ。GN Theorem2によりH2では−I。
g=iota_v iota_w iota_u iota_wはH2でI、omegaを保存するため全period不変。対称族ではg=B1² B2^-2。
参照torusのmodular行列は[[1,-2],[-2,5]]、固有値3±2sqrt2、level2。Cantat–Lorayの既知定理で力学的次数3+2sqrt2、topological entropy log(3+2sqrt2)。
正entropyとアフィンH2恒等は矛盾しない。固定した射影閉包上では双有理写像で、境界の不定点がある。射影正則自己同型のcohomology spectral radiusとの同一視は不可。
Kleinの有理MHS分裂でもこの正entropyが存在する。periodの捩れ性やHodge分裂は力学の有限性を意味しない。次は境界の変更列、cluster tropical作用、局所化した圏の不変量が何を検出するかを調べる（`prop:period-invisible-entropy`）。

## 8. 一次文献と確認範囲

- W. M. Goldman, W. D. Neumann, *Homological action of the modular group on some cubic moduli spaces*, Math. Res. Lett.12 (2005),575–591、DOI https://doi.org/10.4310/MRL.2005.v12.n4.a11 。Theorems1–2、Proposition3、§2のhomology作用を著者PDF https://www.math.columbia.edu/department/neumann/preprints/wmgwdn2.pdf の本文で確認。有限ホモロジー像とVietaの−Iは既知入力。web screenshotはcache missで取得できなかった。
- P. Boalch, R. Paluba, *Symmetric cubic surfaces and G2 character varieties*, J. Algebraic Geom.25 (2016),607–631、DOI https://doi.org/10.1090/jag/668 ; arXiv:1305.6594。Lemma6、式(12)、Corollary11、Proposition18、Remark19、§7を原論文本文で確認。三成分・G2表現・Klein有限軌道は既知。今回のperiod torusとの等式・Hodge比較を区別する。web PDF screenshotは取得エラー。
- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier59 (2009),2927–2978、DOI https://doi.org/10.5802/aif.2512 。著者preprint arXiv:0711.1579v2 TheoremB、Theorems4.7–4.8で力学的次数・entropy=spectral radiusのlogを確認。新しい一般entropy定理ではなく指定wordへの適用。web screenshotはcache missで未取得。
- R. Friedman, *On the geometry of anticanonical pairs*, arXiv:1502.02560v2 (2016)、§3 Proposition3.12、pp.21–23。既存の積分period・線束制限・MHS比較を使う。境界period1へomega/(2pi i)²で合わせる。前回本文・頁画像を確認済み、今回は全論文を再監査していない。
- N. Schock, *The W(E6)-invariant birational geometry of the moduli space of marked cubic surfaces*, Math. Nachr.297 (2024),2639–2666、DOI https://doi.org/10.1002/mana.202300459、§2。Naruki–LooijengaのD4 period torus/root hypertorusの既知構造。出版社全文取得403の制約があり、同論文全体の独立再監査ではない。

既知の有限ホモロジー像、folding、G2底写像、entropyと、本稿の具体的periodによる接続・7/21算術を分ける。後者の文献上の既出性は網羅的には未確認。

## 9. 再現・検証と次の着手

新しい `computations/verify_triality_period_isogeny.py` を実行してPASS。整数行列、Q-Laurent恒等式、Q(zeta21)の厳密演算のみ。小証明書は `triality_period_isogeny_certificate.json`。
対称quartic分解とline section非交叉、実際のperiod、Weyl不変量、mu3、三Klein成分、力学行列を確認した。ホモロジー・縮約・線束period・MHS拡大・entropyは通常証明と引用定理に依存し、計算がその全てを形式検証したのではない。
新節のLuaLaTeX wrapperは5頁、内部参照・overfullなし・画像点検を確認。主論文全体の今回の組版、旧28検証器の全再実行、旧理論の独立査読、新規性の網羅調査は未実施。

次は三成分の3捩れ差を境界線束・代数的対応・有限被覆として実現できるかを調べる。Klein7/21が整数比較の障害になる。他方でH2に見えないgの境界blow-up/downとcluster tropical作用を求め、圏的entropyへの入口を探す。何も構成せずに有理Hodge同型から導来同値を推論しない。一般period基底での代数的Gauss–Manin接続、global標識monodromyも残る。
GitHub mainを正本に保存し、push済み内容はLibraryに保存しない。
