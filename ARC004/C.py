from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
x,y = map(str,input().split('/'))
x = int(x)
y = int(y)
g = math.gcd(x,y)
x//=g
y//=g
f = False

if x<y:
    print('Impossible');exit()

for i in range(2):
    n = 2*x//y+i
    if n%y==0:
        m = n*(n+1)//2 -n//y*x
        if 1<=m<=n:
            print(n,m)
            f = True
if not f:
    print('Impossible')