n,m = map(int,input().split())
from collections import deque
g = [[] for _ in range(n)]
for i in range(m):
    l,r,d = map(int,input().split())
    l-=1
    r-=1
    g[l].append((r,d))
    g[r].append((l,-d))
INF = float('inf')
s = [INF]*n
for i in range(n):
    if s[i] ==INF:
        s[i] = 0
        q = deque([(i,0)])
        while q:
            x,c = q.popleft()
            for y,cc in g[x]:
                if s[y]!=INF and s[y] !=c+cc:
                    print('No');exit()
                if s[y]==INF:
                    s[y] = c+cc
                    q.append((y,c+cc))
print('Yes')