import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n,m = map(int,input().split())
g = [[] for _ in range(n)]
rg = [[] for _ in range(n)]
for _ in range(m):
    s,t = map(int,input().split())
    g[s].append(t)
    rg[t].append(s)
def scc(n,g,rg):
    order = []
    used = [0]*n
    group = [None]*n
    def dfs(s):
        used[s] = 1
        for t in g[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s,col):
        used[s] = 1
        group[s] = col
        for t in rg[s]:
            if not used[t]:
                rdfs(t,col)
    for i in range(n):
        if not used[i]:
            dfs(i)
    used = [0]*n
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s,label)
            label += 1
    return label, group
def construct(n,g,label,group):
    g0 = [set() for i in range(label)]
    gp = [[] for i in range(label)]
    for v in range(n):
        lbs = group[v]
        for w in g[v]:
            lbt = group[w]
            if lbt ==lbs:continue
            g0[lbs].add(lbt)
        gp[lbs].append(v)
    return g0,gp
_,group = scc(n,g,rg)
q = int(input())
for _ in range(q):
    u,v = map(int,input().split())
    print(1 if group[u]==group[v] else 0)
