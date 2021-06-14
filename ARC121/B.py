from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = []
R,G,B = 0,0,0
r,g,b = [],[],[]
L = []
for _ in range(2*n):
    a,c = map(str,input().split())
    if c =="R":
        R += 1
        r.append(int(a))
    elif c=="B":
        B += 1
        b.append(int(a))

    else:
        G += 1
        g.append(int(a))
    L.append([int(a),c])

if R%2==0 and G%2==0 and B%2==0:
    print(0);exit()
L.sort()
rg,gb,br = float('inf'),float('inf'),float('inf')
# print(L)
for i in range(1,2*n):
    diff = abs(L[i][0]-L[i-1][0])
    # print(L[i][1],L[i-1][1],diff)
    if L[i][1]!=L[i-1][1]:
        set_ = set([L[i][1],L[i-1][1]])
        if 'R' not in set_:
            gb = min(gb,diff)
        elif 'G' not in set_:
            br = min(br,diff)
        else:
            rg = min(rg,diff)
if R%2==0:
    print(min(gb,rg+br))
elif B%2==0:
    print(min(rg,br+gb))
else:
    print(min(br,rg+gb))