from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
from typing import Union
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

n = int(input())
L = []
uf = UnionFind(2*10**5+10)
for _ in range(n):
    x,y = map(int,input().split())
    x-=1
    y-=1
    y += 10**5
    L.append((x,y))
    uf.unite(x,y)
dic = defaultdict(lambda :defaultdict(int))
for i in range(10**5):
    x = uf.find(i)
    y = uf.find(10**5+i)
    dic[x][0] += 1
    dic[y][1] += 1
ANS = {}
for k,v in dic.items():
    if dic[k][0] and dic[k][1]:
        ANS[k] = dic[k][0]*dic[k][1]
for x,y in L:
    p = uf.find(x)
    if p in ANS:
        ANS[p]-=1
ans = 0
for k,v in ANS.items():
    ans += v
print(ans)