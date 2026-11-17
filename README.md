# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v24。
**数学的に面白くすることを最優先とし、多様な話題との具体的接続を探す。** 量子so3・中心三次切断・一次元表現を、非可換幾何、指標多様体、特異点、周期、算術、力学の共通模型として研究する。八次元E6成分の分類は保持するが、その完成を他分野との比較の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。日本語LuaLaTeX主論文は [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の成果も同じ主論文へ統合する。

## 周期からG2の三成分を説明する

対称LG等位面のHurwitzホモロジー像は外側三根のS3となり、四つのD4周期は適切な標識で `(eta,xi,eta,eta)` になる。trialityの不変格子と余不変格子の自然写像は指数3。その双対period torusの写像 `(xi,eta)->(xi,eta^3)` はkernel mu3を持ち、Weyl商を取るとBoalch–Palubaの既知のG2三成分写像に正確に一致する。

この一致を形式的な変数操作だけにしないため、対称族のconic成分と交わらないline sectionを明示した。従来の `B^2 != C^2` chartの外にある対称族について別に標識を構成し、上の二変数を実際のLooijenga periodとして実現する。

regularなG2底の三持上げが共通の明示開集合に入る範囲では、三成分のperiodは外側方向で3乗根だけ異なる。したがって有理混合Hodge構造は標識したgraded pieceの下で同型となるが、整数構造の違いは残り得る。Klein三次曲面 `(b,c)=(-1,0)` と二つのコンパニオンでは、整数Hodge拡大類の位数は **7,21,21**。有理化すると全て分裂して同型でも、Kleinとコンパニオンの整数MHSは非同型である。

さらに既知のGoldman–NeumannとCantat–Lorayの定理を適用し、全ホモロジー・periodを固定しながら力学的次数 `3+2sqrt(2)`、正entropyを持つ自己同型を明示する。周期が捉える算術的差と、周期に見えない無限力学を区別する。

証明は [triality・周期isogenyの節](papers/sections/quantum_cubic_triality_isogeny.tex)、再開用の式・範囲・一次文献は [周期ノート](research/conic_period_coordinates.md)。群自体のG2 isogeny、曲面同型、導来/Fukaya同値を構成したとはしない。個別結果の網羅的新規性確認も未了。

## 保持する構造と研究上の区別

LG勾配写像Phi=(vw−u,wu−v,uv−w)のramification divisorはCayley三次曲面で閉トーラスSL2指標多様体。D4ミニバーサル変形、Milnor–Picard整数比較、外部triality、G2のD4/A2共通退化、二種類のbraid、Klein七点上のS7を主論文に保持する。pillowcaseとelliptope、内部実sheetの一意性、nearly Kählerの共通凸体も比較する。
一般conic chartでは整数D4基底の全四周期を `(z1/z2,z2/z3,z3/z4,z3*z4)` と表示し、有理Hodge分裂を円分性で判定する。有理数係数の分裂・非分裂例、対数matching積分、arcsine周期、非分裂rank二局所系を保存する。被覆の分岐、Casimir値の衝突、LG臨界値の衝突は別現象。

七次元PBW正常形、三捩れからの横断積分、仮定付き八次元Hochschild変形、全Artin表示族、smooth DM表示stack、結節中心因子、AW/Fricke比較、root Poisson括弧9倍、Delta15=N5²M5とS5×S5を保持する。旧証明本文と入力節を削除していない。
全intrinsic H3の相対代数化・降下・大域境界、一般相対AS4認識、全Casimir値でのAzumaya性、全rank五代数的Gauss–Manin接続、圏的entropyは未完成。

基礎は [研究ノート](research/research_notes.md)、DAHA/skein/Painlevé/mirrorは [文献比較](research/fricke_daha_comparison.md)、二五次被覆は [Poissonノート](research/poisson_order_notes.md)、LG/G2/braidの基礎は [接続ノート](research/cayley_lg_connections.md) を参照する。

## 再現と検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_triality_period_isogeny.py
python3 computations/verify_all.py  # 全29検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回は新検証器をQ-Laurent恒等式・整数格子・Q(zeta21)上で実行しPASS。小証明書は `computations/triality_period_isogeny_certificate.json`。ホモロジー作用、縮約、線束period比較、Hodge拡大、entropyは本文の通常証明と先行定理への依存であり、計算のみの結論ではない。
新節単体はLuaLaTeXで5頁に組版し、画像・内部参照・overfullなしを確認。主論文全体の今回の組版、旧28検証器の全再実行、独立査読、新規性の網羅調査は未実施。更新差分で旧主論文の保持と新節inputを確認する。

GitHub mainが正本。**pushした内容はLibraryに保存しない。** PDF・ZIP・ログ・中間生成物はGitで追跡しない。全分類は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli) を別の正本とする。旧bundleの取得は再開の前提ではない。
