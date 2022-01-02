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
n,m = map(int,input().split())

g = [list() for i in range(n)]
for i in range(m):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    g[A].append(B)
    g[B].append(A)
k = int(input())
C = list(map(int, input().split()))
for i in range(k):
    C[i] -= 1


def BFS(s):
    cost = [INF] * n
    cost[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in g[x]:
            if cost[y] == INF:
                cost[y] = cost[x] + 1
                q.append(y)
    return [cost[c] for c in C]
 
d = [BFS(c) for c in C]
dp = [[INF] * k for _ in range(1 << k)]
for i in range(k):
    dp[1 << i][i] = 1
 
for bit in range(1 << k):
    for i in range(k):
        if dp[bit][i] == INF:
            continue
        for j in range(k):
            if bit & 1 << j:
                continue
            if dp[bit ^ 1 << j][j] > dp[bit][i] + d[i][j]:
                dp[bit ^ 1 << j][j] = dp[bit][i] + d[i][j]
ans = min(dp[-1])
# print(dp)
print(ans if ans!=INF else -1)