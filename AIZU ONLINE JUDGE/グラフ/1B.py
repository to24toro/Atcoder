def Bellman_ford(s,n):
    dist = [float('inf')]*n
    dist[s] = 0
    for i in range(n):
        update = False
        for x,y,z in g:
            if dist[y]>dist[x]+z:
                dist[y] = dist[x]+z
                update = True
        if not update:
            break
        if i ==n-1:
            return -1
    return dist

v,e,r = map(int,input().split())
g = []
for _ in range(e):
    s,t,d = map(int,input().split())
    g.append((s,t,d))
dist = Bellman_ford(r,v)
if dist==-1:
    print('NEGATIVE CYCLE')
    exit()
for d in dist:
    print(d if d != float('inf') else 'INF')