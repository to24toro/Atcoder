from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,q = map(int,input().split())
d = []
L = []
P = []
for _ in range(n):
    s,t,x = map(int,input().split())
    P.append((s-x,-1,x))
    P.append((t-x,1,x))
    L.append((s-x,t-x,x))
L.sort(key = lambda x:-x[2])
for i in range(q):
    x = int(input())
    d.append(x)
    P.append((x,0,i))
P.sort(reverse=True)

ans = [-1]*n
v = -1
hq = []
while P:
    a,b,c = P.pop()
    if b==0:
        ans[c]= max(-1,v)




#####segfunc#####
def segfunc(x, y):
    return min(x,y)
#################

#####ide_ele#####
ide_ele = INF
#################
class LazySegTree_RUQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [None]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.tree[2*i] = v
            self.tree[2*i+1] = v
    def update(self,l,r,x):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def query(self,l,r):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res
a = [INF]*q
seg = LazySegTree_RUQ(a, segfunc, ide_ele)

for l,r,x in L:
    idx = bisect_left(d,l)
    idy = bisect_left(d,r)
    if idx!=idy:
        seg.update(idx,idy,x)
for i in range(q):
    ans = seg.query(i,i+1)
    print(ans if ans!=INF else -1)