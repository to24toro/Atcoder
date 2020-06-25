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
    def same(self, x, y):
        return self.find(x) == self.find(y)
N,M = map(int,input().split())
p = list(map(int,input().split()))
q = UnionFind(N)

for _ in range(M):
    x,y = map(int,input().split())
    q.union(x-1,y-1)
cnt = 0
for i in range(N):
    if q.same(i,p[i]-1):
        cnt += 1
print(cnt)
