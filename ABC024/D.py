mod = 10**9+7
def inv(n):
    return pow(n, mod - 2, mod)
 
A = int(input())
B = int(input())
C = int(input())

s = inv((A * (inv(B) + inv(C)) - 1) % mod)
r = (A * inv(C) % mod * s - 1) % mod
c = (s - r - 1) % mod
print(r, c)