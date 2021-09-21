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
MOD = 10**9+7
A = list(map(int,input().split()))
SUM = [0] + list(accumulate(A))

idx = [[-1]*(n+1) for _ in range(n+1)]
pre = [[-1]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(1,n+1):
        idx[i][j] = pre[j][SUM[i]%j]
        pre[j][SUM[i]%j] = i
DP=[[0]*(n+1) for i in range(n+1)]
DP[0][0]=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if idx[i][j] !=-1:
            DP[i][j]=(DP[idx[i][j]][j]+DP[idx[i][j]][j-1])%MOD
 
print(sum(DP[n])%MOD)