n,m,p = map(int,input().split())
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a-1,b-1,c-p))
d = [-float('inf')]*n
d[0] = 0
for i in range(n):
    for u,v,c in edges:
        if d[u] != -float('inf') and d[u]+c > d[v]:
            d[v] = d[u]+c
            if i ==n-1:
                d[v] = float('inf')

for i in range(n):
    for u,v,c in edges:
        if d[u] != -float('inf') and d[u]+c > d[v]:
            d[v] = d[u]+c
ans = d[-1]
if ans ==float('inf'):
    print(-1)
elif ans <=0:
    print(0)
else:
    print(ans)