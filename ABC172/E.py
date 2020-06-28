N,M = map(int,input().split())
v = min(N,M-N)
dp = [0]*(N+1)

mod = 10**9+7
frac = [1]*(max(M,N)+10)
num=len(frac)
for i in range(num-1):
    frac[i+1] = frac[i]*(i+1)%mod
finv = [1]*(max(M,N)+10)
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,num):
    finv[num-1-i] = finv[num-i]*(num-i)%mod

dp[0] = frac[N]
for i in range(1,v+1):
    dp[i] = dp[i-1]*N*(N-1)%mod
def mCn(m,n):
    return frac[m]*frac[m-n]*frac[n]%mod
if M-N>=N:
    print(mCn(M-N,N)*frac[N]*mCn(M,N)*sum(dp[:v+1])%mod)
else:
    print(frac[M-N]*mCn(M,N)*sum(dp[:v+1])%mod)
