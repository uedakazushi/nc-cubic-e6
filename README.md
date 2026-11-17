# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v20。
**数学的に面白くすることが最優先。多様な分野との具体的な接続を優先して探す。** 量子so3・中心三次切断・一次元表現を、非可換幾何、指標多様体、特異点、周期、実幾何の共通の例として研究する。八次元E6成分の分類は保持するが、その完成を他分野との比較の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。主論文は日本語LuaLaTeXの [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の成果もこの同じ論文へ統合する。

## 一つのLG模型から現れる接続

一次元表現の五重被覆は Phi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。そのramification divisorはCayley三次曲面で、閉トーラスのSL2粗指標多様体。四sheet衝突のD4ミニバーサル変形、trialityの位数3作用、Jacobi留数対、実pillowcase、elliptope内部の一意な実sheetが同じ模型に現れる。

LG等位面 W=H−Au−Bv−Cw=h を三角境界付き三次曲面へコンパクト化すると、局所D4 Milnor fiberの包含からPicardの境界直交補への**整数格子同型**を得る。H2の残る一次元は境界に由来するradical。巡回置換は判別群の三非零元を回し、局所とPicardで同じ外部trialityを検出する。比較は指定した退化に対するもので、全パラメータ上の選択非依存な分裂ではない。

さらにBoalch–Palubaの既知定理を適用すると、対称LG等位面はG2指標多様体の三つの連結成分の一つとなる。第四局所monodromyをregular unipotent共役類の閉包へ動かす退化では、(lambda,h)=(2,7/2)のD4 fiberと(-1/4,1/8)のA2 fiberが現れる。後者は従来のS5証明に使ったsimple foldであり、二つの異なる衝突が同じ例外群の退化を通じて結ばれる。

証明は [Cayley・LGの節](papers/sections/quantum_cubic_cayley_lg.tex) と [Milnor・Picard・G2の節](papers/sections/quantum_cubic_lg_picard.tex)。現在の式・一次文献・未解決課題は [接続ノート](research/cayley_lg_connections.md)。Goldman–Neumannの位相、Deligneの重み理論、Boalch–PalubaのG2実現は既知として引用し、本稿での適用と区別する。G2量子代数の同型、mirror/Fukaya同値、混合Hodge拡大の分裂は未構成。

## 保持する既存成果と適用限界

七次元PBW正常形、三捩れからの横断積分、仮定を明示した八次元Hochschild変形、全Artin表示族、smooth DM表示stackを保持する。結節中心は固定包絡で五SNC因子・A4商で二成分、七次元族では既約六次元因子。既存証明節は削除していない。
AW中央特殊化、Fricke係数写像、量子的Vieta、Goldman型Poisson括弧の正確な9倍、三角境界とD4⊂E6を明示した。純粋q変形の非Casimir切断持上げと固定pointed H3心へのVieta作用には障害があるが、一般変形や心の変更は否定しない。
相対Poisson臨界環は次数15、一次元表現環は次数5で有限平坦。Delta15=N5²M5、二五次の同時幾何Galois群はS5×S5。全H3 admissibility、intrinsic降下、全境界、一般相対AS4、全Casimir値のAzumaya性は未完成。
**被覆の分岐、Casimir値の衝突、LG臨界値の衝突は別現象。** 同じFricke式への座標変換も、元の量子中心と一次元表現の係数を無条件に同一視するものではない。

基礎は [研究ノート](research/research_notes.md)、DAHA/skein/Painlevé/mirrorは [文献比較](research/fricke_daha_comparison.md)、二五次被覆は [Poissonノート](research/poisson_order_notes.md) を参照する。

## 再現と検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_lg_picard_g2.py
python3 computations/verify_all.py  # 全25検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回は新しいLG/Picard/G2検証器をQ・整数格子上で実行しPASS。小証明書は `computations/lg_picard_g2_certificate.json`。位相・Hodge・G2同定は本文の通常証明と一次文献の入力であり、有限計算だけの結論ではない。
新節単体のLuaLaTeX組版4頁と画像点検を実施し、内部参照とoverfullを確認した。主論文全体の今回の組版、旧24検証器の全再実行、独立査読、新規性の網羅調査は未実施。

GitHub mainが正本。**push済みの内容はLibraryに保存しない。** PDF・ZIP・ログ・中間生成物はGitで追跡しない。他の研究は [分類](https://github.com/uedakazushi/nc-cubic-moduli)、[ambient比較](https://github.com/uedakazushi/nc-cubic-ambient-moduli)、[非AS短報](https://github.com/uedakazushi/nc-cubic-non-as) を参照する。
移行元の内容は [固定source commit](https://github.com/uedakazushi/nc-cubic-moduli/tree/c5fd8a8301f6b1c283a6f0510cde80ae6a006e80) を基準に抽出済みで、旧bundleの取得は再開の前提ではない。
