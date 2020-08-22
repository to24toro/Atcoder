n,m = map(int,input().split())
A  =list(map(int,input().split()))
A.sort(reverse =True)
from copy import deepcopy
def cnt(x):
    r = 0
    ans = 0
    l = [0]*n
    for i in range(n-1,-1,-1):
        while r < n and A[r] + A[i] >=x:
            r += 1
        l[i] = r
        ans += r
    return [ans,l]
l,r = 0,2*(10**6)

while l < r:
    mid = (l+r)//2
    if cnt(mid)[0]<=m:
        r = mid
    else:
        l = mid+1
s = [0] + deepcopy(A)
for i in range(n):
    s[i+1] += s[i]
ans = 0
plus = cnt(l)[1]
