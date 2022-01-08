n = int(input())
A = list(map(int,input().split()))
import math
L = [0]*(n-1)
L[0] = A[0]
for i in range(1,n-1):
    L[i] = math.gcd(L[i-1],A[i-1])
R = [0]*(n-1)
R[-1] = A[-1]
for i in reversed(range(n-1,1)):
    R[i-1] = math.gcd(R[i],A[i])
ans = 1
for a in A[1:]:
    
for i in range(n):
    a = A[i]
