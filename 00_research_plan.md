# 研究方針：楕円E6成分とDAHA・character varietyの幾何学

2026-11-17 / triangle-component-v16。**再開時は本書を最初に読む。**
GitHub mainの現行ファイルだけで再開する。主論文は `papers/nc-cubic-e6.tex`。基本ノートは `research/research_notes.md`、関連分野の現行比較は `research/fricke_daha_comparison.md`、Poisson量子化と延長障害の要点は `research/poisson_order_notes.md`。これらは主題別の現行知識であって更新履歴ではない。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、面白さ、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。関連分野との接続は名称の類似で済ませず、正確な準同型、変形、圏的対応、障害として定式化する。
重要な方針変更では現在の理由と元の目標の達成部分・残存部分を明記し、時系列の変更履歴を蓄積しない。
証明済み、追加仮定付き、未完成、予想、計算的観察を区別し、主要主張の仮定・依存結果・証明箇所・未解決部分を明記する。原稿に証明があること、今回点検したこと、計算を実行したこと、独立査読を混同しない。誤りは依存する本文・要約・方針にも反映する。
先行研究は一次資料で確認し、適用範囲を具体的に比較する。未確認の文献内容・書誌・新規性を推測で埋めない。文献のPDFや検索結果を大量収録しない。
原稿は日本語LuaLaTeXを原則とする。関連分野で得た公表価値のある結果も**同じ主論文の適切な位置に統合する**。分割は数学的なまとまりと公表上の利点が明確な場合にのみ再検討する。価値ある既存成果と必要証明を軽量化のために削除しない。
研究ノートは有用な補題、着想、障害、反例、文献比較、再取得困難な情報を保持し、日誌や論文と重複する全文証明にしない。主張の状態・記法・参照を現行文書間で整合させる。
再開用の一式は現行方針・ノート・論文と、必要最小限のコード・入力・証明書・再現手順で自己完結させる。旧ZIP、旧原稿、バックアップ、更新記録、ログ、キャッシュ、コンパイル中間物は含めない。
研究区切りでの承諾不要Library保存は一般に許可されているが、**GitHubにpushした内容はLibraryへ重複保存しない**。GitHub mainを正本とし、push成功を確認した成果はGitHubのみで管理する。pushに失敗して未保存成果を保全する必要がある場合に限りLibraryを緊急退避先にできる。既存Libraryファイルは明示指示なしに削除しない。
日付・版番号を付け、生成・検証・commit・push・Library保存を別状態として報告する。約15分または数学的区切りでmainへ通常のfast-forward保存を行い、force push、不要なPR、GitHub Actionsは使わない。PDF・ZIPをGitで追跡しない。

## II. 現在の目標と達成基準

**上位目標は、非可換三次曲面の幾何学的理解・面白さ・公表価値の最大化である。**
既知の七次元H3族を含む楕円E6成分の完全決定を中心課題として保持し、DAHA/Askey--Wilson・四穴球面character variety・Goldman Poisson・skein・cluster/mirrorとの関係を具体的な結果へ発展させる。

成分分類の対象は構造対象付きexact同値によるintrinsic H3であり、任意の導来同値による商ではない。完全決定には成分の存在・一意性、次元・一般点、全対象の被覆、全矢・慣性、境界・交叉、相対再構成・降下が必要である。七次元族・八次元形式近傍・表示stack・結節中心因子は現在の到達点だが、全intrinsic族の代数化と全境界は未解決。

**現在の研究選択の理由。** root-of-unity交換子とGoldman括弧の関係は本稿の規約で確定した。一方、非Casimir切断は指定した純粋なq変形の平坦商に一次から持ち上がらず、Vieta作用も固定pointed H3心へは延長しない。したがって「qだけを動かす」「同じ心の自己同値を作る」をそのまま追い続けず、同時Sklyanin変形・境界の双有理変更・心を動かす導来対応を優先する。この障害は既存の八次元無障害変形と矛盾しない。
全H3分類の他の枝を本限定研究で置き換えない。

## III. 主要な到達点と確実性

1. **七次元正常形。** q²+q+1=0、包絡 `yz-qzy=tx+a t²`（巡回）。PBW/CY AS4、五つの中心三次、全中心式を保持。対称PBW行列の非対角成分は一意に平行移動で消え、対角非零部分は正常化される。楕円境界のH3開部分と全同型は `[V/A4]`。固定包絡四次元族は余次元3で成分ではない。主論文 `prop:pbw`, `thm:normal`, §2–3。
2. **三捩れからの横断積分。** Hesse曲線と平行移動点を使い、低次中心の消滅から9×9単元minorで指定中央三次を全次数に持ち上げる。Rees包絡・商は平坦。独立な超越的中心値では局所化からH3を得る。任意の数値Dや全パラメータでの開性は未証明。`lem:central-lift`, `prop:formal-integral`, `lem:generic-D`。
3. **八次元Hochschild変形。** 滑らかな三次中心C・反標準楕円境界D・記載した局所root order模型の下でHH⁰=k, HH¹=0, dim HH²=8, HHⁿ=0 (n≥3)。7方向の対数接束H¹と1方向のH⁰(O_C)。仮定とBrauer捩れを混同しない。`thm:HH8`。
4. **厳密な表示接空間と全Artin族。** 105×40行列rank18、核22、gauge rank14、商8。全Artin potential包絡の平坦性、中央三次同時持上げ、適合enhancement、逆Serre=次数シフトにより選んだ点の全Artin pointed Abel変形を認識する。`thm:artin-potential-envelope`, `thm:intrinsic-formal-eight`。一般Artin再構成だけから相対AS4性を先取りしない。
5. **代数的表示stackと成分。** 明示八変数族からsmooth DM表示stackを構成し、H3幾何学的対象間の全矢を回復する。一般非被約有限型底のintrinsic降下・全H3 locusの開性は別問題。八次元成分の一意性は `thm:conditional-component` の相対比較仮定付きであり、完全分類済みとはしない。
6. **結節中心因子。** 固定包絡では五つの独立な超平面条件がSNC因子、A4商で二成分。五つの孤立A1中心H3例を厳密に確認。a,b,cを動かすと一次元表現の連結有限étale五重被覆から既約六次元因子を得る。中心の特異性をH3境界と同一視しない。`thm:nodal-divisors`, `prop:five-nodal-witnesses`, `thm:seven-nodal-irreducible`。
7. **DAHA・Fricke・D4⊂E6。** AW中央特殊化とCasimir規約Omega_AW=3(q+2)Omega、Fricke係数への優越写像、量子的Vieta、Goldman型Jacobian括弧、三角形の直交D4根格子を明示。Goldman--Toledo、Naruki--Looijenga等の古典的内容は既知。一般楕円E6族を四穴球面DAHAそのものと同一視しない。`sec:daha-character`。
8. **量子化由来のPoisson order（証明・厳密実行）。** Q=q exp(h) と動かすと `{X,Y}=-9 P_Z`（巡回）、OmegaはCasimir。Fricke座標ではJacobian括弧の正確に9倍。Brown--Gordon Theorem4.2から同一Fricke切断のsmooth locusで有限次元中心fiber代数は同型。全DでM3となることは別途未確認。`thm:root-poisson-goldman`, `cor:root-poisson-fibers`。
9. **二つの延長障害（通常の証明と補助検算）。** G=Omega+beta X+gamma Y+delta Z+epsilon のPoisson主イデアル性、指定純粋q変形の一次平坦両側商への持上げ、beta=gamma=delta=0は同値。選択点G0で障害は9X(3Z−2Y)。Vietaのsigma(z)はPBW次数2、sigma(Z)は次数6なので固定pointed H3心へ延長しない。抽象変形・導来同値・心の変更は否定しない。`thm:poisson-cut-obstruction`, `prop:vieta-not-pointed-heart`。

10. **Casimir pencilの十Poisson零点とH3二類型。** 固定包絡a=b=c=0の総中心YはPoisson零点を正確に十点持つ。五点はYの通常二重点で全て一次元表現の中心character、他の五点はYの滑らかなCasimir臨界点。Casimir切断が特異になる値はD=0,2f/3,f,-f/3のみで、全特異点はA1型、個数は1,4,1,4。既存の固定包絡H3判定により、前二値はH3、後二値は非H3である。H3側の節点平滑化パラメータはD方向に二次接触、非H3側は一次横断。量子的VietaとA4は二つの四点集合でS4を生成する。主論文 `sec:casimir-poisson-leaves`、`thm:ten-poisson-points`、`thm:casimir-four-values`、`prop:casimir-smoothing-orders`。厳密検算 `computations/verify_casimir_poisson_leaves.py`。Poissonの十点分類は通常の証明で独立に求めたが、H3判定と文献新規性は別途区別する。

## IV. 優先課題と具体的な着手

**第一優先：障害を回避する幾何学的・圏的対応。**
純粋q方向と既存八変数Sklyanin族の一次potentialを同じ正規形で比較する。中心切断に対するPoisson障害が追加の三次potential方向でどう打ち消されるかを、既存中央持上げと接空間行列から抽出する。並行して、FrickeのVieta変換を境界のblow-up/downまたは導来圏の心の変更で実現する。まずアフィン局所化との可換図式、構造対象の像、K群・Euler形式を計算する。未構成の導来同値を既知のaffine同型から推論しない。

**第二優先：Poisson零点の相対被覆と、H3を検出する局所order。**
固定包絡ではCasimir pencilが十個のPoisson零点を5+5に分け、各種A1節点のH3可否を二次接触／一次横断で区別できた。次はa,b,c可変の三様体でPoisson零点schemeを有限表示・消去で調べ、二次接触部分と一次横断部分を相対的に追跡する。既存の七次元結節因子・一次元表現五重被覆と比較し、Poisson葉上の中心fiber代数および局所Morita模型による一般H3判定へつなぐ。全intrinsic八次元族へ移ると中心が常に大きいとは限らない点に注意する。

**第三優先：Casimir中心上の表現論・H3許容条件へ。**
Fricke sliceのsmooth locusで中心fiberが一定という帰結を使い、各Dで一つの9次元中心fiberを具体的行列代数として認識できる範囲を求める。例外的D、一次元表現・特異leaf、Azumaya locusを区別する。Brown--Gordonはfiberの同型を与えるが、有限globaldimやH3のZariski開性を自動的に与えない。一般楕円切断には今回の括弧が降りない点を必ず尊重する。

**第四優先：skein・DAHA・cluster/mirrorとの正確な比較。**
Baseilhac--RocheのFrobenius/Goldman比較、Huangのroot-of-unity中心、Terwilligerの普遍DAHA埋込みと本稿の表示を定理単位で照合する。中央特殊化後の単射性、spherical idempotentのfullness、Morita範囲を個別に確認する。Bousseauのmirror/theta構成と三角境界のPBW基底を比較し、D4周期・W(D4)作用と楕円E6・W(E6)作用を区別する。個々の式の文献上の既出性は未確定。

**第五優先：全intrinsic族の降下・成分閉包。**
表示stack内の全H3 admissibility、一般非被約底でのSerre作用・反標準環・二次包絡の底変更とfpqc降下を証明する。境界のsmooth/nodal/reducible型、PI位数、低次中心、Nakayama型、対角係数零、他chartへの移行を漏らさない。形式smooth性だけから開性を導かず、Rainsの次数3全被覆の未証明部分を輸入しない。

## V. 再現と検証範囲

リポジトリrootで実行する。
```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_root_poisson.py
python3 computations/verify_poisson_cut_obstruction.py
python3 computations/verify_casimir_poisson_leaves.py
# 全21検証器（今回の実行範囲とは区別）
python3 computations/verify_all.py
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回新規に実行したのはCasimir零点・平滑化次数・S4対称性の検証器で、厳密演算PASS。証明書は `computations/casimir_poisson_leaves_certificate.json`。関連分野の既存五検証器の実行結果は `computations/connections_validation.json` にある。その他15検証器も含め今回は全21検証器を再実行していない。
新Casimir節は独立wrapperでLuaLaTeX組版（3頁）し、初期版の頁を視覚点検した。主論文全体の今回の組版や独立査読は未実施。組版用wrapper・PDF・ログはGitに入れない。
今回の理論的証明の点検、有限恒等式の実行、文献の一次資料照合を区別する。全旧証明の独立再監査・新規性の網羅調査・全主論文の再組版は未実施。GitHub ref到達の確認は保存時に行う。Libraryには重複保存しない。
