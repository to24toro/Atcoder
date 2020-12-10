a,b,c = map(int,input().split())
import math
l,r = 0,1000
eps = 0.000000000001
while r-l>eps:
    m = (l+r)/2
    y = a*m+b*math.sin(c*m*math.pi)
    if y >=100:
        r = m
    else:
        l = m
print(l)