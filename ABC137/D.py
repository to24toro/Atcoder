import heapq
from collections import deque
n,m = map(int,input().split())
A = []
for _ in range(n):
    a,b = map(int,input().split())
    A.append((a,-b))
A.sort()
A = deque(A)
hq = []
ans = 0
for i in range(1,m+1):
    while A:
        if A[0][0] ==i:
            tmp = A.popleft()
            heapq.heappush(hq,tmp[1])
        else:
            break
    if len(hq) == 0:
        continue
    else:
        ans += heapq.heappop(hq)
print(-ans)
        