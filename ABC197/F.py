n,m = map(int,input().split())
g = [[]*n for _ in range(n)]
char = [[None]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(str,input().split())
    a = int(a)-1
    b = int(b)-1
    char[a][b]=c
    char[b][a]=c
    g[a].append(b)
    g[b].append(a)
dist = [[-1]*n for _ in range(n)]
dist[0][n-1]=0
q = [(0,n-1)]
for i,j in q:
    for x in g[i]:
        for y in g[j]:
            if char[i][x]==char[j][y] and dist[x][y]==-1:
                dist[x][y]=dist[i][j]+1
                q.append((x,y))
print(dist[n-1][0])