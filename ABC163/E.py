n = int(input())
a = list(map(int,input().split()))
a = [(num,i) for i,num in enumerate(a)]
a.sort(reverse=True)
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n-i+1):
        if i>0:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+a[i+j-1][0]*abs(a[i+j-1][1]-(i-1)))
        if j>0:
            dp[i][j] = max(dp[i][j],dp[i][j-1]+ a[i+j-1][0]*abs(a[i+j-1][1]-(n-j)))
ans = max(dp[i][n-i] for i in range(n+1))
print(ans)
