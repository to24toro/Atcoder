import collections
from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,k = map(int,input().split())

L = [list(map(int,input().split())) for _ in range(n)]
L.sort(key = lambda x:x[1],reverse=True)
S = 0
set_ = set()
hq = []
cnt = 0
for i in range(k):
    t,d = L[i]
    S += d
    if t in set_:
        heappush(hq,[d,t])
    else:
        cnt+=1
        set_.add(t)
S+=cnt**2
q =deque(L[k:])
ans = S
if cnt==n:
    print(ans)
    exit()
for t,d in L[k:]:
    if not hq:break
    if t in set_:
        continue
    set_.add(t)
    S -= heappop(hq)[0]
    S += d
    S -= cnt**2
    S += (cnt+1)**2
    ans = max(ans,S)
    cnt+=1
print(ans)