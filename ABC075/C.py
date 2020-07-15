n,m = map(int,input().split())
g = [[]*(n+1) for _ in range(n+1)]
d = []
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    d.append([a,b])
seen = [False]*(n+1)
seen[0]=True
def dfs(s):
    seen[s]=True
    for e in g[s]:
        if not seen[e]:
            dfs(e)
cnt = 0
for i in range(m):
    a,b = d[i]
    g[a].remove(b)
    g[b].remove(a)
    dfs(1)
    for i in range(n+1):
        if not seen[i]:
            cnt += 1
            break
    seen = [False]*(n+1)
    seen[0]=True
    g[a].append(b)
    g[b].append(a)
print(cnt)