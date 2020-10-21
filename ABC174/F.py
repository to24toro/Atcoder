class SegTree:
    
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]

    def get(self,k):
        k += self.num
        res = self.tree[k]
        while k>1:
            res = self.segfunc(self.tree[k>>1],res)
            k>>=1
        return res
    
    def update(self,l,r,x):
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.tree[l] = self.segfunc(x,self.tree[l])%mod
                l += 1
            if r&1:
                self.tree[r-1] = self.segfunc(x,self.tree[r-1])%mod
            l>>=1
            r>>=1

n,q = map(int,input().split())
