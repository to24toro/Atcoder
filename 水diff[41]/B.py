h,w,t = map(int,input().split())
S =[input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if S[i][j]=='S':
            sx,sy = i,j
        if S[i][j]=='G':
            gx,gy = i,j
from collections import deque
def helper(c):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[float('inf')]*w for _ in range(h)]
    q = deque([(sx,sy)])
    seen[sx][sy]= 0
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            X = x+dx
            Y = y+dy
            if 0<=X<h and 0<=Y<w:
                cost = c if S[X][Y]=='#' else 1
                if seen[X][Y]>seen[x][y]+cost:
                    seen[X][Y]=seen[x][y]+cost
                    q.append((X,Y))
    return seen[gx][gy]>t

l,r = -1,10**9+1
while r-l>1:
    m = (r+l)//2
    if helper(m):
        r = m
    else:
        l = m
print(l)