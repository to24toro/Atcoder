mod = 10**9+7
n,k = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
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
maxv = 0
for i,a in enumerate(A):
    maxv += nCr(i,k-1)*a
    maxv %=mod
minv = 0
for i,a in enumerate(A):
    minv += nCr(n-i-1,k-1)*a
    minv %= mod
print((maxv-minv)%mod)