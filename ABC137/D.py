from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
dic = defaultdict(list)
for a,b in L:
    dic[a].append(b)
day = m
hq = []
ans = 0
for day in range(m-1,-1,-1):
    for b in dic[m-day]:
        heappush(hq,-b)
    if hq:
        ans -=heappop(hq)
print(ans)