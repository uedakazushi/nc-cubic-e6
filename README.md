# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v21。
**数学的に面白くすることを最優先とし、多様な分野との具体的な接続を探す。** 量子so3・中心三次切断・一次元表現を、非可換幾何、指標多様体、特異点、周期、実幾何の共通模型として研究する。八次元E6成分の分類は保持するが、完成を他分野との比較の前提にしない。

再開時は [研究方針](00_research_plan.md) を先に読む。主論文は日本語LuaLaTeXの [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の成果も同じ論文へ統合する。

## LGからCayley・D4・例外群へ

一次元表現の五重被覆はPhi=(vw−u,wu−v,uv−w)=grad H、H=uvw−(u²+v²+w²)/2。分岐源はCayley三次曲面で閉トーラスSL2指標多様体。四sheet衝突のD4ミニバーサル変形、triality、Jacobi留数対、pillowcase、elliptope内部の実sheet一意性が同じ模型に現れる。
LG等位面を三角境界付き三次曲面へコンパクト化し、指定D4退化の局所Milnor fiberの包含からPicard直交補へ整数格子同型を得る。H2の残る一次元は境界radical。外部trialityを判別群で検出し、混合Hodge構造の重み二の四方向と重み四の一方向を分ける。全域の標準分裂やHodge拡大の分裂ではない。
Boalch–Palubaの既知定理により、対称LG等位面はregularなG2指標多様体の三成分の一つ。unipotent退化の底(6,6)ではD4の(lambda,h)=(2,7/2)とA2の(-1/4,1/8)が現れ、四sheet衝突と従来のsimple foldが結び付く。

## 二種類のbraidと境界周期

[新しいbraid・周期の節](papers/sections/quantum_cubic_g2_braids.tex) では、三成分のラベル被覆を減次三次式z³−3Pz+QのA2 root coverと同定する。その底のbraidは成分をS3で交換する。一方、LG上の明示的Hurwitz生成元B1=(u,2uv−w−2lambda,v)、B2=(w,v,2vw−u−2lambda)は各成分を保ち、W・体積・Jacobian Poisson・留数形式を保存する。抽象群がともにB3でも同じ作用ではない。
一生成元はconic pencil上でtrace2uのSL2行列へ平行移動で移り、反復はChebyshev多項式で表せる。既知Klein七点軌道上の置換像はS7（5040）である。一つの表現像として現れるG2(2)'≅U3(3)（6048）やKlein群168とは別物。
正規化した留数2形式の原始境界cycle上の周期は(2pi i)²で、Hurwitzはこのcycleを固定する。内部四周期、全Gauss–Manin系、混合Hodge拡大の計算はまだ行っていない。

証明は [Cayley・LG](papers/sections/quantum_cubic_cayley_lg.tex)、[Milnor・Picard・G2](papers/sections/quantum_cubic_lg_picard.tex)、[二braid・周期](papers/sections/quantum_cubic_g2_braids.tex)。具体式・一次文献・課題は [接続ノート](research/cayley_lg_connections.md)。古典的なCayley、Fricke位相、G2実現、Hurwitz公式、Klein軌道は既知として引用し、指定模型での適用・検算と区別する。新規性の網羅確認、量子G2同型、mirror/Fukaya同値は未完成。

## 保持する既存成果

七次元PBW正常形、横断積分、仮定付き八次元Hochschild変形、全Artin表示族、smooth DM表示stackを保持する。固定包絡の五結節SNC因子・A4商二成分、七次元族の既約六次元結節因子も保持。
AW中央特殊化、Fricke係数写像、量子的Vieta、Goldman型括弧の9倍、D4⊂E6を明示した。非Casimir切断の純粋q持上げと固定pointed心へのVietaには障害があるが、一般変形・心の変更を否定しない。
相対Poisson臨界環は次数15、一次元表現は次数5で有限平坦。Delta15=N5²M5、二五次の同時幾何Galois群S5×S5。全H3 admissibility、intrinsic降下、全境界、全Casimir値のAzumaya性は未完成。
**被覆の分岐、Casimir値の衝突、LG臨界値の衝突は別現象。** 元の量子中心と一次元表現が同じFricke形を与えても、異なる係数底変更を同一視しない。
基礎は [研究ノート](research/research_notes.md)、DAHA/Painlevé/mirrorは [文献比較](research/fricke_daha_comparison.md)、二五次被覆は [Poissonノート](research/poisson_order_notes.md)。

## 再現と今回の検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_g2_braids_periods.py
python3 computations/verify_all.py  # 全26検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

新検証器をQ恒等式・有限置換群で実行しPASS。小証明書は `computations/g2_braids_periods_certificate.json`。全次数Chebyshev漸化式・configuration space・原始トーラス・周期積分は本文の通常の証明であり、コードだけの結論ではない。
新節単体のLuaLaTeX4頁を組版・全頁画像点検し、内部参照解決とoverfullなしを確認。主論文全体の今回の組版、旧25検証器の全再実行、旧定理の独立再監査、新規性の網羅調査は未実施。

GitHub mainが正本。**push済み内容をLibraryへ保存しない。** PDF・ZIP・ログ・中間生成物はGitで追跡しない。他の研究は [分類](https://github.com/uedakazushi/nc-cubic-moduli)、[ambient比較](https://github.com/uedakazushi/nc-cubic-ambient-moduli)、[非AS短報](https://github.com/uedakazushi/nc-cubic-non-as) を参照。
移行元は [固定source commit](https://github.com/uedakazushi/nc-cubic-moduli/tree/c5fd8a8301f6b1c283a6f0510cde80ae6a006e80) から必要内容を抽出済みで、旧bundleは再開の前提ではない。
