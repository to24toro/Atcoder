n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
M = []
for _ in range(m):
    b,c = map(int,input().split())
    M.append((b,c))
M.sort(key = lambda x:-x[1])
from collections import deque
q = deque(M)
s = 0
f = True
while s<n and q and f:
    b,c = q.popleft()
    cnt = 1
    while s<n and cnt<=b:
        if c>A[s]:
            A[s] = c
            s+=1
            cnt+=1
        else:
            f = False
            break

print(sum(A))


