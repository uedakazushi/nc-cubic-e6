# 非可換三次曲面を結ぶ幾何学 — nc-cubic-e6

2026-11-17 / e6-connections-v19。
**数学的に面白くすることを最優先とし、多様な分野との具体的な接続を優先して探す。** 量子so3とその中心三次切断を、非可換三次曲面・DAHA・指標多様体・特異点論・実幾何の共通の例として研究する。既存の八次元E6成分研究は保持するが、分類の完成を他分野との比較の前提にはしない。

再開時は [研究方針](00_research_plan.md) を最初に読む。主論文は日本語LuaLaTeXの [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。関連分野の成果もこの同じ主論文へ統合する。

## 一つの写像から現れる接続

正規化した一次元表現の五重被覆は

\[
\Phi(u,v,w)=(vw-u,wu-v,uv-w)
=\nabla\left(uvw-\frac12(u^2+v^2+w^2)\right).
\]

この写像のramification divisorはCayley三次曲面で、閉トーラスのSL2指標多様体に一致する。四つの特殊fiberでは四枚のsheetがD4型で衝突し、三係数が加法定数を除くミニバーサル変形を与える。同じ構成にLandau–Ginzburgポテンシャル、exact Lagrangian射影、trialityの位数3作用、Jacobi留数代数、実pillowcase、相関行列のelliptopeが現れる。elliptope内部では勾配写像が単射なので、そこにある実sheetは高々一つ。

証明は主論文の [Cayley・LG・D4・実幾何の節](papers/sections/quantum_cubic_cayley_lg.tex)、再開用の具体式と一次文献は [接続ノート](research/cayley_lg_connections.md)。古典的なCayley商・D4変形・elliptope自体を新発見と主張せず、指定した表現被覆との明示的な対応と帰結を証明する。Picard D4とMilnor D4の標準同定、mirror/Fukaya同値、nearly Kähler幾何との圏的対応は未構成。

**重要な区別：** Casimir値の衝突と五重被覆そのものの分岐は別現象であり、LG臨界値もCasimir値と同じではない。判別式の基底変換公式と具体例を主論文に組み込んだ。

## 保持する既存成果

七次元PBW正常形、三捩れからの横断積分、条件を明示した八次元Hochschild変形、全Artin表示族、smooth DM表示stackを保持する。結節中心は固定包絡で五SNC因子・A4商で二成分、七次元族では連結五重被覆から既約六次元因子となる。主論文の全既存証明節は残している。

AW中央特殊化とCasimir規約、四穴球面Fricke係数への優越写像、量子的Vieta、Goldman型Poisson括弧、三角境界とD4⊂E6を明示した。Q=q exp(h)の交換子微分は本稿のJacobian括弧の9倍。純粋q変形での非Casimir切断の持上げと固定pointed H3心へのVieta作用には障害があるが、一般の圏変形や心の変更を否定するものではない。

相対Poisson臨界環は有限平坦次数15、一次元表現環は次数5。Casimir臨界値多項式はDelta15=N5²M5と分解し、二つの五次因子の同時幾何学的Galois群はS5×S5。全H3 admissibility、intrinsic降下、全境界、一般相対AS4認識、全Casimir値でのAzumaya性は未完成。

基礎知識は [研究ノート](research/research_notes.md)、DAHA/skein/Painlevé/mirror比較は [関連文献ノート](research/fricke_daha_comparison.md)、二つの五次被覆と延長障害は [Poissonノート](research/poisson_order_notes.md) を参照する。

## 再現と検証範囲

```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_cayley_lg_connections.py
python3 computations/verify_all.py  # 全24検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```

今回実行した新検証器は有理数体上の記号演算でPASS。小証明書は `computations/cayley_lg_connections_certificate.json`。新節だけの一時的LuaLaTeX wrapperは5頁で組版成功し、本文外の二つの参照はwrapperでは未解決。主論文全体の今回の組版、旧23検証器の全再実行、独立査読、新規性の網羅調査は未実施。通常の証明と有限恒等式の検算を区別する。

GitHub mainが正本。**GitHubへpush済みの内容はLibraryに保存しない。** PDF・ZIP・組版中間物はGitで追跡しない。他の研究は [分類](https://github.com/uedakazushi/nc-cubic-moduli)、[ambient比較](https://github.com/uedakazushi/nc-cubic-ambient-moduli)、[非AS短報](https://github.com/uedakazushi/nc-cubic-non-as) を参照。
移行元の資料は [固定source commit](https://github.com/uedakazushi/nc-cubic-moduli/tree/c5fd8a8301f6b1c283a6f0510cde80ae6a006e80) を基準に抽出した。旧bundleの取得は再開の前提ではない。
