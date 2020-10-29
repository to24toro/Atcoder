# h,w,n = map(int,input().split())
# L = []
# from collections import defaultdict
# dic = defaultdict(int)
# for _ in range(n):
#     a,b = map(int,input().split())
#     a-=1
#     b-=1
#     L.append((a,b))
# dx = [1,1,1,0,0,0,-1,-1,-1]
# dy = [1,0,-1,1,0,-1,1,0,-1]
# for x,y in L:
#     for i in range(9):
#         nx,ny = x+dx[i],y+dy[i]
#         if 2<=nx<=h-1 and 2<=ny<=w-1:
#             dic[nx*w+ny] += 1

# ans = [(h-2)*(-2),0,0,0,0,0,0,0,0,0]
# for k in dic:
#   ans[0] -= 1
#   ans[dic[k]] += 1
# print(*ans,sep="\n")
H,W,N = map(int,input().split())
from collections import defaultdict
dic = defaultdict(int)
dx = [1,1,1,0,0,0,-1,-1,-1]
dy = [1,0,-1,1,0,-1,1,0,-1]
for _ in range(N):
    a,b = map(int,input().split())
    a-=1
    b-=1
    for i in range(9):
        X = a+dx[i]
        Y = b+dy[i]
        if 0<=X<H and 0<=Y<W:
            dic[(X,Y)] += 1
ans = [(H-2)*(W-2),0,0,0,0,0,0,0,0,0]

for cnt in dic:
    if 0<cnt[0]<H-1 and 0<cnt[1]<W-1:
        ans[0]-=1
        ans[dic[cnt]]+=1
for a in ans:
    print(a)
