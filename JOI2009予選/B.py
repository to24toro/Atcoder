d = int(input())
n = int(input())
m = int(input())
N = [0]
M = []
ans = 0
for _ in range(n-1):
    N.append(int(input()))
for _ in range(m):
    M.append(int(input()))
N.sort()
from bisect import bisect_left
for m in M:
    idx = bisect_left(N,m)
    if idx == n:
        ans += min(abs(d-m),abs(N[idx-1]-m))
    else:
        ans += min(abs(N[idx]-m),abs(N[idx-1]-m))
print(ans)