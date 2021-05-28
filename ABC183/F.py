from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,q = map(int,input().split())
C = list(map(int,input().split()))

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
member=[defaultdict(int) for _ in range(n)]
for i,c in enumerate(C):
    member[i][c]+=1
# print(member)
uf = UnionFind(n)
for _ in range(q):
    n,x,y = map(int,input().split())
    if n==1:
        x-=1
        y-=1
        x = uf.find(x)
        y = uf.find(y)
        if x==y:
            continue
        if uf.size(x)<uf.size(y):
            x,y = y,x
        uf.unite(x,y)
        for k,v in member[y].items():
            member[x][k]+=v
        # print(member,x,y)
    else:
        x-=1
        idx = uf.find(x)
        print(member[idx][y])

