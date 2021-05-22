n = int(input())
A = list(map(int,input().split()))
frac = [1]*(n+1)
finv = [1]*(n+1)
mod = 10**9+7
for i in range(n):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+1):
    finv[n-i] = finv[n-i+1]*(n-i+1)%mod
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]*finv[n-r]*finv[r]%mod

B = []
A = [0]+A+[10**9]
flag = False
pre = 0
cnt = 0
for i in range(1,len(A)):
    if flag:
        if A[i]<0:
            cnt +=1
        else:
            B.append((A[i]-pre,cnt))
            cnt = 0
            pre = A[i]
            flag = False
    else:
        if A[i]<0:
            flag = True
            cnt += 1
        else:
            pre = A[i]
ans = 1
n = 2010
frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+1):
    finv[n-i] = finv[n-i+1]*(n-i+1)%mod
#yは2000以下であることを利用する
for x,y in B:
    a = 1
    for i in range(y):
        a*=x+y-i
        a%=mod
    ans *=a*finv[y]
    ans%=mod
print(ans)