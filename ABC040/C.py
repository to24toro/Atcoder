n = int(input())
A = list(map(int,input().split()))
dp = [float('inf')]*(n)

dp[0] = 0
dp[1] = abs(A[0]-A[1])
for i in range(2,n):
    dp[i] = min(abs(A[i]-A[i-2])+dp[i-2],abs(A[i]-A[i-1])+dp[i-1],dp[i])
print(dp[-1])
