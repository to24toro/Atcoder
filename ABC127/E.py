n,m,k = map(int,input().split())
mod = 10**9+7
N = n
n = n*m
#使えるnCr
frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+1):
    finv[n-i] = finv[n-i+1]*(n-i+1)%mod
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]*finv[n-r]*finv[r]%mod
ans = 0
#距離がdの時の2点を選んで他の選び方を決める
n = N
for i in range(1,n):
    a = (n-i)*m*m%mod
    a*=nCr(n*m-2,k-2)
    a%=mod
    ans += a*i
    ans %=mod
for i in range(1,m):
    a = (m-i)*n*n%mod
    a*=nCr(n*m-2,k-2)
    a%=mod
    ans += a*i
    ans %=mod
print(ans)