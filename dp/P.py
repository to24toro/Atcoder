n = int(input())
g = [[] for _ in range(n)]
mod = 10**9+7
for _ in range(n-1):
    x,y = map(int,input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

def dfs(x,par):
    w,b = 1,1
    for y in g[x]:
        if y == par:continue
        cw,cb = dfs(y,x)
        w*=cw+cb
        b*=cw
    w%=mod
    b%=mod
    return w,b
print(sum(dfs(0,None))%mod)