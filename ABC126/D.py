n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u,v,w = map(int,input().split())
    g[u-1].append((v-1,w))
    g[v-1].append((u-1,w))
ans = [-1]*n
from collections import deque
for i in range(n):
    if ans[i]<0:
        ans[i] = 0
        q = deque([(i,0,0)])
        while q:
            u,d,c = q.popleft()
            for v,e in g[u]:
                if ans[v]<0:
                    if (d+e)%2:
                        ans[v] = 1-c
                    else:
                        ans[v] = c
                    q.append((v,0,ans[v]))
for a in ans:
    print(a)

