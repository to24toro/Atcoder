n,m,t = map(int,input().split())
A = list(map(int,input().split()))
g = [[] for _ in range(n)]
f = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    f[b].append((a,c))

go = [float('inf')]*n
come = [float('inf')]*n
seen = [False]*n

from collections import deque
q = deque([(0,0)])
go[0]=0
while q:
    x,base = q.popleft()
    for y,cost in g[x]:
        if go[y]>base+cost:
            go[y] = base+cost
            q.append((y,base+cost))
q = deque([(0,0)])
come[0]= 0
while q:
    x,base = q.popleft()
    for y,cost in f[x]:
        if come[y]>base+cost:
            come[y] = base+cost
            q.append((y,base+cost))
ans = 0
for i,a in enumerate(A):
    if go[i]>=0 and come[i]>=0:
        ans = max(ans,a*(t-go[i]-come[i]))

print(ans)