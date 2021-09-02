from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
L = [list(map(str,input().split())) for _ in range(n)]
for i in range(n):
    s1,t1 = L[i]
    for j in range(i+1,n):
        s2,t2 = L[j]
        if s1==s2 and t1==t2:
            print('Yes');exit()
print('No')