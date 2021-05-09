n,m,t = map(int,input().split())
A = list(map(int,input().split()))
g = [[] for _ in range(n)]
h = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    h[b].append((a,c))


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

go = dijkstra(0, g, n)
come = dijkstra(0, h, n)

ans = 0
for i in range(n):
    move_cost =go[i]+come[i]
    if move_cost<t:
        ans = max(ans,(t-move_cost)*A[i])
print(ans)
