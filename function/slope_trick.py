from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
q = int(input())
b = 0
L1 = [INF]
L2 = [INF]
l1 = 0
l2 = 0
s1 = 0
s2 = 0

for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] ==1:
        p = query[1]
        b += query[2]
        l0 =-L1[0]
        b += max(0,l0-p)
        heappush(L2,-heappushpop(L1,-p))
        l0 = L2[0]
        b += max(p-l0,0)
        heappush(L1,-heappushpop(L2,p))
    else:
        print(-L1[0],b)