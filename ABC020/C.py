h,w,t = map(int,input().split())
L = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if L[i][j] =='S':
            sx,sy = i,j
        if L[i][j] =='G':
            gx,gy = i,j
from collections import deque

def chk(time):
    dist =[[float('inf')]*w for _ in range(h)]
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    dist[sx][sy] = 0
    q = deque([(sx,sy,0)])
    while q:
        x,y,cost = q.popleft()
        for dx,dy in d:
            X = x + dx
            Y = y + dy
            if 0<=X<h and 0<=Y<w and cost <t:
                if L[X][Y] =='.' and dist[X][Y]>cost +1:
                    dist[X][Y] = cost+1
                    q.append((X,Y,cost+1))
                elif L[X][Y] =='#' and dist[X][Y]>cost +time:
                    dist[X][Y] = cost+time
                    q.append((X,Y,cost+time))
                elif L[X][Y] =='G' and dist[X][Y]>cost +1:
                    dist[X][Y] = cost+1
                    q.append((X,Y,cost+1))
    return dist[gx][gy]

l,r = 0,t
while r-l>1:
    mid = (l+r)//2
    time = chk(mid)
    if time >t:
        r = mid
    else:
        l = mid
print(l)