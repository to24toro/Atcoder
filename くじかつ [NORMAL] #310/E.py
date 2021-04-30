H,W = map(int,input().split())
cx,cy = map(int,input().split())
cx-=1
cy-=1
dx,dy = map(int,input().split())
dx-=1
dy-=1
S = [input() for _ in range(H)]

DX = [-2,-1,0,1,2]
DY = [-2,-1,0,1,2]

from collections import deque

q = deque([(cx,cy,0)])

seen = [[float('inf')]*W for _ in range(H)]

while q:
    x,y,c = q.popleft()
    if seen[x][y]<c:
        continue
    seen[x][y]=c
    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
        X = x+i
        Y = y+j
        if 0<=X<H and 0<=Y<W and seen[X][Y]>c and S[X][Y]=='.':
            seen[X][Y] = c
            q.appendleft((X,Y,c))
    for i in DX:
        for j in DY:
            X = x+i
            Y = y+j
            if 0<=X<H and 0<=Y<W and seen[X][Y]>c+1 and S[X][Y]=='.':
                seen[X][Y] = c+1
                q.append((X,Y,c+1))
print(seen[dx][dy] if seen[dx][dy] != float('inf') else -1)