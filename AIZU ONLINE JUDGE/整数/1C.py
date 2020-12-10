n = int(input())
A = list(map(int,input().split()))
import math
b = 1
def lcm (a,b):
    d = math.gcd(a,b)
    return a*b//d
for a in A:
    b = lcm(a,b)
print(b)