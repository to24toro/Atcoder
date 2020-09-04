n,k = map(int,input().split())
mod = 10**9+7
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
from collections import deque
stack = deque([(0,k)])
seen = [True]*n
seen[0] = False

ans = 1

while stack:
    u,t = stack.popleft()
    ans = (ans*t)%mod
    if u==0: l = k-1
    else: l = k-2
    for v in g[u]:
        if seen[v]:
            seen[v] =False
            stack.append((v,l))
            l -=1
print(ans)