n,w = map(int,input().split())
dp = [[0]*(w+1) for _ in range(n+1)]
V = []
W = []
for _ in range(n):
    a,b = map(int,input().split())
    V.append(a)
    W.append(b)
dp[0][0] = 0
for i in range(n):
    for j in range(w+1):
        if j-W[i]>=0:
            dp[i+1][j] = max(dp[i][j],dp[i][j-W[i]] + V[i])
        else:
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
# print(dp)
print(dp[-1][-1])