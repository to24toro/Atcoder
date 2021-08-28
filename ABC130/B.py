from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,x = map(int,input().split())
L = [0]+list(map(int,input().split()))
d = 0
for i in range(n+1):
    d += L[i]
    if d>x:
        print(i);exit()
print(n+1)