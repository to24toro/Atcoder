n,m,t = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
cur = 0
if A[0]-cur>m:
    ans += A[0]-cur-m
    cur = A[0]
for i in range(1,n):
    if A[i]-cur>2*m:
        ans +=A[i]-cur-2*m
    cur = A[i]
ans += max(0,t-cur-m)
print(ans)