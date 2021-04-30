n,k = map(int,input().split())
ans = 0
for x in range(2,2*n+1):
    y = x-k
    if 2<=y<=2*n:
        ans += min(x-1,2*n+1-x)*min(y-1,2*n+1-y)
print(ans)