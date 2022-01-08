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

n = int(input())
P = list(map(lambda x: int(x)-1,input().split()))
A = []
dic = defaultdict(int)
rdic = defaultdict(int)
for i,p in enumerate(P):
    A.append((p,i))
    dic[p] = i
    rdic[i] = p
uf = UnionFind(n)
m = int(input())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1

    g[a].append(b)
    g[b].append(a)
    uf.unite(a,b)
for p,i in A:
    print(p,i)
    if uf.parents[i]==-1 and p!=i:
        print(-1);exit()
    elif uf.find(i)!=uf.find(p):
        print(-1);exit()

set_ = {uf.find(i) for i in range(n)}
D = defaultdict(list)
for i in range(n):
    D[uf.find(i)].append((dic[i],i))
print(D)
def bfs(s,e,seen):
    q = deque([(s,[])])
    ss = set()
    ss.add(s)
    while q:
        x,path = q.popleft()
        if x==e:
            for a,b in path:
                tmp = rdic[a]
                rdic[a] = rdic[b]
                rdic[b] = tmp
                dic[a] = rdic[a]
                dic[b] = rdic[b]
            return path
        for y in g[x]:
            if y not in ss and y not in seen:
                ss.add(y)
                q.append((y,path+[(x,y)]))
    return [-1,-1]


def find(start,end,seen):
    res = []
    res = bfs(start,end,seen)

    seen.add(start)
    print(res)
    for nxt in g[start]:
        if nxt not in seen:
            seen.add(nxt)
            res += bfs(nxt,dic[nxt],seen)
    return res
for s in set_:
    L = D[s]
    start = -1
    cur = INF
    seen = set()
    for p,i in L:
        if len(g[i])<cur:
            cur = len(g[i])
            start = i
    end = dic[start]
    seen.add(start)
    L = find(start,end,seen)
    print(L)