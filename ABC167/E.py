N,M,K = map(int,input().split())
mod = 998244353
n = 200050
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


# M* n-1Ck*1^k*(M-1)^(N-1-k)
ans = 0
for i in range(K+1):
    tmp=(M*nCr(N-1,i))%mod
    tmp*=pow(M-1,N-1-i,mod)
    ans += tmp%mod
print(ans%mod)