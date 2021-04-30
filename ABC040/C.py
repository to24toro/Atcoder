n = int(input())
dp = [float('inf')]*n
A = list(map(int,input().split()))
dp[0]=0
dp[1] = abs(A[1]-A[0])
for i in range(2,n):
    dp[i] = min(dp[i-2]+abs(A[i]-A[i-2]),dp[i-1]+abs(A[i]-A[i-1]))
print(dp[-1])