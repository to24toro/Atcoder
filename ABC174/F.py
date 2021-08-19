class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
 
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
 
    def sumrange(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
 
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

N,Q = map(int,input().split())
q = [[] for _ in range(N)]
c = list(map(lambda x:int(x)-1,input().split()))
ans = [0]*Q

for i in range(Q):
    l,r = map(int,input().split())
    l-=1
    r-=1
    q[r].append((l,i))

bit = BIT(N)
C = [-1]*N
p = 0

for i in range(N):
    if p==Q:
        break
    if C[c[i]]!=-1:
        bit.add(C[c[i]],-1)
    bit.add(i,1)
    C[c[i]] = i
    for l,j in q[i]:
        ans[j] = bit.sumrange(l,i+1)
        p += 1
        if p==Q:
            break

for a in ans:
    print(a)