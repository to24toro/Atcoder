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


n = int(input())

S = list(map(lambda x: ord(x)-ord('a'),input()))

s ='atcoder'
set_ = set()
for i in s:
    set_.add(ord(i)-ord('a'))

dp = [[0]*8 for _ in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    v = S[i-1]
    if v not in set_:
        dp[i] = dp[i-1]
        continue
    dp[i][0] = dp[i-1][0]
    for j in range(1,8):
        if v==ord(s[j-1])-ord('a'):
            dp[i][j] += dp[i-1][j-1]+dp[i-1][j]
            dp[i][j] %=MOD
        else:
            dp[i][j] = dp[i-1][j]
print(dp)
print(dp[-1][-1]%MOD)
