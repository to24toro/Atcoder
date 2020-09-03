n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
seen = [False]*(n)
tmp = [-1]*n
from collections import deque
for i in range(n):
    q = deque([])
    if not seen[i]:
        q.append((i,i))
        tmp[i] = i
        while q:
            u,cnt = q.popleft()
            seen[u] = True
            tmp[u] = cnt
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    tmp[i] = cnt
                    q.append((v,cnt))

from collections import Counter
counter = Counter(tmp)

ans = sorted(counter.values())
print(ans[-1])
