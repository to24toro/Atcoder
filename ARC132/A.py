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
n = int(input())
R = list(map(int,input().split()))
RR = []
for i,r in enumerate(R):
    RR.append([r,i])
RR.sort(reverse=True)
d = defaultdict(int)
for j in range(n):
    r,i = RR[j]
    d[i] = j
C = list(map(int,input().split()))
CC = []
for i,c in enumerate(C):
    CC.append([c,i])
CC.sort(reverse=True)
dc = defaultdict(int)
for j in range(n):
    c,i = CC[j]
    dc[i] = j
q = int(input())
ans = []
for _ in range(q):
    r,c = map(int,input().split())
    r-=1
    c-=1
    rj = d[r]
    cj = dc[c]
    rr = RR[rj][0]
    cc = CC[cj][0]
    if cj<rr:
        ans.append("#")
    else:
        ans.append('.')
print("".join(ans))