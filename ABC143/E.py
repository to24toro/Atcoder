n,m,l = map(int,input().split())
INF = float('inf')
d = [[INF]*n for _ in range(n)]

for i in range(n):d[i][i] = 0
for i in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    d[a][b] = c
    d[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])
# print(d)
dd = [[INF]*n for _ in range(n)]
for i in range(n):dd[i][i] = 0
for i in range(n):
    for j in range(n):
        if d[i][j]<=l:
            dd[i][j] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            dd[i][j] = min(dd[i][j],dd[i][k]+dd[k][j])
q = int(input())
for _ in range(q):
    s,t = map(int,input().split())
    s-=1
    t-=1
    print(dd[s][t]-1 if dd[s][t] !=INF else -1)

