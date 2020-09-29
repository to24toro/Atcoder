n,k = map(int,input().split())
mod = 998244353
s = []
for _ in range(k):
    l,r = map(int,input().split())
    s.append((l,r))

dp = [0]*(3*n)
dp[1] = 1

def segfunc(x,y):
    return x+y
ide_ele = 0

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
seg = SegTree(dp,segfunc,ide_ele)
for i in range(1,n):
    dp[i] = seg.get(i)%mod
    for l,r in s:
        seg.update(i+l,i+r+1,dp[i])
dp[n] = seg.get(n)
print(dp[n]%mod)


