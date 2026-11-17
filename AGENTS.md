# 研究継続指示 — nc-cubic-e6

2026-11-18 / publication-v33。最初に 00_research_plan.md を読む。

## 現行の構成

- 主論文：papers/nc-cubic-e6.tex（正常形・形式変形・R(1,3)中心切断・AOU比較）。
- 関連論文：papers/fricke-geometry.tex（中心・Poisson被覆・D4周期・triality）。
- 関連論文：papers/cubic-boundary-prym.tex（Pell力学・境界特異点・局所圏・Prym）。
- 共通設定・文献：papers/shared/。各原稿は独立に組版できる。
- 研究ノートの案内と優先課題：研究方針。検証範囲：research/publication_status.md。
- 既存H3入力断片は補助資料。三原稿から読み込まない断片の存在を、全依存証明の完成と取り違えない。

数学的重要性・新規性・理解・応用・正確性・実現可能性を総合して研究価値を最大化する。
現在の最優先は三論文の公表準備。分野間の接続を保持し、既存の価値ある結果と必要証明を削らない。
日本語LuaLaTeX、著者欄は空欄。証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。
一次資料を確認し、原稿の証明・今回の点検・コードの実行・独立査読・新規性確認を別に記す。

## 外してはいけない適用範囲

- 一般のE6八次元表示族はR(1,3)包絡の中心三次商と同じ表示成分。包絡7＋切断1と、固定三捩れの包絡3＋切断4＝曲面7を混同しない。全intrinsic成分の追加仮定は維持する。
- 七次元正常形は固定位数三・中央境界・対角非零の範囲。
- HH²=8、HH³=0は滑らかな中心・反標準楕円分岐と指定局所order模型の下の定理。
- 八変数形式表示と代数的表示stackを、全intrinsic H3の開性・降下・成分境界の完成と同一視しない。
- 反標準環から二次包絡を復元できるのは、表示環の飽和性と構造対象を保つexact同値の範囲。
  AOU §9の無限位数blow-up表示は区別できるが、有限位数を含むAS曲面一般や任意の導来同値を除外していない。
  q³=1の循環量子平面のpoint schemeはP²全体であり、三角形ではない。
- Fricke中心、一次元表現、LG値h、Casimir値D、幾何モノドロミーと有限体分解型を区別する。
- 模型MFの分類を実高重みgermへ延長しない。二周期相対HH=Jacと通常Z-graded dg特異点圏のHH⁰=Tjurinaを区別する。
- Prymの有理Hodge/isogeny因子を整数直積分解、MF部分圏、HMSと読み替えない。
  theta線束の次数bcと偏極isogenyの次数(bc)²を区別する。
- affine Perf entropy=0、射のfiltration率logΛ、proper対象列率2logΛを区別する。

## 保存と再現

GitHub main が正本。約15分または区切りで通常のfast-forward保存を行う。
force push、不要なPR・Actionsは使わない。PDF・ZIP・ログ・キャッシュ・組版中間物をGitで追跡しない。
最新のユーザー指示に従い、研究の区切りで現在の方針・ノート・論文・PDF・再現資産からなる軽量bundleを、
再確認せず保存する。GitHubへのpush後も研究継続用bundleをLibraryへ保存する許可がある。
既存Libraryファイルの削除は明示指示なしに行わない。
生成・検証・commit・push・保存の状態を別々に確認する。

検証入口は make sources, make comparison, make verify, make papers, make bundle。
各主原稿にdocumentclassと自己TeX root指定を保持し、TeX programコメントでlatexmkレシピを迂回しない。ルートとpapers/の双方から組版できる入力パスを維持する。
新しい引用は各論文末尾の UsePublicationReferences のリストにも追加する。
数学に関係するコードを変更した場合だけ、その依存計算を再実行する。
一度確認した検証を、具体的理由なく繰り返さない。全研究継続原則は研究方針§Iにある。
