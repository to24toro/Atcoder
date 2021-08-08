from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

h,w = map(int,input().split())
q = int(input())
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
uf = UnionFind(h*w)
S = [0]*(h*w)
for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        r,c = query[1:]
        r-=1
        c-=1
        p = c + w*r
        S[p] = 1
        # print(uf.parents)
        for i in range(4):
            rrr = r+dx[i]
            ccc = c+dy[i]
            if 0<=rrr<h and 0<=ccc<w:
                pp = ccc + w*rrr
                # print(p,pp,ccc,rrr)
                if S[pp]==1:
                    uf.unite(p,pp)
        # print("AA",uf.parents)
    else:
        r,c,rr,cc = query[1:]
        r-=1
        c-=1
        rr-=1
        cc-=1
        p = c + w*r
        pp = cc + w*rr
        # if uf.parents[p]>=-1 and uf.parents[pp]>=-1:
        # print(uf.find(p))
        if p==pp and S[p] == 0:
            print('No')
        elif uf.same(p,pp):
            print('Yes')
        else:
            print('No')
        # else:
        #     print('No')


