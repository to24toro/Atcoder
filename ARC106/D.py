n,k = map(int,input().split())
A = list(map(int,input().split()))
S  =[]
a = [i for i in A]
x=[1]*(k+1)
mod = 998244353
for i in range(k):
    x[i+1]=(x[i]*(i+1))%mod
C = [0]*(k+1)
S = [0]*(k+1)
C[0] = n
S[0]= n
for i in range(1,k+1):
    cnt = 0
    for j in range(n):
        cnt += A[j]
        A[j]*=a[j]
        A[j]%=mod
    cnt %=mod
    C[i]=cnt
    S[i]=(C[i]*pow(x[i],mod-2,mod))
for i in range(1,k+1):
    ans = 0
    for j in range(i+1):
        ans += S[j]*S[i-j]
        ans %= mod
    ans*=pow(2,mod-2,mod)*x[i]
    ans-=pow(2,i-1,mod)*C[i]
    print(ans%mod)
