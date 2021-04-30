from math import *
a,b = map(int,input().split())
if a>b:a,b = b,a
n = int(input())
for _ in range(n):
    c,d = map(int,input().split())
    if c>d:c,d=d,c
    l,r = atan(a/b),pi/4
    while r-l>1e-9:
        m = (l+r)/2
        if a*sin(m)+b*cos(m)<d:
            r = m
        else:
            l = m
    if a*cos(l)+b*sin(l)< c or a<c and b<d:
        print('YES')
    else:
        print('NO')