ax,ay,bx,by = map(int,input().split())
n = int(input())
def helper(ax,ay,bx,by,x,y):
    ans = (by-ay)*(x-ax)-(bx-ax)*(y-ay)
    return 1 if ans>0 else -1
cnt = 0
L = []
for i in range(n):
    x,y = map(int,input().split())
    L.append((x,y))
L.append(L[0])
for i in range(n):
    if helper(ax,ay,bx,by,L[i][0],L[i][1])*helper(ax,ay,bx,by,L[i+1][0],L[i+1][1])<0 and helper(L[i][0],L[i][1],L[i+1][0],L[i+1][1],ax,ay)*helper(L[i][0],L[i][1],L[i+1][0],L[i+1][1],bx,by)<0:
        cnt += 1
print(1+cnt//2)