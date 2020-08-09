n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = float('inf')
if n==1:print(0);exit()
tmp =A[0]
for i in range(1,n):
    if A[i]<=A[i-1]:
        break
    else:
        tmp = A[i]
n-=i
k-=i
A = A[i:]
for bit in range(1<<n):
    cnt = 0
    money = 0
    tmp2 = tmp
    for i in range(n):
        if ((bit>>i)&1):
            cnt += 1
            val = max(tmp2+1-A[i],0)
            money += val
            tmp2 = val+A[i]
    if cnt <k:
        continue
    else:
        ans = min(ans,money)
print(ans)

