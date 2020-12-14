n,m = map(int,input().split())
g = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j] =='s':
            sx,sy = i,j
        if g[i][j] =='g':
            gx,gy = i,j
import heapq as hq
q = []
hq.heappush(q,(-10,1,sx,sy))
seen = [[-float('inf')]*m for _ in range(n)]
seen[gx][gy] =10
d = [(0,1),(0,-1),(1,0),(-1,0)]
P = [1]

while q:
    light,t,x,y = hq.heappop(q)
    light *= -1
    if light<seen[x][y]:
        continue
    for dx,dy in d:
        X = x+dx
        Y = y+dy
        if 0<=X<n and 0<=Y<m:
            if g[X][Y] =='g' or g[X][Y]=='#':
                continue
            if g[X][Y] =='s':
                print(light*0.99);exit()
            # # print(light,g[X][Y],x,y)
            # if seen[X][Y]<nl:
            #     seen[X][Y]=nl
            nl = min(light*0.99,float(g[X][Y]))
            if seen[X][Y]<nl:
                hq.heappush(q,(-nl,t+1,X,Y))
                seen[X][Y] = nl
# print(seen)
