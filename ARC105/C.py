from bisect import bisect_left

from itertools import permutations,accumulate

n,m = map(int,input().split())
w = list(map(int,input().split()))
P = [tuple(map(int,input().split())) for _ in range(m)]
P.sort(key = lambda x:x[1])
L = [p[0] for p in P]
V = [p[1] for p in P]

for i in range(1,m):
    L[i] = max(L[i],L[i-1])
if max(w)>min(V):
    print(-1);exit()

ans = float('inf')
for W in permutations((w)):
    S = list(accumulate(W))
    dp = [0]*n
    for i in range(n):
        for j in range(n):
            diff = S[i]-(S[j-1] if j>0 else 0)
            idx = bisect_left(V, diff)
            length = L[idx-1] if idx>0 else 0
            dp[i] = max(dp[i],dp[j]+length)
    ans = min(ans,dp[i])
print(ans)
