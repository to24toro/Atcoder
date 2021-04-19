n,k = map(int,input().split())
A = [int(input()) for _ in range(n)]
if sum(A)==k:print(1);exit()
if sum(A)==0:print(0);exit()
dp = [[float('inf')]*(n+1) for _ in range(n+1)]
dp[1][1]=1
dp[0][0]=0
dp[1][0]=0
s = A[0]
for i in range(1,n):
    a = A[i]
    for j in range(i+1):
        p = dp[i][j]*a
        p = p//s + 1
        if p<=a:
            dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j]+p)
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
    s+=a
for i in range(n,-1,-1):
    if dp[-1][i]<=k:
        print(i)
        exit()
print(0)