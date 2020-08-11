import heapq
n,w,k= map(int,input().split())
edge = [[] for i in range(n)]
for i in range(w):
    x,y,z = map(int,input().split())
    edge[x-1].append([z,y-1])
    edge[y-1].append([z,x-1])
seen = [False]*n
edges = []
edgeweight = []
for e in edge[0]:
    heapq.heappush(edges,e)
seen[0] = True
res = 0
while len(edges)!=0:
    minedge = heapq.heappop(edges)
    if seen[minedge[1]]:
        continue
    v = minedge[1]
    seen[v] = True
    for e in edge[v]:
        if not seen[e[1]]:
            heapq.heappush(edges,e)
    res += minedge[0]
    edgeweight.append(minedge[0])
edgeweight.sort()

while k > 1:
    res -= edgeweight.pop()
    k -= 1
print(res)
