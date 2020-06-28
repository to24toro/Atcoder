N = int(input())
dp = [float('inf')]*(N+1)
dp[0] = 0
for i in range(1,N+1):
    dp[i] = 1 + dp[i-1]
    j,k = 1,1
    while pow(6,j)<=i:
        dp[i] = min(dp[i],1+dp[i-pow(6,j)])
        j += 1
    while pow(9,k)<=i:
        dp[i] = min(dp[i],1+dp[i-pow(9,k)])
        k += 1
print(dp[-1])
    