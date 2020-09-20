r,c = map(int,input().split())
x,y = map(int,input().split())
d,l = map(int,input().split())
mod = 10**9+7
XY = (r-x+1)*(c-y+1)
n= 1000
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

ng = 0
ng += 2*nCr((x-1)*y,d+l) + 2*nCr((x*(y-1)),d+l)
ng-= 4*nCr((x-1)*(y-1),d+l) + nCr((x-2)*y,d+l) + nCr(x*(y-2),d+l)
ng += 2*nCr((x-2)*(y-1),d+l) + 2*nCr((x-1)*(y-2),d+l)
if x>1 and y>1:
    ng-=nCr((x-2)*(y-2),d+l)

ans = nCr(x*y,d+l)-ng
ans *= XY
ans *= nCr(d+l,d)
ans %=mod
print(ans)
