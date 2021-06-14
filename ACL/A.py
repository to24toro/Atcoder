from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
from typing import Union
sys.setrecursionlimit(1<<20)
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

n = int(input())
dic = {}
L = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    y = L[i][1]
    y-=1
    dic[y]= i
L.sort()
l = []
uf = UnionFind(n)
for x,y in L:
    y-=1
    m = y
    while l and l[-1]<y:
        v = l.pop()
        uf.unite(v,y)
        m = min(m,v)
    l.append(m)
ans = [-1]*n
for y in range(n):
    ans[dic[y]] = uf.size(y)
print("\n".join(map(str, ans)))