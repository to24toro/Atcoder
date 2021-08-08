from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import numpy as np
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

import math
t=int(input())
l,x,y=map(int,input().split())
q=int(input())
for i in range(q):
    p=int(input())
    print(180*math.atan((l/2-l*math.cos(2*math.pi*p/t)/2)/(math.sqrt(x**2+(y+l*math.sin(2*math.pi*p/t)/2)**2)))/math.pi)