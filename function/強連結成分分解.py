#強連結成分分解
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
        group[s] = col
        used[s] = 1
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
            if lbs==lbt:continue
            g0[lbs].add(lbt)
        gp[lbs].append(v)
    return g0,gp
