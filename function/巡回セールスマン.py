n = int(input())
dp = [[-1]*n for _ in range(1<<n)]

def rec(s,v):
    if dp[s][v]>=0:
        return dp[s][v]
    if (s==(1<<n)-1 and v==0):
        dp[s][v]=0
        return dp[s][v]
    res = float('inf')
    for i in range(n):
        if !((s>>i)&1):
            res = min(res,rec(s|1<<u,u)+d[v][u])
    dp[s][v]=res
    return res
