def dfs(v,t,f,used,graph):
    if v ==t: return f
    used[v] = True
    for to in graph[v]:
        c = graph[v][to]
        if used[to] or c==0:
            continue
        d = dfs(to,t,min(f,c),used,graph)
        if d>0:
            graph[v][to] -= d
            graph[to][v] += d
            return d
    return 0

def max_flow(s,t,graph):
    flow = 0
    while True:
        used = [False]*len(graph)
        f = dfs(s,t,float('inf'),used,graph)
        flow += f
        if f==0:
            return flow
n,g,e = map(int,input().split())
p = list(map(int,input().split()))
graph = [{} for _ in range(n+1)]

for i in range(g):
    graph[p[i]][n] = 1
    graph[n][p[i]] = 0

for i in range(e):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

ans = max_flow(0,n,graph)
print(ans)