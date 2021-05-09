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