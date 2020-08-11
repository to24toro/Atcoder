m = int(input())
M = [tuple(map(int,input().split())) for i in range(m)]
n = int(input())
N = [tuple(map(int,input().split())) for i in range(n)]
set_ = set(N)
for i in range(n):
    dx = N[i][0]-M[0][0]
    dy = N[i][1]-M[0][1]
    flag = False
    for j in range(1,m):
        if (M[j][0] + dx,M[j][1] + dy) not in set_:
            flag = True
            break
    if not flag:
        print(dx,dy);exit()