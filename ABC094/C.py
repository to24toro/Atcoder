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
X = list(map(int,input().split()))
D = []
for i,x in enumerate(X):
    D.append((x,i))
D.sort()
dic = {}
for i,(d,idx) in enumerate(D):
    dic[idx] = i
s,t = D[(n+1)//2]
for i in range(n):
    if i == t:
        print(D[(n+1)//2-1][0])
    elif dic[i]<(n+1)//2:
        print(s)
    else:
        print(D[(n+1)//2-1][0])

