from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

h,w = map(int,input().split())
S = [input() for _ in range(h)]
dp = {}
def memo(i,j):
    if h<=i or w <=j:
        return True
    if S[i][j]=='#':
        return True
    if (i,j) in dp:
        return dp[(i,j)]
    res = False
    if memo(i+1,j)==False:
        res = True
    if memo(i,j+1)==False:
        res = True
    if memo(i+1,j+1)==False:
        res = True
    dp[(i,j)]=res
    return res

print('First' if memo(0,0) else 'Second')
