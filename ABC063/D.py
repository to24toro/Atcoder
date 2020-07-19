n,a,b = map(int,input().split())
s = 0
H = []
for _ in range(n):
    h = int(input())
    H.append(h)
from copy import deepcopy

from math import ceil
def count(x):
    Hc = deepcopy(H)
    cnt = 0
    for i in range(n):
        Hc[i] -= b*x
        if Hc[i]>0:
            cnt += ceil(Hc[i]/(a-b))
    return cnt <= x

l,r = 0, max(H)//b + 1
while l < r:
    mid = (l+r)//2
    if count(mid):
        r = mid
    else:
        l = mid+1
print(r)