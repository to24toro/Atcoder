n,m = map(int,input().split())
A = list(map(int,input().split()))
for i,a in enumerate(A):
    A[i] //=2
from math import gcd,ceil
def lcm(a, b):
    return a*b//gcd(a,b)
b = 1

div_two_cnt = None
for a in A:
    cnt = 0
    while a % 2 == 0:
        a //= 2
        cnt += 1
    if div_two_cnt is None:
        div_two_cnt = cnt
    elif cnt != div_two_cnt:
        print(0)
        exit()

for i in range(n):
    a = A[i]
    b = lcm(a,b)


print(ceil((m//b)/2))

