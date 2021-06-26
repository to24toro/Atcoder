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
A = list(map(int,input().split()))
dic = defaultdict(int)
for a in A:
    dic[a]+=1
s = n*(n-1)//2
for k,v in dic.items():
    if v>1:
        s-=v*(v-1)//2
print(s)