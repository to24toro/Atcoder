from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def IR(n):
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
 
sys.setrecursionlimit(1000000)
mod = 1000000007
R,C = LI()
A = LIR(R)
B = LIR(R-1)
dist= [[float('inf')]*C for _ in range(R)]

q = [(0,0,0)]
D = [(1,0),(0,1),(0,-1)]
import heapq
heapq.heapify(q)
dist[0][0]=0
while q:
    c,x,y = heapq.heappop(q)
    if dist[x][y]<c:
        continue
    if x==R-1 and y==C-1:
        print(c);exit()
    X = x+1
    Y = y
    for i,(dx,dy) in enumerate(D):
        Y,X = y+dy,x+dx
        if 0 <= X < R and 0 <= Y < C:
            if i == 0:
                nd = c+B[x][y]
            elif i == 1:
                nd = c+A[x][y]
            else:
                nd = c+A[x][Y]
            if nd < dist[X][Y]:
                dist[X][Y] = nd
                heappush(q,(nd,X,Y))
    for i in range(1,x+1):
        X = x-i
        Y = y
        cnt =i+1+c
        if dist[X][Y]>cnt:
            dist[X][Y] = cnt
            heapq.heappush(q,(cnt,X,Y))


