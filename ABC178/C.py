n = int(input())
mod = 10**9+7
a = pow(9,n,mod)
b = pow(8,n,mod)
c = pow(10,n,mod)
ans = c-2*a+b
print(ans%mod)