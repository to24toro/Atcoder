from itertools import *
from collections import *
from heapq import *
import math
dic = defaultdict(list)
h,w = map(int,input().split())
A = [input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if A[i][j]=='S':
            sx,sy = i,j
        elif A[i][j]=='G':
            gx,gy = i,j
        elif A[i][j]=='.' or A[i][j] =='#':continue
        else:
            c = A[i][j]
            dic[c].append((i,j))
q  =deque([(sx,sy,0)])
dist = [[float('inf')]*w for _ in range(h)]
dist[sx][sy] = 0
seen = defaultdict(int)
while q:
    x,y,time = q.popleft()
    if dist[x][y]<time:continue
    for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
        X  =x+dx
        Y = y + dy
        if 0<=X<h and 0<=Y<w:
            c = A[X][Y]
            # print(c,'.',dist[X][Y]<time+1)
            if (c!='#') and dist[X][Y]>time+1:
                # print(dist[X][Y])
                dist[X][Y] = time+1
                q.append((X,Y,time+1))
            if seen[c]==0 and c not in [".",'#',"S","G"]:
                # print(dic[c])
                seen[c]=1
                for xx,yy in dic[c]:
                    if xx==X and yy==Y:continue
                    elif dist[xx][yy]>time+2:
                        dist[xx][yy]=time+2
                        q.append((xx,yy,time+2))

# print(dist)
print(dist[gx][gy] if dist[gx][gy]!=float('inf') else -1)
