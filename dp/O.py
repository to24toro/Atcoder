n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(1<<n)
dp[0] = 1
mod = 10**9+7
for i in range(1,1<<n):
    cnt = 0
    for j in range(n+1): cnt += (i>>j)&1
    for j in range(n):
        if (i>>j)&1==0: continue
        dp[i] +=dp[i-(1<<j)]*A[cnt-1][j]
        dp[i] %=mod
print(dp[-1]%mod)