n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dp = [[float('inf')]*(m+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n+1):
    for j in range(m+1):
        if i<n and j<m:
            dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j]+(1 if A[i]!=B[j] else 0))
        if i<n:
            dp[i+1][j]=min(dp[i+1][j],dp[i][j]+1)
        if j<m:
            dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
print(dp[-1][-1])