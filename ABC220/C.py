
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
A = list(map(int,input().split()))
x = int(input())
s = sum(A)
shou = x//s

x-=x//s*s

res = 0
for i in range(n):
    res += A[i]
    if res>x:
        print(shou*n+i+1);exit()
