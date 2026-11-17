# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v25。
**数学的に面白くすることを最優先とし、多様な話題との具体的接続を探す。** 量子so3・中心三次切断・一次元表現を、非可換幾何、指標多様体、特異点、周期、算術、力学の共通模型として研究する。八次元E6成分の分類は保持するが、その完成を他分野との比較の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。日本語LuaLaTeX主論文は [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の成果も同じ論文へ統合する。

## 周期には見えない作用を、境界で見る

滑らかなLG等位面で、四つのVieta involutionの合成 `g=iota_v iota_w iota_u iota_w` はH2と全periodへ恒等に作用する一方、正entropyを持つ。これを三角境界の単項式付値で観測すると、`Theta(r,t)=(|r|,|t|,|r+t|)` により行列 `[[1,-2],[-2,5]]` の作用となる。

反復の**最小**多項式次数は `1,7,41,239,1393,...`、漸化式 `d(n+2)=6d(n+1)-d(n)`。係数に依存せず、Pell単数 `1+sqrt(2)` の奇数冪と一致する。射影hyperplaneの交点次数はn≥1で2d_nであり、二つの次数を区別する。

境界には二つの二次無理固有付値があり、有理な方向に周期点がない。このため、指定した三次コンパクト化を支配する有限境界blow-upでgを正則自己同型へ延長できない。一方、`g_*^n ord(D_w)` という**一つの付値を抽出する**corner blow-upの最小回数は正確に4n。指数的な極次数と線型の抽出深さが共存する。

証明は [境界付値・Pell力学の節](papers/sections/quantum_cubic_boundary_dynamics.tex)、再開用の式と限界は [境界力学ノート](research/boundary_pell_dynamics.md)。一般tropical線型化はJang、境界力学・entropyはCantat–Lorayの先行研究として扱い、本稿ではperiodの核にある明示語の正確な計算を与える。全ての別コンパクト化の不存在、algebraic stabilityの不存在、圏的entropyを主張するものではない。

## 周期からG2の三成分を説明する

対称LG等位面のHurwitzホモロジー像は外側三根のS3、四つのD4周期は適切な標識で `(eta,xi,eta,eta)`。trialityの不変格子と余不変格子の指数3から、period torusのisogeny `(xi,eta)->(xi,eta^3)` が得られ、そのWeyl商はBoalch–PalubaのG2三成分写像に一致する。

従来の `B^2 != C^2` chartの外にある対称族について、conic成分と交わらないline sectionから別の標識を構成し、実際のLooijenga periodとしてこの二変数を実現する。
regularな底の三持上げが共通の明示開集合に入る範囲で、有理混合Hodge構造は標識graded pieceの下で同型となる。整数拡大の差は残り、Klein曲面と二つのコンパニオンで位数は **7,21,21**。全て有理分裂でも整数MHSは異なる。
証明は [triality・周期isogenyの節](papers/sections/quantum_cubic_triality_isogeny.tex)、具体式と適用範囲は [周期ノート](research/conic_period_coordinates.md)。群自体のG2 isogeny、曲面同型、導来/Fukaya同値を構成したとはしない。

## 保持する構造と研究上の区別

LG勾配写像の分岐源Cayley、閉トーラスSL2指標多様体、D4ミニバーサル変形、Milnor–Picard整数比較、外部triality、G2のD4/A2共通退化、二種類のbraid、Klein七点上のS7を保持する。pillowcase、elliptope内の一意実sheet、nearly Kählerの共通凸体も比較する。
一般conic chartで全四周期は `(z1/z2,z2/z3,z3/z4,z3*z4)`、有理Hodge分裂は円分性で判定。対数matching積分、arcsine周期、有理数係数の分裂・非分裂例、非分裂rank二局所系を保持。被覆の分岐、Casimir値衝突、LG臨界値衝突は別現象。
七次元PBW正常形、横断積分、仮定付き八次元HH変形、全Artin表示族、smooth DM表示stack、結節中心、AW/Fricke、root Poisson9倍、Delta15=N5²M5とS5×S5も保持する。旧証明本文・入力節を削除していない。
全intrinsic H3の相対代数化・降下・大域境界、一般相対AS4、全Casimir値でのAzumaya性、全rank五代数的Gauss–Manin接続、圏的entropyは未完成。

基礎は [研究ノート](research/research_notes.md)、DAHA/skein/Painlevé/mirrorは [文献比較](research/fricke_daha_comparison.md)、二五次被覆は [Poissonノート](research/poisson_order_notes.md)、LG/G2/braidの基礎は [接続ノート](research/cayley_lg_connections.md)。

## 再現と検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_boundary_pell_dynamics.py
python3 computations/verify_all.py  # 全30検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回実行した新検証器はQ多項式、有理chamber、整数行列上でPASS。小証明書は `computations/boundary_pell_dynamics_certificate.json`。全12 chamberの36線型恒等式、n=24までのPell・連分数を確認。全nの次数・最低次数性・付値・非正則化は本文の通常証明であり、有限回の外挿ではない。
新節単体はLuaLaTeX4頁で組版・全頁画像点検・内部参照とoverfullを確認した。主論文全体の今回の組版、旧29検証器全再実行、独立査読、新規性の網羅調査は未実施。主論文差分で旧証明の保持と新節inputを確認する。

GitHub mainが正本。**pushした内容はLibraryに保存しない。** PDF・ZIP・ログ・中間生成物をGitで追跡しない。全分類は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli) が別の正本。旧bundleの取得は再開の前提ではない。
