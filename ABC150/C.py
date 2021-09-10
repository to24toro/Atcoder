from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n = int(input())
P = list(map(lambda x:int(x)-1,input().split()))
Q = list(map(lambda x:int(x)-1,input().split()))
L = []
for l in permutations(range(n),n):
    L.append(list(l))
for i,l in enumerate(L):
    if l==P:
        a = i
    if l == Q:
        b = i
print(abs(a-b))