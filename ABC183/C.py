from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,k = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
s = [i for i in range(1,n)]
for v in permutations(s):
    t = 0
    ss = list(v)
    t +=T[0][ss[0]]
    ss.append(0)
    for i in range(1,len(ss)):
        t += T[ss[i-1]][ss[i]]
    if t == k:
        cnt += 1
print(cnt)