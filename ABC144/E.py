n,k = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))
F.sort()
A.sort(reverse=True)

l,r = -1,10**12+1
while r-l>1:
    m = (r+l)//2
    res = 0
    for i in range(n):
        a = A[i]
        f = F[i]
        if a*f-m>0:
            res += (a*f-m-1)//f + 1
    if res>k:
        l = m
    else:
        r = m
print(r)