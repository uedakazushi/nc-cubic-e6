# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v20。**再開時は本書を最初に読む。**
GitHub mainが正本。主論文は `papers/nc-cubic-e6.tex`。基礎知識は `research/research_notes.md`、DAHA・Fricke比較は `research/fricke_daha_comparison.md`、Poissonと二五次被覆は `research/poisson_order_notes.md`、Cayley・LG・格子・G2の接続は `research/cayley_lg_connections.md`。主題別の現行知識として整理し、旧bundleの取得を再開の前提にしない。

## I. 恒常的な研究原則と保存許可

**最優先目標は研究と論文を数学的に面白くすること。優先的な戦略は、多様な話題との具体的な関連を見つけ、検証可能な数学へ育てることである。** 意外な同型・共通構造、見通し、新たな問いや方法を重視する。関連の名称や定理の数を増やすこと自体は目的にしない。
正確性はこの優先順位で犠牲にしない。数学的重要性、新規性、理解の深化、応用可能性、実現可能性を総合して価値を最大化する。既定の分類の完遂が、より面白い接続より自動的に優先されるわけではない。
重要な方針変更では現在の理由と元の目標の達成部分・残存部分を簡潔に示し、時系列の履歴を蓄積しない。
証明済み、仮定付き、未完成、予想、計算的観察を区別する。主要主張の仮定、依存結果、証明の所在、未解決箇所を明記する。原稿に証明があること、今回点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。
先行研究は一次資料で確認し、適用範囲と本研究の貢献をIntroductionで比較する。未確認の内容・書誌・新規性を推測で埋めない。外部PDF・検索結果を大量収録しない。
原稿は日本語LuaLaTeXを原則とする。公表価値ある関連分野の成果も同じ主論文へ統合する。分割は数学的まとまりと公表上の利点が明確な場合に検討する。軽量化のために価値ある成果や必要証明を削除しない。
研究ノートは着想・補題・反例・障害・文献比較・再取得困難な情報を保持し、日誌、会話、更新履歴、重複証明にしない。論文に証明がある事項は参照する。
現行方針・ノート・論文と最小限のコード・入力・証明書・再現手順で自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・中間生成物は含めない。数学的内容と検証可能性を損なわず整理する。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryへ保存しない**。push失敗で未保存成果の保全が必要な場合だけLibraryを緊急退避先にできる。既存Libraryファイルは明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を区別して報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行う。force push、不要なPR・Actionsは使わず、PDF・ZIPをGitで追跡しない。未実行をPASSと言わない。

## II. 現在の問いと達成基準

中心的な問いは、**同じ非可換三次曲面の代数から多様な幾何がどう回復され、実際の写像・作用・変形で結ばれるか**である。
現在の共通例は三乗根の量子so3、中心三次切断、一次元表現の五重被覆。中心は四穴球面のFrickeへ、量子化はPoisson orderへ、一次元表現はLG臨界点族へつながる。分岐源はCayleyで閉トーラスの指標多様体、局所四sheet衝突はD4である。
今回、このD4のMilnor格子をLG近傍等位面のPicard直交補へ包含で同定できた。さらに対称LG族をBoalch–PalubaのG2実現へ移すと、D4衝突と従来のsimple foldによるA2衝突が同じG2退化の二成分となる。これを軸に局所・大域・例外群・周期の接続を深める。
元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍・表示stack、結節因子、二つの五次被覆は本文に証明がある。全intrinsic H3の相対代数化・降下・全境界は未完成だが、新しい接続研究の前提にはしない。
達成基準は、具体的な準同型、変形、局所模型、格子写像、圏的対応、障害のいずれかを正確に与えること。既知の一般理論と本稿での明示的適用、新規性未確認の結果を分ける。型や名称の一致だけで同一視しない。

## III. 主要成果と所在

### A. 変形・モジュライの既存成果

七次元中央PBW正常形、全係数CY AS4、全中心式、固定包絡四次元部分の非成分性（`prop:pbw`, `thm:normal`）を保持。中央境界・対角非零の適用範囲を外さない。
横断積分は全次数平坦で、独立な超越的中心値でH3（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、商8。全Artin表示族と指定enhancement、smooth DM八次元表示stackを構成。一般非被約底のintrinsic降下・全H3開性・大域境界は未完成で、`thm:conditional-component`の仮定を外さない。

### B. Poisson・DAHA・二五次被覆

固定包絡の五結節SNC因子、A4商の二成分、一般低次係数での既約六次元結節因子を保持（`sec:nodal-centers`）。中心特異性とH3境界は同じではない。
AW中央特殊化、Casimirスケール、Fricke係数写像、量子的Vieta、古典的D4⊂E6（`sec:daha-character`）。Q=q exp(h)の中心交換子は指定Goldman型括弧の9倍、Brown–Gordonによるsmooth locusの中心fiber比較（`sec:root-poisson-orders`）。全DでのM3やMorita同値は未確認。
非Casimir切断の純粋q変形と固定pointed H3心へのVieta作用には障害。一般変形や心の変更を否定するものではない。
固定包絡の十Poisson零点は五節点と五滑らか臨界点。四Casimir特異値のA1型、既存判定下でのH3可否、二次接触／一次横断、S4作用を明示。
相対Poisson臨界環は全域有限平坦次数15、一次元表現環は次数5。Delta15=N5²M5、二五次の同時幾何Galois群S5×S5（`sec:relative-poisson-cover`）。算術有限体検算とGoursat・基本群の通常証明を区別する。今回これら旧定理を独立再監査したとはしない。

### C. Cayley・LG・実幾何

`sec:cayley-lg-connections`ではPhi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。W=H−Au−Bv−CwのJacobi環はrank5、graph(dH)はexact Lagrangian。
ramification divisorはCayley曲面で閉トーラスのSL2粗指標多様体。対数Poisson括弧、四sheetのD4ミニバーサル変形、巡回三枝作用を明示。原点Jacobi留数対は非退化。
原点では五重被覆がetaleでもCasimir値が四重に衝突する。被覆の分岐・Casimir値衝突・Wの臨界値衝突を区別する。
実elliptopeの境界はSU2トーラスpillowcase、内部の厳密凹性から実sheetは高々一つ。Dixonのnearly Kähler S3×S3のmulti-moment像との共通凸体は既知比較であり、圏同値や計量退化は未構成。

### D. 局所MilnorからPicardへ、さらにG2へ

証明は `papers/sections/quantum_cubic_lg_picard.tex`（主論文に直接入力）。
LG等位面W=hはp=-2u等でFricke係数(-4A,-4B,-4C,8h)となる。非可換Casimir中心との係数底変更も明示し、一次元表現の正規化A=(1-q)aと混同しない。
滑らかなU=S\Dに整数完全列 0→Z delta_infty→H2(U,Z)→<D_i>^perp→0。右端はD4(-1)、左端は原始radical、H1(U)=0。指定D4退化(A,B,C)=(2,2,2), h≈7/2で、局所Milnor fiberの包含が右端への整数格子同型を与える（`thm:lg-D4-Picard`）。rank4・det4の双方と交叉保存を使う。**選択した退化に対する同型**であり、全域で選択非依存な標準分裂ではない。
巡回置換は境界の判別群(Z/2)²の三非零元を回し、unimodular gluingを介してPicardと局所Milnorの双方の外部trialityを検出する（`cor:lg-picard-triality`）。
Goldman–Neumannの既知affine D4形式のprimitive radicalは(1,1,1,1,2)。無限遠はmonodromy −IのT2束、H1はZ⊕(Z/2)²。pillowcase自体とは異なる。
混合Hodge構造のgraded piecesはGr2=Q(-1)^4, Gr3=0, Gr4=Q(-2)、E_c=1+4xy+(xy)²。拡大の分裂は未主張（`prop:lg-mixed-hodge`）。
Boalch–Palubaの既知定理を対称LG A=B=C=lambdaへ適用。b=-4lambda,c=8h、alpha=8h+2−12lambda、beta=64lambda³+48lambda²−96lambda h−12lambda−2。regular semisimple範囲でLG等位面はG2指標多様体の三成分の一つ。第四共役類をregular unipotentの閉包にするとalpha=beta=6で、(lambda,h)=(2,7/2)のD4成分と(-1/4,1/8)のA2成分が現れる。後者は従来のS5証明のsimple fold。同論文の定理の再発見ではなく、二つの既存模型を結ぶ適用である。

## IV. 優先課題と具体的着手

**第一優先：G2という共通実現から局所と大域の作用を比較する。**
D4とA2を同時に含むG2退化の近傍で、二成分のmonodromy、braid作用、vanishing cycleの配置を記述する。最初にBoalch–Paluba §5の具体的braid式を本稿のLG座標へ移し、今回のPicard/D4作用と比較する。三連結成分のどれを選ぶかと、その交換monodromyを分ける。G2型量子代数や圏同値を既知の古典同型から推論しない。

**並行して優先：境界方向と周期・mirror。**
今回のMilnor–Picard同型を使い、H2の四方向と境界radical一方向を基底化する。混合Hodgeの拡大類、log 2-formのperiod、LGのGauss–Manin系を小さい模型から計算する。重みのgraded pieceだけで拡大の分裂やprimitive formを結論しない。局所D4のmatrix factorization/Fukaya比較へ進む場合は対象・写像・構造対象の像を明示する。

**並行して優先：Cayleyと実安定性。**
トーラスmodular作用の五重被覆への延長範囲、elliptope内の一意sheetと外部sheetの実壁を調べる。nearly Kählerとの共通凸体は保持し、追加の幾何学的写像・形式・fibrationが実際に構成できた場合にだけ強い接続へ進む。

**支える課題：判別式・H3・八次元成分。**
N5,M5のbranchと観測値衝突をtrace pairingと基底変換因子で分離する。Painlevé VIの係数写像との比較を行う。重い大域消去を反復するより、構造・局所例・反例を先に取る。純粋qの障害相殺をSklyanin方向で明示し、Vietaの心の変更を探す。全intrinsic降下・H3開性・全境界は維持するが、一枝だけに研究を固定しない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_lg_picard_g2.py
python3 computations/verify_all.py  # 全25検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回、新しいLG/Picard/G2検証器を実行しPASS。Q上の記号計算・整数格子で、Fricke座標、Gram行列、unimodular基底変換、判別群の巡回、affine D4、境界monodromy、G2係数と二特異値を確認した。小証明書は `computations/lg_picard_g2_certificate.json`。
整数比較完全列・ADE Milnor格子・gluing・混合Hodge・G2指標多様体同定は通常の証明と一次文献への依存であり、計算だけで検証されたとはしない。旧24検証器の今回の全再実行は未実施。
新節単体をLuaLaTeX wrapperで組版（4頁）、頁を画像点検し、overfull boxを修正した。新節の内部参照は解決済み。主論文全体の今回の再組版、全旧証明の独立再監査、新規性の網羅調査は未実施。
既存の数学的証明・入力節を保持し、主論文の要旨・Introduction・結果一覧に今回の接続を統合した。生成物をGitへ入れず、push済み内容をLibraryへ保存しない。
