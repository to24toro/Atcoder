N = int(input())
from copy import copy,deepcopy
dist = [list(map(int,input().split())) for _ in range(N)]
dist2 = deepcopy(dist)
seen = [[False]*N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if (i!=k and k!=j) and dist[i][j]>=dist[i][k]+dist[k][j]:
                dist[i][j]= dist[i][k]+dist[k][j]
ans = 0
for i in range(N):
    for j in range(N):
        flag = True
        if i ==j: continue
        for k in range(N):
            if i==k or j ==k: continue
            if dist2[i][j]>dist[i][k]+dist[k][j]:
                print(-1);exit()
            if dist2[i][j]==dist[i][k]+dist[k][j]:
                flag = False
                break
        if flag:
            ans += dist[i][j]
print(ans//2)