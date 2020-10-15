n,g,e = map(int,input().split())
P = lsit(map(int,input().split()))
g  =[set() for _ in range(n)]
for _ in range(e):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].add(b)
    g[b].add(a)
cnt = 0
for p in P:
    if p-1 in g[0]:
        cnt += 1