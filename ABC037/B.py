n,q = map(int,input().split())
A = [0]*n
for _ in range(q):
    l,r,t = map(int,input().split())
    l-=1
    r-=1
    for i in range(l,r+1):
        A[i]=t
for a in A:
    print(a)