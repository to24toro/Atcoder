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
dp = [[[0,0] for _ in range(26)] for _ in range(n+1)]
dp[1][S[0]][1] = 1
for x in range(1,n):
    dp2 = [[[0,0] for _ in range(26)] for _ in range(n+1)]
    s = S[x]
    print(dp)
    dp2=dp
    dp[1][s][1]
    for i in range(x):
        for j in range(26):
            dp2[i+1][s][1] += dp[i][j][0]+dp[i][j][1]
            dp2[i+1][s][1]%=mod
    dp = dp2
    print(dp)
ans = 0
# print(dp)
for i in range(n+1):
    for j in range(26):
        ans += sum(dp[i][j])
    ans %=mod
print(ans)
ans2 = 0
for i in range(n+1):
    for j in range(26):
        ans2 += sum(dp2[i][j])
    ans2 %=mod
print(ans2)


