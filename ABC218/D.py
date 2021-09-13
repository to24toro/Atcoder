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
dic = defaultdict(int)
L = [list(map(int,input().split())) for _ in range(n)]
for x,y in L:
    dic[(x,y)] = 1
cnt = 0
for i in range(n):
    a,b = L[i]
    for j in range(n):
        c,d = L[j]
        if a==c or b==d:
            continue
        if dic[(a,d)]==1 and dic[(c,b)]==1:
            # print(a,b,c,d)
            cnt += 1
print(cnt//4)