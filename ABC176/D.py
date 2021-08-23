from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
#23:39-23:52
sys.setrecursionlimit(1<<20)
INF = float('inf')
h,w = map(int,input().split())
sx,sy = map(int,input().split())
sx-=1
sy-=1

gx,gy = map(int,input().split())
gx-=1
gy-=1
S = [input() for _ in range(h)]
d = [[INF]*w for _ in range(h)]
q = deque([(0,sx,sy)])
while q:
    cnt,x,y = q.popleft()
    if d[x][y]<cnt:continue
    for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
        X = x+dx
        Y = y+dy
        if 0<=X < h and 0<=Y<w and S[X][Y]=='.' and d[X][Y]>cnt:
            d[X][Y] = cnt
            q.appendleft((cnt,X,Y))
    for dx in range(-2,3):
        for dy in range(-2,3):
            X = x+dx
            Y = y+dy
            if 0<=X < h and 0<=Y<w and S[X][Y]=='.' and d[X][Y]>cnt+1:
                d[X][Y] = cnt+1
                q.append((cnt+1,X,Y))
print(d[gx][gy] if d[gx][gy]!=INF else -1)