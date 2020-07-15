n = int(input())
a = list(map(int,input().split()))
ans = float('inf')
for i in range(1,n):
    a[i] += a[i-1]
for i in range(n-1):
    x = a[i]
    y = a[-1]-a[i]
    ans = min(ans,abs(x-y))
print(ans)