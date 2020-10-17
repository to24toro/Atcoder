n = int(input())
g = [[] for _ in range(n)]
ab = []
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    ab.append((a,b))
    g[a].append(b)
    g[b].append(a)
c = list(map(int,input().split()))
c.sort(reverse=True)
from collections import deque
def bfs(i):
    dist = [-1]*n
    d = deque()
    d.append(i)
    dist[i] = c[0]
    num = 1
    ans = 0
    while d:
        v = d.popleft()
        for j in g[v]:
            if dist[j] != -1:
                continue
            dist[j] = c[num]
            ans += min(dist[v],dist[j])
            num += 1
            d.append(j)
    return dist,ans
dist,ans = bfs(1)
print(ans)
print(' '.join(map(str,dist)))