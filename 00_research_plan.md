# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v27。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎は `research/research_notes.md`、DAHA比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、LG/G2は `research/cayley_lg_connections.md`、四周期/trialityは `research/conic_period_coordinates.md`。境界力学・局所化・絡み目・正規化の現行式は `research/boundary_pell_dynamics.md`。旧bundle・会話履歴を再開の前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先は数学的に面白くすること。優先戦略は多様な話題との具体的接続を見つけ、検証可能な数学へ育てること。** 意外な同型・共通構造、見通し、新しい問いや方法を重視し、名称や定理数の増加を目的にしない。
正確性を犠牲にせず、数学的重要性、新規性、理解の深化、応用、実現可能性を総合して価値を最大化する。既定の分類の完遂が面白い接続より自動的に優先されるわけではない。重要な方針変更は現在の理由と元の目標の達成部分・残存部分を簡潔に示し、時系列の履歴を蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を記す。原稿の証明、今回の点検、計算実行、独立査読を分ける。誤りは依存する本文・要約・方針にも反映する。
一次文献の仮定・適用範囲を確認し、Introductionで既知結果と貢献を具体的に比較する。未確認の内容・書誌・新規性を推測で補わない。外部PDF・検索結果を大量収録しない。
原稿は日本語LuaLaTeX。関連分野の公表価値ある成果も同じ主論文の適切な位置に統合する。分割は数学的まとまりと公表上の利点で判断する。価値ある既存成果・必要証明を軽量化のために削除しない。
研究ノートは着想、補題、計算、反例、本質的障害、文献比較、再取得困難な情報を保持する。日誌・会話・更新履歴・重複証明にせず、主論文に証明があれば参照する。
現行方針・ノート・論文と必要最小限の原稿、コード、入力、小証明書、再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・中間生成物を除くが、数学的内容と検証可能性は保持する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryへ保存しない**。push失敗で未保存成果の保全が必要な場合のみ緊急退避できる。既存Library資料を明示指示なしに削除しない。
日付・版番号を付け、生成・検証・commit・push・Library保存を別状態で報告する。約15分または数学的区切りでmainへ通常のfast-forward保存。force push、不要なPR・Actionsを使わず、PDF・ZIPをGitで追跡しない。未実行をPASSと言わない。

## II. 現在の問いと研究選択

**同じ非可換三次曲面から回復される幾何を、写像・作用・周期・局所模型で結ぶ。** 量子中心はFrickeへ、一次元表現はLG/Cayley/D4へ、対称LGはG2へつながる。trialityの指数3からG2三成分写像を説明し、有理MHS比較と整数拡大位数7,21,21を得た。
周期を固定する正entropyの自己同型gはPell次数を持つが、通常のPerf(U)のDHKK entropyは零。対象だけでなく射の極filtrationと自然な閉包対象の成長を分けて測る必要がある。
今回、閉包の全算術種数が**一つの境界点の二つのPell型cusp**に集中することを証明した。linkはT(2b_n,2c_n)、正規化層と一点欠損層の成長率はlog Lambdaと2log Lambda。Chebyshev実morsificationを既知のCasals構成へ入れ、局所Weinstein模型を指定できた。異なる反復の模型を結ぶ関手や元の大域曲面との同値はまだない。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆の証明は現行原稿にある。全intrinsic H3の相対代数化・降下・大域境界は未完成だが、他分野研究の前提にしない。
達成基準は具体的な写像、変形、局所模型、格子写像、圏的対応、障害、周期式のいずれかを正確に与えること。型・名前・数値の一致から同一視しない。

## III. 主要な到達点と確実性

### A. 非可換変形とモジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の仮定を外さない。横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族・enhancement・smooth DM表示stackを保持。一般非被約底のintrinsic降下、全H3開性・境界は未完成で、成分定理の相対比較仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般係数で既約六次元因子。中心特異性とH3境界は異なる。AW中央特殊化、Casimir規約、Fricke係数写像、量子的Vieta、D4⊂E6を明示。Q=q exp(hbar)の交換子は指定Goldman型括弧の9倍。Brown–Gordonを適用するが、全DでのM3/Morita型は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaに障害がある。一般変形・心の変更は否定しない。固定包絡の十Poisson零点、四Casimir特異値、既存判定のH3可否、二次接触／一次横断、S4作用を保持。
相対Poisson臨界環は有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。有限体検算と群論・基本群の通常証明は別。今回は旧主張を独立再監査していない。

### C. LG・格子・全周期

一次元表現のPhi=grad[uvw−(u²+v²+w²)/2]、Jacobi環rank5、exact Lagrangian graph。分岐源CayleyはトーラスSL2指標多様体。D4 miniversal、三枝巡回、留数対、elliptope/pillowcase、内部実sheet一意性を得た。
U=S\Dで0→Z delta_infty→H2(U,Z)→D^perp→0、右端D4(-1)、左端原始radical。指定D4退化のMilnor包含とPicardの整数比較、外部triality。全域標準分裂ではない。MHSの重み2の4方向と重み4の1方向。nearly Kählerの共通elliptopeは既知比較で、圏同値は未構成。
BPのG2実現でD4/A2の二成分退化。成分交換braidと内部Hurwitz、Klein七点S7と表現像6048は別。
境界周期(2pi i)²、matching対数、Morseのarcsine周期、無限二面体解局所系、有理非分裂h=-1/10。compatible conic標識で四period=(z1/z2,z2/z3,z3/z4,z3*z4)、有理MHS分裂⇔全zi捩れ。数値分裂・非分裂例を保持し、W臨界値・Casimir値・被覆分岐を区別する。

### D. trialityの指数3と三成分

`sec:triality-period-isogeny`。対称Hurwitzホモロジー像は外側三根S3、pure braidは自明（Goldman–Neumann）。周期(xi,eta,eta,eta)、不変→余不変格子diag(1,3)、torus写像(xi,eta)→(xi,eta³)、kernel mu3。
S=sum_{t=eta,xi eta,xi eta²}(t+t^-1)、L=sum_{t=xi,xi eta³,xi²eta³}(t+t^-1)、lambda=(S+2)/4、h=(L+3S+4)/8。対称族は旧B²≠C² chart外なので別の明示line sectionで標識を構成する。
Weyl商alpha=L、beta=S³−3SL−9S−6L−12はBP三成分写像。共通明示開集合で三成分の有理MHSを標識graded pieceの下で比較し、Klein7,21,21の整数拡大位数を得る。全底の標準VMHSや曲面/導来同値ではない。

### E. 境界力学と局所化

`sec:boundary-pell-dynamics`, `sec:localization-entropy`。g=iota_v iota_w iota_u iota_w、Lambda=3+2sqrt2。M=[[1,-2],[-2,5]]、M^n=[[a,-b],[-b,c]]、d=b+c=1,7,41,239,...、d_(n+2)=6d_(n+1)−d_n、d²−2c²=−1。境界Theta(r,t)=(|r|,|t|,|r+t|)。最小多項式次数d、generic射影交点次数2d（n≥1）。指定Sを支配する有限境界blow-up上では正則化できず、個別付値のcorner抽出は4n。algebraic stabilityの不存在ではない。
アフィン引戻しDHKK h_t=0。生成元固定とEnd恒等作用は別。極filtrationは全次数でdim F_m=(3m²+3m+2)/2、射の最小尺度倍率d_n、歪み率log Lambda。像の次元そのものは増えない。
一般conic逆像閉包のclass cD_u+bD_v+dD_w、算術種数delta=1+2bc−d。構造層Q_nのproper対象列の率2log Lambda、開制限は二項自由解消。これは関手entropyではない。filtered HHにはlog Lambdaが見え、rank6のHPと全periodにはgが恒等。個別gに同変なfiltered mirrorは未構成。

### F. 二cusp・link・conductor・欠損層

新節 `sec:boundary-torus-links`。条件kappa²≠1、N_v(kappa)≠0のconic C0={v=kappa}を使う。n≥1の閉包の特異点はp_wだけ、二枝のPuiseux対(b,c)、交叉bc。rho±=kappa±sqrt(kappa²−1)について局所先頭式x=2^-b rho^-a s^b、y=2^-c rho^-b s^c。最低重み式はy^(2b)−2kappa x^c y^b+x^(2c)。全germの解析的右同値を主張しない。解消後z=y^b/x^c=rho±が元の係数を保持。
link=T(2b,2c)、各成分T(b,c)、linking bc。delta=1+2bc−b−c、mu=2delta−1、conductorは両枝s^delta。Milnor fiberのgenus delta−1、境界2、H1 monodromyの正確な位数2bcでspectral radius1。nを動かすgの力学とは別。
正規化B_n=nu_*O_P1、欠損Z_n=B_n/Q_n。Z_nはp_wだけ、length delta、H1(Q_n)=H0(Z_n)。proper対象列の率はB_nがlog Lambda、Z_nが2log Lambda。開制限ではZ_n=0、B_n=Q_n。
Chebyshev実morsificationはdelta個の零level nodeとdelta−1個の極値を持つ。Casalsの既知定理からlocal Weinstein pairのMilnor Lagrangian曲面＋mu thimble模型を得る。二handleで閉じた四多様体のEuler3と元のUのEuler6を区別する。模型間の関手・equivariant mirrorは未構成。

## IV. 優先課題と具体的着手

**第一優先：局所模型を対象・射の対応へ進める。**
n=1のT(4,10)についてChebyshev divideの交叉、thimble配置、microlocal sheafの小さいquiverを計算し、正規化完全列とconductorに対応するexact triangleを探す。局所模型の存在からglobal Uやgのwrapped圏との同値を推論しない。

**並行して優先：反復間の対応と係数保存。**
逆反復でPuiseux対は **(b,c)→(b+2c,2b+5c)** と変わる。これをtoric解消の共通細分、例外torus上のz=rho±とともに記述し、exact cobordism・stop変更・代数的局所化のどれへ持ち上がるか調べる。局所の有限Milnor monodromyと反復間の双曲型gを混同しない。

**並行して優先：三成分Hodge比較の幾何学化。**
3捩れperiod差を境界線束の変更・有限被覆・代数的対応として構成できるか、Klein7/21のline配置から調べる。有理Hodge同型から曲面・圏同値を推論しない。Spin8→G2 character、捩れ位数、全rank五接続も維持する。

**支える課題：非可換成分と独立監査。**
N5,M5のbranch/観測値衝突、Sklyanin方向での純粋q障害相殺、Vietaの心の変更、全H3 admissibility・intrinsic降下・全境界を継続する。公表前に旧依存定理も独立監査する。一枝の重い計算に研究を固定しない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_boundary_torus_links.py
python3 computations/verify_all.py  # 全32検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
新検証器をQ・Z上で実行しPASS。全係数一反復、帰納式、24反復の整数値、n1 Jacobi次元27・conductor14、Milnor多項式、Chebyshev臨界値resultantを確認。証明書 `computations/boundary_torus_links_certificate.json`。
全nのPuiseux型、link/conductor/Milnor理論、正規化複雑度、Casals構成は本文の通常証明と一次資料への依存であり、有限検算だけの形式証明ではない。旧31検証器は今回全再実行していない。
新節単体をLuaLaTeX wrapperで5頁に組版し、全画像・内部参照・overfullなしを点検。主論文全体の今回の組版、旧証明の独立再監査、global filtered mirror、新規性の網羅調査は未実施。
主論文差分で旧証明本文・入力節・文献表の保持を確認する。main refと必要ファイル、実行コードの一致を保存後に確認。PDF・wrapper・画像・ログをGitへ入れず、push済み内容をLibraryへ保存しない。
