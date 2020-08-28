n,m,l = map(int,input().split())
g = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    g[a][b] = c
    g[b][a] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j],g[i][k] + g[k][j])
h = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j]<=l:
            h[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            h[i][j] = min(h[i][j],h[i][k] + h[k][j])
Q = int(input())
for _ in range(Q):
    s,t = map(int,input().split())
    s -=1
    t-=1
    if h[s][t] ==float('inf'):
        print(-1)
    else:
        print(h[s][t]-1)


