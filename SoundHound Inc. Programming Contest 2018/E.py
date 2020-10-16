from collections import deque
 
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, s = map(int, input().split())
    g[u].append((v, s))
    g[v].append((u, s))

val = [None]*(n+1)
val[1] = (1,0)
