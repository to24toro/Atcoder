from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import numpy as np
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

n = int(input())
A = [[0]*1011 for _ in range(1011)]
for _ in range(n):
    a,b,c,d = map(int,input().split())
    A[a][b] += 1
    A[a][d] -= 1
    A[c][d] += 1
    A[c][b] -= 1
for i in range(1010):
    for j in range(1,1010):
        A[i][j]+=A[i][j-1]
for i in range(1,1010):
    for j in range(1010):
        A[i][j]+=A[i-1][j]
Ans = defaultdict(int)
for i in range(1001):
    for j in range(1001):
        if A[i][j]>=1:
            Ans[A[i][j]] += 1
for i in range(1,n+1):
    print(Ans[i])
