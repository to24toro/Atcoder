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

n,q = map(int,input().split())
g = [-1]*(n+1)
rg = [-1]*(n+1)
A = []
for i in range(q):
    L = list(map(int,input().split()))
    if L[0]==3:
        ans = []
        x = L[1]
        y = x
        while x!=-1:
            ans.append(x)
            x = g[x]
        ans2 = []
        while y!=-1:
            ans2.append(y)
            y = rg[y]
        ans2 = ans2[1:][::-1]
        aa = ans2+ans
        A.append([len(aa),*aa])
    elif L[0]==2:
        x,y = L[1:]
        rg[g[x]]=-1
        g[x] = -1

    else:
        x,y = L[1:]
        g[x] = y
        rg[y] = x
for a in A:
    print(*a)
