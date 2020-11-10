class STLP:#Range Minimum Query and Range Update Query 
    def __init__(self,n,segfunc=min,ele=float('inf')):
        self.segfunc = segfunc
        self.ide_ele = ele
        self.LV = (n-1).bit_length()
        self.data = [self.ide_ele]*(2*(2**self.LV))
        self.lazy = [None]*(2*(2**self.LV))
    
    def gindex(self,l,r):
        L = (1+2**self.LV)>>1;R = (r+2**self.LV)>>1
        lc = 0 if l&1 else (L&-L).bit_length()
        rc = 0 if r&1 else (R&-R).bit_length()
        for i in range(self.LV):
            if rc<=i:
                yield R
            if L<R and lc<=i:
                yield L
            L>>=1;R>>=1
    
    def propagates(self,*ids):# 遅延伝搬処理
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None:
                continue
            self.lazy[2*i-1] = self.data[2*i-1] = self.lazy[2*i] = self.data[2*i] = v
            self.lazy[i-1] = None
    
    # 区間[l, r)をxで更新
    def update(self,l, r, x):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L = 2**self.LV + l; R = 2**self.LV + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.data[R-1] = x
            if L & 1:
                self.lazy[L-1] = self.data[L-1] = x
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            self.data[i-1] = min(self.data[2*i-1], self.data[2*i])

    # 区間[l, r)内の最小値を求める
    def query(self,l, r):
        self.propagates(*self.gindex(l, r))
        L = 2**self.LV + l; R = 2**self.LV + r

        s = self.ide_ele
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])
            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

class segtree:
    def __init__(self,n):
        self.NN = n
        self.XX = [0]*(2**(n+1)-1)
    def getmax(self,i):
        j = 2**self.NN+i-1
        ma = -1
        while j>=0:
            ma = max(ma,self.XX[j])
            j = (j-1)//2
        return -1 if ma<=0 else (1<<50)-ma
    def updaterange(self,a,b,x):
        l = a+(1<<self.NN)
        r = b+(1<<self.NN)
        s = 0
        while l<r:
            if l%2:
                self.XX[l-1] = max(self.XX[l-1],x)
                l+=1
            if r%2:
                r-=1
                self.XX[r-1] = max(self.XX[r-1],x)
            l>>=1
            r>>=1

ans = []
# from bisect import bisect_left as bl
# N, Q = map(int, input().split())
# st = segtree(18)
# X = []
# D = []
# for _ in range(N):
#     s, t, x = map(int, input().split())
#     X.append((s, t, x))
# for _ in range(Q):
#     D.append(int(input()))
# for s, t, x in X:
#     st.updaterange(bl(D, s-x), bl(D, t-x), (1<<50)-x)
# for i in range(Q):
#     print(st.getmax(i))
from bisect import bisect_left as bl
N, Q = map(int, input().split())
X = []
D = []
for _ in range(N):
    s, t, x = map(int, input().split())
    X.append((s, t, x))
X.sort(key = lambda x:x[2])
for _ in range(Q):
    D.append(int(input()))
skip = [-1]*Q
ans = [-1]*Q
for s, t, x in X:
    l = bl(D,s-x)
    r = bl(D,t-x)
    while l<r:
        if skip[l]==-1:
            ans[l]=x
            skip[l]=r
            l += 1
        else:
            l = skip[l]
print(*ans,sep='\n')