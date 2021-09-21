from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
ans = 0
A = [list(map(int,input().split())) for _ in range(4)]
def dfs1(i,j):
    d = [(1,0),(0,-1),(-1,0),(0,1)]
    for di,dj in d:
        I = i+di
        J = j+dj
        if 0<=I<6 and 0<=J<6:
            if B[I][J] ==1:
                B[I][J] = 2
                dfs1(I,J)
def dfs2(i,j):
    d = [(1,0),(0,-1),(-1,0),(0,1)]
    for di,dj in d:
        I = i+di
        J = j+dj
        if 0<=I<6 and 0<=J<6:
            if B[I][J] ==0:
                B[I][J] = 2
                dfs2(I,J)
for bit in range(1<<16):
    B = [[0,0,0,0,0,0] for _ in range(6)]
    f = True
    for i in range(16):
        if (bit>>i)&1:
            x = i//4
            y = i%4
            B[x+1][y+1] = 1
        else:
            if A[i//4][i%4]==1:
                f = False
                break
    if not f:
        continue
    # print(B)
    f = True
    for i in range(6):
        p=False
        for j in range(6):
            if B[i][j] ==1:
                B[i][j] = 2
                dfs1(i,j)
                p=True
                break
        if p:break
    for i in range(6):
        p = False
        for j in range(6):
            if B[i][j] ==0:
                B[i][j] = 3
                dfs2(i,j)
                p=True
                break
        if p:break
    # print(B)
    for i in range(6):
        for j in range(6):
            if B[i][j]==0 or B[i][j] ==1:
                f = False
                break
    if f:
        ans += 1
    # if ans ==10:
    #     break
print(ans)
