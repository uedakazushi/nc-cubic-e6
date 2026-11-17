# 研究方針：非可換三次曲面から広がる幾何学

2026-11-18 / e6-connections-v30。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎は `research/research_notes.md`、DAHA比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、LG/G2は `research/cayley_lg_connections.md`、全period/trialityは `research/conic_period_coordinates.md`。境界力学・link・局所化は `research/boundary_pell_dynamics.md`、閾値・解析modulus・MF・楕円/Prymは `research/boundary_analytic_moduli.md`。旧bundle・会話履歴を再開の前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先は数学的に面白くすること。優先戦略は、多様な話題との具体的な接続を見つけ、検証可能な数学へ育てること。** 意外な同型・共通構造、見通し、新しい問い・方法を重視し、名称や定理数を増やすことを目的にしない。
正確性を犠牲にせず、重要性、新規性、理解の深化、応用、実現可能性を総合して研究価値を最大化する。既定の分類の完遂が他の面白い接続より自動的に優先されるわけではない。重要な方針変更は現在の理由と元の目標の達成部分・残存部分を簡潔に記し、履歴を時系列に蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を示す。原稿中の証明、今回の点検、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。
先行研究を一次資料で確認し、Introductionで既知結果の範囲と本稿の貢献を比較する。未確認の内容・書誌・新規性を推測で補わない。文献PDFや検索結果を大量収録しない。
原稿は日本語LuaLaTeX。公表価値ある関連分野の結果も同じ主論文へ統合する。分割は数学的まとまりと公表上の利点で判断し、価値ある既存成果・必要証明を軽量化のために削除しない。
研究ノートは着想、補題、計算、反例、障害、文献比較、再取得困難な情報を保持する。日誌・会話・更新履歴・重複証明にせず、主論文に証明があれば参照する。
現行方針・ノート・論文と必要最小限の原稿、コード、入力、小証明書、再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・組版中間物は除くが、数学的内容と検証可能性を損なわない。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryに保存しない**。push失敗で未保存成果の保全が必要な場合だけ緊急退避できる。既存Libraryファイルを明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を別状態として報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行う。force push、不要なPR・Actionsを使わず、PDF・ZIPをGitで追跡しない。未実行をPASSと言わない。

## II. 現在の問いと研究選択

**同じ非可換三次曲面から回復される幾何を、実際の写像・作用・周期・局所模型で結ぶ。** 量子中心はFrickeへ、一次元表現はLG/Cayley/D4へ、対称LGはG2へつながる。周期、境界力学、局所特異点、圏のどの情報がどの不変量に残るかを比較する。
現在の中心は、境界の解析modulus K=kappa²と高重み情報である。重み付き模型のMFは(n,K)で分類され、同じlink・閾値・HH次元でも非同値。四点配置の二捩れ付き楕円曲線も同じKを記録する。
今回、その付随楕円曲線への**実際の有限写像**を、重み付きMilnor曲線の二次Kummer被覆から構成した。元の曲線では指定したzを保つ写像に平方類[x]の障害があり、sqrt(x)で正確に解消される。Prym内の有理Hodge因子、全n共通のCiani genus3中間曲線、楕円因子の超幾何方程式を得た。
実germのmu27,tau24と主部のtau27を区別する問題は、通常のZ-graded dg特異点圏についてHua–KellerのHH0=Tjurinaにより解決した。**strictな二周期MFの相対HH公式との全比較は未構成**であり、次数と基礎環を明記する。Prym構成を高重みの実germへ解析的に移すことも未解決。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆は現行原稿にある。全intrinsic H3の相対代数化・降下・大域境界は未完成で、他分野研究の前提にしない。
達成基準は、具体的写像、変形、局所模型、格子写像、圏的対応、障害、周期式を正確に与えること。型・名前・数値の一致だけで同一視しない。

## III. 主要な到達点と確実性

### A. 非可換変形とモジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の仮定を外さない。横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。接空間rank18、gauge14、商8。全Artin表示族・enhancement・smooth DM八次元表示stackを保持。一般非被約底のintrinsic降下・H3開性・全境界は未完成で、成分定理の相対比較仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般係数で既約六次元因子。中心特異性とH3境界は異なる。AW中央特殊化、Casimir規約、Fricke係数写像、量子的Vieta、D4⊂E6を明示。Q=q exp(hbar)の交換子は指定Goldman型括弧の9倍。Brown–Gordonを適用するが全DでのM3/Morita型は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaには障害があり、一般変形・心の変更は否定しない。十Poisson零点、四Casimir特異値、H3可否、二次接触／一次横断、S4作用を保持。
相対Poisson臨界環は有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。有限体計算と群論・基本群の証明は別。今回旧主張の独立再監査はしていない。

### C. LG・格子・全period・triality

一次元表現Phi=grad[uvw−(u²+v²+w²)/2]、Jacobi環rank5、exact Lagrangian graph。分岐源CayleyはトーラスSL2指標多様体。D4 miniversal、三枝巡回、留数対、elliptope/pillowcaseと内部実sheet一意性。
U=S\Dで0→Z delta_infty→H2(U,Z)→D^perp→0、右端D4(-1)、左端原始radical。指定退化のMilnor包含によるPicard整数比較、外部triality。全域標準分裂ではない。MHSは重み2の4方向と重み4の1方向。
G2実現のD4/A2二成分、成分交換と内部Hurwitz、Klein七点S7と表現像6048を区別。境界周期(2pi i)²、matching対数、Morseのarcsine周期、無限二面体のrank二解局所系、有理非分裂例を保持。
conic標識上の全四period=(z1/z2,z2/z3,z3/z4,z3*z4)、指定開集合で有理MHS分裂⇔全zi捩れ。W臨界値、Casimir値、被覆分岐は別。
対称Hurwitzホモロジー像は外側S3、pure braidは自明。period=(xi,eta,eta,eta)、格子指数3とtorus isogeny(xi,eta)→(xi,eta³)。Weyl商はBP三成分写像。共通開集合で有理MHS比較、Klein整数拡大位数7,21,21。全底の標準VMHS・曲面/導来同値ではない。

### D. 境界力学・局所化・二枝

g=iota_v iota_w iota_u iota_w、Lambda=3+2sqrt2、M=[[1,-2],[-2,5]]。
M^n=[[a,-b],[-b,c]]、d=b+c=1,7,41,...。境界Theta(r,t)=(|r|,|t|,|r+t|)、最小次数d、射影交点次数2d。無理固有付値、指定コンパクト化を支配する有限境界blow-up上の非正則化、個別付値抽出4n。algebraic stabilityの否定ではない。
アフィン引戻しDHKK h_t=0、射の極filtrationの歪み率log Lambda。閉包class cD_u+bD_v+dD_w、算術種数delta=1+2bc−d、proper対象列率2log Lambda。filtered HHとrank6のHPを区別。
条件kappa²≠1、N_v(kappa)≠0で境界はp_wの二枝、Puiseux(b,c)、交叉bc。最低面F_nk=y^(2b)−2kappa x^c y^b+x^(2c)、link T(2b,2c)、Milnor数(2b−1)(2c−1)、homology monodromy位数2bc。正規化と一点欠損の率log Lambda、2log Lambda。Chebyshev/Casals局所Weinstein模型は大域曲面や反復間の関手と未同定。

### E. 閾値・解析modulus・MF・level2楕円曲線

`subsec:boundary-thresholds-mf`, `sec:boundary-analytic-moduli`。
lct=(b+c)/(2bc)、0<tau<1の乗数イデアルはb(i+1)+c(j+1)>2bc tau。実境界MFのHH次元は(2b−1)(2c−1)、異なるnはMorita非同値。
二枝先頭比I=(r1+r2)²/(4r1r2)=kappa²は高重み項のある実germにも解析的不変量。
**重み付き模型**の二周期MF分類は(n,K)一致と同値。DyckerhoffのHHを代数として使い、Euler Jac=TjurinaとMather–Yauによる。通常Ext代数が同じでも高次A∞積に係数が現れる。一般高重みgermへの同じ証明の流用はしない。
四点0,infty,rho±の二重被覆E_k:eta²=z(z²−2kappa z+1)、T=(0,0)。K=kappa²はY0(2)粗modulus、j=64(4K−3)³/(K−1)。K0と9/8はj1728が同じでも模型MFは非同値。2isogeny K→K/(K−1)も一般にMF同値でない。
実例A=B=C=0,h=1、初期v=2,n=1はmu27,tau24。元のVietaからresultant、正則初期列socle26と重み31jetで厳密に確認。主部tau27へ接触非同値。今回の新コードでも独立再計算した。

### F. Kummer–Milnor被覆、Ciani、Prym、dg復元

新節 `papers/sections/quantum_cubic_boundary_prym.tex`、`sec:boundary-milnor-prym`。
CはF_nk=1の滑らかな射影模型。z=y^b/x^cについてz(z²−2kappa z+1)=x*(y^(b/2)/x^((3c+1)/2))²。xは2b個の単純零点を持つので非平方。**同じzを保つC→E_kはない**が、a²=xの連結二次被覆tildeCではz=y^b/a^(2c), eta=y^(b/2)/a^(3c)が次数2bcの写像qを与える。
g(C)=2bc−b−c、g(tildeC)=4bc−b−2c−1、Prym次元2bc−c−1。deckがEの逆元に対応し、q*EはPrymに入る。q*q*/(2bc)（正確な順序は本文のq^*q_*）が有理冪等射を与える。整数・偏極付き積分解は未主張。
全nで共通のCiani四次X4+Y4−2kappa X²Y²=Z4へ(X,Y)=(a^c,y^(b/2))、次数bc/2。Jac(Ciani)はEi²×D_kにisogenous、Eiはj1728、D_k:T²=r4−2kappa r²+1。PrymにEi×D_kの二次元部分が入る。D_k→E_kは(z,eta)=(r²,rT)の2isogenyで、既存level2対応を実際の商で実現する。
楕円周期は(kappa²−1)Pi''+2kappa Pi'+Pi/4=0。完全微分恒等式から証明し、Gauss超幾何(1/2,1/2;1)へ変換。kappa変動の周期であり、固定kappaのMilnor値monodromyやLGのh周期とは異なる。
Hua–Keller最終v6 Thm5.9の**通常Z-graded dg特異点圏**でHH0=Tjurina。実tau24と主部tau27はdg Morita非同値。実germで異なるKもこの圏が区別する。Z/2相対HH=Jacとの全忘却・periodization比較や、実germへのPrym移行を済ませたとはしない。

## IV. 次の優先課題と具体的着手

**第一優先：実germと主部の比較を、次数と追加構造を保って進める。**
Z-graded dg特異点圏の復元は適用できた。次はstrict二周期MFの相対HHと絶対Zdg HHの関係を、Hua–Keller、Dyckerhoff、periodizationの一次資料から具体化する。n=1でkappa,hの変動による厳密Tjurina跳躍とJacobian積を計算し、[f]と高重み変形がどこに残るかを調べる。tau差だけの議論を、基礎環・次数の違う圏へ流用しない。

**並行して優先：Prym因子を整数構造と変形へ進める。**
全n共通のCiani写像とnormを使い、楕円factorのpullback kernel・誘導偏極・整数格子を最初のb2,c5で求める。PFからkappa=±1,inftyのmonodromyを計算し、Kのlevel2標識との関係を調べる。Kummer被覆が最小なのは指定zを保つ平方根の意味であり、元のCから任意の楕円写像がないとは主張しない。
高重みの実germには解析的同型がないため、Prym因子が変形で残るか、極限Hodge構造・stable reductionでのみ現れるかを別問題として定式化する。isogeny因子を圏の部分圏やHMSへ飛躍させない。

**並行して優先：局所Weinsteinとfiltered mirror。**
局所MF、局所Weinstein、大域H3を分け、対象・End環・action filtrationを指定する。通常affine Perf entropyは零なので正値を再発見しようとしない。pole/actionの線型比較に加えて特定gへの同変性が必要。

**維持する課題：三成分Hodgeと非可換成分。**
trialityの3捩れperiod差、Klein7/21、N5/M5のbranchと値衝突を保持。Sklyanin方向のq障害相殺、Vietaの心の変更、全H3開性・降下・全境界も維持する。公表前には旧依存定理を独立監査する。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_boundary_prym.py
python3 computations/verify_all.py  # 全35検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回は新Prym検証器を実行しPASS。Q上のKummer/Ciani代入、楕円j/isogeny、指標射影、PF完全微分、整数Pell/種数式と、元のVietaからのmu27/tau24を再計算した。証明書は `computations/boundary_prym_certificate.json`。連結性・Riemann–Hurwitz・norm・Hodge因子・dg復元は本文の通常証明と引用定理への依存である。
新節単体のLuaLaTeX組版4頁、全頁画像、内部参照・overfullなしを確認。主論文全体の今回の再組版、旧34検証器全再実行、独立査読、新規性の網羅調査は未実施。
主論文差分で既存証明本文・入力節・文献表を保持した。保存後main ref、必要ファイル、実行コードとblob SHAを確認する。PDF・wrapper・ログ・画像はGitへ入れず、pushした内容をLibraryへ保存しない。
