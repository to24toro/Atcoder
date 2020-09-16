n,m = map(int,input().split())
g = []
dp = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    dp[i][i]=0
for _ in range(m):
    a,b,c = map(int,input().split())
    g.append((a-1,b-1,c))
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
# print(dp)
cnt = 0

for a,b,c in g:
    f = True
    for i in range(n):
        if dp[i][a]+c==dp[i][b]:
            f = False
            break
    if f:
        cnt += 1
print(cnt)
import heapq
def dijkstra(s):
    dist =[float('inf')]*n
    dist[s] = 0
    seen = [False]*n
    p = []
    heapq.heappush(p,(dist[s],s))
    while p:
        d,u = heapq.heappop(p)
        if dist[u]<d:
            continue
        seen[u] = True
        for x,y in g[u]:
            if c[x] ==False and dist[u] + y <dist[x]:
                dist[x] = dist[u] + y
                heapq.heappush(p,(dist[x],x))
    return dist