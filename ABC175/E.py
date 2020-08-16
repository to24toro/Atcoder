r,c,k = map(int,input().split())
dp = [[[0]*(c+1) for _ in range(r+1)] for _ in range(4)]
g = [[0]*(c+1) for _ in range(r+1)]
for _ in range(k):
    a,b,v = map(int,input().split())
    g[a][b] = v

for i in range(r+1):
    for j in range(c+1):
        for m in range(4):
            tmp  =dp[m][i][j]
            if i+1<=r:
                dp[0][i+1][j] = max(tmp,dp[0][i+1][j])
                dp[1][i+1][j] = max(dp[1][i+1][j],tmp + g[i+1][j])
            if j+1<=c:
                dp[m][i][j+1] = max(dp[m][i][j+1],tmp)
                if m<3:
                    dp[m+1][i][j+1] = max(dp[m+1][i][j+1],tmp + g[i][j+1]) 
ans = 0
for m in range(4):
    ans = max(ans,dp[m][-1][-1])
print(ans)
 