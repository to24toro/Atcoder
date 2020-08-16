def gcd (a, b):
    while b != 0:
        a, b = b, a%b
    return a
 
def lcm(a, b,mod):
    return a*b//gcd(a,b)
 
N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
b = 1
for i in range(N):
    a = A[i]
    b = lcm(a,b,mod)
ans = 0
for a in A:
    ans += b//a
print(ans%mod)