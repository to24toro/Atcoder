
N = int(input())
P = list(map(int,input().split()))
from collections import deque
ans = 0
cost = [min(i,N-1-i,j,N-1-j) for i in range(N) for j in range(N)]
s = [1]*(N**2)
d = [1,N,-1,-N]
for p in P:
    p-=1
    ans += cost[p]
    s[p]=0
    q = deque()
    q.append(p)
    while q:
        x = q.popleft()
        c = cost[x]+s[x]
        for dd in d:
            y = x+dd
            if 0<=y<N**2 and cost[y]>c:
                cost[y] = c
                q.append(y)
print(ans)