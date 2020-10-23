n = int(input())
ans = float('inf')
for i in range(1,n+1):
    m = n%i + abs(i-n//i)
    ans = min(ans,m)
print(ans)
