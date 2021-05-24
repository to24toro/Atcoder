from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
AA = list(map(int,input().split()))
BB = list(map(int,input().split()))

A = [a + i for i,a in enumerate(AA)]
B = [b + i for i,b in enumerate(BB)]

if set(A)!=set(B):
    print(-1);exit()

C = []