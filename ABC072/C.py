n = int(input())
a = list(map(int,input().split()))
from collections import Counter
d = Counter(a)
ans = 0
for key,val in d.items():
    ans = max(ans,d[key]+d[key-1]+d[key+1])
print(ans)