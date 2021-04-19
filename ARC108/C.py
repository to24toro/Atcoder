n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u,v,c = map(int,input().split())
    u-=1
    v-=1
    g[u].append((v,c))
    g[v].append((u,c))

from collections import deque
cnt = 1
q = deque([(0,1,cnt)])
seen = [-1]*n
seen[0]=cnt
while q:
    s,color,cnt = q.popleft()
    for t,c in g[s]:
        if seen[t]<0:
            if color!=c:
                seen[t]=c
                q.append((t,c,cnt))
            else:
                if cnt==color:
                    cnt=2
                seen[t] = cnt
                q.append((t,cnt,1))
for i in seen:
    if i<0:print('No')
print(*seen,sep = '\n')