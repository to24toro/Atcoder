n = int(input())
D = []
for _ in range(n):
    x,y = map(int,input().split())
    D.append((x,y))
D.sort()
set_ = set(D)
ans = 0
from itertools import combinations
for p1,p2 in combinations(D,2):
    x1,y1 = p1
    x2,y2 = p2
    if (x2+y2-y1,y2+x1-x2) in set_ and (x1+y2-y1, y1+x1-x2) in set_:
        ans = max(ans,(x1-x2)**2 + (y1-y2)**2)
print(ans)
