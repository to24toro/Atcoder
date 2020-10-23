class UnionFind:
    def __init__(self, n: int):
        self.nodes = n
        self.parents = [-1] * n
        self.rank = [0] * n
    
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
        if self.rank[x] < self.rank[y]:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
        else:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
 
    def get_size(self, x):
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)

n,m = map(int,input().split())

bridges = []
for _ in range(m):
    a,b,y = map(int,input().split())
    bridges.append((a,b,y))
bridges.sort(key = lambda x:x[2])

q = int(input())
citizen = []
for i in range(q):
    v,w = map(int,input().split())
    citizen.append((i,v,w))
citizen.sort(key = lambda x:-x[2])

ans = [0]*q

uf = UnionFind(n+1)
for i,v,w in citizen:
    while bridges and bridges[-1][2]>w:
        a,b,c = bridges.pop()
        uf.unite(a,b)
    ans[i] = uf.get_size(v)

for a in ans:
    print(a)
