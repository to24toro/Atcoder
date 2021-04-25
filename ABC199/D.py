n,m = map(int,input().split())
# g = [[] for _ in range(n)]
# for _ in range(m):
#     a,b = map(int,input().split())
#     a-=1
#     b-=1
#     g[a].append(b)
#     g[b].append(a)
# seen = [0]*n
# L = []
# def dfs(i):
#     seen[i]=1
#     ans = [i]
#     for j in g[i]:
#         if not seen[j]:
#             ans+=dfs(j)
#     return ans

# for i in range(n):
#     if not seen[i]:
#         L+=dfs(i)
# print(L)

from itertools import product
AB = [list(map(lambda x:int(x)-1,input().split())) for _ in range(m)]
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
uf = UnionFind(n)
ans =0
for bit in product([0,1], repeat=n):
    uf = UnionFind(2*n)
    for a,b in AB:
        if bit[a]==0 and bit[b]==0:
            break
        elif bit[a]==1 and bit[b]==1:
            uf.unite(a,b+n)
            uf.unite(b,a+n)
    else:
        for i in range(n):
            if uf.same(i,i+n):
                break
        else:
            ans += 2**(uf.group_count()//2-(n-sum(bit)))
        
print(ans)