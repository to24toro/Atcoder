n = int(input())
s = 1
u = 1
import math
for _ in range(n):
    t = int(input())
    s = math.gcd(u,t)
    u*=t
    u//=s
print(u)