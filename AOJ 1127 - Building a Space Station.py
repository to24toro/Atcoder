import math
import heapq
while True:
    n = int(input())
    if n==0: break
    if n==1: print(0);exit()
    edges = [[] for _ in range(n)]
    coordinates = []
    for _ in range(n):
        x,y,z,r = map(float,input().split())
        coordinates.append((x,y,z,r))
    for i in range(n):
        for j in range(i+1,n):
            dist = math.sqrt((coordinates[i][0]-coordinates[j][0])**2 + (coordinates[i][1]-coordinates[j][1])**2+(coordinates[i][2]-coordinates[j][2])**2)
            if coordinates[i][3] + coordinates[j][3]>=dist:
                dist = 0
            else:
                dist -=coordinates[i][3] + coordinates[j][3]
            edges[i].append((dist,j))
            edges[j].append((dist,i))
    seen = [False]*n
    hq = []
    res = 0
    for e in edges[0]:
        heapq.heappush(hq,e)
    seen[0] = True
    while len(hq):
        minedge = heapq.heappop(hq)
        if seen[minedge[1]]:
            continue
        seen[minedge[1]] = True
        v = minedge[1]
        for e in edges[v]:
            heapq.heappush(hq,e)
        res += minedge[0]
    print(f"{res:.3f}")

