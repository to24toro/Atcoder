n = int(input())
A = list(map(int,input().split()))
dp = [[0,0,0] for _ in range(n+1)]
ans = 1
mod = 10**9+7
for i in range(n):
    for j in range(3):
        dp[i+1][j] = dp[i][j]
    for j in range(3):
        if A[i]==dp[i+1][j]:
            dp[i+1][j] += 1
            break
for i in range(n):
    ans *= dp[i].count(A[i])
    ans %= mod
print(ans)