#シンプルにパスカルの三角形i段目左からj番目をもとめるdp
n =10
dp = [[0]*n for _ in range(n)]
for i in range(n):
    if i==0:
        dp[i][0] = dp[i][i]=1
    else:
        dp[i][0]=dp[i][i]=dp[i-1][0]
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
print(dp)