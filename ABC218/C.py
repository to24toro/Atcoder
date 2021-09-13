from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
SS = [input() for _ in range(n)]
TT = [input() for _ in range(n)]
S = []
T = []
ss = 0
tt = 0
for i in range(n):
    for j in range(n):
        if SS[i][j]=='#':
            ss += 1
        if TT[i][j]=='#':
            tt += 1
if ss!=tt:print('No');exit()
for i in range(n):
    tmp  =[]
    for j in range(n):
        s = SS[i][j]
        tmp.append(s)
    S.append(tmp)
for i in range(n):
    tmp  =[]
    for j in range(n):
        s =TT[i][j]
        tmp.append(s)
    T.append(tmp)
SA = S
SB =[['']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        SB[j][n-1-i] = SA[i][j]
SC =[['']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        SC[j][n-1-i] = SB[i][j]
SD =[['']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        SD[j][n-1-i] = SC[i][j]
f = False
for i in range(n):
    for j in range(n):
        if T[i][j]=="#":
            tx,ty = i,j
            f =True
            break
    if f:
        break

t = [[0]* n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if T[i][j]=="#":
            t[i][j] = 1
def helper(A,tx,ty,t):
    f =False
    for i in range(n):
        for j in range(n):
            if A[i][j]=="#":
                sx,sy = i,j
                f =True
                break
        if f:
            break
    for i in range(n):
        for j in range(n):
            if A[i][j] =="#":
                if 0<=tx-sx+i <n and 0<=ty-sy+j<n:
                    t[tx-sx+i][ty-sy+j] = 0
                    A[i][j]=0
    # print(t)
    for i in range(n):
        for j in range(n):
            if t[i][j]==1:
                return False
    for i in range(n):
        for j in range(n):
            if A[i][j]==1:
                return False
    return True

if helper(SA,tx,ty,deepcopy(t)):
    print('Yes');exit()
if helper(SB,tx,ty,deepcopy(t)):
    print('Yes');exit()
if helper(SC,tx,ty,deepcopy(t)):
    print('Yes');exit()
if helper(SD,tx,ty,deepcopy(t)):
    print('Yes');exit()
print('No')