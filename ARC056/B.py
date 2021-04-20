n,m,s = map(int,input().split())
s-=1
g = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)
import heapq
hq = []
hq = [(-float('inf'),s)]
heapq.heapify(hq)
seen = [0]*n
vis = set()
while hq:
    c,p = heapq.heappop(hq)
    if p in vis:continue
    seen[p]=-c
    vis.add(p)
    for q in g[p]:
        if q not in vis:
            heapq.heappush(hq,(max(c,-p),q))
for i in range(n):
    if i<seen[i]:
        print(i+1)