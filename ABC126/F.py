m,k = map(int,input().split())
if k>=pow(2,m):print(-1);exit()
if m ==0:
    if k==0:
        print(0,0)
    else:
        print(-1)
elif m ==1:
    if k ==0:
        print(0,0,1,1)
    else:
        print(-1)
else:
    tmp = []
    for i in range(1<<m):
        if i!=k:
            tmp.append(i)
    tmp2 = tmp[::-1]
    ans = [str(a) for a in tmp+[k]+tmp2+[k]]
    print(' '.join(ans))