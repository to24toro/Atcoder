from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

a,b,c,d = map(int,input().split())
n = int(input())
N = []
for _ in range(n):
    x,y = map(int,input().split())
    N.append((x,y))
N.append(N[0])
# print(N)
def linear(x1,y1,x2,y2,a,b,c,d):
    y1_l= (a - c) * (y1 - b) + (b - d) * (a - x1)
    y2_l= (a - c) * (y2 - b) + (b - d) * (a - x2)
    if y1_l*y2_l<0:
        return True
    else:
        return False
cnt = 0
for i in range(n):
    if linear(N[i][0],N[i][1],N[i+1][0],N[i+1][1],a,b,c,d) and linear(a,b,c,d,N[i][0],N[i][1],N[i+1][0],N[i+1][1]):
        cnt += 1
print(1+cnt//2)
