from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,m =map(int,input().split())
S = [0]*(n+1)
L = -1
R = n+1
for _ in range(m):
    l,r = map(int,input().split())
    L = max(L,l)
    R = min(r,R)
print(R-L+1)