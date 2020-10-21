h,w,n = map(int,input().split())
L = []
from collections import defaultdict
dic = defaultdict(int)
for _ in range(n):
    a,b = map(int,input().split())
    a-=1
    b-=1
    L.append((a,b))
dx = [1,1,1,0,0,0,-1,-1,-1]
dy = [1,0,-1,1,0,-1,1,0,-1]
for x,y in L:
    for i in range(9):
        nx,ny = x+dx[i],y+dy[i]
        if 2<=nx<=h-1 and 2<=ny<=w-1:
            dic[nx*w+ny] += 1

ans = [(h-2)*(w-2),0,0,0,0,0,0,0,0,0]
for k in dic:
  ans[0] -= 1
  ans[dic[k]] += 1
print(*ans,sep="\n")