mod = 10**9+7
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(b-1)

from collections import deque
seen = [False]*n
q = deque([(0,1,1)])
seen[0] = True
ans =1
while q:
    x,w,b = q.popleft()
    f = True
    for y in g[x]:
        if not seen[y]:
            f = False
            seen[y] = True
            q.append((y,w+b,w))
    if f:
        ans *=(w+b)
print(ans)