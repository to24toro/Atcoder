n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))
Q,k = map(int,input().split())
k-=1

seen = [False]*(n)
dist = [float('inf')]*n
dist[k] = 0

from collections import deque
q = deque([k])
while q:
    u = q.popleft()
    seen[u] = True
    for v,cost in g[u]:
        if not seen[v]:
            q.append(v)
            dist[v] = dist[u]+cost
for _ in range(Q):
    x,y = map(int,input().split())
    print(dist[x-1]+dist[y-1])