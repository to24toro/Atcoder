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
L = []
for i in range(n):
    s,p = map(str,input().split())
    L.append((s,int(p),i))
L.sort(key = lambda x:(x[0],-x[1]))
for s,p,i in L:
    print(i+1)