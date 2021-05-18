n,m,l = map(int,input().split())
d = [[float('inf')]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    d[a][b]=c
    d[b][a]=c
q = int(input())
Q = [list(map(int,input().split())) for _ in range(q)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])

dd = [[float('inf')]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if d[i][j]<=l:
            dd[i][j] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            dd[i][j] = min(dd[i][j],dd[i][k] + dd[k][j])
for s,t in Q:
    s-=1
    t-=1
    print(dd[s][t]-1 if dd[s][t]!= float('inf') else -1)
