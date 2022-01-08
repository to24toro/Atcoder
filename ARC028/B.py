from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,k = map(int,input().split())
XX = list(map(int,input().split()))
X = []
for i,x in enumerate(XX):
    X.append([-x,i+1])
K = X[:k]
heapify(K)
print(K[0][1])
for i in range(k,n):
    heappush(K,X[i])
    heappop(K)
    print(K[0][1])


