n,k = map(int,input().split())
P = []
for _ in range(n):
    w,p = map(int,input().split())
    P.append((w,p))

l,r = 0,100
while r-l>10**-8:
    mid = (l+r)/2
    tmp = []
    for w,p in P:
        tmp.append((w*(p-mid)/100,w,p))
    tmp.sort(reverse=True)
    res = 0
    for i in range(k):
        res += tmp[i][0]
    if res>=0:
        l = mid
    else:
        r = mid
print(l)