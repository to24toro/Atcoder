n = int(input())
import sys
sys.setrecursionlimit(1<<20)
dp = [-1]*n
cnt = [[] for _ in range(n)]
for i in range(1,n):
    a = int(input())
    a-=1
    cnt[a].append(i)

def helper(i):
    if dp[i]>0:
        return dp[i]
    L = cnt[i]
    A = []
    for l in L:
        A.append(helper(l))
    if not A:
        dp[i]=0
        return dp[i]
    A.sort(reverse=True)
    ans = 0
    for j in range(1,len(L)+1):
        ans = max(ans,A[j-1]+j)
    dp[i]=ans
    return dp[i]
ans = helper(0)
print(ans)

