V,E = map(int,input().split())
dist = [[] for _ in range(V)]
for _ in range(E):
    s,t,d = map(int,input().split())
    dist[s].append((t,d))
dp = [[float('inf')]*V for _ in range(1<<V)] #dp[S][i]:bitが立っているもの集合Sを巡回する経路のうちiが執着のもの

for t,d in dist[0]:#0から出発するとしてその初期化
    dp[1<<t][t] = d#0からtへの経路の代入

for bit in range(1<<V):
    for i in range(E):
        if bit&(1<<i):#bitのある桁が1のとき
            for j,d in dist[i]:
                if not bit&(1<<j):#各頂点を1度だけ通る条件
                  next_bit = bit|(1<<j)
                  dp[next_bit][j] = min(dp[bit][i] + d, dp[next_bit][j])
ans = dp[(1<<V)-1][0]
print(ans if ans!=float('inf') else -1)