def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
PD = []
for a in A:
    L = prime_factorize(a)
    d = defaultdict(int)
    for l in L:
        d[l]+=1
    PD.append(d)
 
LCMD = defaultdict(int)
for pd in PD:
    for k,v in pd.items():
        LCMD[k] += max(0,v-LCMD[k])
 
lcm = 1
for k,v in LCMD.items():
    lcm *= k**v
ans = 0
MOD=10**9+7
for a in A:
    ans += lcm*pow(a,MOD-2,MOD)

print(int(ans%MOD))