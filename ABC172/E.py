n,m = map(int,input().split())
#包除定理で「少なくともk個値が一致する配列」を考える
#kこ選んでmPkで並べてここりのN-kをAとBに対してm-kPn-kで並べる
MOD = 10**9+7
size = 500001
frac = [1]*size
finv = [1]*size
for i in range(size-1):
    frac[i+1] = (frac[i]*(i+1))%MOD
finv[-1] = pow(frac[-1],MOD-2,MOD)
for i in range(size-2,-1,-1):
    finv[i] = (finv[i+1]*(i+1))%MOD
def comb(n,r):
    if n < r or r < 0:
    	return 0
    elif n == 0 or r == 0 or n == r:
        return 1
    else:
        return (frac[n]*finv[n-r]*finv[r])%MOD
def nPk(n,k):
    return frac[n]*finv[n-k]%MOD
ans = 0
for i in range(n+1):
    res = comb(n,i) * nPk(m,i) * (nPk(m-i,n-i)**2)
    res %=MOD
    if i%2: res*=-1
    ans += res
    ans %= MOD
# ans *= frac[m]*finv[m-n]
print(ans%MOD)