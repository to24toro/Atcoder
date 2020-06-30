H,W = map(int,input().split())
S =[]
for _ in range(H):
    a = input()
    S.append(a)
count =0
for i in range(H):
    for j in range(W):
        if S[i][j] =='.':
            count += 1
from collections import deque

seen = [[False]*(W) for _ in range(H)]
seen[0][0] = True
dq = deque([(0,0,1)])
d = [(1,0),(0,1),(0,-1),(-1,0)]
while dq:
    x,y,cnt = dq.popleft()
    if x ==H-1 and y ==W-1:
        print(count-cnt);exit()
    for dx,dy in d:
        if 0<=x+dx<H and 0<=y+dy<W and seen[x+dx][y+dy] ==False and S[x+dx][y+dy]=='.':
            seen[x+dx][y+dy] = True
            dq.append((x+dx,y+dy,cnt+1))
print(-1)