n = int(input())
g = [[]*(n) for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
ds = [0]*n
de = [0]*n
from collections import deque
def bfs(s,d):
    q = deque()
    q.append((s,1))
    visit = [False]*n
    visit[s] = True
    cnt =1
    while q:
        s,p = q.popleft()
        if cnt==n: break
        for i in g[s]:
            if not visit[i]:
                d[i] = p
                visit[i] = True
                cnt += 1
                q.append((i,p+1))
bfs(0,ds)
bfs(n-1,de)
s,e=0,0
for i in range(n):
    if ds[i]<=de[i]:
        s+=1
    else:
        e+=1
if s>e:
    print('Fennec')
else:
    print('Snuke')

