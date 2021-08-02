from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
q = int(input())
T = []
s = 0
A = []
dic = defaultdict(list)
d2 = defaultdict(int)
heapify(A)
a = 0
ANS = []
B = []
for i in range(q):
    query = list(map(int,input().split()))
    if query[0]==1:
        v = query[1]
        dic[v+s].append(i)
        heappush(A,v+s)
        a+=1
    elif query[0]==2:
        v = query[1]
        s-=v
        d2[i] = s
        B.append(i)
    else:
        res = heappop(A)
        b = dic[res].pop()
        ANS.append(res-s)

print(*ANS,sep = '\n')