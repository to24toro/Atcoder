n,k = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))
A.sort()
F.sort(reverse=True)
l,r = 0,10**12+1
while l <r:
    mid = (l+r)//2
    cnt = 0
    for a,f in zip(A,F):
        cnt += max(0,a-mid//f)
    if cnt <=k:
        r = mid
    else:
        l = mid+1
print(l)