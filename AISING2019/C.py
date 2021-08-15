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
A = [input() for _ in range(h)]
S = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if A[i][j] =='.':
            S[i][j] = 1
D = [[-1]*w for _ in range(h)]
q = deque([(0,0,0,0,S[0][0])])
def dfs(i,j,cnt,color):
    for di,dj in [(1,0),(0,1),(0,-1),(-1,0)]:
        I = i+ di
        J = j + dj
        if 0<=I<h and 0<=J<w and D[I][J]==-1 and S[I][J] == 1-color:
            D[I][J] = cnt
            dfs(I,J,cnt,1-color)
cnt = 0
for i in range(h):
    for j in range(w):
        if D[i][j]==-1:
            D[i][j] = cnt
            dfs(i,j,cnt,S[i][j])
            cnt +=1
# print(*D)
ans = 0
L = [[0,0] for _ in range(cnt)]
for i in range(h):
    for j in range(w):
        L[D[i][j]][S[i][j]]+=1
for i in range(cnt):
    ans += L[i][0]*L[i][1]
print(ans)

