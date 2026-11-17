# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v22。
**数学的に面白くすることを最優先とし、多様な分野との具体的な接続を探す。** 量子so3・中心三次切断・一次元表現を、非可換幾何、指標多様体、特異点、周期、実幾何の共通模型として研究する。八次元E6成分の分類は保持するが、完成を他分野との比較の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。日本語LuaLaTeX主論文は [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の公表価値ある成果も同じ主論文へ統合する。

## 対数周期からLooijenga対と混合Hodge構造へ

LG等位面 W=uvw−(u²+v²+w²)/2−Au−Bv−Cw=h のconic pencilを二重被覆上で書くと、留数形式は dlog z∧dlog a に分かれる。単純零点を結ぶmatching球面の周期は2pi i log(z_+/z_-)となる。A=B=C=0の原点へ消える実球面では

\[
\Pi_0(h)=4\pi\arcsin\sqrt{-2h},\qquad -1/2<h<0.
\]

境界周期Pi_infty=(2pi i)²とともに二階Picard–Fuchs方程式を満たし、rank2解局所系のmonodromyは無限二面体群。全rank5 Gauss–Manin系を決定したという主張ではない。
指数化Q=exp(Pi0/(2pi i))は **Q+Q^-1=2+8h** を満たす代数的なトーラス座標となる。Friedmanのperiod比較により、これはLooijenga対の境界線束制限と結ばれる。h=−1/10ではQ=(3−4i)/5が非捩れであり、同fiberの混合Hodge構造が有理係数でも非分裂であることを証明した。
証明は [対数周期の節](papers/sections/quantum_cubic_log_periods.tex)、式と適用限界・文献は [接続ノート](research/cayley_lg_connections.md)。全四内部周期の同時整数基底、全Gauss–Manin接続、mirrorや非Archimedeanモデルは未構成。

## 共通模型に現れる幾何学

一次元表現の五重被覆はPhi=(vw−u,wu−v,uv−w)=grad H。ramification divisorはCayley曲面で閉トーラスSL2粗指標多様体となる。四sheet衝突はD4ミニバーサル変形、実型はpillowcaseとelliptopeへつながり、elliptope内部では実sheetが高々一つ。
LG等位面の三角境界付きコンパクト化に対し、指定D4退化の局所Milnor fiberの包含がPicard直交補へ整数格子同型を与える。境界radical、外部triality、混合Hodgeの重み2の四方向と重み4の一方向を分離する。全域の選択非依存な標準分裂ではない。
Boalch–Palubaの既知G2実現を用いると、対称LG等位面は三連結成分の一つ。unipotent退化のD4成分とA2成分が、従来の四sheet衝突とsimple foldをまとめる。底の成分ラベルを交換するB3と、各成分を保つHurwitz B3は別の作用。Chebyshev反復、Klein七点上のS7と位数6048の表現像の違い、境界周期を明示した。

既知のCayley、ADE、Looijenga period、G2実現と、本稿の具体的な適用・検算を区別する。G2型量子代数、Fukaya圏、nearly Kähler幾何との圏同値は未構成。

## 保持する非可換幾何と未完成部分

七次元PBW正常形、三捩れからの横断積分、仮定付き八次元Hochschild変形、全Artin表示族、smooth DM表示stack、結節中心因子を保持する。既存の数学的証明節は削除していない。
AW中央特殊化、Fricke係数写像、量子的Vieta、Goldman型Poissonの正確な9倍、D4⊂E6を明示。非Casimir切断の純粋q持上げと固定pointed H3心へのVieta作用には障害があるが、一般変形や心の変更を否定しない。
相対Poisson臨界環は次数15、一次元表現環は次数5で有限平坦。Delta15=N5²M5、同時幾何Galois群S5×S5。全H3 admissibility、intrinsic降下、全境界、一般相対AS4、全Casimir値のAzumaya性は未完成。
**被覆の分岐、Casimir値の衝突、LG臨界値の衝突は別現象。** 今回の係数monodromyのrank2解局所系非分裂と、一fiberの混合Hodge非分裂も別の主張である。

基礎は [研究ノート](research/research_notes.md)、DAHA/skein/Painlevéは [文献比較](research/fricke_daha_comparison.md)、二五次被覆は [Poissonノート](research/poisson_order_notes.md)、LG・格子・作用・periodは [接続ノート](research/cayley_lg_connections.md) を参照する。

## 再現と検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_logarithmic_periods.py
python3 computations/verify_all.py  # 全27検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回は新しい対数周期検証器を厳密実行しPASS。小証明書は `computations/logarithmic_periods_certificate.json`。球面の構成・積分・解析接続・Friedman比較・有理MHS非分裂は本文の通常証明と一次資料への依存であり、有限計算だけの結論ではない。
新節単体のLuaLaTeX組版4頁を全頁画像点検し、内部参照とoverfullなしを確認。主論文全体の今回の組版、旧26検証器の全再実行、独立査読、新規性の網羅調査は未実施。

GitHub mainが正本。**push済み内容はLibraryへ保存しない。** PDF・ZIP・ログ・中間生成物はGitで追跡しない。他の研究は [分類](https://github.com/uedakazushi/nc-cubic-moduli)、[ambient比較](https://github.com/uedakazushi/nc-cubic-ambient)、[標識忘却](https://github.com/uedakazushi/nc-cubic-unmark)、[非AS短報](https://github.com/uedakazushi/nc-cubic-non-as) を参照する。移行元は [固定source commit](https://github.com/uedakazushi/nc-cubic-moduli/tree/c5fd8a8301f6b1c283a6f0510cde80ae6a006e80) を基準に抽出済みで、旧bundleを再開の前提にしない。
