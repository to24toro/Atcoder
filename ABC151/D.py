h,w = map(int,input().split())
g = []
for _ in range(h):
    S = input()
    tmp = [str(i) for i in S]
    g.append(tmp)
from collections import deque
# print(g)
dp = [[0]*w for _ in range(h)]
def dfs(i,j):
    seen = [[False]*w for _ in range(h)]
    seen[i][j] = True
    q = deque([])
    q.append((i,j,0))
    dist=[(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x,y,cnt = q.popleft()
        for dx,dy in dist:
            if 0 <=x+dx<h and 0<=y+dy<w and seen[x+dx][y+dy]==False and g[x+dx][y+dy]=='.':
                seen[x+dx][y+dy] = True
                q.append((x+dx,y+dy,cnt+1))
    return cnt
ans = 0
for i in range(h):
    for j in range(w):
        if g[i][j] =='.':
            ans =max(ans,dfs(i,j))
print(ans)