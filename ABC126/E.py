n,m = map(int,input().split())
p = []
g = [[] for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    p.append((x,y,z))
    g[x-1].append(y-1)
    g[y-1].append(x-1)

seen = [False]*n

from collections import deque
cnt = 0
for i in range(n):
    if not seen[i]:
        seen[i] = True
        q = deque([i])
        cnt += 1
        while q:
            u = q.popleft()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)
                
print(cnt)