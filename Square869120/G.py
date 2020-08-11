n,m = map(int,input().split())
dist = [[] for _ in range(n)]
for _ in range(m):
    s,t,d,time = map(int,input().split())
    dist[s-1].append((t-1,d,time))
    dist[t-1].append((s-1,d,time))

dp = [[[float('inf'),0] for _ in range(n)] for _ in range(1<<n)] #dp[S][j]:集合Sで終着点jの時の[最小距離,場合の数]のペア
dp[0][0] = [0,1]

for t,d,time in dist[0]:
    if d <=time: #時間内
        if dp[1<<t][t][0]>d:
            dp[1<<t][t] = [d,1]
        elif dp[1<<t][t][0]==d:
            dp[1<<t][t][1] += 1

for bit in range(2,1<<n,2):
    for i in range(n):
        if ((bit>>i)&1):
            for t,d,time in dist[i]:
                if not ((bit>>i)&1) and dp[bit][i][0] + d <=time:
                    next_bit = bit|(1<<t)
                    if dp[bit][i][0] + d < dp[next_bit][t][0]:
                        dp[next_bit][t] = [dp[bit][i][0] + d,dp[bit][i][1]]
                    elif dp[bit][i][0] + d == dp[next_bit][t][0]:
                        dp[next_bit][t][1] += dp[bit][i][1]
ans = dp[-1][0]
print(' '.join(map(str,ans)) if ans[1]>0 else 'IMPOSSIBLE')



