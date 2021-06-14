class LCA():
    """
    木の最小共通祖先(Least Common Ancestor)をダブリングで求める。
    頂点番号が0, 1, ..., n-1で与えられた木のrepnを入力としてインスタンス化、2頂点を入力してLCAを返す。
    """
    def __init__(self, repn):
        import sys
        sys.setrecursionlimit(10**8)
        self.n = len(repn)
        self.repn = repn
        self.log_depth = len(bin(self.n - 1)[2:])
        self.parent = [[-1] * self.n for _ in range(self.log_depth)]  # parent[k][v] = (頂点vから2^k上の親)
        self.depth = [0] + [-1] * (self.n - 1)  # 根（頂点0）からの距離
        
        # dfs
        def dfs(v, p, d):
            for nv in repn[v]:
                if nv == p: continue
                self.parent[0][nv] = v
                self.depth[nv] = d + 1
                dfs(nv, v, d + 1)
        
        dfs(0, -1, 0)
        # doubling preprocess
        for k in range(self.log_depth - 1):
            for v in range(self.n):
                if self.parent[k][v] < 0:
                    self.parent[k + 1][v] = -1
                else:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]
 
    def __call__(self, u, v):
        if self.depth[u] < self.depth[v]: u, v = v, u
        for k in range(self.log_depth):
            if ((self.depth[u] - self.depth[v]) >> k & 1):
                u = self.parent[k][u]
 
        if u == v: return u
        for k in range(self.log_depth - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
 
        return self.parent[0][u]
import sys
sys.setrecursionlimit(10**6)

readline = sys.stdin.readline
write = sys.stdout.write
n = int(readline())
g = [[] for _ in range(n)]
for i in range(n):
    a = list(map(int,readline().split()))
    for j in range(1,len(a)):
        g[i].append(a[j])
        # g[a[j]].append(i)
tree =LCA(g)
ans = []
q = int(input())
for _ in range(q):
    u,v = map(int,input().split())
    ans.append(tree(u,v))
print(*ans,sep='\n')
