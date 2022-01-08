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
V = list(map(int,input().split()))
hq = []
heapify(hq)
s = sum(V)
for i in range(1,n+1):
    a = V[n-i]
    b = V[n+i-1]
    heappush(hq,a)
    heappush(hq,b)
    c = heappop(hq)
    s-=c
print(s)
