n,m = map(int,input().split())
if m<0 or m==n:
    print(-1);exit()

if m==0:
    for i in range(1,2*n,2):
        print(i,i+1)
    exit()
if 1<=m<=n-2:
    cnt=0
    i=2
    while cnt!=m+1:
        print(i,i+1)
        i+=2
        cnt+=1
    print(1,i)
    i+=1
    for _ in range(n-m-2):
        print(i,i+1)
        i+=2
    exit()

print(-1)