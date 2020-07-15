mod = 10**9+7
n,k = map(int,input().split())
ans = 0
for i in range(k,n+2):
    ans += (i*n-i*(i-1)+1)%mod
ans %=mod
print(ans)