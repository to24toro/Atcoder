n,p = map(int,input().split())
dp = [[0]*(p+1) for _ in range(n)]
W,V = [],[]
for _ in range(n):
    w,v = map(int,input().split())
    W.append(w)
    V.append(v)
for i in range(n):
    for j in range(p+1):
        if j -W[i]>=0:
            dp[i][j] = max(dp[i][j], dp[i-1][j],dp[i-1][j-W[i]] + V[i])
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
print(max(dp[-1]))
