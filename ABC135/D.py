s = list(input())
dp = [[0]*13 for _ in range(100005)]
n = len(s)
res = 0
mod = 10**9+7
dp[0][0] = 1
for i in range(n):
    c = int(s[i]) if s[i] !='?' else -1
    for j in range(10):
        if c!=-1 and c!=j: continue
        for k in range(13):
            dp[i+1][(k*10+j)%13] += dp[i][k]
    for j in range(13):
        dp[i+1][j] %= mod

print(dp[n][5])