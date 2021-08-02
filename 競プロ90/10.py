from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

n = int(input())
sa = []
sb = []
for i in range(n):
    c,p = map(int,input().split())
    if c==1:
        sa.append(p)
        sb.append(0)
    else:
        sa.append(0)
        sb.append(p)

SA = [0]+ list(accumulate(sa))
SB = [0]+ list(accumulate(sb))
q = int(input())
for _ in range(q):
    l,r = map(int,input().split())
    l-=1
    print(SA[r]-SA[l],SB[r]-SB[l])
