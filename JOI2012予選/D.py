mod = 10000
n,k = map(int,input().split())
dic = {}
for _ in range(k):
    a,b = map(int,input().split())
    dic[a-1] = b-1

dp = [[[0,0],[0,0],[0,0]] for _ in range(n)]

if 0 in dic:
    dp[0][dic[a]][0] = 1
else:
    dp[0][0][0] = 1
    dp[0][1][0] = 1
    dp[0][2][0] = 1

for i in range(1,n):
    for j in range(3):
        if i not in dic:
            dp[i][j][0] += dp[i-1][(j+1)%3][0] + dp[i-1][(j+1)%3][1] + dp[i-1][(j+2)%3][0] + dp[i-1][(j+2)%3][1] 
            dp[i][j][1] += dp[i-1][j][0]
    if i in dic:
        dp[i][dic[i]][0] += dp[i-1][(dic[i]+1)%3][0] + dp[i-1][(dic[i]+1)%3][1] + dp[i-1][(dic[i]+2)%3][0] + dp[i-1][(dic[i]+2)%3][1]
        dp[i][dic[i]][1] += dp[i-1][dic[i]][0]
ans = 0
for j in range(3):
    for m in range(2):
        ans += dp[-1][j][m]
print(ans%mod)