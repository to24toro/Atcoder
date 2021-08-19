n,k = map(int,input().split())
A = list(map(int,input().split()))

l,r = 0,10**9+1

while r-l >1:
    m = (r+l)//2
    cnt = 0
    for a in A:
        cnt += (a-1)//m
    if cnt>k:
        l = m
    else:
        r = m
print(r)