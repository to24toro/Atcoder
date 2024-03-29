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

N,M = map(int,input().split())
uf = UnionFind(N)
g = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    uf.unite(a,b)
    g[a].append(b)
    g[b].append(a)


# def dfs(x,pre):
#     for y in g[x]:
#         if y==pre:continue
#         if L[y] == L[x] and L[x]!=-1:
#             return False
#         L[y] = (dic[y]+L[x])%3
#     return True
def helper(s):
    n = len(s)-1
    
    ans = 0
    def dfs(x,pre):
        ans = 1
        for y in g[x]:
            if y==pre:continue
            if L[y] == L[x] and L[x]!=-1:
                return 0
            if L[y]!=-1:continue
            L[y] = (dic[y]+L[x])%3
            ans *=dfs(y,x)
        return ans
    for bit in range(1<<n):
        L = [-1]*N
        L[s[0]] = 0
        dic = defaultdict(int)
        for i in range(n):
            if (bit>>i)&1:
                dic[s[i+1]] = 2
            else:
                dic[s[i+1]] = 1
        flag = dfs(s[0],-1)
        if flag:
            ans += 1
    return ans
Ans = 1
D = defaultdict(list)
for i in range(N):
    D[uf.find(i)].append(i)
# print(D)
for k,li in D.items():
    Ans *= helper(li)*3
print(Ans)
