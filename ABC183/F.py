n,q = map(int,input().split())
from collections import  defaultdict

member = [defaultdict(int) for _ in range(n)]
for i,c in enumerate(map(int,input().split())):
    member[i][c-1] = 1

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
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return x
 
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
for _ in range(q):
    t,x,y = map(int,input().split())
    x-=1
    y-=1
    if t ==1:
        x = uf.find(x)
        y = uf.find(y)
        if x!=y:
            r = uf.union(x,y)
            if r!=x:
                x,y = y,x
            for key,val in member[y].items():
                member[x][key]+= val
    else:
        print(member[uf.find(x)][y])