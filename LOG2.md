8/10
ABC155-D k番目->xがkこ未満を満たすxの最大値

8/13
dp-N 一度まとめたスライムを分割していくことを考える。dp[l][r]: 区間[l,r]におけるスライム分割の最小コスト。
dp-O bitdp,dp[i]:部分集合Sにおける場合の数。遷移はdp[i-(1<<j)]->dp[i]を考える。jは集合iのbitが立っているところ部分。i-(1<<j)はそのうち一つのbitを0にした時。
dp-P 木dpというらしい。dp[i][j]を頂点iをjに塗った時のiを親とする部分木の場合の数
JOI 2008 本選 3 - ダーツ 二分探索 あらかじめダーツ日本使った時の点数をメモするのがポイント
ARC54-B 微分を実装して二分探索*

8/14
ABC153-A math.ceil
ABC153-B sum
ABC153-C sort
ABC153-D 2の階乗
ABC153-E dp[i]: i体力減らすのに必要な最小コスト
ABC153-F x-d,x+d,をx,x+2dに変換,sort,累積和

8/15
ABC175-A なし
ABC175-B なし
ABC175-C 偶奇
ABC175-D 場合分け、グラフ、一つ気づかず
ABC175-E dpで場合分けするだけ、先に解いとくべきだった 

8/16
ABC174-A なし
ABC174-B なし
ABC174-C なし
ABC174-D 10**5なので全数字に対してメモすれば良い
ABC174-E 最小公倍数
AOJ 1160 - 島はいくつある？ dfs
JOI 2009 予選 4 - 薄氷渡り dfs

8/17
ABC138-A なし
ABC138-B なし
ABC138-C sort
ABC138-D dfs, recursiveだとover
ABC138-E sのi文字目から次のアルファベットまでの距離をメモしておく
ALDS_10_C - 最長共通部分列
ALDS_10_A - フィボナッチ数
DPL_1_A - コイン問題
DPL_1_B - 0,1ナップザック問題
DPL_1_C - ナップザック問題

8/18
ABC150-A なし
ABC150-B count
ABC150-C permutation
ABC150-D Xとa/2の2で割り切れる回数は一致する必要がある。これに気づけなかった。
ABC150-E Cをソートする。Cがi場面に選ばれ時を考えて足し合わせる

8/19
ABC145-A なし
ABC145-B なし
ABC145-C permutation
ABC145-D mod3で考えるあとはパスカル三角形
ABC145-E Aでsortして1-j番目まで考えて美味しいもののコスト.選ぶ中で最大のAを最後に選べば良い。Bでそーとしてた

8/20
ABC144-A なし
ABC144-B 全探索
ABC144-C 約数
ABC144-D 数学
ABC144-E 二部探索

8/21
ABC151-A なし
ABC151-B なし
ABC151-C なし
ABC151-D bfs
ABC151-E maxとminを独立に考える
Dまでノーミスでとけば1300くらい、早くとかないと1200いかない、早いかつ1ミス以内

8/26
ABC147-A なし
ABC147-B なし
ABC147-C 全探索
ABC147-D 各位の01のカウント
ABC147-E dp:(i,j)で偏りkになるか否か

8/27
ABC146-A なし
ABC146-B なし
ABC146-C 二分探索
ABC146-D bfs*
ABC146-E 累積和、数え方

8/28
ABC143-A なし
ABC143-B なし
ABC146-C deque
ABC146-D 二分探索
ABC146-E ワーシャルフロイド、L以下を1と置き直す*

9/2
ABC134-A なし
ABC134-B なし
ABC134-C 上二つを押さえておけば良い
ABC134-D 大きい方から埋めていく
ABC134-E LISと同義*

9/3
ABC133-A なし
ABC133-B ユークリッド距離
ABC133-C たかだか2019のループ
ABC133-D 連立方程式
ABC133-E dfs直接繋がっている色は変える,距離1と2を考えるだけで良い
2000相当

9/4
ABC133-A なし
ABC133-B なし
ABC133-C sort
ABC133-D コンビネーション
ABC133-E 各頂点余りが0,1,2を考えてbfsとかでできる、解けるべき*
1500相当

9/13
ABC178-A なし
ABC178-B なし
ABC178-C 余事象
ABC178-D 数学
ABC178-E マンハッタン

9/16
ABC50-A replace
ABC50-B 全探索
ABC50-C 一つ見つける
ABC50-D dijkstra or ワーシャルフロイド
ABC51-A なし
ABC51-B なし
ABC51-C sort&count
ABC51-D 桁dp わからん* https://betrue12.hateblo.jp/entry/2019/02/07/002335

9/20
ABC002-A なし
ABC002-B なし
ABC002-A sort
ABC002-A 包除原理* XYを選ぶ方法のところは簡単。端を使わない本数を包除原理を使って求める。奇数は足して偶数は引く。

9/21
ABC015-A なし
ABC015-B なし
ABC015-C bfs
ABC015-D 線分を横切れば良い、　ハマった
ABC016-A なし
ABC016-B なし
ABC016-C itertools product
ABC016-D dp できなさすぎ*

9/24
dp4問
ABC047-D 発想問題*

10/2
ARC080 セグメント木*

10/4
ABC054 D グラムの最大値を求めて三次元dp,*

10/5
ABC046 C その都度最小になるようにする*

10/6
ABC104 C 
