# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v27。
**数学的に面白くすることを最優先とし、多様な分野との具体的な接続を探す。** 量子so3・中心三次切断・一次元表現を、非可換幾何、指標多様体、特異点、周期、算術、力学、局所化、絡み目の共通模型として研究する。八次元E6成分の分類は保持するが、その完成を他分野との比較の前提にしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。日本語LuaLaTeX主論文は [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の成果も同じ論文へ統合する。

## 周期に見えない力学を、二つのcuspと絡み目で観測する

全H2・periodを固定する四Vieta合成gは、境界付値ではM=[[1,-2],[-2,5]]により双曲的に作用する。M^n=[[a_n,-b_n],[-b_n,c_n]]、d_n=b_n+c_n=1,7,41,239,...。最小次数はPell式に従い、射の極filtrationの歪み率はlog(3+2sqrt2)。通常のアフィンPerf(U)のDHKK entropyは生成元O_Uを固定するため零で、これとは別の量である。

一般conic C0={v=kappa}の反復逆像の閉包は、**一つの境界頂点に二つのPuiseux対(b_n,c_n)の枝**を持つ。二枝の相互交叉はb_nc_n、linkはT(2b_n,2c_n)。解消後の二点z=rho±はz+z^-1=2kappaを満たし、Pell型の特異性が増大しても元のconicの係数を保持する。

閉包の算術種数delta_n=1+2b_nc_n-b_n-c_nは、全てその一点の正規化欠損に等しい。正規化の押出し層の対象成長率はlog Lambda、欠損層は2log Lambda、開曲面へ制限すると前者は二項自由解消、後者は零。これらは対象列の率であり、新しい自己関手のentropyではない。

局所Milnor fiberは種数delta_n−1、二境界成分を持ち、H1 monodromyの位数は2b_nc_n。各monodromyは有限位数だが、その位数の列は指数増大する。明示Chebyshev実morsificationをCasalsの既知定理へ適用し、局所Weinstein pairのLagrangian曲面とthimble模型も得た。これを元の大域曲面やgのwrapped自己同値と同一視しない。

証明は [境界linkと正規化欠損](papers/sections/quantum_cubic_boundary_links.tex)、前提は [境界Pell](papers/sections/quantum_cubic_boundary_dynamics.tex) と [局所化とentropy](papers/sections/quantum_cubic_localization_entropy.tex)。具体式・適用範囲・一次文献・次の着手は [境界研究ノート](research/boundary_pell_dynamics.md) にまとめた。

## 保持する他分野との接続

対称LGのtriality不変格子と余不変格子の指数3からperiod isogeny(xi,eta)→(xi,eta³)を得、そのWeyl商がBoalch–PalubaのG2三成分写像に一致する。共通の明示開集合では三成分の有理MHSを比較し、Kleinと二コンパニオンの整数拡大位数7,21,21の差を検出する。有理Hodge同型から曲面同型・圏同値は推論しない。
一次元表現の勾配写像のramification divisorはCayleyの閉トーラスSL2指標多様体。D4 miniversal、Milnor–Picard整数比較、外部triality、G2のD4/A2共通退化、二種類のbraid、Klein七点上のS7を保持する。pillowcase、elliptopeと内部実sheet一意性、nearly Kählerの共通凸体も比較する。
conic標識による全四periodは(z1/z2,z2/z3,z3/z4,z3*z4)。有理Hodge分裂を円分性で判定し、分裂・非分裂の有理係数例を得た。対数matching積分とarcsine周期を保持する。被覆の分岐、Casimir値の衝突、LG臨界値の衝突は異なる。
七次元PBW正常形、横断積分、仮定付き八次元HH変形、全Artin表示族、smooth DM表示stack、結節因子、AW/Fricke、root Poisson括弧9倍、Delta15=N5²M5とS5×S5は主論文に保持。全intrinsic H3代数化・降下・全境界、一般相対AS4、全Casimir値のAzumaya性、全rank五接続、filtered equivariant mirrorは未完成。

基礎は [研究ノート](research/research_notes.md)、DAHA/skein/Painlevé/mirrorは [文献比較](research/fricke_daha_comparison.md)、二五次被覆は [Poissonノート](research/poisson_order_notes.md)、LG/G2/braidは [接続ノート](research/cayley_lg_connections.md)、全周期は [周期ノート](research/conic_period_coordinates.md) を参照する。

## 再現と検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_boundary_torus_links.py
python3 computations/verify_all.py  # 全32検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回は新しい境界link検証器をQ・Z上で実行しPASS。全係数先頭式、帰納式、24反復の整数値、最初の局所Jacobi次元27・conductor14、monodromy多項式とChebyshev resultantsを確認。小証明書は `computations/boundary_torus_links_certificate.json`。全nの証明、Puiseux/link、Milnor、DHKK、Casals構成は通常証明と一次資料への依存であり、計算のみの形式検証ではない。
新節単体はLuaLaTeX5頁に組版し、全頁画像・内部参照・overfullなしを点検。主論文全体の今回の組版、旧31検証器の全再実行、独立査読、新規性の網羅調査は未実施。更新差分で旧証明本文・入力節・文献表の保持を確認する。

GitHub mainが正本。**pushした内容はLibraryに保存しない。** PDF・ZIP・ログ・中間生成物はGitで追跡しない。全分類は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli) を別の正本とする。旧bundleは再開の前提ではない。
