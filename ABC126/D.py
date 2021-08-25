n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    a-=1;b-=1
    g[a].append((c,b))
    g[b].append((c,a))

s = [-1]*n
from collections import deque
q = deque([(0,0)])
s[0] = 0
while q:
    color,x = q.popleft()
    for d,y in g[x]:
        if s[y]==-1:
            if d%2:
                s[y]=1-color
                q.append((1-color,y))
            else:
                s[y]=color
                q.append((color,y))
print(*s,sep='\n')