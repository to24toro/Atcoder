n,m = map(int,input().split())
dp = [0]*(n+1)
mod = 10**9+7
dp[0]=1
for _ in range(m):
    a = int(input())
    dp[a]=-1
for i in range(n+1):
    if dp[i]==-1:
        continue
    if i+1<n+1 and dp[i+1]!=-1:
        dp[i+1]+=dp[i]
    if i+2<n+1 and dp[i+2]!=-1:
        dp[i+2]+=dp[i]

print(dp[-1]%mod)