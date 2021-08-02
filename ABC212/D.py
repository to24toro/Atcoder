from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = 2**31 - 1
#################

class LazySegmentTree:
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        num: n以上の最小の2のべき乗
        data: 値配列(1-index)
        lazy: 遅延配列(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):
            """
            伝搬する対象の区間を求める
            lm: 伝搬する必要のある最大の左閉区間
            rm: 伝搬する必要のある最大の右開区間
            """
            l += self.num
            r += self.num
            lm = l >> (l & -l).bit_length()
            rm = r >> (r & -r).bit_length()

            while r > l:
                if l <= lm:
                    yield l
                if r <= rm:
                    yield r
                r >>= 1
                l >>= 1
            while l:
                yield l
                l >>= 1

    def propagates(self, *ids):
        """
        遅延伝搬処理
        ids: 伝搬する対象の区間 
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if not v:
                continue
            self.lazy[2 * i] += v
            self.lazy[2 * i + 1] += v
            self.data[2 * i] += v
            self.data[2 * i + 1] += v
            self.lazy[i] = 0

    def add(self, l, r, x):
        """
        区間[l, r)の値にxを加算
        l, r: index(0-index)
        x: additional value
        """
        *ids, = self.gindex(l, r)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] += x
                self.data[l] += x
                l += 1
            if r & 1:
                self.lazy[r - 1] += x
                self.data[r - 1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1]) + self.lazy[i]


    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res
class SegmentTree:
    def __init__(self,n,segfunc=min,ele = 10**10):
        self.n = n
        self.segfunc = segfunc
        self.ide_ele = ele
        self.num = 2**(n-1).bit_length()
        self.seg = [self.ide_ele]*2*self.num
    
    def init(self,init_val):#[0-indexで良い]
        for i in range(self.n):
            self.seg[i+self.num-1] = init_val[i]
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.segfunc(self.seg[2*i+1],self.seg[2*i+2])
    

    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
    
    def query(self,p,q):#qは含まない
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res = self.ide_ele
        while q-p>1:
            if p%2==0:
                res = self.segfunc(res,self.seg[p])
            if q%2==1:
                res = self.segfunc(res,self.seg[q])
                q-=1
            p//=2
            q = (q-1)//2
        if p==q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]), self.seg[q])
        return res
    
    def get_val(self,k):
        k+=self.num-1
        return self.seg[k]

q = int(input())
A = [10**10]*q
st = LazySegmentTree(A,segfunc=segfunc,ide_ele = INF)
st2 = SegmentTree(q,segfunc=segfunc,ele = INF)
p = 0
for _ in range(q):
    query = list(map(int,input().split()))
    if query[0]==1:
        v = query[1]
        st.add(p,p+1,v-10**10)
        p+=1
    elif query[0]==2:
        v = query[1]
        st.add(0,p+1,v-10**10)
    else:
        res = st.query(0,p+1)



