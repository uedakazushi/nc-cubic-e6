# 公表用原稿の状態と検証範囲

2026-11-18 / publication-v33

本書は、現行原稿に証明があること、今回点検したこと、計算で確認したことを区別する。研究の再開入口と次の課題は [研究方針](../00_research_plan.md) に置く。いずれの原稿も、新規性の網羅調査と独立査読を完了した投稿確定稿ではない。

## 1. 現行の公表用原稿

| 原稿 | 組版 | 現在の主張の範囲 |
|---|---:|---|
| papers/nc-cubic-e6.tex | 34頁 | R(1,3)中心三次商との係数比較、七次元PBW正常形、指定局所orderの下での八次元Hochschild変形、全Artin形式表示と再構成。全H3の相対認識・開性・降下を必要とする大域成分定理は条件付き。 |
| papers/fricke-geometry.tex | 45頁 | AW/Fricke表示、根でのPoisson構造、二つの五次被覆、整数D4格子、指定標識での四周期、trialityと周期トーラスのisogeny。本文の通常証明と外部入力を区別する。 |
| papers/cubic-boundary-prym.tex | 30頁 | Pell境界付値、局所化前後の成長率、二枝の位相・解析modulus、重み付き主部の局所圏とMilnor被覆のPrym偏極。実germと重み付き主部の圏同値は一般には主張しない。 |

三原稿は日本語LuaLaTeXであり、共通の組版設定と文献情報を papers/shared/ に置く。元の総合原稿にあった定理・証明は対応する原稿へ配置した。補助的なH3認識の入力断片は、それ自体で外部依存を閉じた証明と見なさず、研究ノートの入力表から参照する。

## 2. 原稿の証明と一次資料の確認範囲

今回の数学的点検は、R(1,3)との係数比較・次元の区別・成分主張の範囲に集中した。Pymの一次本文§3.4 (9)とambient原稿の中心三次ペンシルを確認し、新比較節に通常の証明を置いた。以下の既存結果の確認情報は保持するが、従来の全証明・一次文献を今回もう一度独立監査したという意味ではない。

| 論点 | 点検した範囲・所在 | 残る限界 |
|---|---|---|
| R(1,3)比較 | 新節 e6_r13_comparison.tex。巡回potentialの交代・対称分解、八変数族の係数変換、Hesse判別条件、一般rank2中心incidenceを点検。Pym arXiv:1403.6444 §3.4 (9)を一次本文と画像で確認。 | 全intrinsic H3の開性・相対降下・全境界は条件付き。表示の一致からAOUのAS性を推論しない。 |
| HH次元8 | 第一論文 thm:HH8。局所模型 k[[s,w]] ⋊ μ3 の非恒等sectorの不変部分、対数接束のコホモロジー h=(0,7,0)、二次外積の計算を点検。 | 具体的な中心商がこのorder模型を満たすことは ass:order の認識入力。全H3認識の独立な再証明は未実施。 |
| 反標準二次包絡 | lem:anticanonical-quadratic-hull、prop:aou-infinite-order-exclusion。構造対象を保つexact同値から反標準orbit環を復元し、次数1・2から二次包絡を復元する証明を記載・点検。 | 飽和反標準環との同定が必要。AOU §9 の無限位数blow-up構成との比較に限る。 |
| AOU/AS曲面の範囲 | [AOU, arXiv:2404.00175v1](https://arxiv.org/abs/2404.00175v1), §9, (9.6)–(9.10), Lemma 9.2, Theorem 9.4、および [Okawa–Ueda, arXiv:2508.04986v1](https://arxiv.org/abs/2508.04986v1), Definition 1.1 の一次本文を確認。三乗根の斉次量子平面のpoint schemeは全P²、無限位数Sklyanin側は楕円曲線。 | 有限位数AS部分、別の構造対象・標識、任意の導来同値、八次元族全体のAS性は未決着。Theorem 9.4の導来同値をpointed exact同値へ読み替えない。 |
| CY/PBWとPainlevé表示 | [Etingof–Ginzburg, arXiv:0709.3593v4](https://arxiv.org/abs/0709.3593v4), Theorem 3.3.2、および [Chekhov–Mazzocco–Rubtsov, arXiv:1905.02772v2](https://arxiv.org/abs/1905.02772v2), Definition 1.1, (1.5), Theorem 1.5, Proposition 4.2 を一次本文で確認。第一論文の注意に関係式の明示的特殊化を記載。 | CMRのqが根でないという仮定は維持する。三乗根での関係式の特殊化と同文献の定理の適用を区別。全パラメータ同型類・新規性の比較は未完。 |
| 局所MF・dg特異点圏 | [Dyckerhoff, arXiv:0904.4713v5](https://arxiv.org/abs/0904.4713v5), Theorem 5.9, Corollary 6.5 のJacobian代数と高次積、および [Hua–Keller, arXiv:1810.00749v6](https://arxiv.org/abs/1810.00749v6), Theorem 5.9, pp.36–37 の通常の整数次数付きdg圏のHH⁰＝Tjurina環を確認。 | 二周期の相対Hochschild理論と通常の整数次数付きdg理論を同一視しない。一般の高次項を持つ実germの二周期MF分類は未完成。 |
| 境界のホモロジー作用 | [Goldman–Neumann, arXiv:math/0402039](https://arxiv.org/abs/math/0402039), Theorems 1–2 の原文と、第三論文で用いる座標正規化を確認。 | H3圏上の非可換自己同値を構成したことにはならない。 |
| PrymとPicard–Fuchs | 巡回被覆の連結性・完全分岐、Jacobian引戻しの核、normによる偏極比較を点検。表示されたPicard–Fuchsの完全微分恒等式を独立にSymPyで検算。 | bcは楕円因子上のtheta線束の次数であり、偏極isogenyの次数は(bc)²。全Prymの整数直積分解、実germの高次項を含む構成は未完成。 |

上記は限定した論点の点検である。二つの幾何S5被覆、全ての整数標識・periodの開条件、形式変形比較の外部入力を含め、三原稿全体の独立査読を意味しない。先行研究の書誌と参照箇所は papers/shared/bibliography.tex および各研究ノートにも記載する。

## 3. 実行した計算

computations/validation.json には、computations/verify_all.py が列挙する **36検証器の既存の全成功記録**を保持する。今回この36本は再実行していない。実行環境は Python 3.12.14、SymPy 1.14.0、NetworkX 3.6.1。終了時刻は2026-11-18 05:41:40 JSTである。

各検証器、共通補助コード、requirements.txt のSHA-256は computations/validation.json に記録されており、今回も現行ソースとの一致を確認した。この実行の後に実行時刻・hash・失敗記録の出力処理を改善したため、同JSONは実際に実行されたrunnerのhashを保持し、記録形式を整えたことを明示している。検証器本体と共通計算コードは実行時から不変である。未実行の新runnerを実行済みとは記載しない。

新たに computations/verify_r13_comparison.py を実行しPASSを得た。三次巡回語11方向、対称三次10方向、全十九単項式について57個の微分恒等式、八変数の全係数変換と三関係、Hesse勾配式の多項式結合、特殊点の単元性を厳密検算した。source hashを r13_comparison_certificate.json に記録する。有限標本による確認ではない。

計算の対象は多項式恒等式、有限行列、整数格子、特定の局所環や具体例、証明書の再現である。圏同値、全次数の平坦性、大域モジュライ、新規性などは、このPASSだけでは保証されない。計算が使う数学的入力と保証しない事項は validation.json にも列挙する。

再現方法：

~~~sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_all.py
python3 computations/verify_r13_comparison.py
~~~

## 4. ソースとPDF

元ソースではルートからの make papers は三本とも成功した一方、papers/内の `latexmk -lualatex fricke-geometry.tex` は共通プリアンブルが見つからず失敗した。これを入力パスの問題として再現し、三主原稿にdocumentclassと自己TeX root指定を置き、ルートとpapers/の両方からinputを解決するよう修正した。LuaLaTeX単発起動を優先するTeX programコメントを除き、latexmkレシピを明示した。出力先は設定ファイルの位置から計算し、一時環境の絶対パスをソースへ埋め込まない。

今回の検証は次の範囲である。VS CodeのGUI自体は実行しておらず、その設定とCLIによる同等の組版を区別する。

- 三原稿の入力・ラベル・参照・引用・文献選択、各主ファイルにdocumentclassと自己root指定があることを verify_sources.py で検査しPASS。
- ルートからの make papers、papers/からの三原稿それぞれのクリーンなlatexmk再組版、ルートからの latexmk -cd によるFricke原稿の組版は全て終了コード0。
- 最終ログの未解決参照・引用、重複ラベル、overfull/underfull box、PDF bookmark警告はいずれも0。環境由来の日本語フォント倍率・数式小サイズ置換等の警告とは区別する。
- 冒頭、新比較節の式と定理、他二論文の数式ページ、各文献末尾を画像で点検し、欠字・はみ出し・重なりがないことを確認。全ページの画像通読や数学の独立査読ではない。
- git diff --check、旧36検証器と補助ソースのhash一致、新比較証明書のhash一致を検査。PDF・ZIP・ログはGitへ保存しない。

~~~sh
make sources
make comparison
make papers
(cd papers && latexmk -lualatex fricke-geometry.tex)
(cd papers && latexmk -lualatex cubic-boundary-prym.tex)
make bundle
~~~

bundle生成器は必須ファイル、入力より古いPDF、既存36検証器・補助コードと新比較検算のhash、ZIPのCRCと全収録ファイルのSHA-256を検査する。生成・検証、GitHubへの反映、Libraryへの保存は別操作として扱う。組版実行結果は上記のとおり確認済みである。

## 5. 公表前の優先課題

1. 第二・第三論文の中心定理ごとに既知結果との同一性・差分を確定する。一般理論の適用、具体的な計算、新しい比較定理をIntroductionで区別する。
2. 第一論文の ass:recognition、ass:order にある飽和性・order・Serre作用・H3認識の入力を、固定した文献と証明へ一本ずつ接続する。必要なら主定理を入力付きの変形定理として確定する。
3. 二五次被覆の独立な幾何S5、D4周期標識、Prymの整数偏極を、計算証明書と独立に通読する。
4. 全H3の代数化・開性・降下、任意のAS標識との比較、mirrorや非可換自己同値の構成は、今回の公表用定理列が既に解決した問題として扱わない。
