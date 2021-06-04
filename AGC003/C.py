from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = [int(input()) for _ in range(n)]
dic = defaultdict(int)
for i,a in enumerate(sorted(A)):
    dic[a] = i+1
cnt = 0
for i,a in enumerate(A):
    if (i+1)%2!=dic[a]%2:
        cnt += 1
print(cnt//2)