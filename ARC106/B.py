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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
from collections import defaultdict
da = defaultdict(int)
db = defaultdict(int)
uf = UnionFind(n)
for i in range(m):
    c,d = map(int,input().split())
    c-=1
    d-=1
    uf.unite(c,d)
for i in range(n):
    x = uf.find(i)
    da[x]+=A[i]
    db[x]+=B[i]
for key in da.keys():
    if da[key]!=db[key]:
        print('No');exit()
print('Yes')