n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
from collections import deque
ans = []
for i in range(n):
    q = deque([(i,0)])
    seen = [False]*n
    res = 0
    seen[i] = True
    while q:
        u,cnt = q.popleft()
        if cnt ==2:
            res += 1
        else:
            for v in g[u]:
                if seen[v]==False:
                    seen[v]=True
                    q.append((v,cnt+1))
    ans.append(res)
for a in ans:
    print(a)
