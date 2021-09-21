r,x,y = map(int,input().split())
from math import sqrt
d = sqrt(x**2+y**2)
if d==0:
    print(0);exit()
if r>d:print(2);exit()
if d%r==0:
    print(int(d//r))
else:
    print(int(d//r)+1)