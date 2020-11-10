class SegmentTree:
    def __init__(self,n,segfunc=min,ele = 10**10):
        self.n = n
        self.segfunc = segfunc
        self.ide_ele = ele
        self.num = 2**(n-1).bit_length()
        self.seg = [self.ide_ele]*2*self.num
    
    def init(self,init_val):
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

    def updaterange(self, a, b, x):
        l = a + (1<<self.n)
        r = b + (1<<self.n)
        s = 0
        while l < r:
            if l%2:
                self.seg[l-1] = max(self.seg[l-1], x)
                l += 1
            if r%2:
                r -= 1
                self.seg[r-1] = max(self.seg[r-1], x)
            l >>= 1
            r >>= 1
    def query(self,p,q):
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
    
    def get_va(self,k):
        k+=self.num-1
        return self.seg[k]
from bisect import bisect_left
n,q = map(int,input().split())
st = SegmentTree(n,min,float('inf'))
X = []
D = []
for _ in range(n):
    s, t, x = map(int, input().split())
    X.append((s, t, x))
for _ in range(q):
    D.append(int(input()))
for s,t,x in X:
    st.updaterange(bisect_left(D,s-x),bisect_left(D,t-x),x)

for i in range(q):
    print(st.query(i,i))