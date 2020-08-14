from collections import deque
import math
n,d,a = map(int,input().split())
F = []
for _ in range(n):
    x,h = map(int,input().split())
    F.append((x,h))
F.sort()
total = 0
d *=2
ans = 0
q = deque([])
for x,h in F:
    while q and q[0][0]<x:#累積和
        total -= q.popleft()[1]
    h-=total
    if h >0:
        tmp = math.ceil(h/a)
        ans += tmp
        damage = tmp*a
        total += damage
        q.append((x+d,damage))
print(ans)
