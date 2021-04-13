n = int(input())
A = list(map(int,input().split()))
from math import gcd
L = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ans = float('inf')
for bit in range(1<<15):
    tmp = 1
    for i in range(15):
        if (bit>>i)&1:
            tmp*=L[i]
    for a in A:
        if gcd(a,tmp)==1:
            break
    else:
        ans = min(ans,tmp)
print(ans)
