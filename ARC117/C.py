n = int(input())
C = input()
D = []
for c in C:
    if c=='W':
        D.append(0)
    elif c=='R':
        D.append(1)
    else:
        D.append(2)
mod = 3
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
s = 1
f = -1 if n%2==0 else 1
for i,d in enumerate(D):
    s*=
    ans+=nCr(n-1,i)*d
    print(ans,nCr(n-1,i))
    ans%=mod
ans*=f
if ans%mod==0:
    print('W')
elif ans%mod==1:
    print('R')
else:
    print('B')