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
s = list(input())
n = len(s)
for i in range(n):
    s[i] = int(s[i])
if s[0] !=1 or s[-1] != 0:
    print(-1);exit()
if any(s[i]!=s[n-2-i] for i in range(n-1)):
    print(-1);exit()
m = n-1
g = []
for i in range(n-1)[::-1]:
    g.append([i+1,m+1])
    if s[i] == 1:
        m = i
for a,b in g:
    print(a,b)
