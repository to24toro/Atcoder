n,q = map(int,input().split())
g = [[] for _ in range(n+1)]
d = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for _ in range(q):
    p,x = map(int,input().split())
    d[p] += x
ans = [0]*(n+1)
seen = [False]*(n+1)
from collections import deque
q = deque([(1,d[1])])
while q:
    s,cost = q.popleft()
    seen[s] = True
    ans[s] += cost
    for e in g[s]:
        if not seen[e]:
            q.append((e,cost+d[e]))
# def helper(s,cost):
#     seen[s] = True
#     ans[s] += cost
#     for e in g[s]:
#         if not seen[e]:
#             helper(e,cost+d[e])
# for i in range(1,n+1):
#     if not seen[i]:
#         helper(i,d[i])
res = []
for a in ans[1:]:
    res.append(str(a))

print(' '.join(res))