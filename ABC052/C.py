N= int(input())
d = [0]*(N+1)
f = [0]*(N+1)
ans = 1
mod = 10**9+7
def spf(n,d):
    for i in range(2,n+1):
        if d[i]==0:
            j = i
            while j<n+1:
                d[j]=i
                j+=i
    return
spf(N,d)
def solve(n):#約数の個数
    helper = [0]*(n+1)
    while n!=1:
        helper[d[n]]+=1sts 
        n//=d[n]
    return
# print(d)
def factorization(n,f):
    tmp = n
    while n!=1:
        f[d[n]]+=1
        n//=d[n]

for n in range(1,N+1):
    factorization(n,f)

f[1]=0
for i in f:
    if i>0:
        ans *= (i+1)
        ans %=mod

print(ans%mod)