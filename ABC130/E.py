n,m = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
mod = 10**9+7
dp = [1]*(m+1)#Tをiまで見た時のSとの部分列のも場合の数
for i in range(n):
    tmp = dp[:]
    for j in range(m):
        if S[i]==T[j]:
            dp[j+1] = (tmp[j+1] + dp[j])%mod
        else:
            dp[j+1] =(tmp[j+1]+dp[j]-tmp[j])%mod
print(dp[-1])
