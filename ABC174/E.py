n,k = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
M = max(A)
l,r = 1,M
cnt = 0
while l<=r:
    cnt = 0
    mid = (l+r)//2
    for a in A:
        tmp= a//mid if a>mid else 0 #a==midの時+1されるのを回避する
        cnt += tmp
    if cnt <=k:
        r = mid-1
    else:
        l = mid+1
print(l)
