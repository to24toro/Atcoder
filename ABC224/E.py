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
=======
h,w,n = map(int,input().split())
L  =[]
for i in range(n):
    r,c,a = map(int,input().split())
    r-=1
    c-=1
    L.append((a,r,c,i))
L.sort(reverse=True)
D = defaultdict(list)
for a,r,c,i in L:
    D[a].append((r,c,i))
dp = [0]*n
rm = [0]*h
cm = [0]*w
pre = INF
L = sorted(D.items(),reverse=True)
for k,l in L:
    for r,c,i in l:
        dp[i] = max(rm[r],cm[c])
    for r,c,i in l:
        rm[r] = max(rm[r],dp[i]+1)
        cm[c] = max(cm[c],dp[i]+1)
for p in dp:
    print(p)
>>>>>>> c0748bd4c077c3dfd6e4d18e63f762403879af12
