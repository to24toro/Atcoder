N = int(input())
from collections import Counter
A = Counter(list(map(int,input().split())))
cnt = 0
for key,val in A.items():
   if val>=key: cnt += min(val-key,val)
   else:
       cnt += val
print(cnt)