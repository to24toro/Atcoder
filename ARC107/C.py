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

n,K = map(int,input().split())
mod = 998244353

uf1 = UnionFind(n)
A = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if A[i][k]+A[j][k]>K:
                break
        else:
            uf1.unite(i,j)
ans =1
dic = defaultdict(int)
for i in range(n):
    dic[uf1.find(i)] += 1
for k,v in dic.items():
    for j in range(1,v+1):
        ans *= j
        ans %=mod

uf2 = UnionFind(n)
for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if A[k][i]+A[k][j]>K:
                break
        else:
            uf2.unite(i,j)

dic = defaultdict(int)
for i in range(n):
    dic[uf2.find(i)] += 1
for k,v in dic.items():
    for j in range(1,v+1):
        ans *= j
        ans %=mod

print(ans)
