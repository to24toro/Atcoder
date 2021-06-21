from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
r,g,b, = map(int,input().split())
def calc_cost(r,l,base):
    r0 = r - base
    l0 = l - base
    if r0*l0<0:
        return r0*(r0+1)//2 + l0*(l0-1)//2
    else:
        return abs(r0+l0)*(r0-l0+1)//2


ans = INF

for rr in range(-350,50):
    rl = rr-r+1
    rcost = calc_cost(rr,rl,-100)
    for bl in range(-49,351):
        if bl -rr -1 <g:continue
        br = bl+b-1
        bcost = calc_cost(br,bl,100)

        if rr+1>-(g//2):
            gl = rr+1
            gr = gl+g-1
        elif bl-1<g//2:
            gr = bl-1
            gl = gr-g+1
        else:
            gr = (g-1)//2
            gl = -(g//2)
        gcost = calc_cost(gr,gl,0)

        ans = min(ans,rcost+gcost+bcost)
print(ans)
