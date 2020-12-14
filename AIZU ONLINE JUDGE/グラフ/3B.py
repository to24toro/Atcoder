def low_links(nodes):
    N = len(nodes)
    visited = [False]*N
    prenum = [0]*N
    parent =[0]*N
    lowest = [0]*N
    bridges = []
    timer = 1
    def rec(cur,prev,timer):
        prenum[cur] = lowest[cur]=timer
        timer += 1
        visited[cur] = True
        for nxt in nodes[cur]:
            if not visited[nxt]:
                parent[nxt] = cur
                timer = rec(nxt,cur,timer)
                lowest[cur]=min(lowest[cur],lowest[nxt])
                if lowest[nxt]==prenum[nxt]:
                    bridges.append((min(cur,nxt),max(cur,nxt)))
            elif nxt!=prev:
                lowest[cur] = min(lowest[cur],prenum[nxt])
        return timer
    for i in range(N):
        if not visited[i]:
            timer =rec(i,-1,timer)
    aps = set()
    np = 0
    for i in range(1,N):
        p = parent[i]
        if p==0:
            np+=1
        elif prenum[p]<=lowest[i]:
            aps.add(p)
    if np>1:
        aps.add(0)
    return aps,bridges
# N,M = map(int,input().split())
# nodes = [[] for _ in range(N)]
# for _ in range(M):
#     u,v = map(int,input().split())
#     nodes[u].append(v)
#     nodes[v].append(u)
# aps,bridges = low_links(nodes)
# bridges = sorted(bridges)
# for x in bridges:
#     print(*x)
N, M = map(int,input().split())
nodes = [[] for i in range(N)]
for i in range(M):
    u, v = map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)

aps, bridges = low_links(nodes)

bridges = sorted(bridges)
for x in bridges:
    print(*x)