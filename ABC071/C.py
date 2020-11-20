n = int(input())
A = list(map(int,input().split()))
from collections import Counter
cnt = Counter(A)
d = []
for k,v in cnt.items():
    if v>=2:
        d.append((k,v))
if len(d)<2:print(0)
else:
    d.sort(reverse = True)
    if d[0][1]>=4:
        print(d[0][0]**2)
    else:
        print(d[0][0]*d[1][])