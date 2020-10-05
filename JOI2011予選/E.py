h,w,n = map(int,input().split())
L = [list(input()) for _ in range(h)]
cur = 1
seen = [[False]*w for _ in range(h)]
from copy import deepcopy
from collections import defaultdict,deque
q = deque([])
for i in range(h):
    for j in range(w):
        if L[i][j]=='S':
            x = i
            y = j
dist = [(1,0),(-1,0),(0,1),(0,-1)]
q.append((x,y,1,0))
seen2 = deepcopy(seen)
seen2[x][y] = True
while q:
    x,y,a,cur = q.popleft()
    if L[x][y]==str(a):
        if a==n:
            print(cur);exit()
        a += 1
        seen2= deepcopy(seen)
        seen2[x][y] = True
        q = deque([])
        q.append((x,y,a,cur))
    else:
        for dx,dy in dist:
            X = x+dx
            Y = y + dy
            if 0<=X<h and 0<=Y<w and not seen2[X][Y] and L[X][Y] != 'X':
                seen2[X][Y] = True
                q.append((X,Y,a,cur+1))
print(-1)
