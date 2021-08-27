from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
mod = 998244353
n = int(input())
S = input()
S = [ord(s)-ord('A') for s in S]
dp = [[[0]*10 for _ in range(1<<10)] for _ in range(n+1)]
for i in range(1,n+1):
    s = S[i-1]
    for bit in range(1<<10):
        for j in range(10):
            dp[i][bit][j]+=dp[i-1][bit][j]
            if s==j:
                dp[i][bit][j]+=dp[i-1][bit][j]
            if bit&(1<<s)==0:
                dp[i][bit|(1<<s)][s] += dp[i-1][bit][j]
            dp[i][bit][j]%=mod
        if bit==1<<s:
            dp[i][bit][s]+=1
ans = 0
d = dp[-1]
for i in range(1<<10):
    for j in range(10):
        ans += d[i][j]
        ans %= mod
print(ans)