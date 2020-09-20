from collections import deque
n,k = map(int,input().split())
r = list(map(int,input().split()))
r.sort()
r = r[n-k:]
cur = 0
for a in r:
    if cur<a:
        cur = (cur+a)/2
    else:
        continue
print(cur)