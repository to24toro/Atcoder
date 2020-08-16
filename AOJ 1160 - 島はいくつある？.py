w,h = map(int,input().split())
d = []
for _ in range(h):
    d.append(list(map(int,input().split())))
seen = [[False]*w for _ in range(h)]
dist = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
def dfs(i,j):
    if not seen[i][j]:
        seen[i][j] = True
        for x,y in dist:
            X = x + i
            Y = y + j
            if 0<=X<h and 0<=Y<w and not seen[X][Y] and d[X][Y]==1:
                dfs(X,Y)
cnt = 0
for i in range(h):
    for j in range(w):
        if d[i][j] ==0:
            seen[i][j] = True
        elif not seen[i][j]:
            cnt += 1
            dfs(i,j)
print(cnt)
