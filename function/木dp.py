def dfs(i,pre,rest):
    res = rest
    used = 1
    for j in g[i]:
        if i!=j:
            res*=dfs(j,i,k-used)
            used+=1
    return res

# bfsについてはABC133E