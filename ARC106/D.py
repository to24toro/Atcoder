n,k = map(int,input().split())

A = list(map(int,input().split()))
mod = 998244353
T = [[1]*n]
for i in range(1,k+1):
    t = T[-1]
    nt=[]
    for i,a in enumerate(A):
        nt.append((t[i]*a)%mod)
    T.append(nt)
S = [0]*(k+1)
for i in range(k+1):
    S[i]=sum(T[i])

frac = [1]*(k+1)
finv = [1]*(k+1)
for i in range(k):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,k+1):
    finv[k-i] = finv[k-i+1]*(k-i+1)%mod
def nCr(k,r):
    if k<0 or r<0 or k<r: return 0
    r = min(r,k-r)
    return frac[k]*finv[k-r]*finv[r]%mod
inv2=pow(2,mod-2,mod)
p = [1]
for i in range(1,k+1):
    p.append(p[-1]*2)
    p[-1]%=mod
for x in range(1,k+1):
    ans = 0
    for l in range(x+1):
        ans += nCr(x,l)*S[l]*S[x-l]
        ans %=mod
    ans-=S[x]*p[x]
    ans*=inv2
    ans%=mod
    print(ans)

