n,k = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
if n==1:
    if k==A[-1]:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
    exit()
if A[-1]<k:
    print('IMPOSSIBLE')
    exit()
from math import gcd
g = gcd(A[0],A[1])
for i in range(2,n):
    g = gcd(g,A[i])
if k%g:print('IMPOSSIBLE')
else:
    print('POSSIBLE')