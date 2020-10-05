n,ma,mb = map(int,input().split())
l = []
sum_a = 0
sum_b = 0

for _ in range(n):
    a,b,c = map(int,input().split())
    sum_a += a
    sum_b += b
    l.append([a,b,c])

INF = float('inf')

dp = list( list([INF for i in range(450)] for i in range(450)) for i in range(45))
dp[0][0][0] = 0

for i in range(n):
    for j in range(sum_a+1):
        for k in range(sum_b+1):
            a,b,c = l[i]
            dp[i+1][j][k] = min(dp[i][j][k],dp[i+1][j][k],dp[i][j-a][k-b]+c)
ans = INF

k = 1
while ma*k<450 and mb*k<450:
    ans = min(ans,dp[n][ma*k][mb*k])
    k += 1
print(ans if ans!=INF else -1)