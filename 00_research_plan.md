# 研究方針：非可換三次曲面から広がる幾何学

2026-11-18 / e6-connections-v29。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎は `research/research_notes.md`、DAHA比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、LG/G2は `research/cayley_lg_connections.md`、全period/trialityは `research/conic_period_coordinates.md`。境界力学・link・局所化は `research/boundary_pell_dynamics.md`、閾値・解析的modulus・MF・二捩れ楕円曲線は `research/boundary_analytic_moduli.md`。旧bundleや会話履歴を再開の前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先は数学的に面白くすること。優先戦略は多様な話題との具体的な接続を見つけ、検証可能な数学へ育てること。** 意外な同型・共通構造、見通し、新しい問い・方法を重視し、名称や定理数を増やすことを目的にしない。
正確性を犠牲にせず、重要性、新規性、理解の深化、応用、実現可能性を総合して研究価値を最大化する。既定の分類の完遂が他の面白い接続より自動的に優先されるわけではない。重要な方針変更は現在の理由と元の目標の達成部分・残存部分を簡潔に記し、時系列の履歴は蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張には仮定・依存結果・証明箇所・未解決点を示す。原稿中の証明、今回の点検、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。
先行研究を一次資料で確認し、Introductionで既知結果の範囲と本稿の貢献を比較する。未確認の内容・書誌・新規性を推測で補わない。文献PDFや検索結果を大量収録しない。
原稿は日本語LuaLaTeX。公表価値ある関連分野の結果も同じ主論文へ統合する。分割は数学的まとまりと公表上の利点で判断し、価値ある既存成果・必要証明を軽量化のために削除しない。
研究ノートは着想、補題、計算、反例、本質的障害、文献比較、再取得困難な情報を保持する。日誌・会話・履歴・重複証明にせず、主論文に証明がある事項は参照する。
現行方針・ノート・論文と必要最小限の原稿、コード、入力、小証明書、再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・組版中間物は除くが、数学的内容と検証可能性を損なわない。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryに保存しない**。push失敗で未保存成果の保全が必要な場合だけ緊急退避できる。既存Libraryファイルを明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を別状態として報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行い、force push、不要なPR・Actionsを使わない。PDF・ZIPをGitで追跡せず、未実行をPASSと言わない。

## II. 現在の問いと研究選択

**同じ非可換三次曲面から回復される幾何を、写像・作用・周期・局所模型で結ぶ。** 量子中心はFrickeへ、一次元表現はLG/Cayley/D4へ、対称LGはG2へつながる。周期isogeny、境界力学、局所特異点、圏のどの情報がどの不変量に残るかを比較する。
今回、境界の二枝に残る解析的modulus K=kappa²を取り出した。重み付き主部の二周期MF圏は(n,K)で分類でき、同じlink・閾値・Hochschild次元でも非同値となる。解消上の四点に付随する非零二捩れ標識付き楕円曲線の粗modulusもKであり、jや二同種関係だけでは圏を区別できない。
同時に、**実際の一反復境界にはmu=27,tau=24の例があり、重み付き主部(mu=tau=27)へ解析的には置き換えられない**ことを確認した。したがって主部の完全分類を実際の境界MFへ無条件に延長しない。Hochschildの積、指定した類[f]、高重み変形を区別することが現在の核心である。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆の証明は現行原稿にある。全intrinsic H3の相対代数化・降下・大域境界は未完成で、他分野研究の前提にしない。
達成基準は具体的写像、変形、局所模型、格子写像、圏的対応、障害、周期式を正確に与えること。型・名前・数値の一致から同一視しない。

## III. 主要な到達点と確実性

### A. 非可換変形とモジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の仮定を外さない。横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。接空間行列rank18、gauge14、商8。全Artin表示族・enhancement・smooth DM表示stackを保持。一般非被約底のintrinsic降下・H3開性・全境界は未完成で、成分定理の相対比較仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般係数で既約六次元因子。中心特異性とH3境界は異なる。AW中央特殊化、Casimir規約、Fricke係数写像、量子的Vieta、D4⊂E6を明示。Q=q exp(hbar)の交換子は指定Goldman型括弧の9倍。Brown–Gordonを適用するが全DでのM3/Morita型は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaには障害があり、一般変形・心の変更は否定しない。固定包絡の十Poisson零点、四Casimir特異値、H3可否、二次接触／一次横断、S4作用を保持。
相対Poisson臨界環は有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。有限体計算と群論・基本群の証明は別。今回旧主張の独立再監査はしていない。

### C. LG・格子・全周期

一次元表現のPhi=grad[uvw−(u²+v²+w²)/2]、Jacobi環rank5、exact Lagrangian graph。分岐源CayleyはトーラスSL2指標多様体。D4 miniversal、三枝巡回、留数対、elliptope/pillowcaseと内部実sheet一意性を明示。
U=S\Dで0→Z delta_infty→H2(U,Z)→D^perp→0、右端D4(-1)、左端原始radical。指定退化のMilnor包含によるPicardとの整数同型、外部triality。全域標準分裂ではない。MHSは重み2の4方向と重み4の1方向。
G2実現のD4/A2二成分、成分交換と内部Hurwitz、Klein七点S7と表現像6048を区別。境界周期(2pi i)²、matching対数、Morseのarcsine周期、rank二の無限二面体解局所系、有理MHS非分裂例を保持。
compatible conic標識上で四period=(z1/z2,z2/z3,z3/z4,z3*z4)。指定開集合で有理MHS分裂⇔全zi捩れ。W臨界値、Casimir値、被覆の分岐を混同しない。

### D. trialityと三成分Hodge比較

対称Hurwitzのホモロジー像は外側三根S3、pure braidは自明。period=(xi,eta,eta,eta)、不変→余不変格子diag(1,3)、torus写像(xi,eta)→(xi,eta³)にkernel mu3。
Weyl不変量S,Lからlambda=(S+2)/4、h=(L+3S+4)/8、alpha=L、beta=S³−3SL−9S−6L−12でBP三成分写像を得る。旧conic chart外の対称族は別の明示sectionで標識を構成。共通開集合で有理MHS比較、Kleinの整数拡大位数7,21,21。全底の標準VMHS、曲面同型、導来同値ではない。

### E. 境界力学・局所化・二枝

g=iota_v iota_w iota_u iota_w、Lambda=3+2sqrt2、M=[[1,-2],[-2,5]]。
M^n=[[a,-b],[-b,c]]、d=b+c=1,7,41,...。Theta(r,t)=(|r|,|t|,|r+t|)。最小次数d、射影交点次数2d、無理固有付値、指定コンパクト化上の有限境界blow-up非正則化、個別付値抽出4nを保持。algebraic stabilityの否定ではない。
アフィン引戻しDHKK h_t=0。極filtrationの射歪み率log Lambda、像の次元自体は増えない。反復conic閉包のclass cD_u+bD_v+dD_w、算術種数delta=1+2bc−d、構造層のproper対象列率2log Lambda。HHのfiltrationとrank6のHPの違いを区別。
初期conicの条件kappa²≠1、N_v(kappa)≠0の下で、境界はp_wの二枝、Puiseux対(b,c)、交叉bc。局所先頭式はx=2^-b rho^-a s^b、y=2^-c rho^-b s^c、面はy^(2b)−2kappa x^c y^b+x^(2c)。link T(2b,2c)、conductor各枝delta、Milnor数(2b−1)(2c−1)、homology monodromyの位数2bc。重み付き主部への解析的同値は主張しない。
正規化層の対象列率log Lambda、一点欠損層の率2log Lambda。Chebyshev実morsificationとCasalsの局所Weinstein模型を得るが、元の大域曲面や反復間の関手とは同一視しない。

### F. 閾値、解析的modulus、MF、二捩れ楕円曲線

主論文 `subsec:boundary-thresholds-mf`, `sec:boundary-analytic-moduli`。
Newton面からlct=(b+c)/(2bc)、0<tau<1で乗数イデアルは b(i+1)+c(j+1)>2bc tau の単項式で生成。減衰率log Lambda。実境界の局所MFのHH次元は(2b−1)(2c−1)、増大率2log Lambda。異なるnのMFはMorita非同値。
二枝の先頭根r1,r2からI=(r1+r2)²/(4r1r2)を回収でき、実germの解析同型はkappa²一致を必要とする。
**重み付き模型**F_nk=y^(2b)−2kappa x^c y^b+x^(2c)の二周期MFは、dg Morita同値⇔nとkappa²が一致（`thm:weighted-boundary-Morita-classification`）。DyckerhoffのHHを代数として用い、Euler式でJac=Tjurina、Mather–Yauと座標変換から証明。固定nで同じlink・閾値・HH次元でも無限個の圏がある。生成元の通常Ext代数は外積代数で同じだが、適合minimal A∞模型の高次積に係数が現れる。
解消上の四点0,infty,rho±の二重被覆E_k: eta²=z(z²−2kappa z+1)にT=(0,0)を標識。粗modulusはK=kappa²∈A1\{1}=Y0(2)、j=64(4K−3)³/(K−1)。K=0と9/8はj1728が同じでもMF模型は非同値。二捩れ商K→K/(K−1)でも一般にMF同値にはならない。これは四点から付随させた曲線で、元の反標準境界・Milnor quotient・圏の部分圏とは未同定。
**実germの障害例**：A=B=C=0,h=1、初期v=2、n=1でmu27,tau24。resultantの重み31jetと正則初期列のsocle重み26による厳密線型代数で確認（`prop:actual-boundary-tjurina-defect`）。主部はmu=tau27なので接触非同値。tau差だけで標識なし二周期MFの非同値を結論しない。一般MFでTjurinaを得るにはJacobian環中の指定類[f]が必要である。

## IV. 次の優先課題と着手方法

**第一優先：実境界の高重み情報と圏の追加構造。**
mu27,tau24の具体例でJacobian環の積を主部と比較する。指定類[f]をdg圏のどの追加構造が回復するか、Hua–Keller等の復元定理を一次資料で適用範囲から確認する。重み付きEuler式がない場合にMather–Yauを直接適用しない。まずn=1のkappa・ambient hの有理な変動で有限jetとTjurina次元の跳躍を調べ、位相一定でも動く解析moduliを明示する。

**並行して優先：二捩れ楕円曲線の位置付け。**
同じKがMF模型とY0(2)に現れる理由を、解消上の四点・Hochschild積・高次A∞積の比較から深める。単なるmoduli空間の一致を圏同値としない。2isogenyがMF同値を与えない反例を保持し、自然な対応・kernel・equivariant構造が存在するかを検討する。付随曲線をMilnor fiberの商と無検証に主張しない。

**並行して優先：局所Weinstein模型とfiltered mirror。**
Pell linkの実divide・thimbleを具体的にし、局所対象のEnd環とaction filtrationを指定する。通常のPerf(U)のentropyは零なので正値を再発見しようとしない。poleとactionの線型比較だけでなく、特定gへの同変性が必要。局所MF・局所Weinstein・大域H3の三圏を区別する。

**支える課題：三成分Hodgeと非可換成分。**
3捩れperiod差とKlein7/21を境界線束変更・有限被覆・代数的対応へ移す。有理Hodge同型から曲面/圏同値を推論しない。N5,M5のbranchと値衝突、Sklyanin方向のq障害相殺、Vietaの心の変更、全H3開性・降下・全境界を保持する。公表前には旧依存定理も独立に監査する。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_boundary_thresholds.py
python3 computations/verify_boundary_analytic_moduli.py
python3 computations/verify_all.py  # 全34検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回は上の個別二検証器を実行しPASS。前回未pushだった閾値の原稿・コードも現行主論文へ統合した。新計算はQとQ(sqrt2)上で、模型Jacobian環、Euler式、j・二同種恒等式、実Vietaのresultant、重み付き有限jetのrank18/21・mu27/tau24を再現。全分類・Mather–Yau・Morita不変性・filtered Koszul・楕円moduliは通常の証明と一次文献への依存で、有限検算そのものではない。
新解析modulus節の独立LuaLaTeX組版は5頁で成功し、全頁を画像点検。内部参照解決、overfullなし。主論文全体の今回の再組版、既存32検証器の全再実行、独立査読、新規性の網羅調査は未実施。
主論文差分で旧証明本文・入力節・文献表の保持を確認する。保存後はmain ref、必要ファイル、実行コードとblob SHAの一致を確認する。PDF・wrapper・ログ・画像はGitに入れず、push済み内容はLibraryへ保存しない。
