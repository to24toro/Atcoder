n = int(input())
dp = [[-1]*n for _ in range(1<<n)]

# def rec(s,v):
#     if dp[s][v]>=0:
#         return dp[s][v]
#     if (s==(1<<n)-1 and v==0):
#         dp[s][v]=0
#         return dp[s][v]
#     res = float('inf')
#     for u in range(n):
#         if not ((s>>u)&1):
#             res = min(res,rec(s|1<<u,u)+d[v][u])
#     dp[s][v]=res
#     return res
dp = [[INF] * K for i in range(1 << K)]
for i in range(K):
    dp[1 << i][i] = 1
 
for bit in range(1 << K):
    for i in range(K):
        if dp[bit][i] == INF:
            continue
        for j in range(K):
            if bit & 1 << j:
                continue
            if dp[bit ^ 1 << j][j] > dp[bit][i] + cost[i][j]:
                dp[bit ^ 1 << j][j] = dp[bit][i] + cost[i][j]