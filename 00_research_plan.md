# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v24。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎知識は `research/research_notes.md`、DAHA・Frickeは `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、LG・G2・braidの基礎は `research/cayley_lg_connections.md`、四周期・triality・三成分Hodge比較の現行知識は `research/conic_period_coordinates.md`。現行一式だけで再開し、旧bundleや会話履歴を前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先目標は数学的に面白くすること。優先的戦略は、多様な話題との具体的な関連を見つけ、検証可能な数学へ育てることである。** 意外な同型・共通構造、見通し、新しい問いや方法を重視し、名称や定理の本数を増やすこと自体を目的にしない。
正確性は犠牲にしない。数学的重要性、新規性、理解の深化、応用可能性、実現可能性を総合して研究価値を最大化する。既定の分類を完走することが面白い接続より自動的に優先されるわけではない。
重要な方針変更では現時点での理由と元の目標の達成部分・残存部分を簡潔に記し、時系列の変更履歴を蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を示す。原稿に証明があること、今回点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。
先行研究は一次資料で確認し、仮定・適用範囲・本稿の貢献をIntroductionで具体的に比較する。未確認の内容・書誌・新規性を推測で補わず、不明点を明示する。外部PDF・検索結果を大量収録しない。
原稿は日本語LuaLaTeX。関連分野の公表価値ある成果も同じ主論文の適切な位置へ統合する。分割は数学的まとまりと公表上の利点が明確な場合に検討する。軽量化のために価値ある成果・必要証明を削除しない。
研究ノートは有用な着想・補題・計算・反例・本質的障害・文献比較・再取得困難な情報を保持する。日誌、会話、更新履歴、重複証明にせず、論文に十分な証明があれば参照する。
現行方針・ノート・論文と最小限の原稿、コード、入力、小証明書、再現手順を自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・組版中間物を除き、数学的内容と検証可能性は保持する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryへ保存しない**。push失敗で未保存成果を保全する必要がある場合のみ緊急退避できる。既存Library資料は明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を別状態として報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行う。force push、不要なPR・Actionsを使わず、PDF・ZIPをGitで追跡しない。未実行をPASSと言わない。

## II. 現在の問いと到達基準

**同じ非可換三次曲面から回復される幾何を、写像・作用・変形・周期で結ぶ。** 量子中心はFrickeへ、一次元表現被覆はLG・Cayley・D4へ、対称LGはG2へつながる。現在は周期torusを使って、この最後のG2三成分写像の意味を整数格子から説明できた。
trialityの不変格子と余不変格子の指数3が、周期isogeny `(xi,eta)->(xi,eta^3)` を与える。そのWeyl商がBoalch–Palubaの既知三成分写像に一致する。共通の明示開集合で三成分の有理MHSを同定できるが、整数拡大類の違いは残る。Klein例でその位数は7,21,21となる。
また、ホモロジーと全periodへ自明に作用しながら正entropyを持つ自己同型を、Goldman–NeumannとCantat–Lorayの既知定理の適用として明示できた。従って周期で見える違いと見えない力学を分け、前者を算術へ、後者を境界変更・局所化した圏へ結ぶことを重視する。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二五次被覆の本文の証明は保存済み。全intrinsic H3の相対代数化・降下・大域境界は未完成だが、他分野との接続の前提にはしない。
達成基準は、具体的写像、変形、局所模型、格子写像、圏的対応、障害、周期式のいずれかを正確に与えること。既知理論、明示的適用、新規性未確認の帰結を区別し、型・群名・数値の一致だけで同一視しない。

## III. 現在有効な主要成果

### A. 変形・モジュライ

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）。中央境界・対角非零の適用範囲を外さない。
横断積分は全次数平坦、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族、指定enhancement、smooth DM八次元表示stackを保持。一般非被約底のintrinsic降下・H3開性・全境界は未完成で、`thm:conditional-component`の比較仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般係数の既約六次元結節因子。中心特異性とH3境界は異なる。
AW中央特殊化、Casimir規約、Fricke係数写像、量子的Vieta、古典的D4⊂E6。Q=q exp(hbar)の中心交換子は指定Goldman型括弧の9倍。Brown–Gordonによるsmooth locusの中心fiber比較。全DでのM3やMorita同値は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVietaには障害。一般変形・心の変更を否定しない。
固定包絡の十Poisson零点は五節点と五滑らか臨界点。四Casimir特異値のA1型、既存判定下のH3可否、二次接触／一次横断、S4作用を明示。
相対Poisson臨界環は全域有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、同時幾何Galois群S5×S5。有限体検算と群論・基本群の通常証明を区別する。今回はこれら旧主張を独立再監査したとはしない。

### C. Cayley・LG・Milnor・Picard

Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。W=H−Au−Bv−CwのJacobi環はrank5、graph(dH)はexact Lagrangian。分岐源はCayleyの閉トーラスSL2指標多様体。D4ミニバーサル変形、三枝巡回、留数対、実elliptopeとpillowcase、内部実sheetの一意性を明示。
滑らかなU=S\Dで0→Z delta_infty→H2(U,Z)→D^perp→0。右端D4(-1)、左端原始radical。指定D4退化のMilnor包含はPicard直交補へ整数同型。判別群から両方の外部trialityを検出する。全域の標準分裂ではない。
MHS graded piecesはGr2=Q(-1)^4、Gr3=0、Gr4=Q(-2)。無限遠はmonodromy−IのT2束でpillowcaseとは別。nearly Kähler S3×S3の共通elliptopeは既知比較で、圏同値・計量退化は未構成。

### D. G2・braid・対数周期

Boalch–Palubaの既知G2実現を対称LGへ適用し、unipotent底(6,6)でD4とA2の二成分が現れる。三成分ラベルのA2根被覆と成分内Hurwitz B3は別作用。HurwitzはW・体積・Poissonを保ち、Chebyshev反復を持つ。
Klein七点の置換像S7（5040）と、表現像G2(2)'（6048）、Klein群168を区別する。
omega=du∧dv/(uv−w−C)、原始境界周期は(2pi i)²。適切なconic matching周期は2pi i[log(u+sqrt(u²−1))]。係数零のMorse周期は4pi arcsin sqrt(-2h)、rank二解局所系のmonodromyは無限二面体、指数化Q+Q^-1=2+8h。h=-1/10は有理MHS非分裂例（`sec:logarithmic-periods`）。

### E. 全四periodと円分性

`sec:four-D4-periods`はDisc N≠0、B²−C²≠0のconic開集合。compatible成分選択を縮約してF1標識を得る。Kはeven-sum Z4で、整数基底は(E1−E2,E2−E3,E3−E4,E3+E4−F)。四periodは `(z1/z2,z2/z3,z3/z4,z3*z4)`。
指数行列det2、kernel共通±1、quartic係数Jacobian16(C²−B²)。root hypertorus型判別式を得る。有理Hodge分裂⇔全period捩れ⇔全zi捩れ。
有理係数の分裂例(1/4,1/2,1/4,1/8)は9乗根、非分裂例(-65/16,75/16,-65/16,3575/288)はzi=2,3,4,6または逆数。成分選択・標識を省略しない。Wの臨界値、Casimir値、被覆の分岐は別現象。

### F. trialityのperiod isogenyと三成分Hodge比較

新節 `papers/sections/quantum_cubic_triality_isogeny.tex`、`sec:triality-period-isogeny`。
Goldman–Neumannの既知ホモロジー定理により対称Hurwitz像は外側三根のS3、純braidはH2で自明。Kの基底(c,o1,o2,o3)で周期は(xi,eta,eta,eta)。不変格子は(c,s=o1+o2+o3)、余不変は(cbar,obar)、自然写像diag(1,3)。Gram不変は[[-2,3],[3,-6]]。制限torus写像は `(xi,eta)->(xi,eta^3)`、kernel mu3。
S=sum_{t=eta,xi eta,xi eta²}(t+t^-1)、L=sum_{t=xi,xi eta³,xi²eta³}(t+t^-1)。lambda=(S+2)/4、h=(L+3S+4)/8。
対称族B=Cは従来の開条件外なので別証明が必要。quarticは(u+1)prod_t(u+(t+t^-1)/2)。明示line sectionと非交叉を用いてcompatible成分を選び、z=(-xi eta²,-xi eta,-eta,-1)、四period=(eta,xi,eta,eta)を実現する。六root character≠1、eta,xi eta,xi eta²≠−1の開条件を保持する（`thm:symmetric-period-reconstruction`）。
W(G2)不変量はS,L。isogenyのWeyl商はalpha=L、beta=S³−3SL−9S−6L−12。b_F=−S−2,c_F=L+3S+4と置くとBoalch–Palubaの底写像に正確に一致する（`thm:G2-period-isogeny-quotient`）。これはtorusのisogenyであり、標数零G2群の非自明な中心isogenyではない。
regular底の三持上げ(xi,zeta^j eta)が全て明示開集合にある範囲では、三成分の正規化periodは外側方向でj/3だけ異なる。有理MHSは標識graded pieceの下で同型、分裂可否も同時。全底上の標準VMHS同型や曲面同型は未主張（`thm:G2-companion-rational-Hodge`）。
Kleinではxi=eta=primitive7root、S=L=-1。Fricke(b,c)=(-1,0)と同じG2底の二成分b=(-5±sqrt21)/2,c=−3−3bの整数Hodge拡大類の位数は7,21,21。全て有理分裂だがKleinとコンパニオンの整数MHSは非同型（`cor:Klein-seven-twentyone-Hodge`）。他二成分の有限Hurwitz軌道は未主張。
g=iota_v iota_w iota_u iota_wは全H2・periodで恒等、しかしCantat–Lorayの既知定理からlambda1=3+2sqrt2、entropy=log(3+2sqrt2)。周期が見ない正entropyの具体例（`prop:period-invisible-entropy`）。

## IV. 優先課題と着手方法

**第一優先：三成分を結ぶ有理Hodge同型の幾何学的意味。**
指数3のperiod isogenyを、境界線束の3捩れ変更、代数的対応、有限被覆のどれとして実現できるか調べる。まずKlein/二コンパニオンでコンパクト化のline配置と境界gluingを比較する。有理Hodge同型から曲面の同型、導来同値、動機の同型を推論しない。整数拡大位数7対21は比較を試す際の有効な障害である。

**並行して優先：周期に見えない正entropyを何が検出するか。**
具体的word gの境界blow-up/down列を作り、射影Picardの拡大格子、cluster tropical作用、局所化した圏の作用を比較する。アフィンH2では自明という既知結果と、射影双有理次数の増大を混同しない。圏的entropyやFukaya自己同値は構成対象であり、今回は未計算。

**並行して優先：算術的period、例外群とfolding。**
Kleinの7/21を他のtorsion点へ広げ、mu3で拡大位数がどう変わるかを正確に分類する。有限Hurwitz軌道・量子化のroot-of-unity条件・period捩れ性は別。Spin8の8→1+7、28→14+7+7によるcharacter係数と、長短根交換isogenyの関係を掘り下げる。Langlandsや量子群との圏同値を名称から主張しない。

**支える課題：全周期接続と非可換成分。**
四periodの対数微分から代数的de Rham基底のrank五接続を構成する。対称族の有理MHS比較をglobal VMHSとする際の標識・monodromy障害を求める。N5,M5のbranch・観測値衝突はtrace判別式で分ける。Sklyanin方向での純粋q障害相殺、Vietaの心の変更、全H3 admissibility・intrinsic降下・全境界は維持し、一枝だけに研究を固定しない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_triality_period_isogeny.py
python3 computations/verify_all.py  # 全29検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回、新しいtriality/period isogeny検証器を実行しPASS。整数格子・有理Laurent恒等式・Q(zeta21)で、指数3、root制限、quartic分解、実際のline sectionと非交叉、Weyl不変量、BP写像、Klein三成分の位数7/21/21、力学のSL2行列を確認した。小証明書は `computations/triality_period_isogeny_certificate.json`。
ホモロジー作用、conic縮約・period比較、Hodge拡大、entropyは本文の通常証明・一次資料への依存。計算だけの形式検証ではない。旧28検証器は今回全再実行していない。
新節単体をLuaLaTeX wrapperで5頁に組版し、画像・内部参照・overfullなしを点検した。主論文全体の今回の再組版、旧定理の独立再監査、新規性の網羅調査は未実施。
主論文の差分を確認し、既存証明本文・入力節を保持して新節を統合した。GitHub保存後にmain refと必要ファイルを確認する。生成PDF・wrapper・画像・ログをGitへ入れず、push済み内容をLibraryへ保存しない。
