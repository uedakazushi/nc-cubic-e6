# 非可換三次曲面の変形・包絡・比較に関する研究ノート

2026-11-18 / publication-v32。
再開時は `00_research_plan.md` を最初に読む。本書は、現行の定理を使うための仮定、計算上の要点、障害、未解決問題をまとめる。証明を収録した事項は本文を参照し、証明全文を重複させない。ファイルパスは特記しない限りリポジトリrootからの相対パスである。数学的点検、計算実行、組版の実施範囲は `research/publication_status.md` を正本とする。

| 対象 | 公表用原稿 | 本書との関係 |
|---|---|---|
| 七次元正常形、八変数形式変形、表示stack、結節中心 | `papers/nc-cubic-e6.tex` | 本書の中心。代数・HHの本文は `papers/sections/e6_algebra_deformations.tex`、成分判定の範囲は `papers/sections/e6_moduli_scope.tex` |
| Fricke、Poisson、五次被覆、LG、格子、周期 | `papers/fricke-geometry.tex` | 具体式と未解決比較の入口を本書末尾に置く |
| 境界力学、特異点、MF、Milnor被覆、Prym | `papers/cubic-boundary-prym.tex` | 詳細は `research/boundary_pell_dynamics.md` と `research/boundary_analytic_moduli.md` |

## 1. 記法とH3認識の入力

\(q\) は原始三乗根。\(B_{\mathbf a}\) の低次係数は \(a,b,c\)、中心三次直線の係数は \([\alpha:\beta:\gamma:\delta:\varepsilon]\) とする。Rains式の \(Q,T,a_i,b_i,c_i\) は別の規約であり、包絡の中央一次元 \(t\) と混同しない。H3の同値は構造対象を保つexact同値であり、任意の導来同値による商ではない。

主論文の `ass:recognition` と `ass:order` は、具体的表示をH3圏として認識するための入力を明示する。これらの入力を使う結論と、PBW・中心式・形式表示incidenceだけから得る結論を区別する。

| 入力 | 現行の参照先 | 適用先・限界 |
|---|---|---|
| 固定量子so3包絡のH3切断判定 | `papers/sections/cubic_quantum_triangle_full_cuts.tex`, `thm:quantum-triangle-full-H3` | 原点切片の非空性、結節切断のH3性 |
| 固定位数の被約表示族でのH3開性 | `papers/sections/cubic_finite_order_relative.tex`, `thm:finite-order-relative-H3-open` | 七次元族のH3開集合。位数を変える一般族へは適用しない |
| 境界の局所order模型 | 同上 `lem:finite-order-boundary-order` | HH計算に必要なMorita局所模型 |
| 中央楕円境界とCY包絡 | `papers/sections/cubic_central_elliptic_cy_envelope.tex`, `prop:central-sklyanin-linear-lifts-symmetric` | 対称PBW補正と楕円方向 |
| 楕円境界からのaffine認識 | `papers/sections/cubic_normal_elliptic_boundary.tex`, `thm:normal-elliptic-affine-recognition` | affine商の有限大域次元からH3性を判定 |
| 飽和反標準環としての認識 | 主論文 `ass:recognition` | 表示した \(R\) 自身を反標準orbit環と同定する入力 |
| 認識後の二次包絡の一意性 | `papers/sections/cubic_as_surface_scope.tex`, `lem:anticanonical-quadratic-hull` | 一次生成二次関係環の三次商なら \(Q(R)=B\)。本文に直接証明 |

表のH3認識を支える四つの入力ファイルは関連研究からの入力断片であり、それぞれを単独で公表可能な自己完結した証明とみなさない。主論文での適用は上記仮定により追跡できる。入力の全独立監査・必要部分の完全な統合は公表前の課題である。存在しない別原稿や旧bundleを取得しなければ現在の主張の範囲が分からない構成にはしない。

## 2. 七次元正常形と中心の跳躍

固定位数三の中央PBW拡大を対称行列 \(A=(A_{ij})\) で書くと、
\[
 v=(A_{23},A_{13},A_{12})/(1-q)
\]
による平行移動で非対角二次係数を消せる。対角 \(h_i=A_{ii}\) は変わらず、定数項は
\[
 b'_i=b_i+h_iv_i+(1-q)v_jv_k.
\]
\(h_1h_2h_3\ne0\) なら、有限étale係数拡大の後
\[
 r_i^2=h_jh_k,\qquad r_1r_2r_3=h_1h_2h_3
\]
を選び、対角係数を1へ正規化する。残余は四つの偶符号と巡回置換、すなわち \(\mathfrak A_4\)。中心三次直線の \(\mathbb P^4\) と合わせて七次元となる。証明は `thm:normal`。対角係数零、非中央境界、非正規境界を被覆する定理ではない。

三捩れ点では中心三次の次元が跳ぶため、「一般fiberに中心元が存在する」だけでは指定切断を特殊化できない。`lem:central-lift` はまず楕円曲線と移動点から先頭三次元 \(g_s\) を指定し、低次補正を解く。\(F_2Z(V_0)=k\) により九未知数の交換子行列に単元minorが存在し、一般fiberの存在と特殊fiberの一意性から極を作らず持ち上がる。中心全体を一定rankの束とみなす必要はない。

H3性について、包絡と非定数中心元 \(G\) の定義体を \(F\) とし、中心値 \(D\) を独立な超越変数とすれば
\[
 V_{F(D)}/(G+D)\cong V\otimes_{F[G]}F(G)
\]
という中心局所化から有限大域次元を得る。`lem:generic-D` と `cor:eight-generic-H3` はこれとH3認識入力を使う。任意の数値 \(D\) の許容性や、有限PI次数を横断するH3開性をこの議論から結論しない。

## 3. HH計算の仮定と圏的結論

`ass:order` は、滑らかな三次中心 \(C\)、滑らかな反標準楕円曲線 \(D\)、\(C\setminus D\) 上のAzumaya性、境界での
\[
 k[[s,w]]\rtimes\mu_3,\qquad \zeta(s,w)=(s,\zeta w)
\]
とのMorita局所同値を仮定する。この下で `lem:local-HH` と `thm:HH8` は
\[
 \mathcal{HH}^0=\mathcal O_C,\quad
 \mathcal{HH}^1=T_C(-\log D),\quad
 \mathcal{HH}^2=\bigwedge^2T_C(-\log D)=\mathcal O_C
\]
を与える。非恒等sectorは法線の非自明指標により不変部分が消える。対数接束のcohomologyは \((0,7,0)\) なので
\[
 HH^0=k,\quad HH^1=0,\quad \dim HH^2=8,\quad HH^{\ge3}=0.
\]
したがって指定圏の形式変形は無障害である。

この条件付きHH証明では、局所計算、層の貼合せ、三次曲面の対数接束、spectral sequenceの微分消滅を確認できる。具体的なH3族にorder模型を適用できることは別の入力である。Hochschild homologyのtwisted sector、非捩れroot stackとの大域同値、全H3の成分分類をこのHH cohomology計算と同一視しない。Brauer捩れを無条件に消さず、root stackの位数二に限定された公式を位数三へ流用しない。

## 4. 反標準環のArtin再構成と四係数障害

本文は `papers/sections/quantum_cubic_artin_reconstruction.tex` と `papers/sections/quantum_cubic_quadratic_obstruction.tex`。
\(E_i=\pi R(i)\) には \(j\ge i\) で \(\operatorname{Ext}^{>0}(E_i,E_j)=0\) が成り立つ。AS Cohen--Macaulay性により第一cohomologyが消え、第二は \(R_{i-j-1}^{*}=0\)。全 \(E_i\) はexceptionalで、AZ ampleな無限列となる。De Deken--Lowen Theorem 4.5を \(\operatorname{Ind}(\operatorname{qgr} R)\) に適用し、有向 \(\mathbb Z\)-代数のflat線型変形とflat Abel変形を対応させる。

適合enhancementの条件は、\(E_{i,A}\) がperfect、derived Homが底上perfectで導来底変更に適合することである。特殊fiberで恒等なMorita同値があれば、\(\operatorname{Ext}^1=\operatorname{Ext}^2=0\) による対象持上げの一意性を使い、全正方向Homと合成を同定する。`thm:artin-injective` はAbel変形の**同型類上の単射性**である。与えられたMorita同値自体のt-exact性や自己同値群oidへの充満忠実性ではなく、無限列を有限完全例外列に置き換えてもいない。

smooth proper dg変形と底変更に適合する相対Serre作用の下で、
\[
 P_n=\operatorname{RHom}(E_A,\tau_A^nE_A)
\]
は特殊fiber \(R_n[0]\) を持つperfect複体である。Artin局所最小自由複体から有限自由な次数零加群となる。次数ごとのNakayamaで一次生成と六二次・一三次の有限表示を得る。有限な極大イデアルfiltrationは左右noetherian性を与える（`thm:artin-section-ring`）。

この再構成だけでは二次包絡 \(B_A\) のflat性は出ない。二次関係の挿入
\[
 (V\otimes I_2)\oplus(I_2\otimes V)\longrightarrow I_3
\]
は \(45\times48\) 行列で、特殊fiberのrankは44。単元minorで消去すると
\[
 (B_A)_3\cong A^{19}\oplus A/(o_1,o_2,o_3,o_4),\qquad
 (o_i)=\operatorname{Fitt}_0(I_3/(VI_2+I_2V)).
\]
三次flat性は四係数の消滅と同値で、障害idealは基底非依存・底変更適合である。全次数flat性が得られれば、三次核への左右乗法は各次数で同rank自由加群間の同型となり、核は自動的に正則正規な左右主イデアルになる。両側イデアルとして一元生成であることだけで、この結論を先取りしない。

## 5. potential包絡と八変数同時形式族

### 全Artin包絡

`thm:artin-potential-envelope` は、量子so3点の次数三以下の任意の巡回potential変形について、中央 \(t\) で斉次化した包絡の全次数flat性を証明する。中央係数環 \(A[t]\) 上の自由dg代数を
\[
 x_i:(1,0),\quad \xi_i:(2,1),\quad \zeta:(3,2),\qquad
 d\xi_i=\partial_i\widehat\Phi,\quad d\zeta=\sum_i[x_i,\xi_i]
\]
で定める。各内部次数が有界有限自由で、特殊fiberの \(t=0\) 商はCY量子三空間のacyclic potential複体である。\(t\) の完全列、内部次数の下有界性、Artin最小複体から全次数flat性を得る。bar複体により相対Koszul型14641と双対性も持ち上がる。外部入力はEtingof--Ginzburg §7.1、式(7.1.4)と同箇所のGinzburg定理である。

三次flat性には別の有限行列証明もある。三つの \([t,r_i]\) 展開syzygyと巡回Euler syzygyが全potential係数で持ち上がり、特殊fiberの \(64\times48\) 挿入行列rank44と四syzygyのrank4からSchur補行列が零となる。`computations/verify_universal_cubic_syzygies.py` が全係数多項式恒等式を再現する。有限次数検算そのものを全次数flat性の証明の代用にしない。

### 正則化した中心式

全八変数の中心持上げと形式incidenceは `papers/sections/quantum_cubic_multivariate_formal_chart.tex` に収録する。Rains式の印刷された \(Y\) の一次係数には、内側の \(Q^3b_2\) を \(Q^3\) へ直す必要がある。差は \(-TQ^3b_2(b_2-1)Y\) で非中央である。修正式は著者サイトのMAGMA式と一致し、新しい中心式の発見とはしない。\(b_2=0\) の特殊化にはこの印刷係数は影響しない。

\[
 p=1+\kappa\lambda,\quad Q=q_0/p,\quad T=-3\lambda\eta\zeta/p,
\]
\[
 (a_1,b_1,c_1)=(-\eta\zeta/p,-\zeta/(\eta p),-\eta/(\zeta p)),\quad
 (a_2,b_2,c_2)=(-\eta\zeta a/p,-\zeta b/p,-\eta c/p)
\]
を代入し、\(X=x,Y=\eta y,Z=\zeta z\) と戻す。potentialは
\[
 pxyz-q_0xzy+\lambda(x^3+\eta^3y^3+\zeta^3z^3)
 -\tfrac12(x^2+y^2+z^2)-ax-by-cz.
\]
修正Rains式の正規形を \(N\) とすると、全非定数係数は \(\lambda^2\) で割れ、
\[
 (N_{x^3}/\lambda^2)|_{\lambda=0}=9\eta^2\zeta^2(1+q_0)\ne0.
\]
したがって \(G=(N-N_{\varnothing})/N_{x^3}+D\) は共通因子を除いて正則となり、
\[
 G_0=\kappa\Omega(a,b,c)+X+\eta^3Y+\zeta^3Z+D.
\]
`computations/verify_rains_central_formula.py` は全係数で元関係の102挿入と三交換子を検証する。`computations/verify_central_multivariate_lift.py` は低次係数単項式ごとに \((Q-q_0,T)^2\) への所属と全先頭式を確認する。一般中心恒等式とこのideal所属を組み合わせるため、有限jetからの外挿ではない。

指定点 \(\eta_0^3=2,\zeta_0^3=3,\kappa_0=2,D_0=5\) では、中心incidenceの接空間は22次元、座標・二スカラーのgaugeは14次元。七既知方向に \(\lambda\) 方向 \(x^3+2y^3+3z^3+2xyz\) を加えると接空間を尽くす。22変数形式族への写像と、embedding dimensionからの22変数冪級数環全射の合成に形式逆写像定理を使い、incidenceの完備局所環が正則であることを得る。恒等gauge商は八変数形式円板である。

### 有用な有限計算と実装上の障害

- 基準点 \(a=b=c=0\)、中心係数 \((2,1,2,3,5)\) では、中心特異点idealは \(\mathbb Q(q)\) 上で単位ideal、境界判別式は170、\(\beta\gamma\delta=6\)。一次行列は \(105\times40\)、rank18、核22。gauge rank14、七既知方向までrank21、横断方向を加えて22となる。
- 一変数witness \(\Phi_u=(1+2u)xyz-qxzy+u(x^3+8y^3+27z^3)-(x^2+y^2+z^2)/2\) の中心係数は `computations/transverse_rains_lift_certificate.json`。極限は \(2\Omega+X+8Y+27Z+D\)。有理関数体上の三交換子恒等式であり標本補間ではない。
- `computations/verify_second_order_incidence.py` は36個の二次単項式に対する補正を再現する。係数行列自体も動くため \(B_2=-A_0^{-1}(C_2+A_1B_1+A_2B_0)\) を使い、補正後の元関係から再検算する。一次で規格化した書換え規則だけを二次でも使う方法は不正確である。この二次計算は現在は全形式式の補助検証であり、残された積分課題ではない。
- 121語の有理行列を一括反転すると式が膨張する。再現コードは書換え依存グラフの強連結成分ごとに、最大 \(12\times12\) ブロックを多項式分母付きで解く。

## 6. 一つのH3点の形式分類と代数的表示stack

`papers/sections/quantum_cubic_artin_enhancement.tex` は、order入力の下で、flat切断環からsmooth proper enhancement、相対Serre作用、心を保つ逆Serre作用、反標準環の認識を構成する。De Deken--Lowenのcompact生成性の持上げは一般のGrothendieck圏変形に適用し、geometric helixを仮定しない。特殊fiberの有限generatorをample列の有限部分の厚い閉包に置き、対応する有限直和を持ち上げる。derived Homのperfect性と、nilpotent底でのcompact性検出を対角へ適用してsmooth性を得る。

\(HH^1=0\) により、恒等自己同値の可逆bimodule持上げは対角と同型である。\(\tau_AT_A^{-1}\) にこれを適用し、逆Serre作用 \(\tau_A\) と次数シフト \(T_A\) を同定する。構造対象は相対exceptional、反標準列はAZ ample、\(R_A\) は飽和反標準環となる。rank-one torsion-freeは幾何学的fiberの条件であり、非正則Artin底上の絶対大域次元・整域性の主張ではない。

`computations/verify_potential_recovery.py` の中央一次行列rank3とpotential回復行列rank19は、小拡大帰納法による \(Z(B_A)_1=At\) とpotentialの単元倍までの一意性を支える。pointed exact同値は反標準環と二次包絡を保ち、affine座標変更と二つのスカラーのgaugeへ戻る。

こうして八変数表示族からAbel変形、さらにdg Morita変形への写像は全Artin底で同型類上単射となる。\(\dim HH^2=8,HH^3=0\) との比較により形式逆写像定理を適用し、`thm:intrinsic-formal-eight` を得る。**指定点の全flat pointed Abel形式変形は、上記order認識等の入力の下で分類される。** 全H3の代数性・大域成分・有限慣性を含む全群oidの分類ではない。

有限型の表示については `papers/sections/quantum_cubic_algebraic_boundary.tex` に八変数有理族を構成する。\(\eta\zeta p(p^3+1)\) と中心式の有限個の分母を可逆化した共通開部分で、全包絡・商は次数別flatとなる。noetherian性とdomain性には通常のAS3入力を使い、Hilbert値の計算だけからは導かない。
\[
 C=\kappa+\kappa^2\lambda+(\kappa^3/3+9\eta^3\zeta^3)\lambda^2,
\quad F=q_0p(x^3+\eta^3y^3+\zeta^3z^3)+Cxyz
\]
とすると左右point関係行列の行列式は \(3\lambda F\)。\(\Delta_E=C^3+27p^3\eta^3\zeta^3\ne0\) で相対楕円曲線を得る。\(\lambda=0\) では包絡商のpoint schemeは \(\mathbb P^2\) だが、中心三次切断の多重線型化が \(q_0^{-1}F_0\) となる。相対rank条件を除き、左右kernelから楕円曲線上の自己同型を作る（`thm:relative-THCR-boundary`）。THCRのHilbert値・底変更と中心式から \(R/(t)=\mathrm{THCR}\) を得る。

`computations/verify_boundary_graph.py` の一点計算は一般自己同型の三乗が恒等でないことを示す反例であり、全fiberの位数を標本から判定するものではない。一般fiberで中心三次のTHCR像が零であることを、有限局所自由性から全底へ延長する。独立中心値 \(D\) では先の局所化により幾何学的一般点はH3となる。

`papers/sections/quantum_cubic_presentation_stack.tex` では有限次数の平坦表示開部分上に中央incidence \(Z\) を置き、
\[
 \Gamma=(\mathrm{GL}_3\ltimes\mathbb G_a^3)\times\mathbb G_{m,\Phi}\times\mathbb G_{m,G}
\]
で商を取る。22次元の形式的滑らかさと八変数族の微分から、\(\Gamma\times U'\to Z'\) はétale全射となり、\([Z'/\Gamma]\) はsmooth DM八次元表示stackである。H3の幾何学的対象間の全pointed exact矢はこの作用で記述される。**表示stackの存在、一般点のH3性、指定点の形式H3分類は、それぞれ異なる結論**である。

残る核心は、位数を動かす表示stack内のH3 locusの開性、一般intrinsic族の相対再構成・降下、全境界と大域閉包である。形式smooth性だけでZariski開性を結論せず、有限generatorの相対dg模型と対角perfect性の代数化、または適用可能な非可換Projの有限提示smoothness判定を検証する。Artin代数化には有限提示・効果性などの仮定を個別に確認する。E6型weighted projective/Weyl商との同定も未完成である。

## 7. AS曲面との比較：確定した除外と未解決の範囲

本文は `papers/sections/cubic_as_surface_scope.tex`。飽和反標準環 \(R=B/(G)\) から
\[
 Q(R)=T(R_1)/\langle\ker(R_1\otimes R_1\to R_2)\rangle\cong B
\]
を回復する補題は直接証明する。ただし表示した \(R\) が飽和反標準環であることは別の認識入力である。

AOUのarXiv:2404.00175v1 §9は、滑らかな楕円曲線上の**無限位数**の平行移動から構成する反標準環 \(F=P/(C'_3)\) を扱う。式(9.6)--(9.10)、Lemma 9.2により、比較すべき二次包絡は \(P\)、唯一の中心一次直線は \(kt\)、その商は楕円point schemeを持つSklyanin環である。本七次元族の \(B_{\mathbf a}/(t)=S_q\) は \(q^3=1,q\ne1\) によりpoint schemeが \(\mathbb P^2\)、graphが \(\operatorname{diag}(1,q,q^2)\) である。したがって包絡一意性とpoint schemeの次元差から、両者の**pointed exact同値は存在しない**（`prop:aou-infinite-order-exclusion`）。

この除外を、有限位数の特殊化、別の構造対象・標識、任意の導来同値へ延長しない。AOU Theorem 9.4は導来同値であり、pointed exact同値とは異なる。八次元族の横断方向では中心一次商のpoint schemeが楕円曲線へ動くので、同じ障害は族全体には使えない。Okawa--Ueda Definition 1.1の意味でのAS曲面性・非AS性を全般的に決める問題は未解決である。

次の比較では許容する構造対象と標識を固定し、AOU/Okawa--Ueda側の有限位数部分の適用範囲、very strong helixの構成、心と反標準モデルの関係を調べる。八次元という次元の一致やHHの一致だけでAS曲面性を判定しない。

## 8. 結節中心因子

証明は `papers/sections/quantum_cubic_nodal_centers.tex`。固定包絡の中心三様体
\[
 P=\Omega^3+f\Omega^2-XYZ+e(X^2+Y^2+Z^2),\quad
 f=(1-q)/3,\quad e=-(2q+1)/9
\]
には五つの通常二重点 \(p_0,p_\eta\)（\(\eta_1\eta_2\eta_3=1\)）がある。各点を通る切断条件 \(L_i\) は線型独立で、既存H3判定の開集合では五つの非空既約SNC因子を与える。\(\mathfrak A_4\) 商では原点側と四符号点側の二成分となる。

witnessは \(G_D=2\Omega+X+2Y+3Z+D\) と
\[
 D\in\{0\}\cup\{4f/3-2e(\eta_1+2\eta_2+3\eta_3):\eta_1\eta_2\eta_3=1\}.
\]
境界判別式は170、各Jacobi idealは対応点の極大ideal、Hessian determinantは非零である。`computations/verify_nodal_cuts.py` はこの中心特異点計算を再現し、H3判定そのものの有限大域次元証明を検証するプログラムではない。

七次元族では一次元表現から
\[
 (a,b,c)=((1-q)yz-x,(1-q)zx-y,(1-q)xy-z)
\]
を得る。原点fiberは零と四符号解、Jacobian determinantは \(-1,4,4,4,4\)。射影斉次化の無限遠の三sectionを除くと、既約な開部分上に連結étale次数五被覆が得られる。中心式と全偏微分はこの被覆上で零となる（`computations/verify_character_node_cover.py`）。節点を通る切断の \(\mathbb P^3\) 束の有限像から、七次元族の結節中心因子は既約六次元となる（`thm:seven-nodal-irreducible`）。

中心の特異判別式はH3モジュライの境界と一致しない。八次元族への因子の追跡、intrinsic成分の大域閉包、古典的結節三次三様体との新規性比較は残る。

## 9. Fricke・Poisson側への参照と具体式

以下の証明は `papers/fricke-geometry.tex` に置く。詳細な比較表は `research/fricke_daha_comparison.md`、Poissonの適用限界は `research/poisson_order_notes.md` を参照する。

普遍Askey--Wilson代数のTerwilliger規約では
\[
 A_{\rm AW}=(1-q)x,\quad B_{\rm AW}=(1-q)y,\quad C_{\rm AW}=(1-q)z,
\quad \alpha_{\rm AW}=(1-q)a
\]
（他の中央元も巡回）であり、Casimirは
\[
 \Omega_{\rm AW}=q(1-q)^3\Omega=3(q+2)\Omega.
\]
中心式に \(\Omega=-D\)、\(u=-X/e,v=-Y/e,w=-Z/e\) を代入すると
\[
 u^2+v^2+w^2+uvw+Au+Bv+Cw+T=0,
\]
\[
 A=-(Da+\ell_a)/e^2,\qquad
 T=-(D^3-fD^2+DK-L)/e^3
\]
となる。係数写像のJacobianは \(a=b=c=0\) で \(3D(D-2f/3)^4/e^9\)。四穴球面トレースパラメータからFricke係数へのJacobianは \((1,2,3,4)\) で \(-200\)。有限étale底変更後の**中心**のcharacter variety表示であり、量子代数とcharacter stackの同型ではない。

braid生成元は \(x\leftrightarrow y\)、\(z\mapsto(q^2-q)xy-q^2z+qc\)、\((a,b,c)\leftrightarrow(b,a,c)\)、\(\Omega\) を固定し、Fricke座標では
\[
 (u,v,w;A,B,C,T)\longmapsto(v,u,-uv-C-w;B,A,C,T).
\]
`computations/verify_daha_character.py` と `computations/verify_daha_braid.py` が規約と元関係を再現する。root-of-unity量子化 \(Q=q\exp(\hbar)\) のPoisson括弧は、指定したGoldman型Jacobian括弧の9倍である（`papers/sections/quantum_cubic_poisson_orders.tex`）。一般的な「量子化からGoldman括弧が出るか」という問いはこの規約では解決されており、残るのはskein/DAHA写像の特殊化、全中心fiberのMorita模型、心を変える場合のVieta作用などである。

三角形付き三次曲面の \(D_4\subset E_6\) は古典的Picard格子の構造である。六点blow-upでは境界 \(D_i=H-E_{2i-1}-E_{2i}\)、直交root基底は
\[
 H-E_1-E_3-E_5,\quad E_1-E_2,\quad E_3-E_4,\quad E_5-E_6.
\]
Gram行列は負Cartan \(D_4\)、\(K^\perp=E_6(-1)\)。これを量子・圏的同値の証明とみなさない。

相対Poisson臨界schemeは有限平坦次数15、一次元表現schemeは次数5で、\(\Delta_{15}=N_5^2M_5\)。両五次被覆の幾何monodromyは \(S_5\)、同時群は \(S_5\times S_5\)（`thm:paired-quintic-S5`）。`computations/verify_relative_poisson_cover.py` と `computations/verify_companion_s5.py` は式の検証を担い、群論・基本群の証明と区別する。

Casimir切断では総中心の五節点に由来する \(A_1\) 切断がH3となり、滑らかな総中心のCasimir臨界点に由来する \(A_1\) 切断は非H3となるという指定判定がある。これは既存H3入力に依存する。一般 \(a,b,c\) の全H3判定、一般八次元族での中心形成、全境界への拡張は未完成である。

## 10. 一次文献と照合範囲

新規性の網羅的調査と全依存定理の独立査読は完了していない。本文に出典を記したこと、一次資料の内容を点検したこと、計算証明書を実行したことは別の状態であり、今回の実施範囲は `research/publication_status.md` を参照する。

| 文献 | 参照箇所・識別子 | 使用範囲・留保 |
|---|---|---|
| Abdelgadir--Okawa--Ueda, *Compact moduli of marked noncommutative cubic surfaces* | [arXiv:2404.00175v1](https://arxiv.org/abs/2404.00175v1), §9, (9.1)--(9.10), Lemma 9.2, Theorem 9.4 | 無限位数の仮定、反標準商・二次包絡、Serre作用、導来同値を一次本文で確認。有限位数全般やpointed exact同値へ拡張しない |
| Okawa--Ueda, *Marked Artin--Schelter surfaces of del Pezzo types* | [arXiv:2508.04986v1](https://arxiv.org/abs/2508.04986v1), Definition 1.1 | AS曲面・del Pezzo型・標識の定義を一次本文で確認 |
| Etingof--Ginzburg | [arXiv:0709.3593v4](https://arxiv.org/abs/0709.3593v4), Theorem 3.3.2(i),(ii), §7.1, Appendix 9.1 | potential PBW、中心元、dg複体。中心式の修正は[著者のMAGMA式](https://math.mit.edu/~etingof/delpezzocenter)と整合。一般性の仮定を三捩れ点へ無条件に移さない |
| Negron--Schedler | [arXiv:1809.08715](https://arxiv.org/abs/1809.08715), Theorem 1.1, Appendix A | 固定部分の法線行列式と局所大域spectral sequence |
| Faber--Ingalls--Okawa--Satriano | [arXiv:2206.13359v2](https://arxiv.org/abs/2206.13359v2), Theorem 1.5, Corollary 1.7 | tame orderとBrauer捩れ付きstacky曲面。非捩れ同値として使わない |
| Fu--Porta--Scherotzke--Sibilla | [arXiv:2509.00501v3](https://arxiv.org/abs/2509.00501v3), Proposition 6.17 | root stackの恒等sectorと比較。位数二に限る後半は使わない |
| Rains | [arXiv:2107.13540v2](https://arxiv.org/abs/2107.13540v2), Propositions 2.2, 2.3, Example 2.1, §6末尾 | 次数三の全パラメータ被覆を証明済み入力にしない |
| De Deken--Lowen | J. Noncommut. Geom. 5 (2011), 477--505, [doi:10.4171/JNCG/83](https://doi.org/10.4171/JNCG/83), Propositions 4.4, 4.6, Theorem 4.5, Propositions 5.5, 5.8, 5.9 | 正方向Ext消滅を持つZ生成列、一般Grothendieck変形のcompact生成。有限例外列・geometric helixに限定した別定理と区別 |
| Lowen--Van den Bergh; Lowen | [arXiv:math/0405227](https://arxiv.org/abs/math/0405227); [arXiv:0707.2602](https://arxiv.org/abs/0707.2602) | Abel変形のHH障害理論とexceptional対象の持上げ |
| Stacks Project | [Tag 0BDK](https://stacks.math.columbia.edu/tag/0BDK) | perfect複体のfiber判定。Artin局所版は本文で直接証明 |
| Iyudu--Shkarin | [arXiv:1601.00564](https://arxiv.org/abs/1601.00564), Theorem 1.1, Corollary 6.1 | Sklyanin環のHilbert値・正則性。domain/noetherian性をHilbert値だけから推論しない |
| Chekhov--Mazzocco--Rubtsov | Adv. Math. 376 (2021), 107442, [doi:10.1016/j.aim.2020.107442](https://doi.org/10.1016/j.aim.2020.107442), [arXiv:1905.02772v2](https://arxiv.org/pdf/1905.02772v2), Definition 1.1, (1.5), Theorem 1.5, Proposition 4.2 | 一次本文と表示の係数対応を確認。Definition 1.1の非根仮定のため、三乗根への表示の特殊化を定理の適用と区別する。結節因子・個別公式の既出性の照合は残る |
| Goldman--Toledo; Schock | [arXiv:1006.3838](https://arxiv.org/abs/1006.3838); Math. Nachr. 297 (2024), 2639--2666, §2, [doi:10.1002/mana.202300459](https://doi.org/10.1002/mana.202300459) | Fricke表示の一般性と三角形直交 \(D_4\) は既知。指定量子規約への対応と既知一般理論を分ける |

## 11. 再開時の判断基準

1. 公表準備ではまず入力認識の依存を監査し、既知の定理の適用範囲と本稿の独自計算を明確にする。計算器のPASSを数学的査読と呼ばない。
2. 形式分類をさらに低次jetで確認し続けることは主課題ではない。次の本質的問題は、位数変動下のH3開性と相対降下、数値中心値の許容条件である。
3. AS比較では、構造対象・標識・同値の種類を先に固定する。既知の無限位数locusの除外と、全AS曲面性の判定を分ける。
4. Fricke・境界・Prym側の価値ある結果はそれぞれの現行論文で保持し、未構成の圏的同値や大域対応を名前・次元・格子の一致だけから推論しない。
