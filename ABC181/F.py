class UnionFind:
    def __init__(self,N):
        self.par=[i for i in range(N)]
        self.siz=[1 for _ in range(N)]
        self.rank=[0 for _ in range(N)]
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a==b:
            return 0
        else:
            if self.rank[a]>self.rank[b]:
                self.par[b]=a
                self.siz[a]+=self.siz[b]
            else:
                self.par[a]=b
                self.siz[b]+=self.siz[a]
                if self.rank[a]==self.rank[b]:
                    self.rank[b]+=1
    def size(self,a):
        return self.siz[self.find(a)]
    def same(self,a,b):
        return self.find(a)==self.find(b)
 
n=int(input())
 
point=[tuple(map(int,input().split())) for _ in range(n)]
point.append((0,100))
point.append((0,-100))

def helper(x):
    uf = UnionFind(n+2)
    for i in range(n+2):
        for j in range(i):
            if i==n+1 and j==n:
                continue
            elif i==n+1 or i==n:
                dist = abs(point[i][1]-point[j][1])
                if dist<2*x:
                    uf.union(i,j)
            else:
                x1,y1=point[i]
                x2,y2=point[j]
                dist=((x1-x2)**2+(y1-y2)**2)**0.5
                if dist <2*x:
                    uf.union(i,j)
    if uf.same(n,n+1):
        return False
    else:
        return True
l,r = -1,201
for i in range(50):
    mid = (l+r)/2
    if helper(mid):
        l = mid
    else:
        r = mid
print(l)
