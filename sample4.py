n = int(input())
H =list(map(int,input().split()))
from collections import deque
ans = 0
q = deque([(0,-1)])
for i in range(n):
    h = H[i]
    base = i
    while q and h<=q[-1][0]:
        h0,j = q.pop()
        ans = max(ans,h0*(i-j))
        base = j
    q.append((h,base))#左側にも広げる
while q:
    h,j = q.pop()
    ans = max(ans,h*(n-j))
print(ans)