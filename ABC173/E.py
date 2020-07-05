N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9+7
A.sort()
ans = 1
if A[-1]==0 and K&1: print(0);exit()
if A[-1]<0 and K&1:
    for i in range(N-1,N-1-K,-1):
        ans =(ans*A[i])%mod
    print(ans)
    exit()
l,r = 0,N-1
if K&1:
    ans *= A[-1]
    r-=1
    K-=1
p = K//2
for i in range(p):
    lp = A[l]*A[l+1]
    rp = A[r]*A[r-1]
    if lp>rp:
        ans = (ans*lp)%mod
        l += 2
    else:
        ans = (ans*rp)%mod
        r-=2
print(ans%mod)
