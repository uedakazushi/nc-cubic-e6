# Poisson量子化・中心切断・心の変更：現行研究ノート

2026-11-18 / publication-v32。最初に `00_research_plan.md` を読む。
本書の証明は `papers/fricke-geometry.tex` のPoisson order・Casimir葉・相対被覆の各節に収める。原稿ソースは `papers/sections/quantum_cubic_poisson_orders.tex`、`papers/sections/quantum_cubic_casimir_leaves.tex`、`papers/sections/quantum_cubic_relative_poisson.tex`。基本変形・H3認識は `papers/nc-cubic-e6.tex` と `research/research_notes.md`、広い文献比較は `research/fricke_daha_comparison.md` を参照する。ファイルパスはroot起点とする。検証・組版の実施状態は `research/publication_status.md` と `computations/validation.json` に集約する。
量子化から指定Goldman型括弧への比較、コンパニオン五次のmonodromy、指定Casimir切断の判定は以下の範囲で得られている。一般H3 locusや全中心fiberのMorita型まで解決したとはしない。

## 1. 量子化からの括弧と規約

V=V_{a,b,c} の三関係は yz-qzy=x+a（巡回）、q²+q+1=0。a,b,cを固定して Q=q exp(h) とする。PBW係数環は Q(Q)[a,b,c]、唯一のoverlapはzyx。一般Qの厳密Casimirは

```
Omega_Q=xyz+(x²+Q²y²+z²)/(Q²−1)+(ax+Qby+cz)/(Q−1).
```

Q=qで既存Omegaと一致する。X=x³+q²x等の持上げをx³+Q²x等とすると、中心の括弧は

```
{X,Y}_rt = 9(XY−2eZ+cOmega−ell_c) = −9 P_Z, cyclic;
{Omega,-}_rt=0.
```

この等式は全a,b,cに対する厳密なPBW係数恒等式である。`computations/verify_root_poisson.py` はまず一般QのCasimir三交換子、次に特殊値の中心九交換子、最後に三つの Q d/dQ 微分を確認する。各微分のPBW正規形は13非零係数。浮動小数点、有限体標本、補間は使わない。

Omega=-D、u=-X/e等のFricke座標では `{u,v}_rt=9 F_w`（巡回）。これは本稿で選んだJacobian規約に対する係数9であって、Goldman規約全般に無条件に同じ数値を主張するものではない。Q=q+hを使うと9q^{-1}になる。括弧の中心上の値は持上げ非依存だが、V全体への導分の持上げは内部導分の曖昧さを持つ。

## 2. 表現論へ使える正確な範囲

Vはk[X,Y,Z]上27語 x^i y^j z^k (0≤i,j,k<3) で自由で、全中心上のgeneric rankは9。Brown–Gordonの元の意味でPoisson orderとなる。Casimir切断A_Dには中心部分環 Z(V)/(Omega+D) が単射する（Vが整域で中心元の割算を用いる）。**任意Dで商の全中心がこの部分環に一致するという追加主張はしていない。**

Fricke cubicは全係数で既約かつ無限遠三角形に沿って滑らか、特異点は有限である。そのsmooth locusは一つのsymplectic leaf、各特異点は零次元leaf。Brown–Gordon Theorem4.2から、固定したa,b,c,Dでsmooth locus上の中心fiber代数は全て同型。

従って**一点のfiberがM3なら全smooth locusでM3**。この一点の存在を全Dについて証明したとはしない。generic rank9だけで全特殊DのAzumaya性やglobaldimを結論するのは不可。次の着手は、固定Dでの9次元fiberの行列表現と中心characterの列挙である。Frickeのsmooth locusが空でないことは幾何学的に分かるが、Vのgeneric Azumaya開集合がそのsliceと交わることとは別である。

## 3. 純粋q変形の障害

主張の範囲はOmega係数が非零のchart、すなわち

```
G=Omega+beta X+gamma Y+delta Z+epsilon.
```

中心でGを消去するとP_Gの次数は3で、最高部は −(beta X+gamma Y+delta Z)^3−XYZ。次数≤2の関係はない。`{G,X}/9, {G,Y}/9, {G,Z}/9` の最高二次部は

```
X(delta Z−gamma Y), Y(beta X−delta Z), Z(gamma Y−beta X).
```

よって(G)がPoissonイデアルとなるのはbeta=gamma=delta=0だけ。指定したambient変形V_hの平坦両側商が存在すれば、中心における特殊イデアルはPoissonでなければならない。これは I_h∩h A_h=h I_h から従い、双対数底にも有効。Casimirの場合はOmega_Q+epsilonが全次数の平坦持上げを与える。したがって必要十分である。

本稿の滑らかな楕円H3選択点 G0=2Omega+X+2Y+3Z+5 では障害の最高部は9X(3Z−2Y)。a,b,cの一次変更では消せない。Q=qで中心交換子が全a,b,cについて零なので、これらの方向の微分は零だからである。

**回避すべき誤推論：** これは特定のambient変形の内部での障害であり、一般H3/dg変形や中央切断を含むSklyanin同時変形を妨げない。既存の八変数族はそのような追加方向を持つ。明示例 Phi_u=(1+2u)xyz−qxzy+u(x³+8y³+27z³)−(x²+y²+z²)/2 をpotentialスカラーで規格化すると、Q=q/(1+2u)というq方向と三つの純三次方向が同時に現れる。この組合せの中央持上げは非可換変形原稿 `papers/nc-cubic-e6.tex` の `eq:explicit-integral` で構成されている。次に、各成分が一次中心方程式に与える項を分離すれば、障害の相殺を明示できる見込みがある。この分離計算自体は未実施。

## 4. modular作用と固定したH3心の違い

sigmaはaffine代数に対して x↔y、z→(q²−q)xy−q²z+qc。Casimirを保ち、中心ではZ→(XY+cOmega−ell_c)/e−Z。sigma²=1とrho³=1のPSL2Z作用と、それを覆うbraid群の作用を区別する。

Casimirコンパクト化の両側が強いH3なら、pointed exact同値は反標準graded環と二次包絡を復元し、中心一次直線ktを保存するためPBWのF1を保つ。一方sigma(z)は正確に次数2。中心上でもsigma(Z)は次数6でZの次数3を保たない。したがって局所化後に内部自己同型を合成してもsigmaを誘導できない。これは `prop:vieta-not-pointed-heart` の結論。

古典中心でも、滑らかな射影三次曲面の同型は反標準埋込みで線型になり、無限遠三角形を保存すればspan(1,u,v,w)を保つ。しかしsigma(w)=−uv−C−wは二次であり、正則延長しない。これはCantat–Lorayの双有理幾何と整合する。

**肯定的に構成すべき対象：** affine局所化の圏における作用、境界のblow-up/downを介した非可換対応、導来圏の心の変更。未構成の導来同値を結論しない。固定された構造対象を外せば上の再構成障害はそのままでは適用できず、その範囲も未判定である。

## 5. 十Poisson零点・Casimir pencilのH3二類型

固定包絡a=b=c=0の総中心P=Omega³+f Omega²-XYZ+e(X²+Y²+Z²)、e³=-f³/27。
Poisson零点はP_X=P_Y=P_Z=0、従って
(1) X=Y=Z=0、Omega=0または-f（2点）；
(2) (X,Y,Z)=2e(eta1,eta2,eta3)、eta_i=±1,積+1、Omega=-2f/3またはf/3（8点）。
合計10点。前者のOmega=0と符号点Omega=-2f/3の5点は総中心のA1節点で、残る5点は総中心上は滑らかなOmegaの臨界点。前5点だけがVの1次元表現の中心character。

Casimir切断Omega=-Dの特異値は正確にD=0,2f/3,f,-f/3、A1個数はそれぞれ1,4,1,4。既存の固定包絡H3判定に依存して、前二値はH3、後二値は非H3。この範囲で「切断のPoisson零点が全て総中心の特異点（零点なしも許容）」とH3性は同値。判定に中心のADE型だけを用いない。

さらに空間三変数の非退化Hessianと形式Morse補題から、局所A1平滑化パラメータは原点組で D²(f-D)、四符号組で -(D+f/3)(D-2f/3)²。**H3節点のCasimir方向は二次接触、非H3節点は一次横断**。これらは通常の証明で、因数分解と10点のHessianは `computations/verify_casimir_poisson_leaves.py` で厳密再現済み。

固定包絡のgraded A4対称性と非可換Vieta sigmaは、p0,r0を固定して二つの符号四点集合それぞれにS4を生成する。sigmaは符号三つ組eta1,eta2を交換し、A4の偶符号変更と巡回置換を加えてS4となる。検証器は四点上の置換群の位数24も確かめる。この有限作用をmodular群そのものの有限性と混同しない。証明はFricke原稿 `thm:ten-poisson-points`, `thm:casimir-four-values`, `prop:casimir-smoothing-orders`, `cor:poisson-ten-s4`。

一般a,b,cでのPoisson臨界schemeの有限平坦性と一次元表現被覆のmonodromyは次節で解決した。残る問題はコンパニオン五次の幾何、smooth総中心のPoisson零点の中心fiber代数、非H3の局所order、全Casimir値でのM3やMorita型である。

## 6. 相対Poisson臨界schemeと五次因子

Fricke原稿 `papers/sections/quantum_cubic_relative_poisson.tex`（`thm:relative-critical-flat`, `thm:critical-discriminant-quintics`, `thm:character-cover-S5`）に通常の証明を収めた。

全係数底A=k[a,b,c]上、臨界scheme K=(P,P_X,P_Y,P_Z) は有限平坦rank15。証明の鍵は通常斉次化した四式がP4上の(3,2,2,2)完全交叉（degree24）で、無限遠に三つの座標頂点がそれぞれ長さ3の厚みとして残ること。無限遠X=1でP_X,P_Y,P_Zの(T,Z,Y) Jacobianは2eの単元、完備化ではT=Y=Z=0、P=Omega³。従って affine component はdegree24−9=15。非被約な底変更でも有限自由である。

一次元表現 E=( (1-q)yz−x−a, (1-q)zx−y−b, (1-q)xy−z−c ) は有限平坦rank5。P3の三二次完全交叉（degree8）から無限遠の三単純sectionを引く。総空間はA3_{x,y,z}なので既約。原点fiber5点はétaleであり、全係数恒等式 P=P_X=P_Y=P_Z=P_Omega=0 により中心の五節点としてKに入る。原点の十支持点の(X,Y,Z) Hessianは全て非退化。五節点側ではP_Omega=0、P_OmegaOmega=±2fで、臨界環が二重；他の五点ではP_Omega=f²でétale。原点のZariski開近傍でKは節点Eの相対一次厚み（rank10）と smooth residual E'（rank5, etale）に分解する。E'の幾何学的既約性とmonodromyは§7の `thm:paired-quintic-S5` により決定される。

全域のCasimir臨界値多項式 Δ15(D)=det(D+Omega|K) は N5(D)² M5(D) に分解する。N5(D)=Norm_{E/A}(D+Omega|E) はmonic degree5、M5はmonic degree5。原点で N5=D(D−2f/3)^4、M5=(D−f)(D+f/3)^4。全域への延長は稠密開の分解とmonic除算による。小証明書 `computations/relative_poisson_cover_certificate.json` は原点の15次元Groebner商、15×15の乗法行列、三無限遠Jacobianを厳密チェックした（全域平坦性は通常の証明）。

変数u=(1-q)x,v=(1-q)y,w=(1-q)z、底A'=(1-q)a等を使うと、E→A3は多項式写像(A',B',C')=(vw−u,wu−v,uv−w)。これは potential H=uvw−(u²+v²+w²)/2 の勾配写像。Jacobianは u²+v²+w²+2uvw−1。底A'=B'=C'=−1/4で、(u,v,w)=(1/2,1/2,1/2)が単純fold、その他の三点は(5/4,−1,−1)の順列で非分岐（Jacobian=81/16）。E既約・次数5素数・局所慣性に互換があるためmonodromy=S5。

一次元表現のCasimirは正確にOmega_E=f(uvw−u²−v²−w²)/3。原点の四符号sheetの一次微分は −f/3(eta1 dA'+eta2 dB'+eta3 dC')、互いに異なるのでOmegaはgeneric五sheetを分離する。従ってN5は既約五次・Galois群S5。この式とfoldを `computations/verify_relative_poisson_cover.py` で厳密検算した。

コンパニオンM5の既約性とmonodromyは次節の完全対称群定理で解決した。**現在の数学的課題**は、二つのS5被覆の分岐因子の具体式と交叉、Poisson局所order、一般a,b,cでのH3判定、Painlevé VIの判別式との正確な比較である。任意a,b,cや一般楕円E6成分のH3開性には未解決条件がある。

## 7. 独立な二つの幾何学的S5

Fricke原稿 `thm:paired-quintic-S5` で、残余五次式M5の幾何学的既約性とGalois群S5、N5とM5の同時Galois群 **S5×S5** を証明した。従って二つの分解体は線型非交叉、判別式の平方類も独立。この証明の重要な細部は次の通り。

基礎数体K0=Q(q)、q²+q+1=0。係数(a,b,c)=(30,19,29)を固定し、有限体の二つのsplit素数で中心臨界15次元環と一次元表現5次元環の両方の乗法行列を作る。p=1009, q=374ではM5が既約五次でFrobenius cycle(5)。p=1069, q=86ではN5が既約五次(5)、M5は既約二次と既約三次の積(2,3)。いずれもN5とM5は互いに素で分離的、Delta15=N5²M5を有限体上で独立確認。プログラム `computations/verify_companion_s5.py` と小証明書 `computations/companion_s5_certificate.json` がこの有限体上の算術を厳密再現する（SymPyのみ、浮動小数点・ランダム標本なし）。

M5の算術Galois群は5-cycleと型(2,3)の奇置換を持つ。位数30のS5部分群は存在せず、位数60はA5で奇置換を含まないのでS5。二つの算術S5が作るsubdirect productはGoursatによれば、直積、符号を一致させるC2 fiber product、または自己同型グラフのいずれか。p=1069の同時FrobeniusはN5側(5)偶、M5側(2,3)奇なので真のsubdirectを排除し、算術群S5×S5。

**幾何学的な帰結には有理基点が重要。** 原点近傍で E と E' は双方とも有限etale五重被覆であり、原点fiberの各5点は全てK0有理（Eはp0,p_eta、E'はr0,r_eta）。Stacks Project [Tag0BTX](https://stacks.math.columbia.edu/tag/0BTX) の基本群完全列は原点の有理基点からsplitし、そのGalois(K0) sectionは二被覆の十点に自明に作用する。よって算術monodromy=幾何monodromy=S5×S5。**M5(D)自身は原点で四重根を持つ**ので、原点でétaleなのはDのみの零点schemeではなく四中心座標を保持する E' である。この区別を忘れない。kは任意の標数0代数閉体まで拡張できる。

M5の既約性・Galois群・N5との独立性は上記定理の結論である。残る問題は大域分岐因子の方程式、分岐の交叉、局所Morita/H3 admissibility、一般楕円E6族への接続、詳細な文献新規性である。二素数のFrobenius以外は通常の群論・基本群の証明であり、計算PASSを証明全体の形式検証と混同しない。

## 8. 一次文献と未確認点

- The Stacks Project Authors, [Lemma 58.14.3, Tag 0BTX](https://stacks.math.columbia.edu/tag/0BTX) は幾何学的に連結な底の算術・幾何fundamental group完全列。原点の有理基点sectionと組み合わせる。
- M. Inaba, K. Iwasaki, M.-H. Saito, *Dynamics of the sixth Painlevé equation*, Séminaires & Congrès **14** (2006), 103–167, §9.1 Definition 9.1, https://emis.de/ft/47232 。Fricke判別式を境界トレースに引き戻した際の二乗因子が既知。本稿の別の係数写像による N5² M5 との具体的な同一性は未検証。使用するのは同論文の判別式の記述であり、異なる係数写像を同一視する定理としては使わない。
- M. Havlíček, S. Pošta, *Center of quantum algebra U'_q(so_3)*, J. Math. Phys. 52 (2011), 043521, DOI https://doi.org/10.1063/1.3579992 。三乗根の中心生成元と関係式に関する既知研究。規約の完全照合と新規性調査は未完了。
- S. Baseilhac, P. Roche, *Unrestricted Quantum Moduli Algebras. I. The Case of Punctured Spheres*, SIGMA 18 (2022), 025, 78 pp. DOI https://doi.org/10.3842/SIGMA.2022.025 ; arXiv:1912.02440。Theorems7.17,7.19、Corollary7.20(3)を原PDFで確認。Frobenius中心の有限被覆とGoldmanの比較を既知の一般機構として使う。本稿の全特殊化を同論文のgraph algebraと同定したわけではない。
- K. A. Brown, I. Gordon, *Poisson orders, symplectic reflection algebras and representation theory*, J. Reine Angew. Math. 559 (2003), 193–216; arXiv:math/0201042; 著者PDF https://www.maths.ed.ac.uk/~igordon/pubs/poisord.pdf 。§§2.1–2.2（定義・量子化）およびTheorem4.2（同一symplectic core上の有限fiber代数同型）を原PDFで確認。導分持上げの内部導分の曖昧さを消したことにはしない。
- H.-W. Huang, *Center of the universal Askey–Wilson algebra at roots of unity*, Nuclear Phys. B 909 (2016), 260–296. DOI https://doi.org/10.1016/j.nuclphysb.2016.05.006 ; arXiv:1509.08719。中心の一般表示は既知。本稿の個別規約と全ての中心生成元の完全な比較は未了。
- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier 59 (2009), 2927–2978. DOI https://doi.org/10.5802/aif.2512 ; arXiv:0711.1579。§3.1（無限遠三角形とVieta双有理変換）、Theorem3.1を一次PDFで確認。古典的な非線型対称性の存在を本研究の新規発見としない。

計算コードは表示した規約と障害式の厳密検算を再現する。個々の式・障害定理の文献上の既出性を網羅的に確認したとはしない。

## 9. 再現と未解決問題

中心括弧は `computations/verify_root_poisson.py`、切断障害は `computations/verify_poisson_cut_obstruction.py`、十零点は `computations/verify_casimir_poisson_leaves.py`、相対被覆は `computations/verify_relative_poisson_cover.py`、二つの五次の算術は `computations/verify_companion_s5.py` で再現する。各コードと対応する小証明書を保持する。現行の実行結果は `computations/validation.json`、数学的点検と組版の範囲は `research/publication_status.md` を参照する。計算器の36件PASSは、基本群・群論・局所Morita認識の独立査読や定理全体の形式検証を意味しない。

次の着手は、二つのS5被覆の分岐因子とその交叉、smoothな総中心上のPoisson零点のfiber代数、全Casimir値でのMorita/H3判定である。純粋q方向の障害を相殺する同時Sklyanin方向の各一次寄与も、構成済み中心式から分離できる。数値中心値の判定と一般intrinsic H3 locusの開性を区別して進める。
