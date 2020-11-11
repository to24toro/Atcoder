n,m = map(int,input().split())
g = [[] for _ in range(n)]
for i in range(n-1,0,-1):
    g[i].append((i-1,0))
for _ in range(m):
    l,r,x = map(int,input().split())
    g[l-1].append((r-1,x))
import heapq
hq = []
heapq.heappush(hq,(0,0))
d = [float('inf')]*n
d[0] = 0
while hq:
    s,c = heapq.heappop(hq)
    for t,x in g[s]:
        if d[t]>x+c:
            d[t] = x+c
            heapq.heappush(hq,(t,x+c))
print(-1 if d[-1]==float('inf') else d[-1])