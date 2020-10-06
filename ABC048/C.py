n,x = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
cur = A[0]
if cur > x:
    ans += cur-x
    cur = x
for i in range(1,n):
    if cur+A[i]>x:
        y = cur + A[i] - x
        ans += y
        A[i] = max(0,A[i]-y)
    cur = A[i]
print(ans)