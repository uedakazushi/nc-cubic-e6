# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v22。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎知識は `research/research_notes.md`、DAHA・Fricke比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、Cayley・LG・格子・G2・braid・周期は `research/cayley_lg_connections.md`。現行文書だけで再開し、旧bundleを前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先目標は研究と論文を数学的に面白くすること。優先的戦略は、多様な話題との具体的な関連を見つけ、検証可能な数学へ育てること。** 意外な同型、共通構造、見通し、新しい問いや方法を重視する。名称や定理数の増加自体は目的にしない。
正確性は犠牲にしない。数学的重要性、新規性、理解の深化、応用可能性、実現可能性も総合して価値を最大化する。既定の分類の完遂が、面白い接続より自動的に優先されるわけではない。
重要な方針変更では現在の理由、元の目標の達成部分と残る部分を簡潔に示し、時系列の変更履歴を蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別し、主要主張に仮定・依存結果・証明箇所・未解決点を付す。原稿に証明があること、今回点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。
先行研究は一次資料で確認し、適用範囲と貢献をIntroductionで比較する。未確認の内容・書誌・新規性を推測で補わない。外部PDFや検索結果を大量収録しない。
原稿は日本語LuaLaTeX。公表価値ある関連分野の成果も同じ主論文へ統合する。分割は数学的まとまりと公表上の利点が明確な場合に検討する。軽量化のために価値ある成果や必要証明を削除しない。
研究ノートは着想・補題・反例・本質的障害・文献比較・再取得困難な情報を保持し、日誌・会話・更新履歴・重複証明にしない。論文に十分な証明がある事項は参照する。
現行方針・ノート・論文と必要最小限の原稿、コード、入力、小証明書、再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・組版中間物は収録せず、数学的内容と検証可能性を保って整理する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubへpushした内容はLibraryに保存しない**。push失敗で未保存成果を保全する必要がある場合だけ緊急退避できる。既存Library資料は明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を別状態として報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行い、force push、不要なPR・Actionsを使わない。PDF・ZIPはGitで追跡せず、未実行の検証をPASSと言わない。

## II. 現在の問いと達成基準

**同じ非可換三次曲面から回復される幾何を、実際の写像・作用・変形・周期で結ぶ。** 中心はFricke指標多様体へ、一次元表現被覆はLG・Cayley・D4へ、対称LG等位面はG2へつながる。局所MilnorとPicardの整数D4比較、二種類のbraid作用、境界周期を得た。
現在は内部周期を具体化できた。conic匹配球面の周期は対数、係数零の一変数族はarcsineで表され、指数化するとLooijenga対の代数的periodになる。h=-1/10で有理混合Hodge拡大が非分裂と分かった。次はこの式を内部四方向の同時格子へ広げ、作用・周期・mirrorの比較へ進む。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆には本文の証明がある。全intrinsic H3の相対代数化・降下・大域境界は未完成だが、他分野との接続の前提にしない。
達成基準は具体的写像、変形、局所模型、格子写像、圏的対応、障害、周期式のいずれかを正確に与えること。既知理論、明示的適用、新規性未確認の結果を分け、型・群名・数値の一致だけで同一視しない。

## III. 現在有効な主要成果

### A. 変形・モジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の適用範囲を外さない。
横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族・指定enhancement・smooth DM八次元表示stack。一般非被約底のintrinsic降下・H3開性・全境界は未完成で、`thm:conditional-component`の仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般係数の既約六次元結節因子。中心特異性とH3境界は異なる。
AW中央特殊化、Casimirスケール、Fricke係数写像、量子的Vieta、古典的D4⊂E6。Q=q exp(hbar)の中心交換子は指定Goldman型括弧の9倍。Brown–Gordonによるsmooth locusの中心fiber比較。全DでのM3やMorita同値は未確認。
非Casimir切断の純粋q変形、固定pointed H3心へのVietaに障害。一般変形・心の変更を否定しない。
固定包絡の十Poisson零点は五節点と五滑らか臨界点。四Casimir特異値のA1型、既存判定下のH3可否、二次接触／一次横断、S4作用を明示。
相対Poisson臨界環は全域有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。有限体検算と群論・基本群の通常証明を区別し、今回旧定理の独立再監査をしたとはしない。

### C. Cayley・LG・実幾何

Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。W=H−Au−Bv−CwのJacobi環はrank5、graph(dH)はexact Lagrangian。
ramification divisorはCayleyで閉トーラスSL2粗指標多様体。対数Poisson、D4ミニバーサル変形、巡回三枝作用、原点Jacobi留数対（`sec:cayley-lg-connections`）。
原点で被覆はetaleでもCasimir値は四重衝突。被覆の分岐・Casimir値衝突・W臨界値衝突を区別する。
実elliptopeの境界はSU2トーラスpillowcase、内部の厳密凹性から実sheetは高々一つ。nearly Kähler S3×S3との共通凸体はDixonの既知比較で、圏同値・計量退化は未構成。

### D. Milnor・Picard・G2

LG等位面はp=-2u等でFricke係数(-4A,-4B,-4C,8h)。量子中心との底変更は一次元表現の正規化A=(1-q)aとは異なる。
滑らかなU=S\Dで0→Z delta_infty→H2(U,Z)→<D_i>^perp→0。右端D4(-1)、左端原始radical、H1(U)=0。指定D4退化(2,2,2),h≈7/2のMilnor fiberの包含が右端へ整数格子同型（`thm:lg-D4-Picard`）。全域の標準分裂ではない。
巡回置換は判別群(Z/2)²の三非零元を回し、gluingから局所・Picard双方の外部trialityを検出する。affine D4のradicalは(1,1,1,1,2)、無限遠はmonodromy−IのT2束、H1=Z⊕(Z/2)²。
混合Hodge graded piecesはGr2=Q(-1)^4, Gr3=0, Gr4=Q(-2)、E_c=1+4xy+(xy)²。拡大は一般に自明としない（具体的非分裂例はF）。
Boalch–PalubaのG2実現を対称LGへ適用。b=-4lambda,c=8h、alpha=c+2+3b、beta=−b³+3b²+3bc+3b−2。regular範囲でLGは三つの連結成分の一つ。unipotent底(6,6)のD4成分(2,7/2)とA2成分(-1/4,1/8)が、四sheet衝突とsimple foldを結ぶ。

### E. braid・有限軌道・境界周期

成分ラベル式はz³−3Pz+Q、P=alpha+3,Q=beta+6alpha+12、label monodromy S3、判別式補集合の基本群B3。d=4P³−Q²の引戻しは−(b²+b−c−1)²(b²−8b−4c−16)。cusp(-3,6)のLGは3A1。成分分岐と曲面特異型は異なる。
HurwitzはB1=(u,2uv−w−2lambda,v)、B2=(w,v,2vw−u−2lambda)。W、体積、Poisson、留数形式を保存し、B1B2=(w,u,v)、中心は自明に作用。底loopのB3と別物。一生成元はtrace2uのSL2行列となりChebyshev反復を持つ。
Klein七点の置換像はS7（5040）。一つの表現像G2(2)'≅U3(3)（6048）やKlein群168と区別する。
omega=du∧dv/(uv−w−C)、原始境界cycleの周期Pi_infty=(2pi i)²。Hurwitzは形式とcycleを保存する（`sec:g2-braids-periods`）。

### F. 内部の対数周期・Looijenga period・非分裂MHS

新節 `papers/sections/quantum_cubic_log_periods.tex`。d=u²−1、N=(u²+2Au+2h)d+B²+C²+2uBC。conicの中心を移し、s²=d、a=T−(u+s)V、b=T−(u−s)Vを用いるとab=−N/d、omega=(du/s)∧dlog a。z=u+sでomega=dlog z∧dlog a。単純零点u_±を±1や他の根を避けて結ぶmatching球面の周期は2pi i[log(u+s)]_-^+（`thm:conic-matching-log-period`）。枝・道・向きを必ず指定し、退化u=±1へ無条件に適用しない。
A=B=C=0、−1/2<h<0では原点へ消える実球面を明示し、Pi0(h)=4pi asin sqrt(−2h)。自己交叉−2で原始的（`thm:explicit-morse-period`）。
Pi0とPi_inftyは2h(1+2h)y''+(1+4h)y'=0の二解。0と−1/2のmonodromyは[[1,0],[0,−1]]、[[1,0],[−1,−1]]で、無限二面体群。定数解を含むrank2解局所系は非分裂。全rank5ホモロジー作用を決定したわけではない。
指数化period P(gamma)=exp(integral_gamma omega/(2pi i))は境界cycleの持上げ非依存。Friedman Proposition3.12を用いてLooijenga対のD^perp→Pic0(D)=C*という線束制限と一致する。matching値はz_+/z_-なので有限根選択被覆上代数的。
零係数族ではQ=exp(Pi0/(2pi i))、Q+Q^-1=2+8h、h=(Q−1)²/(8Q)。SL2固有値/traceと同型な反転商が周期から現れるが、表現固有値そのものとの同定は未構成。
h=−1/10でQ=(3−4i)/5。Q+Q^-1=6/5は非整数なのでQは1の冪根でない。有理MHSが分裂すればF2の境界正規化が有理classとなりQが根の1になるため矛盾。よって0→Q(-1)^4→H²(U,Q)→Q(-2)→0は非分裂（`thm:explicit-nonsplit-MHS`）。局所系非分裂と点ごとのMHS非分裂は別主張。

## IV. 優先課題と具体的着手

**第一優先：四内部periodを同時に格子・代数座標へつなぐ。**
Nの四根のmatching pathと三つのconic pencilを組み合わせ、D4の整数基底を具体化する。交叉数を局所モデルまたは既存Milnor–Picard比較から確認し、各periodをz_i/z_jの積で書く。四根だけの差はrank3に留まる可能性があるので、u=±1や別pencilのcycleを欠落させない。全rank5 Gauss–Maninと、一本で計算したrank2解局所系を混同しない。

**並行して優先：Looijenga period、mirror、非Archimedeanとの具体的比較。**
Friedmanの積分/線束制限比較を使い、明示した代数的periodを境界上の線束gluingデータからも再計算する。Lai–Zhouのmirror period、Karwa–Laiの非Archimedean periodとの比較は、良い還元・モデル等の適用条件を確認してから進める。今回のQ(h)だけでSYZモデルや圏同値を構成したとはしない。非捩れ例を基準にMHS拡大の変動・捩れ特殊点の意味を調べる。

**並行して優先：braid・G2・triality。**
固定fiberのHurwitzと係数monodromyを分離したまま、period座標への作用を比較する。G2三成分の交換、D4/A2衝突、trialityが同じlogarithmic period atlasでどう見えるかを調べる。局所matrix factorization/Fukaya比較には対象と写像を明示する。

**支える課題：実幾何・判別式・H3成分。**
Cayleyのmodular延長、elliptope実sheetの壁、nearly Kähler共通凸体を保持。N5,M5のbranchと観測値衝突をtrace pairingで分離し、Painlevé VIと正確に比較する。重い大域消去を目的化しない。純粋q障害のSklyanin方向での相殺、Vietaの心の変更、全intrinsic降下・H3開性・全境界は保持するが、一枝に研究を固定しない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_logarithmic_periods.py
python3 computations/verify_all.py  # 全27検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回実行した新検証器はQと記号的平方根上でPASS。conic恒等式、留数形式、実球面、PF作用素、指数化period、monodromy行列、h=−1/10の値を確認。小証明書は `computations/logarithmic_periods_certificate.json`。
球面の構成、解析的積分・接続、Friedman比較、MHS非分裂は通常の証明と一次資料への依存であり、有限計算だけの検証ではない。旧26検証器は今回全再実行していない。
新節単体のLuaLaTeX wrapperは4頁で組版成功、全頁画像・内部参照・overfullなしを確認。主論文全体の今回の再組版、全旧証明の独立再監査、新規性の網羅調査は未実施。主論文の変更差分で既存証明を保持したことを確認し、要旨・Introduction・結果一覧に新成果を統合した。
生成物をGitへ入れず、push済み内容をLibraryへ保存しない。GitHub ref到達とファイル整合性は保存時に確認する。
