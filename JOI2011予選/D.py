n = int(input())
A  =list(map(int,input().split()))
dp = [[0]*(21) for _ in range(n)]
dp[0][A[0]] = 1
for i in range(1,n):
    for j in range(21):
        if j-A[i]>=0:
            dp[i][j] += dp[i-1][j-A[i]]
        if j+A[i]<=20:
            dp[i][j] += dp[i-1][j+A[i]]
print(dp[-1][0])