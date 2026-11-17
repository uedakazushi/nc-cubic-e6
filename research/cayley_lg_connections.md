# Cayley・Landau–Ginzburg・D4・pillowcaseの接続

2026-11-17 / e6-connections-v19。再開時は `../00_research_plan.md` を先に読む。
完全な証明は主論文から読む `../papers/sections/quantum_cubic_cayley_lg.tex`。本ノートは具体式、概念の区別、比較対象、次の着手を整理し、論文の証明を重複させない。

## 1. 共通の模型と三種類の空間

正規化u=(1-q)x等、A=(1-q)a等により、一次元表現の係数写像は

Phi(u,v,w)=(vw-u,wu-v,uv-w)=grad H,
H=uvw−(u²+v²+w²)/2.

一次元表現の総空間E=A3_{u,v,w}、その係数底S=A3_{A,B,C}、元の非可換代数の中心Y=Spec k[X,Y,Z,Omega]/Pは異なる。特に本ノートのA,B,CはFricke方程式の三係数ではなく、u,v,wは中心生成元ではない。

W_{A,B,C}=H−Au−Bv−Cw の臨界スキームはE→Sそのもの。既存の有限平坦次数5定理によりJacobi代数はrank5。graph(dH)はT* A3内のexact Lagrangianで、余接座標への射影がPhi。これをLG模型と呼ぶことは、非可換三次曲面とのmirror同値やtamenessを証明したという意味ではない。

## 2. Cayley曲面の新しい出現箇所

Hessian J=[[-1,w,v],[w,-1,u],[v,u,-1]]、det J=R=u²+v²+w²+2uvw−1。
したがってramification divisor R=0はCayley三次曲面。変数x=-2u等でx²+y²+z²−xyz−4=0となる。

トーラス表示：
u=−(r+r^-1)/2、v=−(t+t^-1)/2、w=−(rt+(rt)^-1)/2。
同時反転(r,t)↦(r^-1,t^-1)の不変環を使うと、R=0は(Gm)²/±、すなわち閉トーラスのSL2粗指標多様体。四つのA1点はu,v,w=±1で積−1。これは、従来のFricke中心とは**別の場所で、表現被覆の内側に指標多様体が再出現する**ことを意味する。

トーラスの{r,t}=rtから{u,v}=−R_w/2（巡回）を厳密に得る。GL2(Z)の単項式作用はPGL2(Z)作用としてCayleyへ降り、det=1でPoisson、det=−1で反Poisson。
注意：この括弧と、元の量子代数の中心にあるroot-of-unity括弧9倍とは別の空間の構造。Cayleyのmodular作用がE→S全体へ延びるかは未証明。

## 3. D4の局所模型と三係数のversal性

Rの四節点sigma（±1、積−1）についてPhi(sigma)=−2sigma。fiberはsigmaに長さ4の局所部分、−2sigmaに長さ1の単純部分で4+1に分かれる。

代表点sigma=(-1,-1,-1)、底(A,B,C)=(2,2,2)で、
u=-1+x、v=-1+y、w=-1+ell-x-y、A=2+alpha等、L=ell-xy+gammaと置くと、正確に

W=−L²/2−xy(x+y)+x²y²/2−gamma xy−(alpha−gamma)x−(beta−gamma)y
  +7/2+alpha+beta+gamma+gamma²/2.

残ったg=-xy(x+y)+x²y²/2はD4 germ。局所Jacobi環は基底1,x,y,xyで、x²=y²=-2xy、x²y=xy²=0、Milnor数4。パラメータ微分の非定数類−x,−y,x+y−xyは独立なので、三係数が加法定数を除くミニバーサル変形。別sheet(-2sigma)でdet J=27。

巡回置換のHessian核上の作用は(x,y)↦(y,−x−y)、位数3で三枝を回す。D4 trialityとG2折り畳みの具体的な入口になる。ただしこの局所Milnor D4と、反標準三角形に直交するPicard D4の標準同定は未構成。W(D4)の作用、四臨界点の置換、既存のS5群を混同しない。

## 4. 留数対と判別式の二つの意味

係数原点ではE→Sはetale。fiberは0と四つの符号点eta（積+1）。Hessian determinantは−1,4,4,4,4なので

tau(h)=−h(0)+(1/4) sum_eta h(eta)

が非退化な対(h1,h2)=tau(h1h2)を与える。基底1,u,v,w,uvwの対のdetは−1。これは明示的なrank5 Frobenius代数である。primitive formやFrobenius多様体はまだ構成していない。

同じ原点でOmega_E=f(uvw−u²−v²−w²)/3の値は0と−2f/3（4回）。N5=D(D−2f/3)^4は重根を持つ。従ってDisc_D N5=0とE→Sのbranch locusは別物。
一般のtrace pairingに対し、power basis=(任意基底)Tならdisc(power basis)=(det T)²disc(任意基底)。det Tの消滅は「一つの観測量がsheetを区別しなくなる」現象を加える。

さらにWの臨界値は−2uvw+(u²+v²+w²)/2であり、Omega_Eと同じ関数ではない。LGのMaxwell locus（異なる臨界点の臨界値衝突）との比較では、この違いを最初に処理する必要がある。今後の判別式因子の探索は、branch・値衝突・Casimir切断の特異性を分けて行う。

## 5. 実型・elliptope・nearly Kähler

正規化した写像は実係数であり、その実型を考えられる。q自体が実数になるわけではない。
C=-Hess H=[[1,-w,-v],[-w,1,-u],[-v,-u,1]]の半正定値領域は符号変更した3-elliptope。det C=-R、境界はR=0と[-1,1]³の交わりである。
境界はr=e^(i theta),t=e^(i phi)のトーラス表示、すなわちSU2トーラスcharacter varietyのpillowcase。Gram行列で同じ記述が得られる。

内部ではHが厳密に凹、領域は凸。線分に沿ったHessian積分によりPhiは内部で単射。したがって任意の実係数に対し、この領域に入る実sheetは高々一つ。
Dixonは同じelliptopeをnearly Kähler S3×S3のmulti-moment像として記述する。この共通凸体は確立した比較だが、非可換曲面との圏同値・metric degeneration・同一fibrationは構成していない。

## 6. 先行研究と一次確認箇所

- S. Cantat, F. Loray, *Dynamics on Character Varieties and Malgrange irreducibility of Painlevé VI equation*, Ann. Inst. Fourier 59 (2009), 2927–2978, DOI https://doi.org/10.5802/aif.2512 。§1.5のCayley、トーラス商、modular作用を確認。対応するarXiv:0711.1579v2は別題 *Holomorphic dynamics, Painlevé VI equation and character varieties*、§1.5。webのPDF画像でも確認した。これらの古典的同型自体は本研究の新規結果ではない。
- M. Mikosz, A. Weber, *Triality, characteristic classes, D4 and G2 singularities*, J. Homotopy Relat. Struct. 10 (2015), 995–1011, DOI https://doi.org/10.1007/s40062-014-0094-3 。公開本文のProposition 3、§5でD4ミニバーサル変形、Jacobi基底とtrialityを確認。局所標準理論を本稿の明示germに適用する。
- K. Dixon, *The multi-moment maps of the nearly Kähler S3×S3*, Geom. Dedicata 200 (2019), 351–362, DOI https://doi.org/10.1007/s10711-018-0375-9 。公開本文Lemma 3.5と§3のelliptope/Cayley記述を確認。同じ凸体が現れることを使い、追加の圏的対応は主張しない。
- W. M. Goldman, W. D. Neumann, *Homological action of the modular group on some cubic moduli spaces*, arXiv:math/0402039 。一次本文のIntroductionを確認。一次穴トーラス・四穴球面の三次曲面とそのhomology作用の比較候補。ここでのD4消滅サイクルとの完全な対応は未確認。

新規性が未確認のまま、個別のCayley、D4、elliptopeを新発見とは呼ばない。本研究で得た価値は、同じ表現被覆の具体式による接続と、四sheet衝突・versal性・実単射性・判別式の区別を一緒に扱えることである。

## 7. 次に作る数学と検証状況

最も有望なのは局所D4 vanishing cycleとPicard D4を結ぶ対応、trialityの圏的実現、WとOmegaの二つの値写像の比較、Cayleyのmodular作用の被覆への延長である。大域消去計算を反復する前に、局所模型・交叉形式・構造対象の像・小さい反例を求める。
`computations/verify_cayley_lg_connections.py` は今回実行してPASS。全てQ上の記号計算。小証明書は `cayley_lg_connections_certificate.json`。不変環の全生成、解析的右同値、versal性の一般判定、凹性による単射性は本文の通常の証明。
新節のLuaLaTeX wrapperは5頁で組版成功。本文外の参照二つはwrapperにないため未解決であり、全主論文の組版成功とはしない。旧23検証器の全再実行・旧証明の再監査・独立査読・新規性の網羅調査は今回未実施。GitHub main保存後にLibraryへ重複保存しない。
