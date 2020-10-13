n = int(input())
a,b = map(int,input().split())
a-=1
b-=1

m = int(input())
g = [[] for _ in range(n)]
for _ in range(m):
    x,y = map(int,input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

mod = 10**9+7
from collections import deque
d = [float('inf')]*n
d1= [0]*n
d[a] = 0
d1[a] = 1
q = deque([a])
def bfs(s):
    while s:
        v  = s.popleft()
        c = d[v]
        for i in g[v]:
            if d[i]>c+1:
                d[i] = c+1
                d1[i] = d1[v]
                s.append(i)
            elif d[i] == c+1:
                d1[i] += d1[v]
bfs(q)
print(d1[b]%mod)
