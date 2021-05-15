n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u,v,w = map(int,input().split())
    u-=1
    v-=1
    w %=2
    g[u].append((v,w))
    g[v].append((u,w))

color = [-1]*n

from collections import deque
q = deque([(0,0)])
color[0]=0
while q:
    x,c = q.popleft()
    for y,w in g[x]:
        if color[y]<0:
            color[y]=(c+w)%2
            q.append((y,(c+w)%2))
        elif color[y]!=(c+w)%2:
            print(-1)
            exit()
        else:
            continue
print(*color,sep='\n')