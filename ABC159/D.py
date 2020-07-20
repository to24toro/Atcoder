n = int(input())
A = list(map(int,input().split()))
from collections import Counter
cnt = Counter(A)
ans = 0
for key,val in cnt.items():
    if val>=2:
        ans += val*(val-1)//2
for a in A:
    cur = ans
    if cnt[a]>=2:
        cur -= cnt[a]-1
    print(cur)