n = int(input())
a = list(map(int,input().split()))
from collections import defaultdict
d = defaultdict(int)
for i in a:
    d[i] += 1
for i in range(1,n+1):
    print(d[i])
