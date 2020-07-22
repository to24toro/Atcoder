h,w = map(int,input().split())
A = [list(input()) for _ in range(h)]
dp = [[0]*(w) for _ in range(h)]
dp[0][0] = 1
mod = 10**9+7
for i in range(h):
    if A[i][0]=='.':
        dp[i][0] = 1
    else:
        break
for i in range(w):
    if A[0][i]=='.':
        dp[0][i] =1
    else:
        break
for i in range(1,h):
    for j in range(1,w):
        if A[i][j]=='.':
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
            dp[i][j] %= mod
print(dp[-1][-1])