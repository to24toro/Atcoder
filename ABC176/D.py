h,w = map(int,input().split())
a,b = map(int,input().split())
c,d = map(int,input().split())
a -= 1
b -= 1
c -= 1
d -= 1

g = []
for _ in range(h):
    s = list(input())
    tmp = []
    for i in s:
        tmp.append(i)
    g.append(tmp)
if g[c][d] =='#':print(-1);exit()
from collections import deque
q = deque([])
p  =deque([])
dp = [[float('inf')]*w for _ in range(h)]

q.append((a,b,0))
dist = [(1,0),(0,1),(0,-1),(-1,0)]
seen = [[False]*w for _ in range(h)]

dp[a][b] = 0
seen[a][b] = True

while p or q:
    while q:
        x,y,cnt = q.popleft()
        p.append((x,y,cnt+1))
        for dx,dy in dist:
            X = x+dx
            Y = y + dy
            if 0<=X<h and 0<=Y<w and not seen[X][Y] and g[X][Y]=='.':
                if dp[X][Y]>cnt:
                    dp[X][Y] = min(dp[X][Y],cnt)
                    seen[X][Y] = True
                    q.append((X,Y,cnt))
                    p.append((X,Y,cnt+1))
    while p:
        x,y,cnt = p.popleft()
        for dx in range(-2,3,1):
            for dy in range(-2,3,1):
                X = x+dx
                Y = y + dy
                if 0<=X<h and 0<=Y<w and not seen[X][Y] and g[X][Y]=='.':
                    if dp[X][Y]>cnt:
                        dp[X][Y] = min(dp[X][Y],cnt)
                        seen[X][Y] = True
                        q.append((X,Y,cnt))
    # print(dp)
print(dp[c][d] if dp[c][d]!=float('inf') else -1)



    
