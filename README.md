# 楕円 E6 量子化成分 — nc-cubic-e6

2026-11-17 / triangle-component-v18。
内在的非可換三次曲面H3の、量子so3・Fricke cubic・Askey–Wilson部分族を含む8次元候補成分と、関連分野への具体的な接続を研究する。

**最初に [研究方針](00_research_plan.md) を読む。** 現行日本語LuaLaTeX原稿は [nc-cubic-e6.tex](papers/nc-cubic-e6.tex)。基本知識は [研究ノート](research/research_notes.md)、関連分野は [Fricke/DAHA比較](research/fricke_daha_comparison.md) と [Poisson量子化・延長障害ノート](research/poisson_order_notes.md) を参照する。公表価値のある関連分野研究も同じ主論文へ統合する。

固定包絡の結節中心H3切断五例を厳密計算で認識し、許容四次元族では五つの正規交叉因子・A4商で二既約成分を得た。七次元族では1次元表現の連結五重被覆から、この結節中心軌跡が一つの既約六次元因子になる（主論文 `thm:nodal-divisors`, `thm:seven-nodal-irreducible`）。

**普遍Askey–Wilson代数・Casimir規約との表示同型、四穴球面Fricke係数への優越写像、量子的Fricke–Vieta生成元、Goldman型Poisson・log Calabi–Yau三角境界・PicardのD4⊂E6格子** を明示した（`papers/sections/quantum_cubic_daha_character.tex`）。古典的なFricke実現と根格子同定は既知結果であり、新規性と計算の独立確認を区別する。三角境界は一般E6の楕円境界とは異なる。

**量子化からのPoisson構造と二つの障害** を主論文に統合した（`papers/sections/quantum_cubic_poisson_orders.tex`）。Q=q exp(h) の交換子微分はFrickeのJacobian括弧の正確に9倍であり、Brown–Gordonにより同一smooth locus上の中心fiber代数を比較できる。一方、Omega係数が非零の非Casimir切断は指定した純粋q変形の平坦商に一次で持ち上がらず、Vieta作用は固定pointed H3心に延長しない。これは抽象変形・導来同値の非存在ではなく、同時Sklyanin変形と心を動かす対応を研究するための障害である。

**固定包絡のCasimir pencilに十個のPoisson零点を完全列挙**し、総中心の五節点と五滑らか臨界点を区別した。中心曲面の特異値は4つで全てA1型だが、二つの値だけが既存判定によりH3となる。平滑化の二次接触／一次横断、一次元表現の中心character、VietaとA4による符号四点のS4作用も証明した（`papers/sections/quantum_cubic_casimir_leaves.tex`）。

**相対Poisson臨界被覆の有限平坦性とS5対称性：** 三低次係数の全域で相対臨界環は次数15、一次元表現は次数5で有限平坦。Casimir切断の判別式は \(\Delta_{15}=N_5^2M_5\) と因数分解し、一次元表現のCasimir norm \(N_5\) は既約五次でGalois群 \(S_5\)。主論文 `papers/sections/quantum_cubic_relative_poisson.tex` に証明を統合し、`computations/verify_relative_poisson_cover.py` と小証明書に再現計算を保存した。さらに \(M_5\) も幾何学的に既約・Galois群 \(S_5\)、二つの分解体は線型非交叉で、同時monodromyが \(S_5\times S_5\) となる（\`thm:paired-quintic-S5\`、\`computations/verify_companion_s5.py\`）。分岐因子と全H3判定は未解決。

主原稿で読み込む証明節は `papers/sections/quantum_cubic_*.tex`。固定位数3の一般H3認識・三角境界の関連証明も必要な範囲で保持する。**全intrinsic H3成分の大域閉包・全境界と一般相対AS4認識は未完成**。全Casimir値でのAzumaya性や導来Vieta対応も未解決。

## 再現と今回の検証範囲
```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_root_poisson.py
python3 computations/verify_poisson_cut_obstruction.py
python3 computations/verify_companion_s5.py
python3 computations/verify_all.py  # 全23検証器
latexmk -lualatex papers/nc-cubic-e6.tex
```
今回新規実行した二素数Frobenius検証器の小証明書は `computations/companion_s5_certificate.json`。前回の相対Poisson・S5検証器の証明書は `computations/relative_poisson_cover_certificate.json`。前回のCasimir零点検証器の証明書は `computations/casimir_poisson_leaves_certificate.json`。他の22検証器の今回の全再実行は未実施。前回の五検証器の結果は `computations/connections_validation.json` に記録。DAHA節と新Poisson節の一時的wrapperによるLuaLaTeX組版・該当頁点検は成功したが、主論文全体の今回の再組版ではない。

GitHub mainが正本。**GitHubへpush済みの内容はLibraryに重複保存しない。** PDF・ZIP・組版中間物はGitで追跡しない。他の研究は [分類](https://github.com/uedakazushi/nc-cubic-moduli)、[ambient比較](https://github.com/uedakazushi/nc-cubic-ambient-moduli)、[非AS短報](https://github.com/uedakazushi/nc-cubic-non-as) を参照。
移行元の資料は [固定source commit](https://github.com/uedakazushi/nc-cubic-moduli/tree/c5fd8a8301f6b1c283a6f0510cde80ae6a006e80) を基準に抽出した。旧bundleは不要。
