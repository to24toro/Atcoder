from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

h,w = map(int,input().split())
S = [input() for _ in range(h)]
uf = UnionFind(h+w)
ans = INF
for i in range(h):
    for j in range(w):
        if S[i][j]=="#":
            uf.unite(i,h+j)
uf.unite(0,h)
uf.unite(h-1,h)
uf.unite(0,h+w-1)
uf.unite(h-1,h+w-1)
l = [0]*(h+w)
for i in range(h):
    l[uf.find(i)] = 1
ans = min(ans,sum(l)-1)
l = [0]*(h+w)
for i in range(h,h+w):
    l[uf.find(i)] = 1
ans = min(ans,sum(l)-1)
print(ans)