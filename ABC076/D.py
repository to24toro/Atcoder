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
T = list(map(int,input().split()))
V = list(map(int,input().split()))
dp = [[0]*101 for _ in range(n+1)]
dp[0][0] = 1
for i in range(0,n):
    t = T[i]
    VV = V[i]
    for v in range(101):
        if dp[i][v] and v<=VV:
            for w in range(101):
                if w<=VV:
                    if t<abs(v-w):
                        continue
                    a = VV-v
                    b = VV-w
                    if a+b<=t:
                        S = (VV+v)*a/2 + VV*(t-a-b) + (w + VV)*b/2
                    else:
                        x = (w-v+t)/2
                        y = (t-w+v)/2
                        S = (2*v+x)*x/2 + (w+v+x)*y/2
                    dp[i+1][w] = max(dp[i+1][w], dp[i][v]+S)
print(dp[n][0]-1)