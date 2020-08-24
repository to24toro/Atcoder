n = int(input())
A = list(map(int,input().split()))
from collections import deque
q = deque(A)
i = 1
ans = []
while i <= n and q:
    a = q.popleft()
    if a==i:
        ans.append(a)
        i += 1
if len(ans)==0:
    print(-1)
else:
    print(n-len(ans))

