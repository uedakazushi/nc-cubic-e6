# 楕円 E6 量子化成分 — nc-cubic-e6

内在的非可換三次曲面H3の、量子so3・Fricke cubic・Askey–Wilson部分族を含む8次元候補成分を研究する。

**最初に [研究方針](00_research_plan.md) を読む。** 現行日本語LuaLaTeX原稿は [quantum_cubic_component.tex](papers/nc-cubic-e6.tex)、[研究ノート](research/research_notes.md)、[Fricke/DAHA比較](research/fricke_daha_comparison.md)。

主原稿で読み込む証明節は `papers/sections/quantum_cubic_*.tex`。固定位数3の一般H3認識・三角境界の関連証明は必要な範囲で別途保持する。**全intrinsic H3成分の大域閉包・全境界と相対AS4認識は未完成**。

## 再現
```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_all.py
latexmk -lualatex papers/nc-cubic-e6.tex
```

GitHub mainが正本。PDF・ZIP・組版中間物は追跡しない。他の研究は [分類](https://github.com/uedakazushi/nc-cubic-moduli)、[ambient比較](https://github.com/uedakazushi/nc-cubic-ambient-moduli)、[非AS短報](https://github.com/uedakazushi/nc-cubic-non-as) を参照。
移行元の資料は [固定source commit](https://github.com/uedakazushi/nc-cubic-moduli/tree/c5fd8a8301f6b1c283a6f0510cde80ae6a006e80) を基準に抽出した。旧bundleは不要。
