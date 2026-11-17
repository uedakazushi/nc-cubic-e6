# 成分研究ノート

2026-11-17 / triangle-component-v17。方針はルートの `00_research_plan.md`、証明は `papers/nc-cubic-e6.tex`（rootからのパス）。
このノートは履歴ではなく、現在の入力・障害・再開のための知識を記す。

## 1. 記法と既存入力

qは原始三乗根。B_aの低次係数はa,b,c、中心三次線の係数はalpha,beta,gamma,delta,epsilon。
添字RはEtingof--Ginzburg/Rains公式の変数であり、包絡の中心一次元tとは区別する。

依存する既存H3分類原稿の固定参照は nc-cubic-moduli commit
`846c1361651790082f54b524350370ead81811d5`。
この保存済み基点には七次元族と以下の入力がある。別の旧bundleの復元は不要である。

| 入力 | ファイルとラベル | 今回の使い方 |
|---|---|---|
| 固定qso3包絡の全H3切断 | `papers/sections/cubic_quantum_triangle_full_cuts.tex`, `thm:quantum-triangle-full-H3` | 原点切片の非空性・滑らかな中心を持つ例 |
| 位数固定の相対H3開性 | `papers/sections/cubic_finite_order_relative.tex`, `thm:finite-order-relative-H3-open` | 七次元族のH3開集合 |
| 境界の局所order | 同上 `lem:finite-order-boundary-order` | HH層計算の局所Morita入力 |
| 中央境界CY認識と対称PBW | `papers/sections/cubic_central_elliptic_cy_envelope.tex`, `prop:central-sklyanin-linear-lifts-symmetric` | 正常形と一般Sklyanin持上げ |
| 楕円境界からのaffine認識 | `papers/sections/cubic_normal_elliptic_boundary.tex`, `thm:normal-elliptic-affine-recognition` | 超越的中心値のH3性 |
| 包絡・商の復元 | `papers/weak_cubic_axioms.tex` のH3認識部分 | pointed exact同値とgraded同型の比較 |

これらの入力の内容は現行論文に明記してある。全依存定理の独立再監査は未実施である。
この専用ディレクトリに既存の全AS4分類ノートや旧論文のコピーを重複させない。入力の現行ファイルは同じリポジトリに存在する。

## 2. 固定位数3の正常形で有効な式

対称PBW行列Aに対してv=(A23,A13,A12)/(1-q)を平行移動量に取る。
対角h_i=Aiiは不変、新定数はb'_i=b_i+h_i v_i+(1-q)v_jv_k。
hiが単元ならri²=hj hk、r1r2r3=h1h2h3を選んで対角を1へ正規化する。
4つの偶符号と巡回置換が残る。これに中心三次線P4を加えたものが7次元正常形。
対角係数零は未被覆の境界であり、この正規化から消してはいけない。

## 3. 全次数持上げで重要な障害の回避

中心が跳ぶ点で「一般中心元が存在する」だけでは指定切断へ特殊化できない。
まずEと移動点rhoを使って、先頭中央三次g_sを指定する。
その後、F_2Z(V_0)=kを使うと低次補正の9未知数に単元minorがある。
一般fiberでの存在と特殊fiberでの一意性を組み合わせれば、極を導入せず持ち上げられる。
これは全中央三次を一括して中心束のrank一定とみなす誤りを避ける方法である。

一般中心値DのH3性はV⊗_{F[G]}F(G)という中心局所化で証明できる。
有限PI次数を横断する全係数のH3開性と混同しない。
数値D=5に対する明示的な有理積分は中心性・平坦性まで確認しており、一般uのH3性は未判定。
Dを独立な超越変数にすれば中心局所化の議論が使える。

## 4. HH計算で保持すべき区別

一般点の中心Cと分岐Dは滑らか、D=-K_C。局所orderはk[[s,w]]⋊mu3。
非恒等sectorは法線の非自明指標のためHH cohomologyへの寄与が消える。
恒等sectorを粗空間へ押すとO_C、T_C(-logD)、O_Cとなる。
H^1(T_C(-logD))=7、H^0(O_C)=1、他の正の障害項は零。
従ってHH²=8、HH³=0。Hochschild homologyのtwisted sectorと混同しない。
Brauer捩れ付き圏を無条件に非捩れroot stackと同一視しない。
局所Moritaと層の貼合せによる証明を使い、root stackのn=2限定公式をn=3へ転用しない。

## 5. 厳密計算の意味

witness A: a=b=c=0, central coefficients(2,1,2,3,5)。
affine中心特異点idealはQ(q)上で(1)、境界Delta170、beta gamma delta6。
ポテンシャル20係数と中心元20係数に対し105×40行列rank18、核22。
12 affine座標方向+potential scalar+cut scalarのrank14を直接確認。
既知7方向とのspanはrank21、横断Phi'=x³+2y³+3z³+2xyzを加えて22。
「105式あるから余次元105」などの単純な方程式数の議論は無効。

witness B: Phi_u=(1+2u)xyz-qxzy+u(x³+8y³+27z³)-(x²+y²+z²)/2。
中央三次元の有理係数は `transverse_rains_lift_certificate.json` に収録。
正則なu0極限は2Omega+X+8Y+27Z+D。三交換子をQ(q)(u)上で厳密に零へ還元した。
有限標本からの補間・外挿ではない。

一般の121語の大きな有理行列を直接逆転すると式が膨張する。
現在の再現コードは書換え依存グラフの強連結成分に分け、最大12×12ブロックを多項式分母付きで解く。
失敗した重複実装や作業ログは同梱せず、この有効な実装だけを残す。

## 6. 文献確認と未確認点

- Chekhov--Mazzocco--Rubtsov: Adv. Math. 376 (2021), 107442, DOI 10.1016/j.aim.2020.107442、arXiv:1905.02772。一般化Sklyanin--Painlevé代数・PBW/Koszul・量子del Pezzoの関連を公表要旨で確認した。全文の定理単位の照合、七次元パラメータの厳密な比較、五節点因子の新規性判定は未実施。研究比較は`research/fricke_daha_comparison.md`。
- Etingof--Ginzburg: arXiv:0709.3593v4, Theorem3.3.2(i),(ii), Appendix9.1。
  一次本文を確認。今回のRains式は規約変換後に原関係でも独立検証した。
- Negron--Schedler: arXiv:1809.08715, Theorem1.1, AppendixA。
  固定部分のdet normalと局所から大域のspectral sequenceを確認。
- Faber--Ingalls--Okawa--Satriano: arXiv:2206.13359v2, Theorem1.5, Corollary1.7。
  smooth tame orderと捩れ付きstacky曲面の比較として使う。非捩れ同値とはしない。
- Fu--Porta--Scherotzke--Sibilla: arXiv:2509.00501v3 (2026-01-20), Proposition6.17。
  一般root stackのHH恒等sectorへの帰着と比較した。n=2限定の後半は利用しない。
- Rains: arXiv:2107.13540v2 (2022-02-17), Props2.2,2.3, Example2.1, §6末尾。
  次数3の全パラメータ被覆は論文の証明済み結論として使わない。
- De Deken--Lowen: J. Noncommut. Geom. 5 (2011), 477–505, DOI 10.4171/JNCG/83。
  Theorem4.5とProposition4.6、pp.495–496をEMSの一次本文で確認。Z-generating列のExt1,2消滅を照合。
  一般のGrothendieck変形に関するProp5.5/5.8/5.9は使用し、geometric helix/有限例外列に限定した定理は使用しない。
- Stacks Project Tag0BDK: perfect複体のfiberが一つの次数の自由加群である条件。
  Artin局所版は最小自由複体を使い本文で直接証明。
- Lowen--Van den Bergh: arXiv:math/0405227、Lowen: arXiv:0707.2602。
  abelian deformationのHH障害理論、exceptional object持上げの根拠。

PDF一次資料の抽出本文を使用した。web screenshot取得はキャッシュエラーで成功していない。
今回の新規PDFはローカルでレンダリングして点検した。
新規性の網羅的な調査、全H3原稿の独立査読は未了。

## 7. 大域成分の完全決定に必要なもの

現在の成分定理 `thm:conditional-component` は相対モジュライ比較仮定付きである。
条件(2)の単射性は次節の適合したenhanced Abel変形の範囲で解決したが、他の条件は未完成。
形式圏変形の正則8次元性だけから、全H3の代数性・全境界の分類は出ない。
E6型のweighted projective/Weyl商が候補だが、境界のH3必要十分条件と全群oidを証明するまで同一視しない。
次の作業は研究方針§IVを読む。

## 8. Artin再構成の現在有効な要点

証明は `papers/sections/quantum_cubic_artin_reconstruction.tex`、主論文第8節へ組込む。
E_i=pi R(i)についてj>=iならExt^{>0}(E_i,E_j)=0。AS-CM性でH1が消え、
H2はR_{i-j-1}の双対なので消える。全E_iはexceptionalでAZ ampleなZ列となる。
De Deken--Lowen Theorem4.5をGrothendieck圏Ind(qgr R)へ適用して、
有向Z代数のflat線型変形とflat Abel変形の同値を得る。

適合したenhancementの意味：持ち上げたE_iがperfect、derived Homが底上perfectで底変更に適合する。
特殊fiberで恒等なMorita同値があれば、各exceptional E_iの持上げはExt1=Ext2=0により同型類として一意。
各iの同型を選んで正方向Homと合成を同定し、Z代数再構成によりpointed exact同値を得る。
これは全Artin底での同型類の単射性であり、与えたMorita同値自体のt-exact性や群oidの充満忠実性ではない。
無限列を有限完全例外列に置き換えない。一般dg変形のheart存在も別問題である。

smooth proper dg変形と底変更に適合する相対Serre作用の下で、
P_n=RHom(E_A,tau_A^n E_A)はperfectかつ特殊fiberがR_n[0]。
最小自由複体の議論によりP_nは有限自由加群の次数0集中となる。
乗法の余核を次数ごとにNakayamaで消して一次生成を得る。
T(A^4)からR_Aへの核I_nは有限自由で特殊fiberと可換。
I2の六基底とI3の三次生成元を持ち上げ、各次数のI_n/J_nへNakayamaを適用すると全関係を生成する。
有限m-adic filtrationにより左右noetherian性も従う。

残る障害：この証明は二次包絡B_Aのflat性・AS4性を含まない。
三次関係の両側イデアル生成と正則正規な左右主イデアル生成を区別する。
主張の状態を強めるには三次syzygyと高次Koszul複体の持上げを実証する必要がある。


## 9. 二次包絡の四係数障害と平坦性後の正規性

`papers/sections/quantum_cubic_quadratic_obstruction.tex` に通常の証明を置く。R_A flatならI2rank6,I3rank45。六二次関係の左右挿入45×48行列は特殊fiberでrank44なので単元44minorがあり、Schur補行は1×4の(o1,o2,o3,o4)。従ってB_A,3 = A^19 ⊕ A/(o_i)、三次flat性は四係数零と同値。障害idealはFitt0(I3/(VI2+I2V))なので基底非依存・底変更に適合する。全次数flat性を別途仮定すると、B_A→R_Aの核の各次数は自由でrank B0,n−3、G0の持上げによる左右乗法は特殊fiberで同型、従って全次数で同型。三次核は自動的に左右正則正規主イデアルとなる。

量子so3点の四変数斉次表示の曖昧語zyx,tyx,tzx,tzyについて、20巡回potential方向それぞれの一次overlapをQ(q),q²+q+1=0上で全80件計算し零を確認した。`verify_cubic_obstruction.py` と小証明書に再生。これは指定方向での三次障害の一次項の消滅であり、全intrinsic変形、高次障害、全次数flat性をこの有限検算だけから結論しない。成分研究の次の核心は、この四係数の全Artin底での消滅と高次Koszul認識である。


## 10. 指定potential chartの全Artin包絡認識

`thm:artin-potential-envelope` は平方零制限なしに、量子so3点の任意の次数≤3巡回potential変形の斉次包絡を全次数flatとする。中央tを係数とする自由dg代数Dをx_i (内部1,homol0)、xi_i (2,1)、zeta (3,2)、d xi_i=cyclic derivative、d zeta=Σ[x_i,xi_i]で定める。各内部次数は有界有限自由A複体。特殊fiberでt0商はCY量子3spaceの標準potential dg代数で正次数acyclic。外部入力は一次資料EG arXiv0709.3593v4 §7.1 (7.1.4)、同箇所のGinzburg Thm5.3.1引用。本文§7.1–7.3の定義・仮定・証明を今回確認した。t乗法の複体短完全列と内部次数の下有界性から特殊fiber Dもacyclic、H0,nの次元binomial(n+3,3)。perfect複体のArtin最小模型により任意底でH0,n自由となり、任意Artin底変更に適合する。bar複体と特殊fiberのKoszul性から相対14641解消と双対性。有限m-adic filtrationから左右noetherian。中央gが持ち上がるなら分裂単射により商もflat。

これは一般R_Aの二次包絡を無条件に認識する定理ではない。全intrinsic/Abel/dg変形のpotential chartによる被覆、全8方向同時の中央三次持上げ、相対H3性・代数化は未解決。
全Artin底での三次flat性は、別の有限行列証明もある。六関係c_i=[t,x_i],r_i=∂_i Phi^hに対し、三つの[t,r_i]展開syzygyと巡回Euler syzygyが厳密に持ち上がる。特殊fiberで64×48挿入行列rank44、四syzygy48×4rank4。単元44minorのSchur補行列は四syzygyの残り4×4可逆部分により零となる。`verify_universal_cubic_syzygies.py` は打切りなしの20係数多項式環で全四恒等式を検証する。

次は中央incidenceの二次障害：一次8方向の全対について、重なりの解消済み乗法を二次まで展開し、105×40行列Mの余核に二次交換子を射影する。全対で零か、8変数同時積分を妨げる条件が出るかを調べる。全intrinsic被覆とはなお区別する。


## 11. 全八方向の二次中心incidence

`verify_second_order_incidence.py` は一次の七既知方向と一横断方向を取り、36個の二次monomial全てについて中心交換子の二次障害を求める。105×40のMと105×36のQでrank(M|-Q)=rankM=18。二次補正Hを厳密に解き、**補正後の元関係から**三つの中心交換子の次数0,1,2を再計算して全て零を確認した。一般のpotential変形では逆順語係数行列Aも動くため、B2=−A0^-1(C2+A1B1+A2B0)を使う。一次でbase-normalizeしたδ規則だけを再使用する誤りを避ける。

従って8変数m³=0の同時potential・中央三次族が構成され、全Artin包絡定理から包絡も三次商も全次数flat。証明は `prop:eight-second-order`、八方向と二次補正の小証明書は `second_order_incidence_certificate.json`。二次jetの存在を全次数形式積分、H3相対認識、全intrinsic被覆や成分の完成としない。
次は、低次jetを無制限に増やすだけでなく、中央三次incidenceの特異点を解消する明示的chartを構成する。generic中心三次のRains式の三捩れ極限を、cut先頭係数と横断パラメータの多変数族へ拡張する方針が有望。EG Theorem3.4.4/3.4.5はgeneric仮定を持ち、三捩れ点の全intrinsic被覆へ無条件に適用しない。


## 12. 八変数同時形式族と表示incidenceの形式的滑らかさ

証明は `papers/sections/quantum_cubic_multivariate_formal_chart.tex`。EG arXiv0709.3593v4 Appendix9.1 p35のY一次係数内のQ³*b2は余分なb2を除きQ³へ修正する必要がある。PDF原本画像も確認した。`verify_rains_central_formula.py` は修正式を全係数QQ(Q,T)[a1,b1,c1,a2,b2,c2]上で元関係102挿入・三交換子により独立検証。印刷式との差−TQ³b2(b2−1)Yが非中央であることも全係数で確認。従来のb2=0特殊化は影響を受けない。

p=1+kappa*lambda、Q=q0/p,T=−3lambda*eta*zeta/p、a1=−eta*zeta/p,b1=−zeta/(eta*p),c1=−eta/(zeta*p)、a2=−eta*zeta*a/p,b2=−zeta*b/p,c2=−eta*c/p、X=x,Y=eta*y,Z=zeta*zを代入する。potentialはp xyz−q0 xzy+lambda(x³+eta³y³+zeta³z³)−(x²+y²+z²)/2−ax−by−cz。修正Rains式の正規形をNとすると、非定数係数は全てlambda²で割れ、N_x³/lambda²のlambda0値は9eta²zeta²(1+q0)で単元。**G=(N−N_constant)/N_x³+D** は共通lambda²を除いて正則な明示的有理式である。
`verify_central_multivariate_lift.py` は各低次係数単項式で(Q−q0,T)の0,1jetが零であること、二次の全先頭式を検証し、G0=kappa*Omega(a,b,c)+X+eta³Y+zeta³Z+Dを得る。単なるjetの外挿ではなく、一般中心恒等式と厳密なイデアル二乗所属により全次数同時形式持上げとなる。全Artin包絡定理により包絡・商はflat。

eta0³2,zeta0³3,kappa0=2,D0=5で、七既知方向に加えlambda方向potentialがx³+2y³+3z³+2xyzとなり既存の横断方向に一致する。14座標方向を加えた形式22変数写像はincidenceの接空間上同型。embedding dimension22の完備局所環への冪級数環全射と、形式22変数族への写像の合成が形式自己同型となるので、incidence自体が形式smooth22次元である。恒等近傍の14次元gaugeを除いた形式sliceは8変数。有限の特殊fiber自己同型を含む全群oid、全intrinsic変形の被覆とは別である。

次の核心は相対qgrのH3認識：この全次数flat・相対AS4・中央正則三次商の形式族が、smooth proper enhancement、heart、逆Serre、相対exceptional構造対象とAZ列を持つことを証明する。その後、既存の全Artin単射性とHH2dim8/HH3zeroを使い、全intrinsic形式変形への被覆を比較する。単に表示incidenceがsmooth8であるだけでは大域H3成分の決定ではない。


## 13. qgr enhancement・逆Serre認識と一形式近傍の全Artin分類

`papers/sections/quantum_cubic_artin_enhancement.tex` に通常の証明を追加した。特殊fiberのcompact圏がsmooth properであることは既存の滑らかな中心・楕円分岐order同定を仮定する。De Deken–Lowen原論文（doi10.4171/JNCG/83）Prop4.4/Thm4.5/Prop4.6およびProp5.5/5.8/5.9をpp495–500で今回確認した。後二つは一般のGrothendieck圏変形に関する命題で、geometric helixを必要としない。flat graded R_Aの付随Z代数からflat Abel変形QGrR_Aを得、ample列O(i)のflat持上げはcompactに生成する。特殊fiberの有限generatorがこの列の有限部分の厚い閉包に入ることから有限直和generatorを持ち上げる。derived Homのfiberは元の有限次元Hom、Artin最小複体によりA-perfect。dgEndのsmooth性は「derived fiberがcompactならcompact」の有限A-filtrationによる補題を対角へ適用して従う。任意のAbel変形でも同じ議論が適用でき、既存Artin単射性のenhancement仮定を満たす。

HH1=0により恒等自己同値の可逆bimodule持上げは対角と同型である。相対Serreの底変更と次数シフトTを比べるとtau_A*T_A^-1がこの状況にあり、tau_A≅T_A。従ってheart保存と反標準環R_Aのgraded認識を得る。構造対象の相対exceptionalityはperfect Homと特殊fiberk0から、AZ ampleはtails構成から、二次包絡はQ(R_A)=B_Aから従う。rank-one/TFは幾何学的fiber条件、非正則Artin底上の絶対大域次元や整域性の主張ではない。Zhang twistのH3不変性を使っていない。

`verify_potential_recovery.py` で20巡回potentialの勾配を関係商へ写す30×20行列rank19、kernel kPhi0、中央一次40×4行列rank3/kernel ktを確認。小拡大帰納によりpotentialは関係空間から単元倍まで一意、中央一次直線はAtだけ。pointed Abel同値はcanonicalRをgradedに保存するので、表示incidenceの同型はaffine座標と二スカラーのgaugeへ戻る。

この点の表示形式8変数族→Abel→dgの写像は全Artin底で同型類上単射。HH2dim8,HH3zeroの無障害miniversal底への接写像は次元から同型。形式逆写像定理で8変数族自体がversalとなり、全dg/pointed Abel変形を実現する。単射性からパラメータも一意。**選んだH3点の全Artin形式近傍の分類**はこれで得る（`thm:intrinsic-formal-eight`）。前提の局所order同定・HH計算・対象持上げ・DDLを明記する。全H3の大域分類、相対stack代数性、成分閉包、全境界と有限慣性の分類ではない。

次は形式近傍の結果を代数的H3開族へ移す。明示8変数有理係数族はあるが、形式smooth性からH3性のZariski開性を無条件に推論しない。相対有限generatorのdg模型と対角perfect性の代数化、または非可換Projの有限表示smoothness criterionを検証する。Artin代数化を適用するなら変形functorの有限提示・効果性の仮定を個別に確認する。大域境界はその後の別課題。


## 14. 有限型の平坦表示族と正規化した楕円境界

`papers/sections/quantum_cubic_algebraic_boundary.tex`。p=1+kappa*lambdaとしてeta*zeta*p*(p³+1)を可逆化すれば、斉次Sklyanin三係数(p,−q0,3lambda*eta*zeta)は二係数非零かつ立方非全一致となる。IS arXiv1601.00564v2 Theorem1.1/Cor6.1を一次本文で再確認した。CY3先頭環へのEG3.3.2(i)PBWと正則中央一次拡大LBSにより全fiberの包絡は同じAS4 Hilbert値。noetherian/domainについては標準AS3の既存入力を使用し、ISのHilbert計算だけから導かない。smooth reduced Jacobson底で各次数の表示行列rankが全fiber一定なので、同一の有限開部分上で全次数locally free。中心式の有限個の分母とN_x³/lambda²も可逆化すれば、中央三次商も次数別flat・任意底変更に適合する。これはH3全fiber認識ではない。

C=kappa+kappa²lambda+(kappa³/3+9eta³zeta³)lambda²、F=q0*p*(x³+eta³y³+zeta³z³)+Cxyz。点関係行列Mのdetは厳密に3lambda*F。DeltaE=C³+27p³eta³zeta³が非零ならF0はsmooth相対楕円曲線。lambda0ではDeltaE=kappa³+27eta³zeta³、指定点値170。lambda0のMはP2全体でrank2、graphはdiag(1,q0,q0²)、G0の多重線型化がq0^-1*F0に一致。`verify_algebraic_boundary.py`で全恒等式と三射影patchのrank条件を確認。

EG arXivv4のb2印刷係数は、著者サイトMAGMA（https://math.mit.edu/~etingof/delpezzocenter）で正しい形となっている。今回原本を取得確認し、既存 `verify_cubic_clifford_integration.py` も同じ正しい式を用いていることを確認した。今回の全係数再生は三捩れchartに正則な別の正常形での検証であり、新しい中心式の発見ではない。
次はこのF曲線とMのgraphから相対THCR境界を認識し、一般中心値のH3性を明示8変数族へ適用する。全パラメータのH3 admissibility、H3 locusのZariski開性、成分の大域閉包はなお未解決。


## 15. 相対THCR認識と幾何学的一般点H3

`thm:relative-THCR-boundary`。左右関係行列のdetは共に3lambda F。lambda0で両方rank2、projectiveE上のrank1閉部分をproper射影で除くと、左右kernelから相対自己同型sigmaと逆が構成される。THCRのLnは次数3nでH1zero、H0rank3nと底変更。base-point-free pencilと平面三次の二次関係不存在により次数1生成。S=B/(t)→THCRの全射を得る。

generic sigma³は恒等でない。`verify_boundary_graph.py` は有理section(0:zeta:−eta)をlambda1/2,kappa2,eta=zeta1で三反復し、第一座標が0から非零になることを厳密確認。これはgeneric恒等式を否定する一点反例であって、全fiber非三周期の標本外挿ではない。THCRの関数体skew Laurent埋込みから、sigma³非恒等なら中央次数3部分は零。従って中央Gbarの像はgenericに零、有限局所自由切断加群のtorsion-free性で全底へ延長。Hilbert値一致からR/(t)=THCR、任意底変更に適合する。正則中央列t,GとTHCR整域性から全幾何fiberのRも整域。H3 smoothnessとは別。

独立中心値Dのgenericfiberは、V_K⊗K[H] K(H)という中心局所化で有限globaldim。既存の中央smoothE境界認識により**明示八変数族の幾何学的一般点はH3**（`cor:eight-generic-H3`）。全数値Dや位数変動下の一様H3開性はまだ主張しない。

## 16. smooth DM八次元の代数的表示stack

`papers/sections/quantum_cubic_presentation_stack.tex`。全20potentialの次数2,3,4関係挿入行列について、Artin包絡flat性から期待rankを越すminorが局所m全冪に入り、Krull intersectionと係数空間の整域性から恒等的に零。期待rank minorを可逆化する共通開W上でB2/B3/B4がvector bundleとなる。この有限次数の開性を全次数AS4へ無条件に外挿しない。

W上の三次bundleから零を除き、Gの三交換子を四次bundleで零とする有限型incidence Zを作る。作用群Gamma=(GL3⋉Ga3)×Gm_Phi×Gm_Gは14次元。既存形式分類から指定点でZの完備局所環は22変数、従ってZはその点でsmooth22。明示代数的8族と作用からのGamma×U→Zは接写像同型なのでetale。作用の不変性でetale locus=Gamma×U'、像Z'は不変開。center1 rank3/potential recovery rank19も課せる。**[Z'/Gamma]はsmooth DM次元8、U'がetale全射atlas**。全fiberの包絡AS4・商domain・smoothE境界はsourceの証明から移る。

H3幾何学的対象間の全pointed exact矢は、canonicalRのgraded回復→中央一次tの保存→filtered affine同型→rank19でpotential scalar回復→三次kernel scalar回復によりGamma作用に一致する。共通次数スカラーはt1非斉次化で除去済み。これは幾何学的群oidの全矢の主張であり、H3 locusがZariski開であることや全intrinsic族のfpqc降下は未証明。表示stackの一般点H3と、指定点の全ArtinH3形式分類の両方を得たが、全H3成分の大域分類ではない。

次の具体的課題はこの有限型表示stack内のH3 admissibilityの全値判定。滑らかな楕円境界でaffine central quotientの有限globaldimへ帰着済みである。一般中心値だけでなく、悪い中心値と高次元有限表示・Morita局所模型を調べ、H3 locusのconstructibility/Zariski開性を証明するか、障害を見つける。幾何学的root条件やblowup六点との比較には証明済みの適用範囲を確認し、Rainsの次数3全被覆を未証明のまま輸入しない。

## 17. 固定包絡の結節中心H3因子（現在有効な結果）

中心三様体はP=Omega^3+f Omega^2-XYZ+e(X²+Y²+Z²)=0、f=(1-q)/3、e=-(2q+1)/9。既存固定包絡判定はcut超平面Hがdual Y*を避け、Delta≠0ならH3とする。五つの通常二重点p0, p_eta（符号積+1）を通る切断条件L_iは線型独立で、中心のsingular locus in H3 = U∩(L0∪⋃L_eta)。五つはU上の非空既約SNC因子、A4商ではp0側と四符号点の軌道側の二つの既約因子となる。証明・対象範囲は主論文`thm:nodal-divisors`。

検証可能な非空性witness：a=b=c=0、G_D=2Omega+X+2Y+3Z+D、D∈{0}∪{4f/3−2e(eta1+2eta2+3eta3): eta1eta2eta3=1}。いずれも境界Delta=170で、各DのJacobi idealは対応p_iの極大イデアル、三変数Hessian detは非零。従って中心は孤立A1一つ。既存固定包絡H3 criterionを適用すると五例ともH3かつpointed exactで互いに非同型。`computations/verify_nodal_cuts.py`をSymPy/Q(sqrt(-3))で実行し`nodal_cuts_certificate.json`を生成。通常の数学的入力である固定包絡H3 criterionそのものの有限globaldim証明はこのプログラムの検証対象外。

七次元PBW族での結合：一次元表現から(a,b,c)=((1-q)yz-x,(1-q)zx-y,(1-q)xy-z)を得る。原点fiberは(x,y,z)=0と4つの符号解(eta1,eta2,eta3)/(1-q)、Jacobian detは-1,4,4,4,4。三二次式のP3斉次化では無限遠に3つの定数座標頂点があり、原点fiberの全8点は単純。有限etale次数8の射影解schemeから無限遠の3 sectionを除いて次数5のE→A'を得る。EはA3_xyzの開部分なので既約・連結。中心P_a及びそのX,Y,Z,Omega偏微分はこのE上で全係数恒等的に零（`verify_character_node_cover.py`で厳密確認）。中心三様体の五ODPの相対持上げとなる。節点を通るcutを添字付けるP3束はE上既約次元6、有限像はA'×P4の既約因子。固定位数3 H3開集合との交わりも非空既約、七次元族の結節中心因子はA4商で一つになる。主論文`thm:seven-nodal-irreducible`に幾何学的証明を記す。これはH3全体の特異中心軌跡の記述でも、八次元intrinsic成分の大域因子でもない。

意味：中心の特異判別式はH3モジュライの境界とは一致しない。次の問題はこの既約因子を八次元の表示stack・intrinsic H3族へ追跡することであり、全大域成分の既約閉包とH3開性は未解決。古典的な結節三次三様体の文献との新規性比較は未完了。

## 18. DAHA・character variety・skein・mirrorへの有効な接続

固定q（三乗根）の量子so3を V_{abc} とすると、普遍AWのTerwilliger規約で A_aw=(1-q)x, B_aw=(1-q)y, C_aw=(1-q)z, 中央三元 alpha_aw=(1-q)a 等。**Casimirの厳密定数** Omega_aw=q(1-q)^3 Omega=3(q+2)Omega。従って切断Omega=-DはAW四中心パラメータ同時特殊化。証明は主論文 `thm:aw-casimir-exact`、厳密計算 `verify_daha_character.py`。

中心P=0にOmega=-Dを入れて $u=-X/e,v=-Y/e,w=-Z/e$ とすると Fricke cubic u²+v²+w²+uvw+Au+Bv+Cw+T=0。A=-(Da+ell_a)/e² 等、T=-(D³-fD²+DK-L)/e³。係数写像Jacobianはa=b=c=0で 3D(D-2f/3)^4/e^9。Goldman四穴球面のトレースパラメータからFricke係数へのJacobianは(1,2,3,4)で-200。両者がgenerically finite dominantなのでgeneric有限etale底変更で**中心**を四穴球面相対SL2 character varietyに同定する（`thm:fricke-trace-dominant`）。量子代数全体とcharacter **stack** の同型ではない。

Terwilligerのbraid生成元 sigma は (a,b,c)↔(b,a,c)、x↔y、z→(q²-q)xy-q²z+qc、Omega不変。中心で X↔Y、Z→(XY+cOmega-ell_c)/e-Z、Frickeで (u,v,w;A,B,C,T)→(v,u,-uv-C-w;B,A,C,T)。元関係を用いたPBWの全係数恒等式を別コード `verify_daha_braid.py` で独立再現。Jacobian括弧 {u,v}=2w+uv+C 等はGoldmanのPoisson括弧と定数・符号を除いて同型、sigmaはPoisson。滑らかなFricke中心の射影閉包は反標準三角形を持つLooijenga pairであり、四穴球面skeinのBousseau mirrorとの比較対象となる。

先行研究・課題の具体表は `research/fricke_daha_comparison.md`。四穴球面skein=普遍AW同型（Crampé等）、rank-one DAHA embedding（Terwilliger）、Racah $U_q(sl2)$、Hikami cluster、Bousseau mirror、Painlevé、EOR E6-GDAHAの各適用範囲を分ける。**残課題**：root-of-unityでのskein/DAHA mapのspecialization、Casimir切断のH3性（一般の三角境界切断の滑らかH3条件とは別）、Brown--Gordon Poisson orderがGoldman bracketになるか、量子的VietaのH3心への延長、D4 triangleからE6 ellipticの相対変形。各個別式の文献新規性は未判定。原稿section `sec:daha-character`、二つの小JSON証明書を参照。

Goldman--Toledo (arXiv:1006.3838) は無限遠が一般tritangent planeである任意の三次曲面を四穴球面character varietyとして実現するので、Fricke cubicへの同型自体は新規ではない。Schock, Math. Nachr. 297 (2024), 2639--2666, §2 は三角形付き三次曲面の直交D4根格子をNaruki--Looijengaの既知構造として記載する。六点blow-upで境界D_i=H-E_(2i-1)-E_(2i)、直交root基底H-E1-E3-E5, E1-E2, E3-E4, E5-E6を得、そのGramが負Cartan D4である。K^perp=E6(-1)。独立整数格子計算は `computations/verify_d4_lattice.py`；主論文命題`prop:d4-inside-e6`。これがD4 DAHA・Fricke側とE6 del Pezzo側を同じPicard格子で結ぶ具体的な古典幾何であり、量子/圏的同値の証明ではない。


## 相対Poisson臨界被覆と$S_5$の現在有効な定理

一般a,b,cに対するPoisson臨界schemeの全域有限平坦次数15、一次元表現schemeの次数5、臨界値多項式の恒等式Delta15=N5²M5、N5の既約性とGalois/幾何monodromy S5を主論文 `papers/sections/quantum_cubic_relative_poisson.tex` に証明した。元のPoisson括弧と全中心は `papers/sections/quantum_cubic_poisson_orders.tex` を参照する。研究再開用の具体式・H3適用限界・未解決のM5は `research/poisson_order_notes.md` §6を参照する。重要：一般a,b,cでの全H3判定、一般8次元楕円境界での中心の形成、M5のmonodromyは未解決。再現コード `computations/verify_relative_poisson_cover.py` と小証明書 `relative_poisson_cover_certificate.json` を保持。Library重複保存は禁止。

## 現行のCasimir Poisson葉とH3判定への接続

Poisson量子化・十零点・CasimirのH3可否・VietaのS4対称性についての有効な証明・計算は主論文 `papers/sections/quantum_cubic_poisson_orders.tex`, `papers/sections/quantum_cubic_casimir_leaves.tex` に統合した。規約、具体的障害と次の研究は `research/poisson_order_notes.md` §1–5を参照する。総中心の五節点から生じるCasimirのA1切断はH3、滑らかな総中心のCasimir臨界点で生じるA1切断は非H3（既存H3定理への依存あり）。一般a,b,cや八次元intrinsic族への拡張は未完成。個別公式の既出性は未確認。
