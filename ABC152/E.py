import math
n = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
if n==1:print(1);exit()
g = A[0]
s = A[0]
for a in A[1:]:
    g = math.gcd(s,a)
    s*=a*pow(g,mod-2,mod)
    # print(s,g)
    s%=mod
ans = 0
# print(s)
coef = sum(pow(x, mod-2, mod) for x in A)
ans = s * coef % mod
print(ans)
