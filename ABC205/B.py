from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = list(map(int,input().split()))
A.sort()
for i in range(1,n+1):
    if i!=A[i-1]:
        print('No');exit()
print('Yes')