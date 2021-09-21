from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(m)]
L.sort(key = lambda x:x[1])
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
class RangeUpdate:
    def __init__(self, n):
        self.p = Bit(n + 1)
        self.q = Bit(n + 1)
     
    def add(self, s, t, x):
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)
     
    def sum(self, s, t):
        t += 1
        return self.p.sum(t) + self.q.sum(t) * t - \
               self.p.sum(s) - self.q.sum(s) * s
bit = RangeUpdate(n)
for l,r,x in L:
    s = bit.sum(l,r)
    if s<x:
        t = x-s
        while t>0:
            e=bit.sum(r,r)
            if e==0:
                bit.add(r,r,1)
                t-=1
            r-=1
A = [0]*(n+1)
for i in range(1,n+1):
    A[i] = bit.sum(i,i)
print(*A[1:])