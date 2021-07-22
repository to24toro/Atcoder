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
se = set()
LR = [-2]*(2*n)
RL = [-2]*(2*n)
f = True
for _ in range(n):
    a,b = map(int,input().split())
    if a!=-1:
        a-=1
    if b!=-1:
        b-=1
    if a!=-1:
        LR[a] = b
        if a in se:
            f = False
        se.add(a)
    if b!=-1:
        RL[b] = a
        if b in se:
            f = False
        se.add(b)
    if a!=-1 and b!=-1 and a>=b:f = False
if not f:print('No');exit()

def chk (l,r):
    if (l>=r):return False
    if (r-l)%2==1:return False
    m = (l+r)//2
    d = (r-l)//2
    for i in range(m,r):
        if LR[i]!=-2:return False
    for i in range(l,m):
        if RL[i]!=-2:return False
    for i in range(l,m):
        if LR[i]>=0 and LR[i] != i+d:return False
        if LR[i]==-1 and RL[i+d] !=-2:return False
    for i in range(m,r):
        if RL[i]>=0 and RL[i] != i-d:return False
        if RL[i]==-1 and LR[i-d] !=-2:return False
    return True
valid = [[False]*(2*n+1) for _ in range(2*n+1)]
for i in range(2*n):
    for j in range(i+1,2*n+1):
        valid[i][j] = chk(i,j)

dp = [False]*(2*n+1)
dp[0] = True

for i in range(2*n):
    if not dp[i]:continue
    for j in range(i+1,2*n+1):
        if valid[i][j]:dp[j] = True
if dp[2*n]:print('Yes')
else:print('No')
