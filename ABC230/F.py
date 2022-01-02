from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
MOD = 998244353
n = int(input())
A = [0] + list(map(int,input().split()))
f = [0]*(n+1)
s = 0
d = defaultdict(int)
for i in range(n+1):
    s +=A[i]
    f[i] = d[s]
    d[s] = i
dp = [0]*(n+1)
dp[1] = 1
for i in range(1,n):
    dp[i+1] = (dp[i]*2 -dp[f[i]])%MOD
print(dp[-1])