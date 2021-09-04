from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
cnt = 0
n = int(input())
P = list(map(int,input().split()))
for i in range(1,n-1):
    p,q,r = P[i-1:i+2]
    if p<=q<=r or r<=q<=p:
        cnt +=1
print(cnt)