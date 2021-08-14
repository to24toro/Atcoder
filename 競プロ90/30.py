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

n,k = map(int,input().split())
p = [0]*(n+1)
for i in range(2,n+1):
    if p[i] != 0:
        continue
    for j in range(i,n+1,i):
        p[j] += 1
cnt = 0
for j in range(n+1):
    if p[j]>=k:
        cnt += 1
print(cnt)
