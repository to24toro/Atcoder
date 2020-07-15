n,m = map(int,input().split())
g = [set() for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].add(b)
    g[b].add(a)
for i in g[0]:
    if i in g[n-1]: print('POSSIBLE');exit()
print('IMPOSSIBLE')