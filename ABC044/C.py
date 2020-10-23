n,a = map(int,input().split())
X = [0]+list(map(int,input().split()))
dp = [[[0]*(max(X)*n+1) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1
for i in range(1,n+1):
    for j in range(n+1):
        for k in range(max(X)*n+1):
            if k<X[i]:
                dp[i][j][k] = dp[i-1][j][k]
            elif 1<=k and X[i]<=k:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k-X[i]]

ans = 0
for i in range(1,n+1):
    if i*a<=n*max(X):
        ans += dp[n][i][i*a]
print(ans)