# 研究方針：楕円E6量子化成分の完全決定

2026-11-17 / triangle-component-v14 / 独立リポジトリ。**再開時は本書を最初に読む。**
この一式は `nc-cubic-e6` の成分研究に必要な現行成果を集約したもので、旧bundleを必要としない。
パスはリポジトリrootからの相対パスで記す。本体は `papers/nc-cubic-e6.tex`、補足は `research/research_notes.md`。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。
重要な方針変更では現在の理由と元の目標の達成部分・残存部分を明記し、時系列の変更履歴を蓄積しない。
証明済み、追加仮定付き、未完成、予想、計算的観察を区別し、主要主張の仮定・依存結果・証明箇所・未解決部分を明記する。
原稿に証明があること、今回の点検、計算の実行、独立査読を混同しない。誤りは依存する要約・本文・方針にも反映する。
先行研究は一次資料で確認し、適用範囲を比較する。未確認の文献内容・書誌・新規性を推測で埋めない。
原稿は日本語LuaLaTeXを原則とし、現在の成果を論理順に構成する。公表価値のある結果と必要な証明を削除して軽量化しない。
ノートは有用な補題、着想、障害、反例、文献比較、再取得困難な情報を保持し、日誌や重複証明にしない。
最新の方針・ノート・論文と必要最小限のコード・証明書だけで再開できるようにする。旧ZIP、旧原稿、ログ、キャッシュ、バックアップを含めない。
研究の区切りごとにユーザーの追加承諾なく軽量で自己完結した現行研究bundleをLibraryへ保存することは許可されている。GitHub mainを開発上の正本とし、成功時も現行版の継続bundleを別途Libraryに保存する。Library既存資料は明示指示なしに削除しない。
日付・版番号を付け、生成・検証・commit・push・Library保存を別状態として報告する。通常のfast-forward main保存のみを使い、force push、不要なPR、GitHub Actionsは使わない。

## II. 現在の目標と達成基準

**上位目標は、非可換三次曲面の楕円E6量子化成分の幾何学的理解と公表価値を最大化すること。**
中心課題は既知の7次元H3族を含む既約成分の完全決定だが、それと並行して四穴球面character variety、Askey--Wilson/DAHA、skein・Goldman Poisson・cluster/mirrorとの厳密な相互関係を定式化する。
従来の目標について、七次元族・八次元形式近傍・表示stack・結節中心因子までは解決したが、全intrinsic族の代数化と全境界の分類は未解決。
対象は構造対象付きexact同値を射とするintrinsic H3であり、単なる導来同値類ではない。
達成基準は、成分の存在と一意性、次元・一般点、全対象の被覆、全矢・慣性、境界・交叉、相対再構成・降下を揃えること。
元の固定包絡4次元族の成分性は否定済み。7次元族は3-torsion中央境界の開正常形であり、最終的な成分と決め打ちしない。
現在の有力候補は一般のEtingof--Ginzburg型中央三次商を含む8次元成分である。
全H3分類の他の枝の進捗をこの限定研究から置き換えない。

## III. 到達点と確実性

1. **七次元族の構成と全同型。** 包絡 `yz-qzy=tx+a t^2`（巡回）、q^2+q+1=0。
   全係数PBW/CY AS4、五つの中心三次、全中心の三次式を保持。
   楕円境界開集合で既存の有限位数H3開性を使い `[V/A4]` を得る。
   4次元固定包絡族はa=b=c=0の余次元3部分。原稿§2。
2. **固定位数3の正常形。** 全対称PBW行列Aの非対角を一意の平行移動で消去し、対角3係数が非零の開集合を正規化する。
   7次元族はこの範囲の全正常形である。原稿定理3.1。全係数恒等式を実行済み。
3. **三捩れを離れる積分。** Hesse曲線Eを固定し平行移動点を動かす。
   低次中心が定数だけであることから9×9の単元minorを使い、指定中心三次の持上げを全次数で構成する。
   Rees包絡・商は平坦、一般中心値は中心局所化によって有限大域次元、従ってH3となる。原稿§4。
   任意の固定数値DでのH3性や、有限位数を横断する一様H3開性は主張しない。
4. **一般点のHochschild cohomology。** 中心が滑らかな三次曲面C、分岐が滑らかなD=-K_C、局所orderがroot模型の場合、
   HH^0=k, HH^1=0, dim HH^2=8, HH^{>=3}=0。
   内訳はH^1(T_C(-logD))の7方向とH^0(O_C)の1方向。圏の形式変形は無障害。原稿定理5.3。
   全H3変形の相対再構成をこの定理に混入しない。
5. **厳密な接空間と有理積分の証明書。** 一つの滑らかなH3点で105×40行列rank18、核22、座標方向rank14、商8。
   既知7方向と明示横断方向が核を張る。別の明示的有理族の中央三次持上げを原関係で全係数検証。原稿§6。
6. **成分の8次元性は比較仮定を明示。** 相対H3モジュライの代数性、無限小変形の忠実な圏比較、8次元表示族の相対実現の下で、
   7次元族一般点を通る成分は唯一の8次元成分になる。原稿定理7.1。
   適合したenhanced Abel変形に対する圏比較の単射性は、下記の全Artin定理で解決した。相対代数性・H3族の実現と全大域境界は未完成であり、「完全分類済み」としない。
7. **全Artin底の相対再構成。** AS-Cohen--MacaulayなH3反標準列の正方向Ext消滅からDe Deken--Lowen Theorem4.5を適用し、適合したenhanced Abel変形からdg圏変形への同型類上の単射性を証明した。全dg変形にheartが存在するとは主張しない。相対Serre作用が底変更に適合するsmooth proper dg変形では反標準環は次数別有限自由・左右noetherianで、四生成元・六二次関係・一三次関係の表示を持つ。二次包絡のAS4性と三次の正則正規性は別の未解決条件。証明は原稿第8節（`thm:artin-injective`, `thm:artin-section-ring`）。

8. **結節中心H3因子の七次元族への結合。** 固定包絡の許容四次元切断空間では五つの独立な節点条件が単純正規交叉因子をなし、A4商では二つの既約因子となる。相異なる5つのA1中心H3例を厳密Jacobi基底で確認した。さらにa,b,cを動かすと一次元表現が係数原点のZariski近傍で連結な有限etale五重被覆を与え、五節点条件のincidenceは既約六次元因子になる。七次元H3許容開集合との交わりも既約である。証明は主論文`thm:nodal-divisors`, `prop:five-nodal-witnesses`, `thm:seven-nodal-irreducible`。厳密計算は`computations/verify_nodal_cuts.py`, `computations/verify_character_node_cover.py`。全八次元intrinsic成分への延長は未証明。

9. **DAHA--character varietyの厳密な接続。** 三乗根での普遍Askey--Wilson代数の中央特殊化と量子so3包絡の同型、Casimir規約 `Omega_AW=3(q+2)Omega`、Casimir切断中心からFricke係数空間への4次元優越写像を証明した。Goldmanの四穴球面トレース係数とも一般有限分離底変更で比較できる。Goldman--Toledoによる任意の適切なtritangent三次曲面のcharacter variety実現は既知であり、新規性を主張しない。Artin braid生成元がFricke--Vieta変換 `(u,v,w)->(v,u,-uv-C-w)` を非可換持上げし、Goldman型Jacobian Poisson構造を保つ。切断の三角形反標準境界はLooijenga pairで、Picard格子のD_i直交補はD4(-1)、K直交補はE6(-1)（既知幾何を明示的単純根で計算）。証明は主論文 `sec:daha-character`；独立厳密再生は `computations/verify_daha_character.py`, `verify_daha_braid.py`, `verify_d4_lattice.py`。これらの個別式の既出性・直接spherical DAHA同型・一般楕円E6全域への延長は未確認。

## IV. 次の課題と具体的な着手

**第一優先：DAHA--character varietyから楕円E6成分への幾何学的橋渡し。**
量子的Fricke--Vieta変換の対応をskein代数の半Dehn twistと一次文献の定理単位で比較し、Casimir切断（反標準三角境界）と楕円境界H3族を中央三次切断・平行移動の変形を介してつなぐ。Askey--Wilsonの三乗根特殊化とspherical DAHAの中心・Morita locusを区別して明示する。D4根格子を固定する境界三角形の周期写像・W(D4)作用と、境界を動かすE6格子/W(E6)作用の相違を調べる。構成可能なら有限位数でのPoisson orderとGoldman括弧の定数を計算し、character varietyのcluster/mirrorとの比較を新しい独立定理へ昇格する。比較の未確認点は `research/fricke_daha_comparison.md` を参照。

**第二優先：有限型表示stack内の全H3 admissibility。**
選んだ点の全Artin形式近傍は8変数族で分類済み。明示族は有限型底へ延び、相対THCR境界・全fiberの整域性・幾何学的一般点H3を認識した。さらにsmooth DM八次元表示stack [Z'/Gamma]とetale atlasを構成し、H3対象間の全幾何学的矢を決定した。
固定包絡・七次元族では結節中心であってもH3の内部に入ることが確定したため、中心の特異判別式をH3境界と同一視しない。七次元族の既約結節因子が八次元表示stackでどのように延長されるかを追跡する。次は一般中心値に限らない有限globaldimの全値判定を行う。悪い中心値、有限表示、局所Morita型を調べ、H3 locusのconstructibility/Zariski開性を証明するか反例を得る。形式smooth性だけから開性を推論しない。Rainsの次数3全被覆を未証明のまま使わない。

**第三優先：全intrinsic族の相対再構成と降下。**
幾何学的矢と全Artin形式分類は得たが、一般非被約有限型底のSerre作用・反標準環・二次包絡の底変更とfpqc降下はまだ別問題である。表示stackのH3部分が実際のintrinsic族を全て被覆する範囲を証明し、有限慣性・分離性を決定する。

**第四優先：全成分の閉包・境界。**
一般像の閉包に含まれるH3を、境界のsmooth/nodal/reducible型、PI位数、低次中心、Nakayama型で層別化する。
固定位数3の対角係数零、滑らかな楕円境界の欠落、他の表示chartへの移行を漏らさない。
RainsのE6/Weyl表示と比較するが、次数3・全パラメータ被覆を同文献の未証明部分から輸入しない。

## V. 再現と検証範囲

リポジトリrootで次を実行する。
```sh
python3 -m pip install -r computations/requirements.txt
python3 computations/verify_all.py
latexmk -lualatex papers/nc-cubic-e6.tex
```
コードと小証明書は同じ専用ディレクトリに置き、統合結果はその `validation.json` に再生成する。
通常の証明であるArtin再構成を計算PASSと同一視しない。既存13検証器の厳密計算PASSは旧証明書に記録されている。新規`verify_nodal_cuts.py`と`verify_character_node_cover.py`は今回厳密再実行した。
今回のDAHA節の独立LuaLaTeX組版（六頁）を確認し、DAHA二検証器およびD4格子検証器を厳密演算で実行した。主論文全体の組版は未実施。巨大な既存H3原稿全体の再組版・網羅再検証・独立査読は対象外。
Git追跡対象は現行TeX・Markdown・Python・小JSONのみ。PDF・ZIP・中間物・cacheは含めない。
生成・検証結果はコードと文書に、GitHub refの到達確認は保存時の応答に分けて記載する。
