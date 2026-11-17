# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v23。
**数学的に面白くすることを最優先とし、多様な分野との具体的接続を探す。** 量子so3・中心三次切断・一次元表現を、非可換幾何、指標多様体、特異点、周期、実幾何の共通模型として研究する。八次元E6成分の分類は保持するが、その完成を他分野との比較の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。主論文は日本語LuaLaTeXの [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の成果も同じ主論文へ統合する。

## 四つの整数D4周期を同時に記述する

LG等位面W=uvw−(u²+v²+w²)/2−Au−Bv−Cw=hのconic pencilを使う。適切なsmooth開集合と有限標識被覆上で、退化conicの選択成分E1..E4から境界に直交する整数D4基底

alpha=(E1−E2, E2−E3, E3−E4, E3+E4−F)

を構成した。選択成分が境界に会う座標をz_i、conic退化値をu_iとするとz_i+z_i^-1=2u_iであり、四つの指数化周期は

**P(alpha)=(z1/z2, z2/z3, z3/z4, z3*z4)**

となる。線束制限のgluingとFriedmanのperiod比較を通じ、整数サイクルの積分と同定する。局所対数を選べば境界周期(2pi i)²と合わせてH2の全五方向の周期を記述できる。標準的な全域cycle基底や代数的Gauss–Manin接続行列を選択なしに与えるものではない。

このchartでは **有理混合Hodge分裂 ⇔ 全四periodがroots of unity ⇔ 全z_iがroots of unity**。有理数係数の滑らかな分裂例(A,B,C,h)=(1/4,1/2,1/4,1/8)は9乗根を与え、非分裂例(-65/16,75/16,-65/16,3575/288)はz_iが2,3,4,6の逆数選択となる。整数Hodge拡大の自明性、元の量子q³=1、有限Hurwitz軌道とは別の条件である。

証明は [四周期と円分分裂の節](papers/sections/quantum_cubic_four_periods.tex)、再開用の式・仮定・一次文献は [conic周期ノート](research/conic_period_coordinates.md)。Naruki–LooijengaのD4 period torusとFriedman–Carlsonの一般理論は既知として引用する。

## 共通模型から広がる接続

一次元表現はPhi=(vw−u,wu−v,uv−w)=grad Hという五重被覆。そのramification divisorはCayley曲面＝閉トーラスSL2指標多様体。四sheet衝突のD4ミニバーサル変形、triality、Jacobi留数対、pillowcase、elliptope内の実sheet一意性を同じ模型で扱う。
LG近傍等位面の局所Milnor fiberの包含はPicardの境界直交補へ整数D4同型を与える。残るH2の一方向は境界radical。対称LGは既知定理によりG2指標多様体の一成分となり、D4衝突とA2 simple foldが同じG2退化の二成分として現れる。
底の三成分交換braidと各成分内のHurwitzを区別する。Chebyshev反復、Klein七点軌道の置換群S7、境界周期を明示。conic matching周期は対数に帰着し、係数零のMorse球面は4pi arcsin sqrt(-2h)。h=-1/10は別の有理MHS非分裂例である。
これらの証明は主論文のCayley・LG、Milnor・Picard・G2、braid、対数周期各節。古典的な一般理論・先行研究の適用と、本稿での正規化・計算を区別する。

## 保持する成果と未解決点

七次元PBW正常形、横断積分、仮定付き八次元Hochschild変形、全Artin表示族、smooth DM表示stack、結節中心因子を保持する。AW中央特殊化、Fricke係数写像、量子的Vieta、指定Goldman型括弧の9倍を明示した。純粋q変形の非Casimir切断と固定pointed H3心へのVietaには障害があるが、一般変形・心の変更は否定しない。
相対Poisson臨界環は次数15、一次元表現環は次数5で有限平坦。Delta15=N5²M5、二五次の同時幾何Galois群S5×S5。全H3 admissibility・intrinsic降下・全境界・一般相対AS4・全Casimir値でのAzumaya性は未完成。
**被覆のbranch、Casimir値衝突、LG臨界値衝突は異なる。** 同じFricke式への変換も異なる係数写像を同一視するものではない。mirror/Fukaya同値、G2型量子代数との同型、非Archimedeanモデルは未構成。

基礎は [研究ノート](research/research_notes.md)、DAHA/skein/Painlevé/mirrorは [文献比較](research/fricke_daha_comparison.md)、二五次被覆は [Poissonノート](research/poisson_order_notes.md)、LG・G2・周期の基礎は [接続ノート](research/cayley_lg_connections.md)。全四周期の現行結論は上記conic周期ノートを参照する。

## 再現と検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_conic_period_coordinates.py
python3 computations/verify_all.py  # 全28検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回の新検証器はQ・整数格子・Laurent恒等式でPASS。証明書は `computations/conic_period_coordinates_certificate.json`。縮約・標識・gluing・period比較・Hodge分裂は本文の通常証明であり、計算だけで形式検証したとはしない。
新節単体はLuaLaTeX4頁に組版し、全頁画像・内部参照・overfullなしを確認。主論文の更新差分で既存証明を保持したことを確認した。主論文全体の今回の再組版、旧27検証器の全再実行、独立査読、新規性の網羅調査は未実施。

GitHub mainが正本。**push済み内容をLibraryへ保存しない。** PDF・ZIP・ログ・組版中間物はGitで追跡しない。他の研究は [分類](https://github.com/uedakazushi/nc-cubic-moduli)、[ambient比較](https://github.com/uedakazushi/nc-cubic-ambient)、[非AS短報](https://github.com/uedakazushi/nc-cubic-non-as) を参照する。
移行元の内容は [固定source commit](https://github.com/uedakazushi/nc-cubic-moduli/tree/c5fd8a8301f6b1c283a6f0510cde80ae6a006e80) を基準に抽出済みで、旧bundleの取得は再開の前提ではない。
