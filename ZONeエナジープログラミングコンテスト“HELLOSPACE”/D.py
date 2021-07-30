from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

R,C = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(R)]
B = [list(map(int,input().split())) for _ in range(R-1)]

dist = [[INF]*C for _ in range(R)]
# dist[0][0] = 0
hq = [(0,0,0)]
heapify(hq)
while hq:
    cost,x,y = heappop(hq)
    if dist[x][y]<cost:
        continue
    if x==R-1 and y ==C-1:
        print(cost);exit()
    dist[x][y] = cost
    X = x
    Y = y+1
    if 0<=X<R and 0<=Y<C:
        cc = A[x][y]
        if dist[X][Y]>cost + cc:
            dist[X][Y] = cost + cc
            heappush(hq,(cost+cc,X,Y))
    X = x
    Y = y-1
    if 0<=X<R and 0<=Y<C:
        cc = A[X][Y]
        if dist[X][Y]>cost + cc:
            dist[X][Y] = cost + cc
            heappush(hq,(cost+cc,X,Y))
    X = x+1
    Y = y
    if 0<=X<R and 0<=Y<C:
        cc = B[x][y]
        if dist[X][Y]>cost + cc:
            dist[X][Y] = cost + cc
            heappush(hq,(cost+cc,X,Y))
    for i in range(1,x+1):
        X = x - i
        Y = y
        if 0<=X<R and 0<=Y<C and dist[X][Y]>cost + 1 + i:
            dist[X][Y] = cost + 1 + i
            heappush(hq,(cost+1+i,X,Y))

