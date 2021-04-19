N,M = map(int,input().split())
mod = 998244353
ans = 1
n = N+M
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
ans = 1
if M==1:print(ans);exit()
if N==1:print(M);exit()
from collections import defaultdict
primes = [[] for _ in range(M+1)]
for p in range(2,M+1):
    if primes[p]:continue
    for i in range(p,M+1,p):
        primes[i].append(p)

for m in range(2,M+1):
    dic = defaultdict(int)
    val = m
    tmp = 1
    for p in primes[m]:
        cnt = 0
        while val%p==0:
            val//=p
            cnt+=1
        tmp*=nCr(N-1+cnt,cnt)
        tmp%=mod   
    ans += tmp
    ans %=mod
print(ans)
