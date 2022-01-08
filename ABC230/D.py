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
<<<<<<< HEAD
n,d = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
L.sort(key = lambda x:x[1])
cnt = 0
q = []
for l,r in L:
    if not q:
        q.append([l,r])
    else:
        if q[-1][-1]+d-1<l:
            cnt += 1
            q.pop()
            q.append([l,r])
        else:
            continue
if q:
    cnt += 1
print(cnt)
=======
>>>>>>> 7ef5272f22bc7d556fd1b34ce9cb0c92784a0a0b
