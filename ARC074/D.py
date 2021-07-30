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
A = list(map(int,input().split()))

S = [0]*(3*n)
T = [0]*(3*n)
pq = [0] * n
s = 0
 
for i in range(3 * n):
    x = heappop(pq)
    s -= x
    x = max(x, A[i])
    heappush(pq, x)
    s += x
    S[i] = s

pq = [-10 ** 10] * n
s = n * 10 ** 10
 
for i in range(3*n-1, -1, -1):
    x = -heappop(pq)
    s -= x
    x = min(x, A[i])
    heappush(pq, -x)
    s += x
    T[i] = s
ans = -INF

for i in range(n-1,2*n):
    ans = max(ans,S[i]-T[i+1])
print(ans)


