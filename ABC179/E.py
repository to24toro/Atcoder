from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,x,m = map(int,input().split())

h = {}
h[x] = 0
a = [x]

p = -1
while True:
    v = a[-1]*a[-1]%m
    if v in h:
        p = len(a)-h[v]
        break
    a.append(v)
    h[v]=len(a)-1
t = len(a)-p
if n <=len(a):
    print(sum(a[:n]))
else:
    s = (n-t)//p
    u = (n-t)%p + t
    print(sum(a[:u])+s*sum(a[t:]))