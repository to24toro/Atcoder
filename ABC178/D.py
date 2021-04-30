mod = 10**9+7
s = int(input())
n = 2*s
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
if s<3:print(0);exit()
ans = 0
for i in range(1,s//3+1):
    t=s-3*i
    ans += nCr(t+i-1,t)
    ans %=mod
print(ans)
