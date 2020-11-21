n,m = map(int,input().split())
seen = [False]*n
g = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))
from collections import deque
ans = [-1]*n
q = deque([(0,1)])
ans[0]=1
while q:
    u,idx = q.popleft()
    for v,label in g[u]:
        if label==idx:
            if ans[v]==-1:
                ans[v] = idx + 1 if idx==1 else idx-1
                q.append((v,ans[v]))
            else:
                continue
        else:
            if ans[v]==-1:
                ans[v]=label
                q.append((v,ans[v]))
            else:
                continue
for a in ans:
    print(a)
