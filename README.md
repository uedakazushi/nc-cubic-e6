# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v26。
**数学的に面白くすることを最優先とし、多様な分野との具体的接続を探す。** 量子so3・中心三次切断・一次元表現を、非可換幾何、指標多様体、特異点、周期、算術、力学、圏的局所化の共通模型として研究する。八次元E6成分の分類は保持するが、完成を他分野との比較の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。日本語LuaLaTeX主論文は [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の成果も同じ主論文へ統合する。

## 同じPell写像の三つの成長率

全ホモロジーとperiodを固定するLG曲面の自己同型gについて、古典的力学・境界付値はLambda=3+2sqrt2の指数増大を持つ。最小次数は1,7,41,239,...のPell列、二つの固有方向は二次無理数、一付値のcorner抽出回数は4n。指定コンパクト化の有限境界blow-upで正則自己同型へ延長することはできない。

一方、**通常のアフィンperfect圏のDHKK entropyは零**である。g*は生成元O_Uを固定するからであり、End(O_U)への作用まで自明という意味ではない。射の極次数filtrationを残すと反復歪み率はlog Lambdaとなり、周期巡回homologyでは恒等作用になることと対照的である。

一般conic C0={v=kappa}の反復逆像は全て同じ滑らかなaffine有理曲線だが、射影閉包の算術種数は境界だけで増大する。M^n=[[a,-b],[-b,c]]、d=b+cと書けば、閉包の次数は2d、算術種数は1+2bc−d。最初の(degree,genus)は(2,0),(14,14),(82,656),(478,23422)。proper圏の任意の固定生成元に対する閉包構造層の複雑度率は2log Lambdaだが、開曲面へ制限すると二項の自由解消を持ち、複雑度は2以下となる。

**2log Lambdaは対象列の増大率であり、射影圏の自己関手entropyではない。** 閉包操作のexact性や、閉包列を反復像に持つ自己同値は構成していない。filtered・equivariantなmirror比較には射のfiltrationを相互に線型比較する追加仮定が必要で、静的growthの比較だけでは足りない。

証明は [局所化とentropyの節](papers/sections/quantum_cubic_localization_entropy.tex)、先行する [境界Pell節](papers/sections/quantum_cubic_boundary_dynamics.tex)、現在の式・文献・未解決課題は [境界・局所化ノート](research/boundary_pell_dynamics.md)。DHKK、Côté–Kartal、HKRの一般理論は既知として引用し、本稿の具体的適用と区別する。

## 保持する接続と未解決部分

trialityの不変・余不変格子の指数3がperiod torusのmu3 isogenyとなり、そのWeyl商はBoalch–PalubaのG2三成分写像と一致する。共通の明示開集合で三成分の有理MHSを比較し、Klein例の整数拡大位数7,21,21を得る。曲面同型・導来同値・全域標準VMHS同型ではない。証明は [triality節](papers/sections/quantum_cubic_triality_isogeny.tex)、式と適用範囲は [周期ノート](research/conic_period_coordinates.md)。

LG勾配写像のCayley分岐源、トーラス指標多様体、D4ミニバーサル変形、Milnor–Picard整数比較、外部triality、G2のD4/A2共通退化、二種類のbraid、Klein七点上のS7、pillowcase/elliptopeを保持する。一般conic chartの四periodと円分的Hodge分裂、対数matching積分、arcsine周期も現行原稿にある。被覆のbranch、Casimir値衝突、LG臨界値衝突は別現象。

七次元PBW正常形、横断積分、仮定付き八次元Hochschild変形、全Artin表示族、smooth DM表示stack、結節中心因子、AW/Fricke比較、Poisson括弧9倍、Delta15=N5²M5とS5×S5を保持する。主論文の旧証明本文・入力節・文献表は削除していない。
全intrinsic H3の相対代数化・降下・大域境界、一般相対AS4、全Casimir値でのAzumaya性、全rank五代数的Gauss–Manin接続、元の非可換H3圏の自己同値、filtered equivariant mirrorは未構成。

基礎は [研究ノート](research/research_notes.md)、DAHA/skein/Painlevéは [文献比較](research/fricke_daha_comparison.md)、二五次被覆は [Poissonノート](research/poisson_order_notes.md)、LG/G2の基礎は [接続ノート](research/cayley_lg_connections.md) を参照する。

## 再現と確認済み範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_localization_entropy.py
python3 computations/verify_all.py  # 全31検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回は新検証器を全係数多項式・Q・整数行列で実行しPASS。小証明書は `computations/localization_entropy_certificate.json`。全nの主張、圏的複雑度、正規化種数、HKRは通常証明・先行理論への依存であり、有限検算のみの結論ではない。
新節単体はLuaLaTeX5頁で全頁を画像点検。内部参照は解決、前節Pell定理は抜粋用の参照名で表示、overfullなし。主論文全体の今回の組版、旧30検証器の全再実行、独立査読、網羅的新規性調査は未実施。主論文の変更差分で旧証明の保持を確認した。

GitHub mainが正本。**push済み内容はLibraryへ保存しない。** PDF・ZIP・ログ・中間生成物はGitで追跡しない。全H3分類は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli) が別の正本であり、旧bundleの取得は再開の前提ではない。
