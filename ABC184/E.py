from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
h,w = map(int,input().split())
s = [[INF]*w for _ in range(h)]
A = [input() for _ in range(h)]
d = defaultdict(list)
for i in range(h):
    for j in range(w):
        if A[i][j]=="S":
            sx,sy = i,j
        elif A[i][j]=="G":
            gx,gy = i,j
        elif A[i][j] !='.' and A[i][j] !="#":
            d[A[i][j]].append((i,j))

q = [(0,sx,sy)]
seen = defaultdict(int)
heapify(q)

while q:
    cnt,x,y = heappop(q)
    if s[x][y]<cnt:
        continue
    s[x][y] = cnt
    for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
        X = x + dx
        Y = y + dy
        if 0<=X<h and 0<=Y<w:
            a = A[X][Y]
            if a!="#" and s[X][Y]>cnt+1:
                s[X][Y] = cnt+1
                heappush(q,(cnt+1,X,Y))
            if seen[a] ==0 and a!="." and a !="S" and a != "G":
                seen[a]=1
                for xx,yy in d[a]:
                    if xx==X and yy==Y:continue
                    if s[xx][yy]>cnt+2:
                        s[xx][yy] = cnt+2
                        heappush(q,(cnt+2,X,Y))

print(s[gx][gy] if s[gx][gy]!=INF else -1)

