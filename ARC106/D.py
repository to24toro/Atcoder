n,k = map(int,input().split())
mod = 998244353
p = pow(2,mod-2,mod)
A = list(map(int,input().split()))
K = [n,sum(A)]
for i in range(2,k+1):
    for j in range(n):
        A[j]*=A[j]*pow(i,mod-2,mod)
        A[j]%=mod
    K.append(sum(A)%mod)
L = [1]

for i in range(1,k+1):
    L.append(L[-1]*i)
    L[-1]%=mod

print(L,K)
for i in range(1,k+1):
    ans = 0
    tmp = 0
    for j in range(i+1):
        tmp+=K[j]*K[i-j]
        tmp%=mod
    ans+=tmp
    ans*=L[i]
    ans-=tmp
    ans//=2
    ans%=mod
    print(ans)



    


