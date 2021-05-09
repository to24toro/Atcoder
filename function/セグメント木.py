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

def op(a,b): return a ^ b
st = SegmentTree(n,segfunc=op,ele = 0)
# st.init(A)


# def segfunc(x,y):
#     return gcd(x,y)
# ide_ele = 1
# class SegTree:
#     def __init__(self, init_val, segfunc, ide_ele):
#         n = len(init_val)
#         self.segfunc = segfunc
#         self.ide_ele = ide_ele
#         self.num = 1 << (n - 1).bit_length()
#         self.tree = [ide_ele] * 2 * self.num
#         # 配列の値を葉にセット
#         for i in range(n):
#             self.tree[self.num + i] = init_val[i]
#         # 構築していく
#         for i in range(self.num - 1, 0, -1):
#             self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

#     def update(self,l,r,x):
#         l += self.num
#         r += self.num
#         while l<r:
#             if l&1:
#                 self.tree[l] = self.segfunc(x,self.tree[l])
#                 l += 1
#             if r&1:
#                 self.tree[r-1] = self.segfunc(x,self.tree[r-1])
#             l>>=1
#             r>>=1

#     def query(self, l, r):

#         res = self.ide_ele

#         l += self.num
#         r += self.num
#         while l < r:
#             if l & 1:
#                 res = self.segfunc(res, self.tree[l])
#                 l += 1
#             if r & 1:
#                 res = self.segfunc(res, self.tree[r - 1])
#             l >>= 1
#             r >>= 1
#         return res
