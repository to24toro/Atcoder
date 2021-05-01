n,m = map(int,input().split())
dp = [[float('inf')]*n for _ in range(n)]

for _ in range(m):
    u,v,l = map(int,input().split())
    u-=1
    v-=1
    dp[u][v]=l
    dp[v][u]=l
for i in range(n):
    dp[i][i] = 0
for k in range(1,n):
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
ans = float('inf')
# print(dp)
for i in range(1,n):
    for j in range(i+1,n):
        if dp[0][i] != float('inf') and dp[j][0] != float('inf'):
            ans = min(ans,dp[0][i]+dp[j][0] + dp[i][j])
            # print(ans,i,j)
print(-1 if ans ==float('inf') else ans)