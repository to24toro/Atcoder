def Bellmanford(n,edges,r):
    d = [float('inf')]*n
    d[r] = 0
    for i in range(n):
        for u,v,c in edges:
            if d[u] != float('inf') and d[u]+c < d[v]:
                d[v] = d[u]+c
                if i ==n-1 and v == n-1:
                    return 'inf'
    return -d[n-1]
n,m = map(int,input().split())
edges = [None]*m
for i in range(m):
    a,b,c = map(int,input().split())
    edges[i] = (a-1,b-1,-c)
ans = Bellmanford(n,edges,0)
print(ans)