# conic標識・四つのD4周期・円分的Hodge分裂

2026-11-17 / e6-connections-v23。再開時は `../00_research_plan.md` を読む。
証明は `../papers/sections/quantum_cubic_four_periods.tex` にあり、主論文 `nc-cubic-e6.tex` が直接読む。対数積分と境界正規化は `quantum_cubic_log_periods.tex`、位相は `quantum_cubic_lg_picard.tex`。本ノートは式・適用範囲・次の着手を整理する。従来ノートの「全四内部周期が未計算」という課題は、以下のconic開集合と有限標識被覆の範囲では解決している。全rank五の代数的接続行列の構成とは別である。

## 1. 対象・開条件・整数標識

W=uvw−(u²+v²+w²)/2−Au−Bv−Cw、U={W=h}、omega=du∧dv/(uv−w−C)。境界周期は(2pi i)²。
N(u)=(u²+2Au+2h)(u²−1)+B²+C²+2uBC。
今回の適用範囲は **Disc N≠0, B²−C²≠0**。これは十分なsmooth chartで、全smooth locusの必要条件ではない。以前のA=B=C=0のarcsine sliceはこのchartに直接入らないが、そちらの独立証明は有効である。

射影閉包のD1={u_hom=t=0}はconic pencilの二重切断。特異fiberは四根u_iと無限遠D2+D3。
D1,D2に交わらずD3に交わるline section sを選び、各fiberのsと交わらない成分E1..E4とE5=D2を縮約するとF1となる。したがってPicardにs,F,E1..E5を取り、s²=-1,sF=1,F²=0,Ei²=-1、他の交叉は0。
D1=2s+2F−ΣEi、D2=E5、D3=F−E5。
**成分選択はcompatible markingから来る。** 四つの平方根の符号を初めから独立自由とみなさない。各単純根・line section・成分は有限エタール被覆上で選べる。

## 2. 全四周期と整数格子

境界直交補Kは bF+Σ_(i=1)^4 c_iEi、2b+Σc_i=0、すなわちeven-sum Z4。形式は−Σci²。
整数基底はalpha1=E1−E2、alpha2=E2−E3、alpha3=E3−E4、alpha4=E3+E4−F。Gramは負D4、det4。係数行列のdet2はeven-sum latticeの指数2と一致する。

D1の座標z=w/vで、選択Eiの交点をziとする。zi+zi^-1=2ui。一般fiberはD1と二点で交わり、そのz座標の積は1。
境界線束のgluingからP(bF+ΣciEi)=prod zi^ci、従って

p=(p1,p2,p3,p4)=(z1/z2,z2/z3,z3/z4,z3*z4)。

境界の向き・zの向きを一度そろえる。Friedman Prop3.12でこのPはexp(integral omega/(2pi i))に一致する。alpha_iの任意整数持上げgamma_iとdelta_inftyがH2(U,Z)基底となり、全内部周期は2pi i log p_i modulo (2pi i)²Z。
局所的なlog枝とcycle持上げは選択を要する。全パラメータ上の選択非依存なcycle基底、代数的de Rham接続行列、Hurwitz作用の行列を構成したわけではない。

## 3. period torusとroot hypertori

指数行列は
[1,-1,0,0]; [0,1,-1,0]; [0,0,1,-1]; [0,0,1,1]。
det2、Smithは1,1,1,2。したがって(C*)^4→Hom(D4,C*)は次数2 isogenyで、核は共通±1。
(A,B,C,h)からquartic係数(2A,2h−1,2BC−2A,B²+C²−2h)へのJacobianは16(C²−B²)。根の順序付けとziの選択がetaleな開条件と合わせ、p1..p4は有限標識被覆上の局所座標。

ui−uj=(zi−zj)(zi*zj−1)/(2zi*zj)から
Disc N=prod_(i<j)(zi−zj)²(zi*zj−1)²/[2^12(prod zi)^6]。
従って本chartのconic退化がD4のroot character zi/zj,zi*zjの値1に対応する。古典的な標識三次曲面のperiod torusの具体式であって、新しい一般Torelli定理ではない。
Weylによる標識変更と固定fiberのHurwitz自己同型、五重被覆のS5、G2成分交換S3は別作用として比較する。

## 4. 有理混合Hodge構造の分裂判定

本chartでは次は同値：
(1) 0→Q(-1)^4→H²(U,Q)→Q(-2)→0 が分裂。
(2) 全p_iがroots of unity。
(3) 全ziがroots of unity。

(1)⇔(2)はF²=[omega]を境界periodで正規化した線が有理であることと、整数基底上の全評価が有理であることを用いる。F¹は全空間であり、この有理線があればHodge filtrationを保つsectionを得る。(2)⇒(3)はz3²=p3p4から順に従う。
**有理分裂と整数拡大の自明性は別。** またroot-of-unity periodは元の量子化パラメータq³=1とも有限braid軌道とも別条件。

Q上の分裂例：
(A,B,C,h)=(1/4,1/2,1/4,1/8)、N=(2u+1)(8u³−6u+1)/16。
16 z^4 N((z+z^-1)/2)=(z^9−1)/(z−1)。
四uiはcos(2pi k/9),k1..4、全ziはどの逆数選択でも9乗根。Nはsquare-free、N(1)=9/16,N(-1)=1/16なのでsmooth。

Q上の非分裂例：
(A,B,C,h)=(-65/16,75/16,-65/16,3575/288)、
N=(u−5/4)(u−5/3)(u−17/8)(u−37/12)。
各ziは2,3,4,6またはその逆数で非捩れ。全根相異なり±1を避け、同じchartでsmooth。特定の符号組をcompatible markingと無断で同定せず、捩れ性が反転に不変なことを使う。

## 5. 一次文献・既知性

R. Friedman, *On the geometry of anticanonical pairs*, arXiv:1502.02560v2 (2016), §3 Proposition3.12、pp.21–23。原PDF https://arxiv.org/pdf/1502.02560 の該当頁を本文と画像で確認。積分periodとPic0(D)の制限の比較、およびMHSとの関係を既知入力として使う。本稿では境界period1の規約へomega/(2pi i)²で合わせる。
N. Schock, *The W(E6)-invariant birational geometry of the moduli space of marked cubic surfaces*, Math. Nachr.297 (2024),2639–2666、DOI https://doi.org/10.1002/mana.202300459 、§2。標識三次曲面のD4 period torusとroot hypertorusに関するNaruki–Looijengaの既知構造を参照する。今回出版社一次本文の検索索引で該当記述を確認したが、直接全文取得は403であり、同論文全体を今回再監査したとはしない。
Friedman–Carlsonの一般理論や古典period torusの新規性を主張しない。今回の座標・縮約・二例の文献上の既出性は網羅的には未確認。

## 6. 次の研究の入口

まず一つのHurwitz生成元が保存するconic pencilで、Eiの像、D4根基底の変換、p_iの変換を同時に求める。trialityではpencilが変わるのでF1標識間の遷移が必要。固定曲面の作用、基底の変換、底loopのmonodromyを分ける。
円分的分裂例はKummer型Hodge拡大と代数的torus座標の具体例になる。9乗根という事実だけで量子代数や有限表現に結び付けず、境界線束の位数と比較写像を先に求める。
全四periodが局所座標となったので、de Rham基底によるrank五Gauss–Maninの明示化、mirror torus側の座標との比較も着手できる。ただし現段階では未構成。

## 7. 検証と保存

`computations/verify_conic_period_coordinates.py` を実行しPASS。Q・整数格子・形式Laurent式だけを用いる。出力は `conic_period_coordinates_certificate.json`。幾何学的縮約、gluing、Friedman比較、MHS分裂は本文の通常の証明。
新節を一時LuaLaTeX wrapperで4頁に組版し、全頁画像・内部参照・overfullなしを確認した。主論文全体の今回の再組版、旧27検証器全再実行、独立査読、新規性の網羅調査は未実施。主論文への入力と既存証明の保持を差分で確認した。GitHub mainを正本とし、push済み内容をLibraryへ保存しない。
