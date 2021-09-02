from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
R = [0]*(10**5+1)
dic = defaultdict(lambda:defaultdict(int))
n = int(input())
L = []
for _ in range(n):
    r,h = map(int,input().split())
    dic[r][h%3] += 1
    R[r]+=1
    L.append((r,h))
S = list(accumulate(R))
for r,h in L:
    w,l,d = 0,0,0
    w += S[r-1]
    l +=S[-1]-S[r]
    w += dic[r][(h+1)%3]
    l += dic[r][(h+2)%3]
    d += dic[r][h%3]-1
    print(w,l,d)
