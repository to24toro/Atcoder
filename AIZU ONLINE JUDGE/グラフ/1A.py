v,e,r = map(int,input().split())
g = [[] for _ in range(v)]
for _ in range(e):
    s,t,d = map(int,input().split())
    g[s].append((t,d))
from collections import deque
q = deque([(r,0)])
dist = [float('inf')]*v
dist[r] = 0
while q:
    u,d = q.popleft()
    for v,d_tmp in g[u]:
        if dist[v]>d+d_tmp:
            dist[v] = d+d_tmp
            q.append((v,d+d_tmp))
for d in dist:
    print(d if d != float('inf') else 'INF')
