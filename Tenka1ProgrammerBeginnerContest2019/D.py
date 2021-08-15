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
k = None
for i in range(0,n+2):
    if i*(i-1)//2>n:
        break
    if i*(i-1)//2==n:
        k = i
if k==None:
    print('No')
else:
    print('Yes')
    print(k)
    z = [[] for i in range(k)]
    d = 1
    for i in range(k):
        for j in range(i+1,k):
            z[i].append(d)
            z[j].append(d)
            d+=1
    for i in z:
        print(len(i),*i)