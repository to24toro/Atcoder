n = int(input())
P = list(map(float,input().split()))
dp = [[0]*(n+1) for _ in range(n)]
dp[0][0] = 1-P[0]
dp[0][1] = P[0]
for i in range(1,n):
    for j in range(i+2):
        if j ==0:
            dp[i][j]= dp[i-1][j]*(1-P[i])
        else:
            dp[i][j] = P[i]*dp[i-1][j-1] + (1-P[i])*dp[i-1][j]

print(sum(dp[-1][(n+1)//2:]))