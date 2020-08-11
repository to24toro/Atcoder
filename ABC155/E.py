N = input()
dp = [[0] * 2 for _ in range(len(N) + 1)]
dp[0][1] = 1

for i in range(len(N)):
    n = int(N[i])
    dp[i + 1][0] = min(dp[i][0] + n, dp[i][1] + 10 - n)
    dp[i + 1][1] = min(dp[i][0] + n + 1, dp[i][1] + 10 - (n + 1))

print(dp[-1][0])
