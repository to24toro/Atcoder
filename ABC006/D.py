n = int(input())
import bisect
def LIS(L):
    dp = [L[0]]
    for i in range(len(L)):
        if(L[i] > dp[-1]):
            dp.append(L[i])
        else:
            dp[bisect.bisect_left(dp,L[i])] = L[i]
    return dp
L = [int(input()) for _ in range(n)]
l = len(LIS(L))
print(n-l)