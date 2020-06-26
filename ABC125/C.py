N = int(input())
A = list(map(int,input().split()))
if N==2: print(max(A));exit()
from math import gcd
L = {}
R = {}
L[0] = A[0]
R[N-1] = A[-1]
ans = 0
for i in range(1,N):
    L[i] = gcd(L[i-1],A[i])
    R[N-i-1] = gcd(R[N-i],A[N-i-1])
for i in range(2,N):
    ans = max(ans,gcd(L[i-2],R[i]))
ans = max(ans,R[1])
ans = max(ans,L[N-2])
ans = max(ans,R[0])
print(ans)