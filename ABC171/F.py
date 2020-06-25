k = int(input())
s = input()

mod = 10**9+7
n = len(s) + k

frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+1):
    finv[n-i] = finv[n-i+1]*(n-i+1)%mod
def nCr(n,r,m):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]*finv[n-r]*finv[r]%mod
a,b = [1],[1]
for _ in range(k+1):
    a.append(a[-1]*25%mod)
    b.append(b[-1]*26%mod)
n = len(s)
ans = 0
for i in range(k+1):
    ans += a[i]*b[k-i]*nCr(i+n-1,n-1,mod)
    ans %= mod
print(ans)