H,W,K=map(int,input().split())
G=[[0]*(W+1) for _ in range(H+1)]
dp=[[[0]*(W+1) for _ in range(H+1)] for _ in range(4)]
for i in range(K):
  h,w,v=map(int,input().split())
  G[h][w]=v

for i in range(1,H+1):
  for j in range(1,W+1):
    dp[0][i][j]=max(dp[0][i-1][j],dp[0][i][j-1],dp[1][i-1][j],dp[2][i-1][j],dp[3][i-1][j])
    dp[1][i][j]=max(dp[0][i][j]+G[i][j],dp[1][i][j-1])
    dp[2][i][j]=max(dp[1][i][j-1]+G[i][j],dp[2][i][j-1])
    dp[3][i][j]=max(dp[2][i][j-1]+G[i][j],dp[3][i
    ][j-1])

print(max(dp[0][H][W],dp[1][H][W],dp[2][H][W],dp[3][H][W]))