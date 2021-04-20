n,k = map(int,input().split())
A = list(map(int,input().split()))
from collections import Counter
count = Counter(A)
now = k
ans = 0
for i in range(n+1):
    v = count[i]
    if v>=k:
        continue
    else:
        k = v
    ans += i*(now-v)
    now = v
    if now<=0:
        break
print(ans)