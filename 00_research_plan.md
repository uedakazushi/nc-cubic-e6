# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v21。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎知識は `research/research_notes.md`、DAHA・Fricke比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、Cayley・LG・格子・G2・braid・周期は `research/cayley_lg_connections.md`。現行文書だけで再開できるようにし、旧bundleを前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先目標は研究と論文を数学的に面白くすること。優先的戦略は、多様な話題との具体的な関連を見つけ、検証可能な数学へ育てること。** 意外な同型、共通構造、見通し、新たな問いや方法を重視し、名称や定理数の増加を目的にしない。
正確性はこの優先順位で犠牲にしない。数学的重要性、新規性、理解の深化、応用可能性、実現可能性も総合して研究価値を最大化する。既定の分類の完遂が、面白い接続より自動的に優先されるわけではない。
重要な方針変更では現在の理由と元の目標の達成部分・残存部分を簡潔に記し、時系列の履歴を蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を明記する。原稿に証明があること、今回点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針へも反映する。
先行研究は一次資料で確認し、適用範囲と本稿の貢献をIntroductionで具体的に比較する。未確認の内容・書誌・新規性を推測で補わない。外部PDFや検索結果を大量収録しない。
原稿は日本語LuaLaTeX。公表価値のある関連分野の成果は同じ主論文へ統合する。分割は数学的まとまりと公表上の利点が明確な場合に検討する。既存の価値ある成果や必要証明を軽量化のために削除しない。
研究ノートは着想・補題・反例・本質的障害・文献比較・再取得困難な情報を保持し、日誌、会話、更新履歴、重複証明にしない。論文に証明がある事項は参照する。
現行方針・ノート・論文と必要最小限のコード・入力・小証明書・再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・組版中間物を含めず、内容と検証可能性を損なわず整理する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubへpushした内容はLibraryに保存しない**。push失敗で未保存成果の保全が必要な場合のみ緊急退避できる。既存Library資料を明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を区別して報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行う。force push、不要なPR・Actionsを使わず、PDF・ZIPをGitで追跡しない。未実行をPASSと言わない。

## II. 現在の問いと達成基準

**同じ非可換三次曲面の代数から、どのような幾何が回復され、実際の写像・作用・変形で結ばれるか**を調べる。量子so3の中心は四穴球面Frickeへ、一次元表現被覆はLG・Cayley・D4へ、対称LG等位面はG2指標多様体へつながる。
局所MilnorとPicardの整数D4比較を得たので、現在は作用と周期を調べる。成分ラベルを交換する底のbraidと、成分を保つHurwitz braidを区別でき、境界radicalの周期も正規化できた。次の未知量は内部四周期、混合Hodge拡大、D4商への作用、および有限軌道の圏的・算術的意味である。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆には本文の証明がある。全intrinsic H3の相対代数化・降下・大域境界は未完成だが、新しい接続研究の前提にしない。
達成基準は、具体的写像・変形・局所模型・格子写像・圏的対応・障害のいずれかを正確に示すこと。既知理論、本稿の明示的適用、新規性未確認の結果を分ける。型・群名・数値の一致だけで同一視しない。

## III. 現在有効な主要成果

### A. 変形・モジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）を保持。中央境界・対角非零の適用範囲を外さない。
横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族・指定enhancement・smooth DM八次元表示stackを構成。一般非被約底のintrinsic降下・H3開性・全境界は未完成で、`thm:conditional-component`の仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般係数の既約六次元結節因子（`sec:nodal-centers`）。中心特異性とH3境界を区別する。
AW中央特殊化、Casimirスケール、Fricke係数写像、量子的Vieta、古典的D4⊂E6。Q=q exp(h)の中心交換子は指定Goldman型括弧の9倍。Brown–Gordonによるsmooth locusの中心fiber比較。全DでのM3やMorita同値は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaには障害。一般変形・心の変更を否定しない。
固定包絡の十Poisson零点は五節点と五滑らか臨界点。四Casimir特異値のA1型、既存判定下のH3可否、二次接触／一次横断、S4作用を明示。
相対Poisson臨界環は全域有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5（`sec:relative-poisson-cover`）。有限体検算と群論・基本群の証明を区別する。旧定理の今回の独立再監査はしていない。

### C. Cayley・LG・実幾何

Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。W=H−Au−Bv−CwのJacobi環はrank5、graph(dH)はexact Lagrangian。
ramification divisorはCayleyで閉トーラスSL2粗指標多様体。対数Poisson、D4ミニバーサル変形、巡回三枝作用、原点Jacobi留数対を明示（`sec:cayley-lg-connections`）。
原点で被覆はetaleでもCasimir値は四重衝突する。被覆の分岐・Casimir値衝突・W臨界値衝突は別現象。
実elliptopeの境界はSU2トーラスpillowcase、内部の厳密凹性から実sheetは高々一つ。nearly Kähler S3×S3のmulti-moment像との共通凸体はDixonの既知比較。追加の圏同値・計量退化は未構成。

### D. Milnor・Picard・例外群G2

LG等位面はp=-2u等でFricke係数(-4A,-4B,-4C,8h)となる。元の量子中心との底変更は一次元表現の正規化A=(1-q)aとは異なる。
滑らかなU=S\Dで0→Z delta_infty→H2(U,Z)→<D_i>^perp→0。右端D4(-1)、左端原始radical、H1(U)=0。指定D4退化(2,2,2),h≈7/2のMilnor fiberの包含が右端へ整数格子同型を与える（`thm:lg-D4-Picard`）。選択した退化の比較であり、全域の標準分裂ではない。
巡回置換は判別群(Z/2)²の三非零元を回し、gluingから局所・Picard双方の外部trialityを検出する。
Goldman–Neumannのaffine D4のradicalは(1,1,1,1,2)。無限遠はmonodromy−IのT2束、H1はZ⊕(Z/2)²でpillowcaseとは別。混合Hodge graded piecesはGr2=Q(-1)^4, Gr3=0, Gr4=Q(-2)、E_c=1+4xy+(xy)²。拡大の分裂は未主張。
Boalch–Palubaの既知G2実現を対称LGへ適用。b=-4lambda,c=8h、alpha=c+2+3b、beta=−b³+3b²+3bc+3b−2。regular範囲でLGは三つの連結成分の一つ。unipotent底(6,6)のD4成分(lambda,h)=(2,7/2)とA2成分(-1/4,1/8)は、以前の四sheet衝突とsimple foldを結ぶ（`sec:lg-picard-g2`）。

### E. 二種類のbraid、有限軌道、境界周期

新しい証明は `papers/sections/quantum_cubic_g2_braids.tex`、ラベル `sec:g2-braids-periods`。
成分ラベル三次式はxi³+6xi²+3(1−alpha)xi+beta+2。z=xi+2、P=alpha+3、Q=beta+6alpha+12でz³−3Pz+Qとなり、A2 root cover、label monodromy S3、判別式補集合の基本群B3。d=4P³−Q²の引戻しは−(b²+b−c−1)²(b²−8b−4c−16)。cusp(-3,6)のLGは(lambda,h)=(1/2,1/8)で3A1。成分分岐と曲面特異点型は別情報（`thm:g2-component-A2`, `cor:g2-cusp-three-nodes`）。
HurwitzはB1=(u,2uv−w−2lambda,v)、B2=(w,v,2vw−u−2lambda)。W、体積、Jacobian Poisson、留数形式を保ち、braid関係、B1B2=(w,u,v)、(B1B2)³=1。b,cを固定するので各成分を保つ。底の成分交換B3と同一視しない。u固定のB1は平行移動後にtrace2uのSL2行列となりChebyshevで反復できる。
既知Klein七点軌道では置換像がS7（5040）と直接証明・全列挙。Boalch–Palubaの一つの表現像G2(2)'≅U3(3)（6048）やKlein群168とは別。G2底(-1,-1)の成分式は(xi+1)(xi²+5xi+1)、他二成分はQ(sqrt21)上（`prop:klein-seven-S7`）。
正規化omega=Res(du dv dw/(W−h))の原始境界cycle上の周期は(2pi i)²。局所二重留数1と境界トーラスの原始性から通常の証明で得る。Hurwitzはomegaとdelta_inftyを固定しD4商へ降りる。内部四周期・全Gauss–Manin系・MHS拡大の分裂は未計算（`thm:boundary-residue-period`）。

## IV. 次の優先課題

**第一優先：内部四周期と作用を結ぶ。**
境界周期が定数に正規化されたので、対称LGの小さな係数sliceで内部cycleのperiodを計算する。conic pencilとChebyshevの固定u表示を使い積分を低次元へ還元し、D4消滅点での漸近を照合する。まず一つの局所cycleの周期微分と対称性を求め、全Gauss–Manin系を未導出のまま宣言しない。境界方向を含むMHS拡大は別に追跡する。

**並行して優先：二braidとtrialityの比較。**
成分ラベルのS3、成分内部のPSL2Z、Picard判別群のtriality、有限軌道のS7を別の対象への作用として整理し、比較図式を構成する。三成分間の解析接続と一成分内のHurwitzを安易に同一視しない。H2/D4商への具体行列・消滅路による基底依存性を明示する。

**並行して優先：有限軌道・Fano・量子化。**
Klein軌道のS7と、Fano平面・八元数からの6048表現像の関係を、安定化群や局所系など具体的な対象を介して調べる。他二成分のQ(sqrt21)構造や実点と比較する。古典的G2同型から量子G2代数や圏同値を推論しない。

**保持する探索：実幾何・mirror・H3。**
Cayley modular作用の表現被覆への延長、elliptopeの実壁、LG留数・matrix factorization・Fukaya比較を小さい模型から進める。N5,M5のbranchと観測値衝突をtrace pairingで分離しPainlevé係数写像と比較する。純粋qの障害相殺、Vietaの心の変更、intrinsic降下・H3開性・全境界は保持するが、一枝だけに研究を固定しない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_g2_braids_periods.py
python3 computations/verify_all.py  # 全26検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回は新検証器を実行しPASS。Q上の恒等式、七点の置換群5040元、分岐式、Poisson保存、有限次数Chebyshev検算、境界二重留数を確認。小証明書は `computations/g2_braids_periods_certificate.json`。全次数漸化式・configuration space・境界トーラスの原始性と積分は通常の証明であり、コードの形式検証ではない。旧25検証器を今回全再実行していない。
新節単体はLuaLaTeX4頁で組版し、全頁を画像点検。内部参照解決済み、overfullなし。主論文全体の今回の組版、全旧証明の独立再監査、個別新規性の網羅調査は未実施。既存の数学的証明を保持して主論文・要旨・Introduction・方針・ノートを更新し、生成物をGitへ入れず、push済み内容をLibraryへ保存しない。
