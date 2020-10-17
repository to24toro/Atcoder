q = int(input())
mod = 1000003
frac = [1]*mod
for i in range(1,mod):
    frac[i] = i*frac[i-1]%mod
finv = [1]*mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(mod-1,0,-1):
    finv[i-1] = i*finv[i]%mod
for _ in range(q):
    x,d,n = map(int,input().split())
    if d==0:
        print(pow(x,n,mod))
        continue
    y = (x*pow(d,mod-2,mod)+n-1)%mod
    if y<n:
        ans = 0
    else:
        ans = frac[y]*finv[y-n]*pow(d,n,mod)%mod
    print(ans)

