from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
cnt = 0
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
da = Counter(A)

for j in range(n):
    b = B[C[j]-1]
    cnt+=da[b]
print(cnt)