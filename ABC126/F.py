m,k = map(int,input().split())
if pow(2,m)<=k:print(-1);exit()
if m==0:
    print(0,0)
elif m==1:
    if k==0:
        print(0,0,1,1)
    else:
        print(-1)
else:
    s = []
    for i in range(2**m):
        if i!=k:
            s.append(i)
    print(k,*s,k,*s[::-1])