n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = float('inf')
for i in range(n-k+1):
    l,r = A[i],A[i+k-1]
    cost = 0
    if l<=0 and r<=0:
        cost = abs(l)
    elif l>=0 and r>=0:
        cost = abs(r)
    else:
        cost = 2*min(abs(l),abs(r)) + max(abs(r),abs(l))
    ans = min(ans,cost)
print(ans if ans != float('inf') else 0)
