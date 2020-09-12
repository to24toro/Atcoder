n,k = map(int,input().split())
A = list(map(int,input().split()))
ans,cnt = 0,0
tmp = 0
for a in A:
    while cnt < k:
        if tmp>=n:
            break
        cnt +=A[tmp]
        tmp += 1
    else:
        ans += n-tmp+1
    cnt-=a
print(ans)