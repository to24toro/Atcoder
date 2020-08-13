n=int(input())
A = list(map(int,input().split()))
from itertools import accumulate
S = [0] + list(accumulate(A))
dp = [[0]*(n+1) for _ in range(n+1)]
for d in range(2,n+1):
    for i in range(n-d+1):
        j = i+d
# for i in range(n+1):
#     for j in range(i+1,n+1):
        val = float('inf')
        for k in range(i+1,j):
            val = min(val,dp[i][k]+dp[k][j])
        dp[i][j] += S[j]-S[i] + val
print(dp[0][-1])