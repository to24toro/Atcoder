def Bellman_ford(s,n,g):
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