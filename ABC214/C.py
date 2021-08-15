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
S = list(map(int,input().split()))
T = list(map(int,input().split()))

s = sum(S)
idx = T.index(min(T))
for i in range(idx,n+idx):
    j = i%n
    T[(j+1)%n] = min(T[(j+1)%n],T[j]+S[j])
for t in T:
    print(t)