# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-18 / e6-connections-v31。
**数学的に面白くすることを最優先し、多様な分野との具体的な接続を探す。** 量子so3・中心三次切断・一次元表現から、指標多様体、Poisson、LG、特異点、周期、境界力学、局所圏へ進む。八次元E6成分の分類は保持するが、その完成を他分野研究の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。主論文は日本語LuaLaTeXの [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の公表価値ある成果も同じ論文に統合する。

## 境界modulusをMilnor被覆のHodge因子へ

境界二枝の重み付き模型 F=y^(2b)−2kappa x^c y^b+x^(2c) に対し、F=1の射影模型をCとする。四点配置から付随させた楕円曲線 E:eta²=z(z²−2kappa z+1) への写像には、指定z=y^b/x^cの下で平方類[x]の障害がある。
**a²=xの二次Kummer被覆tildeCでは、z=y^b/a^(2c), eta=y^(b/2)/a^(3c)が次数2bcの有限写像を与える。** deck involutionがEの逆元に対応し、EはPrym(tildeC/C)のisogeny因子となる。

全Pell指数に共通するgenus3のCiani四次 X4+Y4−2kappa X²Y²=Z4 が中間に入り、JacobianはEi²×D_kにisogenous（Eiはj1728）。D_k→Eの2isogenyにより、以前のlevel2対応を実際の商写像で実現する。高genusが増大しても同じ可変楕円因子が残り、その周期は (kappa²−1)Pi''+2kappa Pi'+Pi/4=0 を満たす。
証明は [Prym・Ciani・dg復元の節](papers/sections/quantum_cubic_boundary_prym.tex)。Prym理論、Ciani分解、dg復元の一般定理は既知として引用し、この明示構成と区別する。

## 巡回Prymの整数偏極と極端有理楕円曲面

Milnorの二次Kummer被覆からCianiの楕円$D_κ$への射は**次数$bc$の巡回Galois被覆**、合成して$E_κ$への射は次数$2bc$の巡回Galois被覆。前者の完全分岐と$D_κ→E_κ$の非分岐二同種により、$J(E_κ)→J(\widetilde C)$の核が正確に標識二捩れ$[(0,0)-O]$と分かる。Prym内の楕円因子$D_κ$への標準thetaの制限次数は**$bc=10,348,11830,\dots$**。Prym全体が整数直積として分裂したわけではない。

さらに$E_κ:\eta^2=z^3-2κz^2+z$を$\mathbb P^1_κ$上で動かすと、$I_1,I_1,I_4^*$の三fiberを持つMiranda--Perssonの極端有理楕円曲面**$X_{411}$**となる。Mordell--Weilは$\mathbb Z/2$で、$j=64(4κ^2-3)^3/(κ^2-1)$は次数6、分岐型$(3,3),(2,2,2),(4,1,1)$のBelyi写像。六枚の幾何学的置換群は$S_4$（$S_4/C_4$の六剰余類への忠実な作用）で、厳密なbranch cycle計算を再現可能にした。Poisson零点にも現れる$S_4$との標準同定は未構成。古典的な楕円曲面の分類そのものは既知で、今回はPell--Prym系との具体的接続として同定した。

[整数偏極・Belyiの新節](papers/sections/quantum_cubic_prym_polarization.tex) ／ [再現コード](computations/verify_prym_integral_belyi.py) ／ [現行研究ノート](research/boundary_analytic_moduli.md)。

## 位相・模型・実germ・圏の区別

模型の二周期MFは(n,K=kappa²)でdg Morita分類される。同じlink・閾値・HH次元でもHochschildの積がmodulusを検出する。Kは二捩れ標識付き楕円曲線の粗modulus Y0(2)でもあり、jやisogenyだけではMF模型を区別できない。

一方、実際のA=B=C=0,h=1、初期v=2の一反復境界はmu27,tau24、主部はmu=tau27で接触非同値。Hua–Kellerの最終版Thm5.9を適用し、**通常の整数次数付きdg特異点圏**もHH0次元24対27でMorita非同値と分かった。
二周期MFの相対HH=Jacobianと整数次数付きdg圏の絶対HH0=Tjurinaを混同しない。両者の忘却・periodizationの全比較、実germへのPrym構成、整数偏極付きの分解、MF部分圏やHMSは未構成。
具体式・一次文献・再開課題は [境界解析・MF・Prymノート](research/boundary_analytic_moduli.md)。

## 保持する成果

境界Newton閾値(b+c)/(2bc)、局所MF次元(2b−1)(2c−1)、Pell反復最低次数1,7,41,...、有限境界blow-up非正則化、二枝linkとconductor、正規化欠損、局所Weinstein模型を保持する。通常affine Perf entropyは零、射filtration率log Lambda、proper閉包対象列率2log Lambdaは異なる量。
量子中心とFricke/AW、root Poisson括弧9倍、七次元正常形・八次元形式族、二五次S5×S5、Cayley/LG/D4、Milnor–Picard、G2 D4/A2、全四period、trialityと三成分Hodge比較の証明を削除していない。
全intrinsic H3の代数化・降下・全境界、非可換H3圏の自己同値、filtered equivariant HMSは未完成。

主題別に [基礎](research/research_notes.md)、[DAHA比較](research/fricke_daha_comparison.md)、[Poisson](research/poisson_order_notes.md)、[LG/G2](research/cayley_lg_connections.md)、[全period](research/conic_period_coordinates.md)、[境界力学](research/boundary_pell_dynamics.md) を参照する。

## 再現・確認済み範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_prym_integral_belyi.py
python3 computations/verify_all.py  # 全36検証器。今回は全実行していない
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回の巡回Prym検証器は整数合同式、Pell分岐数、楕円Weierstrass不変量、Belyi分岐を厳密計算してPASS。完全分岐からのJacobian単射、norm・偏極、Kodaira/Shioda--Tateは通常の証明と一次資料の入力。旧35検証器の全再実行、主論文全体の今回の組版、独立査読、新規性網羅調査は未実施。新節単体の組版状態は研究方針に明記する。既存の証明本文・入力節を保持。

GitHub mainが正本。**push済み内容をLibraryへ保存しない。** PDF・ZIP・ログ・組版中間物はGitで追跡しない。全H3分類は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli)、関連研究は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) と [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as) を参照する。
