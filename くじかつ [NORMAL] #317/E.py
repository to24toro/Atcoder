L = input()
n = len(L)
mod = 10**9+7
dp = [[0,0] for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(2):
        if L[i]=='1':
            if j==0:
                dp[i+1][0]=2*dp[i][0]
                dp[i+1][0]%=mod
                dp[i+1][1]=dp[i][0]
                dp[i+1][1]%=mod
            else:
                dp[i+1][1]+=3*dp[i][1]
                dp[i+1][1]%=mod
        else:
            if j==0:
                dp[i+1][0]=dp[i][0]
                dp[i+1][0]%=mod
            else:
                dp[i+1][1]+=3*dp[i][1]
                dp[i+1][1]%=mod

print(sum(dp[-1])%mod)