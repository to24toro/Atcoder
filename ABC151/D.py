from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
h,w = map(int,input().split())
INF = float('inf')
S = [input() for _ in range(h)]
def helper(i,j):
    s = [[INF]*w for _ in range(h)]
    s[i][j] = 0
    res = 0
    q = deque([(0,i,j)])
    while q:
        c,x,y = q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            X = x + dx
            Y = y + dy
            if 0<=X<h and 0<=Y<w and S[X][Y]=='.' and s[X][Y]>c+1:
                s[X][Y] = c+1
                q.append((c+1,X,Y))
    for i in range(h):
        for j in range(w):
            if s[i][j] !=INF:
                res = max(res,s[i][j])
    return res
ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j]=='.':
            ans = max(ans,helper(i,j))
print(ans)