n,k = map(int,input().split())
A = list(map(int,input().split()))
l,r = 0,10**9+1
tmp = 0
import math
while r-l>1:
    m = (r+l)//2
    cnt = 0
    for a in A:
        cnt += math.ceil(a/m)-1
    if cnt <=k:
        r = m
    else:
        l = m
print(r)
