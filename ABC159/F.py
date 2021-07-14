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

MOD = 10**9+7

n,s = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
# dp = [0]*s

# for i,a in enumerate(A):
#     if a>s:
#         continue
#     if a==s:
#         ans += (i+1)*(n-i)
#         ans%=MOD
#     else:
#         ans += dp[s-a]*(n-i)
#         ans%=MOD
#         for j in range(s-1,a,-1):
#             dp[j]+=dp[j-a]
#             dp[j]%=MOD
#         dp[a]+=(i+1)
#         dp[a]%=MOD
# print(ans)
f = np.zeros(3010,np.int64)
for a in A:
    f[0]+=1
    f[a:] += f[:-a].copy()
    f%=MOD
    ans += f[s]
    ans%=MOD
ans %= MOD
print(ans)