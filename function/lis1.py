#計算量O(n^2)

def LIS(L):
    dp = [1]*N
    res = 0
    for i in range(N):
        for j in range(i):
            if(L[i]>L[j]):
                dp[i] = max(dp[j]+1,dp[i])
        res = max(res,dp[i])
    return res