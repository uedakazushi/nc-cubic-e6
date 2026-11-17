# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v23。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎知識は `research/research_notes.md`、DAHA・Fricke比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、Cayley・LG・G2・braid・周期の基礎は `research/cayley_lg_connections.md`、全四周期の現在の結論と次の着手は `research/conic_period_coordinates.md`。現行文書だけで再開し、旧bundleを前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先目標は研究と論文を数学的に面白くすること。優先的戦略は、多様な話題との具体的な関連を発見し、検証可能な数学へ育てること。** 意外な同型・共通構造、見通し、新しい問いや方法を重視する。名称や定理数を増やすこと自体を目的にしない。
正確性は犠牲にしない。数学的重要性、新規性、理解の深化、応用可能性、実現可能性も総合して研究価値を最大化する。既定の分類の完遂が面白い接続より自動的に優先されるわけではない。
重要な方針変更では現在の理由と元の目標の達成部分・残存部分を明記し、時系列の履歴を蓄積しない。
証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を示す。原稿に証明があること、今回点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。
先行研究は一次資料で確認し、適用範囲と貢献をIntroductionで比較する。未確認の内容・書誌・新規性を推測で補わない。外部PDFや検索結果を大量収録しない。
原稿は日本語LuaLaTeX。公表価値ある関連分野の成果も同じ主論文へ統合する。分割は数学的まとまりと公表上の利点が明確な場合に検討する。軽量化のために価値ある成果・必要証明を削除しない。
研究ノートは着想・補題・反例・本質的障害・文献比較・再取得困難な情報を保持し、日誌・会話・更新履歴・重複証明にしない。論文に証明がある事項は参照する。
現行方針・ノート・論文と必要最小限の原稿、コード、入力、小証明書、再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・組版中間物を収録せず、数学的内容と検証可能性を保持する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubへpushした内容はLibraryに保存しない**。push失敗で未保存成果を保全する必要がある場合だけ緊急退避できる。既存Library資料を明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を別状態で報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行う。force push、不要なPR・Actionsを使わず、PDF・ZIPをGitで追跡しない。未実行をPASSと言わない。

## II. 現在の問いと到達基準

**同じ非可換三次曲面から回復される幾何を、実際の写像・作用・変形・周期で結ぶ。** 量子中心はFrickeへ、一次元表現はLG・Cayley・D4へ、対称LGはG2へつながる。局所MilnorとPicardの整数D4、二種類のbraid、境界周期、具体的内部周期を得た。
現在は、退化conicの成分を選ぶ有限標識被覆上で整数D4基底と全四periodを同時に記述できた。これにより指定開集合では有理Hodge分裂を円分性で完全判定し、有理数体上の滑らかな分裂例と非分裂例を構成した。次は、この四次元period torus上でHurwitz・triality・境界変更を比較し、Hodge拡大の算術とmirror側の意味を調べる。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆には現行本文の証明がある。全intrinsic H3の相対代数化・降下・大域境界は未完成だが、他分野との接続研究の前提にはしない。
達成基準は具体的写像、変形、局所模型、格子写像、圏的対応、障害、周期式のいずれかを正確に与えること。既知理論、本稿の明示的適用、新規性未確認の結果を区別し、型・群名・数値の一致だけで同一視しない。

## III. 現在有効な主要成果

### A. 変形・モジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の適用範囲を外さない。
横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族、指定enhancement、smooth DM八次元表示stackを保持。一般非被約底のintrinsic降下・H3開性・全境界は未完成で、`thm:conditional-component`の比較仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般係数で既約六次元結節因子。中心特異性とH3境界を区別する。
AW中央特殊化、Casimir規約、Fricke係数写像、量子的Vieta、古典的D4⊂E6。Q=q exp(hbar)の中心交換子は指定Goldman型括弧の9倍。Brown–Gordonによるsmooth locusの中心fiber比較。全DでのM3やMorita同値は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaには障害。一般変形・心の変更を否定しない。
固定包絡の十Poisson零点は五節点と五滑らか臨界点。四Casimir特異値のA1型、既存判定下のH3可否、二次接触／一次横断、S4作用を明示。
相対Poisson臨界環は全域有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。有限体検算と群論・基本群の通常証明を区別し、今回旧定理の独立再監査をしたとはしない。

### C. Cayley・LG・実幾何

Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。W=H−Au−Bv−CwのJacobi環はrank5、graph(dH)はexact Lagrangian。
ramification divisorはCayleyで閉トーラスSL2粗指標多様体。対数Poisson、D4ミニバーサル変形、巡回三枝作用、Jacobi留数対（`sec:cayley-lg-connections`）。原点で被覆はetaleでもCasimir値は四重衝突し、branch・値衝突・W臨界値衝突は別現象。
実elliptopeの境界はSU2トーラスpillowcase、厳密凹性で内部実sheetは高々一つ。nearly Kähler S3×S3との共通凸体はDixonの既知比較で、追加の圏同値・計量退化は未構成。

### D. Milnor・Picard・G2・braid

滑らかなLG等位面U=S\Dで0→Z delta_infty→H2(U,Z)→D^perp→0。右端D4(-1)、左端原始radical、H1(U)=0。指定D4退化(2,2,2),h≈7/2のMilnor fiberの包含がPicard直交補へ整数同型を与え、巡回置換が両者の外部trialityを検出する。全域の標準分裂ではない。
混合Hodge graded piecesはGr2=Q(-1)^4, Gr3=0, Gr4=Q(-2)、E_c=1+4xy+(xy)²。無限遠はmonodromy−IのT2束。pillowcaseとは別空間。
Boalch–PalubaのG2実現を対称LGへ適用し、unipotent底(6,6)でD4成分(2,7/2)とA2成分(-1/4,1/8)が現れる。三成分ラベルのA2三次根被覆と、その内部のHurwitz B3を区別。HurwitzはW・体積・Poissonを保ち、一生成元はChebyshevで反復できる。
Klein七点の置換像S7（5040）を、表現像G2(2)'（6048）やKlein群168と区別する。既知の軌道・G2実現は先行結果として扱う。

### E. 対数周期と一つの非分裂例

omega=du∧dv/(uv−w−C)、原始境界周期は(2pi i)²。
d=u²−1、N=(u²+2Au+2h)d+B²+C²+2uBC。conicを平行移動してs²=d、z=u+sを使うとomega=dlog z∧dlog a。適切なmatching球面は2pi i[log z]_-^+。
A=B=C=0ではMorse球面の周期4pi arcsin sqrt(-2h)、Picard–Fuchsは2h(1+2h)y''+(1+4h)y'=0。二次元解局所系は無限二面体monodromyを持つ。指数化Q+Q^-1=2+8h。h=-1/10でQ=(3−4i)/5が非捩れなので有理MHS非分裂（`sec:logarithmic-periods`）。これは全rank五接続の行列ではない。

### F. 全四つの整数D4 periodと円分性

新節 `papers/sections/quantum_cubic_four_periods.tex`、`sec:four-D4-periods`。
適用範囲はDisc N≠0、B²−C²≠0。四根u_iは相異なり±1と異なる。境界D1を二重切断とするconic bundleで、五つの特異fiberの成分をcompatibleに選んで縮約しF1を得る。Picard基底s,F,E1..E5、境界D1=2s+2F−ΣEi、D2=E5、D3=F−E5。有限標識被覆上の選択であり、四つの平方根の符号を最初から任意としない。
K=D^perpはeven-sum Z4、整数基底alpha=(E1−E2,E2−E3,E3−E4,E3+E4−F)。選択成分が境界に会う座標z_i+z_i^-1=2u_iを用いて

P(alpha)=(z1/z2,z2/z3,z3/z4,z3*z4)。

境界線束のgluingとFriedman Prop3.12から積分periodと一致する。境界cycleとalphaの任意整数持上げが全H2の基底となり、内部周期は2pi i log P(alpha) modulo (2pi i)²Z。
指数行列det2、period torusへのisogenyの核は同時符号±1。係数からquartic係数へのJacobianは16(C²−B²)。根・成分を選ぶ開集合上で全四periodが局所座標。
Disc N=prod_{i<j}(zi−zj)²(zi*zj−1)²/[2^12(prod zi)^6]。これはD4 root hypertorusの古典的記述の本座標での実現であり、新しい一般Torelli定理ではない。
**必要十分条件：** このchartでは有理MHSの分裂 ⇔ 四periodが全てroots of unity ⇔ 全z_iがroots of unity。全整数基底への正規化periodの有理性を使う。整数拡大の自明性や有限Hurwitz軌道は結論しない。
分裂例は(A,B,C,h)=(1/4,1/2,1/4,1/8)、16z^4 N((z+z^-1)/2)=(z^9−1)/(z−1)。非分裂例は(-65/16,75/16,-65/16,3575/288)、z_i=2,3,4,6の各逆数選択。ともにQ上の滑らかな曲面。証明・検算の所在は新節と `verify_conic_period_coordinates.py`。

## IV. 次の優先課題と具体的着手

**第一優先：四period上の作用を具体化する。**
Hurwitzの一生成元が固定するconic pencilを選び、選択直線の像とD4基底への作用を計算する。周期値の不変性、標識変更、底の解析接続を区別する。trialityではconic pencil自体が変わるので、異なるF1標識の遷移を先に求める。Weylのeven signed permutations、固定fiberの非線型作用、S5の別被覆を混同しない。

**並行して優先：円分的Hodge分裂の意味を広げる。**
分裂例の9乗根と境界線束の有限位数を、Kummer型拡大、arithmetical period、mirrorのtorus座標へ結ぶ。元の量子q³=1、有限Hurwitz軌道、整数Hodge分裂とは別の条件。まず分裂例で四periodの正確な位数と標識変換を調べ、必要なら反例を用いて関連の限界を示す。

**並行して優先：周期・接続・非可換比較。**
今回の全四周期は有限標識被覆上の局所的な積分・線束座標を与える。代数的de Rham基底でのrank五Gauss–Manin接続は未構成なので、dlog p_iと境界方向を起点に具体的な基底を探す。混合Hodgeの拡大、log形式、LGのvanishing cyclesとmirror/Fukaya比較を、小さい局所模型から進める。

**支える課題：H3・八次元成分と判別式。**
N5,M5のbranchと観測値衝突を分離し、Painlevé VIの係数写像と比較する。純粋q障害のSklyanin方向による相殺、Vietaの心の変更、一般H3開性・intrinsic降下・全境界を保持する。大域消去の反復を目的化せず、構造・意味・小さい検証を先に取る。

## V. 再現と検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_conic_period_coordinates.py
python3 computations/verify_all.py  # 全28検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回実行した新検証器はQ・整数格子・Laurent恒等式の厳密計算でPASS。conic determinant、係数Jacobian、D4基底、指数行列、判別式の因子恒等式、分裂・非分裂例とsmooth開条件を確認した。証明書は `computations/conic_period_coordinates_certificate.json`。
縮約とcompatible markingの存在、線束gluing、Friedman比較、MHS分裂判定は通常の証明であり、有限計算のPASSと区別する。旧27検証器は今回全再実行していない。
新節単体のLuaLaTeX組版4頁、全頁の画像点検、内部参照、overfullなしを確認。主論文への入力と更新差分を点検し、既存の証明本文を保持した。主論文全体の今回の再組版、旧証明の独立再監査、新規性の網羅調査は未実施。生成PDF等はGitへ入れず、push済み内容をLibraryへ保存しない。
