n,q = map(int,input().split())
A = list(map(int,input().split()))
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
st.init(A)

for _ in range(q):
    t,x,y = map(int,input().split())
    x-=1
    if t==1:
        st.update(x,st.get_val(x)^y)
    else:
        print(st.query(x,y))
