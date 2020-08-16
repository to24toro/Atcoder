m = int(input())
n = int(input())
A =[]
for _ in range(n):
    A.append(list(map(int,input().split())))
seen = [[False]*m for _ in range(n)]
dist = [(1,0),(0,1),(-1,0),(0,-1)]
ans = 0
def dfs(i,j,cnt):
    global ans
    ans = max(ans,cnt)
    for dx,dy in dist:
        x = i+dx
        y = j+dy
        if 0<=x<n and 0<=y<m and A[x][y] ==1 and not seen[x][y]:
            seen[x][y] = True
            dfs(x,y,cnt+1)
            seen[x][y] = False
for i in range(n):
    for j in range(m):
        if A[i][j]==1:
            dfs(i,j,0)

print(ans)
