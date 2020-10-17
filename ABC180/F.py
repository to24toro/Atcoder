mod = 10**9+7
n,m,l = map(int,input().split())
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

if m<l-1:print(0)
m-=l-1
res = 0
for i in range(1,n-l):
    tmp = nCr(n-l,i)
    p=n-l-i
    tmp2 = 0
    for j in range(p):
        if 2*(j+1)>p:continue
        tmp3 = nCr(p,2*(j+1))*frac[2*(j+1)]
        q = p-(j+1)*2
        r = m-(j+1)
        if q<0: continue
        if r==q-1-j:
            tmp2 +=tmp3*nCr(q+j,j)//pow(2,j+1)
    res += tmp*tmp2

if res==0:
    res = 1
ans = frac[l]*nCr(n,l)*res
if l!=1:ans//=2
ans %=mod
print(ans)


