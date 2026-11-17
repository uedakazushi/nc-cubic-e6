# 研究方針：非可換三次曲面から広がる幾何学

2026-11-17 / e6-connections-v19。**再開時は本書を最初に読む。**
正本はGitHub main。主論文は `papers/nc-cubic-e6.tex`。基礎的な研究知識は `research/research_notes.md`、DAHA・Fricke比較は `research/fricke_daha_comparison.md`、Poissonと二つの五次被覆は `research/poisson_order_notes.md`、新しいCayley・LG・実幾何の接続は `research/cayley_lg_connections.md` に置く。これらは主題別の現行知識であり、作業履歴の保存ではない。

## I. 恒常的な研究原則と保存許可

**最優先目標は、研究と論文を数学的に面白くすること。優先的な研究戦略は、できるだけ多様な話題との関連を発見し、検証可能な数学へ育てることである。** 面白さは、意外な同型・共通構造、概念の見通し、新しい問いや方法を生むこととして評価する。関連の名称を多く列挙することや定理の本数を増やすこと自体は目的にしない。
正確性はこの優先順位で犠牲にしない。数学的重要性、新規性、理解の深化、応用可能性、実現可能性も総合して全体の価値を最大化する。既定の分類問題を完走することが、より面白い接続より自動的に優先されるわけではない。
重要な方針変更では、現在の理由、元の目標で解決した部分・残る部分を簡潔に記す。時系列の変更履歴を蓄積しない。
証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。主要な主張に仮定・依存結果・証明箇所・未解決部分を付す。原稿に証明があること、今回その証明を点検したこと、計算実行、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。
先行研究は一次資料で確認し、適用範囲と本研究の貢献をIntroductionで比較する。未確認の文献内容・書誌・新規性を推測で埋めない。外部PDF・検索結果の大量収録はしない。
原稿は日本語LuaLaTeXを原則とし、関連分野で得た公表価値ある成果も**同じ主論文へ統合する**。独立論文への分割は数学的まとまりと公表上の利点が明確な場合に検討する。既存の価値ある成果・必要証明を削除して軽量化しない。
研究ノートには着想、補題、反例、失敗した方法の本質的障害、文献比較、再取得困難な情報を残す。日誌、過去の会話、重複証明、解決済み課題の経緯は不要。主論文に十分な証明があるものは参照する。
現行方針・ノート・論文と最小限のコード・入力・小証明書・再現手順だけで再開できるようにする。旧版ZIP、旧原稿、バックアップ、更新記録、ログ、キャッシュ、コンパイル中間物は収録しない。軽量化のために数学的内容を損なわない。
研究区切りの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryに保存しない**。GitHub mainを正本とし、push成功後は重複保存しない。pushに失敗して未保存成果の保全が必要な場合だけLibraryを緊急退避先にできる。既存Libraryファイルは明示指示なしに削除しない。
主要文書に日付・版番号を付け、生成・検証・commit・push・Library保存を別状態として報告する。約15分または数学的区切りで通常のfast-forward保存を行い、force push、不要なPR、GitHub Actionsは使わない。PDF・ZIPはGitで追跡しない。未実行の検証をPASSと言わない。

## II. 現在の中心的な問いと達成基準

中心的な問いは、**同じ非可換三次曲面の具体的な表示から、どれほど多様な幾何が回復され、その相互関係が何を説明するか**である。

現在の共通例は三乗根の量子so3包絡、中心三次切断、一次元表現の五重被覆である。中心は四穴球面のFricke幾何へ、root-of-unity変形はPoisson orderへ、一次元表現はLandau–Ginzburgの臨界点族へつながる。さらに五重被覆のramification divisorがCayley曲面となり、トーラス指標多様体、D4の局所変形とtriality、Frobenius代数、pillowcase、相関行列の凸幾何が同じ写像に現れる。

元の八次元E6成分の完全決定は保持する。七次元正常形、横断積分、八次元形式近傍、代数的表示stack、結節因子、二つの五次被覆までは本文に証明がある。全intrinsic H3の相対代数化・降下・全境界は未解決。これらの完成を、新たな関連分野を研究するための前提にはしない。

接続の達成基準は、具体的な写像・方程式・局所モデル・作用・圏的対応・障害の少なくとも一つを正確に記述すること。既知の構造の新たな出現、独立に確認した公式、本研究の新規性候補を分ける。完全な圏同値を作る前でも、有効な局所モデルや反例は主論文へ組み込む。

## III. 現在有効な主要成果と所在

### A. 非可換三次曲面と変形・モジュライ

七次元の中央PBW正常形、全係数CY AS4、中心の全三次関係、固定包絡四次元部分の非成分性を保持する（主論文 `prop:pbw`, `thm:normal`, §2–3）。中央境界・対角非零の適用範囲を外さない。
Hesse曲線と平行移動を使う横断変形は全次数平坦で、独立な超越的中心値でH3となる（`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`）。任意の数値中心値のH3性は別問題。
滑らかな三次中心・反標準楕円境界・指定局所order模型の下でHH²=8、HH³=0（`thm:HH8`）。105×40行列rank18、gauge14、接空間商8を厳密確認。全Artin表示族と指定enhancementの認識、smooth DM八次元表示stackを構成した。一般非被約底のintrinsic降下・H3開性・全大域境界は未完成。`thm:conditional-component` の比較仮定を無断で外さない。

### B. 結節中心とPoisson・DAHA

固定包絡では五つの結節中心SNC因子、A4商で二成分。一般低次係数では一次元表現の連結五重被覆から既約六次元因子を得る（`thm:nodal-divisors`, `thm:seven-nodal-irreducible`）。中心特異性とH3境界は同じではない。
AW中央特殊化、Casimir規約Omega_AW=3(q+2)Omega、Fricke係数写像、量子的Vieta、古典的D4⊂E6を明示（`sec:daha-character`）。Q=q exp(h)の中心交換子微分はGoldman型Jacobian括弧の9倍。Brown–Gordonにより固定Fricke sliceのsmooth locus上の中心fiber代数は同型（`sec:root-poisson-orders`）。全DでM3になることやMorita同値は未確認。
非Casimir切断は指定した純粋q変形の平坦商へ一次にも持ち上がらず、Vietaは固定pointed H3心へ延長しない。抽象変形・Sklyanin同時変形・心の変更を否定するものではない。
固定包絡の十Poisson零点は五節点と五滑らかなCasimir臨界点。特異値0,2f/3,f,-f/3は全てA1型で、既存H3判定により前二値だけH3。二次接触／一次横断とS4作用も明示（`sec:casimir-poisson-leaves`）。

### C. 二つの独立な五次被覆

相対Poisson臨界スキームは全係数で有限平坦次数15、一次元表現は次数5。Casimir臨界値多項式はDelta15=N5²M5。両五次因子は幾何学的に既約で、同時Galois群はS5×S5、分解体は線型非交叉（`sec:relative-poisson-cover`, `thm:paired-quintic-S5`）。原点でDだけの多項式に重根があっても、四中心座標を保った残余被覆はetaleである。
証明は二素数のFrobenius型、Goursat補題、有理完全分裂fiberと基本群完全列を用いる。有限体計算のPASSと幾何学的証明を区別する。一般係数のH3判定、分岐・値衝突因子の具体式、文献新規性は未解決。

### D. Cayley・Landau–Ginzburg・D4・実幾何

主論文 `sec:cayley-lg-connections` に統合した。
正規化一次元表現写像はPhi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。W=H−Au−Bv−CwのJacobi代数はrank5で、graph(dH)はexact Lagrangian。
ramification divisorはR=u²+v²+w²+2uvw−1=0。これはCayley三次曲面で、(Gm)²の同時反転商、すなわち閉トーラスのSL2粗指標多様体。対数Poisson括弧も具体的に同定（`thm:ramification-cayley-torus`, `prop:ramification-log-poisson`）。元の非可換中心とは別の空間である。
Rの四節点に対応するfiberは長さ4のD4局所Jacobi環と一つの単純点。三係数は加法定数を除くミニバーサル変形で、巡回置換は三枝を回す位数3作用（`thm:character-D4-unfolding`, `cor:gradient-local-triality`）。局所Milnor格子と既存Picard D4の標準同定は未構成。
原点のrank5 Jacobi代数に留数対を明示し、非退化性を厳密確認。Casimir値衝突と被覆自体の分岐の違いを例と判別式の基底変換式で示した（`prop:jacobi-residue-maxwell`）。
実型のelliptopeは負Hessianの半正定値領域で、境界はSU2トーラスのpillowcase。内部の厳密凹性から実sheetが高々一つ（`prop:elliptope-gradient-injective`）。Dixonのnearly Kähler S3×S3 multi-moment像と同じ凸体だが、圏同値・metric degenerationを意味しない。

## IV. 優先する探索と具体的な着手

**第一優先：異なるD4を比較し、trialityと局所圏の接続を作る。**
今回のD4 germのMilnor fiber、vanishing cycle、局所monodromyを計算し、三次曲面の反標準三角形に直交するPicard D4との比較写像を探す。三枝巡回作用が両側でどの作用になるかを確認する。単なる格子型の一致やG2という名称から圏同値を推論しない。最初の具体課題は4+1 fiberの局所消滅サイクルとパラメータのKodaira–Spencer基底の対応。

**並行して優先：LG・留数代数とmirror/Fukayaの接続。**
Wの臨界点とCasimir観測量を別々に扱い、臨界値写像、留数対、Gauss–Manin系の最小模型を構成する。rank5 Jacobi代数だけから三次曲面全体のmirrorやFukaya–Seidel同値を主張しない。局所D4模型、matrix factorization、境界局所化のどこに自然な比較があるかを探す。

**並行して優先：トーラス・pillowcase・実安定性。**
Cayley上の単項式modular作用が五重被覆全体へどの範囲で延びるかを試す。elliptope内部の一意sheetと外側の実sheetの出現、壁・安定性との関係を調べる。nearly Kählerとの共通凸体は既知比較として保持し、追加の写像・形式・fibrationが構成できる場合だけ強い主張へ進む。

**支える課題：判別式、Poisson局所order、八次元成分。**
N5,M5の分岐因子と観測値衝突因子をtrace判別式と基底変換行列で分離する。Painlevé VIのtrace判別式との係数写像の比較を行う。重い大域消去を反復するより、局所模型・不変量・反例を先に取り、興味深い意味が見えた計算を深める。
純粋q変形の障害相殺をSklyanin方向で明示し、Vietaの境界双有理変更・導来圏の心の変更を探す。全H3 admissibility、intrinsic降下、全境界は維持するが、これら一枝だけに全作業を固定しない。

探索は複数の入口を持たせるが、各区切りで成果を現在の主論文・ノートへ整理する。着想だけの接続は未構成と明記し、具体的帰結が得られない類似を大きな定理に見せない。

## V. 再現・検証・保存

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_cayley_lg_connections.py
python3 computations/verify_all.py  # 全24検証器。今回の実行範囲とは別
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回実行したのは新しいCayley/LG検証器1本。Cayley・トーラスPoisson恒等式、D4局所化Jacobi環、三versal方向、4+1 fiber、位数3作用、原点留数対を有理数体上の記号演算で確認しPASS。小証明書は `computations/cayley_lg_connections_certificate.json`。不変環生成、解析的右同値、versal性判定、実凹性は本文の通常の証明である。
新節の一時的LuaLaTeX wrapperは5頁で組版成功。本文外の二つの参照は独立wrapperでは未解決であり、これを主論文全体の組版成功とは報告しない。主論文への入力・文献キーをGitHub保存後に確認する。旧23検証器の今回は全再実行をしていない。
主論文の題名・要旨・Introduction・結果一覧を、分野間の接続が読める現在の構成へ改稿した。既存の数学的証明と全入力節は保持する。PDF・一時wrapper・画像・ログはGitに含めず、pushした内容をLibraryへ保存しない。
