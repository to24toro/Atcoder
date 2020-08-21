n,k,m = map(int,input().split())
A = list(map(int,input().split()))
val = m*(n-1)-sum(A)
if m + val<=0:
    print(0)
elif m+val <=k:
    print(m+val)
else:
    print(-1)