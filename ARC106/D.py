n,k = map(int,input().split())
mod = 998244353
p = pow(2,mod-2,mod)
A = list(map(int,input().split()))
s = [1]
t = [1]
for i in range(1,k+1):
    a = 0
    for j in range(1,n):
        a += pow(A[j],i,mod)
    s.append(a)
    t.append(t[-1]*A[0]%mod)
    print(s,t)
    ans = 0
    for j in range(len(s)):
        ans += s[j]*t[len(s)-1-i]
        ans %=mod
    print(ans*(n-1)%mod)


