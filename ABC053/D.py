n = int(input())
A = list(map(int,input().split()))
from collections import Counter
cnt = Counter(A)
chk = 0
ans = 0
for a in cnt:
    if cnt[a]%2==0:
        chk += 1
    else:
        ans += 1
if chk%2:
    chk-=1
print(ans+chk)