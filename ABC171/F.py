k = int(input())
S = input()
N = len(S)
A = [1,25]
B = [1,26]
mod = 10**9+7
for i in range(k+1):
    A.append((A[-1]*25)%mod)
for j in range(k+1):
    B.append((B[-1]*26)%mod)
n = N+k
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
for i in range(k+1):
    ans += B[i]*A[k-i]*nCr(N-1+k-i,N-1)
    ans%=mod
print(ans)