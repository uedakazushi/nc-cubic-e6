# 周期に見えない境界力学とPell成長

2026-11-17 / e6-connections-v25。再開時は `../00_research_plan.md` を先に読む。
完全な証明は主論文が入力する `../papers/sections/quantum_cubic_boundary_dynamics.tex`。前提のH2恒等性とentropyは `quantum_cubic_triality_isogeny.tex` の `prop:period-invisible-entropy`。本ノートは現在有効な式、注意、再開課題だけを保持する。

## 1. 同じ自己同型を二つの場所で観測する

滑らかなU={uvw−(u²+v²+w²)/2−Au−Bv−Cw=h}、通常の三次閉包S、三角境界D=D_u+D_v+D_w。g=iota_v iota_w iota_u iota_w（右から合成）。各Vietaは該当座標を2*(他二座標の積)−元座標−2*(対応係数)へ移す。
Goldman–Neumannの既知のホモロジー定理から、gはH2(U,Z)で恒等、留数形式と全periodを保つ。これは今回全独立再監査したものではなく、既存原稿への依存である。
今回の対象は境界の単項式付値。ここではgが無限軌道と無理固有方向を持ち、極次数は指数増大する。periodの分類・有理Hodge同型と、開曲面上の力学の検出は別の課題である。

## 2. 境界付値の正確な模型

u頂点の局所式からT=2VZ*unit。重みnu(V)=alpha, nu(Z)=betaの座標極次数は(alpha+beta,beta,alpha)。三頂点を貼ると
C={(a,b,c)≥0, 2max(a,b,c)=a+b+c}\{0}。
Theta(r,t)=(|r|,|t|,|r+t|)により(R²\{0})/±と同定。軸は元の境界成分のgeneric divisorial valuation、有理方向はcorner blow-upで抽出可能なdivisorの方向。

Vietaの作用はT_u=(2max(b,c)−a,b,c)と巡回式。重要な恒等式は
u_coordinate * iota_u(u_coordinate)=v²+w²+2Bv+2Cw+2h。
多項式式2vw−u−2Aに単純maxを適用すると最大錐で先頭項の消去を見落とす。積表示の右辺で同重みでも二つの平方は別のLaurent単項式なので、単項式付値で消えない。
Theta上の三行列はRu=[[-1,-2],[0,1]], Rv=[[1,0],[-2,-1]], Rw=diag(1,-1)。積Rv Rw Ru Rw=−M、M=[[1,-2],[-2,5]]。同時符号商ではMと同じ。全係数に独立。

## 3. 最小次数と射影交点次数は違う

deg_Uは座標環の元を表す多項式の最小全次数。N=[[1,2],[2,5]]、(p_n,q_n)=N^n(1,1)。n≥1にg^nの三座標の最小次数は(p_n,q_n,q_n−p_n)。
一回の最高項は4uv²,64u²v⁵,8uv³。全反復の最高項もu,vのみの単項式で、係数2^(degree−1)。gr O(U)=C[u,v,w]/(uvw)だから曲面関係で次数を下げられない。本文では最高項の全n帰納法を示す。
d_n=q_nは1,7,41,239,1393,8119,...、d_(n+2)=6d_(n+1)−d_n。
M^n=[[a_n,-b_n],[-b_n,c_n]]ならd_n=b_n+c_n、d_n²−2c_n²=−1、d_n+c_n sqrt2=(1+sqrt2)^(2n+1)。

H=[D]=O_S(1)についてn≥1に
(g^n)^*H=c_nD_u+b_nD_v+(b_n+c_n)D_w、H·(g^n)^*H=2d_n。
これはgeneric hyperplaneの引戻しの極因子からの**divisor class**の計算で、gがS上のmorphismであるという意味ではない。n=0ではH²=3なので2d0を適用しない。
両次数の指数率は3+2sqrt2で、既存Cantat–Lorayのdynamical degreeと整合する。

## 4. 二次無理固有付値と非正則化

拡大固有線は(r,t)=(1,−1−sqrt2)、縮小は(1,−1+sqrt2)。極次数ではv_+=(1,1+sqrt2,sqrt2)、v_-=(1,sqrt2−1,sqrt2)。g_*はそれぞれLambda=3+2sqrt2、Lambda^-1倍する。射影境界はnorth–south型で有理方向に周期点がない。
有限境界point blow-up後も元のD_iのstrict transformは残る。正則自己同型なら有限個の境界成分を置換するため、その付値は周期的となり矛盾。従って**指定したSを支配する有限境界blow-up**上へ正則自己同型として延長できない。
この結論を、全く別のコンパクト化の不存在やalgebraic stabilityの不存在へ拡張しない。境界の滑らかな点のblow-upを混ぜても上の矛盾は有効。

## 5. 個別付値の抽出深さ

nu_n=g_*^n ord(D_w)の極次数は(3,7,4),(17,41,24),(99,239,140),...。n≥1の中心はv頂点で、局所原始重みは(p_n,q_n−p_n)。
(q_n−p_n)/p_n=[1; 2,...,2,3]、2は2n−2個。subtractive Euclidで付値中心を追い、終端(1,1)で最後に一回blow-upするため、最小corner回数は部分商の和**4n**。
これは一つの指定されたdivisorial valuationを抽出する回数であり、g^nの全indeterminacyを解消する総回数ではない。
係数不変な境界力学、Pell単数、連分数の周期性は同じ整数行列から生じる。新たな算術同値を示したのではない。

## 6. 一次文献と新規性の範囲

- S. u. Jang, *Tropical Dynamics of Markov Surfaces*, arXiv:2306.11357v2, https://arxiv.org/abs/2306.11357v2 。取得したPDFは2025年12月版。Lemma4.8のR²/±との共役、Theorem4.10のholomorphic coefficientの場合を本文数式で確認。本稿のThetaと一般tropical反射の構造は先行研究に既にある。新しい一般tropical化定理とはしない。別版の題名 *Vieta Involutions on Tropical Markov Cubics* と節番号を混在させない。
- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier59 (2009),2927–2978, DOI https://doi.org/10.5802/aif.2512 。出版版§3.1の境界幾何を確認。
- 同著者長稿 *Holomorphic dynamics, Painlevé VI equation and character varieties*, https://perso.univ-rennes1.fr/serge.cantat/Articles/painleve_long.pdf 、§4.2 Remark4.5で境界節点の反復blow-upと円周作用を確認。出版版と節番号が違う点に注意。今回web screenshotは複数のURLでcache missとなり未取得。解析テキストの式と独立記号計算を比較し、図の解釈には依存していない。

境界力学・entropy・一般線型化は既知。本稿の役割はperiodの核にある特定語について、最小次数・射影交点次数・抽出深さを区別し、非正則化の範囲を明示すること。個別公式の文献新規性は網羅確認未了。

## 7. 再現と次の問題

`computations/verify_boundary_pell_dynamics.py` を今回厳密実行しPASS。全係数Vieta式、12 chamberの36線型恒等式、n=24までの整数行列・Pell式・連分数、固有方向を検算。証明書は同ディレクトリの `boundary_pell_dynamics_certificate.json`。全nの主張は本文の帰納法による。付値空間・引戻し・非正則化の通常証明を有限計算による形式検証と呼ばない。
新節は日本語LuaLaTeXで4頁、全頁を画像点検し、未解決内部参照・overfullがないことを確認。主論文全体の今回の再組版、旧29検証器の全再実行、旧証明の独立査読は未実施。
次は、一Vietaの局所corner変換とwrapped対象・非可換局所化の対象の像を比較する。古典entropyから圏的entropyを推測で結論しない。一般語の連分数と抽出深さの研究、三成分のperiod isogenyの幾何学的実現も並行して保持する。
GitHub mainが正本。pushした内容をLibraryへ保存しない。
