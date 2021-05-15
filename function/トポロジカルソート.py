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

