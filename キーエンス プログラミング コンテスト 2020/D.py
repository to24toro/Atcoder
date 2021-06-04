from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
AB = [A,B]
dp = [[float('inf')]*n for _ in range(1<<n)]

for i in range(n):
    dp[1<<i][i] = 0

for bit in range(1<<n):
    for j in range(n):
        if dp[bit][j]<float('inf'):
            count1 = bin(bit).count('1')
            vj = AB[abs(j - count1 + 1) % 2][j]
            cnt = 0
            for k in range(n):
                if bit >> k & 1:
                    cnt += 1
                else:
                    vk = AB[abs(k - count1) % 2][k]
                    if vj <= vk:
                        nBIT = bit | (1 << k)
                        dp[bit|nBIT][k] = min(dp[nBIT][k], dp[bit][j] + (count1 - cnt))
    ans = min(dp[-1])
if ans == float('inf'):
    print(-1)
else:
    print(ans)