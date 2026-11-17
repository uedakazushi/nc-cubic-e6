# 量子三次曲面、Fricke幾何、境界Prym

2026-11-18 / publication-v32

三乗根量子三次曲面から得られる変形・表現・周期・境界特異点を、三つの公表用原稿に整理した研究リポジトリです。**再開時は [研究方針](00_research_plan.md) を最初に読んでください。**

## 論文

| 原稿 | 中心となる内容 |
|---|---|
| [nc-cubic-e6.tex](papers/nc-cubic-e6.tex) | **三乗根量子三次曲面の正常形と形式変形**。七次元PBW正常形、指定局所order模型のHH²=8・HH³=0、八変数形式表示、反標準二次包絡とAOU無限位数部分との比較。 |
| [fricke-geometry.tex](papers/fricke-geometry.tex) | **量子三次曲面のFricke幾何と周期**。AW/Fricke、相対Poisson臨界被覆、N5²M5とS5×S5、LG/D4、四周期とtriality。 |
| [cubic-boundary-prym.tex](papers/cubic-boundary-prym.tex) | **三次曲面のPell力学と境界特異点**。境界二枝、局所化の成長、模型MFと実germ、Milnor被覆のPrym・整数偏極。 |

既存の結果と証明は現在の三原稿に保持しています。長い総合原稿の旧版を重複して収録していません。三原稿はそれぞれ独立にLuaLaTeXで組版でき、共通の設定・文献データだけを共有します。

## 確定した範囲と未解決部分

- **第一論文**の八次元Hochschild変形は、滑らかな三次中心・反標準楕円境界・指定局所order模型の下の定理です。八変数形式表示や代数的表示stackを、全intrinsic H3モジュライの分類と同一視していません。相対代数化・開性・降下・全境界は未完成です。
- **AOUとの比較**では、飽和反標準環から二次包絡を復元し、AOU §9の無限位数blow-up表示とのpointed exact同値を除外します。有限位数を含むAS曲面一般、任意の導来同値、八次元横断族の非AS性を結論していません。
- **第二論文**では中心、一次元表現、LG等位面を明示的な式で結びます。既知のFricke/G2理論と、その具体的な係数・格子・周期比較を区別しています。
- **第三論文**では重み付き模型と実際の境界germを区別します。実例のμ=27、τ=24は主部のτ=27と異なります。Prymの楕円因子から、実germへの移行やMF部分圏・HMSを推論していません。

主張ごとの仮定と証明所在は研究方針、今回の計算・組版・数学的点検の範囲は [公表準備と検証状態](research/publication_status.md) にあります。計算のPASSは全論文の独立査読や新規性の確認ではありません。

## 研究ノート

| 話題 | ノート |
|---|---|
| 正常形・形式変形・AS比較・入力仮定 | [research_notes.md](research/research_notes.md) |
| AW・DAHA・Fricke | [fricke_daha_comparison.md](research/fricke_daha_comparison.md) |
| Poissonと二つの五次被覆 | [poisson_order_notes.md](research/poisson_order_notes.md) |
| LG・Milnor/Picard・G2 | [cayley_lg_connections.md](research/cayley_lg_connections.md) |
| 四周期・triality | [conic_period_coordinates.md](research/conic_period_coordinates.md) |
| Pell力学・局所化・二枝 | [boundary_pell_dynamics.md](research/boundary_pell_dynamics.md) |
| 解析modulus・MF・Milnor/Prym | [boundary_analytic_moduli.md](research/boundary_analytic_moduli.md) |

## 組版と再現

リポジトリルートから実行します。必要なものはPython 3、[固定したPython依存](computations/requirements.txt)、LuaLaTeX・latexmk・日本語TeX環境（ltjsarticle、luatexja-preset、HaranoAji）です。

~~~sh
python3 -m pip install -r computations/requirements.txt
make sources       # 入力・参照・引用の静的確認
make verify        # 36個の厳密計算検証器
make papers        # 三原稿のLuaLaTeX全文組版
make bundle        # 現行ソース・PDF・再現資産のZIP
~~~

個別に主論文だけを組版する場合：

~~~sh
latexmk -r .latexmkrc -lualatex papers/nc-cubic-e6.tex
~~~

PDFとSyncTeXは build/ に出力します。VS Codeではリポジトリルートをワークスペースとして開き、三つの主ファイルのいずれかをビルドします。papers/sections/ は入力用の節であり、単独のdocumentclassは持ちません。

computations/validation.json は直近の全36検証器の結果・実行時刻・使用ソースのhashを記録します。入力断片に付随する computations/auxiliary/ の検証器はこの36個に含まれません。scripts/build_bundle.py は旧版、PDF以外の組版生成物、ログ、キャッシュ、.git を含めず、必要な現在の一式を作ります。

GitHubには原稿・ノート・計算資産を保存し、PDF・ZIPを追跡しません。全H3分類の関連研究は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli)、ambient研究は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) を参照してください。
