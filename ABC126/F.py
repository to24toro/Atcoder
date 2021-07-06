m,k = map(int,input().split())
if pow(2,m)<=k:print(-1);exit()
if m==0:
    print(0,0)
elif m==1:
    if k==1:
        print(-1)
    else:
        print(0,0,1,1)
else:
    b = []
    for i in range(pow(2,m)):
        if i==k:
            continue
        b.append(i)
    print(k,*b,k,*b[::-1])

