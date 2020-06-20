class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n
    
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def same(self,x,y):
        return self.find(x)==self.find(y)
    
    def size(self,x):
        return -self.parents[self.find(x)]
    
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x ==y: return 
        if self.parents[x]>self.parents[y]:
            x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

N,M = map(int,input().split())
edge = []
uf = UnionFind(N)
for i in range(M):
    a,b = map(int,input().split())
    edge.append((a-1,b-1))
ans = N*(N-1)//2
l = []
for i in range(M)[::-1]:
    l.append(ans)
    if not uf.same(edge[i][0],edge[i][1]):
        ans -= uf.size(edge[i][0])*uf.size(edge[i][1])
    uf.union(edge[i][0],edge[i][1])
print(*l[::-1], sep="\n")