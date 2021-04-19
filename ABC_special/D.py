mod = 10**9+7
n,p = map(int,input().split())
ans = 1
ans*=p-1
if n>=2:
    ans*=pow(p-2,n-1,mod)
print(ans%mod)