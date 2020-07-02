N,M = map(int,input().split())
from collections import deque
g = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

dist = [float('inf')]*(N)
ans = [0]*N
dist[0] = 0
q = deque([])
q.append((0,0))
while q:
    idx,d = q.popleft()
    for nxt in g[idx]:
        if d + 1 < dist[nxt]:
            ans[nxt] = idx+1
            dist[nxt] = d+1
            q.append((nxt,d+1))
for i in range(N):
    if dist[i]==float('inf'):
        print('No');exit()
print('Yes')
for i in range(1,N):
    print(ans[i])
