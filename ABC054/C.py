n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
seen = [False]*n
seen[0] = True
ans = 0


def dfs(seen,u,cnt):
    global ans
    if cnt ==n:
        ans += 1
        return
    for v in g[u]:
        if not seen[v]:
            seen[v] = True
            dfs(seen,v,cnt+1)
            seen[v] = False
    return
for v in g[0]:
    seen[v] = True
    dfs(seen,v,2)
    seen[v] = False
print(ans)