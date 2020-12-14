n,m = map(int,input().split())
g = [[] for _ in range(n)]
from collections import defaultdict
in_cnt = defaultdict(int)
for _ in range(m):
    s,t = map(int,input().split())
    g[s].append(t)
    in_cnt[t]+=1

def topological_sort(n,g,in_cnt):
    res = []
    from collections import deque
    queue = deque([i for i in range(n) if in_cnt[i]==0])
    while len(queue)!=0:
        u = queue.popleft()
        res.append(u)
        for v in g[u]:
            in_cnt[v]-=1
            if in_cnt[v]==0:
                queue.append(v)
    return res
res = topological_sort(n,g,in_cnt)
for r in res:
    print(r)
