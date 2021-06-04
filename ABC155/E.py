n = input()
dp = [[0]*2 for _ in range(len(n)+1)]
n = n[::-1]
dp[0][1] = 1
l = len(n)
dp[0][0] = 0
for i in range(l):
    t = int(n[i])
    dp[i+1][0] = min(dp[i][0]+t,dp[i][1]+10-t)
    dp[i+1][1] = min(dp[i][0]+t+1,dp[i][1]+9-t)
print(dp[l][0])
