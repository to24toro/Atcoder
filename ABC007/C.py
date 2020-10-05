r,c = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
sx-=1
sy-=1
gx-=1
gy-=1
L = [list(input()) for _ in range(r)]
seen = [[False]*c for _ in range(r)]
seen[sx][sy] = True
dist = [(1,0),(-1,0),(0,1),(0,-1)]
from collections import deque
q = deque([(sx,sy,0)])
while q:
    x,y,d = q.popleft()
    if x==gx and y ==gy:
        print(d);exit()
    for dx,dy in dist:
        X = x+dx
        Y = y + dy
        if 0<=X<r and 0<=Y<c and L[X][Y]=='.' and not seen[X][Y]:
            seen[X][Y] = True
            q.append((X,Y,d+1))
print(-1)