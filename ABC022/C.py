n,m = map(int,input().split())
d = [[float('inf')]*n for _ in range(n)]
for i in range(n): d[i][i] = 0
g = [[] for _ in range(n)]
for _ in range(m):
    x,y,l = map(int,input().split())
    g[x-1].append((y-1,l))
    g[y-1].append((x-1,l))
    if x-1!=0 and y-1!=0:
        d[x-1][y-1] = l
        d[y-1][x-1] = l
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])
if len(g[0])<2: print(-1);exit()
ans = float('inf')
for i in range(len(g[0])):
    for j in range(i+1,len(g[0])):
        res = g[0][i][1] + g[0][j][1]
        ans =min(ans,res + d[g[0][i][0]][g[0][j][0]])
print(ans if ans != float('inf') else -1)

