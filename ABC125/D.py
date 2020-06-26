N = int(input())
A = list(map(int,input().split()))
dp = [[0,0] for _ in range(N+1)]
dp[0][1] = -float('inf')
for i in range(1,N+1):
    dp[i][0] = max(dp[i-1][0]+A[i-1],dp[i-1][1]-A[i-1])
    dp[i][1] = max(dp[i-1][0]-A[i-1],dp[i-1][1]+A[i-1])
print(dp[-1][0])

