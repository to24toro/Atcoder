n,m = map(int,input().split())
INF = float('inf')
D = [[INF]*n for _ in range(n)]

for _ in range(m):
    u,v,l = map(int,input().split())
    u-=1;v-=1
    D[u][v] = l
    D[v][u] = l
for i in range(n):
    D[i][i] = 0
ans = INF
for k in range(1,n):
    for i in range(1,n):
        for j in range(1,n):
            D[i][j] = min(D[i][j],D[i][k]+D[k][j])
for i in range(1,n):
    for j in range(1,n):
        if i==j:continue
        ans = min(ans,D[0][i]+D[i][j]+D[j][0])
print(ans if ans!=INF else -1)


















# n,m = map(int,input().split())
# dist = [[float('inf')]*n for _ in range(n)]

# for _ in range(m):
#     a,b,l = map(int,input().split())
#     a-=1
#     b-=1
#     dist[a][b] = l
#     dist[b][a] = l

# ans = float('inf')
# for i in range(n):
#     dist[i][i] = 0
# for k in range(1,n):
#     for i in range(1,n):
#         for j in range(1,n):
#             dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

# for i in range(1,n):
#     for j in range(i+1,n):
#         if dist[0][i] != float('inf') and dist[j][0] != float('inf'):
#             ans = min(ans,dist[0][i]+dist[j][0]+dist[i][j])
# print(ans if ans != float('inf') else -1)