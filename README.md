# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-18 / e6-connections-v29。
**数学的に面白くすることを最優先し、多様な分野との具体的な接続を探す。** 量子so3・中心三次切断・一次元表現から、指標多様体、Poisson、LG、特異点、周期、境界力学、局所圏へ進む。八次元E6成分の分類は保持するが、その完成を他分野研究の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。主論文は日本語LuaLaTeXの [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の公表価値ある成果も同じ論文に統合する。

## 境界の位相が忘れる係数と圏

Pell反復の境界二枝の主部は F_nk=y^(2b_n)−2kappa x^(c_n)y^(b_n)+x^(2c_n)。全て同じnでは同じトーラス絡み目を持つが、K=kappa²は実際の高重み項を持つgermにも残る解析的不変量である。
**重み付き模型**の二周期matrix factorization圏は、dg Morita同値であるための必要十分条件が「nとKの一致」となる。同じlink・閾値・Hochschild次元でも、Hochschildの積が連続なmodulusを検出する。証明にはDyckerhoffとMather–Yauの既知定理を使い、その一般理論自体を新規としない。

解消上の四点0,infty,rho±から二捩れT=(0,0)付き楕円曲線 eta²=z(z²−2kappa z+1)を付随させる。その粗modulusもKで、j=64(4K−3)³/(K−1)。同じj1728でもK=0と9/8はMF模型が非同値。二同種写像K→K/(K−1)も一般にはMF同値を与えない。この付随楕円曲線を元の反標準境界やMilnor fiberの商と同一視していない。

**実際のgermと主部は別である。** A=B=C=0,h=1、初期conic v=2の一反復では、元のVieta式から厳密にmu=27,tau=24を得た。主部はmu=tau27なので接触非同値。模型のMorita分類を実germへ無条件に延長せず、Jacobian環中の指定類[f]と高重み項の役割を次の課題とする。
証明は [解析modulusの節](papers/sections/quantum_cubic_boundary_moduli.tex)、再開用情報は [解析・MFノート](research/boundary_analytic_moduli.md)。

## 既存の接続と保持する成果

Newton閾値は(b+c)/(2bc)、局所MFのHH次元は(2b−1)(2c−1)。これらの結果も前回の未反映分から主論文へ統合した。反復による閾値の減衰率log LambdaとHH次元増大率2log Lambdaを、自己関手のentropyと混同しない。
境界力学では、全periodを固定するgがPell行列M=[[1,-2],[-2,5]]で境界を動かし、最低次数1,7,41,...を持つ。アフィンPerfのDHKK entropyは零、射の極filtrationの歪み率はlog Lambda、閉包対象列の複雑度率は2log Lambda。二枝のPuiseux対、T(2b,2c) link、conductor、正規化欠損、Chebyshevと局所Weinstein模型を保持する。

量子中心とFricke/AW、root Poisson括弧9倍、七次元正常形・八次元形式族、二五次被覆のS5×S5、Cayley/LG/D4、Milnor–Picard、G2のD4/A2、全四period、trialityと三成分Hodge比較の証明は削除していない。
全intrinsic H3の代数化・降下・全境界、元の非可換H3圏の自己同値、filtered equivariant HMS、一般高重みgermのMF分類は未完成。

主題別に [基礎ノート](research/research_notes.md)、[DAHA比較](research/fricke_daha_comparison.md)、[Poisson](research/poisson_order_notes.md)、[LG/G2](research/cayley_lg_connections.md)、[全period](research/conic_period_coordinates.md)、[境界力学](research/boundary_pell_dynamics.md) を参照する。

## 再現と確認済み範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_boundary_thresholds.py
python3 computations/verify_boundary_analytic_moduli.py
python3 computations/verify_all.py  # 全34検証器。今回は全実行していない
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回の個別二検証器は厳密演算でPASS。模型Jacobian環、楕円曲線・二同種恒等式、元のVietaからのresultant、正則初期列で正当化した有限jetのrank18/21を確認した。通常の分類証明・Morita不変性・strictnessの理論と、有限計算は別である。
新解析modulus節単体をLuaLaTeX5頁に組版し、画像・内部参照・overfullを点検。主論文全体の今回の再組版、既存32検証器の全再実行、独立査読、新規性の網羅調査は未実施。既存の証明本文・入力節・文献表の保持を主論文差分で確認した。

GitHub mainが正本。**push済み内容をLibraryへ保存しない。** PDF・ZIP・ログ・組版中間物はGitで追跡しない。全H3分類は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli)、関連研究は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) と [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) を参照する。
