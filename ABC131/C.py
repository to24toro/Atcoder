a,b,c,d = map(int,input().split())
from math import gcd
e  =c*d//gcd(c,d)
xa = a//c if a%c else a//c - 1
xb = b//c
ya = a//d if a%d else a//d - 1
yb = b//d
za = a//e if a%e else a//e - 1
zb = b//e
x = xb-xa
y  = yb-ya
z = zb-za
print(b-a+1-x-y+z)