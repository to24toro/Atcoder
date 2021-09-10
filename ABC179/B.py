from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
cnt = 0
D = []
for _ in range(n):
    a,b = map(int,input().split())
    D.append((a,b))
for a,b in D:
    if a==b:
        cnt += 1
        if cnt == 3:
            print('Yes');exit()
    else:
        cnt = 0
print('No')
            
