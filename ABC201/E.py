n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u,v,w = map(int,input().split())
    u-=1
    v-=1
    g[u].append((w,v))
    g[v].append((w,u))

def dijkstra(start,graph,n):
    import heapq

    dist = [float('inf')]*n

    hq = []

    heapq.heappush(hq,(0,start))
    dist[start]=0
    while hq:
        d,x = heapq.heappop(hq)
        if dist[x]<d:
            continue
        for y,d2 in graph[x]:
            if dist[y]>d+d2:
                dist[y]=d+d2
                heapq.heappush(hq,(d+d2,y))
    return dist
from collections import deque
q = deque([(0,0)])
seen = [-1]*n
seen[0]=0
while q:
    x,cnt  = q.popleft()
    for c2,y in g[x]:
        if seen[y]<0:
            seen[y] = c2^cnt
            q.append((y,c2^cnt))
ans = 0
mod = 10**9+7
# print(seen)
for i in range(60):
    cnt = 0
    for j in range(n):
        if seen[j]&(1<<i):
            # print(n,seen[j],seen[j]>>i)
            cnt += 1
    ans += pow(2,i)*cnt*(n-cnt)
    # print(ans,cnt,n-cnt)
    ans %=mod
print(ans)
