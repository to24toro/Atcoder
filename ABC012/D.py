n,m =map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,t))
    g[b].append((a,t))
A = []
from collections import deque
def bfs(i):
    q = deque([(i,0)])
    dist = [float('inf')]*n
    dist[i] = 0
    while q:
        u,t = q.popleft()
        for v,time in g[u]:
            if dist[v]>t+time:
                dist[v] = t+time
                q.append((v,t+time))
    return dist
for i in range(n):
    A.append(bfs(i))
ans = float('inf')
for a in A:
    ans = min(ans,max(a))
print(ans)

